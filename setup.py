import setuptools

setuptools.setup(
    name="krutils",
    version="0.20230411.1644",
    author="bonfireof",
    author_email="bonfireof@gmail.com",
    description="Some utils for me.",
    url="https://github.com/bonfireof/krutils",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    # package_dir={"": "krutils"},
    # packages=setuptools.find_packages(where="krutils"),
    package_dir={"krutils": "krutils"},
    packages=["krutils"],
    python_requires=">=3.0",
    install_requires=[
        "PyMySQL>=1.0.3"
    ]
)
