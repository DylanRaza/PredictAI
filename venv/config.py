import os

class Config:
    """Base configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une_clé_secrète_très_difficile_à_deviner'
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///default.db'

class DevelopmentConfig(Config):
    """Development configuration class."""
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev.db'

class TestingConfig(Config):
    """Testing configuration class."""
    TESTING = True
    DATABASE_URI = 'sqlite:///test.db'

class ProductionConfig(Config):
    """Production configuration class."""
    DATABASE_URI = 'sqlite:///prod.db'
