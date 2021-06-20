from django.urls import path

from admins.views import index, UserListView, UserUpdateView, UserDeleteView, CreateUser

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create/', CreateUser.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),  # передали primary key
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='admin_users_delete'),
]
