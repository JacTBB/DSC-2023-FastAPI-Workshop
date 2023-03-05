import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import *
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)