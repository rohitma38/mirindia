from setuptools import setup, find_packages


setup(
    name='mirindia',
    version='0.1',
    license='MIT',
    author="rma",
    package_dir={'': 'mirindia'},
    packages=find_packages('mirindia'),
    url='https://github.com/rohitma38/mirindia',
    keywords='',
    install_requires=[
          'matplotlib','pandas','numpy','scipy',
          'librosa==0.8','seaborn','praat-parselmouth',
          'soundfile','ffmpeg','ipython','jupyter'
      ],

)
