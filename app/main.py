import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

with open(BASE_DIR / 'projects.json', 'r', encoding='utf-8') as f:
    projects_data = json.load(f)

@app.get("/")
def home(request: Request):
    main_projects = [p for p in projects_data if p.get('main')]
    return templates.TemplateResponse("home.html", {"request": request, "projects": main_projects})

@app.get("/projects")
def projects_page(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request, "projects": projects_data})

# --- 이 부분을 추가하면 됩니다 ---
@app.get("/about")
def about_page(request: Request):
    # app/templates/about.html 파일을 보여줍니다.
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact")
def contact_page(request: Request):
    # app/templates/contact.html 파일을 보여줍니다.
    return templates.TemplateResponse("contact.html", {"request": request})
# --------------------------------

# 기존에 사용하시던 라우터 포함 코드는 일단 주석 처리합니다.
# from app.routers import about, contact, home, projects
# app.include_router(home.router)
# app.include_router(projects.router)
# app.include_router(about.router)
# app.include_router(contact.router)