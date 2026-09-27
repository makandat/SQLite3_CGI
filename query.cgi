#!/usr/bin/env python3
#  query.cgi
import CGI365Lib as CGI
import SQLite3

# GET method
def on_GET(req, res):
  res.sendHtml("./templates/query.html", charset="utf-8")
  return
  
 # Start
if __name__ == "__main__":
  req, res = (CGI.Request(), CGI.Response())
  if req.method == "GET":
    on_GET(req, res)
  else:
    CGI.Response.status(405, CGI.METHOD_NOT_ALLOWED)
