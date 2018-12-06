import json

def to_ascii(json_obj):
    json_str = json.dumps(json_obj).replace('\r\n', '')
    json_str = json_str.decode('unicode_escape').encode('ascii','ignore')
    json_str = json_str.replace('\r\n', '')
    return json.loads(json_str) 
string = ""
with open("json_unicode.json", "r") as f:
    string = f.read()
    print string.decode('unicode_escape').encode('ascii','ignore')
