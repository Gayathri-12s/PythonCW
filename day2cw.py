header = '''           BOOKSTORE RECEIPT
         Customer Purchase Details
        --------------------------'''

Book1_Title = "Python Basics"
Book1_Price =  450

Book2_Title = "Data Science Intro"
Book2_Price =  600

item1 = "Book1_Title : {}\t {}".format(Book1_Title, Book1_Price)
item2 = "Book2_Title : {}\t {}".format(Book2_Title, Book2_Price)

total_price = Book1_Price + Book2_Price
Total_Amount = "Total Amount:  {}".format(total_price)

m = '\t'+'THANK YOU'

total_line = header +'\n' '\t' + Total_Amount + '\n' '\t' + m

print(total_line.upper())

 
  
 