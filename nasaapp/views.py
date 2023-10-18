from django.shortcuts import render
import requests
import datetime
# Create your views here.
def home(request):
    today = datetime.date.today()
    if 'nasa' in request.POST:
        nasa = request.POST['nasa']
    else:
        nasa = today
    URL = 'https://api.nasa.gov/planetary/apod'
    key = 'Jpf8dmlqbwsVZLWw2fCFqKoVGS1w2cnAiNTYuRY3'
    params = {"date": nasa ,"api_key": key,"thumbs":True}
    response = requests.get(URL,params).json()
    title = response['title']
    description = response['explanation']
    picture = response['hdurl']
    return render(request,'home.html',{"date": nasa,"title":title,"picture":picture,"description": description})