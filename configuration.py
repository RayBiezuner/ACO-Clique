

class Config:
    """
    Classe, implementada como um Singleton, responsável por armazenar as configurações de parâmetros do algoritmo.
    """
    __instance = None
    input_file = None
    parameters = {
        "iterations":None,
        "num_ants": None,
        "alpha":None,
        "evaporation": None,
        "optimal":None
    }
    @staticmethod
    def get_instance():
        """
        Obtém a instância única da classe Config.

        :return: Instância da classe Config.
        """
        if Config.__instance is None:
            Config()
        return Config.__instance

    def __init__(self):
        """
        Inicializa a classe Config.

        Lança uma exceção se uma instância da classe já existe.
        Pede ao usuário para inserir os valores das configurações.
        """
        if Config.__instance is not None:
            raise Exception("O Config já foi instanciado.")
        else:
            Config.__instance = self
            Config.parameters["iterations"] = int(input("Número máximo de iterações: "))
            Config.parameters["num_ants"] = int(input("Número de formigas: "))
            Config.parameters["optimal"] = int(input("Ótimo esperado: "))
            Config.parameters["evaporation"] = float(input("Taxa de evaporação: "))
            Config.parameters["alpha"] = float(input("Valor de alpha: "))
            print("-"*50)
            


