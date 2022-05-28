"""
boto3 producer : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html
producer API : https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html

logGenerator function requirements :
- number of records varies by time of day
- 
"""
import time

while True:
    print("ATTEMPT TO PUT 100 records >>> mooping-ecommerce-activities-stream")
    time.sleep(30)