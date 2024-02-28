from django.contrib.auth.models import Group
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('general', '一般ユーザ'),
        ('store', '店舗ユーザ'),
        ('admin', '管理者'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='myapp_customuser_permissions'
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='custom_user_set',
        related_query_name='user',
    )


class StoreDetail(models.Model):
    # 店舗名
    name = models.CharField(max_length=100, primary_key=True)
    # ジャンル
    genre = models.CharField(max_length=100)
    # 都道府県
    prefecture = models.CharField(max_length=10)
    # 都道府県に続く住所
    address = models.CharField(max_length=100)


class GeneralUser(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class StoreUser(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Administrator(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)