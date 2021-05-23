from rest_framework.response import Response
from django.template.response import TemplateResponse
from rest_framework.views import APIView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# from django.core import serializers

from .models import Companie, Vacancy, Responses
from .serializers import CompanyCompactSerializer, CompanySerializer
from .forms import CompanyForm

# Create your views here.
class CompaniesView(APIView):
    def get(self, request):
        companies = Companie.objects.all()
        companies_serialized = CompanyCompactSerializer(companies, many=True)
        return Response({"companies": companies_serialized.data})

class CompaniesAllHtmlView(APIView):
    def get(self, request):
        companies = Companie.objects.all()
        companies_serialized = CompanyCompactSerializer(companies, many=True)
        return TemplateResponse(request, 'companies/list.html', {"companies": companies_serialized.data})

class CompanyDetailView(APIView):
    def get(self, request, pk):
        company = Companie.objects.get(id=pk)
        # TODO: BIG SEREILIZED
        company_serialized = CompanySerializer(company)
        # company_serialized = serializers.serialize('json', company)
        return Response({"company": company_serialized.data})

class CompanyNewView(APIView):
    @method_decorator(login_required)
    def get(self, request):
        form = CompanyForm()
        return TemplateResponse(request, 'companies/new.html', {'form': form})
    
    @method_decorator(login_required)
    def post(self, request):
        company_form = CompanyForm(request.POST, request.FILES)
        if company_form.is_valid():
            company = company_form.save()
            #
            return Response({"id": company.id})
        else:
            return

def companie_detail(request, pk):
    if request.method == 'GET':
        return JsonResponse({
            'ID': pk,
            'name': 'ООО "Сладкий Пирожок"',
            'logo': 'http://pic-cream.ru/pie.jpeg',
            'site': 'www.example.com',
            'description': '''
                Самая крутецкая и вкусненькая компания 
                на всём восточном побережье!
                Мммм, тут ТАААКИЕЕ вкусные булочки! Ум отъешь!
                Приходи к нам работать, у нас есть печеньки!
            ''',
            'number_of_vacancies': 2,
        })
