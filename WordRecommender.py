#/usr/share/dict/words



def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def compare(item1, item2):
    return int(item1[1]) - int(item2[1])

def main():
    with open("/usr/share/dict/words") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    length = len(content)

    print length

    word_set = set(content)
    input_word = raw_input("Enter the word: ")
    list_res = []
    content2 = []
    content2.append("raw")
    content2.append("rack")
    for word in word_set:
        val = levenshtein(word, input_word)
        #print val
        list_res.append((word, val))


    list_res = sorted(list_res, cmp=compare)
    i = 0
    while i<6 and i<len(list_res):
        if list_res[i][0] != input_word:
            print list_res[i][0]
        i+=1

if __name__=='__main__':
    main()
