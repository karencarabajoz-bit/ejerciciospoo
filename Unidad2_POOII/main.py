from modelo import GestionMedicamento
from vista import VistaFarmacia
from controlador import controladorFarmacia

modelo = GestionMedicamento()
vista = VistaFarmacia()
controlador= controladorFarmacia(modelo, vista)

controlador.ejecutar()
