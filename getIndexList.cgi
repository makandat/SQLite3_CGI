#!/usr/bin/env python3
#  getIndexList.cgi
import CGI365Lib as CGI
import SQLite3

# GET method
def on_GET(req, res):
  db = req.getParam("db")
  rows = SQLite3.query(db, "SELECT name FROM sqlite_master WHERE type='index' ORDER BY name")
  result = []
  for row in rows:
    if row[0].startswith("sqlite_"):
      pass
    else:
      result.append(row[0])
  res.sendJSON(result)
  return

# Start
if __name__ == "__main__":
  req, res = (CGI.Request(), CGI.Response())
  if req.method == "GET":
    on_GET(req, res)
  else:
    CGI.Response.status(405, CGI.METHOD_NOT_ALLOWED)
