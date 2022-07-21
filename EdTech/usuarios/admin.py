from django.contrib import admin

from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'tipo_usuario')
    search_fields = ('tipo_usuario',)
    
    # Para ocultar password
    def save_model(self, request, obj, form, change):
        if obj.password.startswith('pbkdf2'):
            obj.password=obj.password
        else:
            obj.set_password(obj.password) 
        super().save_model(request, obj, form, change)
        
admin.site.register(Usuario, UsuarioAdmin)