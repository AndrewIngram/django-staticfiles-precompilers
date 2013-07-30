from setuptools import setup

setup(
    name='django-staticfiles-precompilers',
    version='0.0.1',
    url='https://github.com/AndrewIngram/django-staticfiles-precompilers',
    install_requires=[
        'Django>=1.4.3',
        'django-appconf>=0.4',
        'envoy>=0.0.2',
    ],
    description="Lets Django's static template tag take care of precompilation",
    long_description=open('README.rst', 'r').read(),
    license="MIT",
    author="Andrew Ingram",
    author_email="andy@andrewingram.net",
    packages=['staticfiles_precompilers'],
    package_dir={'staticfiles_precompilers': 'staticfiles_precompilers'},
    include_package_data = True,    # include everything in source control
    package_data={'staticfiles_precompilers': ['*.py','templatetags/*.py']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python']
)