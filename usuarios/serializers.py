from rest_framework import serializers
from .models import UserProfile
class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ "name", "age", "gender", "cc", "phone_number", "email", "password"]

    def create(self, validated_data):
        # To-Do: Hashear la contraseña
        return super().create(validated_data)

