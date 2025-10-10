import pathlib
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import home, projects
# 만약 라우터 파일이 있다면 주석 해제

app = FastAPI()

# static 폴더를 FastAPI 앱에 연결하는 올바른 코드
app.mount("/static", StaticFiles(directory="static"), name="static")

# 라우터들을 앱에 포함시키는 코드
# app.include_router(home.router)
# app.include_router(projects.router)

# 참고: templates 폴더 렌더링은 각 라우터 파일 안에서 처리해야 합니다.