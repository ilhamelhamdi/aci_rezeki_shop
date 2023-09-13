from django.shortcuts import render

# Create your views here.
def show_homepage(request):
    context = {
        'author_name': "Ilham Abdillah Alhamdi",
        'class': "PBP B"
    }
    return render(request, "index.html", context)

def show_shop(request):
    context = {}
    return render(request, "shop.html", context)
