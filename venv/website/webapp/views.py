from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import JobForm, ButtonForm
from careerjet_api_client import CareerjetAPIClient
from .models import Job
from .webscraper import getDescription

# Create your views here.


def home(request):
    return render(request, "webapp/home.html")


def findJob(request):
    if request.method == "POST":
        form = JobForm(request.POST)

        if form.is_valid():
            lc = form.cleaned_data["location"]
            kw = form.cleaned_data["keywords"]
            cj = CareerjetAPIClient("en_US")
            result_json = cj.search({
                'location': lc,
                'keywords': kw,
                'affid': '213e213hd12344552',
                'user_ip': '11.22.33.44',
                'url': 'http://127.0.0.1:8888/findJob/',
                'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
            })
            jobs = result_json["jobs"]
            all_jobs = []
            for i in jobs:
                job = Job()
                job.title = i["title"]
                job.company = i["company"]
                job.salary = i["salary"]
                job.location = i["locations"]
                job.url = i["url"]
                job.description = str(getDescription(job.url))
                all_jobs.append(job)
            return render(request, 'webapp/results.html/', {"jobs": all_jobs})
            # return redirect("/results/")
    else:
        form = JobForm()
    return render(request, 'webapp/findJob.html', {'form': form})


def results(request):
    return render(request, "webapp/results.html")


def favorites(request):
    return render(request, "webapp/favorites.html")
