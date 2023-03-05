import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import *
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
from Note import Note
import shelve

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/notes', response_class=HTMLResponse)
async def notes(request: Request):
    notes = {}
    db = shelve.open('notes.db', 'r')

    try:
        notes = db['Notes']
    except:
        print("Error in retrieving Notes from notes.db.")

    db.close()
    
    return templates.TemplateResponse('notes.html', {'request': request, 'notes': notes})


@app.get('/createnote', response_class=HTMLResponse)
async def createnote(request: Request):
    return templates.TemplateResponse('createnote.html', {'request': request})

@app.post('/createnote')
async def createnoteform(title: str = Form(), note: str = Form()):
    notes = {}
    notesID = 0
    db = shelve.open('notes.db', 'c')

    try:
        notes = db['Notes']
        notesID = db['NotesID']
    except:
        print("Error in retrieving Notes from notes.db.")

    NewNote = Note(title, note)

    notesID = notesID + 1
    notes[notesID] = NewNote
    db['Notes'] = notes
    db['NotesID'] = notesID

    db.close()
    
    return RedirectResponse(url="/notes", status_code=HTTP_302_FOUND)

@app.post('/deletenote/{id}')
async def deletenote(id: int):
    notes = {}
    db = shelve.open('notes.db', 'c')

    try:
        notes = db['Notes']
    except:
        print("Error in retrieving Notes from notes.db.")

    print(id)
    notes.pop(id)
    db['Notes'] = notes

    db.close()
    
    return RedirectResponse(url="/notes", status_code=HTTP_302_FOUND)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)