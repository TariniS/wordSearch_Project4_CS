#Name:Tarini Srikanth
#Instructor: Turner
#Project 4- Tests

import unittest
from funcs import *

class TestStrSpn(unittest.TestCase):
   def test_1(self):
       puzzle="EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
       words ="CHICKEN DOG CAT BEAR RABBIT ZEBRA MOUSE RACCOON"
       string3 = words.split(" ")
       wordsList= list(string3)
       puzzleFinal = turnInto10by10(puzzle)
       self.assertEqual(check_forwards(puzzleFinal,wordsList),["ZEBRA","RACCOON",1,2,0,2])
   def test_2(self):
       puzzle="EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
       words ="CHICKEN DOG CAT BEAR RABBIT ZEBRA MOUSE RACCOON"
       string3 = words.split(" ")
       wordsList= list(string3)
       puzzleFinal = turnInto10by10(puzzle)
       self.assertEqual(check_backwards(puzzleFinal,wordsList),["RAEB",1,3])
   def test_3(self):
       puzzle="EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
       words ="CHICKEN DOG CAT BEAR RABBIT ZEBRA MOUSE RACCOON"
       string3 = words.split(" ")
       wordsList= list(string3)
       puzzleFinal = turnInto10by10(puzzle)
       self.assertEqual(check_up(puzzleFinal,wordsList),["NEKCIHC",8,2])
   def test_4(self):
       puzzle="EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
       words ="CHICKEN DOG CAT BEAR RABBIT ZEBRA MOUSE RACCOON"
       string3 = words.split(" ")
       wordsList= list(string3)
       puzzleFinal = turnInto10by10(puzzle)
       self.assertEqual(check_down(puzzleFinal,wordsList),["RABBIT",3,1])
   def test_5(self):
       puzzle="EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
       words ="CHICKEN DOG CAT BEAR RABBIT ZEBRA MOUSE RACCOON"
       string3 = words.split(" ")
       wordsList= list(string3)
       puzzleFinal = turnInto10by10(puzzle)
       self.assertEqual(check_diagonal(puzzleFinal,wordsList),[])
   def test_6(self):
       puzzle="WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
       words ="UNIX CALPOLY GCC SLO CPE COMPILE VIM TEST"
       string3 = words.split(" ")
       wordsList= list(string3)
       puzzleFinal = turnInto10by10(puzzle)
       self.assertEqual(check_forwards(puzzleFinal,wordsList),["SLO","UNIX",7,9,2,3])
   def test_7(self):
       puzzle="WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
       words ="UNIX CALPOLY GCC SLO CPE COMPILE VIM TEST"
       string3 = words.split(" ")
       wordsList= list(string3)
       puzzleFinal = turnInto10by10(puzzle)
       self.assertEqual(check_backwards(puzzleFinal,wordsList),["MIV",1,2])
   def test_8(self):
       puzzle="WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
       words ="UNIX CALPOLY GCC SLO CPE COMPILE VIM TEST"
       string3 = words.split(" ")
       wordsList= list(string3)
       puzzleFinal = turnInto10by10(puzzle)
       self.assertEqual(check_up(puzzleFinal,wordsList),["ELIPMOC",8,0])
   def test_9(self):
       puzzle="WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
       words ="UNIX CALPOLY GCC SLO CPE COMPILE VIM TEST"
       string3 = words.split(" ")
       wordsList= list(string3)
       puzzleFinal = turnInto10by10(puzzle)
       self.assertEqual(check_down(puzzleFinal,wordsList),["CALPOLY",0,1])
   def test_10(self):
       puzzle="WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
       words ="UNIX CALPOLY GCC SLO CPE COMPILE VIM TEST"
       string3 = words.split(" ")
       wordsList= list(string3)
       puzzleFinal = turnInto10by10(puzzle)
       self.assertEqual(check_diagonal(puzzleFinal,wordsList),["GCC","CPE",1,1,5,0])
    
  
    
   #def test_2(self):
       #self.assertEqual(my_strspn("calpoly","place"),4)
   #def test_3(self):
       #self.assertEqual(my_strspn("cccca","office"),4)
   #def test_4(self):
       #self.assertEqual(my_strspn("minute","simulation"),5)
       
if __name__ == '__main__':
   unittest.main()
