def minor_mutation(code, level):
    return code.replace(f'Level: {level}', f'Level: {max(1, level+1)}')
