from django.urls import path
from apps import views

app_name = "apps"
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('musician_details/<pk>/', views.DetailView.as_view(), name='musician_details'),







]
