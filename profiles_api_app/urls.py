from django.urls import path, include
from profiles_api_app import views
from rest_framework.routers import DefaultRouter

#definig a router
router = DefaultRouter()
router.register('HelloViewSet/', views.HelloViewSet, base_name='HelloViewSet')

urlpatterns = [
                path('HelloApiView/', views.HelloApiView.as_view()),
                path('', include(router.urls)),
]
