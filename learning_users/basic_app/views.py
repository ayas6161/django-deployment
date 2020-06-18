from django.shortcuts import render
from basic_app.forms import UserForms,UserProfleForms


from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate


# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def registration(request):
    registered=False

    if (request.method =='POST'):

        user_form=UserForms(data=request.POST)
        profile_form=UserProfleForms(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)

            profile=profile_form.save(commit=False)
            profile.user=user
            if('profile_pic' in  request.FILES):
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True
        else:
            print(profile_form.errors,user_form.errors)
    else:
        user_form=UserForms()
        profile_form=UserProfleForms()

    return render(request,'basic_app/registration.html',context={'user_form':user_form,'profile_form':profile_form,'registered':registered})



def user_login(request):

        if (request.method=='POST'):

            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username,password)

            user=authenticate(username=username,password=password)
            print(user)
            if user:
                if user.is_active:
                    login(request,user)
                    return(HttpResponseRedirect(reverse('index')))
                else:
                    return HttpResponse("The account is not active")

            else:
                print('Invalid credentials')
               
                return HttpResponse("Invalid credentials supplied'")


        else:
            return render(request,'basic_app/login.html')





        