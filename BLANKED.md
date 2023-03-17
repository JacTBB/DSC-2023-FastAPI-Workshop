# NYP Developer Student Club 2023 Fast API Workshop

Description:

This workshop will teach you the basics of Fast API, a web framework used to develop APIs in Python.
We will also cover Jinja Templating and Shelve Database, and use what we have learnt to built a basic website to store notes.

## Contents
- [Practical 1](#practical-1-setup-and-basic-code)
- [Practical 2](#practical-2-jinja-templating)
- [Practical 3](#practical-3-shelve-database-creating-notes)
- [Practical 4](#practical-4-shelve-database-viewing-notes)
- [Practical 5](#practical-5-shelve-database-deleting-notes)

# Practical 1: Setup And Basic Code

https://fastapi.tiangolo.com/tutorial/

pip install fastapi

pip install "uvicorn[standard]"

## main.py
```py
import uvicorn
from fastapi import FastAPI
from fastapi.responses import *

# Initialise The App

# Return a Message

# Return HTML Code

# Return a HTML File (test.html)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
```
## test.html
```py
<html>
    <head>
        <title>Some HTML in here</title>
    </head>
    <body>
        <h1>Oh look, a HTML File!</h1>
    </body>
</html>
```

Run on http://127.0.0.1:8000/

___

# Practical 2: Jinja Templating

https://jinja.palletsprojects.com/en/3.1.x/
https://jinja.palletsprojects.com/en/3.1.x/templates/

pip install jinja2

## **Delimiters:**

`{% ... %}` for **Statements**

`{{ ... }}` for **Expressions** to print to the template output

`{# ... #}` for **Comments** not included in the template output

## **Inheritance:**

`{% block <name> %} {% endblock %}`

`{% extends "base.html" %}`

## **Control Structures:**

`{% for user in users %} {% endfor %}`

`{% for key, value in my_dict.items() %} {% endfor %}`

## main.py
```py
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import *
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Declare the Jinja templates

# Return home.html

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
```
## navbar.html
```html
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="/"> My Notes </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="collapsibleNavbar">
        <ul class="navbar-nav">

            <li class="nav-item">
            <a class="nav-link" href="/">Home</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="notes">View Notes</a>
                </li>
            
            <li class="nav-item">
            <a class="nav-link" href="createnote">Create Notes</a>
            </li>
            
        </ul>
        </div>
    </div>
</nav>
```
## base.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    # Title Block

    <!-- Bootstrap 5.1.2 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>

    # Include the navbar



    <div class="container-fluid">
        # Content Block
    </div>

    # Scripts Block Include the Bootstrap scripts below

    <!-- Popper 2.10.2, Bootstrap 5.1.2 JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</html>
```
## home.html
```html
# Extends
# Title

# This is the content
<h1 class="display-4">Notes Homepage</h1>
<p> Let's note some notes! </p>
```
```
File Structure
Root:
    - main.py
    - templates
        - includes
            - navbar.html
        - base.html
        - home.html
```

___

# Practical 3: Shelve Database Creating Notes

https://docs.python.org/3/library/shelve.html

pip install shelve
pip install starlette

## main.py
```py
import uvicorn
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import *
from fastapi.templating import Jinja2Templates
from Note import Note
import shelve

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})

# HTTP GET Create Note Endpoint

# HTTP POST Create Note Endpoint
    # Open the database
        try:
            notes = database['Notes'] or {}
            notesID = database['NotesID'] or 0
            
            # Use the NoteClass to make a new note

            # Increment NoteID and make a new note
            # Update the database with the updated notes dictionary
            
            return RedirectResponse(url="/notes", status_code=302)
        except KeyError:
            raise HTTPException(status_code=404, detail="Item not found")

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
```
## Note.py
```py
class Note:
    def __init__(self, title, note):
        self.title = title
        self.note = note
```
## createnote.html
```html
{% extends "base.html" %}
{% block title %} New Note {% endblock %}

{% block content %}
<h1 class="display-4">Create A New Note</h1>

<form method="POST">
  Title:
  <input type="text" name="title">

  <br>

  Note:
  <textarea name="note"></textarea>

  <br>

  <input type="submit" value="Submit" class="btn btn-primary"/>
</form>
{% endblock %}
```

___

# Practical 4: Shelve Database Viewing Notes

## main.py
```py
import uvicorn
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import *
from fastapi.templating import Jinja2Templates
from Note import Note
import shelve

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/notes', response_class=HTMLResponse)
async def notes(request: Request):
    # Open the database
        try:
            # Get the notes and return the note jinja template
        except KeyError:
            raise HTTPException(status_code=404, detail="Item not found")

@app.get('/createnote', response_class=HTMLResponse)
async def createnote(request: Request):
    return templates.TemplateResponse('createnote.html', {'request': request})

@app.post('/createnote')
async def createnoteform(title: str = Form(), note: str = Form()):
    with shelve.open('notes.db', writeback=True) as database:
        try:
            notes = database['Notes'] or {}
            notesID = database['NotesID'] or 0
            
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
```
## notes.html
```html
{% extends "base.html" %}
{% block title %} My Notes {% endblock %}

{% block content %}
<h1>Notes</h1>

# Jinja For Loop
    <div style="border: solid 1px grey;">
        <h3>Note: {{uid}} | {{ notes[uid].title }}</h3>
        <p>{{ notes[uid].note }}</p>
    </div>

{% endblock %}
```

___

# Practical 5: Shelve Database Deleting Notes

## main.py
```py
import uvicorn
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import *
from fastapi.templating import Jinja2Templates
from Note import Note
import shelve

app = FastAPI()

templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})

@app.get('/notes', response_class=HTMLResponse)
async def notes(request: Request):
    with shelve.open('notes.db', flag='c') as database:
        try:
            notes = database['Notes']
            return templates.TemplateResponse('notes.html', {'request': request, 'notes': notes})
        except KeyError:
            raise HTTPException(status_code=404, detail="Item not found")

@app.get('/createnote', response_class=HTMLResponse)
async def createnote(request: Request):
    return templates.TemplateResponse('createnote.html', {'request': request})

@app.post('/createnote')
async def createnoteform(title: str = Form(), note: str = Form()):
    with shelve.open('notes.db', writeback=True) as database:
        try:
            notes = database['Notes'] or {}
            notesID = database['NotesID'] or 0
            
            NewNote = Note(title, note)

            notesID += 1
            notes[notesID] = NewNote
            database['Notes'] = notes
            database['NotesID'] = notesID
            
            return RedirectResponse(url="/notes", status_code=302)
        except KeyError:
            raise HTTPException(status_code=404, detail="Item not found")

# Delete Note Endpoint with parameter ID
    with shelve.open('notes.db', writeback=True) as database:
        try:
            notes = database['Notes']
            # Remove the note from the dictionary using the ID
            database['Notes'] = notes
            return RedirectResponse(url="/notes", status_code=302)
        except KeyError:
            raise HTTPException(status_code=404, detail="Item not found")

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
```
## notes.html
```html
{% extends "base.html" %}
{% block title %} My Notes {% endblock %}

{% block content %}
<h1>Notes</h1>

{% for uid in notes %}
    <div style="border: solid 1px grey;">
        <h3>Note: {{uid}} | {{ notes[uid].title }}</h3>
        <p>{{ notes[uid].note }}</p>
        <form method="POST" action="/deletenote/{{uid}}">
            <input type="submit" value="Delete" class="btn btn-danger"/>
        </form>
    </div>
{% endfor %}

{% endblock %}
```