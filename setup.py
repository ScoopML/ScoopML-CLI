from setuptools import setup, find_packages

long_description = '''
 A CLI for scoopml 
'''


setup(
    name='ScoopMLCLI',
    packages=['ScoopML'],  # this must be the same as the name above
    version='1.0.0',
    description='A CLI for scoopml',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ScoopML',
    author_email='harishsg99@gmail.com',
    url='https://github.com/ScoopML/ScoopML-CLI',
    keywords=['deep learning', 'tensorflow', 'keras', 'automl', 'xgboost'],
    classifiers=[],
    license='MIT',

    python_requires='>=3.5',
    include_package_data=True,
    install_requires=['requests' , 'click']
)
