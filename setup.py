from setuptools import setup, find_namespace_packages

setup(
    name='knowledge_base',
    version='1.0.0',
    description='adressbook',
    url='https://github.com/Vladosinfo/knowledge_base',
    author='Vladyslav Vyasadev, Yar Valeriy, Prus Valerii, Oleksiy Tsybrovskyi, Palamar Anna',
    author_email='vladyslav.pasko@gmail.com, prusvalerii@gmail.com, tsybrovsky@gmail.com, yar.valeriy@yahoo.com, anna.palamar1210@gmail.com',
    license='BSD',
    packages=find_namespace_packages(),
    install_requires=[],
    entry_points={'console_scripts': ['bot-helper = src.main:main']},
)
