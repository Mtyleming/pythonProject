###########
goods_list:list[tuple[str,float,int]] = []

def add_goods(name:str, price:float,num:int):
    global goods_list
    goods_list.append((name,price,num))



add_goods("苹果",6000.00,2)
add_goods("小米",2000.00,1)
add_goods("华为",3000.00,2)

print(goods_list)

def cal_order(goods_list,coupon,score,express):
    total = sum([goods[1]*goods[2] for goods in goods_list])
    if total > 5000 and total > coupon:
        total -= coupon
    if total > 5000 and total > score//100:
        total -= score//100
    if express:
        total += express
    return total


print(cal_order(goods_list,1000,1000,5))