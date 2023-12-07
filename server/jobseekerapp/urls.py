from django.urls import path, include
from rest_framework import routers
from .views import JobSeekerViewSet, EmployerViewSet, JobViewSet, JobApplicationViewSet
from .views import welcome_view


router = routers.DefaultRouter()
router.register(r'jobseekers', JobSeekerViewSet)
router.register(r'employers', EmployerViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'applications', JobApplicationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', welcome_view, name='welcome_view'),
]
