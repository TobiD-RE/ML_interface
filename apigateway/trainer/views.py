from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import requests
# Create your views here.

class TrainModelProxyView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        dataset_source = request.data.get('datasetSource')
        algorithm = request.data.get('algorithm')
        dataset_url = request.data.get('datasetUrl')
        dataset_file = request.FILES.get('datasetFile')

        proxy_url = 'http://localhost:8001/train-model/'

        data = {
            'datasetSource': dataset_source,
            'algorithm': algorithm,
            'datasetUrl': dataset_url
        }

        files = {'datasetFile': dataset_file.file} if dataset_file else None

        try:
            response = request.post(proxy_url, data=data, files=files)
        except request.RequestException as e:
            return Response({'error': 'Failed to reach ML service', 'details': str(e)}, status=503)
        
        if response.status_code != 200:
            return Response({'error': 'ML service error', 'details': response.text}, status=response.status_code)
        
        return HttpResponse(response.content, content_type='application/octet-stream', headers={
            'Constent-Disposition': 'attachment; filename="model.pkl"'
        })