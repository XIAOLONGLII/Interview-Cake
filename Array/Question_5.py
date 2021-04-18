
"""
My cake shop is so popular, I'm adding some tables and hiring wait staff so folks can have a cute sit-down cake-eating experience.

  Take Out Orders: [1, 3, 5]
 Dine In Orders: [2, 4, 6]
  Served Orders: [1, 2, 4, 6, 5, 3]

would not be first-come, first-served, since order 3 was requested before order 5 but order 5 was served first. 


  Take Out Orders: [17, 8, 24]
 Dine In Orders: [12, 19, 2]
  Served Orders: [17, 8, 12, 19, 24, 2]

would be first-come, first-served. 
"""
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    
    # 3 pointers: takeout, dine served 
    ptr1 = 0
    ptr2 = 0
    for i in range(len(served_orders)):
        if ptr1 < len(take_out_orders) and served_orders[i] == take_out_orders[ptr1]:
            ptr1 += 1
        elif ptr2 < len(dine_in_orders) and served_orders[i] == dine_in_orders[ptr2]:
            ptr2 += 1
        else:
            return False
    if ptr1 != len(take_out_orders) or ptr2 != len(dine_in_orders):
        return False
    return True
