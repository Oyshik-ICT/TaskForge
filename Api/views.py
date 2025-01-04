from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .models import Task
from .serializers import TaskSerializer, UserSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing all users and creating new users.
    GET: List all users (admin only)
    POST: Create a new user (public access)

    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


class UserRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating and deleting a specific user.
    Users can only manage their own accounts.
    GET: Retrieve user details
    PUT/PATCH: Update user details
    DELETE: Delete user account

    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = User.objects.filter(id=self.kwargs["pk"], username=self.request.user)
        return qs


class TaskListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing and creating tasks.
    Regular users can only see their own tasks, staff can see all tasks.
    GET: List tasks with optional status filter
    POST: Create a new task (authenticated users only)

    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["status"]

    def get_queryset(self):
        qs = Task.objects.all()

        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)

        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for managing individual tasks.
    Users can only manage their own tasks.
    GET: Retrieve task details
    PUT/PATCH: Update task details
    DELETE: Delete task
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Task.objects.filter(user=self.request.user)
        return qs
