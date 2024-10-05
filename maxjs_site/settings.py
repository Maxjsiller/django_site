import os
from pathlib import Path

# BASE_DIR represents the root of your project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False in production

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'mrmczoo.com']  # Add your production domain later

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add your custom apps here
    # 'your_app_name',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'maxjs_site.urls'  # Replace with your actual project name

WSGI_APPLICATION = 'maxjs_site.wsgi.application'  # Replace with your actual project name

# Database Configuration for SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # The SQLite database file is created here
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] 

# Internationalization
LANGUAGE_CODE = 'en-gb'  # Change to your preferred language code
TIME_ZONE = 'UTC'  # Change to your preferred timezone
USE_I18N = True
USE_L10N = True
USE_TZ = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maxjs_site.settings')
