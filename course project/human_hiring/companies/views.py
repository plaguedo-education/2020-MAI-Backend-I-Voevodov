from django.http.response import JsonResponse
from django.shortcuts import render


# Create your views here.
def companies_list(request):
    if request.method == 'GET':
        return JsonResponse({
            'companies': [
                {
                  'ID': '00112233-4455-6677-8899-aabbccddeeff',
                  'name': 'ООО "Сладкий Пирожок"',
                  'logo': 'http://pic-cream.ru/pie.jpeg',
                  'number_of_vacancies': 2 
                },
                {
                  'ID': '00112233-4455-6677-8899-aabbccddeeff',
                  'name': 'ООО "Шоколадный глаз"',
                  'logo': 'http://pic-cream.ru/eye.png',
                  'number_of_vacancies': 4 
                },
                {
                  'ID': '00112233-4455-6677-8899-aabbccddeeff',
                  'name': 'ИП "Биба и Боба"',
                  'logo': 'http://pic-cream.ru/guys.jpeg',
                  'number_of_vacancies': 10 
                },
            ]
        })

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
