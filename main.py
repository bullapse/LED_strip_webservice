import led_service
import config
# import requests_toolbelt.adapters.appengine

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
# requests_toolbelt.adapters.appengine.monkeypatch()

app = notspotify.create_app()


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
