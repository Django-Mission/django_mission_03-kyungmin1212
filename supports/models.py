from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Faq(models.Model):
    question = models.CharField(verbose_name='제목',max_length=126)
    category_choice= [
        ('G','일반'),
        ('A','계정'),
        ('E','기타')
    ]
    category = models.CharField(
        verbose_name='카테고리',
        max_length=2,
        choices=category_choice
    )
    
    update_at = models.DateTimeField(verbose_name='최종 수정 일시',auto_now=True) 

class Inquiry(models.Model):
    question = models.CharField(verbose_name='질문 제목',max_length=126)
    category_choice= [
        ('G','일반'),
        ('A','계정'),
        ('E','기타')
    ]
    category = models.CharField(
        verbose_name='카테고리',
        max_length=2,
        choices=category_choice
    )
    
    created_at = models.DateTimeField(verbose_name='생성일시',auto_now_add=True)
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE ,null=True,blank=True)

class Answer(models.Model):
    content = models.TextField(verbose_name='내용')
    inquiry = models.ForeignKey(to='Inquiry',on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE ,null=True,blank=True)
