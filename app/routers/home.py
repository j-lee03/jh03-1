import json
import pathlib

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()

# 현재 파일 위치를 기준으로 프로젝트 루트 경로(BASE_DIR)를 계산합니다.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 프로젝트 루트 아래에 있는 'templates' 폴더를 절대 경로로 지정합니다.
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))


@router.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    # 이제 서버는 templates 폴더 안의 home.html 파일을 정확히 찾을 수 있습니다.
    return templates.TemplateResponse("home.html", {"request": request})