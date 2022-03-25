from re import A


def swappingFile():
    doc1 = input("Enter Your First File Name : ")
    doc2 = input("Enter Your Second File Name : ")

    with open(doc1,'r') as a:
     data_1 = a.read()

    with open(doc1,'w') as a:
        a.write(data_1)

    with open(doc2,'r') as b:
     data_2 = b.read()

    with open(doc1,'w') as b:
        b.write(data_2)


swappingFile()