import pathlib

import app
from app.routers import home, about, contact, projects
from app.routers import home, about, contact, projects

# ...

app.include_router(home.router)
app.include_router(about.router)
app.include_router(projects.router)
app.include_router(contact.router)