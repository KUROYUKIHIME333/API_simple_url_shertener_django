import requests
from django.shortcuts import render
import qrcode
import base64
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@csrf_exempt
@api_view(['POST'])
def home(request):
    # short_url = None
    # qr_code_data =None
    if 'url' not in request.data:
        return Response({'error': 'URL non fournie'}, status=status.HTTP_400_BAD_REQUEST)
    
    original_url = request.data['url']

    # Shorten URL with an open source API
    response = requests.get(f'https://is.gd/create.php?format=simple&url={original_url}')

    if response.status_code != 200:
        return Response({'error': 'Erreur lors du raccourcissement de l\'URL'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    short_url = response.text  # La réponse contient l'URL raccourcie

    # Generate QR Code
    qr_img = qrcode.make(short_url)
    buffered = BytesIO()
    qr_img.save(buffered, format="PNG")
    qr_code_data = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return Response({'original_url': original_url, 'short_url': short_url, 'qr_code_data': qr_code_data})
