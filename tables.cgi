#!/usr/bin/env python3
#  SQLite3/tables.cgi
#  http://localhost/cgi-bin/SQLite3/table.cgi
import CGI365Lib as CGI
import SQLite3

res = CGI.Response()
res.sendHtml("./templates/tables.html", "utf-8")
