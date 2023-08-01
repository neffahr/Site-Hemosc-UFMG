from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

HemoscUser = get_user_model()

class HemoscUserBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = HemoscUser.objects.get(email=email)
        except HemoscUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None
    
    def get_user(self, user_id):
        try:
            return HemoscUser.objects.get(pk=user_id)
        except HemoscUser.DoesNotExist:
            return None