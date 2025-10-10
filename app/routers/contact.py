import json
import pathlib
import smtplib
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()

# 현재 파일 위치를 기준으로 프로젝트 루트 경로(BASE_DIR)를 계산
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 프로젝트 루트 아래에 있는 'templates' 폴더를 절대 경로로 지정
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))