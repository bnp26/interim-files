import json
import pdb

def json_crawl(obj, ref, storage=dict(), missing=list(), path=""):
    if type(obj) not in [list, dict]:
        return obj, missing

    for key, val in obj.iteritems():
	if key in ref:
	    if type(val) is dict:
                new_path = ""
                if path == "":
                    new_path = key
                else:
                    new_path = path + "." + key
		a, b = json_crawl(val, ref[key], {}, missing, new_path)
                storage[key] = a
	    elif type(val) is list and val:
                if path == "":
                    new_path = key
                else:
                    new_path = path + "." + key
                temp_obj = {}
                for i in val:
                    a, b = json_crawl(i, ref[key][0], {}, missing, new_path)
                    temp_obj.update(a)
                storage[key] = temp_obj
	    else:
                storage[key] = val
        else:
            missing.append((path, key, ))
	    if type(val) is dict:
                new_path = ""
                if path == "":
                    new_path = key
                else:
                    new_path = path + "." + key
		a, b = json_crawl(val, ref[key], {}, missing, new_path)
                storage[key] = a
	    elif type(val) is list and val:
                new_path = ""
                if path == "":
                    new_path = key
                else:
                    new_path = path + "." + key 
                if type(storage) is list:
		    a, b = json_crawl(val[0], ref[0], {}, missing, new_path)
                    storage.append(a)
                else:
                    a, b = json_crawl(val[0], ref[0], {}, missing, new_path)
                    storage[key] = a
            else:
                storage[key] = val
    return storage, missing

ref_file = open("doordash_sample.json", "r")
payload_file = open("doordash_example.json", "r")

ref_json = json.loads(ref_file.read())
payload_json = json.loads(payload_file.read())

ref_file.close()
payload_file.close()
obj, missing = json_crawl(payload_json, ref_json)
print "reference: \n{}".format(ref_json)
print "\n\n"
print "payload built obj: \n{}".format(obj)
print "\n\n"
print "missing values:"
for path, key in missing:
    print "path: {0}\tkey: {1}".format(path, key)
print "\n\n"
print "missing values list:\n{}".format(missing)
