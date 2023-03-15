from setuptools import setup, find_packages

setup(
    name='weather',
    version='1.0.0',
    author='Rivka Finkelstein',
    description='Get weather information for a location using the OpenWeatherMap API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rifinkelstein/weather_app',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    install_requires=[
        'beautifulsoup4==4.11.2',
        'numpy==1.24.2',
        'pandas==1.5.3',
        'requests==2.27.1',
        'tabulate==0.8.9,'
    ],

    entry_points={
        'console_scripts': ['weather=weather:main']
    }
)
