from django.shortcuts import render,redirect
from .serializers import AlumnosSerializers,InstitucionSerializers
from .models import Alumnos, Institucion
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from NASHEAPP.forms import FormAlumnos


def veralumnos(request):
    alum = Alumnos.objects.all()
    data = {'Alumnos': list(alum.values('id','nombre','telefono','fechainscripcion','institucion','hora','estado','observacion'))}
    return JsonResponse(data)





class AlumnosLista(APIView):
    def get(self, request):
        alum = Alumnos.objects.all()
        serial = AlumnosSerializers(alum, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = AlumnosSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class AlumnosDetalle(APIView):
    def get_object(self, pk):
        try:
            return Alumnos.objects.get(pk=pk)
        except Alumnos.DoesNotExist:
            return Http404

    def get(self, request, pk):
        alum = self.get_object(pk)
        serial = AlumnosSerializers(alum)
        return Response(serial.data)

    def put(self, request, pk):
        alum = self.get_object(pk)
        serial = AlumnosSerializers(alum, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(status=status.HTTP_204_NO_CONTENT)                                
    


def index(request):
    return render(request, 'index.html')

def listar_Inscripciones(request):
    ins = Alumnos.objects.all()
    data = {'inscripcion': ins}
    return render(request, 'listar_inscripcion.html', data)

def agregar_inscripcion(request):
    form = FormAlumnos()
    if request.method == 'POST':
        form = FormAlumnos(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_inscripcion.html', data)

def eliminar_inscripcion(request, id):
    ins = Alumnos.objects.get(id = id)
    ins.delete()
    return redirect( '/listar')

def actualizar_inscripcion(request, id):
    ins = Alumnos.objects.get(id = id)
    form = FormAlumnos(instance=ins)
    if request.method == 'POST':
        form = FormAlumnos(request.POST, instance=ins)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregar_inscripcion.html', data)   


@api_view (['GET', 'POST'])
def InstitucionLista(request):
    if request.method == 'GET':
        estu = Institucion.objects.all()
        serial = InstitucionSerializers(estu, many=True)
        return Response(serial.data)
        
    if request.method == 'POST':
        serial = InstitucionSerializers(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def InstitucionDetalle(request, pk):
    try:
        estu = Institucion.objects.get(id=pk)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serial = InstitucionSerializers(estu)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = InstitucionSerializers(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
