from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import * 
from django.template import Context
from models import Author,Book

def hello(requset):
    return HttpResponse("Hello world")
def homepage(ruquest):
    book_list = Book.objects.all()
    c = Context({"book_list":book_list})    
    return render_to_response("head.html", c) 
def delete(request):
    delete_id  =request.GET["id"]
    Book.objects.filter(ISBN= delete_id).delete()
    return  HttpResponseRedirect('/home/')
def search(request):
    post=request.POST['search']
    p=Author.objects.filter(Name= post)
    book_list=Book.objects.filter(Authors=p)
    L=[p,book_list]
    c=Context({"L":L})
    return render_to_response("search.html",c)  
def more(request):
    more_id =request.GET["id"]
    book=Book.objects.filter(ISBN=more_id)
    c = Context({"book":book}) 
    return render_to_response("more.html",c)  
def addbook(request):
    author_id=request.GET["id"]
    c = Context({"authorid":author_id}) 
    return render_to_response("addbook.html",c)
def submit(request):
    if request.POST:    
        post = request.POST
        p=Author.objects.get(AuthorID =post["authorid"])
        new_book = Book(
            Title = post["title"],
            ISBN = post["isbn"],
            Publisher = post["pub"],
            PublishDate = post["date"],
            Price = post["price"],
            Authors=p)
        new_book.save()
        return  HttpResponseRedirect('/home/') 
def deleteauthor(request):
    delete_id  =request.GET["id"]
    p=Author.objects.get(AuthorID= delete_id)
    Book.objects.filter(Authors= p).delete()
    Author.objects.get(AuthorID= delete_id).delete()
    return  HttpResponseRedirect('/authorlist/')
def addauthor(request):
    return render_to_response("addauthor.html")
def submitauthor(request):
    if request.POST:    
        post = request.POST
        new_author = Author(
            AuthorID = post["id"],
            Name = post["name"],
            Age = post["age"],
            Country=post["country"]
            )
        new_author.save()
        return  HttpResponseRedirect('/authorlist/') 
def authorlist(request):
    author_list = Author.objects.all()
    c = Context({"author_list":author_list})    
    return render_to_response("authorlist.html", c) 

    

    
    
    
    
    
    
    
    
    

    
        
    
    
