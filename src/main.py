import json

import cherrypy

import bibilopixel


class StringGeneratorWebService(object):
  exposed = True
  default_color = "hex_white"  # white
  default_patter = "solid"  # solid color
  LED_strip_size = 32

  # Load driver for the AllPixel
  from bibliopixel.drivers.serial_driver import *
  # set number of pixels & LED type here
  driver = DriverSerial(num=10, type=LEDTYPE.WS2812B)
  # load the LEDStrip class
  from bibliopixel.led import *
  led = LEDStrip(driver)

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
    color = json_req['color']
    pattern = json_req['pattern']
    if power is False:
      print("Turning off the LED\n")
      # make call to turn off the LED
      led.all_off()
      led.update()
      # if turn off successful, set result = 'success'
      result = 'success'
    elif color is not None:
      R = color['R']
      G = color['G']
      B = color['B']
      led.fillRGB(R, G, B, 0, LED_strip_size - 1)
      let.update()
      result = 'success'
    elif pattern is not None:
      # To be implemented
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
            'tools.response_headeer.headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.quickstart(StringGeneratorWebService(), '/', conf)
