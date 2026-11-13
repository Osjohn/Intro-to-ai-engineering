text = "language models predict the next word and language models predict text"

# 1. Tokens: split text into pieces
tokens = text.split()
print("Tokens:", tokens)
print("Number of tokens:", len(tokens))

# 2. Next-word prediction: record which word follows which
follows = {}
for i in range(len(tokens) - 1):
    follows.setdefault(tokens[i], []).append(tokens[i + 1])

def predict_next(word):
    options = follows.get(word)
    if not options:
        return "(no prediction)"
    return max(set(options), key=options.count)

for w in ["language", "models", "the"]:
    print("After", w, "->", predict_next(w))
