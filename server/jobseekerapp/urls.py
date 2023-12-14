from django.urls import path, include
from rest_framework import routers
from .views import JobSeekerViewSet, EmployerViewSet, JobViewSet, JobApplicationViewSet
from .views import welcome_view, register_user
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_user, profile


router = routers.DefaultRouter()
router.register(r'jobseekers', JobSeekerViewSet)
router.register(r'employers', EmployerViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applications', JobApplicationViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', welcome_view, name='welcome_view'),
    path('register/', register_user, name='register_user'),
    path('my-applications/', JobApplicationViewSet.as_view({'get': 'my_applications'}), name='my-applications'),
    path('jobs/<int:pk>/applicants/', JobViewSet.as_view({'get': 'my_applicants'}), name='job-applicants'),
    path('accounts/profile/', profile, name='profile'),    
]
