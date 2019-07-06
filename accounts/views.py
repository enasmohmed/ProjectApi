from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.


"""def signup_view(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
        #log in the user
            return redirect('/')

    else:
        form = UserCreationForm

    context = {
        'form' : form ,
    }

    return render(request, 'accounts/signup.html', context )   
   
"""


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            
        #log in the user
            return redirect('Post:all_posts')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})   




def logout_request(request):
    logout(request)
    return redirect('/')