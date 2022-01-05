import sys

sys.setrecursionlimit(100001)


def solution(words, queries):
    answer = []
    reverse_words, counted = [], []

    for word in words:
        reverse_words.append(word[::-1])
        counted.append(len(word))

    pre_trie = make_trie({}, words)
    post_trie = make_trie({}, reverse_words)

    for query in queries:
        if query[0] == '?' and query[-1] == '?':
            answer.append(counted.count(len(query)))
        elif query[0] == '?':
            answer.append(search_trie(post_trie, query[::-1], len(query)))
        elif query[-1] == '?':
            answer.append(search_trie(pre_trie, query, len(query)))

    return answer


def make_trie(trie, words):
    for word in words:
        cur = trie
        l = len(word)
        for char in word:
            if char in cur:
                cur = cur[char]
                cur['!'].append(l)
            else:
                cur[char] = {}
                cur = cur[char]
                cur['!'] = [l]
    return trie


def search_trie(trie, query, length):
    count = 0
    if query[0] == '?':
        return trie['!'].count(length)
    elif query[0] in trie:
        count += search_trie(trie[query[0]], query[1:], length)

    return count


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))