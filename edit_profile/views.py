from django.shortcuts import render, get_object_or_404, redirect
from edit_profile.models import User
from .forms.user_form import UserCreateForm, UserUpdateName, UserUpdateEmail, UserUpdatePhone

people = [
    {
        "id": 0,
        "name": "Aron",
        "mail": "arona22@ru.is",
        "phone": "898-3234",
        "proimg": "img/profile_pic.jpg"
    },
    {
        "id": 1,
        "name": "Lulli",
        "mail": "lulli@ru.is",
        "phone": "898-3894",
        "proimg": "img/marga_pizza.jpg"
    },
        {
        "id": 2,
        "name": "janus",
        "mail": "janni22@ru.is",
        "phone": "898-1114",
        "proimg": "img/logo.jpg"
    }
]

# Create your views here.
def index(request):
    return render(request, 'edit_profile/index.html', context={'people': people})

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

def update_name(request, id):
    instance = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UserUpdateName(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('edit_profile-index')
    else:
        form = UserUpdateName(instance=instance)
    return render(request, 'edit_profile/update_name.html'), {
        'form': form,
        'id': id
    }

def update_email(request, id):
    instance = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UserUpdateEmail(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('edit_profile-index')
    else:
        form = UserUpdateEmail(instance=instance)
    return render(request, 'edit_profile/update_email.html'), {
        'form': form,
        'id': id
    }

def update_phone(request, id):
    instance = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UserUpdatePhone(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('edit_profile-index')
    else:
        form = UserUpdatePhone(instance=instance)
    return render(request, 'edit_profile/update_phone.html'), {
        'form': form,
        'id': id
    }
