# from django.middleware import csrf
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.http.response import JsonResponse


@ensure_csrf_cookie
@api_view(["GET"])
def csrftoken(request):
    return Response({"cookie": "Csrf Cookie Setted Succesfully"})


@csrf_protect
@api_view(["POST"])
def LoginPage(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            return Response({"status": 201})

        username = request.data['username'].lower()
        password = request.data['password']
        isEmail = request.data['isEmail']

        if not isEmail:
            try:
                user = User.objects.get(username=username)
            except:
                user = None
        else:
            try:
                user = User.objects.get(email=username)
            except:
                user = None

        if not user:
            return Response({"status": 404})

        if user.check_password(password):
            login(request=request, user=user)
            return Response({"status": 200})
        else:
            return Response({"status": 404})
    else:
        return Response({"status": 403})


@api_view(["GET"])
def logoutPage(request):
    try:
        logout(request)
        return Response({"status": 200})
    except:
        print("error")
        return Response({"status": 404})


@csrf_protect
@api_view(["POST"])
def RegisterPage(request):
    data = request.data
    if request.user.is_authenticated:
        return Response({"status": 201})

    username = data["username"].lower()
    email = data["email"].lower()
    first_name = data["first_name"]
    last_name = data["last_name"]
    password = data["password"]

    try:
        User.objects.get(username=username)
        User.objects.get(email=email)

        return Response({"status": 202})
    except:
        pass

    user = User.objects.create(username=username.lower(
    ), email=email, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.save()

    return Response({"status": 200})


# if you logged in user don't use api_view decorator or it will mark user as anonymous user
def isAuthenticateApi(request):
    if request.user.is_authenticated:
        return JsonResponse({"status": 200})
    return JsonResponse({"status": 400})


@api_view(["GET"])
def Demo_api(request):
    content = {
        "Site": "Heatlhify",
        "Developer Name": "Pranjul Jain",
    }

    return Response(content)


'''               
@api_view(['GET'])
 def csrftoken(request):
     response = Response({"message": "csrftoken"})
     response['X-CSRFToken'] = csrf.get_token(request)
     try:
         print(response)
         print(response.items())
     except Exception as e:
         print(e)
     return response 
'''
