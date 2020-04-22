from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """My first APIView"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP functions as methods (get, put, post, patch, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your app logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})