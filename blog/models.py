from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Pessoa(models.Model):
    nome = models.CharField(max_length=255, verbose_name=u'Nome')
    cpf = models.CharField(max_length=15, verbose_name=u'CPF')
    email = models.EmailField(verbose_name=u'Email')
    telefone = models.CharField(max_length=30, verbose_name=u'Telefone')
    data_nascimento = models.DateField(verbose_name=u'Data de nascimento')
    rg = models.CharField(max_length=30, verbose_name=u'RG', null=True, blank=True)
    endereco = models.CharField(max_length=255, verbose_name=u'Endereço residencial', null=True, blank=True)
    bairro = models.CharField(max_length=100, verbose_name=u'Bairro', null=True, blank=True)


    def __str__(self):
        return self.nome
