from django.urls import path
from .views import StudentView
urlpatterns = [
    path('student/',StudentView.as_view(),name='student'),
    path('student/<int:stud_id>',StudentView.as_view(),name='individual_student'),
]
