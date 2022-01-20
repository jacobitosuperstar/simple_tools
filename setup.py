from setuptools import setup

setup(
    name='simple_tool-jacobitosuperstar',
    version='0.0.0',
    author='Jacobo Mateo Bedoya Oquendo',
    author_email='jacobobedoya@gmail.com',
    description='Simplified implementations of the more complex parts of the Python Library',
    long_description='Simplified implementations of the more complex parts of the Python Library',
    long_description_content_type="text/markdown",
    url='https://github.com/jacobitosuperstar/simple_tools',
    project_urls={
        "Bug Tracker": "https://github.com/jacobitosuperstar/simple_tools/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires = ">=3.8",
)
