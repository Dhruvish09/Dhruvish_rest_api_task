from rest_framework import serializers,validators
from myapp.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  class Meta:
    model = User
    fields=['email','name','phone_number','dob','password', 'password2']
    extra_kwargs={
      'password':{'write_only':True},
      'email': {
                'required': True,
                'allow_blank': True,
                'validators':[
                    validators.UniqueValidator(User.objects.all(),"A user with that Email already exists.")
                ]             
                }
    }

  # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = '__all__'



    