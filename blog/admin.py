from django.contrib import admin

from blog.models import Post, Pessoa

# Register your models here.

admin.site.register(Post)


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Informações Pessoais', {'fields': ('nome', 'cpf')}),
        ('Contato', {'fields': ('email',)}),
    )
    list_display = ('usuario', 'nome', 'cpf', 'email' )
    search_fields = ('cpf', 'usuario__username', 'usuario__first_name', 'usuario__last_name')
    list_filter = ('data_nascimento',)