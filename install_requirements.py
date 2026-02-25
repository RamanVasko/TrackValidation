#!/usr/bin/env python3
"""
Alternative installation script for environments with proxy issues
"""

import subprocess
import sys
import os

def install_package(package):
    """Install a single package with pip"""
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f"✓ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to install {package}: {e}")
        return False

def main():
    """Install packages one by one to handle proxy issues"""
    
    # Core packages that are essential
    essential_packages = [
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
    ]
    
    # Optional packages for notifications and development
    optional_packages = [
        'aiosmtplib',
        'jinja2',
        'httpx',
        'Pillow',
        'structlog',
        'pytest',
        'pytest-asyncio',
        'black',
        'flake8',
        'mypy',
    ]
    
    print("Installing essential packages...")
    success_count = 0
    
    for package in essential_packages:
        if install_package(package):
            success_count += 1
    
    print(f"\nInstalled {success_count}/{len(essential_packages)} essential packages")
    
    # Try optional packages
    print("\nInstalling optional packages...")
    optional_success = 0
    
    for package in optional_packages:
        if install_package(package):
            optional_success += 1
    
    print(f"Installed {optional_success}/{len(optional_packages)} optional packages")
    
    if success_count == len(essential_packages):
        print("\n🎉 Installation completed successfully!")
        print("You can now run: cd backend && uvicorn app.main:app --reload")
    else:
        print(f"\n⚠️  Installation partially completed. {success_count} essential packages installed.")
        print("You may still be able to run the application with limited functionality.")

if __name__ == "__main__":
    main()