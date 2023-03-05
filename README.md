# NYP Developer Student Club 2023 Fast API Workshop
## Contents
[Practical 1](#practical-1-setup-and-basic-code)
[Practical 2](#practical-2-jinja-templating)
[Practical 3](#practical-3-shelve-database)

# Practical 1: Setup And Basic Code

<details>
https://fastapi.tiangolo.com/tutorial/

pip install fastapi

pip install "uvicorn[standard]"

```py
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
    uvicorn.run(app, host='127.0.0.1', port=8000)
```

Run on http://127.0.0.1:8000/

Note: Response Classes
</details>

___

# Practical 2: Jinja Templating
<details>

https://jinja.palletsprojects.com/en/3.1.x/
https://jinja.palletsprojects.com/en/3.1.x/templates/

pip install jinja2

`{% ... %}` for **Statements**

`{{ ... }}` for **Expressions** to print to the template output

`{# ... #}` for **Comments** not included in the template output

***Further elaborate on Jinja Tags & Blocks & Inheritance**

## main.py
```py
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
                <a class="nav-link" href="/notes">View Notes</a>
                </li>
            
            <li class="nav-item">
            <a class="nav-link" href="/createnote">Create Notes</a>
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
    <title>{% block title %}{% endblock %}</title>

    <!-- Bootstrap 5.1.2 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>

    {% block navbar %}
            {% include 'includes/navbar.html' %}
    {% endblock %}



    <div class="container-fluid">
        {% block content %}
        {% endblock %}
    </div>

    {% block scripts %}

    <!-- Popper 2.10.2, Bootstrap 5.1.2 JavaScript -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>

    {% endblock %}

</body>
</html>
```
## home.html
```html
{% extends "base.html" %}
{% block title %} My Notes {% endblock %}

{% block content %}
<h1 class="display-4">Notes Homepage</h1>
<p> Let's note some notes! </p>
{% endblock %}
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
</details>

___

# Practical 3: Shelve Database

<details>
https://docs.python.org/3/library/shelve.html

pip install shelve

## main.py
```py
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
```
## Notes.py
```py
class Note:
    def __init__(self, title, note):
        self.title = title
        self.note = note
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
</details>