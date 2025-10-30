from setuptools import setup, find_packages
from typing import List
import os
import datetime
 
def get_requires(file:str)->List[str]:
    dot="-e ."
    requirements = []
    with open(file) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if dot in requirements:
            requirements.remove(dot)
    return requirements 
    
def create_info_file():
    info_content = f"""Package: basic_structure
Version: 0.0.1
Author: chaitanaya
Description: basic structure of python package
Created: {datetime.datetime.now()}
"""
    with open('basicstructure.info', 'w') as f:
        f.write(info_content)
    print("basicstructure.info file created!")

# Call the function
create_info_file()

setup( name="basic_structure"
    ,version="0.0.1"
    ,author="chaitanaya"
    ,description="basic structure of python package"
    ,packages=find_packages(),
    install_requires=get_requires('requirements.txt')
    )