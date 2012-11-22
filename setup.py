from setuptools import setup
setup(
    name = 'helloworld',
    version = '0.1',
    author = 'Daniel Mizyrycki',
    author_email='daniel.mizyrycki@dotcloud.com',

    packages=['helloworld'],

    install_requires = ['nose == 1.2.1'],
 
    test_suite = 'nose.collector',
)
