from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def clean_password(self, password, user=None):
        print('custom')
        return super().clean_password(password)