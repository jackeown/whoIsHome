from setuptools import setup

setup(
    name='whoishome',
    version='0.0.3',
    url="https://github.com/jackeown/whoishome",
    description = ("A simple python CLI dashboard which uses nmap to help you keep track of who's on your network (made beautiful with the python library 'rich')."),
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    scripts=['whoishome/whoishome'],
    install_requires=[
        'rich',
    ],
)