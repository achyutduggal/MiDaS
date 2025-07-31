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
    python_requires=">=3.8",
    install_requires=[
        # Core dependencies with exact versions
        'numpy==1.26.4',
        'opencv-python==4.11.0.86',
        
        # PyTorch ecosystem - CUDA 12.1 compatible versions
        'torch==2.3.1',
        'torchvision==0.18.1',
        'torchaudio==2.3.1',
        
        # Model libraries
        'timm>=0.9.12,<1.0.0',
        'antialiased_cnns>=0.3,<0.4'
    ]
)
