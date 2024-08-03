def computeLPSArray(s):
    lps = [0] * len(s)
    length = 0
    i = 1

    while i < len(s):
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def maximumDeletionLength(s):
    lps = computeLPSArray(s)
    max_length = lps[-1]
    return max_length

print(maximumDeletionLength("abcabcdabc"))  
print(maximumDeletionLength("aaabaab"))     
print(maximumDeletionLength("aaaaa"))       
