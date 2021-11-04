from django.db import models

# Create your models here.

class DnaRegistration(models.Model):
    dna = models.JSONField()
    mutation = models.BooleanField()
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    
    class Meta:
        ordering = ('create_date',)
        verbose_name = 'DNA'
        verbose_name_plural = 'DNAs'

    def __str__(self):
        return str(self.dna)
    