from setuptools import setup, find_packages

setup(
    name='example_package',
    version='0.1',
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple example package',
    long_description=open('README.md').read(),
    url='https://github.com/yourusername/example_package',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ]
)
