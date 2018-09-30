# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class AnolectivoAdmin(admin.ModelAdmin):

    list_display = ('id_anolectivo', 'nombre', 'estado')
    list_filter = ('estado',)


class AuthGroupAdmin(admin.ModelAdmin):

    list_display = ('id', 'name')
    search_fields = ('name',)


class AuthGroupPermissionsAdmin(admin.ModelAdmin):

    list_display = ('id', 'group', 'permission')
    list_filter = ('group',)


class AuthPermissionAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'content_type', 'codename')
    search_fields = ('name',)


class AuthUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'cedula',
        'genero',
        'direccion',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
    )


class AuthUserGroupsAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'group')
    list_filter = ('user', 'group')


class AuthUserUserPermissionsAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'permission')
    list_filter = ('user',)


class DjangoAdminLogAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message',
        'content_type',
        'user',
    )
    list_filter = ('action_time', 'user')


class DjangoContentTypeAdmin(admin.ModelAdmin):

    list_display = ('id', 'app_label', 'model')


class DjangoMigrationsAdmin(admin.ModelAdmin):

    list_display = ('id', 'app', 'name', 'applied')
    list_filter = ('applied',)
    search_fields = ('name',)


class DjangoSessionAdmin(admin.ModelAdmin):

    list_display = ('session_key', 'session_data', 'expire_date')
    list_filter = ('expire_date',)


class EstudianteAdmin(admin.ModelAdmin):

    list_display = (
        'id_estudiante',
        'tipo_sangre',
        'alergias',
        # 'id_secretaria',
        'id',
        'id_representante',
    )
    list_filter = ('id', 'id_representante')


class MatriculaAdmin(admin.ModelAdmin):

    list_display = (
        'id_matricula',
        'costo',
        'fecha',
        'id_preinscripcion',
        'id_paralelo',
    )
    list_filter = ('fecha', 'id_preinscripcion', 'id_paralelo')


class NivelAdmin(admin.ModelAdmin):

    list_display = ('id_nivel', 'nombre', 'id_anolectivo')
    list_filter = ('id_anolectivo',)


class ParaleloAdmin(admin.ModelAdmin):

    list_display = ('id_paralelo', 'id_profesor')
    list_filter = ('id_profesor',)


class PensionAdmin(admin.ModelAdmin):

    list_display = ('id_pension', 'costo', 'id_matricula')
    list_filter = ('id_matricula',)


class PreinscripcionAdmin(admin.ModelAdmin):

    list_display = (
        'id_preinscripcion',
        'fecha',
        'id_estudiante',
        'id_representante',
        'id_nivel',
        'id_secretaria',
    )
    list_filter = (
        'fecha',
        'id_estudiante',
        'id_representante',
        'id_nivel',
        'id_secretaria',
    )


class ProfesorAdmin(admin.ModelAdmin):

    list_display = (
        'id_profesor',
        'titulo_profesor',
        'celular',
        'estado_civil',
        'id',
    )
    list_filter = ('id',)


class RepresentanteAdmin(admin.ModelAdmin):

    list_display = ('id_representante', 'celular', 'correo', 'id')
    list_filter = ('id',)


class RolAdmin(admin.ModelAdmin):

    list_display = ('id_rol', 'estudiante', 'profesor', 'id')
    list_filter = ('estudiante', 'profesor', 'id')


class SecretariaAdmin(admin.ModelAdmin):

    list_display = ('id_secretaria', 'fecha_ingreso', 'id')
    list_filter = ('fecha_ingreso', 'id')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Anolectivo, AnolectivoAdmin)
_register(models.AuthGroup, AuthGroupAdmin)
_register(models.AuthGroupPermissions, AuthGroupPermissionsAdmin)
_register(models.AuthPermission, AuthPermissionAdmin)
_register(models.AuthUser, AuthUserAdmin)
_register(models.AuthUserGroups, AuthUserGroupsAdmin)
_register(models.AuthUserUserPermissions, AuthUserUserPermissionsAdmin)
_register(models.DjangoAdminLog, DjangoAdminLogAdmin)
_register(models.DjangoContentType, DjangoContentTypeAdmin)
_register(models.DjangoMigrations, DjangoMigrationsAdmin)
_register(models.DjangoSession, DjangoSessionAdmin)
_register(models.Estudiante, EstudianteAdmin)
_register(models.Matricula, MatriculaAdmin)
_register(models.Nivel, NivelAdmin)
_register(models.Paralelo, ParaleloAdmin)
_register(models.Pension, PensionAdmin)
_register(models.Preinscripcion, PreinscripcionAdmin)
_register(models.Profesor, ProfesorAdmin)
_register(models.Representante, RepresentanteAdmin)
_register(models.Rol, RolAdmin)
_register(models.Secretaria, SecretariaAdmin)
