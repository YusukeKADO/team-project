from django.shortcuts import render

# Create your views here.

from django.contrib.auth import get_user_model
from django.shortcuts import render

def user_profile(request, username):
    context = {
        'User': get_user_model().objects.get(username=username),
    }

    return render(request, 'accounts/user_profile.html', context)

def profile(request):
    if request.method == "POST":
        profile = User(title=request.POST['title'], body=request.POST['text'])
        profile.save()
        return redirect(user_profile, profile.id)
    context = {
        "profiles": User.objects.all(),
    }
    return render(request, 'accounts/user_profile.html', context)