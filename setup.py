from setuptools import setup, find_packages

setup(
    name="pyemail",
    version="1.0",
    author="zhipengye",
    author_email="939647181@qq.com",
    description="A simple email sending tool.",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.6',
)