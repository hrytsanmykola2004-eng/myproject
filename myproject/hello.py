from django.http import HttpResponse

from django.shortcuts import render

def hello(request):
    return render (request, "hello.html")

def reverse(request):
   
    user_text = request.GET.get("usertext", "")
    reversed_text = user_text[::-1]
    word_count = len(user_text.split())
    return render(request, "reverse.html", {
        "original_text": user_text,
        "reversed_text": reversed_text,
        "word_count": word_count,
    })
    
