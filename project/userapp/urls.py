from django.urls import path
from . import views
from userapp.api.views import AppListAPIView

urlpatterns = [
   
    path('api/home/', AppListAPIView.as_view(), name='apps_api'),  # API endpoint
    
    path('', views.Welcome_page, name='Welcome_page'),
    path('user_signup/', views.user_signup_view, name='user_signup'),
    path('user_login/', views.user_login_view, name='user_login'),
    path('logout/', views.user_logout_view, name='logout'),
    path('home/', views.user_home_view, name='home'),
    path('profile/', views.profile, name='profile'),
    path('points/', views.points, name='points'),
    path('task/', views.task, name='task'),
    path('app_downloader/', views.app_downloader, name='app_downloader'),
     path('complete_task/<int:app_id>/', views.complete_task, name='complete_task'),
    # path('task_done/<int:myid>', views.task_done, name='task_done'),

]
