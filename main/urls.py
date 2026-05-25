from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rules', views.rules, name='rules'),
    path('client', views.client, name='client'),
    path('faq', views.faq, name='faq'),
    path('games', views.games, name='games'),
    path('management', views.management, name='management'),
]
handler404 = "views.page_not_found"
