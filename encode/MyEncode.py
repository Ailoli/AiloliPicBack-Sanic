import json

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        # if isinstance(obj, bytes):
        #     return str(obj, encoding='utf-8');
        temp = {}
        for item in obj:
            if isinstance(obj[item], bytes):
                temp[item] = str(obj[item], encoding='utf-8')
            else:
                temp[item] = str(obj[item])
        return temp
        # return json.JSONEncoder.default(self, obj)