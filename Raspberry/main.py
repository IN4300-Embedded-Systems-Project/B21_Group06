from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)

        boolean_value = params.get("bool", [None])[0]

        if boolean_value is not None:
            boolean_value = boolean_value.lower() == 'true'

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        if boolean_value is not None:
            response = f"Received boolean: {boolean_value}"
            GPIO.output(16, GPIO.HIGH) # Turn on relay (unlock the door)
            print("Turning on relay")
            time.sleep(300)
            GPIO.output(16, GPIO.LOW) #After 5min Turn off relay
            print("Turning on relay")
            GPIO.cleanup()

        else:
            response = "No boolean value received"

        self.wfile.write(response.encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
