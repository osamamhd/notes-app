from django.urls import path

from . import views

app_name = "note"

urlpatterns = [
    path(
        route='',view=views.NoteListView.as_view(), name='list'
    ),
    path(
        route='<slug:slug>/', view=views.NoteDetailView.as_view(), name='detail'
    ),
]