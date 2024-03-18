from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser, 
        PermissionsMixin,
        BaseUserManager
    )

class UserManager(BaseUserManager):
    # 슈퍼 유저 생성
    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    # 일반 유저 생성
    def create_user(self, email, password):
        if not email:
            raise ValueError("Please enter your email address")
        
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique = True)
    nickname = models.CharField(max_length=255)
    is_bussiness = models.BooleanField(default=False)

    # PermissionMixin: 권한 관리
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # 필수정보인 유저네임을 이메일로 대체한다.
    USERNAME_FIELD = 'email' 

    # 유저를 생성 및 관리 (유저를 구분해서 관리하기 위해 -관리자계정, 일반계정)
    objects = UserManager()

    def __str__(self):
        return f'email: {self.email}, nickname: {self.nickname}'