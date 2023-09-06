from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Dilan 1990',
        'price': 'Rp.54.000',
        'amount':'10',
        'description':'Buku romantis anak SMA',
        'genre':'Romance'
    }

    return render(request, "main.html", context)