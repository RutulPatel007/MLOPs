from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()
    return requirements

print(get_requirements('requirements.txt'))


setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Credit Score Prediction',
    author='RutulPatel007',
    install_requires=get_requirements('requirements.txt'),
    license='',
)
