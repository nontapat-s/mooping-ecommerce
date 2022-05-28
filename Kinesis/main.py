import time
import boto3


if __name__=='__main__':
    kinesis_client = boto3.client('kinesis')

    while True:
        
        # generate orders
        records = []
        
        ''' 
        === 1 record format === 
            {
                'Data': b'bytes',               # this could be anything, we might do json
                'ExplicitHashKey': 'string',
                'PartitionKey': 'string'
            }
        '''

        # call put_records API
        response = kinesis_client.put_records(
        Records=[
            # list of many records
        ],
        StreamName='string'
        )
        time.sleep(30)