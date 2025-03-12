from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        # Validasi input kosong
        if not username or not password:
            return render(request, 'accounts/login.html', {
                'error': 'Username dan password harus diisi.'
            })

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:index_dashboard')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Username atau password salah.'
            })
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')