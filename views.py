from django.http import HttpResponse
from django.shortcuts import render
import datetime
from models import *

def index(request):
    	return render(request,'polls/index.html')

def insertbook(request):
    	return render(request,'polls/insertbook.html')

def deletebook(request):
    	return render(request,'polls/deletebook.html')

def searchbook(request):
    	return render(request,'polls/searchbook.html')

def search_temp(request):
    	return render(request,'polls/search_temp.html')

def contact(request):
    	return render(request,'polls/contact.html')

def bookslist(request):
	c=book.objects.all()
	context={"c":c}
    	return render(request,'polls/bookslist.html', context)

def search(request):
	if (request.POST):
		title = request.POST["title"]
		author = request.POST["author"]
		b=book.objects.filter(title=title,author=author)
		if(b.exists()):
			b=book.objects.filter(title=title,author=author)[0]
			context={"b":b}
			return render(request,"polls/search_temp.html",context)
		else :
			return HttpResponse("<h1>nothing was there for search</h1>")
	
def copies(request, book_id):	
	if(request.method=='POST'):
		num=request.POST["num_copies"]
		bk=book.objects.get(pk=book_id)
		if(bk.num_copies>=int(num)):
			cost=int(num)*bk.price
			return HttpResponse("The required no. of copies are available and the total cost is Rs. %s." % cost)
		else:
			return HttpResponse("Required number of copies are not available")


def insert(request):
	title = request.POST["title"]
	author = request.POST["author"]
	price = request.POST["price"]
	publisher = request.POST["publisher"]
	num_copies = request.POST["num_copies"]
	if(title=="" or author=="" or publisher ==""):
		return HttpResponse("<font color=red>Please enter every details</font>")
	else:
		book_obj = book(title=title,author=author,publisher=publisher,price=price,num_copies=num_copies)
		book_obj.save()
		return HttpResponse("Book successfully inserted into the database")

def delete(request):
	title = request.POST["title"]
	author = request.POST["author"]
	b=book.objects.filter(title=title,author=author)
	if(b.exists()):
		b.delete()
		return HttpResponse("Book is removed from the shelf")	
	else:
		return HttpResponse("Book is not on shelf") 


