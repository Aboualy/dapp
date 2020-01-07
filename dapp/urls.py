"""dapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_registration/', user_views.user_registration, name='user_registration'),
    path('user_profile/', user_views.user_profile, name='user_profile'),
    url(r'^sign_in/$', auth_views.LoginView.as_view(template_name='accounts/sign_in.html',
                                                    redirect_authenticated_user=True), name='sign_in'),

    path('sign_out/', auth_views.LogoutView.as_view(template_name='accounts/sign_out.html'), name='sign_out'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),


    path('', include('gameboard.urls')),

]


