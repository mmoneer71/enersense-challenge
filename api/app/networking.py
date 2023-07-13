from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app import __version__
from app.db import close_db_connect, connect_and_init_db
from app.error import BadRequest, UnprocessableError
from app.health import health_router
from app.router import api_router
from utils.logger import get_logger

app = FastAPI(
    version=__version__,
    title="Get EV data",
    description="Application API for the Enersense challenge, retreives mqtt records from db",
)
app.add_event_handler("startup", connect_and_init_db)
app.add_event_handler("shutdown", close_db_connect)
logger = get_logger("api_root")


# HTTP error responses
@app.exception_handler(BadRequest)
async def bad_request_handler(req: Request, exc: BadRequest) -> JSONResponse:
    return exc.gen_err_resp()


@app.exception_handler(RequestValidationError)
async def invalid_req_handler(
    req: Request, exc: RequestValidationError
) -> JSONResponse:
    logger.error(f"Request invalid. {str(exc)}")
    return JSONResponse(
        status_code=400,
        content={
            "type": "about:blank",
            "title": "Bad Request",
            "status": 400,
            "detail": [str(exc)],
        },
    )


@app.exception_handler(UnprocessableError)
async def unprocessable_error_handler(
    req: Request, exc: UnprocessableError
) -> JSONResponse:
    return exc.gen_err_resp()


# API Path
app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(api_router, prefix="/readings", tags=["readings"])
