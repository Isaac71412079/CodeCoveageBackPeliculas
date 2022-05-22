from flask import jsonify
from utils.constants import *
import re

# Helpers
def error(request):
    message = {
        "message": "Oops! Something went wrong - " + request.url,
        "status": ERROR_CODE,
    }
    response = jsonify(message)
    response.status_code = ERROR_CODE
    return response


def get_field(request, field):
    return request.json.get(field, None)


def remove_oid(string):
    while True:
        pattern = re.compile('{\s*"\$oid":\s*("[a-z0-9]{1,}")\s*}')
        match = re.search(pattern, string)
        if match:
            string = string.replace(match.group(0), match.group(1))
        else:
            return string
