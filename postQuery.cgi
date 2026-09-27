#!/usr/bin/env python3
#  postQuery.cgi
import CGI365Lib as CGI
import SQLite3

# POST method
def on_POST(req, res):
  db = req.getParam("db")
  sql = req.getParam("sql")
  try:
    rows = SQLite3.query(db, sql)
    res.sendJSON(rows, "utf-8")
  except:
    res.sendJSON("エラーを検出。", "utf-8")
  return
  
# Start
if __name__ == "__main__":
  req, res = (CGI.Request(), CGI.Response())
  if req.method == "POST":
    on_POST(req, res)
  else:
    CGI.Response.status(405, CGI.METHOD_NOT_ALLOWED)
