from django.shortcuts import render

# Create your views here.
def show_homepage(request):
    context = {
        'app_name': "Aci Rezeki Shop",
        'author_name': "Ilham Abdillah Alhamdi",
        'class': "PBP B"
    }
    return render(request, "index.html", context)