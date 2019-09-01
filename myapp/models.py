from django.db import models

# Create your models here.

class Post(models.Model):
    message = models.CharField(
        max_length=100, # 最大入力可能文字数
        verbose_name="タスク", # 項目の表示名
    ) # messageという項目が、文字列の属性を持つと定義
    complete_flag = models.BooleanField(
        verbose_name="完了フラグ"
    )
    created_date = models.DateField(
        verbose_name="登録日付"
    )
    created_by = models.CharField(
        max_length=100,
        verbose_name="登録者"
    )