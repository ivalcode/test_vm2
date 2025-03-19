from calc_io import COMMANDS, VARS
from casm_opcodes import BYTECODES, FLAGS

pointer = 0
DATA = [None] * len(VARS)


def add(num1, num2):
  DATA[num1] += DATA[num2]

def sub(num1, num2):
  DATA[num1] -= DATA[num2]

def mul(num1, num2):
  DATA[num1] *= DATA[num2]

def div(num1, num2):
  DATA[num1] /= DATA[num2]

def idiv(num1, num2):
  DATA[num1] //= DATA[num2]

def mod(num1, num2):
  DATA[num1] %= DATA[num2]

def mov(name, val):
  DATA[name] = val

def movm(name, val):
  DATA[name] = DATA[val]

def cmp(num1, num2):
  DATA[VARS['num1']] = DATA[num1]
  DATA[VARS['num2']] = DATA[num2]

# условия:
def eq():
  if DATA[VARS['num1']] == DATA[VARS['num2']]:
    FLAGS[0] = True
  else:
    FLAGS[0] = False

def ne():
  if DATA[VARS['num1']] != DATA[VARS['num2']]:
    FLAGS[0] = True
  else:
    FLAGS[0] = False

def lt():
  if DATA[VARS['num1']] < DATA[VARS['num2']]:
    FLAGS[0] = True
  else:
    FLAGS[0] = False

def gt():
  if DATA[VARS['num1']] > DATA[VARS['num2']]:
    FLAGS[0] = True
  else:
    FLAGS[0] = False

def le():
  if DATA[VARS['num1']] <= DATA[VARS['num2']]:
    FLAGS[0] = True
  else:
    FLAGS[0] = False

def ge():
  if DATA[VARS['num1']] >= DATA[VARS['num2']]:
    FLAGS[0] = True
  else:
    FLAGS[0] = False

def vm_print(key):
  print(DATA[key])

def read(var):
  DATA[var] = int(input())


OPCODES = {
  BYTECODES['add']: add,
  BYTECODES['sub']: sub,
  BYTECODES['mul']: mul,
  BYTECODES['div']: div,
  BYTECODES['idiv']: idiv,
  BYTECODES['mod']: mod,
  BYTECODES['mov']: mov,
  BYTECODES['movm']: movm,
  BYTECODES['cmp']: cmp,
  BYTECODES['print']: print,
  BYTECODES['read']: read,
}

is_running = True
while is_running:
  #print(pointer, COMMANDS[pointer])
  opcode = COMMANDS[pointer]
  pointer +=1
  if opcode in OPCODES:

    args = COMMANDS[pointer:pointer + 2]
    OPCODES[opcode](*args)
    poi
    is_running = False
    break
  elif COMMANDS[pointer] == BYTECODES['add']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    add(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['sub']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    sub(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['mul']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    mul(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['div']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    div(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['idiv']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    idiv(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['mod']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    mod(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['mov']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    mov(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['movm']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    movm(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['cmp']:
    pointer += 1
    val1 = COMMANDS[pointer]
    pointer += 1
    val2 = COMMANDS[pointer]
    cmp(val1, val2)
  elif COMMANDS[pointer] == BYTECODES['jmp_eq']:
    eq()
    if FLAGS[0]:
      pointer = COMMANDS[pointer + 1]
      continue
    else:
      pointer += 2
      continue
  elif COMMANDS[pointer] == BYTECODES['jmp_ne']:
    ne()
    if FLAGS[0]:
      pointer = COMMANDS[pointer + 1]
      continue
    else:
      pointer += 2
      continue
  elif COMMANDS[pointer] == BYTECODES['jmp_lt']:
    lt()
    if FLAGS[0]:
      pointer = COMMANDS[pointer + 1]
      continue
    else:
      pointer += 2
      continue
  elif COMMANDS[pointer] == BYTECODES['jmp_gt']:
    gt()
    if FLAGS[0]:
      pointer = COMMANDS[pointer + 1]
      continue
    else:
      pointer += 2
      continue
  elif COMMANDS[pointer] == BYTECODES['jmp_le']:
    le()
    if FLAGS[0]:
      pointer = COMMANDS[pointer + 1]
      continue
    else:
      pointer += 2
      continue
  elif COMMANDS[pointer] == BYTECODES['jmp_ge']:
    ge()
    if FLAGS[0]:
      pointer = COMMANDS[pointer + 1]
      continue
    else:
      pointer += 2
      continue
  elif COMMANDS[pointer] == BYTECODES['jmp']:
    pointer = COMMANDS[pointer + 1]
    continue
  elif COMMANDS[pointer] == BYTECODES['print']:
    pointer += 1
    vm_print(COMMANDS[pointer])
  elif COMMANDS[pointer] == BYTECODES['read']:
    pointer += 1
    read(COMMANDS[pointer])
  else:
    print("Ошибка байткода!")
    is_running = False
    break

  pointer += 1
