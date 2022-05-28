from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeList.as_view(), name='list_home'),
    path('<int:hid>', HomeDetail.as_view(), name='detail_home'),
    path('create', HomeCreate.as_view(), name='create_home'),
    path('update/<int:hid>', HomeUpdate.as_view(), name='update_home'),
    path('delete/<int:hid>', HomeDelete.as_view(), name='delete_home'),
    path('admission', LogListAdmission.as_view(), name='log_list_admission'),
    path('admission/<int:aid>', LogViewAdmission.as_view(), name='log_view_admission'),
    path('admission/create', LogCreateAdmission.as_view(), name='log_create_admission'),
    path('admission/<int:aid>/update', LogUpdateAdmission.as_view(), name='log_update_admission'),
    path('admission/<int:aid>/delete', LogDeleteAdmission.as_view(), name='log_delete_admission'),
    path('department', LogListDepartment.as_view(), name='log_list_department'),
    path('department/<int:did>', LogViewDepartment.as_view(), name='log_view_department'),
    path('department/create', LogCreateDepartment.as_view(), name='log_create_department'),
    path('department/<int:did>/update', LogUpdateDepartment.as_view(), name='log_update_department'),
    path('department/<int:did>/delete', LogDeleteDepartment.as_view(), name='log_delete_department'),
    path('school', LogListSchool.as_view(), name='log_list_school'),
    path('school/<int:sid>', LogViewSchool.as_view(), name='log_view_school'),
    path('school/create', LogCreateSchool.as_view(), name='log_create_school'),
    path('school/<int:sid>/update', LogUpdateSchool.as_view(), name='log_update_school'),
    path('school/<int:sid>/delete', LogDeleteSchool.as_view(), name='log_delete_school'),
]