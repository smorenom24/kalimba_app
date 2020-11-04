from django.db import models

# Create your models here.
class Envio(models.Model):
	fecha = models.DateField()
	precio_envio = models.IntegerField()
	codigo_envio = models.CharField(max_length=200)

class producto(models.Model):
	color = models.CharField(max_length = 200)
	dibujo = models.CharField(max_length = 200)
	diseño_especial = models.BooleanField(default=False)
	precio_venta = models.IntegerField()
	image = models.ImageField(upload_to = "imagenes_kalimbas", null = True)
	envio = models.ForeignKey(Envio,on_delete = models.CASCADE)
	stock = 0
	def add_stock(self,amount):
		self.stock += amount 
	def subtract_stock(self,amount):
		self.stock -= amount


