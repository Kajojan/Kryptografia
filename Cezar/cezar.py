# Kajetan Jankowski
import sys
from funkcje_Cezar import *
from funkcje_afiniczny import *
def szyfr():
    def start():
        szyfr, opcja = sys.argv[1], sys.argv[2]        
        while True:
            if(szyfr == "-c" or szyfr == "-a"):
                    while True:
                         if (opcja in {"-e", "-d", "-j", "-k"}):
                              break
                         else:
                             opcja=input("-e (szyfrowanie),-d (odszyfrowywanie),-j (kryptoanaliza z tekstem jawnym),-k (kryptoanaliza wyłącznie w oparciu o kryptogram): ")
                    break
            else:
                szyfr=input("-c (szyfr Cezara), -a (szyfr afiniczny): ")
            
        # if(szyfr == "-c"):
        #     match opcja:
        #             case "-e":
        #                 kodowanie()
        #             case "-d":
        #                 odszyfrowanie()
        #             case "-j":
        #                 kryptoanaliza_z_tekstem_jawnym()
        #             case "-k":
        #                 kryptoanaliza_wyłącznie_w_oparciu_o_kryptogram()
        # else:
        #      match opcja:
        #             case "-e":
        #                 kodowanie_afinicznie()
        #             case "-d":
        #                 odszyfrowanie_afiniczne()
        #             case "-j":
        #                 kryptoanaliza_z_tekstem_jawnym_afiniczny()
        #             case "-k":
        #                 kryptoanaliza_wyłącznie_w_oparciu_o_kryptogram_afiniczny()

                      
                    
        if(szyfr == "-c"):
                if(opcja=="-e"):
                    kodowanie()
                if(opcja == "-d"):
                    odszyfrowanie()
                if(opcja == "-j"):
                    kryptoanaliza_z_tekstem_jawnym()
                if(opcja == "-k"):
                    kryptoanaliza_wyłącznie_w_oparciu_o_kryptogram()
        else:
            if(opcja=="-e"):
                        kodowanie_afinicznie()
            if(opcja == "-d"):
                        odszyfrowanie_afiniczne()
            if(opcja == "-j"):
                        kryptoanaliza_z_tekstem_jawnym_afiniczny()
            if(opcja == "-k"):
                        kryptoanaliza_wyłącznie_w_oparciu_o_kryptogram_afiniczny()
                            
                            

                        

                  
                  
                              
                  
    start()



szyfr()

