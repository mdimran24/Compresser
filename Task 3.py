while True:
    import os
    import gzip
    ans = input('Do you want to add to a file or write in a new one? Newfile = 1. Add to file = 2. Export file = 3.')
    if ans == '1':
        sentences = input("Enter the text you want to compress: ")
        name = input("Please enter your desired file name: ")
        with gzip.open(name + ".gz", "wt") as outfile:
            outfile.write(sentences)
        with gzip.open(name + '.gz', 'r') as f:
            file_content = f.read()
            print(file_content)
            elif ans == '2':
                sentences2 = input("Enter the text you want to compress: ")
                name2 = input("Which file do you want to add to: ")
                with gzip.open(name2 + ".gz", "wt") as outfile:
                    outfile.write(sentences2)
                with gzip.open(name2 + '.gz', 'r') as f:
                    file_content2 = f.read()
                    print(file_content2)
                    elif ans == '3':
                        name2 = input('Enter the file name: ')
                        archive = gzip.open(name2 + '.gz', 'r')
                        os.startfile(name2+'.gz')
                        while ans != '1' and ans != '2' and ans != '3':
                            print('ererrrrrrrrorrrrrrrrrrrrrrrr bro')
                            break
