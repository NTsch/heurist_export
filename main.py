import subprocess
import json
import xml.etree.ElementTree as ET
import requests

url = "https://heurist.huma-num.fr/heurist/api/stutzmann_himanis/records/98012"
xml_file_url = "http://localhost:8080/rest/db/niklas/import-test.xml"

# Execute the curl command using subprocess
result = subprocess.run(["curl", "-X", "GET", url], capture_output=True, text=True)

# Check the command's output
if result.returncode == 0:
    # Parse the JSON response
    response = json.loads(result.stdout)

    # Extract the value of rec_Title
    rec_title = response["rec_Title"]

    # Create the XML element
    tei_pers_name = ET.Element("tei:persName")
    tei_pers_name.text = rec_title

    # Create the root element and add the tei_pers_name as a child
    root = ET.Element("root")
    root.append(tei_pers_name)

    # Create the XML tree
    tree = ET.ElementTree(root)

    # Save the XML tree to a file
    tree.write("import-test.xml")

    # Send a POST request to upload the XML file
    with open("import-test.xml", "rb") as file:
        response = requests.post(xml_file_url, files={"file": file})

    if response.status_code == 201:
        print("XML file uploaded successfully!")
    else:
        print("An error occurred while uploading the XML file.")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
else:
    print("An error occurred while executing the command:")
    print(result.stderr)
