from types_data import Number
from casm_opcodes import BYTECODES


LABELS = {
}

VARS = {
  'num1': 2,
  'num2': 3,
  'rez': 4,
}
COMMANDS = [
  BYTECODES['mov'], VARS['num1'], 5,
  BYTECODES['mov'], VARS['num2'], 4,
  BYTECODES['movm'], VARS['rez'], VARS['num1'],
  BYTECODES['add'], VARS['rez'], VARS['num2'],
  BYTECODES['print'], VARS['rez'],
  BYTECODES['movm'], VARS['rez'], VARS['num1'],
  BYTECODES['sub'], VARS['rez'], VARS['num2'],
  BYTECODES['print'], VARS['rez'],
  BYTECODES['movm'], VARS['rez'], VARS['num1'],
  BYTECODES['mul'], VARS['rez'], VARS['num2'],
  BYTECODES['print'], VARS['rez'],
  BYTECODES['movm'], VARS['rez'], VARS['num1'],
  BYTECODES['div'], VARS['rez'], VARS['num2'],
  BYTECODES['print'], VARS['rez'],
  BYTECODES['movm'], VARS['rez'], VARS['num1'],
  BYTECODES['idiv'], VARS['rez'], VARS['num2'],
  BYTECODES['print'], VARS['rez'],
  BYTECODES['movm'], VARS['rez'], VARS['num1'],
  BYTECODES['mod'], VARS['rez'], VARS['num2'],
  BYTECODES['print'], VARS['rez'],
  BYTECODES['halt']
]

print(len(COMMANDS))
