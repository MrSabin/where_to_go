from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description_short = models.CharField(max_length=500, verbose_name="Краткое описание")
    description_long = models.TextField(verbose_name="Полное описание")
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        "Place",
        verbose_name="К какому месту относится",
        related_name="images",
        on_delete=models.CASCADE,
    )
    image = models.ImageField(verbose_name="Фото")
    order = models.PositiveSmallIntegerField(verbose_name="Порядок", db_index=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.id} - {self.place}"
