from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.db.models import Q
from django.utils import timezone


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
    def get(self, request):
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
    
class StaffDetail(APIView):
    def get_object(self, id):
        try:
            return Staff.objects.get(staff_no = id)
        except Staff.DoesNotExist:
            raise Http404

    def get(self, request, id):
        queryset = self.get_object(id)
        serializer = StaffSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, id):
        queryset = self.get_object(id)
        serializer = StaffSerializer(queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

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
        data = {
            "branch": queryset1,
            "staff": queryset2
        }
        manager = self.get_manager(branch_no = branch_no)
        serializer = StaffByBranchSerializer(data)

        serialized_data = serializer.data
        serialized_data["manager_name"] = manager.fname + " " + manager.lname
        serialized_data["length"] = queryset2.count()
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

class   PropertyByBranch(APIView): #----------------------------------------------------------------------------------
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
        queryset2 = Propertyforrent.objects.filter(regbranch = branch_no, rent_status = 0)
        data = {
            "branch": queryset1,
            "property": queryset2
        }
        manager = self.get_manager(branch_no=branch_no)
        serializer = PropertyByBranchSerializer(data)

        serialized_data = serializer.data
        serialized_data["manager_name"] = manager.fname + " " + manager.lname
        serialized_data["ulength"] = queryset2.count()
        serialized_data["llength"] = Propertyforrent.objects.filter(regbranch = branch_no, rent_status = 1).count()
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
        active_leases = Lease.objects.filter(rent_finish__gt = timezone.now().date())
        property = self.get_object(property_no = propertyno)
        clients = Client.objects.filter(
            regbranch = property.regbranch, 
            maxrent__gt = property.rent, 
            preftype = property.proptype
        ).exclude(
            Q(leaseno__in=active_leases.values("leaseno")) &
            Q(leaseno__isnull=False)
        )
        data = {
            "property": property,
            "client": clients
        }
        serializer = MatchingSerializer(data)
        serialized_data = serializer.data
        serialized_data["length"] = clients.count()
        return Response(serialized_data)

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

class LeaseDetail(APIView):
    def get_object(self, leaseno):
        try:
            return Lease.objects.get(leaseno=leaseno)
        except Lease.DoesNotExist:
            raise Http404

    def get(self, request, leaseno):
        queryset = self.get_object(leaseno)
        serializer = LeaseSerializer(queryset)
        return Response(serializer.data)

    def delete(self, request, id):
        queryset = self.get_object(id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LeaseViewByActiveStatus(APIView):
    def get(self, request):
        today = timezone.now().date()
        inactive = Lease.objects.filter(rent_finish__lt = today)
        active = Lease.objects.filter(rent_finish__gt = today)
        data = {
            "active": active,
            "inactive": inactive
        }
        serializer = LeaseByActiveStatusSerializer(data)
        serialized_data = serializer.data
        for object in serialized_data["active"]:
            property = Propertyforrent.objects.get(propertyno = object["propertyno"])
            object["address"] = property.address
        for object in serialized_data["inactive"]:
            property = Propertyforrent.objects.get(propertyno = object["propertyno"])
            object["address"] = property.address
        return Response(serialized_data)


class BranchSearchView(APIView):
    def get(self, request, format=None):
        search_query = request.query_params.get('q', None)
        if search_query:
            branches = Branch.objects.filter(Q(branch_no__icontains=search_query) | Q(address__icontains=search_query))
            serialized_branches = [{"branch_no": branch.branch_no, "address": branch.address} for branch in branches]
            return Response(serialized_branches)
        else:
            return Response([])

class StaffSearchView(APIView):
    def get(self, request,branch_no, format=None):
        search_query = request.query_params.get('q', None)
        if search_query:
            staffs = Staff.objects.filter(Q(staff_no__icontains=search_query) | Q(fname__icontains=search_query) | Q(lname__icontains=search_query), branch_no = branch_no)
            serialized_staff = [{"staff_no": staff.staff_no, "name": staff.fname + " " + staff.lname} for staff in staffs]
            return Response(serialized_staff)
        else:
            return Response([])
        
class SupervisorByBranchView(APIView):
    def get_object(self, branch_no):
        try:
            return Branch.objects.get(branch_no = branch_no)
        except Branch.DoesNotExist:
            raise Http404
    def get(self, request,branch_no, format=None):
        branch = self.get_object(branch_no)

        staffs = Staff.objects.filter(branch_no = branch.branch_no, pos = "Supervisor")
        serialized_staff = [{"staff_no": staff.staff_no} for staff in staffs]
        return Response(serialized_staff)

class ClientSearchView(APIView):
    def get(self, request, branch_no, format=None):
        search_query = request.query_params.get('q', None)
        if search_query:
            clients = Client.objects.filter(Q(clientno__icontains=search_query) | Q(fname__icontains=search_query) | Q(lname__icontains=search_query), regbranch = branch_no  )
            serialized_client = [{"client_no": client.client_no, "name": client.fname + " " + client.lname} for client in clients]
            return Response(serialized_client)
        else:
            return Response([])

class PropertySearchView(APIView):
    def get(self, request, branch_no, format=None):
        search_query = request.query_params.get('q', None)
        if search_query:
            branches = Propertyforrent.objects.filter(Q(propertyno__icontains=search_query) | Q(address__icontains=search_query), regbranch = branch_no)
            serialized_branches = [{"propertyno": branch.propertyno, "address": branch.address} for branch in branches]
            return Response(serialized_branches)
        else:
            return Response([])

class OwnerSearchView(APIView):
    def get(self, request, branch_no, format=None):
        search_query = request.query_params.get('q', None)
        if search_query:
            branches = Privateowner.objects.filter(Q(ownerno__icontains=search_query) |Q(ownername__icontains=search_query), regbranch = branch_no)
            serialized_branches = [{"ownerno": branch.ownerno, "ownername": branch.ownername} for branch in branches]
            return Response(serialized_branches)
        else:
            return Response([])
