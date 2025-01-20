from django.shortcuts import render
from configuration.utils import get_database_connection


class DomainCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Domain fetch karna
        domain = request.META.get('HTTP_HOST', '')  # Example: 'example.com:8000'
        # print(f"Request is coming from domain: {domain}")
       
        # Variable to store error message (if any)
        error_message = None

        try:
            connection = get_database_connection(domain.split(':')[0])
        except Exception as e:
            print(f"Failed to get database connection: {e}")
            connection = None
            error_message = f"Database connection failed: {str(e)}"  # Catch the error and store the message

        if error_message:
            # Store the error message in request
            request.error_message = error_message
            # Return a response with status 500
            response = render(request, "500.html", {'error_message': error_message})
            response.status_code = 500
            return response

        # if connection:
        #     print("Connection is done")

        # Proceed with the request if no error
        response = self.get_response(request)
        return response
