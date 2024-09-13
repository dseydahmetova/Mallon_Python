import Lib.listoperations as lo

def main():
    newList = [1, 3, 5, 7]
    modifiedList = lo.addOne(newList)
    print("My list:", modifiedList)
    print("List after adding one:", modifiedList)

if __name__ == "__main__":
    main()

