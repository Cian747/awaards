from django.shortcuts import render,redirect,get_object_or_404
from .forms import GreazeRegistrationForm,PostProjectForm,UpdateProjectForm
from .models import Project,Profile,Rate
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from itertools import chain
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def register_user(request):
    rgf =GreazeRegistrationForm()
    if request.method == 'POST':
        rgf = GreazeRegistrationForm(request.POST)
        if rgf.is_valid():
            rgf.save()
            user = rgf.cleaned_data.get('username')
            email = rgf.cleaned_data.get('email')
            # send_welcome_email(user,email)
            messages.success(request, 'Account was created for ' + user)
            return redirect('login_user')
    
    return render(request, 'registration/registration.html', {'rgf': rgf})

def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'registration/login.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')

class HomeView(ListView):
    model = Project
    template_name = 'index.html'


class PostProjectView(CreateView):
    model = Project
    form_class = PostProjectForm
    template_name = 'post_project.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project-detail.html'


def project_details(request,id):
    current_project = Project.objects.get(id=id)
    # comments = Comment.objects.filter(image = id).all()

    # stuff = get_object_or_404(Image, id = request.POST.get('id'))
    # total_likes = current_image.total_likes()

    current_user = request.user
    # com_form = CommentForm()
   
    # if request.method == 'POST':
    #     new_comment = Comment(comment = request.POST.get('comment'), user_id=current_user, image = Image.objects.get(id=id))
    #     new_comment.save()
    #     return HttpResponseRedirect(reverse('image_detail', args=[int(id)]))


    return render(request,'project/project-detail.html',{"object":current_project,"user":current_user})


# class ProfileUpdateView(UpdateView):
#     models = Profile
#     form_class = EditForm
#     template_name = 'profile/edit-profile.html'

    def get_queryset(self): 
        return Profile.objects.all()

class UpdateProjectView(UpdateView):
    model = Project
    form_class = UpdateProjectForm
    template_name = 'project/edit-project.html'



class DeleteProjectView(DeleteView):
    models = Project
    template_name = 'delete-project.html'
    success_url = reverse_lazy('home')

    def get_queryset(self): 
        return Project.objects.all()

def remove_project(request,id):
    project = Project.objects.get(id= id)

    project.delete_project()

    return redirect('home')


# def edit_profile(request,id):
#     editing_profile = Profile.objects.get(id=id)
#     form = EditForm
#     # current_user = request.user
#     if request.method == 'POST':
#         form = EditForm(request.POST,request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user_id = editing_profile.user.id
#             post.save()
#             return redirect(request.META.get('HTTP_REFERER'))

#     return render(request,'profile/edit-profile.html',{"form":form})

def user_profile(request,id):
    user_profile = Profile.objects.get(id = id)
    user_profile_projects = Project.objects.filter(profile = id).all()

    current_user = request.user.id

    my_profile = Profile.objects.get(user =request.user)
    if user_profile.user in my_profile.following.all():
        follow = True
    else:
        follow = False


    return render(request,'profile/profile.html', {"profile":user_profile,"projects":user_profile_projects,"follow":follow,"current_user":current_user})

def search_for_project(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        search_results = Profile.search_by_user(search_term)

        return render(request,'search.html',{"results":search_results})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})







