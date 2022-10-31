import docx
import json
from pdf2docx import Converter
from simplify_docx import simplify
import initialSetup

input_file = ""
#input_file = r"C:\Users\aksha\Downloads\SQL - Quick Guide.pdf"

file_name = input_file.split('\\')[-1]
output_folder = "Docx"
output_docx_file = f"{output_folder}\{file_name}.docx"
output_json_file = f"{output_folder}\{file_name}.json"

initialSetup.createDocxFiles(output_folder)
initialSetup.emptingDocxFolder(output_folder)

docx_converted_file = Converter(input_file)
docx_converted_file.convert(output_docx_file, start=0, end=None)
docx_converted_file.close()

# read in a document
docx_data = docx.Document(output_docx_file)
# coerce to JSON using the standard options
docx_data_as_json = simplify(docx_data)
# or with non-standard options
docx_data_as_json = simplify(docx_data,{"remove-leading-white-space":False})

# Serializing json
json_object = json.dumps(docx_data_as_json, indent=4)
# Writing to sample.json
with open(output_json_file, "w") as outfile:
    outfile.write(json_object)
