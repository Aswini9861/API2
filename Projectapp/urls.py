
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Projectapp import views
router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')




urlpatterns = [
    path('hello-view/',views.HelloApiviews.as_view()),
    path('',include(router.urls))

   
]
