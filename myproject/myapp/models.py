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


class GeneralUser(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StoreUser(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Administrator(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Store(models.Model):
    # ID
    id = models.AutoField(primary_key=True)
    # 店舗名
    name = models.CharField(max_length=100)
    # ジャンル
    genre = models.CharField(max_length=100)
    # 都道府県
    prefecture = models.CharField(max_length=10)
    # 都道府県に続く住所
    address = models.CharField(max_length=100)
    # 写真
    image = models.ImageField(blank=True, null=True)
    # upload_toを使用すれば、MEDIA_ROOT配下の任意のフォルダを指定できる
    # image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name
