import sys
print(sys.path)
from npp import NPP
from ndebug import debug
import time

instructions = """
class Test
{
    public func <const>(arg)
    {
        public variable = arg
        private var = 60
    }
    
    public func printout()
    {
        output(variable)
    }
}

object = Test("This is a test")
call printout()
"""

module = {}

#OPTIONAL
path = None # put directory path
file = "nxx_run" # put name here, with no extensions

npp = NPP(instructions, module)
start = time.perf_counter()

results = npp.execute()

est = time.perf_counter() - start
print(f"{est:.4f}s")

ndb = debug(True)
ndb.print_init(npp)
ndb.print_functions(npp)
ndb.print_classes(npp)
ndb.print_libraries(npp)