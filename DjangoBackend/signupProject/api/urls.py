
from django.urls import path
from api import views

urlpatterns = [
    path('signup/', views.SignupList.as_view()),
    path('signup_details/<id>', views.SignupDetails.as_view()),
]
