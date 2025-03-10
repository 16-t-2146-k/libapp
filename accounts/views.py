from django.contrib.auth.forms import UserCreationForm
from django.urls import	reverse_lazy
from django.views import generic
from django.shortcuts import render



from .forms import CustomUserCreationForm
# Create your views here.
class SignUpView(generic.CreateView):
	form_class=CustomUserCreationForm
	success_url=reverse_lazy('login')
	template_name='accounts/signup.html'

def logout_view(request):
	return render(request,'accounts/logout.html')
