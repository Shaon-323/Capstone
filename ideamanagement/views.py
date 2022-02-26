from django.db.models.expressions import F
from django.shortcuts import render
from .models import IdeaCategory,IdeaPost
from .forms import IdeaForm,MessageForm
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from ideamanagement import models
# Create your views here.

class CategoryListView(ListView):
    context_object_name = 'categories'
    model = IdeaCategory
    template_name = 'ideamanagement/category_list.html'


class IdeaListView(DetailView):
    context_object_name = 'categories'
    model = IdeaCategory
    template_name = 'ideamanagement/idea_list.html'




class IdeaDetailView(DetailView,FormView):
    context_object_name = 'ideas'
    model = IdeaPost
    template_name = 'ideamanagement/idea_detail.html'
    form_class = MessageForm

    def get_context_data(self, **kwargs):
        context = super(IdeaDetailView,self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.form_class
        return context

    def get_success_url(self):
        self.object = self.get_object()
        idea = self.object.idea
        return reverse_lazy('idea_detail',kwargs={'category':idea.slug,'slug':self.object.slug})


    def form_valid(self, form):

        self.object = self.get_object()

        fm = form.save(commit=False)
        fm.author = self.request.user

        fm.idea_name = self.object.messages.name
        fm.idea_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    









class IdeaCreateView(LoginRequiredMixin,CreateView,FormView):
    context_object_name = 'categorie'
    form_class = IdeaForm
    model = IdeaCategory
    template_name = 'ideamanagement/idea_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        return reverse_lazy('idea_list',kwargs={'slug':self.object.slug})

    def form_valid(self, form):
        self.object = self.get_object()
        form = form.save(commit=False)
        form.created_by = self.request.user
        form.idea = self.object
        form.save()
        return super().form_valid(form)

class IdeaUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    context_object_name = 'ideas'
    fields =  ('title','summary','details','post_image1','post_image2','post_image3','video','File','price')
    model = IdeaPost
    template_name = 'ideamanagement/idea_update.html'

    def test_func(self):
        idea = self.get_object()
        if self.request.user == idea.created_by:
            return True
        else:
            return False

class IdeaDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    context_object_name='ideas'
    model= IdeaPost
    template_name ='ideamanagement/idea_delete.html'

    def get_success_url(self):
        self.object = self.get_object()
        idea = self.object.idea
        return reverse_lazy('idea_list',kwargs={'slug':idea.slug})
    
    
    def test_func(self):
        idea = self.get_object()
        if self.request.user == idea.created_by:
            return True
        else:
            return False
    

def codechecking(request):

    if request.method=='GET':
        idea = request.GET.get('ideaname')
        code = request.GET.get('code')

        post = IdeaPost.objects.all().filter(title=idea,download=code)
     
        return render(request,'buy.html',{'post':post})
            

            

