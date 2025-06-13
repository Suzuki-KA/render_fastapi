from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

from fastapi.responses import HTMLResponse #インポート

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>TODO List</title>
        </head>
        <body>
            <h1>・就活</h1>
            <h2>・就活</h2>
            <h3>・就活</h3>
            <h3>・就活就活就活</h3>
            <h3>・就活就活就活就活就活就活就活</h3>
            <h3>・就活就就活就活就活就活就活就活活就活就活就活就活就活</h3>
            <h3>・就活就活就活就活就活就活就活就活就活就活就活就活就活就活就活就活就活就活就活就活就活就活就活就活就活</h3>
            <h1></h1>
            <h3>月4課題</h3>
            <h3>火2課題</h3>
            <h3>火3,4課題</h3>
            <h1></h1>
            <h3>申請書作成</h3>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)