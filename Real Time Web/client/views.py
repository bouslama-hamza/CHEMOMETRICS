from django.shortcuts import render , redirect
from .forms import UserRegisterForm
from django.contrib import messages
from .prediction import Prediction
import json
from django.contrib.auth.decorators import login_required

prediction = Prediction()

# Create your views here.
def client_signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully!')
            return redirect('client-login')
        else :
            messages.error(request, f'Account not created! Please try again.')
            return redirect('client-signup')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/client_signup.html', {'form': form})


# client home
@login_required
def client_home(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('data')
        if uploaded_file.name.endswith('.txt'):
            file_data = uploaded_file.read().decode('utf-8')
            data_list = list(map(int, file_data.split()))
            result = prediction.predict([data_list])
            graph_data = json.dumps(result)
            return render(request, 'app/client_home.html', {'result': result , 'graph_data': graph_data})
        else:
            messages.error(request, 'Please upload a valid file!')
            return redirect('client-home')
    return render(request, 'app/client_home.html')