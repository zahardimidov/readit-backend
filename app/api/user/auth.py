from fastapi import APIRouter, Depends

from app.schemas import UserSignIn, UserSignInResponse
from app.services import UserService

router = APIRouter(prefix='/auth')


@router.post("", summary="Аутентификация пользователя", response_model=UserSignInResponse)
async def telegram_auth(
    data: UserSignIn, service: UserService = Depends(UserService)
):
    auth_token = await service.authenticate_telegram_user(init_data=data.init_data)

    return dict(token=auth_token)
