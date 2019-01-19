
from setuptools import setup, find_packages

setup(
    name="bay12_solution_eposts",
    description="Baseline solution for the 'eposts' problem",
    version="0.1",
    author="Anatoly Makarevich",
    author_email="anatoly_mak@yahoo.com",  
    packages=find_packages(),
    install_requires=[
        'numpy', 'pandas', 
        'scikit-learn', 
        'joblib', 
    ]
    # TODO: Add requirements and such
)
