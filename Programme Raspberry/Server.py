import BaseHTTPServer
import time
import datetime



HOST_NAME = '192.168.1.192'
PORT_NUMBER = 8000



class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/text")
        s.end_headers()
        k=0;
        while True :
           file = open("temp.txt","r")
           data = file.read() 
           s.wfile.write("Systeme de Telemesure : LevelCONTROL \n")
           s.wfile.write(datetime.datetime.now().strftime("%d/%m/%y-%H:%M"))
           s.wfile.write("\n")
           s.wfile.write(data)
           s.wfile.write("\n")
           s.wfile.write("\n")
           time.sleep(1)
                       
    
if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    try:
      httpd.serve_forever()
    except KeyboardInterrupt:
      pass
    

    
