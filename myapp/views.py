from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView # データのリストを表示するためのビュー
from .models import Post

# 指定されたテンプレートを引っ張ってきて、そのまま返すビュー
class MyFirstView(ListView): # 渡すビューを変更（Lesson6）
    template_name = "myapp/index.html"

    def get(self, request, **kwargs): # ビューに単純にアクセスされたときの動き
        posts = Post.objects.all() # Postテーブルのデータを取得する
        context = { 'posts': posts } # Postテーブルの値を「posts」という名前で渡す
        return render(
            request,
            self.template_name, # どのテンプレートにデータを渡すのか
            context             # どのようなデータを渡すのか
        ) # テンプレートにデータを渡す