
from django.urls import path,include
from . import views
urlpatterns = [
    path('cred/', views.Commit, name='signin-sect'),
    path('user/', views.UserData, name='get-user'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]
