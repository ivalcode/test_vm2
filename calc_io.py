from types_data import Number
from casm_opcodes import BYTECODES

COMMANDS = [
BYTECODES["read"], 0,
BYTECODES["read"], 1,
BYTECODES["movm"], 2, 0,
BYTECODES["add"], 2, 1,
BYTECODES["print"], 2,
BYTECODES["movm"], 2, 0,
BYTECODES["sub"], 2, 1,
BYTECODES["print"], 2,
BYTECODES["movm"], 2, 0,
BYTECODES["mul"], 2, 1,
BYTECODES["print"], 2,
BYTECODES["movm"], 2, 0,
BYTECODES["div"], 2, 1,
BYTECODES["print"], 2,
BYTECODES["movm"], 2, 0,
BYTECODES["idiv"], 2, 1,
BYTECODES["print"], 2,
BYTECODES["movm"], 2, 0,
BYTECODES["mod"], 2, 1,
BYTECODES["print"], 2,
BYTECODES["halt"]
]
VARS = {
0: 0,
1: 1,
2: 2,
}
