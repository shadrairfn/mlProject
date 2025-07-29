from setuptools import setup, find_packages

HYPEN_E_DOT='-e .'
def getPackageData(file_path)-> list:
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='ml_project',
    version='0.1',
    author='Shadra',
    author_email='shadrairfn@gmail.com',
    packages=find_packages(),
    install_requires=getPackageData('requirements.txt'),
)