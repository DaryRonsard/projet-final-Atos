from rest_framework import serializers
from employee.models.leave_models import LeaveModels
from employee.models.employe_models import EmployeModels


class LeaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeaveModels
        fields = ['employe', 'type_de_conge', 'date_debut', 'date_fin', 'commentaire']
        #depth = 1
        #read_only_fields = ['employe', 'statut_manager', 'statut_rh']