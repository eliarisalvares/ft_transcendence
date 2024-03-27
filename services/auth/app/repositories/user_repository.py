from ..models.user import User
from ..models.login_type import LoginType
from ..interfaces.repositories.user_repository import IUserRepository
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from asgiref.sync import sync_to_async
from typing import List

class UserRepository(IUserRepository):

  async def get_user_by_username(self, username: str) -> User:
    return await User.objects.aget(user_name=username)
  
  async def get_user_by_email(self, email: str) -> User:
    return await User.objects.aget(email=email)
  
  async def get_user_by_id(self, id: str) -> User:
    return await User.objects.aget(id=id)
  
  async def get_user_by_email_or_username(self, email: str, username: str) -> List[User]:
    users = []
    async for user in await sync_to_async(User.objects.filter, thread_sensitive=True)(
     Q(email=email) | Q(user_name=username),
    ):
      users.append(user)
    return users

  async def create_user(self, user: User) -> User:
    hashed_password = make_password(user.password)
    return await User.objects.acreate(
      user_name=user.user_name,
      email=user.email,
      login_type=user.login_type,
      password=hashed_password
    )
  
  async def update_user(self, user: User) -> User:
    await User.objects.filter(id=user.id).aupdate(
      user_name=user.user_name,
      email=user.email,
      login_type=user.login_type,
      password=user.password,
      enable_2fa=user.enable_2fa,
      is_active=user.is_active
    )
    return user
  
  def update_user_sync(self, user: User) -> User:
    User.objects.filter(id=user.id).update(
      user_name=user.user_name,
      email=user.email,
      login_type=user.login_type,
      password=user.password,
      enable_2fa=user.enable_2fa,
      is_active=user.is_active
    )
    return user
  
  async def delete_user(self, id: str) -> bool:
    await User.objects.filter(id=id).adelete()
    return True