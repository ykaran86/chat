from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm
from .models import Chat
from django.http import HttpResponse, JsonResponse

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
        msg = request.POST.get('chat-msg')
        c= Chat(user=request.user, message=msg)
        if msg !='':
            c.save()
        return redirect('home')
    else:
        return HttpResponse('Request must be POST.')
def Messages(request):
    c= Chat.objects.all()
    return render(request, 'messages.html', {'chat':c})
    
