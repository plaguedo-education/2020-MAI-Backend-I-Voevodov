from django.shortcuts import render
from rest_framework.views import APIView
from django.template.response import TemplateResponse

class LoginView(APIView):
    def get(self, request):
        return render(request, 'login.html')
        #return TemplateResponse(request, 'login.html', {"user" : request.user})

class IndexView(APIView):
    def get(self, request):
        return render(request, 'base.html')

