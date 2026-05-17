from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Project, Category, Profile
from .serializers import ProjectSerializer, CategorySerializer, ProfileSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'is_featured', 'category']
    search_fields = ['title', 'description', 'technologies']
    ordering_fields = ['order', 'created_at', 'title']
    ordering = ['order', '-created_at']

    def get_queryset(self):
        queryset = Project.objects.all()
        category = self.request.query_params.get('category')
        featured = self.request.query_params.get('featured')
        status = self.request.query_params.get('status')

        if category:
            queryset = queryset.filter(category__slug=category)
        if featured:
            queryset = queryset.filter(is_featured=True)
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


@api_view(['GET'])
def api_overview(request):
    return Response({
        'projects': '/api/projects/',
        'categories': '/api/categories/',
        'profile': '/api/profile/',
        'featured_projects': '/api/projects/?featured=true',
    })
