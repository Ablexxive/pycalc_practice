import operator

operations = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
OPS = ["+", "-", "*", "/"]

def calculate_input(inpt: str, op_id: int = 0) -> float:
    # Splits the input string with an operator and then iterates through the list
    # checking to see if there are any unsplit entities.
    # If unsplit - call this function again for that segment.
    # If all segments are split, apply the operator to all values and then return.

    split_input = inpt.split(OPS[op_id])
    while True:
        any_not_split = False
        for idx, each in enumerate(split_input):
            # Convert digits to floats from strings.
            split_flag = False # This flag signifies that something needs to be split.
            if type(each) != float:
                # This 'try' lets us differentiate between multidigit numbers vs strings which might have an operator.
                # I.e. "102" vs "1*2"
                try:
                    each = float(each)
                except:
                    split_flag = True

            if split_flag:
                replace = calculate_input(each, op_id+1)
                split_input[idx] = replace
                any_not_split = True # This flag lets the algo know that the input list still contains entities that need to be split.

        if any_not_split == False:
            initial = float(split_input[0])
            for idx, each in enumerate(split_input):
                if idx == 0:
                    continue
                initial = operations[OPS[op_id]](initial, float(each))
            return initial
