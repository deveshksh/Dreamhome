from rest_framework import serializers
from .models import *

class BranchSerializer(serializers.ModelSerializer):
    branch_no = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        model = Branch
        fields = "__all__"
    
    def create(self, validated_data):
        last_branch = Branch.objects.order_by("branch_no").last()
        if last_branch:
            new_code = "B" + str(int(last_branch.branch_no[1:]) + 1).zfill(5)
        else:
            new_code = "B00001"
        
        branch = Branch.objects.create(branch_no = new_code, **validated_data)
        return branch

class StaffSerializer(serializers.ModelSerializer):
    # branch_no = serializers.PrimaryKeyRelatedField(queryset = Branch.objects.all())
    staff_no = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        model = Staff
        fields = "__all__"
    
    def create(self, validated_data):
        last_staff = Staff.objects.order_by("staff_no").last()
        if last_staff:
            new_code = "S" + str(int(last_staff.staff_no[1:]) + 1).zfill(5)
        else:
            new_code = "S00001"
        
        staff = Staff.objects.create(staff_no = new_code, **validated_data)
        return staff

class SimpleStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ("staff_no", "fname", "lname", "pos")

class SimpleBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ("branch_no", "address", "telno")

class StaffByBranchSerializer(serializers.Serializer):
    # branch_no = serializers.PrimaryKeyRelatedField(queryset = Branch.objects.all())
    staff = SimpleStaffSerializer(many = True)
    branch = SimpleBranchSerializer()
    class Meta:
        model = Staff
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    clientno = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        model = Client
        fields = "__all__"

    def create(self, validated_data):
        last = Client.objects.order_by("clientno").last()
        if last:
            new_id = "C" + str(int(last.clientno[1:]) + 1).zfill(5)
        else:
            new_id = "C00001"
        client = Client.objects.create(clientno = new_id, **validated_data)
        return client

class PrivateOwnerSerializer(serializers.ModelSerializer):
    ownerno = serializers.PrimaryKeyRelatedField(read_only =True)
    class Meta:
        model = Privateowner
        fields = "__all__"
    
    def create(self, validated_data):
        last_owner = Privateowner.objects.order_by("ownerno").last()
        if last_owner:
            new_code = "O" + str(int(last_owner.ownerno[1:]) + 1).zfill(5)
        else:
            new_code = "O00001"
        
        owner = Privateowner.objects.create(ownerno = new_code, **validated_data)
        return owner

class PropertyforrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Propertyforrent
        fields = "__all__"

class SimplePropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Propertyforrent
        fields = ("propertyno", "address", "proptype", "rooms", "rent")

class PropertyByBranchSerializer(serializers.Serializer):
    branch = SimpleBranchSerializer()
    property = SimplePropertySerializer(many = True)
    class Meta:
        model = Staff
        fields = "__all__"

class ViewReportSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        model = ViewReport
        fields = "__all__"
    def create(self, validated_data):
        last = ViewReport.objects.order_by("id").last()
        if last:
            new_id = last.id + 1
        else:
            new_id = 1
        report = ViewReport.objects.create(id = new_id, **validated_data)
        return report

class SimpleReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewReport
        fields = ("clientno", "view_date", "comment")

class ViewReportByPropertySerializer(serializers.Serializer):
    property = SimplePropertySerializer()
    report = SimpleReportSerializer(many = True)
    class Meta:
        model = Staff
        fields = "__all__"

class SimpleClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("clientno", "fname", "lname", "regdate")

class MatchingSerializer(serializers.Serializer):
    property = SimplePropertySerializer()
    client = SimpleClientSerializer(many = True)

class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preferences
        fields = "__all__"

class LeaseSerializer(serializers.ModelSerializer):
    leaseno = serializers.PrimaryKeyRelatedField(read_only = True)
    class Meta:
        model = Lease
        fields = "__all__"

    def create(self, validated_data):
        lease = Lease.objects.order_by("leaseno").last()
        if lease:
            new_no = str(int(lease.leaseno) + 1).zfill(8)
        else:
            new_no = "00000001"
        return Lease.objects.create(leaseno = new_no, **validated_data)