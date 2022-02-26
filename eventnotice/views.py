
from django.views.generic.edit import FormView
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from .models import event
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.


class PostListView(ListView):
    context_object_name = 'posts'
    model = event
    template_name = 'eventnotice/new.html'

class PostDetailView(DetailView):
    model = event
    template_name = 'eventnotice/post_detail.html'



class PostCreate(LoginRequiredMixin,CreateView,FormView):
    model = event
    fields = ['title','details','event_poster', 'numberofpeople','company','contact_details','online_link' ]

    def form_valid(self,form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = event
    fields = ['title','details','event_poster', 'numberofpeople','company','contact_details','online_link' ]

    def form_valid(self,form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.posted_by:
            return True
        else:
            return False


   

