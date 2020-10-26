from django.shortcuts import render,redirect
from . models import *
from .forms import ProjectUpload,UpdateProfileForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import PostSerializer,ProfileSeralizer

def home(request):
    projects = Post.objects.all()
    return render(request,'myprojects/index.html',{"projects":projects})

@login_required (login_url='/accounts/login/?next=/')   
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectUpload(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')
    else:
        form = ProjectUpload()
        return render(request,'myprojects/new_post.html',{"form":form})
    
def search_project(request):
    
    if 'search' in request.GET and request.GET["search"]:

        search_term = request.GET.get("search")
        searched_project = Post.objects.filter(title__icontains=search_term)
        message = f"{search_term}"  
        return render(request, 'myprojects/search.html', {"message": message, "projects": searched_project})

    else:
        message = "You haven't searched for any term "
        return render(request, 'myprojects/search.html', {"message": message})


  
    
    
def update_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    # form = UpdateProfileForm(instance=request.user)
    
    if request.method == "POST":
        form =  UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = UpdateProfileForm(instance=request.user.profile)
        return render(request,'myprojects/update-prof.html', {'form':form})
    
def profile_info(request):
    
    current_user=request.user
    profile_info = Profile.objects.filter(user=current_user).first()
    projects =  request.user.post_set.all()
    
    
    return render(request,'myprojects/profile.html',{"projects":projects,"profile":profile_info,"current_user":current_user})


class PostViewset(viewsets.ModelViewSet):
    '''
    API endpoint that allows one to view the details of projects posted
    '''
    
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer
    
class ProfileViewset(viewsets.ModelViewSet):
    '''
    API endpoint that allows one to view the details of profiles
    '''
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSeralizer