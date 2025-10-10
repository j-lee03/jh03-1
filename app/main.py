import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
# FastAPI 앱 생성
app = FastAPI()

# --- 중요: 정적 파일 경로 수정 ---
# '/static' URL 경로로 'static' 디렉토리를 연결합니다.
app.mount("/static", StaticFiles(directory="static"), name="static")
# --------------------------------

# HTML 템플릿을 사용하기 위한 설정
templates = Jinja2Templates(directory="templates")

# projects.json 파일에서 프로젝트 데이터 불러오기
BASE_DIR = Path(__file__).resolve().parent
with open(BASE_DIR / 'projects.json', 'r', encoding='utf-8') as f:
    projects_data = json.load(f)

# 루트 URL ("/") 접속 시 home.html 템플릿을 렌더링
@app.get("/")
def home(request: Request):
    # projects.json 데이터 중에서 main 값이 true인 것만 필터링
    main_projects = [p for p in projects_data if p.get('main')]
    # home.html에 request와 프로젝트 데이터를 전달
    return templates.TemplateResponse("home.html", {"request": request, "projects": main_projects})

# (추가) 다른 페이지 라우트 예시
@app.get("/projects")
def projects_page(request: Request):
    # 모든 프로젝트 데이터를 projects.html에 전달
    return templates.TemplateResponse("projects.html", {"request": request, "projects": projects_data})

# 기존에 사용하시던 라우터 포함 코드는 일단 주석 처리합니다.
# from app.routers import about, contact, home, projects
# app.include_router(home.router)
# app.include_router(projects.router)
# app.include_router(about.router)
# app.include_router(contact.router)