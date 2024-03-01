import subprocess
from setuptools import setup, find_packages

# Виконайте встановлення всіх пакетів з requirements.txt
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])


# Встановлюємо torch за допомогою light-the-torch
subprocess.run(['ltt', 'install', 'torch'])


# Читаємо залежності з файлу requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='brand_category_classification',
    version='0.0.1',
    author='junscience',
    author_email='temshik03@gmail.com',
    description='Embedding app for classification',
    install_requires=requirements,
    packages=find_packages(),
    scripts=['main.py']
)
