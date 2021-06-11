from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Item

@csrf_exempt
def get_greeting(request):
    
    name = request.POST.get('name')
    result = f"{name}님 안녕하세요"
    print(result)
    # return HttpResponse(result)
    result_dict = dict(result=result)
    return JsonResponse(result_dict) #Dictionary나 List를 JSON 문자열로 변환해서 응답.


from django.core import serializers

@csrf_exempt
def get_item_by_id(request):
    # item_id = request.POST.get('item_id')
    item_no = request.POST.get('item_no')
    print(item_no)
    item = Item.objects.get(pk=item_no)  #JSON Serializer를 위해 QuerySet으로 조회한다.
    result = parsing_item_to_json()
    # result = serializers.serialize('json', item) # [{"model": "api.item", "pk": "id-1", "fields": {"item_name": "제품-1", "item_price": 119000}}]
    
    return JsonResponse(result) #QuerySet은 변환안됨.

@csrf_exempt
def get_item_list(request):
    items = Item.objects.all()
    result = []
    for item in items:
        result.append(parsing_item_to_json(item))
        
    return JsonResponse(result, safe=False) #Dictionary 이외에는 safe=False로 준다.

def parsing_item_to_json(model):
    result = {
        "item_no":model.pk,
        "item_name":model.item_name,
        "item_price":model.item_price
    }
    return result