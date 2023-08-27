# --- Run the following commands ---
# python -m venv ads_venv
# On Windows - ads_venv\Scripts\activate
# On MacOS  - source ads_venv/bin/activate

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    Returns a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='ads_earthchain',
    version='1.0.0',
    author='balendra-singh',
    author_email='balendrasingh19@hotmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


