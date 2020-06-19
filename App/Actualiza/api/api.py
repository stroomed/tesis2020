from rest_framework.response import Response
from .serializers import UserSerializer
from .serializers import PostForm
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render

class UserAPI(APIView):
    def post(self, request):
        serializer = UserSerializer( data = request.data )
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


def base(request):
    return render(request, 'templates/index.html')

def login(request):
    return render(request, 'templates/login.html')

def historial(request):
    return render(request, 'templates/historial.html')
    
def UserRegister(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'templates/register.html',{'form':form})

