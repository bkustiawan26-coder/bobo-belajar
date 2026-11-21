import hashlib
import struct
import sys

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import pkcs12

APK_SIG_BLOCK_MAGIC = b"APK Sig Block 42"
V2_ID = 0x7109871A
SIG_RSA_PKCS1_SHA256 = 0x0103
CHUNK = 1024 * 1024


def find_eocd(data):
    for i in range(len(data) - 22, max(-1, len(data) - 22 - 65536) - 1, -1):
        if data[i:i + 4] == b"PK\x05\x06":
            clen = struct.unpack("<H", data[i + 20:i + 22])[0]
            if i + 22 + clen == len(data):
                return i
    raise SystemExit("EOCD tidak ditemukan")


def strip_existing_block(data, cd_off):
    if cd_off >= 24 and data[cd_off - 16:cd_off] == APK_SIG_BLOCK_MAGIC:
        size = struct.unpack("<Q", data[cd_off - 24:cd_off - 16])[0]
        return cd_off - (size + 8)
    return cd_off


def lp(b):
    return struct.pack("<I", len(b)) + b


def chunk_digest(sections):
    digests = []
    for sec in sections:
        for off in range(0, len(sec), CHUNK):
            c = sec[off:off + CHUNK]
            digests.append(hashlib.sha256(b"\xa5" + struct.pack("<I", len(c)) + c).digest())
    top = hashlib.sha256(b"\x5a" + struct.pack("<I", len(digests)) + b"".join(digests)).digest()
    return top


def main(apk_in, apk_out, ks_path, ks_pass):
    data = open(apk_in, "rb").read()
    eocd = find_eocd(data)
    cd_off = struct.unpack("<I", data[eocd + 16:eocd + 20])[0]
    cd_size = struct.unpack("<I", data[eocd + 12:eocd + 16])[0]
    entries_end = strip_existing_block(data, cd_off)
    entries = data[:entries_end]
    cd = data[cd_off:cd_off + cd_size]
    eocd_bytes = bytearray(data[eocd:])
    eocd_for_digest = bytearray(eocd_bytes)
    struct.pack_into("<I", eocd_for_digest, 16, entries_end)
    digest = chunk_digest([entries, cd, bytes(eocd_for_digest)])

    key, cert, _ = pkcs12.load_key_and_certificates(open(ks_path, "rb").read(), ks_pass.encode())
    cert_der = cert.public_bytes(serialization.Encoding.DER)
    pub_der = key.public_key().public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)

    digests_seq = lp(lp(struct.pack("<I", SIG_RSA_PKCS1_SHA256) + lp(digest)))
    certs_seq = lp(lp(cert_der))
    attrs_seq = lp(b"")
    signed_data = digests_seq + certs_seq + attrs_seq
    sig = key.sign(signed_data, padding.PKCS1v15(), hashes.SHA256())
    sigs_seq = lp(lp(struct.pack("<I", SIG_RSA_PKCS1_SHA256) + lp(sig)))
    signer = lp(signed_data) + sigs_seq + lp(pub_der)
    v2_value = lp(lp(signer))

    pair = struct.pack("<I", V2_ID) + v2_value
    pairs = struct.pack("<Q", len(pair)) + pair
    block_size = len(pairs) + 8 + 16
    block = struct.pack("<Q", block_size) + pairs + struct.pack("<Q", block_size) + APK_SIG_BLOCK_MAGIC

    struct.pack_into("<I", eocd_bytes, 16, entries_end + len(block))
    with open(apk_out, "wb") as f:
        f.write(entries + block + cd + bytes(eocd_bytes))
    print(f"ditandatangani: {apk_out}")


if __name__ == "__main__":
    main(*sys.argv[1:5])
