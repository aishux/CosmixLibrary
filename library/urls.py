from django.contrib import admin
from django.urls import path
from books import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('endgame/', admin.site.urls),
    path('', views.index, name="index"),
    path('signup/', views.sign_up, name="signup"),
    path('student/', views.sdashboard),
    path('admin/', views.adashboard),
    path('admin-addbook/', views.addbook, name="addbook"),
    path('admin-layout/', views.alayout),
    path('admin-orders/', views.orders),
    path('logout/', views.log_out),
    path('student-bksearch/', views.booksearch),
    path('student-books/', views.studentbooks),
    path('admin-issue/', views.issuebook, name="issuebook"),
    path('student-layout/', views.studentlayout),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
