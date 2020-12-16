from setuptools import setup
setup(
    name = 'ListRepoCLI',
    version = '0.1.0',
    packages = ['ListRepoCLI'],
    entry_points = {
        'console_scripts': [
            'ListRepoCLI = ListRepoCLI.__main__:main'
        ]
    })