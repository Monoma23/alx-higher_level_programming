#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nouvelle_list = []
    for w in range(list_length):
        try:
            div_reslt = my_list_1[w] / my_list_2[w]
        except TypeError:
            print("wrong type")
            div_reslt = 0
        except ZeroDivisionError:
            print("division by 0")
            div_reslt = 0
        except IndexError:
            print("out of range")
            div_reslt = 0
        finally:
            nouvelle_list.append(div_reslt)
    return nouvelle_list
