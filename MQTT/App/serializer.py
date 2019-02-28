from rest_framework.serializers import ModelSerializer
from .models import Emp


class EmpSerializer(ModelSerializer):
    class Meta:
        model = Emp
        fields = "__all__"