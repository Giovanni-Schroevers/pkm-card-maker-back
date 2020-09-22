from rest_framework import serializers

from card_maker_app.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'over13',
            'photo',
            'bio',
        )


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'over13',
            'photo',
            'bio',
            'password'
        )


class UserOverviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'photo'
        )


class EmailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)


class UpdateEmailSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, allow_null=True)
    email = serializers.EmailField()


class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
