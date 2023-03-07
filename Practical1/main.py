import uvicorn
from fastapi import FastAPI
from fastapi.responses import *

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/html', response_class=HTMLResponse)
async def returnHTML():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

@app.get('/htmlfile', response_class=FileResponse)
async def returnHTMLFile():
    return 'test.html'

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)