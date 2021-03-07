from django.db import models

class Maradmin(models.Model):
    number = models.CharField(max_length=6)
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=10)
    url_link = models.URLField(max_length=200)
    body = models.TextField()

    class Meta:
        verbose_name = "Maradmin"

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse("Maradmin_detail", kwargs={"pk": self.pk})