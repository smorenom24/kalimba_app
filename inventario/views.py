from django.shortcuts import render
from inventario.models import *
# Create your views here.
def inventario(request):
	kalimbas = Producto.objects.all()
	if request.method == "GET":
		return render(request, "inventario/inventario.html", {"productos": kalimbas})
