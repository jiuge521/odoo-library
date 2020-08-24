#!"D:\DevelopingSoftware\PyCharm Community Edition 2020.1.3\PycharmProjects\odoo-12.0.post20200812\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'Mako==1.0.4','console_scripts','mako-render'
__requires__ = 'Mako==1.0.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Mako==1.0.4', 'console_scripts', 'mako-render')()
    )
