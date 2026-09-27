#!/usr/bin/env python3
#  SQLite3/indexes.cgi
#  http://localhost/cgi-bin/SQLite3/indexes.cgi
import CGI365Lib as CGI
import SQLite3

res = CGI.Response()

res.sendHtml("./templates/indexes.html", "utf-8")
