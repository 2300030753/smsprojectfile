from django.urls import path, include
from . import views

urlpatterns=[
    path('',views.ProjectHomePage,name='ProjectHomePage'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),
    path('printpagelogic/', views.printpagelogic, name='printpagelogic'),
    path('randompagecall/', views.randompagecall,name='randompagecall'),
path('calculatorlogic/',views.calculatorlogic,name='calculatorlogic'),
path('calculatorpagecall/',views.calculatorpagecall,name='calculatorpagecall'),
path('datetimepagecall/',views.datetimepagecall,name='datetimepagecall'),
path('datetimepagelogic/',views.datetimepagelogic,name='datetimepagelogic'),
path('add_task/',views.add_task,name='add_task'),
path('<int:pk>/delete/',views.delete_task,name='delete_task'),
path('UserRegisterPageCall/',views.UserRegisterPageCall,name='UserRegisterPageCall'),
path('UserRegisterLogic/',views.UserRegisterLogic,name='UserRegisterLogic'),
path('UserLoginPageCall/',views.UserLoginPageCall,name='UserLoginPageCall'),
path('UserLoginLogic/',views.UserLoginLogic,name='UserLoginLogic'),
path('logout/',views.logout,name='logout'),
path('add_student/',views.add_student,name='add_student'),
path('student_list/',views.student_list,name='student_list'),


]