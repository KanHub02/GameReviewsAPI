from django.contrib.auth.models import BaseUserManager


class UserBaseManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            password=password,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self._create_user(
            email, username, password, is_staff=True, is_superuser=True
        )
