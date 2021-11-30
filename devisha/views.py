from .models import Devi
from django.shortcuts import render,redirect,get_object_or_404
from .forms import Devisha

# Create your views here.
def index(request):
    return render(request, 'devisha/index.html')
def base(request):
    return render(request, 'devisha/base.html')
def signup(request):
    if request.method == 'GET':
        return render(request, 'devisha/signup.html', {'form': Devisha()})
    else:
        try:
            form = Devisha(request.POST)
            newdevisha = form.save(commit=False)
            newdevisha.save()
            return redirect('signup')
        except ValueError:
            return render(request, 'devisha/signup.html', {'form': Devisha()})

def record(request):
    user1 = Devi.objects.filter()
    #user1 = Devi.objects.all
    return render(request, 'devisha/record.html', {'user1': user1})
def login(request):
    return render(request, 'devisha/login.html')
def display(request, page):
    x = get_object_or_404(Devi, pk=page)
    if request.method =="GET":
        form = Devisha(instance=x)
        return render(request, 'devisha/display.html', {'x':x, 'form':form})
    else:
        try:
            form = Devisha(instance=x)
            form.save()
            return redirect('record')
        except ValueError:
            return render(request, 'devisha/display.html', {'x': x, 'form': form})









