from flask import *
import xml.etree.ElementTree as ET
import subprocess
import threading
from lxml import etree #This is for External Entity Expansion (local system files) since this parser is vulnerable to this attack
import xmltodict
import base64
import sys
from StringIO import StringIO

app=Flask(__name__)

@app.route('/')

def home():
	    return """
    <html>
    <head><title>Vulnerable Flask App</title></head>
    <head><title>Welome Rabbit</title></head>
    <body>
        <p><h3>Welcome to Vulnerable Application with XML Vulnerabilities</h3></p>
        <a href="/bla">1. Billion Laugh Attack</a><br>
        <a href="/Quadratic">2. Quadratic Blowup</a><br>
        <a href="/xxe1">3. External Entity Expansion (Local) </a><br>
        <a href="/XXE2">4. External Entity Expansion (Remote) </a><br>
        <a href="/DTD">5. DTD Retrival </a><br>
        <a href="/GZIP">6. GZIP BOMB</a><br>
        <a href="/XPATH">7. XPATH Injection </a><br>
    </body>
    </html>   
    """


@app.route('/bla', methods = ['POST', 'GET'])
def xml():
    parsed_xml = None
    if request.method == 'POST':
        xml = request.form['xml']
        try:
            # return redirect(url_for('new'))
            tree=ET.fromstring(xml)
        except:
            # return "Some shit happened"
            return """Some Shit Happened"""

    else:
        return  """<html>
           <body>
              <form action = "/bla" method = "POST">
                 <p><h3>Billion Laugh Attack</h3></p>
                 <p><h3>Enter xml to parse</h3></p>
                 <textarea class="input" name="xml" cols="160" rows="25"></textarea>
                 <p><input type = 'submit' value = 'Parse'/></p>
              </form>
           </body>
        </html>
        """


@app.route('/new_tab')
def new():
    return "New here"


@app.route('/xxe1',methods=['GET','POST'])
def xxe1():
  if request.method == 'POST':
    xml=request.form.get('xml')
    xml=str(xml)
    print xml #For printing the xml to the console of flask server
    tree=etree.parse(StringIO(xml))   #Since, We are passing a string to etree.parse(), so we need to wrap it in StringIO object https://stackoverflow.com/questions/10457564/error-failed-to-load-external-entity-when-using-python-lxml
    data=etree.tostring(tree,pretty_print=True)
    return data
    # return Response(xml, mimetype='Application/xml')  # To return xml data to user, we need to define the mimetype
  else:
    return """<html>
    <body>
    <h3>Kindly enter the correct XML data. Since, We currently donot validate the xml. And, You can use this application to run/check the system commands like /etc/passwd</h3>
    <form action="/xxe1" method="POST">
    <textarea class="input" name="xml" cols="100" rows="15"></textarea>
    <p><input type='submit' value='Parse'/></p>
    </body>
    """



# @app.route('/xxe2',methods=['GET','POST'])
# def xxe2():
#   if request.method=='POST':

#   else:
#     return """"home""

app.run(debug=True,host="0.0.0.0")
