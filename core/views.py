from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Note, Tag
from .forms import NoteForm

@login_required
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'core/notes_list.html', {'notes': notes})
    # return HttpResponse("Hello, world")

@login_required
def notes_detail(request, pk):
    note = Note.objects.get(pk=pk)
    return render(request, 'core/notes_detail.html', {'note': note, "pk":pk})

@login_required
def note_new(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid(): 
            note = form.save()
            return redirect('notes-detail', pk=note.pk)
    else:
        form = NoteForm()
        
    return render(request, 'core/notes_new.html', {'form': form})

@login_required
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid(): 
            note = form.save()
            return redirect('notes-detail', pk=note.pk)
    else: 
        form = NoteForm(instance=note)
    return render(request, 'core/notes_new.html', {'form': form})

@login_required
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('/')
