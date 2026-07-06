import logging
import time
from uuid import uuid4

from fastapi import Request, Response

from app.core.logging import request_id_context


logger = logging.getLogger("app.request")


async def request_context_middleware(
    request: Request,
    call_next,
) -> Response:
    incoming_request_id = request.headers.get("X-Request-ID", "")
    request_id = (
        incoming_request_id if 0 < len(incoming_request_id) <= 128 else uuid4().hex
    )
    token = request_id_context.set(request_id)
    request.state.request_id = request_id
    start_time = time.perf_counter()

    try:
        response = await call_next(request)
    except Exception:
        duration_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2,
        )
        logger.exception(
            "Unhandled request error",
            extra={
                "method": request.method,
                "path": request.url.path,
                "duration_ms": duration_ms,
            },
        )
        raise
    else:
        duration_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2,
        )
        response.headers["X-Request-ID"] = request_id
        logger.info(
            "Request completed",
            extra={
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration_ms": duration_ms,
            },
        )
        return response
    finally:
        request_id_context.reset(token)
