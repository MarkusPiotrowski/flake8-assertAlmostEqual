"""Setup file for flake8-assertAlmostEqual."""


import setuptools

requires = [
    "flake8 > 3.0.0",
]


flake8_entry_point = 'flake8.extension'

setuptools.setup(
    name="flake8-assertAlmostEqual",
    license="MIT",
    version="0.3.0",
    description="A flake8 plugin to check for the use of round in asserts",
    author="Markus Piotrowski",
    author_email="Markus.Piotrowski@ruhr-uni-bochum.de",
    url="https://github.com/MarkusPiotrowski/flake8-assertAlmostEqual",
    packages=setuptools.find_packages(),
    py_modules=['flake8_assertAlmostEqual'],
    install_requires=requires,
    entry_points={
        flake8_entry_point: [
            'AAE = flake8_assertAlmostEqual:AAE_checker',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
