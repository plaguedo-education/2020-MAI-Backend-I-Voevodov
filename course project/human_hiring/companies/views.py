from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Companie, Vacancy, Responses
from .serializers import CompanyCompactSerializer
from django.core import serializers

# Create your views here.
class CompaniesView(APIView):
    def get(self, request):
        companies = Companie.objects.all()
        companies_serialized = serializers.serialize('json', companies)
        return Response({"companies", companies_serialized})


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
