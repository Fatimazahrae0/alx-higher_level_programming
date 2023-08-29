#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            results = float(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            results = None
        except TypeError:
            print("wrong type")
            results = None
        except IndexError:
            print("out of range")
            results = None
        finally:
            if results is None:
                new_list.append(0)
            else:
                new_list.append(results)
    return new_list
