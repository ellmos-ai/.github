import markdown
import os
import subprocess

with open('profile/README.md', 'r', encoding='utf-8') as f:
    content = f.read()

html_body = markdown.markdown(content, extensions=['tables', 'fenced_code', 'toc'])

full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{
    background-color: #0d1117;
    color: #c9d1d9;
    font-family: -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",Helvetica,Arial,sans-serif;
    max-width: 1000px;
    margin: 0 auto;
    padding: 32px;
}}
a {{ color: #58a6ff; }}
p[align="center"] {{ text-align: center; }}
table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
th, td {{ border: 1px solid #30363d; padding: 6px 13px; }}
th {{ background-color: #161b22; }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

html_path = os.path.abspath('test_render.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"Saved {html_path}")
