from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import render
from rest_framework.views import APIView,status
from .models import Variants, Registration, Role
from .serializers import VariantSerializer,RegistrationSerializer,RoleSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import UserAdmin, ObjAdmin
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        id =  validated_token.get("user_id")
        try:
            user = Registration.objects.get(id = id)
            user.is_authenticated = True
            return user
        except :
            return None

class RegisterView(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
        query=Registration.objects.all()
        serializer=RegistrationSerializer(query, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)  # Secure authentication

#         if user:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'access_token': str(refresh.access_token),
#                 'refresh_token': str(refresh)
#             }, status=status.HTTP_200_OK)
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LoginView(APIView): 
    permission_classes=[AllowAny]
    def post(self,request):  
        username= request.data.get('username') 
        password= request.data.get('password') 
        current_user= Registration.objects.get(username=username) 
        if current_user and (password==current_user.check_password(password)):
            refresh= RefreshToken.for_user(current_user) 
            refresh_token= str(refresh) 
            access_token= str(refresh.access_token)
            return Response({'access_token': access_token, 'refresh_token':refresh_token}, status= status.HTTP_201_CREATED)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ListView(APIView):
    permission_classes=[AllowAny]
    def get(self,request):
            query=Variants.objects.all()
            serializer=VariantSerializer(query, many=True)
            return Response(serializer.data)
        
class GetbyId(APIView):
    permission_classes=[AllowAny]
    def get(self,request,pk):
            query=Variants.objects.get(pk=pk)
            serializer=VariantSerializer(query)
            return Response(serializer.data)
    
class CreateView(APIView):
    authentication_classes=[CustomJWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
            query=Variants.objects.all()
            serializer=VariantSerializer(query, many=True)
            return Response(serializer.data)
        
    # def post(self, request):
    #     print("Authenticated User:", request.user)  # Debugging check
    #     serializer = VariantSerializer(data=request.data)
            
    def post(self, request):
        user=request.user
        serializer=VariantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(accessed_username=user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)        
      
# class UpdatedeleteView(APIView):
#     # permission_classes=[ObjAdmin]

#     def get(self,request,id):
#         query=Variants.objects.filter(id=id)
#         serializer=VariantSerializer(query, many=True)
#         return Response(serializer.data)
    
#     permission_classes=[ObjAdmin]

#     def put(self, request,id):
#         #permission_classes=[IsAuthenticated]
#         query=Variants.objects.get(id=id)
#         serializer=VariantSerializer(query, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     def delete(self,request,id):
#         #permission_classes=[IsAuthenticated]
#         query=Variants.objects.get(id=id)
#         query.delete()
#         return Response({"msg":"Deleted Successfully"},status = status.HTTP_204_NO_CONTENT)
    
class UpdatedeleteView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[CustomJWTAuthentication]
    permission_classes=[ObjAdmin]
    queryset=Variants.objects.all()
    serializer_class=VariantSerializer
    