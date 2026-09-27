#!/usr/bin/env python3
#  SQLite3/views.cgi
#  http://localhost/cgi-bin/SQLite3/views.cgi
import CGI365Lib as CGI
import SQLite3

res = CGI.Response()

res.sendHtml("./templates/views.html", "utf-8")
