class Consulta:
    def __init__(self, ci, nombrePaciente, apellidoPaciente, idMed, dia, mes, anio):
        self.ci = ci
        self.nombrePaciente = nombrePaciente
        self.apellidoPaciente = apellidoPaciente
        self.idMed = idMed
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def __str__(self):
        return f"{self.ci} - {self.nombrePaciente} {self.apellidoPaciente} | Med:{self.idMed} | Fecha:{self.dia}/{self.mes}/{self.anio}"



class Medico:
    def __init__(self, idMed, nombreMed, apellidoMed, aniosExperiencia):
        self.idMed = idMed
        self.nombreMed = nombreMed
        self.apellidoMed = apellidoMed
        self.aniosExperiencia = aniosExperiencia

    def __str__(self):
        return f"{self.idMed} - {self.nombreMed} {self.apellidoMed}"



class Consultorio:
    def __init__(self):
        self.medicos = []      
        self.consultas = []    

    # A) 
    def alta_medico(self, medico):
        self.medicos.append(medico)

    def alta_consulta(self, consulta):
        self.consultas.append(consulta)

    # B) 
    def baja_medico(self, nombreX, apellidoY):
        medico_encontrado = None

        for m in self.medicos:
            if m.nombreMed == nombreX and m.apellidoMed == apellidoY:
                medico_encontrado = m
                break

        if medico_encontrado:
            self.medicos.remove(medico_encontrado)
            self.consultas = [
                c for c in self.consultas if c.idMed != medico_encontrado.idMed
            ]
            print("\n Médico y sus consultas eliminados correctamente.\n")
        else:
            print("\n El médico no fue encontrado.\n")

    # C) 
    def cambiar_fecha_especial(self, nuevo_dia, nuevo_mes, nuevo_anio):
        for c in self.consultas:
            if (c.dia == 25 and c.mes == 12) or (c.dia == 1 and c.mes == 1):
                c.dia = nuevo_dia
                c.mes = nuevo_mes
                c.anio = nuevo_anio

        print("\n✔ Fechas actualizadas correctamente.\n")

    # D) 
    def pacientes_en_mi_cumple(self, dia, mes):
        return [c for c in self.consultas if c.dia == dia and c.mes == mes]

    
    def mostrar_medicos(self):
        print("\n--- MÉDICOS REGISTRADOS ---")
        for m in self.medicos:
            print(m)
        print()

    def mostrar_consultas(self):
        print("\n--- CONSULTAS REGISTRADAS ---")
        for c in self.consultas:
            print(c)
        print()



def menu():
    consultorio = Consultorio()

    while True:
        print("""
=============== MENÚ PRINCIPAL ===============

1. Registrar Médico
2. Registrar Consulta
3. Dar de baja a un Médico
4. Cambiar fecha (Navidad / Año Nuevo)
5. Pacientes atendidos en mi cumpleaños
6. Mostrar Médicos
7. Mostrar Consultas
0. Salir

===============================================
""")

        opcion = input("Ingrese una opción: ")


        # 1) Registrar Médico

        if opcion == "1":
            print("\n--- Registrar Médico ---")
            idm = int(input("ID Médico: "))
            nom = input("Nombre: ")
            ape = input("Apellido: ")
            exp = int(input("Años de experiencia: "))

            consultorio.alta_medico(Medico(idm, nom, ape, exp))
            print("\n✔ Médico registrado con éxito.\n")


        # 2) Registrar Consulta

        elif opcion == "2":
            print("\n--- Registrar Consulta ---")
            ci = int(input("CI paciente: "))
            nom = input("Nombre paciente: ")
            ape = input("Apellido paciente: ")
            idm = int(input("ID Médico: "))
            d = int(input("Día: "))
            m = int(input("Mes: "))
            a = int(input("Año: "))

            consultorio.alta_consulta(Consulta(ci, nom, ape, idm, d, m, a))
            print("\n✔ Consulta registrada.\n")


        # 3) Dar de baja Médico

        elif opcion == "3":
            print("\n--- Dar de baja Médico ---")
            nom = input("Nombre del médico: ")
            ape = input("Apellido del médico: ")
            consultorio.baja_medico(nom, ape)

        
        # 4) Cambiar fecha especial
        
        elif opcion == "4":
            print("\n--- Cambiar Fechas Especiales ---")
            nd = int(input("Nuevo día: "))
            nm = int(input("Nuevo mes: "))
            na = int(input("Nuevo año: "))
            consultorio.cambiar_fecha_especial(nd, nm, na)

        
        # 5) Pacientes en cumpleaños
    
        elif opcion == "5":
            print("\n--- Pacientes en mi cumpleaños ---")
            d = int(input("Día: "))
            m = int(input("Mes: "))

            lista = consultorio.pacientes_en_mi_cumple(d, m)

            if len(lista) == 0:
                print("\nNo hay pacientes en esa fecha.\n")
            else:
                print("\nPacientes atendidos ese día:")
                for c in lista:
                    print(" -", c)
                print()

  
        # 6) Mostrar médicos
    
        elif opcion == "6":
            consultorio.mostrar_medicos()

        # 7) Mostrar consultas

        elif opcion == "7":
            consultorio.mostrar_consultas()


        # 0) Salir

        elif opcion == "0":
            print("\nSaliendo del sistema...\n")
            break

        else:
            print("\n❌ Opción inválida. Intente nuevamente.\n")


# Ejecutar menú
if __name__ == "__main__":
    menu()
