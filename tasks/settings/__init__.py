import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Production environment
if os.path.isfile(os.path.join(ROOT_DIR, '../../PRO_ENVIRONMENT')):
    from .pro import *
else:
    from .base import *

from .local import *
