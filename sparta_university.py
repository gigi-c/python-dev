# As a user I want to create a trainee

class Trainees:
    def __init__(self, name, age, trainee_id, stream):
        self.name = name
        self.age = age
        self.trainee_id = trainee_id
        self.stream = stream

    def info(self):
        print("Student details: {}, {} years old, Student-ID {}, {} course".format(self.name, self.age, self.trainee_id,
                                                                                  self.stream))

    def trainer(self):
        if self.stream.lower() == "data":
            print("{} from {} stream has Isabella as the trainer".format(self.name, self.stream))
        elif self.stream.lower() == "engineer":
            print("{} from {} stream has Astha as the trainer".format(self.name, self.stream))
        elif self.stream.lower() == "java":
            print("{} from {} stream has Zoe as the trainer".format(self.name, self.stream))

trainee_1 = Trainees("Gigi Chiang", 24, "001", "Data")
trainee_2 = Trainees("CJ", 24, "002", "Data")
trainee_3 = Trainees("Weiyee", 20, "003", "Data")
trainee_4 = Trainees("Alanso", 23, "004", "Java")
trainee_5 = Trainees("Steven", 25, "005", "Engineer")

trainee_5.info()
trainee_4.trainer()

# As a user I want to list all modules

class Modules():
    list_of_modules = []

    def __init__(self, module_name, duration):
        self.module_name = module_name
        self.duration = duration

    def module_length(self):
        if self.duration == 1:
            print ("{} is 1 week long".format(self.module_name))
        else:
            print ("{} is {} weeks long".format(self.module_name, self.duration))

    def add_module(self):
        self.list_of_modules.append(self.module_name)
        return self.list_of_modules

    def print_modules(self):
        print("List of modules:")
        for module in self.list_of_modules:
            print(module)

module_1 = Modules("Business Week", 1)
module_2 = Modules("Excel Week", 1)
module_3 = Modules("SQL and Agile", 1)
module_4 = Modules("Python", 2)
module_5 = Modules("Machine Learning and Cloud", 1)
module_6 = Modules("Tableau", 1)
module_7 = Modules("Final Project", 1)

module_1.add_module()
module_2.add_module()
module_3.add_module()
module_4.add_module()
module_5.add_module()
module_6.add_module()
module_7.add_module()
module_2.module_length()
module_4.module_length()
module_7.print_modules()

# As a user I want to add a student to a batch
# As a user I want to list all students in a batch

class Batches:
    list_of_trainees = []

    def __init__(self, stream, batch, start_date):
        self.batch_name = stream + " " + str(batch)
        self.start_date = start_date

    def add_trainee(self, trainee):
        if trainee not in self.list_of_trainees and trainee.isalpha():
            self.list_of_trainees.append(trainee)
            print("{} successfully added to {}".format(trainee, self.batch_name))
        else:
            print("Invalid name entry")

    def print_trainees(self):
        print("{}:".format(self.batch_name))
        for trainees in self.list_of_trainees:
            print(trainees)

data_9 = Batches("Data", 9, "24 Feb")
data_9.add_trainee("Gigi")
data_9.add_trainee("CJ")
data_9.add_trainee("Weiyee")
data_9.add_trainee("Johnny")
data_9.add_trainee("Y1n")
data_9.print_trainees()

