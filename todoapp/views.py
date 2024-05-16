from django.shortcuts import render, redirect
from .models import Todo_userDetails, Todo_taskDetails

# Views
def login(request):
    if 'username' in request.session:
        return redirect('homepage')
    else:
        data = {'error': None}
        if 'userdata' in request.session:
            return redirect('homepage')
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user_exists = Todo_userDetails.objects.filter(username=username, password=password).exists()
                if user_exists:
                    request.session['username'] = username
                    return redirect('homepage')
                else:
                    data['error'] = "Неправильный логин или пароль"
                    return render(request, 'login.html', data)
            return render(request, 'login.html')

def homepage(request):
    data = {}
    if 'username' in request.session:
        username = request.session['username']
        if request.method == "POST":
            q_data = request.POST
            user = request.session['username']
            date = q_data.get('date')
            time = q_data.get('time')
            priority = q_data.get('priority')
            description = q_data.get('description')
            try:
                task = Todo_taskDetails(userName=user, deadlineDate=date, deadlineTime=time, priority=priority, description=description)
                task.save()
            except Exception as e:
                print(e)
        try:
            orderby_list = ['deadlineDate', 'deadlineTime', 'priority']
            tasks = Todo_taskDetails.objects.filter(userName=username).order_by(*orderby_list).values()
            data = {'tasks': tasks}
        except Exception as e:
            print(e)
        return render(request, 'homepage.html', data)
    else:
        return redirect('login')

def signup(request):
    data = {}
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmpassword")
        if password != confirm_password:
            data["error"] = "Пароли не совпадают"
            return render(request, 'signup.html', data)
        else:
            if Todo_userDetails.objects.filter(username=username).exists():
                data["error"] = "Такое имя пользователя уже есть"
                return render(request, 'signup.html', data)
            elif Todo_userDetails.objects.filter(email=email).exists():
                data["error"] = "Такая почта есть"
                return render(request, 'signup.html', data)
            else:
                try:
                    user = Todo_userDetails(username=username, email=email, password=password)
                    user.save()
                    data["error"] = "Аккаунт был создан успешно"
                    return render(request, 'signup.html', data)
                except Exception as e:
                    data["error"] = "Что-то пошло не так..."
                    return render(request, 'signup.html', data)
    else:
        data["error"] = None
        return render(request, 'signup.html', data)

def reset_password(request):
    data = {}
    return render(request, 'resetPassword.html', data)

def profile_page(request):
    if 'username' in request.session:
        if request.method == 'POST':
            profile_pic = request.POST.get('photo')
            if not profile_pic:
                user_data = Todo_userDetails.objects.filter(username=request.session['username']).values()
                profile_pic = user_data[0]['profilePic']
            full_name = request.POST.get('fullname')
            mobile = request.POST.get('mobile')
            bio = request.POST.get('bio')
            try:
                Todo_userDetails.objects.filter(username=request.session['username']).update(profilePic=profile_pic, fullName=full_name, mobileNumber=mobile, bio=bio)
            except Exception as e:
                print(e)
        user_data = Todo_userDetails.objects.filter(username=request.session['username']).values()
        data = {'details': user_data[0]}
        return render(request, 'profilePage.html', data)
    else:
        return redirect('login')

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('login')

def delete_task(request, idd):
    Todo_taskDetails.objects.filter(taskId=idd, userName=request.session["username"]).delete()
    return redirect('homepage')

def edit_task(request, idd):
    data = {'idd': idd}
    user = request.session['username']
    if request.method == 'POST':
        q_data = request.POST
        date = q_data.get('date')
        time = q_data.get('time')
        priority = q_data.get('priority')
        description = q_data.get('description')
        try:
            Todo_taskDetails.objects.filter(taskId=idd, userName=user).update(deadlineDate=date, deadlineTime=time, priority=priority, description=description)
            return redirect('homepage')
        except Exception as e:
            print(e)
    task_data = Todo_taskDetails.objects.filter(taskId=idd, userName=user).values()
    data['todo'] = task_data[0]
    return render(request, "edittodo.html", data)
