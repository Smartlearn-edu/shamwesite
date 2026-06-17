import re
import urllib.parse

with open('plans.html', 'r', encoding='utf-8') as f:
    content = f.read()

msgs = [
    'السلام عليكم، أريد الاستفسار عن باقة "التعليم المنهجي"',
    'السلام عليكم، أريد الاستفسار عن باقة "التعليم المنهجي الخاص"',
    'السلام عليكم، أريد الاستفسار عن باقة "التعليم المفتوح الخاص"'
]

def repl(match):
    global msgs
    if msgs:
        msg = msgs.pop(0)
        encoded = urllib.parse.quote(msg)
        return f'href="https://wa.me/491578303030?text={encoded}" class="w-full'
    return match.group(0)

# The buttons I created have `class="w-full` immediately after the href.
content = re.sub(r'href="https://wa.me/491578303030" class="w-full', repl, content)

with open('plans.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced whatsapp links successfully")
