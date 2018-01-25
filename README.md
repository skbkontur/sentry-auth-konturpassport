# OpenID Connect for Sentry

An SSO provider for Sentry which enables OpenID Connect authentication.
This is a fork to make it work with AzureAD.


# Setup (AzureAD)

In Azure Portal, go to `Active Directory` service and register a new app.

The redirect URL you need to provide will be : `http://your.sentry.url/auth/sso`.

Create a new secret for this application (using the name you want for this secret).

You will then use the following values for your configuration in the following step :

|Configuration key|Default|Where to find it|
| ------------- | ------------- | ------------- |
|OPENID_AUTHORIZE_URL||https://login.microsoftonline.com/common/oauth2/authorize|
|OPENID_TOKEN_URL||https://login.microsoftonline.com/common/oauth2/token|
|OPENID_CLIENT_ID||In the app description, under the key "Application id"|
|OPENID_CLIENT_SECRET||The secret you created ealier|
|OPENID_NAME_PROP|email|The key in the jwt payload holding the name of the user (ex: `name` in our case)|
|OPENID_EMAIL_PROP|email|The key in the jwt payload holding the email of the user (ex: `upn` in our case)|


# Install with Docker

Using docker-compose and this installation : [onpremise](https://github.com/getsentry/onpremise)

Modify `docker-compose.yml` and add this lines under the `base` service :

```yml
    environment:
      # Run `docker-compose run web config generate-secret-key`
      # to get the SENTRY_SECRET_KEY value.
      SENTRY_SECRET_KEY: ''
      SENTRY_MEMCACHED_HOST: memcached
      SENTRY_REDIS_HOST: redis
      SENTRY_POSTGRES_HOST: postgres
      SENTRY_EMAIL_HOST: smtp
      OPENID_AUTHORIZE_URL:
      OPENID_TOKEN_URL: 
      OPENID_CLIENT_ID: 
      OPENID_CLIENT_SECRET:
      OPENID_NAME_PROP:
      OPENID_EMAIL_PROP: 
```

Then modify `requirements.txt` with this content :
```
# Add plugins here
https://github.com/LFBVR/sentry-auth-openid/archive/master.zip
```

And then modify `sentry.conf.py` to add these lines at the bottom :

```
OPENID_AUTHORIZE_URL = env('OPENID_AUTHORIZE_URL')
OPENID_TOKEN_URL = env('OPENID_TOKEN_URL')
OPENID_CLIENT_ID = env('OPENID_CLIENT_ID')
OPENID_CLIENT_SECRET = env('OPENID_CLIENT_SECRET')
OPENID_NAME_PROP = env('OPENID_NAME_PROP')
OPENID_EMAIL_PROP = env('OPENID_EMAIL_PROP')
SENTRY_FEATURES['organizations:sso'] = True
```

You can now start sentry (you may need to rebuild `base` image through `docker-compose build base`).

Once connected, there will be a new key `Auth` under `Manage` in your organization.
In this view, you will be able to choose to configure a new SSO service. 
