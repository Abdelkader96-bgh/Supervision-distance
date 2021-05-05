# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import serial
import time
import datetime
try :
    mkfifo("temp.txt")
except :
    pass

h=2;  #nombre d'heurs apres l'envoi de chaque  Mail vers les responsables 
t=120;

portserie = serial.Serial('/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0',9600, timeout=3.0) ## Definition de port serie
a=0;
b=0;
k=0;
while True:
    data = portserie.readline()   ##Lire Data from port serie USB
    file=open("temp.txt","w")     ## Envoi de donnes vers le deuxeme programme vers un fichie Txt
    file.write(data)
    file.close()
    ##################
    if(k>=300):                  ## save data chaque 300 seconde [5 min]
      k=0;      
      f = open('Basededonnees.txt','a')
      f.write(datetime.datetime.now().strftime("%d/%m/%y-%H:%M   :"))
      f.write(data)
      f.close()
    k=k+1;
    ###############
    msg = MIMEMultipart()             
    message = "Message From Level Sensor :  %s" %data
    ################
    if ('Level' in data) and a<t :    ## Envoyer un mail si ( on a passe 2 heurs ou ou cas d'erreur)
      print data 
      time.sleep(1)
      a=a+1;
      b=0;
    else :
      print data 
      if(a>=t) :
         reception =['A.KENOUSSI@ocpgroup.ma','aziz.ke@hotmail.com'] ##les mail des responsables 

         password = "0668446164"     ##mon password
         msg['From'] = "azizkenoussi@gmail.com"  ##mon mail
         msg['To'] = ','.join(reception)
         msg['Subject'] = "Level Message"
 
         msg.attach(MIMEText(message, 'plain'))
  

         server = smtplib.SMTP('smtp.gmail.com: 587')
 
         server.starttls()
 
         server.login(msg['From'], password)
 

         server.sendmail(msg['From'], reception, msg.as_string())
         server.quit()
         print "successfully sent email to %s:" % (msg['To'])           
         time.sleep(1)
         a=0
      else :
          if(b==0) :
            reception =['A.KENOUSSI@ocpgroup.ma','aziz.ke@hotmail.com']
            password = "0668446164"
            msg['From'] = "azizkenoussi@gmail.com"
            msg['To'] = ','.join(reception)
            msg['Subject'] = "Level Message"
 
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(msg['From'], password)
 
            server.sendmail(msg['From'], reception, msg.as_string())
            server.quit()
            print "successfully sent email to %s:" % (msg['To'])           
            time.sleep(1)
            b=b+1
            a=a+1
          else :
            time.sleep(1)
            a=a+1  
