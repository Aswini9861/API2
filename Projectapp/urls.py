
from django.urls import path
from Projectapp import views
urlpatterns = [
    path('hello-view/',views.HelloApiviews.as_view())
   
]
