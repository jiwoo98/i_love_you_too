from django.shortcuts import render,redirect
from django.contrib.auth.models import User #이거 추가해줘야함(user에 대한 클래스를 가져와준다.)
from django.contrib import auth             #이거 추가해줘야함(계정에 대한 권한에 대한 것을 가져와준다.)

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html', {'error':'Password must match'})
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #auth.authenticate 라는 말은 DB에서 방금전에 입력한 이 내용이 우리한테 있는 회원명단이 맞는지 확인시켜주는 함수
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:    # is not None = None이 아니라면 = 회원이라면
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request,'login.html')