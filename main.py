from types_data import Number
from casm_opcodes import BYTECODES


LABELS = {
  'for_run_start': 3,
  'new_cod_run_for': 10,
  'for_run_end': 15, # следующая команда после цикла
  'is_prime_start': 17,
  'is_le_or_nechet': 27,
  'pre_for_is_prime_start': 45,
  'for_is_prime_start': 48,
  'for_is_prime_end': 66,
  'end_is_prime': 71,
  'end_program': 76
}

VARS = {
  'i': 1,
  'rez': 2,
  'is_chet': 3,
  'rez_stack': 4,
  'i_is_prime': 5,
  'num1': 6,
  'num2': 7,
  'one': 8,
  'null': 9,
  'two': 10,
  'three': 11,
  'nine': 12
}
COMMANDS = [
  # Точка входа (начало первой функции)
  BYTECODES['mov'], VARS['i'], VARS['null'],
  # for_run_start:
  BYTECODES['cmp'], VARS['i'], 0,
  BYTECODES['jmp_ge'], LABELS['for_run_end'],
  BYTECODES['jmp'], LABELS['is_prime_start'],
  # new_cod_run_for:
  BYTECODES['add'], VARS['i'], VARS['one'],
  BYTECODES['jmp'], LABELS['for_run_start'],
  # for_run_end:
  BYTECODES['jmp'], LABELS['end_program'],
  # конец первой функции

  # начало второй функции
  #is_prime_start:
  BYTECODES['cmp'], VARS['i'], VARS['two'],
  BYTECODES['jmp_ne'], LABELS['is_le_or_nechet'],
  BYTECODES['mov'], VARS['rez'], VARS['one'],
  BYTECODES['jmp'], LABELS['new_cod_run_for'],
  # is_le_or_nechet:
  BYTECODES['cmp'], VARS['i'], VARS['one'],
  BYTECODES['jmp_gt'], LABELS['pre_for_is_prime_start'],
  BYTECODES['mod'], VARS['i'], VARS['two'],
  BYTECODES['cmp'], VARS['i'], VARS['null'],
  BYTECODES['jmp_ne'], LABELS['pre_for_is_prime_start'],
  BYTECODES['mov'], VARS['rez'], VARS['null'],
  BYTECODES['jmp'], LABELS['new_cod_run_for'],
  # pre_for_is_prime_start:
  BYTECODES['mov'], VARS['i_is_prime'], VARS['three'],
  # for_is_prime_start:
  BYTECODES['cmp'], VARS['i_is_prime'], VARS['nine'],
  BYTECODES['jmp_ge'], LABELS['end_is_prime'],
  BYTECODES['mod'], VARS['i'], VARS['i_is_prime'],
  BYTECODES['cmp'], VARS['i'], VARS['null'],
  BYTECODES['jmp_ne'], LABELS['for_is_prime_end'],
  BYTECODES['mov'], VARS['rez'], VARS['null'],
  BYTECODES['jmp'], LABELS['new_cod_run_for'],
  # for_is_prime_end:
  BYTECODES['add'], VARS['i_is_prime'], VARS['two'],
  BYTECODES['jmp'], LABELS['for_is_prime_start'],
  # end_is_prime:
  BYTECODES['mov'], VARS['rez'], VARS['one'],
  BYTECODES['jmp'], LABELS['new_cod_run_for'],
  # конец второй функции
  # end_program:
  None
  # конец программы
]

print(len(COMMANDS))
