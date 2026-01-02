import random
# 6dKym~27xMTf,29JqD__2tjF:b+HanfL
def fuzzer(length: int, char_start: int, char_range: int) -> str:
    return "".join([chr(random.randrange(char_start, char_start+char_range)) for _ in range(length)])


def program(input: str) -> None:
    if "bug" in input:
        raise ValueError("Crash found!")
    return

for i in range(10000):
    seed = fuzzer(10,97,26)
    try:
        program(seed)
    except ValueError as e:
        print(f"Success! Your fuzzer found the input : {seed} at the iteration {i}")