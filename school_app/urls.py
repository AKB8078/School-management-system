from rest_framework.routers import DefaultRouter
from .views import login_view,register_user, CustomUserViewSet,StudentViewSet, LibraryHistoryViewSet, FeesHistoryViewSet
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='user')
router.register('students', StudentViewSet, basename='student')
router.register('library-history', LibraryHistoryViewSet, basename='library-history')
router.register('fees-history', FeesHistoryViewSet, basename='fees-history')

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_user, name='register_user'),
    path('api/', include(router.urls)),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),  # Edit user URL
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),  # Delete user URL
    path('office-staff-dashboard/', views.office_staff_dashboard, name='office_staff_dashboard'),
    path('manage-fees-history/', views.manage_fees_history, name='manage_fees_history'),
    path('add-fee/', views.add_fee, name='add_fee'),
    path('edit-fee/<int:fee_id>/', views.edit_fee, name='edit_fee'),
    path('delete-fee/<int:fee_id>/', views.delete_fee, name='delete_fee'),
    path('librarian-dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
    path('logout/', views.logout_view, name='logout'),
   # path('', views.home, name='home'),
    path('add-student/', views.add_student, name='add_student'),
    path('add/', views.add_student, name='add_student'),
    path('list/', views.student_list, name='student_list'),
    path('librarian-dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
    path('add-library-record/', views.add_library_record, name='add_library_record'),
    path('edit-library-record/<int:pk>/', views.edit_library_record, name='edit_library_record'),
    path('delete-library-record/<int:pk>/', views.delete_library_record, name='delete_library_record'),
]