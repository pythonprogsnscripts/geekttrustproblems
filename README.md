# GeekTrust Traffic Problem 1
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e4c9ccf45bd94e0b8ed32d9ca4c23ffe)](https://www.codacy.com/manual/pythonprogsnscripts/geekttrustproblems?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=pythonprogsnscripts/geekttrustproblems&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/e4c9ccf45bd94e0b8ed32d9ca4c23ffe)](https://www.codacy.com/manual/pythonprogsnscripts/geekttrustproblems?utm_source=github.com&utm_medium=referral&utm_content=pythonprogsnscripts/geekttrustproblems&utm_campaign=Badge_Coverage)
[![Build Status](https://travis-ci.org/pythonprogsnscripts/geekttrustproblems.svg?branch=master)](https://travis-ci.org/pythonprogsnscripts/geekttrustproblems)
[![language](https://img.shields.io/badge/language-python-yellowgreen)]()

## Lengaburu Traffic

Write code to help King Shan decide which vehicle & orbit he should take to reach Hallitharam quickly. Factors that affect your choice woudl be:

*   Weather
*   Vehicle
*   Speed &
*   Craters

King Shan would like to visit Hallitharam and RK Puram on the same day. Write code to determine which orbits & vehicle he should take to visit both destinations in the quickest possible time.

### Analysis

King wants to visit from one residential area to another residential area.

*   Two different places are connected by orbits
*   Available vehicles for the king is Bike, Tuk Tuk and Supercar
*   The decision on which vechilce or orbit to choose depends on the weather conditions as well and the increase/decrease of craters depending on the mentioned weather conditions

### Steps

This problem has been solved using Python 3.7. There is a bifurcation between source files ad test files.

### CI Pipeline

Used Travis CI as the CI pipeline. The CI pipeline does the below steps:

*   Install necessary python modules
*   Do lint of python code
*   Do lint of markdown code
*   Run unit tests, with code coverage
*   The code coverage and code quality results are published in [codacy][codacy]
*   The build pipeline can be viewed [here][travis]

[codacy]: https://app.codacy.com/manual/pythonprogsnscripts/geekttrustproblems/dashboard
[travis]: https://travis-ci.org/pythonprogsnscripts/geekttrustproblems