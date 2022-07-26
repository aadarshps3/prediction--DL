from django.urls import path

from vaccine_app import views, admin_views, center_views, nurse_views, user_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('user_register', views.user_register, name='user_register'),

    path('admin_home', admin_views.admin_home, name='admin_home'),
    path('center_register', admin_views.center_register, name='center_register'),
    path('center_view', admin_views.center_view, name='center_view'),
    path('center_update/<int:id>/', admin_views.center_update, name='center_update'),
    path('center_delete/<int:id>/', admin_views.center_delete, name='center_delete'),
    path('nurse_view', admin_views.nurse_view, name='nurse_view'),
    path('user_view', admin_views.user_view, name='user_view'),
    path('user_delete/<int:id>/', admin_views.user_delete, name='user_delete'),
    path('vaccine_add', admin_views.vaccine_add, name='vaccine_add'),
    path('vaccine_view', admin_views.vaccine_view, name='vaccine_view'),
    path('vaccine_update/<int:id>/', admin_views.vaccine_update, name='vaccine_update'),
    path('vaccine_delete/<int:id>/', admin_views.vaccine_delete, name='vaccine_delete'),

    path('center_home', center_views.center_home, name='center_home'),
    path('nurse_register', center_views.nurse_register, name='nurse_register'),
    path('nurse_view', center_views.nurse_view, name='nurse_view'),
    path('nurse_update/<int:id>/', center_views.nurse_update, name='nurse_update'),
    path('nurse_delete/<int:id>/', center_views.nurse_delete, name='nurse_delete'),
    path('vaccine_view_c', center_views.vaccine_view_c, name='vaccine_view_c'),
    path('appointment_view_c',center_views.appointment_center,name='appointment_view_c'),

    path('nurse_home', nurse_views.nurse_home, name='nurse_home'),
    path('center_view_n', nurse_views.center_view_n, name='center_view_n'),
    path('vaccine_view_n', nurse_views.vaccine_view_n, name='vaccine_view_n'),
    path('schedule_add', nurse_views.schedule_add, name='schedule_add'),
    path('schedule_view', nurse_views.schedule_view, name='schedule_view'),
    path('schedule_update/<int:id>/', nurse_views.schedule_update, name='schedule_update'),
    path('schedule_delete/<int:id>/', nurse_views.schedule_delete, name='schedule_delete'),


    path('user_home', user_views.user_home, name='user_home'),
    path('center_view_u', user_views.center_view_u, name='center_view_u'),
    path('vaccine_view_u', user_views.vaccine_view_u, name='vaccine_view_u'),
    path('schedule_view_u', user_views.schedule_view_u, name='schedule_view_u'),
    path('book_appointment/<int:id>/', user_views.book_appointment, name='book_appointment'),
    path('appointment_view', user_views.appointment_view, name='appointment_view')
]
