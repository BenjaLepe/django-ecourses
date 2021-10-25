from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_user, name="createuser"),
    path('account', views.account, name="account"),
    path('logout', views.log_out, name="logout"),
    path('login', views.log_in, name="login"),
    path('new_course', views.add_course, name="addcourse"),
    path('account/<str:course>/newexam', views.add_exam, name="addexam"),
    path('account/<str:course>/', views.show_course, name="showcourse"),    
    path('account/<str:course>/<int:exam>', views.edit_exam, name="change_exam"),
]
