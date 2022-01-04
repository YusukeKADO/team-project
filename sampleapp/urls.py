from django.urls import path
from . import views

app_name = 'sampleapp'

urlpatterns = [
<<<<<<< HEAD
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('article_create/', views.article_create, name='article_create'),
=======
	#path('', views.apphome, name='apphome'),
    path('', views.index, name='index'),
>>>>>>> 6d9121448ef78e7a760c324615df55681f96e8c3
    path('redirect', views.redirect_test, name='redirect_test'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/delete', views.delete, name='delete'),
    path('<int:article_id>/update', views.delete, name='update'),
    path('media_create/', views.media_create, name='media_create'),
]