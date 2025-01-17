from setuptools import find_packages, setup

version = '5.4.0'

setup(
    name='alerta-prometheus',
    version=version,
    description='Alerta plugin for Prometheus Alertmanager',
    url='https://github.com/veter2005/alerta-contrib',
    license='MIT',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    packages=find_packages(),
    py_modules=['alerta_prometheus'],
    install_requires=[
        'requests',
        'alerta-server>=4.10.1'
    ],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'alerta.plugins': [
            'prometheus = alerta_prometheus:AlertmanagerSilence'
        ]
    }
)
