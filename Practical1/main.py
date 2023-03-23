import uvicorn
from fastapi import FastAPI
from fastapi.responses import *

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/html')
async def returnHTML():
    return HTMLResponse("""
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>HTML!</h1>
        </body>
    </html>
    """)

@app.get('/htmlfile')
async def returnHTMLFile():
    return FileResponse('test.html')

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)