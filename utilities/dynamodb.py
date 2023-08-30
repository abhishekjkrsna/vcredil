import boto3

client = boto3.client('dynamodb')

def create_record(table_name: str, item: dict) -> dict:
    """
    Create a record in dynamodb table
    :param table_name: name of the table
    :param item: record to be created
    :return: return a dictonary with sucess and message
    """    
    try:
        response = client.put_item(
            TableName = table_name,
            Item = item
        )
        return {
            'success': True,
            'response': 'Item successfully stored in table'
        }
    except Exception as e:
        return {
            'success': False,
            'response': str(e)
        }
    
def get_record(table_name: str, value: str) -> dict:
    """
    Get a record from dynamodb table
    :param table_name: name of the table
    :param value: primary key value of the record
    :return: record if found, else None
    :rtype: A dictonary with success and items key    
    """
    try:
        response = client.get_item(
            TableName = table_name,
            Key = {
                'mobile' : {'S' : value}
            }
        )
        return {
            "success": True,
            "items": response.get('Item')
            }
    except Exception as e:
        return {
                "success": False,
                "items": str(e)
            }
 
def delete_record(table_name: str, value: str) -> dict:
    """
    Delete a record from dynamodb table
    :param table_name: name of the table
    :param value: primary key value of the record
    :return: success is true when item successfully deleted from table, else False
    :rtype: a dictonary with success and message key 
    """
    try:
        response = client.delete_item(
            TableName=table_name, 
            Key={
                'mobile': {'S': value}
            })
        return {
                'success': True,
                'message': 'Item successfully deleted from table'
            }
    except Exception as e:
        return {
            'success': False,
            'message': str(e)
        }
   
