from django.shortcuts import render
from .models import Trick, UserProgress
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import UserProgress

def HOME(request):
    return render(request, "home.html")

def ABOUT(request):
    return render(request, "about.html")

def sign_in(request):
    return LoginView.as_view()(request)

@login_required
def CHECKBOXES(request):
    user = request.user
    tricks = Trick.objects.all()
    user_progress = UserProgress.objects.filter(user=user)

    # Create a dictionary to store the user's progress for each trick
    user_progress_dict = {progress.trick_id: progress.selection for progress in user_progress}

    if request.method == 'POST':
        for trick in tricks:
            trick_status = request.POST.get(f'trick_{trick.id}')

            if trick_status:
                # Save the user's progress to the database
                user_progress, created = UserProgress.objects.get_or_create(user=user, trick=trick)
                user_progress.selection = trick_status
                user_progress.save()


    return render(request, 'checkbox.html', {'tricks': tricks, 'user_progress': user_progress_dict})

@login_required
def view_progress(request):
    user_progress = UserProgress.objects.filter(user=request.user)
    return render(request, 'progress_template.html', {'user_progress': user_progress})