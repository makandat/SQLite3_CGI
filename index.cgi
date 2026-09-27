#!/usr/bin/env python3
#  SQLite3/index.cgi v2.0
#  http://localhost/cgi-bin/SQLite3/index.cgi
import CGI365Lib as CGI
import SQLite3

if __name__ == "__main__":
  req, res = (CGI.Request(), CGI.Response())
  if req.method == "GET":
    res.sendHtml("./templates/index.html", "utf-8")
  else:
    CGI.Response.status(405, CGI.METHOD_NOT_ALLOWED)
