from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .process import *
import requests

class ProcessView(APIView):
    parser_class = (JSONParser,)

    @csrf_exempt
    def post(self, request): 
        download_url = request.data['downloadUrl']
        access_token = request.data['accessToken']

        s3_url = None
        for i in range(0, 10):
            try:
                resp = requests.get(url=download_url, headers={'Authorization':'Bearer ' + access_token})
                s3_url = resp.json()['download_url']
            except:
                continue
            break
        df = process(s3_url)
        return Response({"output": df.to_json(orient='records')}, status=status.HTTP_200_OK)
