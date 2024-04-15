from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Trick, UserProgress
from .forms import CustomUserUpdateForm, SignUpForm

def HOME(request):
    return render(request, "home.html")

def ABOUT(request):
    return render(request, "about.html")

def sign_in(request):
    return LoginView.as_view()(request)

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful sign-up
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def skate_dice(request):
    return render(request, 'skate_dice.html')

@login_required
def CHECKBOXES(request):
    user = request.user
    tricks = Trick.objects.all()

    if request.method == 'POST':
        for trick in tricks:
            # Get the status and notes from the submitted form data
            trick_status = request.POST.get(f'trick_{trick.id}')
            notes = request.POST.get(f'notes_{trick.id}', '')

            # Retrieve or create a UserProgress instance for the current user and trick
            user_progress, created = UserProgress.objects.get_or_create(
                user=user, 
                trick=trick,
                defaults={'selection': trick_status, 'notes': notes}
            )

            # Update the UserProgress instance if it already exists
            if not created:
                if trick_status:
                    user_progress.selection = trick_status
                user_progress.notes = notes
                user_progress.save()

    # After processing the form, retrieve the updated UserProgress instances for the user
    user_progresses = UserProgress.objects.filter(user=user)

    # Pass the tricks and user_progresses to the template
    return render(request, 'checkbox.html', {
        'tricks': tricks,
        'user_progresses': user_progresses
    })


@login_required
def view_progress(request):
    user_progress = UserProgress.objects.filter(user=request.user)
    return render(request, 'progress_template.html', {'user_progress': user_progress})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('change_password_done')
    else:
        form = CustomUserUpdateForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})

class CustomLogoutView(LogoutView):
    next_page = 'home'
