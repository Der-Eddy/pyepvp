![logo](logo.png)

[![Build Status](https://img.shields.io/pypi/v/pyepvp.svg)](https://pypi.python.org/pypi/pyepvp) [![Build Status](https://travis-ci.org/Der-Eddy/pyepvp.svg)](https://travis-ci.org/Der-Eddy/pyepvp)  [![Doc Status](https://readthedocs.org/projects/pyepvp/badge/?version=latest)](https://pythonhosted.org/pyepvp/)  [![Issues](https://img.shields.io/github/issues/Der-Eddy/pyepvp.svg)](https://github.com/Der-Eddy/pyepvp/issues)  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Der-Eddy/pyepvp/blob/master/LICENSE)  
A Python API based on the idea of [.NET epvpapi](https://github.com/Mostey/epvpapi)  
Currently in planning phase, let me know if you have any idea for my project!




Requirements
-------------

First of all, you'll need Python >3.4 and some Packages from PyPI, easily installed with pip:

    pip install requests
    pip install PyExecJS
    pip install cfscrape

(OPTIONAL)You will also need to install NodeJS, if you want to bypass the Cloudflare Check  
Install Instructions can be found [here](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager#debian-and-ubuntu-based-linux-distributions)


Samples and Usage
-------------
For that, you should currently take a look at `test.py`  

    import pyepvp
    eddy = pyepvp.session("Der-Eddy", passwordmd5hash, True, secretWord)
    print (eddy.securityToken)
    
    eddy.logout()
    guest = pyepvp.session("guest")
    print (guest.securityToken)


ToDo
-------------
* Add more functionality (TBM, Thread/Post methods and such)
* Update the documentation
* Make a python package out of it (So you can install it through pip)


License
-------------

    The MIT License (MIT)

    Copyright (c) 2015 - 2016 Der-Eddy

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
