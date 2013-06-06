from django.db import models
from django.contrib.auth.models import User, Group

class Nacionalidad (models.Model):
	abbr_estado		= models.CharField(max_length=5, primary_key=True)
	descr			= models.CharField(max_length=100, null=False)
	nacimiento		= models.CharField(max_length=50)
	clave_estado	= models.IntegerField(null=False)

	def __unicode__(self):
		return "%s" % self.abbr_estado

	class Meta:
		db_table ='nacionalidad'
	
#---------------------------------------------
class Genero(models.Model):
	sexo		= models.CharField(max_length=10, primary_key=True)
	descr		= models.CharField(max_length=45, null=False)

	def __unicode__(self):
		return "%s" % self.descr

	class Meta:
		db_table = 'genero'

#---------------------------------------------
class Marital(models.Model):
	estado_civil	= models.CharField(max_length=25, primary_key=True)
	descr			= models.CharField(max_length=25, null=False)

	def __unicode__(self):
		return "%s" % self.descr

	class Meta:
		db_table='marital'

#---------------------------------------------
class Personal(models.Model):
	rfc				= models.CharField(max_length=13, primary_key=True)
	apellidop		= models.CharField(max_length=50, null=False, verbose_name='Ap. Paterno')
	apellidom		= models.CharField(max_length=50, blank=True, verbose_name='Ap. Materno')
	nombre			= models.CharField(max_length=100, null=False)		
	curp			= models.CharField(max_length=18, null=False)
	sexo			= models.ForeignKey(Genero, related_name='personal-genero')
	estado_civil 	= models.ForeignKey(Marital, related_name='personal-marital')
	abbr_estado		= models.ForeignKey(Nacionalidad, related_name='personal-nacionalidad')
	ingreso_gob		= models.DateField(auto_now_add=False)
	ingreso_dep		= models.DateField(auto_now_add=False)
	domicilio		= models.TextField()
	colonia			= models.TextField()
	municipio		= models.TextField()
	cedula_profesional = models.BigIntegerField(default='0')

	def __unicode__(self):
		ap = self.apellidop
		am = self.apellidom
		n  = self.nombre
		return "%s %s %s" % (ap, am,n)

	class Meta:
		db_table = 'personal'
#---------------------------------------------
class Adscripcion(models.Model):
	cr			= models.IntegerField(primary_key=True)
	descr		= models.CharField(max_length=150, null=False)
	jnum		= models.SmallIntegerField(default=0)
	fisicamente	= models.IntegerField(default=0)
	fdescr		= models.CharField(max_length=150, null=False)

	def __unicode__(self):
		return "%s" % (self.descr)

	class Meta:
		db_table = 'adscripcion'

#---------------------------------------------
class Codigos(models.Model):
	id_codigo		= models.IntegerField(primary_key=True)
	codigo			= models.CharField(max_length=7, db_index=True)
	descr			= models.CharField(max_length=50)
	rama			= models.CharField(max_length=25)
	anio			= models.IntegerField()

	def __unicode__(self):
		return "%s: %s" %  (self.codigo, self.descr)

	class Meta:
		db_table= 'codigos'
		unique_together= ('codigo', 'anio')
#---------------------------------------------
class Autoridad(models.Model):
	autoridad		= models.CharField(max_length=25, primary_key=True)
	descr			= models.CharField(max_length=45)

	def __unicode__(self):
		return "%s" % self.descr

	class Meta:
		db_table='autoridad'
#---------------------------------------------
class Programa(models.Model):
	tipo_trabajador 	= models.CharField(max_length=25, primary_key=True)
	descr				= models.CharField(max_length=50)

	def __unicode__(self):
		return "%s" % self.tipo_trabajador

	class Meta:
		db_table = 'programa'
#---------------------------------------------
class Plantilla(models.Model):
	rfc					= models.ForeignKey(Personal, related_name='plantilla-personal')
	vigencia_del		= models.DateField(auto_now_add=False, null=True)
	vigencia_al			= models.DateField(auto_now_add=False, null=True)
	cr					= models.ForeignKey(Adscripcion,related_name='plantilla-adscripcion')
	autoridad			= models.ForeignKey(Autoridad, related_name='plantilla-autoridad')
	activo				= models.SmallIntegerField(default=1)
	tabulador			= models.SmallIntegerField(default=2)
	jornada				= models.SmallIntegerField(default=8)
	tipo_trabajador		= models.ForeignKey(Programa, related_name='plantilla-programa')
	clave_presupuestal	= models.CharField(max_length=30, null=False)
	movto				= models.IntegerField()
	docto				= models.BigIntegerField()
	fakerfc				= models.CharField(max_length=13, null=True)
	codigo				= models.ForeignKey(Codigos, related_name='plantilla-codigos')
	anio				= models.SmallIntegerField()
	quincena			= models.SmallIntegerField()
	id					= models.AutoField(primary_key=True)

	def __unicode__(self):
		return "%s" % (self.clave_presupuestal)

	class Meta:
		db_table= 'plantilla'
		
	
#---------------------------------------------
class Operacion(models.Model):
	operacion			= models.IntegerField(primary_key=True)
	short_descr			= models.CharField(max_length=10)
	long_descr			= models.CharField(max_length=100)
	grupo				= models.SmallIntegerField()
	jerarquia			= models.SmallIntegerField()
	habilitado			= models.SmallIntegerField()

	def __unicode__(self):
		return "%d:%s" % (self.operacion, self.short_descr)

	class Meta:
		db_table = 'operacion'
#---------------------------------------------
class Turnos(models.Model):
	turno			= models.IntegerField(primary_key=True)
	descr			= models.CharField(max_length=50)

	def __unicode__(self):
		return "%s" % (self.descr)

	class Meta:
		db_table = 'turnos'
		
#---------------------------------------------
class Excepcion(models.Model):
	fecha_excepcion			= models.DateField(auto_now_add=False, primary_key=True)
	descr					= models.CharField(max_length=100)
	hora_excepcion			= models.TimeField(auto_now_add=False)
	turno					= models.ForeignKey(Turnos, related_name='excepcion-turno')
	operacion				= models.ForeignKey(Operacion, related_name='excepcion-operacion')
	habilitado				= models.IntegerField(default=1)

	def __unicode__(self):
		return "%s:%s" % (self.operacion, self.descr)

	class Meta:
		db_table = 'excepcion'
		
#---------------------------------------------
class Control(models.Model):
	clave_trabajador		= models.IntegerField(null=False)
	fecha_control			= models.DateField(auto_now_add=False, null=False)
	hora_control			= models.TimeField(auto_now_add=False, null=True)
	observaciones			= models.CharField(max_length=200, null=True, blank=True)
	habilitado				= models.SmallIntegerField(default=1)
	operacion				= models.ForeignKey(Operacion, related_name='control-operacion')
	rfc						= models.ForeignKey(Personal, related_name='control-personal')
	usuario					= models.ForeignKey(User)
	id_control				= models.AutoField(primary_key=True)
	
	def __unicode__(self):
		return "%s:%s" % (self.clave_trabajador, self.operacion)

	class Meta:
		db_table = 'control'
#---------------------------------------------
class Horarios(models.Model):
	clave_trabajador 		= models.ForeignKey(Control, related_name='horario-control')
	dia_de_semana			= models.SmallIntegerField()
	hora					= models.TimeField(auto_now_add=False)
	turno					= models.ForeignKey(Turnos, related_name='horario-turno')
	habilitado				= models.SmallIntegerField(default=1)
	id_horario				= models.AutoField(primary_key=True)

	def __unicode__(self):
		return "%d:%s" % (self.dia_semana,self.hora)

	class Meta:
		db_table='horarios'
#---------------------------------------------

