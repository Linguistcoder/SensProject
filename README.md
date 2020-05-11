# Sens graf web-app test
Simple web application which shows a generated sine wave


## Table of context
* Requirements
* Getting started
* Use cases
* Testing
* Author
* Other comments

## Requirements
The web application needs the following to run:
* [Python][Python] 3.7+
    * [Flask][Flask] 1.1.2+
    * [Matplotlib][mpl] 3.2.1+

[Python]: https://www.python.org/
[Flask]: https://flask.palletsprojects.com/en/1.1.x/
[mpl]: https://matplotlib.org/

Other requirements are usually included in above libraries.
More information in requirement.txt

## Getting Started
The repository includes the following files relevant for running the app:
* app.py 
* config.py
* test.py
* templates/graf.html
* requirements.txt

Make sure you have access to all the files before running the app.

The app can be run in the terminal by running app.py:
```
python app.py
```
You can then go to endpoint http://localhost:5000/graf
which will show a graph with a 1Hz frequency sine wave. 

The frequency of the graph can be changed by the argument _frekvens_:
* http://localhost:5000/graf?frekvens=2  will show 2Hz sine wave
* http://localhost:5000/graf?frekvens=3 will show 3Hz sine wave

http://localhost:5000 will redirect to http://localhost:5000/graf

## Use case
### Getting sine wave graph
The use case starts with the user wanting a sine wave graph.
The user goes to webpage to get graph, which is generated by the system.
The use case ends when the graph is displayed on screen. 

**Actor**: The user

**Basic flow**:
1. User opens webpage
2. System generates graph with default frequency or as defined by argument _frekvens_

**Goal**: Displayed sine wave graph with desired frequency.

## Testing
The code can be tested by test.py.

Test.py contains two unittest for http status and mime type.

The test module is run by: 
```
python test.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.475s

OK

```
or include -v to get more information about tests
```
python test.py -v

test_http_status (__main__.TestGraf)
Test if http status is 200 ... ok
test_mime_type (__main__.TestGraf)
Test if plot mime type is 'image/png' ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.592s

OK

```

## Author
* **Author:** Nathalie Carmen Hau Sørensen 
* **Email:** nathalie.soerensen@gmail.com
* **Date:** 5/11/2020

## Other Comments
This project was made as a test for Sens.

I did all the tasks - including the 3rd secondary task. 