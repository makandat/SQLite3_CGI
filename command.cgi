#!/usr/bin/env python3
#  command.cgi
import CGI365Lib as CGI
import SQLite3

if __name__ == "__main__":
  req, res = (CGI.Request(), CGI.Response())
  if req.method == "GET":
    res.sendHtml("./templates/command.html", charset="utf-8")
  else:
    CGI.Response.status(405, CGI.METHOD_NOT_ALLOWED)

