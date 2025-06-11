from django.db import models

class Certificacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_expedicion = models.DateField()
    fecha_vencimiento = models.DateField()
    imagen = models.ImageField(upload_to='certificados/images', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Certificación"
        verbose_name_plural = "Certificaciones"
        ordering = ['fecha_expedicion']