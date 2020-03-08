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

        resp = requests.get(url=download_url, headers={'Authorization':'Bearer ' + access_token})
        if resp.status_code != 200:
            return Response({"message": "Error downloading file from CDrive"}, status=status.HTTP_400_BAD_REQUEST)
        s3_url = resp.json()['download_url']
        try:
            df = process(s3_url)
            return Response({"output": df.to_json(orient='records')}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({str(e), status=status.HTTP_400_BAD_REQUEST)
