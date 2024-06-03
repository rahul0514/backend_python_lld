from django.http import HttpResponse
from ecom.views import EmptyException


class SimpleClassMiddleware:

    def __init__(self, get_response):
        self.get_reponse = get_response

    def __call__(self, request):  # This will call everytime we get request

        # This is before
        print("This is before part of class base middleware")

        response = self.get_reponse(request)

        # this is after
        print("This is after part of class base middleware")

        return response

    def process_exception(self, request, exception):
        if type(exception) == EmptyException:
            print(str(exception))
            return HttpResponse("This is empty")
        return None
