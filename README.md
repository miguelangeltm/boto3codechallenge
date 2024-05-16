# boto3codechallenge

Code Challenge:
Scripts in Python using boto3, pep8 is a plus, each script must have unit test and a short description and usage information.
The aim of this exercise is to check general knowledge related to Python, AWS and boto3, those are some examples you could implement:
Check if the s3 buckets have public access, if that is the case remove it to avoid undesired access.

## Installation
- Clone this repository: ```git clone  https://github.com/miguelangeltm/boto3codechallenge.git```
- Navigate to the project directory: ```cd boto3codechallenge```
- Install the dependencies: ```pip install -r requirements.txt```

## Usage
- Just run the main.py file ;) ```python main.py```

This is an example with three buckets: one has a public access policy, another does not have a public access policy, and the third has no policies at all (e.g., the CloudFormation bucket templates cf-templates-13hdy9bp6587g76-eu-west-1).

<img width="1200" alt="image" src="https://github.com/miguelangeltm/boto3codechallenge/assets/43521047/8faba723-8f87-4275-98c4-cf7f854349aa">

Public Access policies looks like this:

<img width="1200" alt="image" src="https://github.com/miguelangeltm/boto3codechallenge/assets/43521047/c6a996f2-e396-4c3e-8ad3-028bd2b5d95a">


<img width="1200" alt="image" src="https://github.com/miguelangeltm/boto3codechallenge/assets/43521047/59ffecc4-1a71-494a-b457-976544071fd7">

After script execution:

<img width="1200" alt="image" src="https://github.com/miguelangeltm/boto3codechallenge/assets/43521047/1d2dc47a-1410-47b1-96bb-f57331a49a10">




