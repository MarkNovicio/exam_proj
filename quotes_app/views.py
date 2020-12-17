from django.shortcuts import render, redirect
from django.contrib import messages
from login_app.models import *
from quotes_app.models import *

from .models import *

def success(request):
    if 'user_id' in request.session:

        context = {
            "user": Registration.objects.get(id = request.session['user_id'])
        }
        return render(request, "success.html", context)

    else:
        return redirect('/') #login page

def read_quotes(request):
    if 'user_id' in request.session:

        context = {
            "quotes": Quotes.objects.all(),
            "user": Registration.objects.get(id = request.session['user_id'])

        }
        return render(request, "quotes.html", context)
    else:    
        return redirect('/')

def create_quote(request):
           
    # validate message
    errors = Quotes.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print(errors)
        return redirect('/quotes')
    else:
        Quotes.objects.create(
            quote_author = request.POST['quote_author'],
            quote = request.POST['quote'],
            publisher = Registration.objects.get(id = request.session['user_id'])
        ) 
        return redirect('/quotes') 

def quote_profile(request, quote_id):
    context = {
        "quote": Quotes.objects.get(id=quote_id),
        
    }
    return render(request, "edit_quote.html", context)

def edit_quote(request, quote_id):
    quote = Quotes.objects.get(id =quote_id)
    errors = Quotes.objects.edit_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print(errors)

        return redirect(f'/quotes/{quote_id}')
    
    else:
        quote.quote_author = request.POST['quote_author']
        quote.quote = request.POST['quote']
        quote.save()
        return redirect('/quotes')


def favorite_quote(request, quote_id):
    quote =Quotes.objects.get(id=quote_id) #objtain instance of record
    user = Registration.objects.get(id=request.session['user_id'])
    
    quote.favorites.add(user)
    return redirect('/quotes')

def unfavorite_quote(request, quote_id):
    quote =Quotes.objects.get(id=quote_id) #objtain instance of record
    user = Registration.objects.get(id=request.session['user_id'])
    
    quote.favorites.remove(user)
    return redirect('/quotes')

def delete_quote(request, quote_id):
    delete_quote = Quotes.objects.get(id=quote_id)
    if delete_quote.publisher.id == request.session['user_id']:
        delete_quote.delete()

    return redirect('/quotes')

def user_profile(request, user_id):
    context = {
        "user": Registration.objects.get(id=user_id),
   
    }

    return render(request, "user_profile.html", context)


def logout(request):
    del request.session['user_id']
    return redirect('/')
