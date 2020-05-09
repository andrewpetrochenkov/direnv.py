try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='direnv',
    version='2020.5.9',
    packages=[
        'direnv',
    ],
)
