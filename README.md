# Making Parameters Configurable

First Create a new File ```cofig.json```

Write all parameters.

```python
{
    "params":
    {
        "local_server":"True",
        "local_uri":"mysql+pymysql://root:@localhost/myresume",
        "prod_uri":"mysql+pymysql://root:@localhost/myresume",
        "ins_uri":"https://www.instagram.com/__muhammad_tariq/",
        "fb_uri":"https://www.facebook.com/muhammad6t",
        "link_uri":"https://www.linkedin.com/in/muhammad3/",
        "twitter_uri":"https://twitter.com/_muhammad_tariq"

    }
}
```


## Change the main.py File
Open the ```json``` File. Type

```python
# Open Config.json file with read mode
with open('templates\config.json','r') as c:
    params = json.load(c)["params"]
local_server = True

app = Flask(__name__) #creating the Flask class object   


if(local_server):
    # configure the SQL database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']

else:
    # configure the SQL database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']
```

## Pass Parms
```
return render_template('index.html', params=params)
```
## write params in any HTML file
```
{{params['twitter_uri']}}
```
