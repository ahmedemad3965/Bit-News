from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from core.utils import generate_random_username


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'password')
        model = get_user_model()
        extra_kwargs = {
            'password': {
                'write_only': True, 'min_length': 8
            }
        }

    def create(self, validated_data):
        if validated_data.pop('guest', False):
            validated_data['username'] = generate_random_username()

        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={
            'input_type': 'password'
        },
        trim_whitespace=False,
        required=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password' or None)

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
