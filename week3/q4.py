def sort(str):
    words = str.split()

    for i in range(len(words)):
        for j in range(0, len(words) - i - 1):
            if words[j] > words[j + 1]:
                
                words[j], words[j + 1] = words[j + 1], words[j]

    result = ' '.join(words)
    return result


str = input("Enter a string: ")
sorted = sort(str)

print(f"Words sorted alphabetically: {sorted}")
