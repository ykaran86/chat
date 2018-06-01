from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from .models import Chat
from .models import Dialog
from .models import Number
from django.http import HttpResponse, JsonResponse
from datetime import datetime

@login_required
def home(request):
    c=Chat.objects.all()
    return render(request, 'home.html',{'home':'active','chat':c})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c= Chat(user=request.user, message=msg)
        myDate=datetime.now()
        formatedDate=myDate.strftime("%b %d, %Y, %I:%M %p")
        if msg !='':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username, 'time':formatedDate })
    else:
        return HttpResponse('Request must be POST.')
def Messages(request):
    c= Chat.objects.all()
    return render(request, 'messages.html', {'chat':c})
@login_required
def Dialogue(request):
    d=Dialog.objects.all()
    return render(request, 'Dialogue.html',{'Dialogue':'active','dialog':d})

def dialog(request):
    if request.method == "POST":
        dialog = request.POST.get('dialogbox', None)
        d = Dialog(user1=request.user, dialogue=dialog)
        myDate=datetime.now()
        formatedDate=myDate.strftime("%b %d, %Y, %I:%M %p")
        if dialog !='':
            d.save()
        i=Number.objects.all()
        if(len(i)!=0):
            i=Number.objects.last()
            i=i.number
            if(int(dialog)<i):
                dialog1 = "Nope! Guess a greater number."
                d1 = Dialog(user1=request.user, dialogue=dialog1, user2="fromComputer")
            elif(int(dialog)>i):
                dialog1 = "Nope! Guess a lesser number."
                d1 = Dialog(user1=request.user, dialogue=dialog1, user2="fromComputer")
            else:
                dialog1= "Yupp! you found the number."
                d1 = Dialog(user1=request.user, dialogue=dialog1, user2="fromComputer")
            d1.save()
            return JsonResponse({ 'dialog':dialog, 'user' : d.user1.username, 'time':formatedDate, 'dialog1':dialog1  })
        else:
            return JsonResponse({ 'dialog':dialog, 'user' : d.user1.username, 'time':formatedDate  })
    else:
        return HttpResponse('Request must be POST.')

    
def startconvo(request):
    if request.method == "POST":
        dialog = request.POST.get('dialogue', None)
        user2n = request.POST.get('user2name', None)
        numm = request.POST.get('num', None)
        d = Dialog(user1=request.user, dialogue=dialog, user2=user2n)
        n = Number(user=request.user, number=numm)
        myDate=datetime.now()
        formatedDate=myDate.strftime("%b %d, %Y, %I:%M %p")
        if dialog !='':
            d.save()
            n.save()
        return JsonResponse({ 'dialog':dialog, 'user' : d.user1.username, 'time':formatedDate, 'user2' : d.user2 })
    else:
        return HttpResponse('Request must be POST.')