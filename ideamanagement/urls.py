from os import name
from django import urls
from .import views
from ideamanagement.views import CategoryListView, IdeaListView,IdeaDetailView,IdeaCreateView,IdeaUpdateView,IdeaDeleteView, codechecking

from django.urls import path


urlpatterns = [
   path('category/',CategoryListView.as_view(),name='category'),
   path('buyIdea/',views.codechecking,name='codecheck'),
   path('<slug:slug>',IdeaListView.as_view(),name='idea_list'),
   path('<slug:category>/<slug:slug> ',IdeaDetailView.as_view(),name='idea_detail'),
   path('<slug:slug>/create/',IdeaCreateView.as_view(),name='idea_create'),
   path('<slug:category>/<slug:slug>/update/',IdeaUpdateView.as_view(),name='idea_update'),
   path('<slug:category>/<slug:slug>/delete/',IdeaDeleteView.as_view(),name='idea_delete'),
]
