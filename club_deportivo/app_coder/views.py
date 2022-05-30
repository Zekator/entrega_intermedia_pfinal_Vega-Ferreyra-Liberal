from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse, request
from django.template import loader
from app_coder.models import Sport, Partner, Profesor
#from app_coder.forms import SportForm, ProfesorForm, PartnerForm


# Create your views here.

def index(request):
    return render(request, "app_coder/index.html")


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