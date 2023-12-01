import re
import cgi
import json
from jinja2 import Environment, FileSystemLoader
from wsgiref.simple_server import make_server


class Framah:
    def __init__(self, template_folder="templates") -> None:
        self.url_map = []
        self.template_folder = template_folder
        self.env = Environment(loader=FileSystemLoader(template_folder))


    def route(self, rule, method="GET", template=None):

        def decorator(view):
            self.url_map.append((rule, method, view, template))
            return view

        return decorator
    
    def render_template(self, template_name, **context):
        template = self.env.get_template(template_name)
        return template.render(**context).encode("utf-8")

    def __call__(self, environ, start_response):
        body = b"Content Not Found"
        status = "404 Not Found"
        content_type = "text/html"
        #processar o request
        path = environ["PATH_INFO"]
        request_method = environ["REQUEST_METHOD"]

        # Resolver as URLs
        for rule, method, view, template in self.url_map:
            match = re.match(rule, path)
            if match:
                if method != request_method:
                    continue
                views_args = match.groupdict()
                view_result = view(**views_args)

            
                body = view_result.encode("utf-8")

        #criar o repsonse
        headers = [("Content-type", content_type)]
        start_response(status, headers)
       
        return [body]

    def run(self, host="0.0.0.0", port=8000):
        server = make_server(host, port, self)
        server.serve_forever()