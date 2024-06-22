from setuptools import setup, find_packages

setup(
    name='sh_helper',
    version='0.1',
    author='seung hyun',
    author_email='sh.kang@alcherainc.com',
    description='A simple example package',
    long_description=open('README.md').read(),
    url='https://github.com/Xenrose/sh_helper',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'Pillow',
        'opencv-python',
        'shapely']
)
