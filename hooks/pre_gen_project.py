import re
import sys
import traceback

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{cookiecutter.project_name}}'

try:
    MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
    module_name = '{{cookiecutter.project_name}}'

    print(f"DEBUG: module_name = '{module_name}'")

    if not re.match(MODULE_REGEX, module_name):
        print(f'ERROR: "{module_name}" is not a valid Python module name.')
        sys.exit(1)
except Exception as e:
    print(f"EXCEPTION in hook: {e}")
    traceback.print_exc()
    sys.exit(1)