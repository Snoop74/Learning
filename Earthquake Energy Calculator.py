import math
import sys


richter_s = input("Please enter ritcher scale to calculate energy: ")

if richter_s.isdigit() is False:
      print("Please enter only float type of input")
      sys.exit()



richter_s = float(richter_s)

energy = 10**((1.5*richter_s)+4.8)



print("Ritcher Scale        Joules                        TNT"
      "\n1                  ",(10**((1.5*1)+4.8)), "    ", (10**((1.5*1)+4.8)) /4.184*(10**9),
      "\n5                  ",(10**((1.5*5)+4.8)), "    ", (10**((1.5*5)+4.8)) /4.184*(10**9),
      "\n9.1                ",(10**((1.5*9.1)+4.8)), "  ", (10**((1.5*9.2)+4.8)) /4.184*(10**9),
      "\n9.2                ",(10**((1.5*9.2)+4.8)), "  ", (10**((1.5*9.2)+4.8)) /4.184*(10**9),
      "\n9.5                ",(10**((1.5*9.5)+4.8)), "  ", (10**((1.5*9.5)+4.8)) /4.184*(10**9),
      "\nFor given Ritcher Scale: ","\n"
      ,richter_s,"              ", (10**((1.5*richter_s)+4.8)), "  ", (10**((1.5*richter_s)+4.8)) /4.184*(10**9))
