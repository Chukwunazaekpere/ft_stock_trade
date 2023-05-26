from .base_settings import *

from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
print("\n\t DB_NAME: ", os.getenv("DB_NAME"))
print("\n\t LOCAL_DB_URL: ", os.getenv("LOCAL_DB_URL"))

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv("DB_NAME"),
        "HOST": os.getenv("LOCAL_DB_URL")
    }
}

# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.getenv("LOCAL_DB_URL")
#     )
# }