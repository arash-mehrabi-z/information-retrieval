class PostingList():
    def __init__(self, token):
        self.data = {
            "word" : token,
            "frequency" : 0,
            "info" : {},
        }

    def add(self, doc_id, position):
        self.data["frequency"] += 1
        info = self.data["info"]

        if not doc_id in info:
            info[doc_id] = {
                "document_id" : doc_id,
                "occurence_count" : 1,
                "positions" : [position],
            }
        else:
            info[doc_id]["occurence_count"] += 1
            info[doc_id]["positions"].append(position)

    # def sort(self):
    #     self.docIds.sort()

    # def size(self):
    #     return len(self.docIds)

    # def getDocIds(self):
    #     return self.docIds
    
    def __repr__(self) -> str:
        s = "{word: " + self.data["word"] + ", frequency: " + self.data["frequency"].__str__() + ", info: {"
        for key, value in self.data["info"].items():
            s = s + " {" + "document_id: " + value["document_id"].__str__() + ", count: " + value["occurence_count"].__str__()
            s = s + ", positions: " + value["positions"].__str__() + "},"
        s += "}} }\n"
        return s

    # def AND(self, other):
    #     result = PostingList([])
    #     i, j = 0, 0

    #     while(i < self.size() and j < other.size()):
    #         a = self.docIds[i]
    #         b = other.docIds[j]

    #         if a == b:
    #             result.add(a)
    #             i += 1
    #             j += 1

    #         elif a < b:
    #             i += 1

    #         else:
    #             j += 1
        
    #     return result

    # def OR(self, other):
    #     result = PostingList([])
    #     i, j = 0, 0
    
    #     while(i < self.size() and j < other.size()):
    #         a = self.docIds[i]
    #         b = other.docIds[j]

    #         if a == b:
    #             if a not in result.getDocIds():
    #                 result.add(a)
    #             i += 1
    #             j += 1

    #         elif a < b:
    #             if a not in result.getDocIds():
    #                 result.add(a)
    #             i += 1

    #         else:
    #             if b not in result.getDocIds():
    #                 result.add(b)
    #             j += 1
            
    #         while(i < self.size()):
    #             a = self.docIds[i]
    #             if a not in result.getDocIds():
    #                 result.add(a)
    #             i += 1
        
    #         while(j < other.size()):
    #             b = other.docIds[j]
    #             if b not in result.getDocIds():
    #                 result.add(b)
    #             j += 1

    #     return result

    # def NOT(self, other):
    #     initialDocIds = self.docIds

    #     for otherDocId in other.getDocIds():
    #         if otherDocId in initialDocIds:
    #             initialDocIds.remove(otherDocId)
        
    #     return PostingList(initialDocIds)