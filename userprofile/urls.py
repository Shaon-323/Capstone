import userprofile
from .import views
from userprofile.views import profile,register,signin,signout,enterlist,investorlist
from django.urls import path
urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/',views.signin,name='signin'),
    path('logout/',views.signout,name='signout'),
    path('search/',views.searchbar,name='searchbar'),
    path('investor/',views.investorlist,name='inv'),
    path('enterpreneur/',views.enterlist,name='ent'),
    path('profile/<str:username>/',views.profile,name='profile'),
 
    

]
