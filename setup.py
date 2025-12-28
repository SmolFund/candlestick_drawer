from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='candlestick_drawer',
    version='0.0.1', 
    author='Muhammadreza Haghiri',
    author_email='<haghiri75@gmail.com>',
    url='https://github.com/smolfund/candlestick_drawer',
    license='MIT',
    description='Making candlesticks from OHCL Data',
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'mediapipe'],
    keywords = ['finance', 'fintech', 'candlestick', 'candlestick charts', 'crypto'],
    classifiers = ["Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",]
)