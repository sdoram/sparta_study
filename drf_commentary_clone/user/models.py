from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Meta:
        db_table = 'user'
    genders = (
        ("F", "여자"),
        ("M", "남자"),
    )
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=256)
    name = models.CharField("이름", max_length=20)
    gender = models.CharField(
        "성별", max_length=10, blank=True, default='', choices=genders)
    age = models.IntegerField("나이", null=True)
    introduction = models.TextField("자기 소개", blank=True, default='')

    created_at = models.DateTimeField("생성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정 시간", auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
