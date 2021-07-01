from rest_framework import serializers
from .models import Employee


def starts_with_R(value):
    if value[0].lower() != "r":
        raise serializers.ValidationError("Name must start with R")



# class EmployeeSerializer(serializers.Serializer):
#     # id = serializers.IntegerField()
#     name = serializers.CharField(max_length=20, validators=[starts_with_R])
#     salary = serializers.FloatField()
#     address = serializers.CharField(max_length=50)
    
#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.salary = validated_data.get("salary", instance.salary)
#         instance.address = validated_data.get("address", instance.address)
#         instance.save()
#         return instance



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


