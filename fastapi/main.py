"""
http://127.0.0.1:8000/save_score?id=1&score=2.5
uvicorn test:app --reload
"""
from fastapi import FastAPI, Form
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from operate_table import OperateTable
app = FastAPI()

host = "127.0.0.1"
user = "root"
password = "root"
database = "qa"
table_name = "scores"
operate_table = OperateTable(host,user,password,database,table_name)

@app.post("/save_score/")
async def save_score(request: Request, id: int = Form(...), score: float = Form(...)):
    operate_table.insert(id,score)

@app.post("/best_score/")
async def best_score(request: Request):
    return operate_table.getHighScoreData(10)


templates = Jinja2Templates(directory="templates")

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('score_record.html', {'request': request})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)

