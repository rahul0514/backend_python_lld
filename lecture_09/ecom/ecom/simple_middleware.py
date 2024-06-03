def simple_middleware(get_response):

    print("Setup first middleware")

    def middleware(request):

        # Forward going area
        print("This is before view")

        response = get_response(request)

        print("This is after view")
        # Backward going area

        return response

    return middleware


def another_middleware(get_response):

    print("Setup second middleware")

    def middleware(request):

        # Forward going area
        print("This is another middleware before view")

        response = get_response(request)

        print("This is another middleware after view")
        # Backward going area

        return response

    return middleware
# def sum(a,b):
#
#     return a+b
#
#
# def perform_op(op, a, b):
#     return op(a,b)
#
# perform_op(sum, 2, 3)
