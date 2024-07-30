import hashlib
import os

# def generate_addons_xml():
#     addons_xml = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<addons>\n"
#     for addon in os.listdir('.'):
#         if os.path.isdir(addon) and addon != '.git':
#             try:
#                 with open(os.path.join(addon, 'addon.xml'), 'r') as f:
#                     content = f.read()
#                     addons_xml += content.strip() + "\n"
#             except Exception as e:
#                 print(f"Error reading {addon}/addon.xml: {e}")
#     addons_xml += "</addons>\n"

#     with open('addons.xml', 'w') as f:
#         f.write(addons_xml)

def generate_md5():
    md5 = hashlib.md5()
    with open('addons.xml', 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
    with open('addons.xml.md5', 'w') as f:
        f.write(md5.hexdigest())

# generate_addons_xml()
generate_md5()
