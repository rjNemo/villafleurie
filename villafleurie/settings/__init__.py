import os

if os.environ.get('ENV') == 'PRODUCTION':
    from .production import *
else:
    from .development import *
