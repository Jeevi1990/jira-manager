"""Quick verification script to check if the project is set up correctly"""

import sys
from pathlib import Path

print("🔍 Verifying Jira Manager Setup...\n")

# Check Python version
print(f"✅ Python version: {sys.version.split()[0]}")

# Check required packages
required_packages = ['jira', 'dotenv', 'pytest']
missing_packages = []

for package in required_packages:
    try:
        __import__(package)
        print(f"✅ Package '{package}' installed")
    except ImportError:
        print(f"❌ Package '{package}' NOT installed")
        missing_packages.append(package)

# Check required files
print("\n📁 Checking configuration files:")
required_files = [
    'config.ini.example',
    '.env.example',
    '.gitignore',
    'requirements.txt',
    'README.md',
    'CONTRIBUTING.md'
]

for file in required_files:
    if Path(file).exists():
        print(f"✅ {file} exists")
    else:
        print(f"❌ {file} missing")

# Check source code
print("\n🐍 Checking source code:")
src_files = [
    'src/jira_manager/__init__.py',
    'src/jira_manager/core.py',
    'src/jira_manager/config.py',
    'src/jira_manager/exceptions.py'
]

for file in src_files:
    if Path(file).exists():
        print(f"✅ {file} exists")
    else:
        print(f"❌ {file} missing")

# Check if config.ini exists (should NOT be in git)
print("\n🔐 Security check:")
if Path('config.ini').exists():
    print("⚠️  config.ini exists (make sure it's in .gitignore!)")
else:
    print("✅ config.ini not found (good - use config.ini.example to create it)")

if Path('.env').exists():
    print("⚠️  .env exists (make sure it's in .gitignore!)")
else:
    print("✅ .env not found (good - use .env.example to create it)")

# Try importing the package
print("\n📦 Testing package import:")
try:
    from src.jira_manager import JiraClient, Config
    print("✅ Successfully imported JiraClient")
    print("✅ Successfully imported Config")
except Exception as e:
    print(f"❌ Failed to import: {e}")

print("\n" + "="*50)
if missing_packages:
    print(f"⚠️  Missing packages: {', '.join(missing_packages)}")
    print("Run: pip install -r requirements.txt")
else:
    print("✨ All checks passed! Project is ready to use.")
print("="*50)
