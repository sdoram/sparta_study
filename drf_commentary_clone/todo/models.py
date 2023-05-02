from django.db import models
from user.models import User
from django.utils import timezone

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey(User ,verbose_name="작성자" ,on_delete=models.CASCADE)
    title = models.CharField("할일 제목", max_length=100)
    is_complete = models.BooleanField("완료 여부", default=False)
    created_at = models.DateTimeField("생성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정 시간", auto_now=True)
    completion_at = models.DateTimeField("완료 시간", null=True, blank=True)

    def complete(self):
        """ todo를 완료합니다."""
        # 다시 실행하면 취소 + completion_at 비우기
        self.is_complete = True
        self.completion_at = timezone.now()
        self.save()
