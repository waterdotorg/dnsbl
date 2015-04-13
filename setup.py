from setuptools import setup, find_packages

setup(
    name='dnsbl',
    version=__import__('dnsbl').__version__,
    author='Water.org',
    author_email='dev@water.org',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/waterdotorg/dnsbl/',
    license='GPL',
    description='Backend to query DNS based blackhole lists.',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU GPL License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
    ],
    long_description=open('README.md').read(),
)
