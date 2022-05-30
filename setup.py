from setuptools import setup, find_packages


setup(
    name='mirindia',
    version='0.2',
    license='MIT',
    author="rma",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/rohitma38/mirindia',
    keywords='example project',
    install_requires=[
          'matplotlib','pandas','numpy','scipy',
          'librosa==0.8','seaborn','praat-parselmouth',
          'soundfile','ffmpeg','ipython','jupyter'
      ],

)
