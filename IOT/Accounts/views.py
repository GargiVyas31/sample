from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def register(request):
	if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('Accounts:homepage')
    else:
        form = UserCreationForm()
    return render(request, 'Accounts/register.html', {'form': form})
	#return render(request,'Accounts/register.html')

def login(request):
	if request.method=='POST':
       form =  AuthenticationForm(data=request.POST)
       if form.is_valid():
           user=form.get_user()
           login(request,user)
           return redirect('Accounts:homepage')
    else:

        form = AuthenticationForm()
    return render(request,'Accounts/login.html',{'form':form})

	#return render(request,'Accounts/login.html')

def homepage(request):
	return render(request,'Accounts/homepage.html')