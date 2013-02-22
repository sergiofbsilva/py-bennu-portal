# Create your views here.
from django.template import loader
from django.shortcuts import render_to_response
from domain.models import Host
from django.http import HttpResponse
from bennuportal.settings import HOST

def generate_header_entry(hostname, themename, cssfilename, media = None):
  css_entry_href = "http://%s:8001/static/themes/%s/%s" % (hostname, themename, cssfilename);
  media_string = 'media="%s"' %  media if media else ""
  return '\'<link rel="stylesheet" type="text/css" href="%s" %s/>\'' % (css_entry_href, media_string)

def generate_header(hostname, themename):
    imports = []
    script = []
    script.append('<script type="text/javascript">(function() {')
    script.append("var imports = [")
    imports.append(generate_header_entry(hostname, themename, "print.css", "print"))
    imports.append(generate_header_entry(hostname, themename, "screen.css", "screen"))
    imports.append(generate_header_entry(hostname, themename, themename + ".css"))
    script.append(",".join(imports))
    script.append("];")
    script.append("imports.forEach(function (imp) { $('head').append(imp); } ) })();")
    script.append('</script>')
    return ''.join(script)
      

def index(request, hostname):
  host = Host.objects.get(hostname__contains=hostname)
  template_name = "menu_dot_clean.html" if "ash" in hostname else "menu.html"
  html = loader.render_to_string(template_name, 
                                  { 'hostname' : "http://" + hostname + ":8001",
                                     #'apps' : host.apps.all()
                                     'menus' : map(lambda x : x.menus.all()[0].links.all()[0], host.apps.all()),
                                  })
  response = HttpResponse(html, content_type="text/html; charset=utf-8")
  response["Access-Control-Allow-Origin"] = "*"
  return response

def head(request, hostname):
  print(hostname);
  host = Host.objects.get(hostname__contains=hostname);
  script_header = generate_header(hostname, host.theme.name);
  response = HttpResponse(script_header, content_type="text/html; charset=utf-8")
  response["Access-Control-Allow-Origin"] = "*"
  return response