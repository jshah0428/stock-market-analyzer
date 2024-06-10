from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout

def signup_form(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            #you have to log the user in.
            return render(request,'accounts/signup_successful.html') #specifically to the list article in the articles app, this is name spaced.
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html',{'form':form})

def login_form(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #login the user.
            user = form.get_user()
            login(request, user)
            #this code should be checked after already checking the post request, so that it makes more sense.
            if 'next' in request.POST:
                return(redirect(request.POST.get('next')))
            else:
                return redirect('stock_information:stock_info') # you only want this to happen if the validation is correct.
    else:
        form = AuthenticationForm()
    #supposed to work, but does not, do the is_aunticate thing

    return render(request, 'accounts/login.html', {'form':form})

def logout_form(request):
    if request.method =='POST':
        logout(request)#this already gets rid of all the session data, which means request.sessions is already empty.
        return render(request,'accounts/logout_successful.html')
