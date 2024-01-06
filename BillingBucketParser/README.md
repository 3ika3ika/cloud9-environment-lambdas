This function parses data .csv files in s3 bucket and test it against rules.

Create BoilerPlate Lambda Fuction (in this example runtime: python3.9)
Create two S3 buckets: one to upload .csv files and another bucket to store except files
Download function to the Cloud9 environment
Copy/paste the code to your lambda_function.py (+ template.yaml and event.json)
Test the function by typing in terminal while being in the folder containing the function >> sam local invoke -e event.json
If working, then proceed to next step
Upload to Lambda 
Go to AWS Management Console / Lambda / Configuration / and give appropriate permissions to the IAM role (in this example S3FullAccess)
