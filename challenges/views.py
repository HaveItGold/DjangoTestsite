from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthlyGoals = {
    "january":"Work on new year's resolution",
    "february":"Get a date for Valentine's day",
    "march":"Find a useful holiday",
    "april":"Celebrate your birthday in a cool way",
    "may":"Go outside more",
    "june":"Hang out with friends",
    "july":"Go to Spain",
    "august":"Don't cry when you go back to school",
    "september":"Make new friends",
    "october":"Don't do weird stuff in Spain",
    "november":"Order pumpkin spice latté",
    "december":"Have a merry Christmas"
}

def index(request):
    # dataToReturn = ""
    months = list(monthlyGoals.keys())
    # for i in months:
    #     monthPath = '/challenges/' + i
    #     dataToReturn += f"<li style='color:red'><a href='{monthPath}'>{i.capitalize()}</a></li>\n"
    # reponseData = f"<ul>{dataToReturn}</ul>"
    # return HttpResponse(reponseData)
    return render(request, 'challenges/index.html', {
        "months_key":months})

def monthlyGoalByNum(request, month):
    months = list(monthlyGoal.keys())
    if month > len(months) or month < 1:
        return HttpResponse(f"You entered an invalid numeric month")
    forwardMonth = months[month-1]
    return HttpResponseRedirect("/challenges" + forwardMonth)

def monthlyGoal(request, month):
    strToReturn =  ''
    try:
        strToReturn = monthlyGoals[month]
        return render(request, "challenges/challenge.html", {
            "text": strToReturn,
            "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound("<strong>ERROR ERROR! month not valid :(</strong>")