class Auto:
    Nombre = ""
    color = ""
    Velocidad = 0
    Estado = ""

    def Auto(name, c, velo, state):
        Auto.Nombre = name
        Auto.color = c
        Auto.Velocidad = velo
        Auto.Estado = state

    def Imprimir():
        print("Hola soy un auto y me llamo",Auto.Nombre," y soy de color",Auto.color)
    

    def InfoCoche():
        print("Mi velocidad es de ",Auto.Velocidad)

    def CambiarVelocidad(v):

        Auto.Velocidad = v
        print("Mi nueva Velocidad es de",Auto.Velocidad)

    def CambiarEstado():
        if(Auto.Estado==True):
            Auto.Estado = "Arrancando"
            print("Mi estado es ",Auto.Estado)
        else:
            Auto.Estado = "quieto"
            print("Mi estado es",Auto.Estado)
