from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.urls import *
from .views import home_page,ProductViewSet


router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('home/', home_page, name ='home_page')

]