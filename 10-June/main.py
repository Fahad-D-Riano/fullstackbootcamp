import psycopg2
from flask import Flask, request

app = Flask("Job site")

items = ["python", "perl", "ruby"]



@app.route("/test")
def testing():
    return """
<html>
  <head>
    <title> Welcome to my website </title>
  </head>


  <body>
    <h1> Introduction </h1>
    My name is Noufal Ibrahim. 

    <h1> Stuff I like </h1>
    Here are some things that I enjoy doing. 
    <ol>
      <li> Programming </li>
      <li> Reading </li>
      <li> Sleeping </li>
      <li> Calligraphy </li>
      <li> Martial arts </li>
    </ol>

    <h1> Contact </h1>
    Thanks for visiting. 
    Follow me on twitter at
    <a href="https://twitter.com/noufalibrahim">@noufalibrahim</a>.
  </body>
</html>
"""

@app.route("/") # decorator
def hello():
    dbconn = psycopg2.connect("dbname=naukri")
    cursor = dbconn.cursor()
    cursor.execute("select title, company_name, jd_text from openings")
    ret = []
    for title, company_name, jd in cursor.fetchall():
        item = f"<b>{title}</b> :: {company_name} <br/> {jd}"
        ret.append(item)
    l = "<hr/>".join(ret)
    return f"""List of jobs is:

    {l}"""

# http://127.0.0.1/add?item=x
@app.route("/add")
def add_item():
    item = request.args.get("item")
    items.append(item)
    return f"No. of items is now {len(items)}"


# https://flask.palletsprojects.com/en/2.0.x/
