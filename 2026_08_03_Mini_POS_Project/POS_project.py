
# DRINK WATER 🪿

class POS_system:
     def __init__(self,User_interaction,priceList,foodList,Desserts_Beverages):
        self.User_interaction = User_interaction
        self.foodList = foodList
        self.priceList = priceList
        self.Main_coures = {
                1: {"Yellow Dal Butter Fry": 200.00},
                2: {"Dal Makhani": 230.00},
                3: {"Veg.Lababdar": 280.00},
                4: {"Veg.Kolhapuri": 280.00},
                5: {"Sabji Jaipuri": 280.00},
                6: {"Punjabi Aloo Dum": 280.00},
                7: {"Chilly Paneer": 300.00},
                8: {"Veg.Manchurian": 300.00},
                9: {"Mushroom Masala": 300.00},
                10: {"Aloo Gobi Matar": 300.00},
                11: {"Paneer Do Pyaza": 350.00},
                12: {"Hare Matar Paneer": 350.00},
                13: {"Paneer Lababdar": 350.00},
                14: {"Paneer Butter Masala": 350.00},
                15: {"Paneer Kadai": 350.00},
                16: {"Veg. Navratan Kadrma": 350.00},
                17: {"Katla Kaliya (1PC, 2PCS)": 350.00},
                18: {"Pomfret Masala (1PC)": 450.00},
                19: {"Bhetki Fish in Tomato Curry (4 PCS)": 650.00},
                20: {"Ajwaini Fish (4pcs)": 650.00},
                21: {"Methi Fish Bhetki (4 PCS)": 650.00},
                22: {"Chilli / Garlic Fish Bhetki (6 PCS)": 550.00},
                23: {"Prawn in Coriander Sauce (6 PCS)": 550.00},
                24: {"Prawn Malai Curry / Masala (6 PCS)": 600.00},
                25: {"Chicken Kosha": 350.00},
                26: {"Chilli / Garlic Chicken (6PCS)": 380.00},
                27: {"Shanghai / Schezwan Chicken": 400.00},
                28: {"Hunan / Lemon / Kung Pao Chicken": 400.00},
                29: {"Chicken Bharta / Afghani Bhartha": 450.00},
                30: {"Chicken Tikka / Reshmi Masala": 500.00},
                31: {"Chicken Butter Masala / Do Pyaza": 500.00},
                32: {"Lababdar / Dak Bungalow Chicken": 550.00},
                33: {"Dhania Patta Chicken": 550.00},
                34: {"Clay Pot Smokey Chicken": 550.00},
                35: {"Mutton Liver Masala": 500.00},
                36: {"Mutton Kosha (4PCS)": 650.00},
                37: {"Sohini Mutton (4PCS)": 700.00},
                38: {"Mutton Handi (4PCS)": 700.00},
                39: {"Mutton Rogan Juice (4PCS)": 700.00}
                }
        self.Desserts_Beverages = {
          1: {"Chocolate / Butterscotch / Vanilla Ice Cream": 40.00},
          2: {"Plain Dahi": 80.00},
          3: {"Mix / Pineapple Raita": 100.00},
          4: {"Fried Icecream": 150.00},
          5: {"Sizzling Brownie": 250.00},
          6: {"Soda": 40.00},
          7: {"Mineral Water (Bisleri)": 40.00},
          8: {"Soft Drinks": 70.00},
          9: {"Fresh Lime Soda": 90.00},
          10: {"Masala Softdrinks": 90.00},
          11: {"Red Bull": 220.00}
          }
        self.Tandoori_Breads = {
                  1: {"Roti (Plain / Butter)":  45.00},
                  2: {"Naan (Plain / Butter)":  50.00},
                  3: {"Masala Kulcha": 60.00},
                  4: {"Garlic Nan": 70.00},
                  5: {"Lachha Paratha": 70.00},
                  6: {"Methi Paratha": 70.00},
                  7: {"Steamed Rice": 130.00},
                  8: {"Jeera Pulao / Jeera Rice": 180.00},
                  9: {"Vegetable Pulao": 220.00},
                  10: {"Vegetable / Egg Fried Rice":  220.00},
                  11: {"Chicken / Mixed Fried Rice": 330.00},
                  12: {"Burnt Garlic Rice (Veg / Chicken, Mix)": 350.00},
                  13: {"Vegetable / Egg Noodles": 200.00},
                  14: {"Chicken / Mixed Noodles":  280.00},
                  15: {"Chili Garlic Noodles (Veg / Chicken)":  300.00},
                  16: {"Pan Fried Gravy Chicken / Mix Noodles": 350.00},
                  17: {"Chicken Biriyani (Raita)": 350.00},
                  18: {"Mutton Biriyani (Raita)": 450.00},
                  19: {"777 Special Biriyani (2 Chicken, 2 Egg, 2 Aloo, 2 Mutton)": 777.00}
                  }
        self.Sizzlers = {
                  1: {"Vegetable Oriental Style Sizzler": 399.00},
                  2: {"Assorter Chicken Sizzler": 499.00},
                  3: {"777 Signature Sizzler": 599.00},
                  4: {"Chilli Garlic Pepper Chicken (6)": 350.00},
                  5: {"Konjee Crispy Chicken": 350.00},
                  6: {"Honey Garlic Chicken": 400.00},
                  7: {"Kung Pao Chicken (6)": 400.00},
                  8: {"Chicken Hot Basil (6)": 400.00},
                  9: {"Drums of Heaven (4)": 400.00},
                  10: {"Chicken Tikka / Reshmi (6)": 450.00},
                  11: {"Chicken Chakori / Malai Kabab (6)": 500.00},
                  12: {"Chicken Tangri (2 / 4)": 480.00},
                  13: {"Tandoori Chicken (Half / Full)":  480.00},
                  14: {"Mutton Bhuna": 550.00},
                  15: {"Mutton Adraki Kabab (4)": 600.00},
                  16: {"Mutton Galouti Kabab (4)": 550.00},
                  17: {"Dry Mutton (4)": 650.00}
                  }
        self.Appetizers_Vegetarian = {
                       1: {"Roasted / Fried Papad": 20.00},
                       2: {"Masala Papad": 40.00},
                       3: {"Masala Peanut": 100.00},
                       4: {"Chat Pata Aloo": 120.00},
                       5: {"Boiled Green Peas": 120.00},
                       6: {"French Fries": 150.00},
                       7: {"Veg Fingers": 150.00},
                       8: {"Chilli Garlic Pops": 150.00},
                       9: {"Tandoori Aloo": 150.00},
                       10: {"Paneer Pakora": 200.00},
                       11: {"Cheese Cherry Pineapple": 200.00},
                       12: {"Chilli Paneer": 250.00},
                       13: {"Red Pepper Paneer (Dry)": 250.00},
                       14: {"Mushroom Salt and Pepper": 250.00},
                       15: {"Corn Masala / Salt and Pepper": 250.00},
                       16: {"Veg Manchurian": 250.00},
                       17: {"Crispy Chilli Babycorn": 250.00},
                       18: {"Paneer Tikka": 300.00},
                       19: {"Boiled Egg (2)": 100.00},
                       20: {"Prawn Papad": 100.00},
                       21: {"Omelette / Scrambled (2)": 120.00},
                       22: {"Egg Pakora (2)": 150.00},
                       23: {"Katla Fry (1)": 180.00},
                       24: {"Pomfret Fry / Tandoor (1)":  380.00},
                       25: {"Fish Fry (3/5)": 600.00},
                       26: {"Fish Finger (3/6)": 600.00},
                       27: {"Shrimp Salt and Pepper": 300.00},
                       28: {"Fish Punjabi (3/6)": 300.00},
                       29: {"Garlic / Schezwan / Chilli Prawn (4)": 350.00},
                       30: {"Golden Fried Prawn (2)": 500.00},
                       31: {"Garlic / Schezwan / Chilli Fish (6)": 500.00},
                       32: {"Fish in Butter Garlic Sauce (6)": 550.00},
                       33: {"Fish Tikka / Irani / Afghani (4)": 600.00},
                       34: {"Chicken Pakora (6)": 300.00},
                       35: {"Boiled Veg with Chicken": 350.00},
                       36: {"Chilli / Garlic / Pan Fried Chicken (6)": 350.00}
                       }
        self.Signature_Appetizers = {
                       1: {"Dry Mushroom + French Fries + Baby Corn + Paneer Tikka": 777.00},
                       2: {"Fish Fry (2) + Chilli Fish (2) + Chilli Prawn (2) + French Fries": 777.00},
                       3: {"Chilli Chicken (3) + Chicken Tikka (2) + Chicken Tangri (2)": 777.00},
                       4: {"Mutton Bhuna + Mutton Galouti Kebab (2) + Masala Kulcha (1)": 777.00}
                       }
        self.Shoup = {
                  1: {"Veg / Chicken Clear Soup": 70.00 },
                  2: {"Vegetable Sweet Corn Soup": 100.00},
                  3: {"Chicken Sweet Corn Soup": 120.00},
                  4: {"Veg Hot & Sour Soup": 100.00},
                  5: {"Chicken Hot & Sour Soup": 120.00},
                  6: {"Veg Manchow Soup": 120.00},
                  7: {"Chicken Manchow Soup": 140.00},
                  8: {"Green Salad": 100.00},
                  9: {"Onion Salad": 100.00},
                  10: {"Egg Salad": 150.00},
                  11: {"Chicken Salad": 220.00},
                  12: {"Prawn Salad": 250.00}
                  }

     def show_Main_coures(self): 
        while True:
          print("""          
          
                                                        --- MAIN COURSE --- 
                --- VEGETARIAN ---                                              ---- NON-VEGETARIAN ---
1.YELLOW DAL BUTTER FRY                           200.00        |       17.KATLA KALIYA (1PC,2PCS)                         220.00/350.00        
2.DAL MAKHANI                                     230.00        |       18.POMFRET MASALA (1PC)                            450.00    
3.VEG.LABABDAR                                    280.00        |       19.BHETKI FISH IN TOMATO CURRY (4 PCS)             650.00
4.VEG.KOLHAPURI                                   280.00        |       20.AJWAINI FISH (4pcs)                             650.00
5.SABJI JAIPURI                                   280.00        |       21.METHI FISH BHETKI (4 PCS)                       650.00
6.PUNJABI ALOO DUM                                280.00        |       22.CHILLI/GARLIC FISH BHETKI (6 PCS)               550.00      
7.CHILLY PANEER                                   300.00        |       23.PRAWN IN CORIANDER SAUCE (6 PCS)                550.00
8.VEG.MANCHURIAN                                  300.00        |       24.PRAWN MALAI CURRY/MASALA (6 PCS)                600.00
9.MUSHROOM MASALA                                 300.00        |       25.CHICKEN KOSHA                                   350.00
10.ALOO GOBI MATAR                                300.00        |       26.CHILLI / GARLIC CHICKEN (6PCS)                  380.00
11.PANEER DO PYAZA                                350.00        |       27.SHANGHAI/SCHEZWAN CHICKEN                       400.00
12.HARE MATAR PANEER                              350.00        |       28.HUNAN/LEMON/KUNG PAO CHICKEN                    400.00
13.PANEER LABABDAR                                350.00        |       29.CHICKEN BHARTA/AFGHANI BHARTHA                  450.00
14.PANEER BUTTER MASALA                           350.00        |       30.CHICKEN TIKKA / RESHMI MASALA                   500.00
15.PANEER KADAI                                   350.00        |       31.CHICKEN BUTTER MASALA/DO PYAZA                  500.00
16.VEG. NAVRATAN KORMA                            350.00        |       32.LABABDAR/DAK BUNGALOW CHICKEN                   550.00
                                                                |       33.DHANIA PATTA CHICKEN                            550.00
                        ----------                              |       34.CLAY POT SMOKEY CHICKEN                         550.00
                                                                |       35.MUTTON LIVER MASALA                             500.00
                                                                |       36.MUTTON KOSHA (4PCS)                             650.00
                                                                |       37.SOHINI MUTTON (4PCS)                            700.00
                                                                |       38.MUTTON HANDI (4PCS)                             700.00
                                                                |       39.MUTTON ROGAN JUICE (4PCS)                       700.00
                                                          --------------
                        """)
          self.specific_section(self.Main_coures)  
          choice = input("Would-- you like to EXIT ? (Type anything) OR Stay and explore (Press ENTER) ")
          if choice != "":
               self.check_interaction()
               break

     def show_Tanduri_Breads(self):
          while True:
               print("""
        --- TANDOORI BREADS ---                                 |           --- PULAO, BIRIYANI & NOODLES ---
1.ROTI (PLAIN/BUTTER)                             40.00/45.00   |       7.STEAMED RICE                                    130.00
2.NAAN (PLAIN/BUTTER)                             45.00/50.00   |       8.JEERA PULAO / JEERA RICE                        180.00
3.MASALA KULCHA                                   60.00         |       9.VEGETABLE PULAO                                 220.00
4.GARLIC NAN                                      70.00         |       10.VEGETABLE/EGG FRIED RICE                       200.00/220.00
5.LACHHA PARATHA                                  70.00         |       11.CHICKEN/MIXED FRIED RICE                       280.00/330.00
6.METHI PARATHA                                   70.00         |       12.BURNT GARLIC RICE (VEG/CHICKEN, MIX)           230.00/350.00                       
                 ----------------------------                   |       13.VEGETABLE/EGG NOODLES                          180.00/200.00
                                                                |       14.CHICKEN/MIXED NOODLES                          240.00/280.00
                                                                |       15.CHILI GARLIC NOODLES (VEG/CHICKEN)             240.00/300.00
                                                                |       16.PAN FRIED GRAVY CHICKEN/MIX NOODLES            300.00/350.00
                                                                |       17.CHICKEN BIRIYANI (RAITA)                       350.00
                                                                |       18.MUTTON BIRIYANI (RAITA)                        450.00
                                                                |       19.777 SPECIAL BIRIYANI                           777.00
                                                                |       (2CHICKEN, 2EGG, 2ALOO, 2MUTTON)
                                                                                        ----------------------------                    
                            """)
               self.specific_section(self.Tandoori_Breads)
               choice = input("Would you like to EXIT ? (Type anything) OR Stay and explore (Press ENTER) ")
               if choice != "":
                    self.check_interaction()
                    break
     def show_Desserts_Beverages(self):
          while True:
               print("""
                        --- DESSERTS ---                                                --- BEVERAGES ---
1.CHOCOLATE / BUTTERSCOTCH / VANILLA ICE CREAM    40.00         |       6.SODA                                            40.00
2.PLAIN DAHI                                      80.00         |       7.MINERAL WATER (BISLERI)                         40.00
3.MIX / PINEAPPLE RAITA                           100.00        |       8.SOFT DRINKS                                     70.00
4.FRIED ICECREAM                                  150.00        |       9.FRESH LIME SODA                                 90.00
5.SIZZLING BROWNIE                                250.00        |       10.MASALA SOFTDRINKS                              90.00
                --------------------------                      |       11.RED BULL                                       220.00
                                                                                                ---------------            
                        """)  
               self.specific_section(self.Desserts_Beverages)    
               choice = input("Would you like to EXIT ? (Type anything) OR Stay and explore (Press ENTER) ")
               if choice != "":
                    self.check_interaction()
                    break
     def show_Sizzlers(self):
          while True:
               print("""
                  --- SIZZLERS ---
1.VEGETABLE ORIENTAL STYLE SIZZLER                       399.00
     (ASSORTED BOILED VEG IN BUTTER WITH SIZZLING
     NODDLES & RICE SERVED ON THE BED OF SMASH POTATO)
2.ASSORTER CHICKEN SIZZLER                            499.00
     (2 CHINESE STYLE CHICKEN SERVED WITH SMASH
     (POTATO, EGG ON A BED OF RICE & NOODLES)
3.777 SIGNATURE SIZZLER                                  599.00
     (LEG PIECE & BODY PIECE OF CHICKEN MARINATED WITH
     CHEESE & SERVED WITH SMASH POTATO, EGG ON A BED
     OF RICE & NOODLES)
4.CHILLI GARLIC PEPPER CHICKEN (6)                       350.00
5.KONJEE CRISPY CHICKEN                                  350.00
6.HONEY GARLIC CHICKEN                                   400.00
7.KUNG PAO CHICKEN (6)                                  400.00
8.CHICKEN HOT BASIL (6)                                 400.00
9.DRUMS OF HEAVEN (4)                                   400.00
10.CHICKEN TIKKA/RESHMI (6)                              450.00
11.CHICKEN CHAKORI/MALAI KABAB (6)                       500.00
12.CHICKEN TANGRI (2/4)                                  280.00/480.00
13.TANDOORI CHICKEN (HALF/FULL)                          280.00/480.00
14.MUTTON BHUNA                                          550.00
15.MUTTON ADRAKI KABAB (4)                               600.00
16.MUTTON GALOUTI KABAB (4)                              550.00
17.DRY MUTTON (4)                                        650.00
                                             """)
               self.specific_section(self.Sizzlers) 
               choice = input("Would you like to EXIT ? (Type anything) OR Stay and explore (Press ENTER) ")
               if choice != "":
                    self.check_interaction()
                    break
     def show_Appetizers_Vegetarian(self):
          while True:
               print("""
            --- APPETIZERS - NON-VEGETARIAN ---                                         --- APPETIZERS - VEGETARIAN ---
1.BOILED EGG (2)                                  100.00        |       19.ROASTED/FRIED PAPAD                             20.00
2.PRAWN PAPAD                                     100.00        |       20.MASALA PEANUT                                   100.00
3.OMELETTE / SCRAMBLED (2)                        120.00        |       21.CHAT PATA ALOO                                  120.00
4.EGG PAKORA (2)                                  150.00        |       23.BOILED GREEN PEAS                               120.00
5.KATLA FRY (1)                                   180.00        |       24.FRENCH FRIES                                    150.00
6.POMFRET FRY/TANDOOR (1)                         350.00/380.00 |       25.VEG FINGERS                                     150.00
7.FISH FRY (3/5)                                  350.00/600.00 |       26.CHILLI GARLIC POPS                              150.00
8.FISH FINGER (3/6)                               350.00/600.00 |       27.TANDOORI ALOO                                   150.00
9.SHRIMP SALT AND PEPPER                          300.00        |       28.PANEER PAKORA                                   200.00
10.FISH PUNJABI (3/6)                             300.00/600.00 |       29.CHEESE CHERRY PINEAPPLE                         200.00
11.GARLIC/SCHEZWAN/CHILLI PRAWN (4)               350.00        |       30.CHILLI PANEER                                   250.00
12.GOLDEN FRIED PRAWN (2)                         500.00        |       31.RED PEPPER PANEER (DRY)                         250.00
13.GARLIC/SCHEZWAN/CHILLI FISH (6)                500.00        |       32.MUSHROOM SALT AND PEPPER                        250.00
14.FISH IN BUTTER GARLIC SAUCE (6)                550.00        |       33.CORN MASALA/SALT AND PEPPER                     250.00
15.FISH TIKKA/IRANI/AFGHANI (4)                   600.00        |       34.VEG MANCHURIAN                                  250.00
16.CHICKEN PAKORA (6)                             300.00        |       35.CRISPY CHILLI BABYCORN                          250.00
17.BOILED VEG WITH CHICKEN                        350.00        |       36.PANEER TIKKA                                    300.00
18.CHILLI/GARLIC/PAN FRIED CHICKEN (6)            350.00

                """)
               self.specific_section(self.Appetizers_Vegetarian)  
               choice = input("Would you like to EXIT ? (Type anything) OR Stay and explore (Press ENTER) ")
               if choice != "":
                    self.check_interaction()
                    break
     def show_Signature_Appetizers(self):
          while True:
               print("""
        --- 777 SIGNATURE APPETIZERS ---
1.DRY MUSHROOM + FRENCH FRIES +                   777.00
     BABY CORN + PANEER TIKKA
2.FISH FRY (2) + CHILLI FISH (2) +                777.00
     CHILLI PRAWN (2) + FRENCH FRIES
3.CHILLI CHICKEN (3) + CHICKEN TIKKA (2) +        777.00
     CHICKEN TANGRI (2)
4.MUTTON BHUNA + MUTTON GALOUTI KEBAB (2) +       777.00
     MASALA KULCHA (1)
                                        """)
               self.specific_section(self.Signature_Appetizers)  
               choice = input("Would you like to EXIT ? (Type anything) OR Stay and explore (Press ENTER) ")
               if choice != "":
                    self.check_interaction()
                    break
     def show_Shoup(self):
          while True:
               print("""
--- SOUP ---
1.VEG/CHICKEN CLEAR SOUP                          70.00/80.00
2.VEGETABLE SWEET CORN SOUP                       100.00
3.CHICKEN SWEET CORN SOUP                         120.00
4.VEG HOT & SOUR SOUP                             100.00
5.CHICKEN HOT & SOUR SOUP                         120.00
6.VEG MANCHOW SOUP                                120.00
7.CHICKEN MANCHOW SOUP                            140.00

--- SALADS ---
8.GREEN SALAD                                     100.00
9.ONION SALAD                                     100.00
10.EGG SALAD                                      150.00
11.CHICKEN SALAD                                  220.00
12.PRAWN SALAD                                    250.00

""")
               self.specific_section(self.Shoup)  
               choice = input("Would you like to EXIT ? (Type anything) OR Stay and explore (Press ENTER) ")
               if choice != "":
                    self.check_interaction()
                    break
      
     def check_interaction(self,choice = 0):
          flag = True
          while flag:
               print("""
       -----777 BAR & LOUNGE MENU-----
        
1. Main Course
     --> Vegetarian
     --> Non-Vegetarian
2. Soup & Salads
3. Appetizers
    --> Vegetarian
    --> Non-Vegetarian
4. Tandoori Breads & Pulao, Biryani & Noodles
5. Desserts & Beverages
6. Sizzlers
7. Signature Appetizers
                  """)
               self.User_interaction = input("Please Enter a serial number to get into the menu OR Press ENTER to get your BILL: ")
               if(self.User_interaction == '1'):
                    self.show_Main_coures()
               elif(self.User_interaction == '2'):
                    self.show_Shoup()
               elif(self.User_interaction == '3'):
                    self.show_Appetizers_Vegetarian()
               elif(self.User_interaction == '4'):
                    self.show_Tanduri_Breads()
               elif(self.User_interaction == '5'):
                    self.show_Desserts_Beverages()
               elif(self.User_interaction == '6'):
                    self.show_Sizzlers()
               elif(self.User_interaction == '7'):
                    self.show_Signature_Appetizers()
               elif(self.User_interaction == '0'):
                    self.check_interaction()
               elif(self.User_interaction == ""):
                    self.get_my_bill()
                    import sys
                    sys.exit()
               else:
                    print("Invalid input try angain :(")


     def specific_section(self,products):
          while True:
               sl = int(input("Enter the serial number of the food: ")) 
               if(sl<0 or sl>len(products)):
                    print("Invalid serial Number :( Try again and Enter a valid input: ")
                    continue
               else:
                    self.priceList.append(list(products[sl].values())[0])
                    self.foodList.append(list(products[sl].keys())[0])
                    print(self.foodList)
                    print(self.priceList)
                    break
          

     def get_my_bill(self):
          total_amount = 0
          for i in range(0,len(self.foodList)):
               print("Rs.",self.priceList[i],"0/-             ",self.foodList[i])
          print("_______________________________________________________")
          for j in range(0,len(self.priceList)):
               total_amount = total_amount + self.priceList[j]
          print("TOTAL AMAOUNT                                   Rs.",total_amount,"0/-")
          print("                    THANK YOU. :)         ")
          return total_amount

ps1 = POS_system(0,[],[],{})
ps1.check_interaction()
		