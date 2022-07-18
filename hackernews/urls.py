"""hackernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.core.views import signup
from apps.story.views import frontpage, submit, newest, vote, story
from apps.userprofile.views import userprofile, votes, submissions
from django.contrib.auth import views
from django.views.static import serve
# from django.conf.urls.static import url


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('submit/', submit, name='submit'),
    path('s/<int:story_id>/vote/', vote, name='vote'),
    path('s/<int:story_id>/', story, name='story'),
    path('newest/', newest, name='newest'),
    path('signup/', signup, name='signup'),
    path('signup/', views.LoginView.as_view(template_name = 'core/signup.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('<str:username>/', userprofile, name='userprofile'),
    path('<str:username>/votes/', votes, name='votes'),
    path('<str:username>/submissions/', submissions, name='submissions'),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
