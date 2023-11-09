from setuptools import setup

setup(name='spekpy_mod',
      version='2.0.10',
      description='A Python software toolkit for modelling the x-ray spectra from x-ray tubes',
      url='https://bitbucket.org/spekpy/spekpy_release',
      author='Gavin Poludniowski & Robert Bujila',
      author_email='gpoludniowski@gmail.com',
      license='MIT License',
      install_requires=['matplotlib'],
      packages=['spekpy_mod'],
      zip_safe=False,
      package_data={'spekpy_mod':[r'data/tables/*.dat', r'data/matl_def/*.comp', r'data/matl_usr/*.comp', r'data/state_usr/*.state', r'data/state_def/*.state',r'data/tables/advanced/*.npz']},
      include_package_data=True)
