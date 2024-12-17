from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Office Staff'),
        ('librarian', 'Librarian'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')

    # Add related_name to resolve the conflict with 'auth.User.groups' and 'auth.User.user_permissions'
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_set', 
        blank=True, 
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_set', 
        blank=True, 
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username

# Student Model
class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=50, unique=True)
    grade = models.CharField(max_length=50)  # Renamed from class_name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.roll_number}"

# Library History Model
class LibraryHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='library_records')
    book_name = models.CharField(max_length=255)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    book_status = models.CharField(max_length=50)  # Renamed from 'status'

    def __str__(self):
        return f"{self.book_name} - {self.book_status}"

# Fees History Model
class FeesHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees_records')
    fee_type = models.CharField(max_length=50)  # Renamed from fee_type
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.fee_type} - {self.amount}"
