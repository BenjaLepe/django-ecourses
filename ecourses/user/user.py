from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ..models import Course, Exam, Student
from ..parametros import UNIVERSIDAD


def register(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    universidad = request.POST['universidad']
    password = request.POST['password']
    # verificamos la cuenta
    context = verificar_cuenta(email, username)
    if context:
        return context

    user = User.objects.create_user(
        username=username, first_name=firstname, last_name=lastname, password=password, email=email)
    Student.objects.create(user=user)
    user.student.universidad = universidad
    user.save()
    if user:
        login(request, user)
        return None
    



def verificar_cuenta(email, username):
    try:
        User.objects.get(email=email)
        context = {'universidades': UNIVERSIDAD,
                    'error': "Ya existe una cuenta con este email"}
        return context
    except User.DoesNotExist:
        
        try: 
            User.objects.get(username=username)
            context = {'universidades': UNIVERSIDAD,
                        'error': "Ya existe una cuenta con este nombre de Usuario"}
            return context
        except User.DoesNotExist:
            return None



