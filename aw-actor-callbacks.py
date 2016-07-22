#!/usr/bin/env python
#
import cgi
import wsgiref.handlers
import logging
from actingweb import actor
from actingweb import auth
from actingweb import config

import webapp2
from on_aw import on_aw_callbacks


class MainPage(webapp2.RequestHandler):

    def get(self, id, name):
        myself = actor.actor(id)
        if not myself.id or not name:
            self.response.set_status(404, 'Actor or callback not found')
            return
        if self.request.get('_method') == 'PUT':
            self.put(id, name)
        if self.request.get('_method') == 'POST':
            self.post(id, name)
        if not check.authorise(path='callbacks', subpath=name, method='GET'):
            self.response.set_status(403)
            return
        if not on_aw_callbacks.on_get_callbacks(myself, self, name):
            self.response.set_status(403, 'Forbidden')

    def put(self, id, name):
        self.post(id, name)

    def post(self, id, name):
        myself = actor.actor(id)
        if not myself.id or not name:
            self.response.set_status(404, 'Actor or callback not found')
            return
        if not check.authorise(path='callbacks', subpath=name, method='POST'):
            self.response.set_status(403)
            return
        # Add code here to handle actingweb subscriptions to other actors' properties++
        if not on_aw_callbacks.on_post_callbacks(myself, self, name):
            self.response.set_status(403, 'Forbidden')

application = webapp2.WSGIApplication([
    webapp2.Route(r'/<id>/callbacks<:/?><name:(.*)>', MainPage, name='MainPage'),
], debug=True)
