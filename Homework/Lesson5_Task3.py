import re

text = """<!DOCUTYPE html>

<html lang="en"><head>
    <meta charset="UTF-8">
    <title>My super star task</title>
</head>
<body>
    <div id="block-with-links">
        <div id="google">
            <a href="www.google.com">
                Google
            </a>
        <div>
        <div id="facebook">
            <a href="http://facebook.com/dign-in">
                Facebook
            </a>
        </div>
            <div id="amazon">
                <a href="amazon.com">
                    Amazon
                </a>
            </div>
        </div>
    </div>

</div></body></html>"""

pattern = r"id=\"([^b].+)\">\s+<.+\"(?:.+[/.]|.{0})(.+\..{3}).*\">\s+(.+)"

print(re.findall(pattern, text))
