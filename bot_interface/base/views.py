from django.shortcuts import render
from . import bot
# Create your views here.



somethings = []

def home(request):
    bot_response = None
    
    a = request.GET.get("response")
    
    
    
    
    
    if a:
        a = a.lower()
        if a == "exit":
            pass
        else:
            if  bot.greet(a) != None:
                bot_response = bot.greet(a)
                
            else:
                bot_response = bot.response(a)
                
    nothing = {"user":a,"bot":bot_response}
    somethings.append(nothing)
    print("lol : ",somethings)
    context = {
    
    "user_response":a,
    
    "bot_response":bot_response,
    "somethings":somethings,}
    


   
    return render(request,"base/home.html",context)

def about(request):
    return render(request,"base/about.html")

