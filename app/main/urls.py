from django.urls import path
from .views import UserViewSet, LoginView
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'login', LoginView)
app_name = "main"
urlpatterns = [
    path('', LoginView, name="login")
]
