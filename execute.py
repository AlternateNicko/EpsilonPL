import sys
# Note: Before running, rename the directory for the language's folder to EpsilonPL if already not
sys.path.append("EpsilonPL")

from epsilon import EPS
from edebug import debug
import time

instructions = """
import random

var = random.randint(1, 100)
"""

module = {}

#OPTIONAL
path = None # put directory path
file = "eps_run" # put name here, with no extensions

eps = EPS(instructions, module)
start = time.perf_counter()

results = eps.execute()

est = time.perf_counter() - start
print(f"{est:.4f}s")

ndb = debug(1)
ndb.print_init(eps)
ndb.print_functions(eps)
ndb.print_classes(eps)
ndb.print_libraries(eps)