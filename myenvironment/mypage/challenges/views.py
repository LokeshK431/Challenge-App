from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


monthly_challenges = {
    "january": "Take extra precautions in cold climate.",
    "february": "Stay focused & put on jackets everyday and everywhere.",
    "march": "Dont over eat, You are obese!",
    "april": "Explore new opportunities!",
    "may": "Explore new skills & acquire them.",
    "june": "Get moving, the world never stops. Grab the vulnerable shops and try to handle it.",
    "july": "Adore the forthcoming challenges!",
    "august": "maja nahi aah raha, Push harder!",
    "september": "Set your goals right and very precise.",
    "october": "Set your priorities right.",
    "november": "Stay Calm! Meditate!",
    "december": "Break into the shadows!",
}

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month!")
    
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('Not supported!')