from django.urls import path,include
from . import views
app_name = 'survey'

urlpatterns = [
    path('', views.survey, name='survey'),
    # path('', views.index, name='home'),
    # path('login/', views.login_view, name='login'),
    # path('send_mail/', views.sendmails, name='send_mail'),
    # # path('password-reset/', views.password_reset, name='password_reset'),
    # path('logout/', views.logout_view, name='logout'),
    # path('user_creation/', views.user_creation, name='user_creation'),
    # path('update_user/<int:pk>', views.update_user, name='update_user'),
    # path('delete_user/<int:pk>', views.delete_user, name='delete_user'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('add_students-marks/', views.add_students_marks, name='add_students_marks'),
    # path('students_marklist/', views.students_marklist, name='students_marklist'),
    # path('edit_marks/<int:pk>', views.edit_marks, name='update_marks'),
    # path('delete_student/<int:pk>', views.delete_student, name='delete_student'),
]
