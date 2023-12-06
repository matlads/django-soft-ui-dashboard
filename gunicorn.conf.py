# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

bind = "0.0.0.0:5005"
workers = 2
threads = 4
accesslog = "-"
loglevel = "debug"
capture_output = True
enable_stdio_inheritance = True
worker_tmp_dir = "/dev/shm"
worker_class = "gthread"
wsgi_app = "core.wsgi"
