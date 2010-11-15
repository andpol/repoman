import logging
import simplejson as json

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from repoman.lib.base import BaseController, render
from repoman.lib import beautify
from repoman.model import meta
from repoman.model.user import User

from pylons import app_globals

log = logging.getLogger(__name__)

class WhoamiController(BaseController):

    def whoami(self, format='json'):
        """GET /repoman/whoami: All items in the collection"""
        user = request.environ['REPOMAN_USER']
        if user:
            if format == 'json':
                response.headers['content-type'] = app_globals.json_content_type
                return json.dumps(beautify.user(user))
            else:
                abort(501, '501 Not Implimented')
        else:
            abort(404, '404 Not Found')

    def env(self, format='json'):
        out = {}
        for k,v in request.environ.iteritems():
            out[k] = repr(v)
        response.headers['content-type'] = app_globals.json_content_type
        return json.dumps(out)

