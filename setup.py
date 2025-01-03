from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    
    "The function will return the list of requirements"
    
    reqirements=[]
    with open(file_path) as file_obj:
        reqirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in reqirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="satya",
    author_email="satyasai.ch10@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
) 