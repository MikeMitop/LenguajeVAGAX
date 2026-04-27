class MemoryManager:

    def __init__(self, size):

        self.size = size

        self.memory = {}

        self.next_address = 0


    def allocate(self, name, value):

        if self.next_address >= self.size:
            raise Exception("Out of memory")

        address = self.next_address

        self.memory[address] = {
            "name": name,
            "value": value
        }

        self.next_address += 1

        return address


    def free(self, address):

        if address in self.memory:
            del self.memory[address]


    def get(self, address):

        if address not in self.memory:
            raise Exception("Invalid memory access")

        return self.memory[address]["value"]


    def set(self, address, value):

        if address not in self.memory:
            raise Exception("Invalid memory access")

        self.memory[address]["value"] = value


    def info(self):

        used = len(self.memory)
        free = self.size - used

        print("\nMEMORY STATUS")
        print("Total:", self.size)
        print("Used:", used)
        print("Free:", free)
        print("")


    def gc(self, variables):

        used_addresses = set(variables.values())

        to_delete = []

        for addr in self.memory:

            if addr not in used_addresses:
                to_delete.append(addr)

        for addr in to_delete:
            del self.memory[addr]