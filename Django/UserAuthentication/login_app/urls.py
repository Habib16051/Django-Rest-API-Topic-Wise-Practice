from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path
from . import views


app_name = 'login_app'
urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login_page'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)