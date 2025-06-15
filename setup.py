from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return list of Requirements
    """
    requirements_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt not found. No dependencies will be installed.")

    return requirements_lst


setup(
    name='End To End MLOPS Projects With ETL Pipelines- Building Network Security System',
    version='0.0.1',
    author='Syed Maaz',
    author_email='syedsam7676@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)




          
          
          