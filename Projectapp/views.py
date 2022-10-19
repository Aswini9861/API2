from email import message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Projectapp import serializers
from rest_framework import viewsets
from Projectapp import models
from rest_framework.authentication import TokenAuthentication
from Projectapp import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated



class HelloApiviews(APIView):
    '''test API view'''
    serializer_class=serializers.HelloSerializer


    def get(self,request,format=None):
        '''return a list o APIview feacture'''
        an_apiview=[
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLS'
        ]

        return Response({'message':'hello','an_apiviews':an_apiview})



    def post(self,request):
        '''create a hello message with our name'''
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )


    def put(self,request,pk=None):
        '''handle updating an object'''
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        '''handle partial updating an object'''
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        '''delete an object'''
        return Response({"method":'DELETE'}) 


class HelloViewSet(viewsets.ViewSet):
    '''test API viewset'''

    serializer_class=serializers.HelloSerializer


    def list(self,request):
        '''return a hello message'''
        a_viewset=[
            'Uses action (list,create,retrive,update,partial_update)',
            'Automatically maps URLS using Router',
            'Provides more functionality with less code',

        ]
        return Response({'message':'hello','a_viewset':a_viewset})

    def create(self,request):
        '''create a new hello message'''
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        '''handle getting an object by id'''
        return Response({"http_method":'GET'})

    def update(self,request,pk=None):
        '''handle updating an object'''
        return Response({"http_method":'PUT'})

    def partial_update(self,request,pk=None):
        '''handle an object part of an object'''
        return Response({"http_method":'PATCH'})

    def destroy(self,request,pk=None):
        '''delete an object'''
        return Response({"http_method":'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    '''models creating and updating profiles '''
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email')


class UserLoginApiView(ObtainAuthToken):
    '''Handle creating user authentication token'''
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES



class UserProfileFeedViewSet(viewsets.ModelViewSet):
    '''Handle creating reading and updating profile feed item'''
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.ProfileFeedItemSerializer
    queryset=models.ProfileFeddItem.objects.all()
    permission_classes=(permissions.UpdateOwnStatus,IsAuthenticated)



    def perform_create(self, serializer):
        '''sets the user profile to the logged user'''
        serializer.save(user_profile=self.request.user)
        

