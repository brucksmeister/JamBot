from setuptools import setup, find_packages

setup(
    name='JamBot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pretty_midi',
        'mido',
        'tensorflow',
        'keras',
        'matplotlib',
        'np_utils',
        'h5py',
        'progressbar2'
    ],
    author='Brucksmeister',
    author_email='',
    description='',
    url='https://github.com/brucksmeister/JamBot.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)