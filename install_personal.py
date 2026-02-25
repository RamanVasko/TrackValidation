#!/usr/bin/env python3
"""
Personal installation script that bypasses corporate proxy
"""

import subprocess
import sys
import os
from pathlib import Path

def install_with_direct_pypi():
    """Install packages directly from PyPI, bypassing proxy"""
    
    packages = [
        'fastapi',
        'uvicorn[standard]',
        'sqlalchemy',
        'asyncpg',
        'alembic',
        'python-jose[cryptography]',
        'passlib[bcrypt]',
        'python-multipart',
        'python-dotenv',
        'python-dateutil',
        'aiosmtplib',
        'jinja2',
        'httpx',
        'Pillow',
        'structlog',
    ]
    
    print("📦 Installing packages directly from PyPI...")
    print("This will bypass your corporate proxy settings")
    
    success_count = 0
    
    for package in packages:
        try:
            # Use --index-url to force direct connection to PyPI
            cmd = [
                sys.executable, '-m', 'pip', 'install', 
                '--index-url', 'https://pypi.org/simple',
                '--trusted-host', 'pypi.org',
                '--trusted-host', 'pypi.python.org',
                '--trusted-host', 'files.pythonhosted.org',
                package
            ]
            
            print(f"Installing {package}...")
            subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"✓ {package} installed successfully")
            success_count += 1
            
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to install {package}")
    
    print(f"\nInstalled {success_count}/{len(packages)} packages")
    return success_count == len(packages)

def create_personal_env():
    """Create a personal .env file without corporate settings"""
    
    env_content = """# Personal Project Configuration
# No corporate proxy settings needed

# Database Configuration (Local PostgreSQL)
DATABASE_URL=postgresql://postgres:password@localhost:5432/food_tracker_dev

# Security (Generate your own secret key!)
SECRET_KEY=your-personal-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS (Local development)
ALLOWED_ORIGINS=["http://localhost:3000", "http://localhost:8080", "http://127.0.0.1:3000"]

# Notifications
NOTIFICATION_DAYS_BEFORE=3
EMAIL_ENABLED=false  # Set to true when you configure email
PUSH_ENABLED=false   # Set to true when you configure Firebase

# Email Settings (Optional - for personal email)
# SMTP_SERVER=smtp.gmail.com
# SMTP_PORT=587
# SMTP_USERNAME=your-personal-email@gmail.com
# SMTP_PASSWORD=your-app-specific-password
# EMAIL_FROM=your-personal-email@gmail.com

# Firebase (Optional - for push notifications)
# FIREBASE_CREDENTIALS_PATH=firebase-credentials.json

# File Storage
STATIC_FILES_DIR=static
MAX_FILE_SIZE=5242880
ALLOWED_IMAGE_TYPES=["image/jpeg", "image/png", "image/jpg"]

# External APIs (Optional)
# BARCODE_API_URL=https://api.barcodespider.com/v1
# BARCODE_API_KEY=
# OPEN_FOOD_FACTS_API=https://world.openfoodfacts.org/api/v0/product/
"""
    
    env_file = Path(".env")
    if not env_file.exists():
        with open(env_file, "w") as f:
            f.write(env_content)
        print("✓ Created personal .env file")
        print("💡 This file is configured for personal use without corporate proxy")
    else:
        print("✓ .env file already exists")

def main():
    """Main installation function"""
    print("🚀 Personal Project Setup - Food Expiration Tracker")
    print("=" * 60)
    print("Bypassing corporate proxy for personal use...")
    print()
    
    # Change to backend directory
    os.chdir(Path(__file__).parent)
    
    # Create personal environment file
    create_personal_env()
    
    # Install packages directly from PyPI
    if install_with_direct_pypi():
        print("\n🎉 Installation completed successfully!")
        print("\n📋 Next steps:")
        print("1. Install PostgreSQL locally (if not already installed)")
        print("2. Create database: food_tracker_dev")
        print("3. Update .env with your PostgreSQL credentials")
        print("4. Run: python -m uvicorn app.main:app --reload")
        print("5. Open: http://localhost:8000/docs")
        
        print("\n💡 For PostgreSQL setup:")
        print("   - Default user: postgres")
        print("   - Default password: password (change this!)")
        print("   - Create database: CREATE DATABASE food_tracker_dev;")
        
    else:
        print("\n⚠️  Some packages failed to install")
        print("💡 Try running the script again or install packages manually:")
        print("   pip install fastapi uvicorn[standard] sqlalchemy")

if __name__ == "__main__":
    main()