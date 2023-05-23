def execute_assembly_program(instructions):
    registers = dict()

    for instruction in instructions:
        parts = instruction.replace(',', '').split()
        opcode = parts[0]

        if opcode == 'MV':
            registers[parts[1]] = int(parts[2][1:])
        elif opcode == 'ADD':
            if parts[2].isdigit():
                registers[parts[1]] += int(parts[2])
            else:
                registers[parts[1]] += registers[parts[2]]
        elif opcode == 'SHOW':
            print(f"Registers: {registers}")


def main():
    """
    # Example usage
    5 # denotes no of lines in program
    MV REG1, #2000
    MV REG2, #4000
    ADD REG1, REG2
    ADD REG1, 600
    SHOW REG
    """
    program = []
    n = int(input('No of lines in program: '))
    for i in range(n):
        line = input(f'{i + 1}: ')
        program.append(line)

    execute_assembly_program(program)


if __name__ == '__main__':
    main()
