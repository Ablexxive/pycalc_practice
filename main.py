import operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

OPS = ["+", "-", "*", "/"]


def apply_opp(first_dig: int, second_dig: int, op_id: int):
    print(op_id)
    return ops[OPS[op_id]](first_dig, second_dig)

global_iter = 0
def calculate_input(inpt: str, op_id: int = 0) -> float:
    global global_iter
    global_iter += 1
    print(f"Input: {inpt}, Global Iter: {global_iter}")
    step = inpt.split(OPS[op_id])
    print(step)
    # flag = True;
    while True:
        any_not_split = False
        for idx, each in enumerate(step):
            # Convert digits to ints from strings properly
            split_flag = False
            if type(each) != int:
                try:
                    each = int(each)
                except:
                    split_flag = True

            # if type(each) != int and len(each) != 1:
            # if len(each) != 1:
            if split_flag:
                print(f"Inside loop: {each}")
                replace = calculate_input(each, op_id+1)
                step[idx] = replace
                any_not_split = True

        if any_not_split == False:
            initial = int(step[0])
            for idx, each in enumerate(step):
                if idx == 0:
                    continue
                initial = apply_opp(initial, int(each), op_id)
            return initial





    # return step





### Goals
# Use of simple testing
# General python practice
def split_fcn(inpt: str, op_id: int = 0) -> float:
    print("Input:", inpt)
    step = inpt.split(OPS[op_id])
    for idx, each in enumerate(step):
        if len(each) != 1:
            replace = calculate_input(each, op_id+1)
            step[idx] = replace
    return step
