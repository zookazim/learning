import os
from jinja2 import Environment, FileSystemLoader


# Create templates

# Base template
str_base_test = '''
{%- block title %}
----------------------------------
-- {{ title }}
----------------------------------
{% endblock title %}
{%- block body %}
No body in base template
{% endblock body %}
----------------------------------
'''
# Save template
text_file = open("templates/base_test.txt", "w")
n = text_file.write(str_base_test)
text_file.close()

env = Environment(loader=FileSystemLoader('templates'), lstrip_blocks=True,trim_blocks=True)
template = env.get_template('base_test.txt')

print(template.render(title="Parent Template"))

