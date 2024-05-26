from django.http import HttpResponse, HttpResponse, HttpRequest
from .models import User
import json
from django.shortcuts import get_object_or_404


def users(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        users_info = User.objects.all()  # Return all the objects you have
        serialized_users = [user.name for user in users_info]
        serialized_users_1 = json.dumps([user.id for user in users_info])  # Will check this
        # return HttpResponse(users)     # if just write this line, we will get plain text, that is messy,
        # so serialize return HttpResponse(serialized_users)  # This is still a list, so we need to import json to
        # convert into string
        return HttpResponse(json.dumps(serialized_users))

    if request.method == 'POST':
        body = json.loads(request.body)
        user = User.objects.create(name=body['name'], email=body['email'], age=body['age'])
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name}))


def get_or_update_or_delete_user(request: HttpRequest, id: int) -> HttpResponse:

    if request.method == 'GET':
        user = get_object_or_404(User, id=id)
        # user = User.objects.get(id=id)      # Better way to handled 500 server error
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'email': user.email, 'age': user.age}))

    if request.method == 'PUT':
        body = json.loads(request.body)
        user = get_object_or_404(User, id=id)
        # user = User.objects.get(id=id)   # Better way to handled 500 server error
        user.name = body['name']
        user.age = body['age']
        user.email = body['email']
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name}))

    if request.method == 'DELETE':
        user = get_object_or_404(User, id=id)
        # user = User.objects.get(id=id) # Better way to handled 500 server error
        user.delete()
        return HttpResponse(json.dumps({'id': user.id, 'deleted': True}))
