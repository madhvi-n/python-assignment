def execute_assembly_program(instructions):
    registers = dict()
    for instruction in instructions:
        instruction = instruction.replace('\r', '')
        instruction = instruction.strip()
        parts = instruction.replace(',', ' ').split()
        opcode = parts[0]
        if opcode == 'MV':
            registers[parts[1]] = int(parts[2][1:])
        elif opcode == 'ADD':
            if parts[2].isdigit():
                registers[parts[1]] += int(parts[2])
            else:
                registers[parts[1]] += registers[parts[2]]
    return registers
