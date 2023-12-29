from subprocess import check_output
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import jc
from pydantic import BaseModel
from starlette import status
import uvicorn

app = FastAPI()


class Params(BaseModel):
    count: int = 1


@app.post("/getping/{ip}")
async def getping(ip: str, params: Params):
    out = check_output(["ping", "-c", str(params.count), ip]).decode().strip()
    return JSONResponse(jc.parse("ping", out), status_code=status.HTTP_200_OK)


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("get_ping.main:app", host="0.0.0.0", port=8000, reload=True)
