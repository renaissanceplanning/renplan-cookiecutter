import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{cookiecutter.project_name}}'

print(f"DEBUG: module_name = '{module_name}'")
print(f"DEBUG: regex pattern = {MODULE_REGEX}")

match_result = re.match(MODULE_REGEX, module_name)
print(f"DEBUG: regex match result = {match_result}")

if not match_result:
    print(f'ERROR: "{module_name}" is not a valid Python module name.')
    sys.exit(1)

print("DEBUG: Validation passed, exiting with 0")