from fastapi import APIRouter

from utils.logger import get_logger


router = APIRouter(
    prefix='/health', tags=['Health'])
logger = get_logger(__name__)

@router.get("")
def health():
    logger.info("health check received")
    return {"status": "ok"}