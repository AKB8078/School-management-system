from rest_framework import serializers
from .models import CustomUser, Student, LibraryHistory, FeesHistory

# Custom User Serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll_number', 'grade', 'created_at', 'updated_at']

# Library History Serializer
class LibraryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryHistory
        fields = ['id', 'student', 'book_name', 'borrow_date', 'return_date', 'book_status']

# Fees History Serializer
class FeesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesHistory
        fields = ['id', 'student', 'type_of_fee', 'amount', 'payment_date', 'remarks']
