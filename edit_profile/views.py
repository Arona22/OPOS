from django.shortcuts import render, get_object_or_404, redirect
from edit_profile.models import User
from .forms.user_form import UserCreateForm

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
