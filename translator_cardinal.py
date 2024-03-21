one = {
    "1": "üks",
    "2": "kaks",
    "3": "kolm",
    "4": "neli",
    "5": "viis",
    "6": "kuus",
    "7": "seitse",
    "8": "kaheksa",
    "9": "üheksa"
}

def eval_2(in_2):
    if in_2 == '10':
        return ["kümme"]
    elif in_2[0] == '1':
        return [one[in_2[1]] + "teist"]
    elif in_2[0] == '0':
        return [one[in_2[1]]]
    elif in_2[1] == '0':
        return [one[in_2[0]] + "kümmend"]
    else:
        return [one[in_2[0]] + "kümmend " + one[in_2[1]]]


def eval_3(in_3):
    str_in = str(in_3)
    if len(str_in) == 2:
        return [eval_2(str_in)]
    elif len(str_in) == 3:
        if str_in == '100':
            return ["sada"]
        elif str_in[0] == '0':
            return [eval_2(str_in[1] + str_in[2])]
        elif str_in[1] == '0' and str_in[2] == '0':
            return [one[str_in[0]] + "sada"]
        elif str_in[0] == '1':
            return ["sada " + eval_2(str_in[1] + str_in[2])[0]]
        else:
            return [one[str_in[0]] + "sada " + eval_2(str_in[1] + str_in[2])[0]]


def evaluator(integer):
    str_in = str(integer)
    if len(str_in) == 1:
        return [one[str_in]]
    elif len(str_in) <= 3:
        return [eval_3(str_in)]
    elif len(str_in) == 4:
        if str_in == '1000':
            return ['tuhat']
        elif str_in[1] == '0' and str_in[2] == '0' and str_in[3] == '0':
            return [one[str_in[0]] + " tuhat"]
        elif str_in[0] == '1':
            return ["tuhat " + eval_3(str_in[1] + str_in[2] + str_in[3])[0]]
        else:
            return [one[str_in[0]] + " tuhat " + eval_3(str_in[1] + str_in[2] + str_in[3])[0]]
