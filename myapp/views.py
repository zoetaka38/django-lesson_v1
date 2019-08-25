from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView


# 指定されたテンプレートを引っ張ってきて、そのまま返すビュー
class MyFirstView(TemplateView):
    template_name = "myapp/index.html"

    def get(self, request, *args, **kwargs):
        context = super(MyFirstView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)