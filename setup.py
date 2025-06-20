#!/usr/bin/env python3
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

CLASSIFIERS = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Programming Language :: Python :: 3
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Programming Language :: Python :: 3.12
Programming Language :: Python :: 3.13
Programming Language :: Python :: 3 :: Only
Natural Language :: Korean
Development Status :: 5 - Production/Stable
Operating System :: OS Independent
Typing :: Typed
Topic :: Software Development
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Artificial Intelligence
Topic :: Scientific/Engineering :: Information Analysis
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

# import grpc_tools
#
# setuptools.setup(
#     cmdclass={
#         'build_proto_modules': grpc_tools.command.BuildPackageProtos,
#     }
# )

setuptools.setup(
    name="bareun-apis",
    version="0.15.2",
    author="Gihyun YUN",
    author_email="gih2yun@baikal.ai",
    description="The google protobuf and grpc IDL, generated classes of python 3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bareun.ai/",
    download_url="https://pypi.python.org/pypi/bareun-apis",
    project_urls={
        "Bug Tracker": "https://github.com/barrun-nlp/bareun-apis/issues",
        # "Documentation": get_docs_url(),
        "Source Code": "https://github.com/bareun-nlp/bareun-apis",
    },
    license='BSD',
    platform='Independent',
    packages=setuptools.find_packages(),
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
    python_requires='>=3.6',
)
