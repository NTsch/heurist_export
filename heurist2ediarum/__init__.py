from flask import Flask, request, Response
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    # Get the search query from the URL parameter '?q='
    query = request.args.get('q', '[{"t":"10"},{"sortby":"t"}]')

    # REST API URL
    api_url = f"https://heurist.huma-num.fr/heurist/api/records?db=stutzmann_himanis&q={query}"

    # Make a GET request to the REST API
    response = requests.get(api_url)

    # Get the JSON response from the API
    json_response = response.json()

    # Process the JSON response as per your requirements
    # ...

    # Generate XML content
    root = ET.Element('ul')
    for record in json_response['records']:
        record_elem = ET.SubElement(root, 'li', id=str(record['rec_ID']))
        title_elem = ET.SubElement(record_elem, 'span')
        title_elem.text = record['rec_Title']

    xml_content = ET.tostring(root, encoding='utf-8', xml_declaration=True)

    # Set the response headers for XML content
    headers = {'Content-Type': 'application/xml'}

    # Return the XML content as a Flask response
    return Response(xml_content, headers=headers)