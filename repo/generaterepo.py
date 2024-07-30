# generate_repo.py
import os
import hashlib

def generate_md5(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()

def generate_addons_xml(addons_folder):
    addons_xml = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<addons>\n'

    for addon in os.listdir(addons_folder):
        addon_path = os.path.join(addons_folder, addon)
        if os.path.isdir(addon_path):
            addon_xml_path = os.path.join(addon_path, 'addon.xml')
            if os.path.exists(addon_xml_path):
                with open(addon_xml_path, 'r', encoding='utf-8') as f:
                    addon_xml_content = f.read().strip()
                    addons_xml += addon_xml_content + '\n\n'

    addons_xml += '</addons>\n'
    with open(os.path.join(addons_folder, 'addons.xml'), 'w', encoding='utf-8') as f:
        f.write(addons_xml)
    
    with open(os.path.join(addons_folder, 'addons.xml.md5'), 'w', encoding='utf-8') as f:
        f.write(generate_md5(os.path.join(addons_folder, 'addons.xml')))

generate_addons_xml('D:\Web Series\hometheater')
