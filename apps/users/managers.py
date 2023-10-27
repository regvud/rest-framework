from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_kwargs):
        if not email:
            raise ValueError('Provide an email!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_kwargs):
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_active', True)
        extra_kwargs.setdefault('is_staff', True)

        if not extra_kwargs['is_superuser']:
            raise ValueError('Superuser must contain is_superuser')

        if not extra_kwargs['is_staff']:
            raise ValueError('Superuser must contain is_staff')

        user = self.create_user(email, password, **extra_kwargs)

        return user
