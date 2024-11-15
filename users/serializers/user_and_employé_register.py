from rest_framework import serializers
from users.models.user_models import UserModels
from employee.models.employe_models import EmployeModels


class UserEmployeeRegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    role = serializers.ChoiceField(choices=UserModels.ROLE_CHOICES, required=True)

    sexe = serializers.ChoiceField(choices=EmployeModels.GENRE, required=True)
    contrat = serializers.ChoiceField(choices=EmployeModels.TYPE_DE_CONTRAT, required=True)
    matricule = serializers.CharField(required=True, max_length=6)
    salaire = serializers.CharField(required=True, max_length=60)
    date_embauche = serializers.DateField(required=True)
    department = serializers.CharField(required=True, max_length=255)
    address = serializers.CharField(required=True, max_length=50)
    phone = serializers.CharField(required=True, max_length=50)
    post = serializers.CharField(required=True, max_length=50)
    picture = serializers.ImageField(required=False, allow_null=True)
    social_secure_number = serializers.CharField(required=True, max_length=20)

    class Meta:
        model = UserModels
        fields = (

            'username', 'password', 'first_name', 'last_name', 'email', 'role',

            'sexe', 'contrat', 'matricule', 'salaire', 'date_embauche', 'department',
            'address', 'phone', 'post', 'picture', 'social_secure_number'
        )

    def create(self, validated_data):

        user_data = {
            'username': validated_data.pop('username'),
            'password': validated_data.pop('password'),
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'email': validated_data.pop('email'),
            'role': validated_data.pop('role'),
        }

        user = UserModels.objects.create_user(
            **user_data
        )


        EmployeModels.objects.create(
            user=user,
            sexe=validated_data['sexe'],
            contrat=validated_data['contrat'],
            matricule=validated_data['matricule'],
            salaire=validated_data['salaire'],
            date_embauche=validated_data['date_embauche'],
            department=validated_data['department'],
            address=validated_data['address'],
            phone=validated_data['phone'],
            post=validated_data['post'],
            picture=validated_data.get('picture'),
            social_secure_number=validated_data['social_secure_number']
        )

        return user
