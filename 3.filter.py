#filter---> fun,iterable
alphabet = ['a','b','c','d','e','i','o','u']

def vowel_filter(alphabet):
    vowel = ['a','e','i','o','u']
    if alphabet in vowel:
        return True
    else:
        return False

if __name__ == "__main__":
    results = filter(vowel_filter,alphabet)
    print(results)
    for i in results:
        print(i)
