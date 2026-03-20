import time

start = time.time()

myList = [1,2,3,4,4]

# O(n2)
def algo1():
    for pointer1 in range(len(myList)):
        for pointer2 in range(pointer1+1, len(myList)):
            if myList[pointer1] == myList[pointer2]:
                print("Found em")
                end = time.time()
                print(f"Time taken: {end - start}")
# O(n long n)
def algo2():
    print()


algo1()
algo2()