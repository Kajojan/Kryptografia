from funkcje import *
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
            

        match opcja:
               case "e":
                  code_message()
               case "d":
                  read_code()

                    

                  
                  
                              
                  
    start()



szyfr()

