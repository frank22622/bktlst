from setuptools import setup

setup(
    name='bktlst',
    packages=['bktlst'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pylint'
    ],
)