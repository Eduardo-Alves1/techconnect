from django.urls import path
from . import views

urlpatterns = [
    path('user/register/', views.UserRegisterView.as_view(), name='User-Register'),
    #path('user/list/', views.UserListView.as_view(), name='User-List'),
]