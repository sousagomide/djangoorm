from django.contrib import admin

from core.models import Carro, Chassi, Montadora


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero', )

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('chassi', 'montadora', 'modelo', 'preco')

@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome', )


