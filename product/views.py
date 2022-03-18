# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import BertTokenizer, BertForSequenceClassification
from DICE_mvp.disasterr.test import run_test

@api_view(["POST"])
def InferenceAPI(request):
    text = request.data.get('text')
    output = run_test(text)
  
    return Response({'MESSAGE':output}, status=201)


@api_view(["GET"])
def TestAPI(request):
    dummy = {
        'name': '죠르디',
        'type': '공룡',
        'job': '편의점알바생',
        'age': 5
    }
    
    return Response(dummy)

