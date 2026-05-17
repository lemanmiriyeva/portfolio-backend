from rest_framework import serializers
from .models import Project, ProjectImage, Category, Profile


class ProjectImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'image_url', 'caption', 'order']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class CategorySerializer(serializers.ModelSerializer):
    project_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'project_count']

    def get_project_count(self, obj):
        return obj.projects.count()


class ProjectSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    technologies_list = serializers.SerializerMethodField()
    images = ProjectImageSerializer(many=True, read_only=True)
    cover_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'short_description',
            'category', 'category_name',
            'images', 'cover_image_url',
            'video_url', 'video_file', 'project_url', 'github_url',
            'technologies', 'technologies_list', 'status',
            'is_featured', 'order', 'created_at', 'updated_at'
        ]

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None

    def get_technologies_list(self, obj):
        return obj.get_technologies_list()

    def get_cover_image_url(self, obj):
        request = self.context.get('request')
        cover = obj.cover_image
        if cover and request:
            return request.build_absolute_uri(cover.image.url)
        return None


class ProfileSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id', 'full_name', 'title', 'bio', 'email', 'phone',
            'github', 'linkedin', 'avatar', 'avatar_url',
            'cv', 'years_experience'
        ]

    def get_avatar_url(self, obj):
        request = self.context.get('request')
        if obj.avatar and request:
            return request.build_absolute_uri(obj.avatar.url)
        return None