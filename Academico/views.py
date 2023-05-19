from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages
# Create your views here.
def home(request):
    cursos = Curso.objects.all()
    messages.success(request,'Cursos Listados')
    return render(request,"gestionCursos.html", {"cursos":cursos})

def registrarCurso(request):
    cod=request.POST['txtCodigo']
    nom=request.POST['txtNombre']
    cred = request.POST['numCreditos']

    curso = Curso.objects.create(codigo=cod, nombre=nom,creditos= cred)
    messages.success(request,'Curso Registrado')
    return redirect('/')

def eliminarCurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request,'Curso Eliminado')
    return redirect('/')

def edicionCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'edicionCurso.html',{"curso":curso})

def editarCurso(request):
    cod=request.POST['txtCodigo']
    nom=request.POST['txtNombre']
    cred = request.POST['numCreditos']
    curso = Curso.objects.get(codigo=cod)
    curso.nombre = nom
    curso.creditos = cred
    curso.save()
    messages.success(request,'Curso Actualizado')
    return redirect('/')
