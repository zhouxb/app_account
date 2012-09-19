from setuptools import setup, find_packages

setup(
    name = "app_account",
    version = "0.1",
    author = "zhou.xingbo",
    author_email = "zhou.xingbo@gmail.com",
    description = "a Django user account app",
    long_description = open("README.md").read),
    license = "MIT",
    url = "https://github.com/zhouxb/app_account",
    packages = find_packages(),
    install_requires = [
        #"south",
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
