from django.db import models

class Maradmin(models.Model):
    number = models.CharField(max_length=50)
    title = models.CharField(max_length=300)
    date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=10)
    url_link = models.URLField(max_length=200)
    body = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Maradmin"

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse("Maradmin_detail", kwargs={"pk": self.pk})