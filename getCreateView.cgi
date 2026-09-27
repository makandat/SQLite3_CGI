#!/usr/bin/env python3
#  getCreateView.cgi
import CGI365Lib as CGI
import SQLite3

# GET method
def on_GET(req, res):
  db = req.getParam("db")
  name = req.getParam("name")
  sql = SQLite3.getValue(db, f"SELECT sql FROM sqlite_master WHERE name='{name}' and type='view'")
  res.sendJSON(sql)
  return
  
# Start
if __name__ == "__main__":
  req, res = (CGI.Request(), CGI.Response())
  if req.method == "GET":
    on_GET(req, res)
  else:
    CGI.Response.status(405, CGI.METHOD_NOT_ALLOWED)
