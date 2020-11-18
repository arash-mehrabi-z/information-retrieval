from handle import create_index
from phrase_query import get_query

def pos_intersect(data_1, data_2, k =1):
    answer = []
    data_info_1 = data_1["info"]
    data_info_2 = data_2["info"]
    
    i = 0
    j = 0

    while ( i < len(data_info_1) and j < len(data_info_2)):
        document_id_1 = data_info_1[i]["document_id"]
        document_id_2 = data_info_2[j]["document_id"]
        if ( document_id_1 == document_id_2):
            pos_res_list = [] 
            pos_list_1 = data_info_1[i]["positions"]
            pos_list_2 = data_info_2[j]["positions"]

            k = 0
            
            while ( k < len(pos_list_1) ):
                l = 0
                while (l < len(pos_list_2)) :
                    distance =  abs(pos_list_1[k] - pos_list_2[l])
                    if ( distance <= k):
                        pos_res_list.append(l)
                    elif pos_list_2[l]  > pos_list_1[k]:
                        break
                    l = l + 1

                for item in pos_res_list:
                    distance =  abs(pos_list_2[item] - pos_list_1[k] )
                    if distance > k :
                        pos_res_list.remove(item)
                for item in pos_res_list:
                    answer.append({ "document_id" : document_id_1,  "position_data_1" : pos_list_1[k]  ,  "position_data_2" : pos_list_2[item] }  )
                
                k = k + 1

            i = i + 1
            j = j + 1
        else:
            if document_id_1 < document_id_2:
                i = i + 1
            else:
                j = j + 1

    return answer

if __name__ == '__main__':
    file_address = "/home/arash/learning/information_retrieval/assignment/ir/positionalIndex/data/simple_test.xml"
    index = create_index(file_address)
    indices = get_query(index)
    print(indices)
