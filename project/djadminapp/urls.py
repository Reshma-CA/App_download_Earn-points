from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views
from djadminapp.api.views import AdminAppCreationAPIView,CategoryListAPIView, SubCategoryListAPIView


urlpatterns = [

     path('api/admin_dash/', AdminAppCreationAPIView.as_view(), name='admin_dash'),  # API endpoint
     path('api/categories/', CategoryListAPIView.as_view(), name='categories_list'),
     path('api/subcategories/', SubCategoryListAPIView.as_view(), name='subcategories_list'),

    
    path('dash/', views.admin_dashbord_view, name='admin_dashboard'),
    path('add_app/', views.admin_add_view, name='admin_add_app'),  # Template view
    path('admin_login/', views.admin_login_view, name='admin_login'),
    path('admin_logout/', views.admin_logout_view, name='admin_logout'),
]
