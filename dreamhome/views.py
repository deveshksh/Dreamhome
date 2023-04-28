from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.db.models import Q

#1 BRANCH VIEW
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


#2 CLIENT VIEW
class ClientView(APIView):
    def get(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDetail(APIView):
    def get_object(self, client_no):
        try:
            return Client.objects.get(clientno=client_no)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, id):
        queryset = self.get_object(id)
        serializer = ClientSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, id):
        queryset = self.get_object(id)
        serializer = ClientSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


#3 STAFF VIEW --------------------------------------------------------------------------------------------------------------------------------
class StaffList(APIView):
    def get(self, request, branch_no = None):
        if branch_no:
            queryset = Staff.objects.filter(branch_no = branch_no)
            serializer = StaffSerializer(queryset, many = True)
            return Response(serializer.data)
        queryset = Staff.objects.all()
        serializer = StaffSerializer(queryset, many = True)
        return Response(serializer.data)
    def manager_exists(self, branchno):
        if Staff.objects.filter(pos = "Manager", branch_no = branchno).exists():
            return True
        return False
    def post(self, request):
        serializer = StaffSerializer(data= request.data)        
        if serializer.is_valid():
            if self.manager_exists(serializer.validated_data["branch_no"]) and serializer.validated_data["pos"] == "Manager":
                return Response({"error": "Manager already exists"}, status = status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        return Response(status = status.HTTP_400_BAD_REQUEST)

class StaffByBranch(APIView): #STAFF LISTING ------------------------------------------------------------------------------------------------------
    def get_object(self, branch_no):
        try:
            return Branch.objects.get(branch_no = branch_no)
        except Branch.DoesNotExist:
            raise Http404
    def get_manager(self, branch_no):
        try:
            return Staff.objects.get(branch_no = branch_no, pos = "Manager")
        except Staff.DoesNotExist:
            raise Http404
    def get(self, request, branch_no):
        queryset1 = self.get_object(branch_no)
        queryset2 = Staff.objects.filter(branch_no = branch_no)
        print(queryset2)
        data = {
            "branch": queryset1,
            "staff": queryset2
        }
        manager = self.get_manager(branch_no = branch_no)
        serializer = StaffByBranchSerializer(data)

        serialized_data = serializer.data
        serialized_data["manager_name"] = manager.fname + " " + manager.lname
        return Response(serialized_data)


#4 PRIVATE OWNER VIEW
class PrivateOwnerList(APIView):
    def get(self, request):
        queryset = Privateowner.objects.all()
        serializer = PrivateOwnerSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PrivateOwnerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status = status.HTTP_400_BAD_REQUEST)

class PrivateOwnerDetail(APIView):
    def get_object(self, ownerno):
        try:
            return Privateowner.objects.get(ownerno=ownerno)
        except Privateowner.DoesNotExist:
            raise Http404

    def get(self, request, id):
        queryset = self.get_object(id)
        serializer = PrivateOwnerSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, id):
        queryset = self.get_object(id)
        serializer = PrivateOwnerSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#5 PROPERTY VIEW
class PropertyforrentView(APIView):
    def get(self, request):
        queryset = Propertyforrent.objects.all()
        serializer = PropertyforrentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PropertyforrentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyforrentDetail(APIView):
    def get_object(self, property_no):
        try:
            return Propertyforrent.objects.get(propertyno=property_no)
        except Propertyforrent.DoesNotExist:
            raise Http404

    def get(self, request, id):
        queryset = self.get_object(id)
        serializer = PropertyforrentSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, id):
        queryset = self.get_object(id)
        serializer = PropertyforrentSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PropertyByBranch(APIView): #----------------------------------------------------------------------------------
    def get_object(self, branch_no):
        try:
            return Branch.objects.get(branch_no = branch_no)
        except Branch.DoesNotExist:
            raise Http404
    def get(self, request, branch_no):
        queryset1 = self.get_object(branch_no)
        queryset2 = Propertyforrent.objects.filter(regbranch = branch_no, rent_status = 0)
        data = {
            "branch": queryset1,
            "property": queryset2
        }
        manager = Staff.objects.get(branch_no = branch_no, pos = "Manager")
        serializer = PropertyByBranchSerializer(data)

        serialized_data = serializer.data
        serialized_data["manager_name"] = manager.fname + " " + manager.lname
        return Response(serialized_data)

class ViewPropertyReport(APIView):
    def get(self, request):
        queryset = ViewReport.objects.all()
        serializer = ViewReportSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ViewReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViewPropertyReportListing(APIView):
    def get_object(self, property_no):
        try:
            return Propertyforrent.objects.get(propertyno=property_no)
        except Propertyforrent.DoesNotExist:
            raise Http404
        
    def get(self, request, property_no):
        queryset1 = ViewReport.objects.filter(propertyno = property_no)
        queryset2 = self.get_object(property_no)
        data = {
            "report": queryset1,
            "property": queryset2
        }
        serializer = ViewReportByPropertySerializer(data)

        serialized_data = serializer.data
        for report in serialized_data["report"]:
            # clientno = report["cli    entno"]
            client = Client.objects.get(clientno = report["clientno"])
            report["clientName"] = client.fname + " " + client.lname
        return Response(serialized_data)

class MatchProperty(APIView):
    def get_object(self, property_no):
        try:
            return Propertyforrent.objects.get(propertyno=property_no)
        except Propertyforrent.DoesNotExist:
            raise Http404
    def get(self, request, propertyno):
        property = self.get_object(property_no = propertyno)
        clients = Client.objects.filter(regbranch = property.regbranch, maxrent__gt = property.rent, preftype = property.proptype)
        data = {
            "property": property,
            "client": clients
        }
        serializer = MatchingSerializer(data)
        return Response(serializer.data)

class PreferenceList(APIView):
    def get(self, request):
        queryset = Preferences.objects.all()
        serializer = PreferenceSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PreferenceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status = status.HTTP_400_BAD_REQUEST)

class LeaseView(APIView):
    def get(self, request):
        queryset = Lease.objects.all()
        serializer = LeaseSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LeaseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status = status.HTTP_400_BAD_REQUEST)

class BranchSearchAPI(APIView):
    def get(self, request):
        search_query = request.query_params.get('q', '')
        results = Branch.objects.filter(Q(branch_no__icontains = search_query))
        serializer = SimpleBranchSerializer(results, many = True)
        serialized_data = serializer.data
        print(serialized_data)
        return Response(serializer.data)