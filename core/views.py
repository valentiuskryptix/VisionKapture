from django.http import HttpResponse

def home(request):
    if request.tenant:
        return HttpResponse(f"Hello, {request.tenant.name}!")
    else:
        return HttpResponse("No tenant detected.")
