from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsOfficeStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'staff'

class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'librarian'