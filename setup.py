import setuptools
setuptools.setup(
    name="altered_midas",
    version="0.0.1",
    author="Chris Careaga",
    author_email="careagc256@gmail.com",
    description="",
    url="",
    packages=setuptools.find_packages(),
    license="",
    python_requires=">3.6",
    install_requires=[
        'numpy>=1.23.5',
        'opencv-python>=4.8.0.76',
        'torch>=2.0.1',
        'torchvision>=0.15.2',
        'timm>=0.6.12'
    ]
)
