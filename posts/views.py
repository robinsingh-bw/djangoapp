from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    filtered_posts = [i for i in posts if i['id'] in [4, 2, 7]]
    return render(request, 'posts/index.html', { 'posts': filtered_posts })
