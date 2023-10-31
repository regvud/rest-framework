from django.contrib.auth.base_user import BaseUserManager
from rest_framework.authentication import get_user_model


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password, **extra_kwargs):
        extra_kwargs.setdefault("is_superuser", True)
        extra_kwargs.setdefault("is_staff", True)
        extra_kwargs.setdefault("is_active", True)

        if not extra_kwargs["is_superuser"]:
            raise ValueError("Superuser must contain is_superuser = True")
        if not extra_kwargs["is_staff"]:
            raise ValueError("Superuser must contain is_staff = True")

        user = self.create_user(email, password, **extra_kwargs)

        user.save()
        return user
