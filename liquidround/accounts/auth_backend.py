from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class TokenBackend(ModelBackend):
    """Log in to Django without providing a password.

    """
    def authenticate(self, email=None, username=None, password=None):
        if email:
            try:
                return User.objects.get(email__iexact=email)
            except User.DoesNotExist:
                return None
        elif username:
            return super(TokenBackend, self).authenticate(username=username, password=password)

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None