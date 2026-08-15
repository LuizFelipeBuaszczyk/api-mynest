from fastapi.routing import APIRouter

from controllers.auth_controller import AuthController
from dtos.auth_dto import PostAuthLoginDTO

router = APIRouter(prefix='/auth')

@router.post('/login')
async def post_login(payload: PostAuthLoginDTO):
    return await AuthController.login(payload)
