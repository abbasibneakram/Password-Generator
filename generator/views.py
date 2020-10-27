from django.shortcuts import render
import random

def home(request):
    return render(request,'generator/home.html')

def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyu')
    
    if request.GET.get('upper'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+}{":?><'))

    if request.GET.get('number'):
        characters.extend(list('1234567890'))

    length=int(request.GET.get('length'))
    
    passw=""

    for i in range(length):
        passw+=random.choice(characters)



    return render(request,'generator/password.html',{'password':passw})