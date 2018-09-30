from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class Anolectivo(models.Model):

    # Fields
    id_anolectivo = AutoField(primary_key=True, verbose_name="ID Año Lectivo")
    nombre = CharField(max_length=100)
    estado = BooleanField()


    class Meta:
        ordering = ('-pk',)
        db_table = 'anolectivo'

    def __str__(self):
        return u'%s' % self.nombre

    def get_absolute_url(self):
        return reverse('appjardin_anolectivo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('appjardin_anolectivo_update', args=(self.pk,))


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
    Genero_CHOICES = (
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
    ("Otro", "Otro"),    
    )

    password = models.CharField(max_length=128, verbose_name = 'Contraseña')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(unique=True, max_length=150, verbose_name = 'Nombre de Usuario')
    first_name = models.CharField(max_length=30, verbose_name = 'Nombres')
    last_name = models.CharField(max_length=30, verbose_name = 'Apellidos')
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(blank=True, null=True)
    cedula = models.CharField(max_length=30,blank=True, null=True)
    genero = models.CharField(max_length=30,blank=True, null=True, choices=Genero_CHOICES)
    direccion = models.CharField(max_length=200,blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'auth_user'

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


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

    # Fields
    id_estudiante = AutoField(primary_key=True)
    tipo_sangre = CharField(max_length=10)
    alergias = CharField(max_length=300)
    id_secretaria = IntegerField()

    # Relationship Fields
    id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id')
    id_representante = models.ForeignKey('Representante',
        db_column='id_representante', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)
        db_table = 'estudiante'

    def __str__(self):
        return u'%s %s' % (self.id.first_name, self.id.last_name)

    def get_absolute_url(self):
        return reverse('appjardin_estudiante_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('appjardin_estudiante_update', args=(self.pk,))


class Matricula(models.Model):

    # Fields
    id_matricula = AutoField(primary_key=True)
    costo = FloatField()
    fecha = DateTimeField(auto_now_add=True)

    # Relationship Fields
    id_preinscripcion = models.ForeignKey('Preinscripcion',
        db_column='id_preinscripcion', on_delete=models.CASCADE, verbose_name = 'Preinscripción'
    )
    id_paralelo = models.ForeignKey('Paralelo',
        db_column='id_paralelo', on_delete=models.CASCADE, verbose_name = 'Paralelo'
    )

    class Meta:
        ordering = ('-pk',)
        db_table = 'matricula'

    def __str__(self):
        return u'Est: %s' % self.id_preinscripcion.id_estudiante.id

    def get_absolute_url(self):
        return reverse('appjardin_matricula_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('appjardin_matricula_update', args=(self.pk,))


class Nivel(models.Model):

    # Fields
    id_nivel = AutoField(primary_key=True)
    nombre = CharField(max_length=50)
    paralelo = CharField(max_length=10, verbose_name = 'Paralelo')
    cupos = IntegerField(verbose_name = 'Cupos')
    # Relationship Fields
    id_anolectivo = models.ForeignKey('Anolectivo',
        db_column='id_anolectivo', on_delete=models.CASCADE, verbose_name = 'Año Lectivo'
    )
    id_profesor = models.ForeignKey('Profesor',
        db_column='id_profesor', on_delete=models.CASCADE, verbose_name = 'Profesor'
    )

    class Meta:
        verbose_name_plural = "Niveles"
        ordering = ('-pk',)
        db_table = 'nivel'

    def __str__(self):
        return u'%s' % self.nombre

    def get_absolute_url(self):
        return reverse('appjardin_nivel_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('appjardin_nivel_update', args=(self.pk,))


class Paralelo(models.Model):

    # Fields
    id_paralelo = IntegerField(primary_key=True)
    # Relationship Fields
    id_profesor = models.ForeignKey('Profesor',
        db_column='id_profesor', on_delete=models.CASCADE
    )
    

    class Meta:
        ordering = ('-pk',)
        db_table = 'paralelo'

    def __str__(self):
        return u'Prof. %s' % self.id_profesor.id

    def get_absolute_url(self):
        return reverse('appjardin_paralelo_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('appjardin_paralelo_update', args=(self.pk,))


class Pension(models.Model):

    # Fields
    id_pension = AutoField(primary_key=True)
    costo = FloatField()

    # Relationship Fields
    id_matricula = ForeignKey('Matricula',
        db_column='id_matricula', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)
        db_table = 'pension'

    def __str__(self):
        return u'%s' % self.id_matricula

    def get_absolute_url(self):
        return reverse('appjardin_pension_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('appjardin_pension_update', args=(self.pk,))


class Preinscripcion(models.Model):

    # Fields
    id_preinscripcion = AutoField(primary_key=True)
    fecha = DateTimeField(auto_now_add=True)

    # Relationship Fields
    id_estudiante = ForeignKey('Estudiante',
        db_column='id_estudiante', on_delete=models.CASCADE, verbose_name="Estudiante"
    )
    id_representante = ForeignKey('Representante',
        db_column='id_representante', on_delete=models.CASCADE, verbose_name="Representante"
    )
    id_nivel = ForeignKey('Nivel',
        db_column='id_nivel', on_delete=models.CASCADE, verbose_name="Nivel"
    )
    id_secretaria = ForeignKey('Secretaria',
        db_column='id_secretaria', on_delete=models.CASCADE, verbose_name = "Secretaria"
    )

    class Meta:
        ordering = ('-pk',)
        db_table = 'preinscripcion'

    def __str__(self):
        return u'Pre: %s' % self.id_estudiante.id

    def get_absolute_url(self):
        return reverse('appjardin_preinscripcion_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('appjardin_preinscripcion_update', args=(self.pk,))


class Profesor(models.Model):

    # Choices
    MONTH_CHOICES = (
    ("Soltero", "Soltero"),
    ("Casado", "Casado"),
    ("Divorciado", "Divorciado"),
    ("Viudo", "Viudo"),
    )
    Genero_CHOICES = (
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
    ("Otro", "Otro"),    
    )
    # Fields
    id_profesor = AutoField(primary_key=True)
    imagen = models.ImageField(max_length=100,upload_to='imagenprofesor',verbose_name = 'Imagen')
    titulo_profesor = CharField(max_length=50,verbose_name = 'Título')
    edad = IntegerField(verbose_name = 'Edad')
    ciudad = CharField(max_length=50,verbose_name = 'Ciudad')
    estado_civil = CharField(max_length=10, choices=MONTH_CHOICES,verbose_name = 'Estado Civil')
    genero = CharField(max_length=10, choices=Genero_CHOICES, verbose_name = 'Género')
    direccion = CharField(max_length=50, verbose_name = 'Dirección')
    celular = CharField(max_length=25,verbose_name = 'Celular')
    observacion = CharField(max_length=500, verbose_name = 'Observación')

    # Relationship Fields
    id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id')

    class Meta:
        ordering = ('-pk',)
        db_table = 'profesor'

    def __str__(self):
        return u'%s %s' % (self.id.first_name, self.id.last_name)

    def get_absolute_url(self):
        return reverse('appjardin_profesor_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('appjardin_profesor_update', args=(self.pk,))


class Representante(models.Model):

    # Fields
    id_representante = AutoField(primary_key=True)
    celular = CharField(max_length=25)
    correo = CharField(max_length=150)

    # Relationship Fields
    id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id')

    class Meta:
        ordering = ('-pk',)
        db_table = 'representante'

    def __str__(self):
        return u'%s %s' % (self.id.first_name, self.id.last_name)

    def get_absolute_url(self):
        return reverse('appjardin_representante_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('appjardin_representante_update', args=(self.pk,))


class Rol(models.Model):

    # Fields
    id_rol = AutoField(primary_key=True)
    estudiante = BooleanField()
    profesor = BooleanField()

    # Relationship Fields
    id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id')

    class Meta:
        ordering = ('-pk',)
        db_table = 'rol'

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('appjardin_rol_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('appjardin_rol_update', args=(self.pk,))


class Secretaria(models.Model):

    # Fields
    id_secretaria = AutoField(primary_key=True)
    fecha_ingreso = DateField()

    # Relationship Fields
    id = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id')

    class Meta:
        ordering = ('-pk',)
        db_table = 'secretaria'

    def __str__(self):
        return u'%s %s' % (self.id.first_name, self.id.last_name)

    def get_absolute_url(self):
        return reverse('appjardin_secretaria_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('appjardin_secretaria_update', args=(self.pk,))
