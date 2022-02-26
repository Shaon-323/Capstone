import eventnotice
from .import views
from eventnotice.views import PostListView, PostCreate,PostDetailView,PostUpdateView
from django.urls import path



urlpatterns = [
   
    path('newspost/', PostListView.as_view() ,name='news'),
    path('newspost/<int:pk>',PostDetailView.as_view() ,name='post_detail'),
    path('newspost/<int:pk>/update',PostUpdateView.as_view() ,name='post_update'),
    path('newspost/new',PostCreate.as_view() ,name='createpost'),
  
    

]