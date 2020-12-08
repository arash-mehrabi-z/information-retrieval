class PostingList():
    def __init__(self, token):
        self.data = {
            "word" : token,
            "frequency" : 0,
            "info" : [],
        }

    def get(self):
        return self.data

    def add(self, doc_id, position):
        self.data["frequency"] += 1
        info = self.data["info"]

        for doc_info in info:
            if doc_id == doc_info["document_id"]:
                doc_info["occurence_count"] += 1
                doc_info["positions"].append(position)
                break
        else:
            info.append({
                "document_id" : doc_id,
                "occurence_count" : 1,
                "positions" : [position],
            })
    
    def __repr__(self) -> str:
        s = "{word: " + self.data["word"] + ", frequency: " + self.data["frequency"].__str__() + ", info: ["
        for info in self.data["info"]:
            s = s + " {" + "document_id: " + info["document_id"].__str__() + ", count: " + info["occurence_count"].__str__()
            s = s + ", positions: " + info["positions"].__str__() + "}, "
        s += "] } }\n"
        return s