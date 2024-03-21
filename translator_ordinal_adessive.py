one = {
    "1": "esimesel",
    "2": "teisel",
    "3": "kolmandal",
    "4": "neljandal",
    "5": "viiendal",
    "6": "kuuendal",
    "7": "seitsmendal",
    "8": "kaheksandal",
    "9": "üheksandal"
}

one_omastav = {
    "1": "ühe",
    "2": "kahe",
    "3": "kolme",
    "4": "nelja",
    "5": "viie",
    "6": "kuue",
    "7": "seitsme",
    "8": "kaheksa",
    "9": "üheksa"
}


def eval_2(in_2):
    if in_2 == '10':
        return "kümnendal"
    elif in_2[0] == '1':
        return one_omastav[in_2[1]] + "teistkümnendal"
    elif in_2[0] == '0':
        return one[in_2[1]]
    elif in_2[1] == '0':
        return one_omastav[in_2[0]] + "kümnendal"
    else:
        return one_omastav[in_2[0]] + "kümne " + one[in_2[1]]
    

def eval_3(in_3):
    str_in = str(in_3)
    if len(str_in) == 2:
        return eval_2(str_in)
    elif len(str_in) == 3:
        if str_in == '100':
            return "sajandal"
        elif str_in[0] == '0':
            return eval_2(str_in[1] + str_in[2])
        elif str_in[1] == '0' and str_in[2] == '0':
            return one_omastav[str_in[0]] + "sajandal"
        elif str_in[0] == '1':
            return "saja " + eval_2(str_in[1] + str_in[2])
        else:
            return one_omastav[str_in[0]] + "saja " + eval_2(str_in[1] + str_in[2])

def evaluator(integer):
    str_in = str(integer)
    if len(str_in) == 1:
        return one[str_in]
    elif len(str_in) <= 3:
        return eval_3(str_in)
    elif len(str_in) == 4:
        if str_in == '1000':
            return 'tuhandendal'
        elif str_in[1] == '0' and str_in[2] == '0' and str_in[3] == '0':
            return one_omastav[str_in[0]] + " tuhandendal"
        elif str_in[0] == '1':
            return "tuhande " + eval_3(str_in[1] + str_in[2] + str_in[3])
        else:
            return one_omastav[str_in[0]] + " tuhande " + eval_3(str_in[1] + str_in[2] + str_in[3])
