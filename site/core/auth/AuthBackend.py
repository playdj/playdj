from django.conf import settings
from django.contrib.auth.models import User
from gmusicapi import Mobileclient

class AuthBackend(object):
    """
    Authenticate against the user's google account with gmusicapi

    If this is the User's first time logging in, create them an account.
    """

    def authenticate(self, email=None, password=None):
        # create the gmusicapi client and attempt to login
        # TODO: store the client somewhere so we can use it for music
        gmc = Mobileclient()
        valid = gmc.login(email, password)
        if valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. We don't need to store the password
                user = User(username=username, password='notactuallyused')
                # TODO: store some basic account info
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
