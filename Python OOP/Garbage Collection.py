import gc
print("GC Treshold :",gc.get_threshold())

def create_cycle():
    list1 = [1, 2, 3]
    list1.append(list1)

def main():
    print("Start 1000 cycle...")
    for i in range(1000):
        create_cycle()

    print("Collecting...")
    n = gc.collect()
    print("Object in memory:", n)  

if __name__ == "__main__":
    main()

