from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiviews(APIView):
    '''test API view'''

    def get(self,request,format=None):
        '''return a list o APIview feacture'''
        an_apiview=[
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message':'hello','an_apiviews':an_apiview})