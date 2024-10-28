from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Question
from .models import FillInBlank_by_topic

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
    answer_list_right_id=[]
    answer_list_wrong_assertiva=[]
    answer_list_right_assertiva=[]
    answer_list_wrong_id=[]
    i=1
    
    for answer in question_list:
        if answer.resposta == request.GET[str(i)]:
            answer_list_right_id.append( answer.id)             
        else:
            answer_list_wrong_id.append( answer.id)  
            answer_list_wrong_assertiva.append( request.GET[str(i)])
            answer_list_right_assertiva.append( answer.resposta)          
        i=i+1    
    context = {
        "answer_list_right": answer_list_right_id,
        "answer_list_wrong": zip(answer_list_wrong_id,answer_list_wrong_assertiva,answer_list_right_assertiva),
        "percent": (len(answer_list_right_id)/len(question_list))*100,
              
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

def questionario_topico(request):
    question_list = FillInBlank_by_topic.objects.order_by("id")
    context = {
        "question_list": question_list,
    }
    return render(request, 'simplecontinuouspresent.html',context)

def resultsimplecontinuouspresent(request):
    question_list= FillInBlank_by_topic.objects.order_by("id")    
    respostas = []    
    i=1
    for answer in question_list:
        respostas.append(request.GET[str(i)])
        i=i+1
    context = {
        # "question_list": question_list,
        "question_list" :zip(respostas,question_list),
    }
    return render(request, 'resultsimplecontinuouspresent.html',context)
