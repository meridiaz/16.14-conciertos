from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Contenido, Comentario

formulario_contenido = """
<br>
<form action="" method="POST">
  Introduce el (nuevo) contenido para esta página: 
  <input type="text" name="valor">
  <input type="submit" value="Enviar">
</form>
"""

@csrf_exempt
def get_content(request, llave):
    if request.method == "PUT":
        valor = request.body.decode('utf-8')           
    elif request.method == "POST":
        valor = request.POST['valor']             
    if request.method in ["PUT", "POST"]:
        try:
            c = Contenido.objects.get(clave=llave)
            c.valor = valor
        except Contenido.DoesNotExist:
            c = Contenido(clave=llave, valor=valor)
        c.save()

    contenido = get_object_or_404(Contenido, clave=llave)
    return HttpResponse(contenido.valor + formulario_contenido)
