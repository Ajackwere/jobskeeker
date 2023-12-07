from django.contrib import admin
from django.urls import path, include
from jobseekerapp import urls as jobseeker_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(jobseeker_urls)),
]
