from Kryptografia.Cezar.funkcje_Cezar import *
from Kryptografia.Cezar.funkcje_afiniczny import *
def szyfr():
    def start():
        szyfr=input("-c (szyfr Cezara), -a (szyfr afiniczny): ")
        while True:
            if(szyfr == "c" or szyfr == "a"):
                    opcja=input("-e (szyfrowanie),-d (odszyfrowywanie),-j (kryptoanaliza z tekstem jawnym),-k (kryptoanaliza wyłącznie w oparciu o kryptogram): ")
                    while True:
                         if (opcja in {"e", "d", "j", "k"}):
                              break
                         else:
                             opcja=input("-e (szyfrowanie),-d (odszyfrowywanie),-j (kryptoanaliza z tekstem jawnym),-k (kryptoanaliza wyłącznie w oparciu o kryptogram): ")
                    break
            else:
                szyfr=input("-c (szyfr Cezara), -a (szyfr afiniczny): ")
            
        if(szyfr == "c"):
            match opcja:
                    case "e":
                        kodowanie()
                    case "d":
                        odszyfrowanie()
                    case "j":
                        kryptoanaliza_z_tekstem_jawnym()
                    case "k":
                        kryptoanaliza_wyłącznie_w_oparciu_o_kryptogram()
        else:
             match opcja:
                    case "e":
                        kodowanie()
                    case "d":
                        odszyfrowanie()
                    case "j":
                        kryptoanaliza_z_tekstem_jawnym()
                    case "k":
                        kryptoanaliza_wyłącznie_w_oparciu_o_kryptogram()

                      
                    

                        

                  
                  
                              
                  
    start()



szyfr()

