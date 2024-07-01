# File: pyp_package/__init__.py
import subprocess
import sys


def install(package_name):
    try:
        subprocess.check_call([sys.executable, '-m', 'pyp', 'install', package_name])
        print(f"Package '{package_name}' installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing package '{package_name}': {e}")

def uninstall(package_name):
      subprocess.check_call([sys.executable, '-m', 'pyp', 'uninstall', package_name])
      print(f'Package uninstalled successfully.')
