====================
json-python-coverage
====================

.. image:: https://travis-ci.org/CZ-NIC/json-python-coverage.svg?branch=master
    :target: https://travis-ci.org/CZ-NIC/json-python-coverage

.. image:: https://codecov.io/gh/CZ-NIC/json-python-coverage/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/CZ-NIC/json-python-coverage

JavaScript tool for converting json coverage report to format used by
Python coverage.

------------
Installation
------------

This package is indetended to be installed globally, so that it can be
easily executed via CLI.

::

    npm i -g json-python-coverage

-----
Usage
-----

::

    json-python-coverage <json_filename>

=============== =============================================== =============
Positionals:
=============== =============================================== =============
json\_filename  path to coverage-summary.json                   [string]
|
**Options:**
--version       Show version number                             [boolean]
--fail, -f      coverage fail threshold                         [number] [default: 0]
--regex, -r     path regex for reported files                   [string] [default: ""]
-h, --help      Show help                                       [boolean]
=============== =============================================== =============

-----
Tests
-----

All modules (anything other than index.js) should include unit tests.
Tests are written using jest.

To run tests in terminal:

::

    npm run test
