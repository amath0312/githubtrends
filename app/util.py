import json
def toJson(obj):
    dict = _object2dict(obj)
    return json.dumps(dict)

def toObj(jsn, module, clazz):
    dict = json.loads(jsn)
    dict['__module_-'] = module
    dict['__class__'] = clazz
    return _dict2object(dict)


def _object2dict(obj):
    #convert object to a dict
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d
 
def _dict2object(d):
    #convert dict to object
    if'__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args
        inst = class_(**args) #create new instance
    else:
        inst = d
    return inst