'''
corner case: 
    numU is 0 or not userB or numG == 0 or not bookG: return {}

Method:
corner case
transfer bookG to value:k
scan userB to create new dic 
    for name, create {type:number}
    sort the {}
    add to new dic
scan new dic, output the max number

'''
def favorite(numU, userB, numG, bookG):
    if numU == 0 or not userB or numG == 0 or not bookG:
        return {}
    
    g_dic = {}
    for k, v in bookG.items():
        for elem in v:
            g_dic[elem] = k
    
    dic = {}

    for k, v in userB.items():
        name = k
        tmp_dic = {}
        for elem in v:
            
