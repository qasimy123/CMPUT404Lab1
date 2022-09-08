# CMPUT404 Lab 1

## Question 1: What is your GitHub URL?

_https://github.com/qasimy123/CMPUT404Lab1_

## Question 2: What version is the requests library installed on the system?
2.24.0

## Question 3: What version is the requests library installed in the virtualenv?
2.28.1

## Question 4: What is the difference between the virtual environment and the not virtual environment python?
The virtual environment uses seperate libraries and packages from the system python. This means that the virtual environment can have different versions of the same library or additional packages than the system python. This is helpful for sepearing dependencies between projects, if you have a project that requires a specific version of a library or package, you can create a virtual environment with that specific version of the library or package.

## Question 5: What status code is returned for http://google.com ? What URL must you visit to get a 200 status code?
The status code returned is 301. The URL that must be visited to get a 200 status code is http://www.google.com/
## Question 6: What status code is returned for http://google.com/teapot? Is it the one returned by curl -i or curl -iL? What happens when you curl http://www.google.com/teapot?
The status code returned is 301. Both curl -i and curl -iL return the same status code. When you curl http://www.google.com/teapot, the status code returned is 418.

## Question 7: What changed in the output of https://webdocs.cs.ualberta.ca/~hindle1/1.py when you used -X POST? What is this method useful for?

<DL>
<DT>X: <i>&lt;type 'instance'&gt;</i>
<DD>MiniFieldStorage('X', 'Y')
</DL>

It is useful for sending data to the server.

## Question 8: What is the raw URL to your Python script on GitHub?

https://gist.githubusercontent.com/qasimy123/2ae16c2de74725cb2d0d947ed5d96164/raw/downloaditself.py