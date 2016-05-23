import simplestopwatch

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='simplestopwatch',
    version=simplestopwatch.__version__,
    description='A very simple python module for measuring elapsed time.',
    long_description=simplestopwatch.__doc__,
    author=simplestopwatch.__author__,
    author_email='john -at- 7oars.com, coblekent@gmail.com',
    url='https://github.com/kamakazikamikaze/simplestopwatch',
    download_url='https://github.com/kamakazikamikaze/simplestopwatch',
    license='BSD',
    platforms=['POSIX', 'Windows'],
    keywords=['timer', 'stopwatch', 'execution', 'timeit'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers'
    ],
    packages=['simplestopwatch'],
    py_modules=['simplestopwatch'],
    test_suite='simplestopwatch.tests.suite',
    use_2to3=True,
    zip_safe=True,
)
