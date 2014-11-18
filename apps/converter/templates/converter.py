import xmltodict
import json
from django.conf import settings


def input_to_json(filename, name, extension, output_format):
    if extension == 'xml':
        with open(settings.MEDIA_ROOT + '/' + filename, "r") as _in:
            xml_text = _in.read()
        parser = xmltodict.parse(xml_text)
        result = json.dumps(parser)
        output_name = name + '.json'
        with open(settings.MEDIA_ROOT + '/' + output_name, 'w') as out:
            out.write(result)
        return output_name
    if extension == 'xml':
        return filename
