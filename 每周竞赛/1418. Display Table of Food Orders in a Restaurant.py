class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        info = {}
        all_dish = set()
        for each_order in orders:
            table = each_order[1]
            order = each_order[2]
            all_dish.add(order)
            if table in info:
                info[table].append(order)
            else:
                info[table] = [order]

        all_dish = sorted(list(all_dish))

        res = []
        res.append(['Table'] + all_dish)

        info2 = sorted(info.items(), key = lambda x:int(x[0]))
        for each in info2:
            each_res = [each[0]]
            for food in all_dish:
                count = each[1].count(food)
                each_res.append(str(count))
            res.append(each_res)
        return res

        
                