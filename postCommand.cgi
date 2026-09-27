#!/usr/bin/env python3
#  postCommand.cgi
import CGI365Lib as CGI
import SQLite3


# POST method
def on_POST(req, res):
  sql = req.getParam("sql")
  CGI.info(sql)
  db = req.getParam("db")
  CGI.info(db)
  try:
    SQLite3.execute(db, sql)
    res.sendJSON({"message":"コマンドの実行に成功しました。"}, "utf-8")
  except:
    res.sendJSON({"message":"エラーを検出。"}, "utf-8")
  return
  
# Start
if __name__ == "__main__":
  req, res = (CGI.Request(), CGI.Response())
  if req.method == "POST":
    on_POST(req, res)
  else:
    CGI.Response.status(405, CGI.METHOD_NOT_ALLOWED)
