from django.urls import path
from .views import main_page, edit_content, delete_content, add_project, recreate_content

urlpatterns=[
    path('main_page/', main_page,name="main_page"),
    path('add_project/', add_project, name='add_project'),

    path('edit_content/<int:record_id>', edit_content, name='edit_content'),
    path('delete/<int:pk>/', delete_content, name='delete_content'),

    path('recreate/<int:pk>/', recreate_content, name='recreate_content'),
]