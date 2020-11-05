from django.db import models

# Create your models here.
class Producto(models.Model):
	color = models.CharField(max_length = 200)
	dibujo = models.CharField(max_length = 200)
	diseño_especial = models.BooleanField(default=False)
	precio_venta = models.IntegerField()
	image = models.ImageField(upload_to = "imagenes_kalimbas", null = True)
	stock = 0
	def add_stock(self,amount):
		self.stock += amount 
	def subtract_stock(self,amount):
		self.stock -= amount


