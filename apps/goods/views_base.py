from django.views.generic.base import View
from django.http import  HttpResponse
import json
from django.forms.models import model_to_dict
from goods.models import Goods

class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()[:10]
        for good in goods:
            json_dict = {}
            json_dict = model_to_dict(good)
            json_list.append(json_dict)
        return  HttpResponse(json.dumps(json_list),content_type='application/json')