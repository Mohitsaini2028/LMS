from django.urls import path
from . import views

urlpatterns=[
    path('',views.viewBooks, name="home"),
    path('new-book/',views.newBook),
    path('add-book/',views.addBook),
    path('delete-book/',views.deleteBook),
    path('edit-book/',views.editBook),
    path('edit/',views.edit),
    path('search-book/',views.searchBook),
    path('search/',views.search),
    path('login/',views.userLogin, name="login"),
    path('logout/',views.userLogout, name="login"),
    path('signup/',views.userSignup),
    path('signupHandle/',views.userSignupHandle),
    path('get-book/', views.get_book, name="get_book"),
    path('post-book/', views.post_book, name="post_book"),
    path('patch-book/', views.patch_book, name="post_book"),
    path('delete-book/', views.delete_book, name="delete_book"),
    path('login-api/', views.user_login),



]
