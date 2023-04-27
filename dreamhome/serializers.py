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
    class Meta:
        model = Client
        fields = "__all__"

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