# **Python Serverless Boilerplate**
<img src="https://misc-ddocs.s3-ap-southeast-2.amazonaws.com/py-lambda.png" />

Recently, I've found myself building a backend entirely out of serverless
functions. Using the Serverless framework to bootstrap my workflow, I found 
this starter kit by Postlight which provides quick and simple scaffolding: 
https://github.com/postlight/serverless-babel-starter

Now I'm switching from Node.js to Python which has its own challenges, such as 
large dependencies for data science or machine learning. This boilerplate uses the 
spaCy NLP library to demonstrate how **Lambda layers** can be leveraged to improve 
the development process.

After setting up the repo, send a GET or POST request to the endpoint with the key 
'text' and the value as any body of text, e.g. 'Manchester United have been linked 
with Harry Kane over the years amid the England international's stunning form at 
Tottenham'. The function will extract the names of any people it detects (such as 
'Harry Kane' in the example provided) and return the result in JSON. 🚀

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

Try this sample GET request: 
localhost:4000?text=Manchester%20United%20have%20been%20linked%20with%20Harry%20Kane%20over%20the%20years%20amid%20the%20England%20international%27s%20stunning%20form%20at%20Tottenham

Enjoy!

**Other Notes**
- To demonstrate how layers can be used to offload large dependencies when deploying, 
this example uses the spaCy library and its en_core_web_sm-2.1.0 model.
- Be aware that layers still count towards the 50mb zipped deployment limit; the size 
of the function including the layers is ~40mb).
- The Lambda function is given access to CloudWatch in its IAM role statements. This 
lets it write to CloudWatch logs for easier debugging. Serverless claims that all 
functions have access to CloudWatch logs by default, but for some reason, I didn't observe 
this.
- It also uses the serverless-plugin-warmup to overcome the cold start problem. After 
deployment, the function is automatically invoked once every 5 minutes to reduce any 
noticable latency for the end-user.
- Be wary using Pip on non-Linux systems for packages that contain compiled binary. 
See https://aws.amazon.com/premiumsupport/knowledge-center/lambda-python-package-compatible/
