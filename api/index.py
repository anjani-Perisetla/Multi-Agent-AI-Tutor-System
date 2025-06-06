import logging
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

try:
    app.mount("/static", StaticFiles(directory="api/static"), name="static")
    templates = Jinja2Templates(directory="api/templates")
    logger.info("Templates and static files loaded successfully")
except Exception as e:
    logger.error(f"Failed to set up templates or static files: {e}")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    try:
        return templates.TemplateResponse("ai_tutor.html", {"request": request})
    except Exception as e:
        logger.error(f"Error rendering template: {e}")
        return HTMLResponse(content="Internal Server Error", status_code=500)
