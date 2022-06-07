from django.shortcuts import render
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse, request
from django.template import loader
from django.urls import reverse_lazy
from app_coder.models import Sport, Partner, Profesor
from app_coder.forms import SportForm, ProfesorForm, PartnerForm
from django.views.generic import UpdateView, CreateView, DeleteView,ListView,FormView


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
        template_name="app_coder/sports.html"
    )
    

def profesor_forms(request):
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
        'profesor_forms': profesor_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/profesor_forms.html'
    )

class ProfesorForm(FormView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor_forms'
    

class ProfesorList(ListView): 
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor_list'
        
    
class ProfesorCreate(CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor-create'
    success_url: reverse_lazy ('app_coder:profesor-list')

class ProfesorUpdate(UpdateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor-update'


class ProfesorDelete(DeleteView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesor-delete'

