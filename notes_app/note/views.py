from  django.views.generic import ListView, DetailView, CreateView


from .models import Note

class NoteListView(ListView):
    model = Note

class NoteDetailView(DetailView):
    model = Note

class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'content']