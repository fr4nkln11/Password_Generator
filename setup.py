# Copyright (c) 2020 Franklin Ikeh

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import setuptools
import os

libFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = libFolder + '/requirements.txt'
install_requires = [] # Examples: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

randomchar_classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Development Status :: 3 - Alpha",
    # Indicates who your project is intended for
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
]

setuptools.setup(
    name="password_generator",
    version="1.2.7",
    author="Franklin Ikeh",
    author_email="ikehfranklind3c0d3r@gmail.com",
    description="Simple Password Generator made with the randomchar module",
    long_description=long_description,
    install_requires=install_requires
    long_description_content_type="text/markdown",
    url="https://github.com/fr4nkl1n-1k3h/Password_Generator",
    keywords=["random, strings, digits, characters, tools, module, generator"],
    classifiers=randomchar_classifiers,
    python_requires=">=3.6, <4",
    project_urls={  # Optional
        "Bug Reports": "https://github.com/fr4nkl1n-1k3h/Password_Generator/issues",
        "Source": "https://github.com/fr4nkl1n-1k3h/Password_Generator/",
    },
)
