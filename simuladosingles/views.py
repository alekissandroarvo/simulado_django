from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Question
from .models import FillInBlank_by_topic

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'login.html')

def loginpage(request):
    return render(request, 'login.html')

def questionario(request):
    question_list = Question.objects.order_by("id")
    context = {
            "question_list": question_list,
        }
    return render(request, 'questionario.html')   
   
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
    
def logout_view(request):
    logout(request)
    return render(request, "logoutpage.html")

def simplecontinuouspresent(request):
    if request.user.is_authenticated:
        question_list = FillInBlank_by_topic.objects.filter(assunto="simplecontinuouspresent").order_by("id")
        question_list_questao2 = FillInBlank_by_topic.objects.filter(assunto="simplecontinuouspresentquestao2").order_by("id")
        question_list_questao3 = FillInBlank_by_topic.objects.filter(assunto="simplecontinuouspresentquestao3").order_by("id")
        question_list_questao4 = FillInBlank_by_topic.objects.filter(assunto="simplecontinuouspresentquestao4").order_by("id")

        context = {
                "question_list": question_list,
                "question_list_questao2": question_list_questao2,
                "question_list_questao3": question_list_questao3,
                "question_list_questao4": question_list_questao4,

            }       
        return render(request, 'simplecontinuouspresent.html',context)  
    else:
        return render(request, 'login.html')
        
        
def simplepresent(request):
    if request.user.is_authenticated:
        question_list = FillInBlank_by_topic.objects.filter(assunto="simplepresent").order_by("id")
        question_list_table= FillInBlank_by_topic.objects.filter(assunto="simplepresenttable").order_by("id")  
        question_list_q3= FillInBlank_by_topic.objects.filter(assunto="simplepresentQ3").order_by("id")  
        context = {
                "question_list": question_list,
                "question_list_table": question_list_table,
                "question_list_q3": question_list_q3,       
            }
        return render(request, 'simplepresent.html',context)
    else:
        return render(request, 'login.html')
        
    

def resultsimplepresent(request):
        if request.user.is_authenticated:
            question_list = FillInBlank_by_topic.objects.filter(assunto="simplepresent").order_by("id")
            question_list_table = FillInBlank_by_topic.objects.filter(assunto="simplepresenttable").order_by("id")
            question_list_q3= FillInBlank_by_topic.objects.filter(assunto="simplepresentQ3").order_by("id")  
            respostas = []    
            respostas_table = []
            respostas_q3 = []
            for answer in question_list:
                respostas.append(request.GET[str(answer.id)])
            for answer in question_list_table:
                respostas_table.append(request.GET[str(answer.id)])
            for answer in question_list_q3:
                respostas_q3.append(request.GET[str(answer.id)])
            context = {
                "question_list": zip(question_list,respostas),
                "question_list_table": zip(question_list_table,respostas_table),
                "question_list_q3":zip(question_list_q3,respostas_q3),
            }
            return render(request, 'resultsimplepresent.html',context)
        else:
            return render(request, 'login.html')
    

def resultsimplecontinuouspresent(request):
        if request.user.is_authenticated:
            question_list= FillInBlank_by_topic.objects.filter(assunto="simplecontinuouspresent").order_by("id")  
            question_list_questao2= FillInBlank_by_topic.objects.filter(assunto="simplecontinuouspresentquestao2").order_by("id")  
            question_list_questao3= FillInBlank_by_topic.objects.filter(assunto="simplecontinuouspresentquestao3").order_by("id")  
            question_list_questao4= FillInBlank_by_topic.objects.filter(assunto="simplecontinuouspresentquestao4").order_by("id")  

            respostas = []       
            respostas_questao2 = []
            respostas_questao3 = []
            respostas_questao4 = []
            for answer in question_list:
                respostas.append(request.GET[str(answer.id)])
            for answer in question_list_questao2:
                respostas_questao2.append(request.GET[str(answer.id)])
            for answer in question_list_questao3:
                respostas_questao3.append(request.GET[str(answer.id)])
            for answer in question_list_questao4:
                respostas_questao4.append(request.GET[str(answer.id)])
            context = {
                # "question_list": question_list,
                "question_list" :zip(question_list,respostas),
                "question_list_questao2" :zip(question_list_questao2,respostas_questao2),
                "question_list_questao3" :zip(question_list_questao3,respostas_questao3),
                "question_list_questao4" :zip(question_list_questao4,respostas_questao4),

            }
            return render(request, 'resultsimplecontinuouspresent.html',context)
        else:
            return render(request, 'login.html')
    
