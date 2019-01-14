from __future__ import absolute_import

from sentry.auth import register

from .provider import KonturPassport2Provider

register('openid', KonturPassport2Provider)
