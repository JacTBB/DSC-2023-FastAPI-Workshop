# NYP Developer Student Club 2023 Fast API Workshop

Description:

This workshop will teach you the basics of Fast API, a web framework used to develop APIs in Python.
We will also cover Jinja Templating and Shelve Database, and use what we have learnt to built a basic website to store notes.

## Contents
- [Practical 1](#practical-1-setup-and-basic-code)
- [Practical 2](#practical-2-jinja-templating)
- [Practical 3](#practical-3-shelve-database)

# Practical 1: Setup And Basic Code

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

___

# Practical 3: Shelve Database

https://docs.python.org/3/library/shelve.html

pip install shelve
pip install starlette

TODO: