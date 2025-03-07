from django.shortcuts import render
from django.http import HttpResponse

def chek(request):
    html_content = """
    <html>
        <head>
            <title>Моя HTML-сторінка</title>
        </head>
        <body>
            <h1>Привіт, світ!</h1>
            <p>Це простий HTML-відповідь з Django.</p>
        </body>
    </html>
    """
    return HttpResponse(html_content)
