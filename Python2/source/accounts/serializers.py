from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate, login


class LoginUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True},
            'is_active': {'read_only': True}
        }
    
    def __init__(self, *args, **kwargs):
        super(LoginUserSerializer, self).__init__(*args, **kwargs)
        self.logged_in = False
        self.user = None
        context = kwargs.get('context', None)
        if context:
            self.request = context['request']
    
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user = authenticate(self.request, email=email, password=password)
        if user:
            login(self.request, user)
            self.logged_in = True
            self.user = user
        return self
    
    @property
    def data(self):
        if self.logged_in:
            data = {
                "message": "Logged In",
                'id': self.user.id
            }
        else:
            data = {
                "message": "Something went wrong"
            }
        return data