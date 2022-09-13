from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from library.forms import NewBookForm, SearchForm
from library import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib import messages
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from .serializer import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.views.decorators.csrf import csrf_exempt



def userLogin(request):
    data={}
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,email=email,password=password)
        if user:
            login(request,user)
            request.session['email']=email
            messages.success(request, "User Logged In Succesfully")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Either email or password is incorrect")
            res=render(request,'library/login.html',data)
            return res
    else:
        res=render(request,'library/login.html',data)
        return res

def userSignup(request):
    return render(request, 'library/signup.html')

def userSignupHandle(request):
    if request.method=="POST":
        try:
            # Get the post parameters
            email=request.POST['email']
            fname=request.POST['fname']
            lname=request.POST['lname']
            password=request.POST['pass']
            UserType=request.POST['UserType']

            myuser = User.objects.create_user(email, password, fname, lname)

            if 'Admin' in UserType:
                myuser.is_admin = True
                print("Admin User")
            myuser.save()
            login(request,myuser)
            request.session['email']=email
            messages.success(request, "User Registered Succesfully")
            return redirect('home')
        except Exception as e:
            print(e)
            messages.error(request, "Something went wrong !! Please try again ")
            return redirect('home')
    else:
        messages.error(request, "Invalid credentials !! Please try again ")
        return redirect('home')

@login_required(login_url='/login/')
def userLogout(request):
    try:
        logout(request)
        del request.session['email']
        messages.success(request, "User Logout Succesfully")
        return redirect('login')
    except KeyError:
        messages.success(request, "User Logout Succesfully")
        return redirect('login')


@login_required(login_url='/login/')
def searchBook(request):
    form=SearchForm()
    res=render(request,'library/search_book.html',{'form':form})
    return res

@login_required(login_url='/login/')
def search(request):
    form=SearchForm(request.POST)
    title=form.data['title']
    books=models.Book.objects.filter(title=title)
    messages.success(request, "Search result")
    res=render(request,'library/search_book.html',{'books':books,'form':form})
    return res

@login_required(login_url='/login/')
def editBook(request):
    if request.user.is_admin:
        book=models.Book.objects.get(id=request.GET['bookid'])
        fields={'title':book.title, 'author':book.author,'price':book.price,'publisher':book.publisher}
        form=NewBookForm(initial=fields)
        res=render(request,'library/edit_book.html',{'form':form,'book':book})
        return res
    else:
        messages.error(request, "You are not authorized. Please login as Admin")
        return redirect('home')

@login_required(login_url='/login/')
def edit(request):
    if request.method=="POST":
        if request.user.is_admin:
            form=NewBookForm(request.POST)
            book=models.Book()
            book.id=request.POST['bookid']
            book.title=form.data['title']
            book.author=form.data['author']
            book.price=form.data['price']
            book.publisher=form.data['publisher']
            book.save()
            messages.success(request, "Book edited succesfully")
        else:
            messages.error(request, "You are not authorized. Please login as Admin")
        return redirect('home')

@login_required(login_url='/login/')
def deleteBook(request):
    if request.user.is_admin:
        bookid=request.GET['bookid']
        book=models.Book.objects.filter(id=bookid)
        book.delete()
        messages.success(request, "Book deleted succesfully")
    else:
        messages.error(request, "You are not authorized. Please login as Admin")
    return redirect('home')

@login_required(login_url='/login/')
def viewBooks(request):
    books=models.Book.objects.all()
    res=render(request,'library/view_books.html',{'books':books})
    return res

@login_required(login_url='/login/')
def newBook(request):
    if request.user.is_admin:
        form=NewBookForm()
        res=render(request,'library/new_book.html',{'form':form})
        return res
    else:
        messages.error(request, "You are not authorized. Please login as Admin")
        return redirect('home')

@login_required(login_url='/login/')
def addBook(request):
    if request.method=='POST':
        if request.user.is_admin:
            form=NewBookForm(request.POST)
            book= models.Book()
            book.title=form.data['title']
            book.author=form.data['author']
            book.price=form.data['price']
            book.publisher=form.data['publisher']
            book.save()
            messages.success(request, "Record saved succesfully")
        else:
            messages.error(request, "You are not authorized. Please login as Admin")
            return redirect('home')
    else:
        messages.success(request,"Record cannot be saved in database")
    return redirect('home')


# API Handling
@api_view(['POST'])
def user_login(request):
    try:
        data = request.data
        if not data.get('email') or not data.get('password'):
            return Response({
                    'status' : 401,
                    'message' : 'Please provide correct credentials',
                    })
        user=authenticate(request,email=data.get('email'),password=data.get('password'))
        if user:
            login(request,user)
            return Response({
                    'status' : 200,
                    'message' : 'Succesfully Login',
            })
    except Exception as e:
        print(e)
        return Response({
                'status' : 500,
                'message' : 'Something went wrong',
        })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_book(request):
    try:
        if request.user.is_admin:
            book_objs = models.Book.objects.all()
            serializer = BookSerializer(book_objs, many = True)

            return Response({
                'status': 200,
                'message': 'book fetched',
                'data': serializer.data
            })
        else:
            return Response({
                'status': 401,
                'message': 'You are not authorized',
            })

    except Exception as e:
        print(e)
        return Response({
                'status' : 500,
                'message' : 'Something went wrong',
        })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_book(request):
    try:
        if request.user.is_admin:
            data = request.data
            serializer = BookSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return Response({
                        'status' : 200,
                        'message' : 'success book added',
                        'data' : serializer.data
                })
        else:
            return Response({
                'status': 401,
                'message': 'You are not authorized',
            })
    except Exception as e:
        print(e)
        return Response({
                'status' : 400,
                'message': 'invalid data',
                'data' : serializer.errors
            })


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def patch_book(request):
    try:
        if request.user.is_admin:
            data = request.data
            if not data.get('id'):
                return Response({
                    'status' : 400,
                    'message' : 'id required',
                    'data'  : {}
                    })
            obj = models.Book.objects.get(id = data.get('id'))
            serializer = BookSerializer(obj, data = data , partial = True)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)
                return Response({
                        'status' : 200,
                        'message' : 'book updated',
                        'data' : serializer.data

                    })
        else:
            return Response({
                'status': 401,
                'message': 'You are not authorized',
            })
    except Exception as e:
        print(e)
        return Response({
                'status' : False,
                'message': 'invalid data',
            })



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_book(request):
    try:
        if request.user.is_admin:
            data = request.data
            if not data.get('id'):
                return Response({
                    'status' : 400,
                    'message' : 'id required',
                    'data'  : {}
                    })
            obj = models.Book.objects.get(id = request.GET['id'])
            obj.delete()
            return Response({
                'status' : 200,
                'message' : 'book deleted',
                'data'  : {}
                })
        else:
            return Response({
                'status': 401,
                'message': 'You are not authorized',
            })
    except Exception as e:
        print(e)
        return Response({
            'status' : 400,
            'message': 'invalid data',
        })
