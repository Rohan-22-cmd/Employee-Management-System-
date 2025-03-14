from django.shortcuts import render, redirect
from .models import User, Department, Role
from .forms import UserForm

# Create User
# employee/views.py
from django.shortcuts import render, redirect
from .forms import UserForm

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user to the database
            return redirect('dashboard')  # Redirect to dashboard after saving
    else:
        form = UserForm()

    return render(request, 'add_user.html', {'form': form})

# Update User
def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to dashboard after successful update
    else:
        form = UserForm(instance=user)
    return render(request, 'update_user.html', {'form': form})
def dashboard(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})
from django.shortcuts import render, redirect, get_object_or_404
from .models import User

# Delete User
def delete_user(request, user_id):
    # Get the user to be deleted
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('dashboard')  # Redirect to the dashboard after deletion

    return render(request, 'delete_user.html', {'user': user})
