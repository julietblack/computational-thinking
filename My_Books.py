import Book 

import Q_Sort     

I_Am_Number_Four = Book.Book('I Am Number Four', Book.Author('Pittacus', 'Lore'), 444, '9780061969577')

Bring_the_Heat = Book.Book('Bring the Heat', Book.Author('G.A.', 'Aiken'), 416, '142013163X')

The_Giver = Book.Book('The Giver', Book.Author('Lois', 'Lowry'), 204, '0544336259')

books = [I_Am_Number_Four, Bring_the_Heat, The_Giver]
Q_Sort.quicksort(books)
for n in books:
	print(str(n) + '\n') 
