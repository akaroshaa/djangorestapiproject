import sys
sys.path.append("/.../")

from rest_framework import serializers
from ..models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    
    def validate_salary(self, value):
        if value < 10000:
            raise serializers.ValidationError("Salary must be greater than 10000")
        return value


    def validate(self, data):
        name = data.get("name")
        salary = data.get("salary")
        address = data.get("address")
        if salary < 5000:
            raise serializers.ValidationError("Salary must be greater than 5000")
        elif len(name) < 6:
            raise serializers.ValidationError("Name must have atleast 6 characters")
        return data
