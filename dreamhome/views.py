from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class BranchView(APIView):
    def get(self, request):
        queryset = Branch.objects.all()
        serializer = BranchSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BranchSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status = status.HTTP_400_BAD_REQUEST)

class BranchDetail(APIView):
    def get_object(self, id):
        try:
            return Branch.objects.get(branch_no = id)
        except Branch.DoesNotExist:
            raise Http404

    def get(self, request, id):
        queryset = self.get_object(id)
        serializer = BranchSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, id):
        queryset = self.get_object(id)
        serializer = BranchSerializer(queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)