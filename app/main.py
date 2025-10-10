from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import home, about, contact, projects

app = FastAPI()

# Static files (정적 파일) 연결
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routers (각 페이지) 연결
app.include_router(home.router)
app.include_router(about.router)
app.include_router(contact.router)
app.include_router(projects.router)