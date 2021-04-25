# // Code Written by Minghao Gou

from distutils.core import setup
import setuptools
from Cython.Build import cythonize
import numpy

setup(
    version='1.0.2',
    description='Grasp NMS',
    author='Minghao Gou',
    author_email='gouminghao@gmail.com',
    url='https://github.com/GouMinghao/graspnms',
    name = 'grasp_nms',
    ext_modules=cythonize("grasp_nms.pyx"),
    include_dirs=[numpy.get_include()],
    install_requires=[
        'numpy',
        'cython'
    ]
)
