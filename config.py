"""
Application configuration settings
"""

import os
from typing import List


class Settings:
    """Application settings"""
    
    # Application
    APP_NAME: str = "Food Expiration Tracker"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"
    
    # Database (SQLite for development without PostgreSQL dependency)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./food_tracker.db")
    DATABASE_TEST_URL: str = os.getenv("DATABASE_TEST_URL", "sqlite+aiosqlite:///./food_tracker_test.db")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8080"]
    
    # Notifications
    NOTIFICATION_DAYS_BEFORE: int = 3
    EMAIL_ENABLED: bool = True
    PUSH_ENABLED: bool = True
    
    # Email Settings
    SMTP_SERVER: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = os.getenv("SMTP_USERNAME", "")
    SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")
    EMAIL_FROM: str = os.getenv("EMAIL_FROM", "noreply@foodtracker.com")
    
    # Firebase (Push Notifications)
    FIREBASE_CREDENTIALS_PATH: str = "firebase-credentials.json"
    
    # Barcode API
    BARCODE_API_URL: str = "https://api.barcodespider.com/v1"
    BARCODE_API_KEY: str = ""
    
    # File Storage
    STATIC_FILES_DIR: str = "static"
    MAX_FILE_SIZE: int = 5 * 1024 * 1024  # 5MB
    ALLOWED_IMAGE_TYPES: List[str] = ["image/jpeg", "image/png", "image/jpg"]
    
    # External APIs
    OPEN_FOOD_FACTS_API: str = "https://world.openfoodfacts.org/api/v0/product/"


settings = Settings()
