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
        
        # PyTorch ecosystem - CUDA 12.4 compatible versions (exact matching)
        'torch==2.4.1',
        'torchvision==0.19.1',
        'torchaudio==2.4.1',
        
        # Model libraries - updated for compatibility
        'timm>=0.9.16,<1.0.0',  # Updated for PyTorch 2.4 compatibility
        'antialiased_cnns>=0.3,<0.4'
    ]
)
