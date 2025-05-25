# Grokking Algorithms Exercises

### Chapter 1. Introduction to Algorithms

1.1| Suppose you have a sorted list of 128 names, and you are searching through it using binary search. What is the maximum number of steps it would take? 

Answer: 7

1.2| Suppose you double the size of the list. What’s the maximum number of steps now?

Answer: 8

1.3| You have a name, and you want to find the person's phone number in the phone book. Give the run time in terms of Big O.

Answer: O(logN)

1.4| You have a phone number, and you want to find the person's name in the phone book. (Hint: You'll have to search through the whole book!). Give the run time in terms of Big O.

Answer: O(N)

1.5| You want to read the numbers of every person in the phone book. Give the run time in terms of Big O.

Answer: O(N)

1.6| You want to read the numbers of just the As. (This is a tricky one! It involves concepts that are covered more in chapter 4. Read the answer — you may be surprised!). Give the run time in terms of Big O.

Answer: O(N)

### Chapter 2. Selection Sort

2.1| Suppose you’re building an app to keep track of your finances. Every day, you write down everything you spent money on. At the end of the month, you review your expenses and sum up how much you spent. So, you have lots of inserts and a few reads. Should you use an array or a list?

Answer: Linked List

2.2| Suppose you’re building an app for restaurants to take customer orders. Your app needs to store a list of orders. Servers keep adding orders to this list, and chefs take orders of the list and make them. It’s an order queue: servers add orders to the back of the queue, and the chef takes the first order of the queue and cooks it. Would you use an array or a linked list to implement this queue? (Hint: Linked lists are good for inserts/deletes, and arrays are good for random access. Which one are you going to be doing here?)

Answer: Linked List

2.3| Let’s run a thought experiment. Suppose Facebook keeps a list of usernames. When someone tries to log in to Facebook, a search is done for their username. If their name is in the list of usernames, they can log in. People log in to Facebook pretty often, so there are a lot of searches through this list of usernames. Suppose Facebook uses binary search to search the list. Binary search needs random access—you need to be able to get to the middle of the list of usernames instantly. Knowing this, would you implement the list as an array or a linked list?

Answer: Sorted array

2.4| People sign up for Facebook pretty often, too. Suppose you decided to use an array to store the list of users. What are the downsides of an array for inserts? In particular, suppose you’re using binary search to search for logins. What happens when you add new users to an array?

Answer: Time complexity of inserting in arrays is O(N).

2.5| In reality, Facebook uses neither an array nor a linked list to store user information. Let’s consider a hybrid data structure: an array of linked lists. You have an array with 26 slots. Each slot points to a linked list. For example, the first slot in the array points to a linked list containing all the usernames starting with a. The second slot points to a linked list containing all the usernames starting with b, and so on. Suppose Adit B signs up for Facebook, and you want to add them to the list. You go to slot 1 in the array, go to the linked list for slot 1, and add Adit B at the end. Now, suppose you want to search for Zakhir H. You go to slot 26, which points to a linked list of all the Z names. Then you search through that list to find Zakhir H. Compare this hybrid data structure to arrays and linked lists. Is it slower or faster than each for searching and inserting? You don’t have to give Big O run times, just whether the new data structure would be faster or slower.

Answer: Searching, slower than arrays and faster than linked lists.
        Inserting, faster than arrays, same as in linked lists.

### Chapter 3. Recursion

3.1| Suppose I show you a call stack like this:
            Greet2  | Name: Maggie
            Greet   | Name: Maggie
    What information can you give me, just based on this call stack?

Answer: The function Greet2 is called from inside the function Greet.

3.2| Suppose you accidentally write a recursive function that runs forever. As you saw, your computer allocates memory on the stack for each function call. What happens to the stack when your recursive function runs forever?

Answer: Stack overflow error

### Chapter 4. Quicksort

4.1| Write out the code for the earlier sum function.

Answer: Done

4.2| Write a recursive function to count the number of items in a list.

Answer: Done

4.3| Find the maximum number in a list.

Answer: Done

4.4| Remember binary search from chapter 1? It’s a divide-and-conquer algorithm, too. Can you come up with the base case and recursive case for binary search?

Answer: Done

4.5| How long would it take in Big O notation to print the value of each element in an array?

Answer: O(N)

4.6| How long would it take in Big O notation to double the value of each element in an array?

Answer: O(N)

4.7| How long would it take in Big O notation to double the value of just the first element in an array?

Answer: O(1)

4.8| How long would it take in Big O notation to create a multiplication table with all the elements in the array. So if your array is [2, 3, 7, 8, 10], your first multiply every element by 2, then multiply every element by 3, then by 7, and so on.

Answer: O(N * N)

### Chapter 5. Hash Table

Which of these hash functions are consistent?

5.1| f(x) = 1

Answer: Consistent.

5.2| f(x) = rand()

Answer: Not consistent.

5.3| f(x) = next_empty_slot()

Answer: Not consistent.

5.4| f(x) = len(x)

Answer: Consistent.

It’s important for hash functions to have a good distribution. They should map items as broadly as possible. The worst case is a hash function that maps all items to the same slot in the hash table. Suppose you have these four hash functions that work with strings:

A.  Return “1” for all input.
B.  Use the length of the string as the index.
C.  Use the first character of the string as the index. So, all strings starting with A are hashed together, and so on.
D.  Map every letter to a prime number: a = 2, b = 3, c = 5, d = 7, e = 11, and so on. For a string, the hash function is the sum of all the characters modulo the size of the hash. For example, if your hash size is 10, and the string is “bag”,  the index is (3 + 2 + 17) % 10 = 22 % 10 = 2.

For each of these examples, which hash functions would provide a good distribution? Assume a hash table size of 10 slots.

5.5| A phone book where the keys are names and values are phone numbers. The names are as follows: Esther, Ben, Bob, and Dan.

Answer: (D)

5.6| A mapping from battery size to power. The sizes are A, AA, AAA, and AAAA.

Answer: (B)

5.7| A mapping from book titles to authors. The titles are Maus, Fun Home, and Watchmen.

Answer: (D)

### Chapter 6. Breadth-First Search (BFS)

6.1| 

Answer: 

6.2| 

Answer: 

6.3| 

Answer: 

6.4| 

Answer: 

6.5| 

Answer: 

### Chapter 7. Dijkstra's Algorithm

7.1| 

Answer: 

### Chapter 8. Greedy Algorithms

8.1| 

Answer: 

8.2| 

Answer: 

8.3| 

Answer: 

8.4| 

Answer: 

8.5| 

Answer: 

8.6| 

Answer: 

8.7| 

Answer: 

8.8| 

Answer: 

### Chapter 9. Dynamic Programming

9.1| 

Answer: 

9.2| 

Answer: 

9.3| 

Answer: 

### Chapter 10. K-Nearest Neighbors (KNN)

10.1| 

Answer: 

10.2| 

Answer: 

10.3| 

Answer: 
