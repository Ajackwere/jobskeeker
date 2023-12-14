from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from rest_framework import viewsets
from rest_framework.response import Response
from .models import JobSeeker, Employer, Job, JobApplication
from .serializers import JobSeekerSerializer, EmployerSerializer, JobSerializer, JobApplicationSerializer
from rest_framework.decorators import action
from .forms import CustomUserCreationForm


def welcome_view(request):
    return render(request, 'welcome.html')
class JobSeekerViewSet(viewsets.ModelViewSet):
    queryset = JobSeeker.objects.all()
    serializer_class = JobSeekerSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

class EmployerViewSet(viewsets.ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

    def perform_destroy(self, instance):
        instance.delete()

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
    
    @action(detail=True, methods=['GET'])
    def my_applicants(self, request, pk=None):
        job = self.get_object()
        job_applications = JobApplication.objects.filter(job=job)
        return render(request, 'my_applicants.html', {'job_applications': job_applications})
    
class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    
    @action(detail=False, methods=['GET'])
    def my_applications(self, request):
        job_applications = JobApplication.objects.filter(job_seeker=request.user.jobseeker)
        serializer = self.get_serializer(job_applications, many=True)
        return Response(serializer.data)
    
    def list(self, request, *args, **kwargs):
        # Retrieve applications with a specific status
        status_param = request.query_params.get('status', None)
        if status_param:
            applications = JobApplication.objects.filter(status=status_param)
            serializer = self.get_serializer(applications, many=True)
            return Response(serializer.data)
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data
        data['status'] = data.get('status', instance.status)
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register_user.html', {'form': form})
