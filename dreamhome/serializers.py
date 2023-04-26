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
    branch_no = serializers.PrimaryKeyRelatedField(queryset = Branch.objects.all())
    class Meta:
        model = Staff
        fields = "__all__"