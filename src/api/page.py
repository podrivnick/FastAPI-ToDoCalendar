from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from .users import current_user
from models.users import User

router = APIRouter(
    prefix="/page",
    tags=["page"],
)

# for local start
# templates = Jinja2Templates(directory="front/templates/html")

# for docker start
templates = Jinja2Templates(directory="src/front/templates/html")


@router.get('')
async def index(request: Request, user: User = Depends(current_user)) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request, "user": user})

