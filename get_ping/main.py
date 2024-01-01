import json
from subprocess import check_output, Popen, PIPE
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette import status
import uvicorn

app = FastAPI()


class Params(BaseModel):
    count: int = 1


@app.post("/getping/{ip}")
async def getping(ip: str, params: Params):
    ping_output = Popen(["ping", "-c", str(params.count), ip], stdout=PIPE)
    jc_output = check_output(["jc", "--ping"], stdin=ping_output.stdout)
    ping_output.wait()
    out = json.loads(jc_output.decode())
    print(out)
    return JSONResponse(out, status_code=status.HTTP_200_OK)


def start():
    uvicorn.run("get_ping.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()
