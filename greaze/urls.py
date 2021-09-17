from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, ProjectDetailView,PostProjectView,DeleteProjectView,UpdateProjectView 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user,name='login_user'),
    path('register/',views.register_user,name='register'),
    path('home/',HomeView.as_view(), name='home'),
    path('post/',PostProjectView.as_view(),name='post_project'),
    path('project-detail/<int:id>',views.project_details, name='project_details'),
    path('edit_project/<int:pk>',UpdateProjectView.as_view(),name='update_project'),
    path('delete/<int:pk>',DeleteProjectView.as_view(), name="delete")

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)