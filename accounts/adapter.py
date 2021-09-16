from allauth.account.adapter import DefaultAccountAdapter
from .password_validation import CustomValidator

class CustomAccountAdapter(DefaultAccountAdapter,CustomValidator):

    def clean_password(self, password, user=None):
        super().validate(password)
        return password