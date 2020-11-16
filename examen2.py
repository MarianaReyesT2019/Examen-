import win32com.client
import os

while True:
    apple=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    computer_name = os.getenv('COMPUTERNAME')
    apple.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\cola2"
    queue=apple.Open(1,0)   
    msg=queue.Receive()
    valores=msg.Label
    print (msg.Label)
    queue.Close()
    banano=msg.Label


    archivo = open("names.txt", "a")
    archivo.write(banano)
    archivo.close()
