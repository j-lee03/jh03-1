import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path  # 1. pathlib 임포트

# FastAPI 앱 생성
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# --- 2. 파일을 여는 방식을 이 코드로 수정 ---
# 현재 main.py 파일의 위치를 기준으로 projects.json 경로를 절대 경로로 설정합니다.
BASE_DIR = Path(__file__).resolve().parent
with open(BASE_DIR / 'projects.json', 'r', encoding='utf-8') as f:
    projects_data = json.load(f)
# ------------------------------------

@app.get("/")
def home(request: Request):
    main_projects = [p for p in projects_data if p.get('main')]
    return templates.TemplateResponse("home.html", {"request": request, "projects": main_projects})

@app.get("/projects")
def projects_page(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request, "projects": projects_data})

# (이하 기존 코드)

# 기존에 사용하시던 라우터 포함 코드는 일단 주석 처리합니다.
# from app.routers import about, contact, home, projects
# app.include_router(home.router)
# app.include_router(projects.router)
# app.include_router(about.router)
# app.include_router(contact.router)