#!/usr/bin/env python3
#  getIndexes.cgi
import CGI365Lib as CGI

# Start
if __name__ == "__main__":
  res= CGI.Response()
  res.sendHtml("./templates/indexes.html");

