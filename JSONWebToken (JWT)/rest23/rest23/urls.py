from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
# from api.auth import CustomAuthToken
from rest_framework.authtoken.views import obtain_auth_token

# Creating Router Objects
router = DefaultRouter()

# Register '' with router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('gettoken/', obtain_auth_token),
    # path('gettoken/', CustomAuthToken.as_view()),
]
