from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str):
    requirements=[]
    with open(file_path) as f:
        requirements = f.readlines()
    for i in requirements:
        i.replace('\n','')
    if '-e .' in requirements:
        requirements.remove('-e .')
    return requirements


setup(
    name="DIAMONDPRICEPREDICTION",
    version='0.0.1',
    author="Vikraman",
    author_email="svikraman010101@gmail.com",
    installs_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)