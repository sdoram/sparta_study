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

    def create_superuser(self, email ,password=None):
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
    
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=20)
    # 유니크 값 + 아이디로 사용 
    email = models.EmailField(max_length=254, unique=True)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(null=True)
    introduction = models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # 1. id : 데이터 고유 id 입니다(PK).
    # 2. email : 아이디로 사용되며 유니크한 값입니다.
    # 3. password : 비밀번호로 사용되며 회원 생성, 수정 시 암호화(해시)된 값을 저장해야 합니다.
    # 4. name : 사용자의 이름입니다.
    # 5. gender : 사용자의 성별입니다.
    # 6. age : 사용자의 나이입니다.
    # 7. introduction : 사용자의 자기소개 글 입니다

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