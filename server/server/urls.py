from django.contrib import admin
from django.urls import path, include
from jobseekerapp import urls as jobseeker_urls
from jobseekerapp.forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from jobseekerapp.views import register_user
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Jobseeker API",
        default_version='v1',
        description="This API contains the endpoints for jobseeker app including /my_applications, /my_applicants, /jobs /employers, /jobseeker, /login, /logout , and /register ",
        terms_of_service="https://www.github.com/ajackwere/",
        contact=openapi.Contact(email="austinewere59@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(jobseeker_urls)),
    path('', include(jobseeker_urls)),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_user, name='register_user'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]
