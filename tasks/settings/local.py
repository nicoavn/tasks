from . import base

SECRET_KEY="django-insecure-*-pvppssj8wjv!c728z=-_p0q-5%3_xl!r1cav1^1+5n5$otw0"

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    **base.DATABASES,
    **{
        'default': {
        	**base.DATABASES.get('default', {}),
        	**{
                'NAME': 'postgres',
                'USER': 'postgres',
                'PASSWORD': 'postgres',
                'HOST': 'db',
                'PORT': 5432,
            }
        }
    }
}
