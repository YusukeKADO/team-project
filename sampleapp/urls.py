from django.urls import path
from . import views

app_name = 'sampleapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('article_create/', views.article_create, name='article_create'),
    path('redirect', views.redirect_test, name='redirect_test'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/delete', views.delete, name='delete'),
    path('<int:article_id>/update', views.delete, name='update'),
]