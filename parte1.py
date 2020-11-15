import time 
import win32com.client
import os 
import random
from random import *


while True:
    peo=[" --Cepillin-- "," --Mariana-- "," --Bryan-- "," --Orlando-- "," --Gentle-- "," --Coraline-- "," --Jean_Grey--  "," --Tony_Stark-- "," --Steve_Rogers--  "," --Papa_Noel-- "," --Jack_Frost-- "," --Doctor_Stange-- "," --Harry_Potter ","-- Severus_Snape --"," --Albus_Dumbledore-- ","-- Peter_Parker-- "," --Thor_hijo_de_Odin-- "," --Gamora-- " ," --Homero_Simpspn-- "," --Obama-- "," --Jimmy_Morales-- ","--Charless_Xavier--"," --Gamora-- "," --Keviv_Bryan_Jose_chepeso_emilio_tercero-- "," --Willy_Wonka-- "," --Thanos-- "," --Messi-- "," --Chilindrina-- "]
    gen=randrange(len(peo))
    stu=peo[gen]
    print(stu) #un bucle infinito 

    apple=win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
    computer_name = os.getenv('COMPUTERNAME')
    apple.FormatName="direct=os:"+computer_name+"\\PRIVATE$\\cola2"
    queue=apple.Open(2,0)   # Open a ref to queue
    msg=win32com.client.Dispatch("MSMQ.MSMQMessage")
    msg.Label=stu
    msg.Send(queue)
    time.sleep(2)

    queue.Close()

