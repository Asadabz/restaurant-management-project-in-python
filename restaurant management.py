print(     )
name=input("please enter your name: ")
if name==( ):
 print(        )
print("Hi wellcome to ALADDIN_RESTAURANT")
print(        )
menu={
    'pizza'       :40,
    'pasta'       :50,
    'coffee'      :20,
    'samosa'      :20,
    'water'       :10,
    'beriyani'    :60,
    'shworma'     :50,
    'chicken fry' :60,
    'simple rice' :40
}
print("pizza:40\npasta:50\ncoffee:20\nsomosa:20\nwater:10\nberiyani:60\nshworma:50\nchicken fry:60\nsimple rice:40")
order=0
print(  )
item_1=input("please enter your order: ")
if item_1 in menu:
   order+=menu[item_1]
   print(f"your item {item_1} has been placed")
else:
   print("please enter item from the list")
print( )
second=input("  do you buy another item: ")
if second == "yes":
       print( )
       item_2=input("order your second item: ")
       if item_2 in menu:
          order+=menu[item_2]
          print(f"your item {item_2 } has been placed")
          print( )
       else:
          print("not avalable")
       third=input("  do you buy another item: ")
       if third == "yes":
         print( )
         item_3=input("order your third item: ")
         if item_3 in menu:
          order+=menu[item_3]
          print(f"your item {item_3 } has been placed")
         else:
          print("please order from the menu")
         print( )
         four=input("  do you buy another item: ")
         if four  == "yes":
            print( )
            item_4=input("order your fourth item: ")
            if item_4 in menu:
             order+=menu[item_4]
            print(f"your item {item_4 } has been placed")
            print( )
            print(f"your total amount is { order}\n\npay now otherwise ready to wash plates {name}😤")
         else:
          print( )
          print(f"your total amount is { order}\n\npay now otherwise ready to wash plates {name}😤")
       else:
        print ( )
        print(f"your total amount is { order}\n\npay now otherwise ready to wash plates {name}😤")
else:
 print( )
 print(f"your total amount is { order}\n\npay now otherwise ready to wash plates {name}😤")
