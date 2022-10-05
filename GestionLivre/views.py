from django.shortcuts import render
from .models import Author

# Create your views here.
def index(request):
    result=Author.objects.all()
    context={"listeAuthor":result}
    
    return render(request,'index.html',context)

