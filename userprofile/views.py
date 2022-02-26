from django.urls.base import reverse_lazy
import userprofile
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from userprofile.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login



from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from userprofile.models import UserProfileInfo,User

from django.views.generic import UpdateView

from django.contrib.auth.forms import UserChangeForm
# Create your views here.

def home(request):
    return render(request,'home.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST , request.FILES)
        profile_form = UserProfileInfoForm(request.POST , request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'registration.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    return HttpResponse("Not Active")
        else:
            return HttpResponse("Not Matched")

    else:
        return render(request,'login.html')

@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def profile(request,username):
    user = User.objects.get(username=username)
    if user:
        profile = UserProfileInfo.objects.get(user=user)
        user_type = profile.user_type
        user_img = profile.profile_pic
        facebook = profile.facebooklink
        phone = profile.phone

        data = {
            'profile':profile,
            'user_obj':user,
            'phone':phone,
            'user_type':user_type,
            'user_img':user_img,
         
        }
        
        return render(request,'profile.html',data)

    
def searchbar(request):
    if request.method=='GET':
        search = request.GET.get('search')
        print(search)
        pro = User.objects.all().filter(username__icontains=search)
        return render(request,'search.html',{'pro':pro})
    else:
        
        return render(request,'search.html')


def investorlist(request):
    pr = User.objects.all()
    return render(request,'investor.html',{'pr':pr})
    
def enterlist(request):
    pr = User.objects.all()
    return render(request,'enterpreneur.html',{'pr':pr})


