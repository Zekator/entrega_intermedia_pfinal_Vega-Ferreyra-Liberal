from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse, request
from django.template import loader
from app_coder.models import Sport, Partner, Profesor, Contact_us
from app_coder.forms import SportForm, ProfesorForm, PartnerForm


# Create your views here.

def index(request):
    return render(request, "app_coder/home.html")


def profesors(request):
    profesors = Profesor.objects.all()

    context_dict = {
        'profesors': profesors
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/profesors.html"
    )


def partner(request):
    partners = Partner.objects.all()

    context_dict = {
        'partners': partners
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/partners.html"
    )


def sport(request):
    sports = Sport.objects.all()

    context_dict = {
        'sports': sports
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/sport.html"
    )
    

def contact_us(request):
    contact_us = Contact_us.objets.all()
    

def profesorsFormulario(request):
    return render(request, "app_coder/cursoFormulario.html")


def profesor_forms_django(request):
    if request.method == 'POST':
        profesor_form = ProfesorForm(request.POST)
        if profesor_form.is_valid():
            data = profesor_form.cleaned_data
            profesor = Profesor(
                name=data['name'],
                last_name=data['last_name'],
                email=data['email'],
                profession=data['profession'],
            )
            profesor.save()

            profesors = Profesor.objects.all()
            context_dict = {
                'profesors': profesors
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/profesors.html"
            )

    profesor_form = ProfesorForm(request.POST)
    context_dict = {
        'profesor_form': profesor_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/profesor_django_forms.html'
    )