from django.shortcuts import render

people = {
        "id": 0,
        "name": "Aron",
        "mail": "arona22@ru.is",
        "phone": "898-3234",
        "proimg": "img/profile_pic.jpg"
    }
#         {
#         "id": 1,
#         "name": "Lulli",
#         "mail": "lulli@ru.is",
#         "phone": "898-3894",
#         "proimg": "img/marga_pizza.jpg"
#     }
# ]

# Create your views here.
def index(request):
    return render(request, 'edit_profile/index.html', context={'people': people})
