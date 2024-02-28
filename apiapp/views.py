from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView

class StudentView(APIView):
    def get(self, request, stud_id=None):
        if stud_id is not None:
            student = Student.objects.get(stud_id=stud_id)
            serializer=StudentSerializer(student)
            return Response(serializer.data)
        students = Student.objects.all()
        serializers = StudentSerializer(students, many =True)
        return Response(serializers.data)
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesg ': 'saved successfully'})
        return Response({'mesg': 'not saved error'})
    def put(self,request, stud_id):
        student=Student.objects.get(stud_id=stud_id)
        serializer=StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesg':'updated mesage'})
    def delete(self,request,stud_id):
        student=Student.objects.get(stud_id=stud_id)
        student.delete()
        return Response({'mesg':'deleted'})