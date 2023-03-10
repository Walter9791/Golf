from django.shortcuts import render
from .models import Notes
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import NotesForm

class NotesUpdateView(UpdateView):
    model = Notes
    #instead of fields from Notes, we can use a form class like below //fields = ['title', 'text']
    form_class = NotesForm
    success_url = '/notes'



class NotesCreateView(CreateView):
    model = Notes
    #instead of fields from Notes, we can use a form class like below //fields = ['title', 'text']
    form_class = NotesForm
    success_url = '/notes'


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html" #another way to call notes_list.html for this list view

#the class above handles what is below as a class function easily   
#def list(request):
 #   all_notes = Notes.objects.all()
 #   return render(request, 'notes/notes_list.html', {'notes':all_notes})



class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

# the above code handles how this below function works with the DETAILVIEW. It even throws the error without have to type out the try loop as we have below. 
#
#def detail(request, pk):
 #   try:
  #      note = Notes.objects.get(pk=pk)
   # except Notes.DoesNotExist:
    #    raise Http404("Note DNE")
    #return render(request, 'notes/notes_detail.html', {'note': note})

