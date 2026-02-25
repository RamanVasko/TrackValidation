#!/usr/bin/env python3
"""
Setup script for Food Expiration Tracker Backend
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    return True

def create_env_file():
    """Create a sample .env file"""
    env_content = """# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/food_tracker

# Security
SECRET_KEY=your-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# CORS
ALLOWED_ORIGINS=["http://localhost:3000", "http://localhost:8080"]

# Notifications
NOTIFICATION_DAYS_BEFORE=3
EMAIL_ENABLED=true
PUSH_ENABLED=true

# Email Settings (Optional)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
EMAIL_FROM=noreply@foodtracker.com

# Firebase (Optional)
FIREBASE_CREDENTIALS_PATH=firebase-credentials.json

# Barcode API (Optional)
BARCODE_API_URL=https://api.barcodespider.com/v1
BARCODE_API_KEY=

# File Storage
STATIC_FILES_DIR=static
MAX_FILE_SIZE=5242880
ALLOWED_IMAGE_TYPES=["image/jpeg", "image/png", "image/jpg"]

# External APIs
OPEN_FOOD_FACTS_API=https://world.openfoodfacts.org/api/v0/product/
"""
    
    env_file = Path(".env")
    if not env_file.exists():
        with open(env_file, "w") as f:
            f.write(env_content)
        print("✓ Created .env file with default configuration")
        print("⚠️  Please update the database credentials and other settings as needed")
    else:
        print("✓ .env file already exists")

def install_dependencies():
    """Install Python dependencies"""
    print("📦 Installing Python dependencies...")
    
    try:
        # Try the simple installation first
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies with requirements.txt")
        print("🔄 Trying alternative installation method...")
        
        # Fall back to the alternative installer
        try:
            subprocess.check_call([sys.executable, "install_requirements.py"])
            return True
        except subprocess.CalledProcessError:
            print("❌ Alternative installation also failed")
            print("💡 Try installing packages manually or check your network/proxy settings")
            return False

def setup_database():
    """Setup database tables"""
    print("🗄️  Setting up database...")
    
    try:
        # Import and run database setup
        sys.path.append(str(Path(__file__).parent))
        from app.database.session import run_async_function, create_tables
        
        run_async_function(create_tables)
        print("✓ Database tables created successfully")
        return True
    except Exception as e:
        print(f"❌ Database setup failed: {e}")
        print("💡 Make sure PostgreSQL is running and credentials are correct")
        return False

def main():
    """Main setup function"""
    print("🚀 Food Expiration Tracker Backend Setup")
    print("=" * 50)
    
    # Change to backend directory
    os.chdir(Path(__file__).parent)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create environment file
    create_env_file()
    
    # Install dependencies
    if not install_dependencies():
        print("\n⚠️  Setup incomplete. Please resolve dependency issues.")
        sys.exit(1)
    
    # Setup database
    setup_database()
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed!")
    print("\nNext steps:")
    print("1. Update .env file with your database credentials")
    print("2. Start PostgreSQL server")
    print("3. Run: uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
    print("4. Open http://localhost:8000/docs to view API documentation")

if __name__ == "__main__":
    main()