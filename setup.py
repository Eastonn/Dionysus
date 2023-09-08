from setuptools import setup, find_packages

setup(
    name='dionysus',
    version='1.0.0',
    packages=['src'],
    requires=['pydub',
              'moviepy',
              'setuptools'],
    install_requires=['pydub',
                      'moviepy',
                      'setuptools'],
    author='Easton',
    license='MIT',
    project_urls={
        'Source': 'https://github.com/Eastonn/dionysus',
    },
    entry_points={
        'console_scripts': [
            'dionysus=src.main:main',
        ],
    },
)
