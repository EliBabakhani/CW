from django.shortcuts import render
from .models import Author

def author_list(request):
    all_author=Author.objects.all()
    return render(request, 'Author/author_list.html', {'authors': all_author})

def author_details(request, id):
    author=Author.objects.get(pk=id)
    return render(request, 'Author/author_details.html',{'author': author})