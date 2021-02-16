from  django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    DeleteView,
    UpdateView
)

from django.urls import reverse_lazy

from .models import Note

class NoteListView(ListView):
    model = Note

class NoteDetailView(DetailView):
    model = Note

class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'content']

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'content']
    template_name = 'note/note_update.html'

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note/note_delete.html'
    success_url = reverse_lazy('note:list')