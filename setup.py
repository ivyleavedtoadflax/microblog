from setuptools import setup

setup(
    name='app',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-Login',
        'Flask-OpenID',
        'Flask-SQLAlchemy',
        'Flask-WTF'
    ],
)
