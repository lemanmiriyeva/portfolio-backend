from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kateqoriya adı")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Kateqoriya"
        verbose_name_plural = "Kateqoriyalar"
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('active', 'Aktiv'),
        ('completed', 'Tamamlandı'),
        ('in_progress', 'Davam edir'),
    ]

    title = models.CharField(max_length=200, verbose_name="Başlıq")
    description = models.TextField(verbose_name="Açıqlama")
    short_description = models.CharField(
        max_length=300, blank=True, verbose_name="Qısa açıqlama"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='projects', verbose_name="Kateqoriya"
    )
    video_url = models.URLField(
        blank=True, null=True,
        verbose_name="Video URL (YouTube/Vimeo)"
    )
    video_file = models.FileField(
        upload_to='projects/videos/', blank=True, null=True,
        verbose_name="Video fayl"
    )
    project_url = models.URLField(blank=True, null=True, verbose_name="Proyekt URL")
    github_url = models.URLField(blank=True, null=True, verbose_name="GitHub URL")
    technologies = models.CharField(
        max_length=500, blank=True,
        verbose_name="Texnologiyalar (vergüllə ayırın)"
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES,
        default='completed', verbose_name="Status"
    )
    is_featured = models.BooleanField(default=False, verbose_name="Önə çıxarılsın?")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıra nömrəsi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma tarixi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")

    class Meta:
        verbose_name = "Proyekt"
        verbose_name_plural = "Proyektlər"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        if self.technologies:
            return [t.strip() for t in self.technologies.split(',')]
        return []

    @property
    def cover_image(self):
        """Birinci şəkli qaytarır (kart üçün)"""
        first = self.images.order_by('order').first()
        return first


class ProjectImage(models.Model):
    """Proyektə aid çoxsaylı şəkillər"""
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name='images', verbose_name="Proyekt"
    )
    image = models.ImageField(
        upload_to='projects/gallery/', verbose_name="Şəkil"
    )
    caption = models.CharField(
        max_length=200, blank=True, verbose_name="Şəkil açıqlaması"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Sıra")

    class Meta:
        verbose_name = "Proyekt Şəkli"
        verbose_name_plural = "Proyekt Şəkilləri"
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} — şəkil {self.order + 1}"


class Profile(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Ad Soyad")
    title = models.CharField(max_length=200, verbose_name="Vəzifə/Başlıq")
    bio = models.TextField(verbose_name="Haqqında")
    email = models.EmailField(blank=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    github = models.URLField(blank=True, verbose_name="GitHub")
    linkedin = models.URLField(blank=True, verbose_name="LinkedIn")
    avatar = models.ImageField(
        upload_to='profile/', blank=True, null=True, verbose_name="Profil şəkli"
    )
    cv = models.FileField(
        upload_to='profile/cv/', blank=True, null=True, verbose_name="CV (PDF)"
    )
    years_experience = models.PositiveIntegerField(default=0, verbose_name="Təcrübə (il)")

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"

    def __str__(self):
        return self.full_name