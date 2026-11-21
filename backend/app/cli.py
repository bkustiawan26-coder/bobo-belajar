import argparse
import getpass
import json
import sys

from sqlalchemy import select

from app.core.config import get_settings
from app.core.db import session_factory
from app.core.security import hash_secret
from app.models import User, UserRole
from app.seed.seed import run


def main() -> None:
    p = argparse.ArgumentParser(prog="python -m app.cli")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("seed")
    s.add_argument("--sample", action="store_true")
    s.add_argument("--publish-sample", action="store_true")
    a = sub.add_parser("create-staff")
    a.add_argument("--email", required=True)
    a.add_argument("--name", required=True)
    a.add_argument("--role", choices=["admin", "editor", "reviewer"], default="admin")
    args = p.parse_args()
    db = session_factory()()
    try:
        if args.cmd == "seed":
            if args.publish_sample and get_settings().env == "production":
                print("Konten contoh tidak boleh langsung terbit di production. Jalankan tanpa --publish-sample lalu tinjau lewat CMS.", file=sys.stderr)
                sys.exit(2)
            print(json.dumps(run(db, args.sample, args.publish_sample)))
        elif args.cmd == "create-staff":
            pw = getpass.getpass("Kata sandi (min 12 karakter): ")
            if len(pw) < 12:
                print("Kata sandi terlalu pendek", file=sys.stderr)
                sys.exit(2)
            u = db.scalar(select(User).where(User.email == args.email.lower()))
            if u is None:
                u = User(email=args.email.lower(), display_name=args.name, password_hash=hash_secret(pw))
                db.add(u)
                db.flush()
            if args.role not in [r.role for r in u.roles]:
                u.roles.append(UserRole(role=args.role))
            db.commit()
            print(json.dumps({"user_id": str(u.id), "roles": [r.role for r in u.roles]}))
    finally:
        db.close()


if __name__ == "__main__":
    main()
