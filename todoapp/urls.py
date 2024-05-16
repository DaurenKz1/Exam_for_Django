
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = [
    path('', login , name='login'),
    path('homepage/', homepage , name='homepage'),
    path('signUp/', signup, name='signUp'),
    path('resetPassword/',reset_password , name='resetPassword'),
    path('profilePage/',profile_page , name='profilePage'),
    path('delete/<int:idd>',delete_task,name='delete'),
    path('edit/<int:idd>',edit_task,name='editTodo'),
    path('logOut/', logout , name='logOut'),
]

urlpatterns += staticfiles_urlpatterns()