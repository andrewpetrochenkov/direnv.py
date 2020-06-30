import setuptools

setuptools.setup(
    name='direnv',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
