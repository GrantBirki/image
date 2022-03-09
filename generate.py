from jinja2 import Template
import os

SITE_DIR = f"docs"

def http_template():
    with open(f"template/index.html") as f:
        base = f.read()
    return base

def generate_html(data):
    template = Template(http_template())
    return template.render(list=data)

def main():
    html_ul = ""
    for r, _, f in os.walk(f"{SITE_DIR}/img"):
        for file in f:
            path = os.path.join(r, file).replace(f"{SITE_DIR}/", "")
            html_ul += f'<li><a href="{path}">{path}</a></li>' + "\n   "
    generated_html = generate_html(html_ul)
    with open(f"{SITE_DIR}/index.html", "w") as f:
        f.write(generated_html)

if __name__ == "__main__":
    main()