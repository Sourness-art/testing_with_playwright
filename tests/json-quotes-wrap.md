Two issues with answers given so far, if , 
for instance, one streams such non-standard JSON. 
Because then one might have to interpret an incoming string (not a python dictionary).

Issue 1 - demjson: With Python 3.7.+ and using conda I wasn't able to install 
demjson since obviosly it does not support Python >3.5 currently. 
So I need a solution with simpler means, for instance astand/or json.dumps.

Issue 2 - ast & json.dumps: If a JSON is both single quoted and contains a string in at least one value, 
which in turn contains single quotes, the only simple yet practical solution I have found is applying both:

In the following example we assume line is the incoming JSON string object :

>>> line = str({'abc':'008565','name':'xyz','description':'can control TV\'s and more'})

Step 1: convert the incoming string into a dictionary using ast.literal_eval()
Step 2: apply json.dumps to it for the reliable conversion of keys and values, but without touching the contents of values:

> import ast
> import json
>> print(json.dumps(ast.literal_eval(line)))

{"abc": "008565", "name": "xyz", "description": "can control TV's and more"}
json.dumps alone would not do the job because it does not interpret the JSON, but only see the string. 
> Similar for ast.literal_eval(): although it interprets correctly the JSON (dictionary), it does not convert what we need.