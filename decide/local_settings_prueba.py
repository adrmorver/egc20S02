ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

BASEURL = 'http://localhost:8005'

APIS = {
    'authentication': 'http://localhost:8005',
    'base': 'http://localhost:8005',
    'booth': 'http://localhost:8005',
    'census': 'http://localhost:8005',
    'mixnet': 'http://localhost:8005',
    'postproc': 'http://localhost:8005',
    'store': 'http://localhost:8005',
    'visualizer': 'http://localhost:8005',
    'voting': 'http://localhost:8005',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'decide',
        'USER': 'decide',
        'PASSWORD': 'decide',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
