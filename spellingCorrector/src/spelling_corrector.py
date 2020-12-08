import re

class SpellingCorrector():
    def __init__(self, index):
        self.N = 0
        self.index = index
        for key, posting_list in index.items():
            self.N = self.N + posting_list.get()["frequency"]

    def P(self, word): 
        "Probability of `word`."
        return self.index[word].get()["frequency"] / self.N

    def correction(self, word): 
        "Most probable spelling correction for word."
        return max(self.candidates(word), key=self.P)

    def candidates(self, word): 
        "Generate possible spelling corrections for word."
        return (self.known([word]) or self.known(self.edits1(word)) or self.known(self.edits2(word)) or [word])

    def known(self, words): 
        "The subset of `words` that appear in the dictionary of WORDS."
        return set(w for w in words if w in self.index)

    def edits1(self, word):
        "All edits that are one edit away from `word`."
        letters    = 'آابپتثجچحخدذرزژسشضطظعغفقکگلمنوهی'
        splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
        deletes    = [R + L[1:]               for R, L in splits if L]
        transposes = [R + L[1] + L[0] + L[2:] for R, L in splits if len(L)>1]
        replaces   = [R + c + L[1:]           for R, L in splits if L for c in letters]
        inserts    = [R + c + L               for R, L in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def edits2(self, word): 
        "All edits that are two edits away from `word`."
        return (e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))