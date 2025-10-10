import pathlib
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# APIRouter 객체 생성
router = APIRouter()

# Jinja2 템플릿 설정 (templates 폴더를 가리킴)
templates = Jinja2Templates(directory="templates")

# GET 방식으로 루트 경로("/")에 접속했을 때 이 함수를 실행
@router.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    # home.html 파일을 렌더링하여 반환
    return templates.TemplateResponse("home.html", {"request": request})