import setuptools  # type: ignore

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bless",
    version="0.3.0",  # Bumped version for Bleak v1.1.1 compatibility
    author="Kevin Davis",
    author_email="kevincarrolldavis@gmail.com",
    description="A Bluetooth Low Energy Server supplement to Bleak",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kevincar/bless",
    package_data={"bless": ["py.typed"]},
    packages=setuptools.find_packages(exclude=("test", "examples")),
    include_package_data=True,
    install_requires=[
        "bleak>=1.1.1",  # Updated to require Bleak v1.1.1+
        "pywin32;platform_system=='Windows'",
        "dbus_next;platform_system=='Linux'",
        "pysetupdi @ git+https://github.com/gwangyi/pysetupdi#egg=pysetupdi;platform_system=='Windows'",  # noqa: E501
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
