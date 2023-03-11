"""
blocklist.py

This file contains the blocklist of the JWT tokens. It will be imported by
app and the logout resource so that tokens cant be reused when user logs
out
"""

BLOCKLIST = set()
