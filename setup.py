from setuptools import setup, find_packages

setup(name='PyWaves',
      version='0.9.0',
      description='Object-oriented library for the Waves blockchain platform',
      url='http://github.com/pywaves/pywaves',
      author='PyWaves Developers',
      author_email='dev@pywaves.org',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      keywords = ['waves', 'blockchain', 'analytics'],
      install_requires=[
            'base58',
            'pyblake2',
            'python-axolotl-curve25519',
            'requests',
            'google-api-python-client'
      ]
      )


