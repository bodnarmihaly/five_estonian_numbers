one = {
    "1": "esimene",
    "2": "teine",
    "3": "kolmas",
    "4": "neljas",
    "5": "viies",
    "6": "kuues",
    "7": "seitsmes",
    "8": "kaheksas",
    "9": "üheksas"
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
        return "kümnes"
    elif in_2[0] == '1':
        return one_omastav[in_2[1]] + "teistkümnes"
    elif in_2[0] == '0':
        return one[in_2[1]]
    elif in_2[1] == '0':
        return one_omastav[in_2[0]] + "kümnes"
    else:
        return one_omastav[in_2[0]] + "kümne " + one[in_2[1]]
    

def eval_3(in_3):
    str_in = str(in_3)
    if len(str_in) == 2:
        return eval_2(str_in)
    elif len(str_in) == 3:
        if str_in == '100':
            return "sajas"
        elif str_in[0] == '0':
            return eval_2(str_in[1] + str_in[2])
        elif str_in[1] == '0' and str_in[2] == '0':
            return one_omastav[str_in[0]] + "sajas"
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
            return 'tuhandes'
        elif str_in[1] == '0' and str_in[2] == '0' and str_in[3] == '0':
            return one_omastav[str_in[0]] + " tuhandes"
        elif str_in[0] == '1':
            return "tuhande " + eval_3(str_in[1] + str_in[2] + str_in[3])
        else:
            return one_omastav[str_in[0]] + " tuhande " + eval_3(str_in[1] + str_in[2] + str_in[3])
          
