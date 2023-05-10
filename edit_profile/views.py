from django.shortcuts import render, get_object_or_404, redirect
from show_profile.models import User
from .forms.user_form import UserCreateForm, UserUpdateForm

# Create your views here.
def index(request):
    return render(request, 'edit_profile/index.html')

def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('edit_profile-index')
    else:
        form = UserCreateForm()
    return render(request, 'edit_profile/create_user.html', {
        'form': form
    })

def delete_user(reques, id):
    user = get_object_or_404(User, pk=id)
    user.delete()
    return redirect('edit_profile-index')

def update_user(request, id):
    instance = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UserUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('edit_profile-index')
    else:
        form = UserUpdateForm(instance=instance)
    
    return render(request, 'edit_profile/update_user.html', {
        'form': form,
        'id': id
    })

