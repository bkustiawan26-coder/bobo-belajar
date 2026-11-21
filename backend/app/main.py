import logging
import time
import uuid

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import text

from app.api import admin, auth, parent, student
from app.core.config import get_settings
from app.core.db import session_factory
from app.privacy import privacy_html

log = logging.getLogger("bobo")


def create_app() -> FastAPI:
    s = get_settings()
    app = FastAPI(title="BOBO BELAJAR API", version="0.1.0", docs_url="/docs" if s.env != "production" else None, redoc_url=None)
    app.add_middleware(CORSMiddleware, allow_origins=s.cors_list, allow_credentials=False, allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"], allow_headers=["Authorization", "Content-Type"])

    @app.middleware("http")
    async def request_log(request: Request, call_next):
        rid = uuid.uuid4().hex[:12]
        t0 = time.monotonic()
        try:
            response = await call_next(request)
        except Exception:
            log.exception("unhandled rid=%s path=%s", rid, request.url.path)
            return JSONResponse({"detail": "Terjadi kesalahan di server", "request_id": rid}, status_code=500)
        response.headers["X-Request-ID"] = rid
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "no-referrer"
        log.info('{"rid":"%s","method":"%s","path":"%s","status":%d,"ms":%d}', rid, request.method, request.url.path, response.status_code, int((time.monotonic() - t0) * 1000))
        return response

    @app.get("/health")
    def health():
        db = session_factory()()
        try:
            db.execute(text("select 1"))
            return {"status": "ok"}
        finally:
            db.close()

    @app.get("/privacy", response_class=HTMLResponse)
    def privacy():
        return privacy_html()

    for r in (auth.router, student.router, parent.router, admin.router):
        app.include_router(r, prefix="/v1")
    return app


logging.basicConfig(level=logging.INFO, format="%(message)s")
app = create_app()
