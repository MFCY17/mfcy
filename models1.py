# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Anolectivo(models.Model):
    id_anolectivo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'anolectivo'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    tipo_sangre = models.CharField(max_length=10)
    alergias = models.CharField(max_length=300)
    id_secretaria = models.IntegerField()
    id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'estudiante'


class Matricula(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    id_preinscripcion = models.ForeignKey('Preinscripcion', models.DO_NOTHING, db_column='id_preinscripcion')
    costo = models.FloatField()
    fecha = models.DateTimeField()
    id_paralelo = models.ForeignKey('Paralelo', models.DO_NOTHING, db_column='id_paralelo')

    class Meta:
        managed = False
        db_table = 'matricula'


class Nivel(models.Model):
    id_nivel = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_anolectivo = models.ForeignKey(Anolectivo, models.DO_NOTHING, db_column='id_anolectivo')

    class Meta:
        managed = False
        db_table = 'nivel'


class Paralelo(models.Model):
    id_paralelo = models.IntegerField(primary_key=True)
    id_profesor = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profesor')

    class Meta:
        managed = False
        db_table = 'paralelo'


class Pension(models.Model):
    id_pension = models.AutoField(primary_key=True)
    id_matricula = models.ForeignKey(Matricula, models.DO_NOTHING, db_column='id_matricula')
    costo = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pension'


class Preinscripcion(models.Model):
    id_preinscripcion = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='id_estudiante')
    id_representante = models.ForeignKey('Representante', models.DO_NOTHING, db_column='id_representante')
    id_nivel = models.ForeignKey(Nivel, models.DO_NOTHING, db_column='id_nivel')
    fecha = models.DateTimeField()
    id_secretaria = models.ForeignKey('Secretaria', models.DO_NOTHING, db_column='id_secretaria')

    class Meta:
        managed = False
        db_table = 'preinscripcion'


class Profesor(models.Model):
    id_profesor = models.AutoField(primary_key=True)
    titulo_profesor = models.CharField(max_length=50)
    celular = models.CharField(max_length=25)
    estado_civil = models.CharField(max_length=10)
    id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'profesor'


class Representante(models.Model):
    id_representante = models.AutoField(primary_key=True)
    celular = models.CharField(max_length=25)
    correo = models.CharField(max_length=150)
    id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'representante'


class Representanteestudiante(models.Model):
    id_representanteestudiante = models.AutoField(primary_key=True)
    id_estudiante = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='id_estudiante')
    id_representante = models.ForeignKey(Representante, models.DO_NOTHING, db_column='id_representante')

    class Meta:
        managed = False
        db_table = 'representanteestudiante'


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    estudiante = models.BooleanField()
    profesor = models.BooleanField()
    id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'rol'


class Secretaria(models.Model):
    id_secretaria = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateField()
    id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'secretaria'
