"""
Load factor = (Number of items in the hash table) / (Total number of slots)

Having a load factor greater than 1 means you have more items than slots in your array.
Once the load factor starts to grow, you need to add more slots to your hash table. his is called resizing.
A good rule of thumb is, resize when your load factor is greater than 0.7.

A good hash function is the SHA function.

Time Complexity
---------------

|    ACTION    | HASH TABLES (AVG) | HASH TABLES (WORST) |   ARRAYS   | LINKED LISTS |
|:------------:|:-----------------:|:-------------------:|:----------:|:------------:|
|   Search     |        O(1)       |         O(N)        |     O(1)   |      O(N)    |
|   Insert     |        O(1)       |         O(N)        |     O(N)   |      O(1)    |
|   Delete     |        O(1)       |         O(N)        |     O(N)   |      O(1)    |

"""