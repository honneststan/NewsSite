from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/news/")
    tags = models.TextField(null=True, blank=True, help_text="Write in tag1, Tag2, format")
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "news"

    def __str__(self):
        return str(self.title)



