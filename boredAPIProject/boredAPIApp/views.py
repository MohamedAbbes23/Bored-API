from django.shortcuts import render
import requests





def boredAPIView(request):
    url ="https://www.boredapi.com/api/activity"
    response = requests.get(url)
    data = response.json()
    activity =  data['activity']                 
    return render(request, 'home.html', {'activity':activity})