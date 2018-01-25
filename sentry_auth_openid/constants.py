from __future__ import absolute_import, print_function
from django.conf import settings
AUTHORIZE_URL = getattr(settings, 'OPENID_AUTHORIZE_URL', None)
ACCESS_TOKEN_URL = getattr(settings, 'OPENID_TOKEN_URL', None)
CLIENT_ID = getattr(settings, 'OPENID_CLIENT_ID', None)
CLIENT_SECRET = getattr(settings, 'OPENID_CLIENT_SECRET', None)
SCOPE = getattr(settings, 'OPENID_SCOPE', 'openid email')
EMAIL_PROP = getattr(settings, 'OPENID_EMAIL_PROP', 'email')
ERR_INVALID_RESPONSE = 'Unable to fetch user information.  Please check the log.'
DATA_VERSION = '1'
