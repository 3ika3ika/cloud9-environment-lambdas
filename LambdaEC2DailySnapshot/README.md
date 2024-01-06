This function creates a snapshot of EBS volume (most commonly of an EC2 instance). 

Create BoilerPlate Lambda Fuction (in this example runtime: python3.9)
Download it to the Cloud9 environment
Copy/paste the code to your lambda_function.py (+ template.yaml and event.json)
Test the function by typing in terminal while being in the folder containing the function >> sam local invoke -e event.json
If working, then proceed to next step
Upload to Lambda 
Go to AWS Management Console / Lambda / Configuration / and give appropriate permissions to the IAM role (in this example EC2FullAccess)
Add Trigger EventBridge (CloudWatch Events) and name the trigger and give rate 