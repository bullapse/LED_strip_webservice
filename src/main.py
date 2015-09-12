import json

import cherrypy

import bibilopixel



class StringGeneratorWebService(object):
    exposed = True
    default_color = "hex_white" # white
    default_patter = "solid" # solid color
    LED_strip_size = 32

    #Load driver for the AllPixel
    from bibliopixel.drivers.serial_driver import *
    #set number of pixels & LED type here
    driver = DriverSerial(num = 10, type = LEDTYPE.WS2812B)
    #load the LEDStrip class
    from bibliopixel.led import *
    led = LEDStrip(driver)

    #load channel test animation
    from bibliopixel.animation import StripChannelTest
    anim = StripChannelTest(led)

  @cherrypy.tools.accept(media='applicatoin/json')
  def GET(self):
    return cherrypy.session[current_status]

  @cherrypy.tools.json_in()
  @cherrypy.tools.json_out()
  def POST(self, length=8):
    json_req = cherrypy.request.json
    result = 'did nothing'
    default_color = "hex_white"  # white
    default_patter = "solid"  # solid color

    power = json_req['status']  # if power is false, turn off
    if power is False:
      print("Turning off the LED\n")
      # make call to turn off the LED

      # if turn off successful, set result = 'success'
      result = 'success'
    else:
      color = json_req['color']
      pattern = json_req['pattern']
      # do a check for a valid hex color

      # change the color
      print("Changing the color to: " + color + "\n")

      # check if the pattern is in the list of patterns
      print("Changing the pattern to: " + color + "\n)

      # change the pattern to run

      # if change was successful, set reslut = 'success'
      result = 'success'

    # response
    resp = {"result": result}

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
            'tools.response_heade
rs.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.quickstart(StringGeneratorWebService(), '/', conf)
