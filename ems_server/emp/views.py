from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

# 继承哪个视图类合适
from emp.models import Employee
from emp.serializer import EmployeeModelSerializer
from utils.response import APIResponse


class EmployeeAPIView(ListModelMixin, GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        emp_id = request.GET.get("id")
        emp_obj = Employee.objects.filter(id=emp_id)
        if emp_obj:
            emp_obj.delete()
            return APIResponse(200, "删除成功")
        return APIResponse(401, "删除失败")

