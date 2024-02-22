from django.shortcuts import render,HttpResponse,loader
from .serializer import TeacherSerializer
import json
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


@api_view(['GET'])
def viewDB(request):
    teacherDB = User.objects.all().values()
    serializerobj = TeacherSerializer(teacherDB, many=True)
    return Response(serializerobj.data)


class HomeView(APIView):
    #permission_classes = (IsAuthenticated, )
    
    def post(self,request):
        content = {
            'message' : 'Welcome to the JWT Authentication page usign React Js and Django!'
            
        }
        return Response(content)
    
class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
          try:
               #print(request.data)
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               print(e)
               return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def Commit(request):
      
    print('called in PUT method')
    data = json.loads(request.body.decode("utf-8"))
    #print(data)
    #hashedpassword = make_password(data['password'])
    #print('hashed one is -:', hashedpassword)
    mydata = User.objects.filter(email=data['email'],number=data['number'],password=data['password']).values()
    
    if len(mydata) > 0 :
        print(len(mydata))
        content = {
            'exists' : True,
        }
        return JsonResponse(json.dumps(content), safe=False)
    
    elif len(mydata) == 0:
        newUser = User(name= data['name'], email= data['email'],password= data['password'], number = data['number'])
        newUser.save()
        print('written')
        content = {
            'exists': False,
            'response' : 'success'
        }
        return JsonResponse(json.dumps(content), safe=False)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def UserData(request):
        print('called in POST method')
        data = json.loads(request.body.decode("utf-8"))
        #print('data is', data)
        print('text psscode - ', data['password'])
        #hashedsinguppassword = make_password(data['password'])
        #print('hashed signup pass- ',hashedsinguppassword)
        mydata = User.objects.filter(name=data['username'],password=data['password']).values()
        
        datadisp = TeacherSerializer(mydata, many=True)
        print(datadisp.data)
        if mydata :
            content = {
                'found' : True,
                'profile' : datadisp.data
            }
            
            return JsonResponse(json.dumps(content), safe=False)
            
        content = {
                'found' : False
            }
        return JsonResponse(json.dumps(content), safe=False)
        
    