class Persona:
    def _init_(self, nombre, edad, pesoPersona):
        self.nombre = nombre
        self.edad = edad
        self.pesoPersona = pesoPersona


class Cabina:
    def _init_(self, nroCabina):
        self.nroCabina = nroCabina
        self.personasAbordo = []

    def agregarPersona(self, persona):
        self.personasAbordo.append(persona)

    def totalPersonas(self):
        return len(self.personasAbordo)

    def totalPeso(self):
        total = 0
        for p in self.personasAbordo:
            total += p.pesoPersona
        return total


class Linea:
    def _init_(self, color):
        self.color = color
        self.filaPersonas = []
        self.cabinas = []
        self.cantidadCabinas = 0

    def agregarPersona(self, persona):
        self.filaPersonas.append(persona)

    def agregarCabina(self, nroCabina):
        cab = Cabina(nroCabina)
        self.cabinas.append(cab)
        self.cantidadCabinas += 1

    def agregarPrimeraPersonaCabina(self, nroX):
        if len(self.filaPersonas) == 0:
            print("No hay personas en la fila.")
            return

        persona = self.filaPersonas[0]

        cabina = None
        for c in self.cabinas:
            if c.nroCabina == nroX:
                cabina = c
                break

        if cabina is None:
            print("Cabina no existe.")
            return

        if cabina.totalPersonas() + 1 > 10:
            print("La cabina supera 10 personas.")
            return

        if cabina.totalPeso() + persona.pesoPersona > 850:
            print("La cabina supera 850 kg.")
            return

        cabina.agregarPersona(persona)
        self.filaPersonas.pop(0)

    def verificarCabinas(self):
        for c in self.cabinas:
            if c.totalPersonas() > 10:
                return False
            if c.totalPeso() > 850:
                return False
        return True

    def ingresoTotal(self):
        ingreso = 0
        for c in self.cabinas:
            for p in c.personasAbordo:
                if p.edad < 25 or p.edad > 60:
                    ingreso += 1.5
                else:
                    ingreso += 3
        return ingreso

    def ingresoSoloRegular(self):
        total = 0
        for c in self.cabinas:
            for p in c.personasAbordo:
                if 25 <= p.edad <= 60:
                    total += 3
        return total


class MiTeleferico:
    def _init_(self):
        self.lineas = []
        self.cantidadIngresos = 0

    def agregarLinea(self, linea):
        self.lineas.append(linea)

    def lineaMayorIngresoRegular(self):
        mayor = None
        mayorMonto = -1
        for l in self.lineas:
            ing = l.ingresoSoloRegular()
            if ing > mayorMonto:
                mayorMonto = ing
                mayor = l
        return mayor




mt = MiTeleferico()

numLineas = int(input("Cuántas líneas desea registrar? "))

for i in range(numLineas):
    print("\n REGISTRO DE LINEA ")
    color = input("Color de la línea: ")
    linea = Linea(color)


    numCabinas = int(input("Cuántas cabinas tiene esta línea? "))
    for j in range(numCabinas):
        nro = int(input(f"Nro de cabina {j+1}: "))
        linea.agregarCabina(nro)


    numPersonas = int(input("Cuántas personas en la fila? "))
    for j in range(numPersonas):
        print(f"\nPersona {j+1}:")
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        peso = float(input("Peso: "))
        p = Persona(nombre, edad, peso)
        linea.agregarPersona(p)

    mt.agregarLinea(linea)


print("\n AGREGAR PRIMERA PERSONA A CABINA ")
colorBuscado = input("Línea donde desea agregar persona: ")

nroCab = int(input("Número de cabina destino: "))


lineaSel = None
for l in mt.lineas:
    if l.color == colorBuscado:
        lineaSel = l
        break

if lineaSel is not None:
    lineaSel.agregarPrimeraPersonaCabina(nroCab)
else:
    print("La línea no existe.")



print("\n RESULTADOS \n")

for l in mt.lineas:
    print(f"Línea {l.color}:")
    print("  - Reglas correctas?:", l.verificarCabinas())
    print("  - Ingreso total:", l.ingresoTotal())
    print("  - Ingreso solo tarifa regular:", l.ingre5soSoloRegular())
    print()


top = mt.lineaMayorIngresoRegular()
if top:
    print("La línea con mayor ingreso regular es:", top.color)
else:
    print("No hay líneas registradas.")
