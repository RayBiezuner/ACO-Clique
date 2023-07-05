class Config:
    __instance = None
    input_file = None
    parameters = {
        "iterations":None,
        "num_ants": None,
        "alpha":None,
        "evaporation": None,
        "optimal":None
       ## "seed":None
    }
    @staticmethod
    def get_instance():
        if Config.__instance is None:
            Config()
        return Config.__instance

    def __init__(self):
        if Config.__instance is not None:
            raise Exception("O Config já foi instanciado.")
        else:
            Config.__instance = self
            ##Config.parameters["seed"] = int(input("Seed: "))
            Config.parameters["iterations"] = int(input("Número máximo de iterações: "))
            Config.parameters["num_ants"] = int(input("Número de formigas: "))
            Config.parameters["optimal"] = int(input("Ótimo esperado: "))
            Config.parameters["evaporation"] = float(input("Taxa de evaporação: "))
            Config.parameters["alpha"] = float(input("Valor de alpha: "))
            print("-"*50)
            


