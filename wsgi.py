
import os

from django.core.wsgi import get_wsgi_application


def application(env, start_response):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "latelierchazalote.settings")

    application = get_wsgi_application()


    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return ['<!DOCTYPE html><html><meta charset="utf-8"><title>It works',
            "</title><b>It works!</b><br /><br />This is the server's ",
            'default wsgi.py.']
