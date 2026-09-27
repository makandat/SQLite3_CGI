#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SQLite3.py
#   ver 1.0  2023-02-26
import sqlite3

def log(msg):
  PATH = '/var/www/data/log.txt'
  with open(PATH, "a") as f:
    f.write(msg)
  return

# クエリーを実行する。
def query(db, sql):
  log(db + "\n")
  con = sqlite3.connect(db)
  cur = con.cursor()
  cur.execute(sql)
  result = cur.fetchall()
  con.close()
  return result

# 値を１つだけ返すクエリーを実行する。
def getValue(db, sql):
  con = sqlite3.connect(db)
  cur = con.cursor()
  cur.execute(sql)
  row = cur.fetchone()
  con.close()
  return row[0]

# 1 行だけを返すクエリーを実行する。
def getRow(db, sql):
  con = sqlite3.connect(db)
  cur = con.cursor()
  cur.execute(sql)
  row = cur.fetchone()
  con.close()
  return row

# コマンドを実行する。
def execute(db, sql):
  con = sqlite3.connect(db)
  con.execute(sql)
  con.commit()
  con.close()
  return
