from django.shortcuts import render
from django.views import View

from .models import *


class HomeView(View):
    def get(self,request):

        main_articles = Article.objects.order_by('-important', '-views')[:20]
        latest_articles = Article.objects.order_by('-created_at')[:10]

        context = {
            'main_articles': main_articles,
            'latest_articles': latest_articles,
        }
        return render(request,'index.html', context)
