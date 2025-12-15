from django.shortcuts import render
from django.views import View

from .models import *


class HomeView(View):
    def get(self,request):

        main_articles = Article.objects.order_by('-important', '-views')[:20]

        context = {
            'main_articles': main_articles,
        }
        return render(request,'index.html', context)
