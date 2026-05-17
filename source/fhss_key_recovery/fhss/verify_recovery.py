#!/usr/bin/env python3
import os

ok = True

if os.path.exists("extracted.txt"):
    with open("extracted.txt", "r", encoding="utf-8", errors="ignore") as f:
        text = f.read().strip()
else:
    text = ""

if text == "FHSSHARD1":
    print("FILE_OK")
else:
    print("FILE_FAIL")
    ok = False

if os.path.exists("recover.log"):
    with open("recover.log", "r", encoding="utf-8", errors="ignore") as f:
        log = f.read()
else:
    log = ""

if "recovered_bit=" in log and "diff=" in log:
    print("LOG_OK")
else:
    print("LOG_FAIL")
    ok = False

if ok:
    print("VERIFY_OK")
else:
    print("VERIFY_FAIL")
