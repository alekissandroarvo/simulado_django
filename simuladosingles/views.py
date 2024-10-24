from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Question

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def questionario(request):
    question_list = Question.objects.order_by("id")
    context = {
        "question_list": question_list,
    }
    return render(request, 'questionario.html',context)

def resultado_questionario(request):
    question_list= Question.objects.order_by("id")
    answer_list_right=[]
    answer_list_wrong=[]    
    i=1
    for answer in question_list:
        if answer.resposta == int(request.GET[str(i)]):
            answer_list_right.append( answer.id) 
        else:
            answer_list_wrong.append( answer.id)
        i=i+1    
    context = {
        "answer_list_right": answer_list_right,
        "answer_list_wrong": answer_list_wrong,
        "percent": (len(answer_list_right)/len(question_list))*100
        
    }
    return render(request, 'resultado_questionario.html',context)

def login_view(request):
    username = request.GET["name"]
    password = request.GET["senha"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request)
        context = {
            'nome': username.upper() ,
        }
        return render(request, "welcome.html",context)
    else:
        return render(request, "badlogin.html")
