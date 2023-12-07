from django.contrib import admin
from django.urls import path, include
from jobseekerapp import urls as jobseeker_urls
from jobseekerapp.forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from jobseekerapp.views import register_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(jobseeker_urls)),
    path('', include(jobseeker_urls)),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_user, name='register_user'),
    path('accounts/', include('django.contrib.auth.urls')),
]
