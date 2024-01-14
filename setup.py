from setuptools import setup, find_packages

setup(
    name="pydrama",
    version="0.1.5",
    author="JimEverest",
    author_email="ttqwer1@163.com",
    description="A Python programmer's tool for showing off / slacking off",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eaobservatory/pydrama",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pydrama=pydrama:pydrama',
        ],
    },
    package_data={
        'pydrama': ['data/*.txt'],
        # other patterns...
    }
)
