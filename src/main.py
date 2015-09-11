import json

import cherrypy

class StringGeneratorWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='applicatoin/json')
    def GET(self):
        return cherrypy.session[current_status]
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self, length=8):
        json_req = cherrypy.request.json
        result = 'success'

        power = json_req['status'] # if power is false, turn off
        if power is False :
            print("Turning off the LED")
            # make call to turn off the LED
        else:
            color = json_req['color']
            pattern = json_req['pattern']

        resp = {"result": result }

        return resp

    def PUT(self, another_string):
        cherrypy.session['mystring'] = another_string

    def DELETE(self):
        cherrypy.session.pop('mystring', None)

    if __name__ == '__main__':
        conf = {
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tools.sessions.on': True,
                'tools.response_headers.on': True,
                'tools.response_headers.headers': [('Content-Type', 'text/plain')],
                }
        }
        cherrypy.quickstart(StringGeneratorWebService(), '/', conf)
