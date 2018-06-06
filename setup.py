from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1.0'

install_requires = [
    'dnspython>=1.13.0',
    'geventhttpclient>=1.3.1',
]

test_requires = [
    'mock',
    'nose',
    'gipc',
    'pyOpenSSL>=0.14'
]

setup(
    name='etcd-gevent',
    version=version,
    description="A python client for etcd",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Database :: Front-Ends",
    ],
    keywords='async etcd raft distributed log api client',
    author='Wenjun Si',
    author_email='swj0066@gmail.com',
    url='http://github.com/wjsi/etcd-gevent',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=test_requires,
    test_suite='nose.collector',
)
