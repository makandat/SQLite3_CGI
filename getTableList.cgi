#!/usr/bin/env python3
#  getTableList.cgi
import CGI365Lib as CGI
import SQLite3

def log(msg):
  PATH = '/var/www/data/log.txt'
  with open(PATH, "a") as f:
    f.write(msg)
  return

# GET method
def on_GET(req, res):
  db = req.getParam("db")
  rows = SQLite3.query(db, "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
  result = []
  for row in rows:
    if row[0].startswith("sqlite_"):
      pass
    else:
      result.append(row[0])
      log(row[0])
  res.sendJSON(result)
  return

# Start
if __name__ == "__main__":
  req, res = (CGI.Request(), CGI.Response())
  if req.method == "GET":
    on_GET(req, res)
  else:
    CGI.Response.status(405, CGI.METHOD_NOT_ALLOWED)
