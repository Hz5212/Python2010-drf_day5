from rest_framework.views import APIView

from user.models import Admin
from user.serializer import AdminModelSerializer
from utils.response import APIResponse


class AdminAPIView(APIView):

    def get(self, request, *args, **kwargs):
        #用户登录请求的处理
        name = request.GET.get("name")
        password = request.GET.get("password")

        admin_obj = Admin.objects.filter(name=name, password=password).first()
        print(admin_obj)
        if admin_obj:
            data = AdminModelSerializer(admin_obj).data
            return APIResponse(200, True, results=data)

        return APIResponse(http_status=400)

    def post(self, request, *args, **kwargs):
        #用户的注册请求
        request_data = request.data
        serializer = AdminModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        admin_obj = serializer.save()

        if admin_obj:
            return APIResponse(200, True, results=AdminModelSerializer(admin_obj).data)

        return APIResponse(400, data_message="您提交的注册信息有误")
