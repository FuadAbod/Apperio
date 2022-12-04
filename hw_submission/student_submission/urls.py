from django.urls import path
from . import views


urlpatterns = [
    path('api/homework/',
        views.get_homework,
        name='get_homework'
    ),
    path('api/submit_homework/',
        views.submit_homework,
        name='submit_homework'
    )
]