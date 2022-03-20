# Create your views here.
import os
import PIL
from PIL import Image 
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def GetTrainData(request):
    text= request.data.get("MODE")
    print(text)
    url=request.data.get("IMAGE")
    if text=="Train":
        output="train started"
    elif text=="Inference":
        output='inference started'
        task_url = "https://static.wixstatic.com/media/"
        url = task_url + url.split("/")[3]
        os.system("curl " + url + " > test.jpg")
        img = Image.open("test.jpg")

    else:
        output='Not supported mode...'
    return Response(({'MESSAGE':output},{'IMAGE':url}), status=201)


@api_view(["GET"])
def TestAPI(request):
    dummy = {
        'name': '죠르디',
        'type': '공룡',
        'job': '편의점알바생',
        'age': 5
    }
    
    return Response(dummy)

