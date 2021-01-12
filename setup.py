from setuptools import setup, find_packages


setup(
    name="morepath_static",
    version="0.2.dev0",
    description=("A demo app for Morepath with static resources"),
    long_description=(
        open("README.rst", encoding="utf-8").read()
        + "\n\n"
        + open("CHANGES.rst", encoding="utf-8").read()
    ),
    author="Morepath developers",
    author_email="morepath@googlegroups.com",
    license="BSD",
    url="https://github.com/morepath/morepath_static",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    keywords="morepath demo",
    install_requires=[
        "morepath>=0.14",
        "more.static",
    ],
    extras_require=dict(
        test=[
            "pytest",
            "pytest-cov",
            "webtest",
        ],
    ),
    entry_points={
        "console_scripts": [
            "morepath_static = morepath_static.__main__:run",
        ]
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "License :: OSI Approved :: BSD License",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
