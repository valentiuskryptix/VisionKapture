# from .models import Institution
#
# class TenantMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         self.process_request(request)
#         response = self.get_response(request)
#         return response
#
#     def process_request(self, request):
#         domain = request.META.get('HTTP_HOST', '').split(':')[0]  # Extract domain
#         try:
#             request.tenant = Institution.objects.get(domain=domain)
#         except Institution.DoesNotExist:
#             request.tenant = None
