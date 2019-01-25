# AdvanceLocal excercise

To start off, the overall goal is to get familiar with Chalice,
https://github.com/awslabs/chalice
I spent some time building an environment via their tutorial and successfully implemented Chalice.

1) API status:\
To display the API status, I am using httpie to call the URL, also from the chalice github page.
```
http https://api.nytimes.com/svc/topstories/v2/science.json?api-key=your-key
```
This will return the details of the API (including date, content-type, server, etc.) before displaying the actual results of the API.

2) Publicly available data into something fun:\
So I just built a functioning Chalice service, and in the process created AWS IAM user for the access key and secret. Now on to consuming some public data. 
One of the first questions I wanted to ask, are we constricted to using Chalice for this use case? It would be simpler in my mind to put together something in Python to access different APIs and directly return a response with set parameters.

The question that I wanted to answer was What is the most popular news articles that contain a keyword (i.e. Tesla) for a given date.

So I made an account on https://newsapi.org for an api code.
And using jupyternotebook to test python code, I am able to query successfully.
Next steps would be porting the working code into Chalice

3) Upload PNG image to S3\
The first thing I thought when reading this, is that this code challenge wants me to create a website?! 
Or maybe it's looking to see if I have an existing website on AWS that has images in S3 buckets. 
Well the answer is no, so I just uploaded a png image of a tree to an S3 bucket that I just created.\
Here is the link
```
https://s3.us-east-2.amazonaws.com/advancelocal/png/tree.png
```
Unfortunately, it only has a tree, and if I were have it in a webpage the img src would be the mentioned link.

Daniel Tang
