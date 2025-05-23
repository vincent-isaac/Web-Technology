from django.shortcuts import render
from .models import participant
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    context = {}
    return render(request, 'event/home.html', context)

def register(request):
    context = {}

    if request.method == 'POST':
        p1=participant()
        p1.name = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.phone = request.POST.get('phone','000')
        p1.insitution = request.POST.get('insitution','-')

        if len(participant.objects.all()) > 5 :
            
            return render (request, 'event/failed.html',context)

        else:
            p1.save()
            return render (request, 'event/success.html',context)

    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['insitution'] = ''

    return render(request, 'event/register.html', context)

def listofparticipants(request):
    context = {}
    context['participant'] = participant.objects.all()
    return render(request, 'event/listofparticipants.html', context)
