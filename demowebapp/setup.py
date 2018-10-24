import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="demowebapp",
    version="0.0.2",
    author="syeds",
    author_email="syedsalahuddin@hcl.com",
    description="Demo web application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/syedsrepo/clAutomation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts':[
            'demowebapp = demowebapp.__main__:main'
        ]
    },
)
