
from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('update/<int:id>/', views.update_user, name='updateuser'),
    path('delete/<int:id>/', views.delete_user, name='deleteuser'),
]
