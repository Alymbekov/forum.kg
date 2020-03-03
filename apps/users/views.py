from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .forms import UserRegistrationModelForm
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.category.models import Category

class UserRegistrationView(CreateView):
    form_class = UserRegistrationModelForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'

class TestListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users.html'

    def get_queryset(self):
       return self.model.objects.filter(username__icontains='dastan')
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


# def index(request):
#     objects = Object.objects.all()
#     return render(request, 'asd', {'objects': objects})


class CabinetView(LoginRequiredMixin, DetailView):
    model = User
    def get_object(self):
        return self.request.user
    
    
