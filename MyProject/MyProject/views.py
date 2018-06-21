from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def test(request):
    return JsonResponse({"sucess":200})



# The jinja library requires a template this is used to render the given json
# into a varying column and row table and the respective table header which
# repeats itself every page with the column width
# The page-break-inside rule eliminates the possiblity of a element being split across pages
temp="""
<!doctype html>
<head>
<style>thead{color:blue;overflow-x: visible !important;margin:0; padding:0;}
table{word-break: break-word;}
tr{page-break-inside: avoid !important;}
table,th,td{border: 1px solid black;border-collapse:collapse;padding:2px;text-align: center;}
table{width:100%}
{% for width in styles %}
  .col{{loop}}{{width}}
{% endfor %}
</style> <meta charset="utf-8"> </head>
<table >
  <thead><div style="overflow-x: visible !important;">
     {% for cell in header %}
       <th width="{{cell.width}}"><b>{{ cell.title }} </b></th>
     {% endfor %}

  </thead>
  <tbody>
  {% for row in fillups %}
    <tr>
      {% for cell in row %}
       {% if loop.index == imageflag %}
            <td><img src="{{cell}}"></td>
       {% else %}
        <td >{{cell}}</td>
       {% endif %}
      {% endfor %}
    </tr>
  {% endfor %}
  </tbody>
</table>
"""

#This is a sample template for any table creation json
display_dictionary={
    "imageflag":2,
    "header":[{"title":"Serial number","width":"10%"},{"title":"நேரம்","width":"15%"},{"title":"எடுத்துக்கொள்ள வேண்டிய உணவு","width":"50%"},{"title":"மருந்து","width":"25%"}],
    "fillups":[["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"],
    ["1","4:30AM - 5:00 AM","Chapathi","OlgredDSR -(1)<br>Eritel 80mg -(1)<br>Galvus 50Mg -(1)<br>"]
    ]

}


from jinja2 import Template
import pdfkit
@csrf_exempt
def test1(request):
    # Initializing the html template to a jinja object
    template = Template(temp)

    # Extracting the request data as a json object
    data = json.loads(request.body)
    #print(data)

    # Render the given json as a html table and returns as a string
    s=template.render(data)
    #If the given json request is not working feel free to test with this json by uncommenting this line
    #s = template.render(display_dictionary)

    #configure the pdf render options as given in "https://wkhtmltopdf.org/usage/wkhtmltopdf.txt"
    option={"--header-html":'file:///C:/Users/User/Desktop/Django_Folder/django_env/MyProject/tamil.html',  #the path to the header html file
    "--header-spacing":15,      #Adds some padding between th eheadr and the body to prevent overlapping
    "--margin-top": "35mm",     #The content spacing to enable ample space for headers and footers
    "--margin-bottom": "15mm",
    'encoding': "UTF-8" }       #The encoding of the pdf contents


    "C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe" # This is the path to wkhtmltopdf.exe
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wktohtml2\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')


    #The function to render thepdf from a string from
    #(<The html string>,<Boolean if false returns the contents as return type OR if true writes to a pdf file specified should be supplied as a path>,<wkhtmltopdf configuration>,<options for pdf styling>)
    pdf=pdfkit.from_string(s, output_path=False ,configuration=config,options=option)


    #configuring the response object
    #filename = "sample_pdf.pdf"
    response = HttpResponse(content_type="application/pdf")
    response.write(pdf)
    return response


import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
def newPdf(request):
    app = QtWidgets.QApplication(sys.argv)
    loader = QtWebEngineWidgets.QWebEngineView()
    loader.setZoomFactor(1)
    loader.page().pdfPrintingFinished.connect(lambda *args: print('finished:', args))
    #loader.load(QtCore.QUrl('https://en.wikipedia.org/wiki/Main_Page'))
    loader.load(QtCore.QUrl('file:\\C:\\Users\\User\\Desktop\\Django_Folder\\django_env\\MyProject\\tamil.html'))

    def emit_pdf(finished):
        loader.show()
        loader.page().printToPdf("test1.pdf")
    loader.loadFinished.connect(emit_pdf)

    app.exec()
    return JsonResponse({"sucess":200})

import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
def pyqttrial(request):

    #loader.load(QtCore.QUrl("file:///C:/Users/User/Desktop/Django_Folder/django_env/index.html"))
    app = QtWidgets.QApplication(sys.argv)
    loader = QtWebEngineWidgets.QWebEngineView()
    loader.setZoomFactor(1)
    loader.page().pdfPrintingFinished.connect(
        lambda *args: print('finished:', args))
    loader.load(QtCore.QUrl('http://www.google.co.in/'))

    def emit_pdf(finished):
        loader.show()
        #loader.page().printToPdf("test2.pdf")
    loader.loadFinished.connect(emit_pdf)

    app.exec()
    #app.exit()
    return JsonResponse({"sucess":200})

@csrf_exempt
def requestjson(request):
    data= json.loads(request.body)
    print(data)
    #print(data['styles'])
    return JsonResponse({"sucess":200})
