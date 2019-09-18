# **Python Serverless Boilerplate**
<img src="https://misc-ddocs.s3-ap-southeast-2.amazonaws.com/py-lambda.png" />

Recently, I've found myself building a backend entirely out of serverless
functions. Having used the Serverless framework to bootstrap my workflow, 
I found this starter kit by Postlight which proved even more helpful for 
a quick and simple scaffolding: https://github.com/postlight/serverless-babel-starter

Now I'm switching over to Python and found it has its own unique challenges, 
such as dealing with large libraries used for data science or machine learning. 
Also, Serverless isn't as well integrated with Pip as it is with NPM; therefore, 
there's more reliance on plugins such as serverless-python-requirements. 
This boilerplate will hopefully make it simpler to deploy your Python code 
to Lambda! 🚀

**Instructions**
Ensure that you have Node.js, NPM, and the Serverless Framework installed. 
Also ensure that your **AWS credentials are configured**. If in doubt, follow 
these steps: https://serverless.com/framework/docs/providers/aws/guide/quick-start/

> git clone https://github.com/jkhaui/serverless-python-boilerplate
> cd serverless-python-boilerplate
> npm install

Then, to run and test locally at http://localhost:4000
> serverless offline

To deploy the entire function as part of a CloudFormation stack:
> serverless deploy

Enjoy!

**Other Tips**
- Clone the spacy branch for an example of a serverless machine learning model 
which is less than 1mb in size thanks to Lambda layers (be aware that layers still 
count towards the 50mb zipped deployment limit; the size of the function including 
the layers is ~40mb).
- The Lambda function is given access to CloudWatch in its IAM role 
statements. This lets it write to CloudWatch logs for easier debugging. Serverless 
claims that all functions have access to CloudWatch logs by default, but for some 
reason, I didn't observe this.
