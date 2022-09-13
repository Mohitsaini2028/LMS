from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password must be provided")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default
    id = models.AutoField(primary_key=True)
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.FloatField()
    publisher=models.CharField(max_length=100)

    def __str__(self):
        return self.title[:20]+"   - "+self.author
