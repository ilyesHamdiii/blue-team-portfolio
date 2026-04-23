from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from database.db import (
    get_timeline,get_connection,get_top_commands,get_top_ips,search_events
)
app=FastAPI()
templates=Jinja2Templates(directory="templates")
@app.get("/",response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {
        "request": request
    })
@app.get("/api/timeline")
def timeline():
    return get_timeline()
@app.get("/api/commands")
def commands():
    return get_top_commands()
@app.get("/api/top-ips")
def top_ips():
    return get_top_ips()
@app.get("/api/search")
def search(q:str=""):
    return search_events()