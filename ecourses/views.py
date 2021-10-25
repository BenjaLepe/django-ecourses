from django.shortcuts import render
from .models import Course, Exam, Student
from .parametros import UNIVERSIDAD
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .user.user import register


def index(request):
    cursos = Course.objects.all()
    context = {'cursos': cursos, 'user': request.user}
    return render(request, 'ecourses/home.html', context)


def create_user(request):
    if request.method == "POST":
        context = register(request)
        if context:
            return render(request, 'ecourses/signin.html', context)
        else:
            return account(request)

    else:
        context = {'universidades': UNIVERSIDAD}
        return render(request, 'ecourses/signin.html', context)


@login_required
def new_exam(request):
    cursos = Course.objects.all().filter(student=request.user.student)


def log_in(request):
    print("login")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('account'))
        else:
            request.method = 'GET'
            return render(request, 'ecourses/login.html', {'error': "No hay coincidencias con el nombre de usuario y la contraseña"})
    return render(request, 'ecourses/login.html', {'error': None})


@login_required
def show_course(request, course="Curso"):
    curso = Course.objects.get(student=request.user.student, name=course)
    exams = curso.exam_set.all()
    context = {'curso': curso, 'exams': exams}
    return render(request, 'ecourses/course.html', context)


@login_required
def add_course(request):
    if request.method == "POST":
        dt = datetime.today()
        if dt.month <= 6:
            semestre = 1
        else:
            semestre = 2
        curso = Course(student=request.user.student,
                       name=request.POST["name"],
                       semester=semestre,
                       year=dt.year)
        curso.save()
        return HttpResponseRedirect(reverse('account'))


@login_required
def edit_exam(request, course, exam):
    curso = Course.objects.get(student=request.user.student, name=course)
    exam = Exam.objects.get(course=curso, id=exam)
    exam.score = request.POST["calificacion"]
    exam.save()
    suma = 0
    p_final = 0
    for exam in curso.exam_set.all():
        if exam.score > 0:
            suma += exam.score*exam.ponderacion
            p_final += exam.ponderacion
    curso.promedio = round(suma/p_final,2)
    curso.save()
    return HttpResponseRedirect(reverse('showcourse',  kwargs={'course':course}))

@login_required
def add_exam(request, course="Curso"):
    curso = Course.objects.get(student=request.user.student, name=course)
    nombre = request.POST["name"]
    ponderacion = request.POST["ponderacion"]
    exam = Exam(course=curso, name=nombre, score=0, ponderacion=ponderacion)
    exam.save()
    return HttpResponseRedirect(reverse('showcourse',  kwargs={'course':curso.name}))

@login_required
def account(request):
    cursos = Course.objects.all().filter(student=request.user.student)
    context = {'user': request.user, 'cursos': cursos}
    return render(request, 'ecourses/account.html', context)


@login_required
def log_out(request):
    print(log_out)
    logout(request)
    return render(request, 'ecourses/home.html', {})
