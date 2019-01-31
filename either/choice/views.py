from django.shortcuts import render,redirect
from .models import Question,Comment
# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request,"choice/index.html",{"questions":questions})
    
def new(request):
    return render(request,"choice/new.html")
    
def create(request):
    title = request.POST.get("title")
    c1 = request.POST.get("c1")
    c2 = request.POST.get("c2")
    
    # 위의 코드 한줄로
    Question.objects.create(title=title,c1=c1,c2=c2)
    
    return redirect("/choices")
    
def read(request,id):
    question = Question.objects.get(pk=id)
    return render(request,"choice/read.html",{"question":question})
    
def delete(request,id):
    question = Question.objects.get(pk=id)
    question.delete()
    
    return redirect("/choices")
    
def edit(request,id):
    question = Question.objects.get(pk=id)
    return render(request,"choice/edit.html",{"question":question})   

def update(request,id):
    question=Question.objects.get(pk=id)
    title=request.POST.get("title")
    c1=request.POST.get("c1")
    c2=request.POST.get("c2")
    
    
    question.title = title
    question.c1= c1
    question.c2= c2
    question.save()
    
    return redirect(f"/choices/{id}")    
    
def comment_create(request,id):
    question = Question.objects.get(pk=id)
    content = request.POST.get("content")
    c1Cnt = request.POST.get("c1")
    c2Cnt = request.POST.get("c2")
    if c1Cnt == "1" : 
        question.c1Cnt += 1
        question.save()
    else : 
        question.c2Cnt += 1
        question.save()   
        
    Comment.objects.create(question = question, content=content)
    # from 
    
    
    return redirect(f"/choices/{id}/")