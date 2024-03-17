import unittest
from src.text_alignment.utils import *
class test_text_alignment(unittest.TestCase):
    def test_alignment1(self):
        #5
        actual_input=text_alignment()
        expected_output='''    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H     
'''
        self.assertEqual(actual_input,expected_output)
    def test_alignment2(self):
        #2
        actual_input=text_alignment()
        expected_output=''' H 
HHH
 HH      HH     
 HH      HH     
 HH      HH     
 HHHHHHHHHH 
 HH      HH     
 HH      HH     
 HH      HH     
        HHH 
         H  
'''
        self.assertEqual(actual_input,expected_output)
    def test_alignment3(self):
        #1
        actual_input=text_alignment()
        expected_output='''H
H   H   
H   H   
HHHHH 
H   H   
H   H   
    H 
'''
        self.assertEqual(actual_input,expected_output)

if __name__ == '__main__':
    unittest.main()