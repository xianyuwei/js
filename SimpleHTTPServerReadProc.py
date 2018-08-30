#!/usr/bin/env python

import os
import posixpath
import BaseHTTPServer
import urllib
import cgi
import shutil
import mimetypes
import re

__all__ = ["SimpleHTTPRequestHandler"]
__author__ = "wxy"

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer

igh_proc_file_path = '/proc/ethercat/igh_ec_performance_log'
class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)
		
    def do_GET (self):
        """Serve a GET request."""
        try:
            f =open(igh_proc_file_path, 'r')
            buf = f.readline()
            f.close()
        except IOError:
            buf = '0\t0\t0\t0'
            print "File is not accessible."
        self.protocal_version = 'HTTP/1.1'
        self.send_response(200)  
        self.send_header("Welcome", "Contect")         
        self.end_headers()  
        self.wfile.write(buf)


if __name__ == '__main__':
    BaseHTTPServer.test(CORSRequestHandler, BaseHTTPServer.HTTPServer)
