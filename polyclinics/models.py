from django.db import models


class Polyclinic(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nama Poli")
    description = models.TextField(blank=True, null=True, verbose_name="Deskripsi")
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "polyclinics"
        ordering = ["name"]
        verbose_name = "Poliklinik"
        verbose_name_plural = "Poliklinik"

    def __str__(self):
        return self.name
