from setuptools import setup, find_packages

setup(
    name='QuestionsAPI',
    version=1.0,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'click==7.1.1',
        'Flask==1.1.2',
        'Flask-CLI==0.4.0',
        'flask-marshmallow==0.11.0',
        'Flask-Script==2.0.6',
        'Flask-SQLAlchemy==2.4.1',
        'marshmallow-sqlalchemy==0.22.3',
        'itsdangerous==1.1.0',
        'Jinja2==2.11.2',
        'MarkupSafe==1.1.1',
        'marshmallow==3.5.1',
        'pip==20.0.2',
        'setuptools==46.1.3',
        'six==1.14.0',
        'SQLAlchemy==1.3.16',
        'Werkzeug==1.0.1',
        'wheel==0.34.2'
    ],
)