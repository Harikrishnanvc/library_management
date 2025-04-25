from django.core.exceptions import ValidationError


def custom_password_validator(password):

    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least one numeral.")
    if not any(char.isalpha() for char in password):
        raise ValidationError("Password must contain at least one letter.")
    if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/~`' for char in password):
        raise ValidationError("Password must contain at least one special character.")
