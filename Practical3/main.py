import uvicorn
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import *
from fastapi.templating import Jinja2Templates
from note import Note
import shelve

with shelve.open('notes.db', writeback=True) as database:
    if 'Notes' not in database:
        database['Notes'] = {}
        database['NotesID'] = 0 

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/createnote')
async def createnote(request: Request):
    return templates.TemplateResponse('createnote.html', {'request': request})

@app.post('/createnote')
async def createnoteform(title: str = Form(), note: str = Form()):
    with shelve.open('notes.db', writeback=True) as database:
        try:
            notes = database['Notes']
            notesID = database['NotesID']
            
            NewNote = Note(title, note)

            notesID += 1
            notes[notesID] = NewNote
            database['Notes'] = notes
            database['NotesID'] = notesID
            
            return RedirectResponse(url="/notes", status_code=302)
        except KeyError:
            raise HTTPException(status_code=404, detail="Item not found")

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)