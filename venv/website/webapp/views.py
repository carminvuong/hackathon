from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import JobForm, ButtonForm
from careerjet_api_client import CareerjetAPIClient
from .models import Job
from .webscraper import getDescription, getSeeMore

# Create your views here.

fav = []


def home(request):
    return render(request, "webapp/home.html")


def findJob(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = JobForm(request.POST)
            if request.POST.get("favorite"):

                object_id = request.POST["favorite"]
                job_object = Job.objects.get(id=object_id)
                job_object.favorite = True
                fav.append(job_object)
                return HttpResponseRedirect('/favorites/')
            if request.POST.get("moreInfo"):

                object_id = request.POST["moreInfo"]
                job_object = Job.objects.get(id=object_id)
                description = getDescription(job_object.url)
                description = description.replace("<br/>", "\n")
                description = description.replace("<li>", " \n .")
                description = description.replace("</li>", "")
                description = description.replace("<b>", " ")
                description = description.replace("</b>", " ")
                job_object.fullDescription = description

                return render(request, "webapp/moreInfo.html/", {"job": job_object})

            elif form.is_valid():
                lc = form.cleaned_data["location"]
                kw = form.cleaned_data["keywords"]
                cj = CareerjetAPIClient("en_US")
                result_json = cj.search({
                    'location': lc,
                    'keywords': kw,
                    'affid': '213e213hd12344552',
                    'user_ip': '11.22.33.44',
                    'url': 'https://www.careerjet.com/search/jobs?s=Computer+Science&l=New+York',
                    'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
                })
                jobs = result_json["jobs"]
                all_jobs = []
                kw_list = "+".join(kw.split(" "))
                lc_list = "+".join(lc.split(" "))
                descriptions = getSeeMore(
                    f"https://www.careerjet.com/search/jobs?s={kw_list}&l={lc_list}")
                count = 0
                user = request.user
                for i in jobs:

                    job = Job()
                    job.user = user
                    job.title = i["title"]
                    job.company = i["company"]
                    job.salary = i["salary"]
                    job.location = i["locations"]
                    job.url = i["url"]
                    job.description = descriptions[count]
                    count += 1
                    all_jobs.append(job)
                    job.save()
                return render(request, 'webapp/results.html/', {"jobs": all_jobs,  "a": kw})
        else:
            form = JobForm()
        return render(request, 'webapp/findJob.html', {'form': form})
    else:
        return HttpResponseRedirect("/signup/")


def results(request):
    if request.user.is_authenticated:
        return render(request, "webapp/results.html")
    return HttpResponseRedirect("/signup/")


def favorites(request):
    if request.user.is_authenticated:
        return render(request, "webapp/favorites.html", {"fav": fav})
    return HttpResponseRedirect("/signup/")


def moreInfo(request):
    return render(request, 'webapp/moreInfo.html')
