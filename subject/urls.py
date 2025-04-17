from django.urls import path

from subject.views import test, lesson_list, main

urlpatterns = [
    path('',main,name='main'),
    path('lesson_list/', lesson_list, name='lesson_list'),
    path('<int:pk>/lesson_list', test, name='test'),
]
