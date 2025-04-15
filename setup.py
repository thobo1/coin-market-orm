from setuptools import find_packages, setup

setup(
    name="coin-market-orm",  # Le nom que vous utiliserez pour pip install
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy>=1.4.0",
        "psycopg2-binary",
    ],
    python_requires=">=3.7",
    author="Anthony Thiery",
    author_email="votre@email.com",
    description="Une description courte de votre package",
)
