from django.utils.deprecation import MiddlewareMixin

# from customermanage.models import Myuser


# class CommonMiddleware(MiddlewareMixin):
#
#     def process_request(self, request):
#         if request.user:
#             try:
#                 user = Myuser.objects.filter(user_ptr=request.user).first()
#                 if not user:
#                     new = Myuser()
#                     new.user_ptr = request.user
#                     new.save()
#                     user = new
#                 request.myUser = user
#             # 匿名用户
#             except TypeError:
#                 return None
#         return None
