from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from drfapp.serializer import StudentSerializer
from drfapp.models import Student
from rest_framework.permissions import IsAuthenticated
class Test(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        serializer = StudentSerializer(Student.objects.all().last(),many=False)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)