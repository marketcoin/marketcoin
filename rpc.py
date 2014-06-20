import requests
import json

call_id = 0

class RPC:
    def __getattr__(self, name):
        def func(*args):
            global call_id
            url = "http://localhost:2736/jsonrpc"
            headers = {'content-type': 'application/json'}
            payload = {
                "method": name,
                "params": args,
                "jsonrpc": "2.0",
                "id": call_id,
            }
            response = requests.post(url, data=json.dumps(payload), headers=headers).json()
            assert response['id'] == call_id
            call_id += 1
            return response['result']
        return func