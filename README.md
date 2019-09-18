**Python Serverless Boilerplate**

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

- git clone https://github.com/jkhaui/serverless-python-boilerplate
- cd serverless-python-boilerplate
- npm install

Then, to run and test locally at http://localhost:4000
- serverless offline

To deploy the entire function as part of a CloudFormation stack:
- serverless deploy

Enjoy!