class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_cpu(self):
        return self.__cpu

    def set_memory(self, memory):
        self.__memory = memory

    def get_memory(self):
        return self.__memory

    def make_computations(self):
        return self.__cpu * self.__memory

    def __str__(self):
        return f"Computer with CPU: {self.__cpu} and Memory: {self.__memory} GB"

    def __eq__(self, other):

        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


class Phone:
    def __init__(self, __sim_cards_list):
        self.__sim_cards_list = __sim_cards_list

    def set_sim_cards(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards(self):
        return self.__sim_cards_list

    def call(self, sim_card_number, call_to_number):
        carrier = self.__get_carrier(sim_card_number)
        print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {carrier}")

    def __get_carrier(self, sim_card_number):
        carriers = {1: "Beeline", 2: "MegaCom"}
        return carriers.get(sim_card_number, "Неизвестный оператор")

    def __str__(self):
        return f"Phone with SIM cards: {', '.join(map(str, self.__sim_cards_list))}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)



    def use_gps(self, location):
        print(f"Маршрут построен до {location}")


    def __str__(self):
        return f"SmartPhone with cpu: {self.get_cpu()} Memory: {self.get_memory()} GB and sim cards: {', '.join(map(str, self.get_sim_cards()))}"


computer = Computer(3.5, 16)
phone = Phone([1, 2, 3])
smartphone1 = SmartPhone(2.3, 8, [1, 2])
smartphone2 = SmartPhone(3.2, 12, [1, 2])


print(computer)
print(phone)
print(smartphone1)
print(smartphone2)


print(f"Результат вычислений на компьютере: {computer.make_computations()}")
phone.call(1, "+996 777 99 99 99")
smartphone1.use_gps("Бишкек")
