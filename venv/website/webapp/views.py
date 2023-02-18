from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import JobForm
from careerjet_api_client import CareerjetAPIClient


# Create your views here.


def home(request):
    return render(request, "webapp/home.html")


def findJob(request):
    if request.method == "POST":
        form = JobForm(request.POST)

        if form.is_valid():
            data = request.POST
            lc = form.cleaned_data["location"]
            kw = form.cleaned_data["keywords"]
            cj = CareerjetAPIClient("en_GB")
            result_json = cj.search({
                'location': lc,
                'keywords': kw,
                'affid': '213e213hd12344552',
                'user_ip': '11.22.33.44',
                'url': 'http://www.example.com/jobsearch?q=python&l=london',
                'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
            })
            jobs = result_json["jobs"]
            title = []
            d = []
            for i in jobs:
                title.append(i['title'])
                d.append(i["description"])
            print(title)
            return render(request, 'webapp/results.html/', {'jobs': jobs, "t": title, "d": d, "j": jobs})
            # return redirect("/results/")
    else:
        form = JobForm()
    return render(request, 'webapp/findJob.html', {'form': form})


def results(request):
    l = request.POST
    return render(request, "webapp/results.html")
