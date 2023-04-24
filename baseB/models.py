from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):
    cpf = models.CharField(max_length=16, null=False, blank=False)
    nome = models.CharField(max_length=150, null=False)
    idade = models.IntegerField(null=False)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField(null=True)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)
    lista_de_bens = models.TextField()
    fonte_renda = models.TextField()
    movimentacao_financeira = models.DateTimeField(timezone.now, auto_now_add=True)
    ultima_consulta = models.DateTimeField(timezone.now, auto_now_add=True)


    def __str__(self): 
        return '%s' % (self.nome)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Cliente.objects.get(pk=self.pk)
            if orig.lista_de_bens != self.lista_de_bens:
                self.movimentacao_financeira = timezone.now()
        super().save(*args, **kwargs)