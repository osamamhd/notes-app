from django.urls import path

from . import views

app_name = "note"

urlpatterns = [
    path(
        route='',view=views.NoteListView.as_view(), name='list'
    ),
    path(
        route='new/', view=views.NoteCreateView.as_view(), name='new'
    ),
    path(
        route='<slug:slug>/', view=views.NoteDetailView.as_view(), name='detail'
    ),
    path(
        route='update/<slug:slug>/', view=views.NoteUpdateView.as_view(), name='update'
    ),
    path(
        route='delete/<slug:slug>/', view=views.NoteDeleteView.as_view(), name='delete'
    ),
]