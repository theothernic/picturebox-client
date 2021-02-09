from setuptools import setup, find_packages

setup(
    name='picturebox',
    version='0.2.6',
    url='https://www.nicholasbarr.net',
    author='Nic Barr',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.9',
    install_requires=['PyQt5'],
    entry_points={
        "console_scripts": [
            'picturebox = picturebox:main'
        ]
    }
)
