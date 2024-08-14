from django.urls import path

from users.views import LoginUserView, UserCreateView, ProfileView, LogoutView

app_name = 'users'

urlpatterns = [
    # path('user/<int:user_id>/follow/', follow_user, name='follow_user'),
    # path('user/<int:user_id>/unfollow/', unfollow_user, name='unfollow_user'),
    # path('profiles/', ProfileView.as_view(), name='profiles'),
    #
    path('register/', UserCreateView.as_view(), name='register_page'),
    path('login/', LoginUserView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #
    #
    path('profile/', ProfileView.as_view(), name='profile_page'),
    #
    # path('user_detail/<int:user_id>/', user_profile, name='user_detail'),
    # path('users_list/', UserListView.as_view(), name='user_list'),
    #
    #
    # path('update/', UpdateProfileView.as_view(), name='update_page')
]


