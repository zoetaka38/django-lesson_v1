from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdminTest(admin.ModelAdmin):
    list_display = ('message', 'complete_flag','created_date',) # 表示する項目を制御する場合
    list_display_links = ('message','created_date',) # リンクをつける表示項目を設定

class PostAdmin(admin.ModelAdmin):
    class Meta:
        pass # まるっとオブジェクトとして表示

admin.site.register(Post,PostAdminTest) # 管理者画面に表示するという動作を宣言