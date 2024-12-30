import utils


class Computer:

    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input
        self.init()

    def init(self):
        register_block_raw, program_raw = puzzle_input.split("\n\n")
        registers_raw = register_block_raw.split("\n")
        self.A, self.B, self.C = [int(n) for _, n in [elem.split(": ") for elem in registers_raw]]
        _, program_numbers_raw = program_raw.split(": ")
        self.program = [int(n) for n in program_numbers_raw.split(",")]
        self.pointer = 0
        self.output = []
        self.instructions = [
            self.adv,
            self.bxl,
            self.bst,
            self.jnz,
            self.bxc,
            self.out,
            self.bdv,
            self.cdv
        ]
        self.exp = len(self.program) - 1

    def match_program(self):
        A = 8 ** self.exp
        self.A = A

        while True:
            self.run()

            if tuple(self.program) == tuple(self.output):
                return A

            self.calc_exp()
            A += 8 ** self.exp
            self.init()
            self.A = A

    def run(self):

        while self.pointer < len(self.program):
            opcode, operand = self.program[self.pointer], self.program[self.pointer + 1]
            self.instructions[opcode](operand)


    def adv(self, operand):
        self.A //= (2 ** self.combo(operand))
        self.pointer += 2

    def bxl(self, operand):
        self.B ^= operand
        self.pointer += 2

    def bst(self, operand):
        self.B = self.combo(operand) % 8
        self.pointer += 2

    def jnz(self, operand):

        if self.A:
            self.pointer = operand
        else:
            self.pointer += 2

    def bxc(self, operand):
        self.B ^= self.C
        self.pointer += 2

    def out(self, operand):
        self.output.append(self.combo(operand) % 8)
        self.pointer += 2

    def bdv(self, operand):
        self.B = self.A // (2 ** self.combo(operand))
        self.pointer += 2

    def cdv(self, operand):
        self.C = self.A // (2 ** self.combo(operand))
        self.pointer += 2

    def combo(self, operand):

        if 0 <= operand <= 3:
            return operand

        if operand == 4:
            return self.A

        if operand == 5:
            return self.B

        if operand == 6:
            return self.C

    def calc_exp(self):

        for i, (a, b) in enumerate(zip(self.program[::-1], self.output[::-1]), start=1):

            if a == b:
                self.exp = len(self.program) - 1 - i
                continue

            break


if __name__ == "__main__":
    timer = utils.Timer()

    puzzle_input = utils.read()

    # Part 1
    timer.start()
    computer = Computer(puzzle_input)
    computer.run()
    print(",".join([str(n) for n in computer.output]))
    timer.stop()  # 0.05ms

    # Part 2
    timer.start()
    computer = Computer(puzzle_input)
    print(computer.match_program())
    timer.stop()  # 1.69ms