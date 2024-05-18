#Para que funcionen se deben importar los objetos asignados a cada funcion

#Se crea la funcion Ingresar Paciente
from models.paciente import Paciente
conn=pyscopg2.connect(
    host = "localhost"
    database = "Diplomado_model01"
    user = "postgres"
    password = "BNX66K312031"
)

def ingresar_paciente():
    print("Ingrese los datos del paciente:")
    nombre = input("Nombre: ")
    rut = input("Número de Rut: ")
    diagnostico = input("Nombre del diagnostico: ")
    medico = input("Nombre del Medico tratante: ")
    habitacion = input("Número de Habitacion: ")

    # Crea una instancia de la clase Paciente con los datos ingresados
    paciente = Paciente(nombre, rut, diagnostico, medico, habitacion)
    return paciente

nuevo_paciente = ingresar_paciente()
print("Se ha ingresado al paciente:", nuevo_paciente.nombre)

###################Se crea la funcion Asignar paciente a Medico############################
#La lista de doctores se encuentra en la base de datos, para eso debemos crear una conexion desde la base de datos
#para que nos muestre el listado de doctores y seleccionarlo. Debemos consultar desde la base de datos que nos muestre
#la lista y podamos asignarle un medico/doctor y actualizar.
def obtener_lista_doctores():
    #consulta para obtener lista
    query= "SELECT medico_id FROM medicos"
    with conn.cursor() as cur:
        cur.execute(query)
        medicos=cur.fetchall()
    return medicos
def asignar_doctor_a_paciente(paciente_id, medico_id):
    #actualizar la tabla de pacientes con el medicoa signado
    query="UPDATE pacientes SET medico_id= %s WHERE id=%s"
    with conn.cursor() as cur:
        cur.execute(query,(medico_id, paciente_id))
        conn.commit()
def main()
#obtener la lista de medicos
    medicos=obtener_lista_doctores
    #solicitar datos del paciente recien ingresado
    nuevo_paciente = ingresar_paciente()
    #mostrar lista de medicos disponibles
print("Medicos disponibles:")
for medico_id, nombre, especialidad in medicos:
    print(f"{medico_id}: {nombre}: {especialidad}")
    doctor_id_seleccionado=int(input("Seleccione el ID del medico para asignar al paciente:"))
    #asignar el medico al paciente recien ingresado
    #reemplaza paciente_id con el ID real del apceinte recien ingresado
    paciente_id= #poner id del paciente recien ingresado
    asignar_doctor_a_paciente(paciente_id,doctor_id_seleccionado)
    print(Doctor asignado correctamente al paciente.")


##########Se crea la funcion para pedir examen/resultado a paciente###############
def obtener_lista_de_examenes():
    #consulta para obtener la lista de examenes
    query="SELECT tipo from examenes"
    with conn.cursor() as cur:
        cur.execute(query)
        examenes=cur.fetchall()
    return examenes
def asignar_examen_a_paciente (paciente_id, tipo):
    #actualizar la tabla de paceintes con el examen asignado
    query="UPDATE pacientes SET tipo= %s WHERE id=%s"
    with conn.cursor() as cur:
        cur.execute(query, (tipo, paciente_id))
    conn.commit()
def main():
    #obtener lsita de examenes
    examenes= obtener_lista_de_examenes
    #solicitar al usuario el ID del paciente
    paciente_id=int(input("Ingrese rut del paciente:"))
    #mostrar la lista de examenes disponibles 
    print("Exámenes disponibles :")
    for tipo in examenes:
        print(f"{tipo}")
    #solicitar al usuario que seleccione un examen 
    examen_id_seleccionado=int(input("Seleccione el tipo de examen para asignarlo al paciente:"))
    #asignar el examen al paciente
    #reemplaza paciente_id con el rut real del paciente recien ingresado
    asignar_examen_a_paciente(paciente_id,examen_id_seleccionado)
    print(f"Examen asignado correctamente al paciente con rut {paciente_id}.")
if __name__=="___main__":
    main()
    
#########Se crea la funcion Diagnosticar enfermedad a un paciente######################
def obtener_examen_asociado(paciente_id):
    # Consulta para obtener el examen asociado al paciente
    query = "SELECT examenes FROM pacientes WHERE id = %s"
    with conn.cursor() as cur:
        cur.execute(query, (paciente_id,))
        examen = cur.fetchone()
    return examenes[0] if examen else None

def asignar_diagnostico_a_paciente(paciente_id, diagnosticos):
    # Actualizar la tabla de pacientes con el diagnóstico asignado
    query = "UPDATE pacientes SET diagnosticos = %s WHERE id = %s"
    with conn.cursor() as cur:
        cur.execute(query, (diagnostico, paciente_id))
    conn.commit()

def main():
    # Solicitar al usuario el ID del paciente y el diagnóstico
    paciente_id = int(input("Ingrese el rut del paciente: "))
    diagnosticos = input("Ingrese el diagnóstico a asignar: ")

    # Obtener el examen asociado al paciente
    examen_asociado = obtener_examen_asociado(paciente_id)

    if examen_asociado:
        print(f"Examen asociado al paciente: {examen_asociado}")
        # Asignar el diagnóstico al paciente
        asignar_diagnostico_a_paciente(paciente_id, diagnosticos)
        print(f"Diagnóstico '{diagnosticos}' asignado correctamente al paciente con rut {paciente_id}.")
    else:
        print(f"No se encontró ningún examen asociado al paciente con rut {paciente_id}.")

if __name__ == "__main__":
    main()

#Se crea la funcion listar pacientes
#PENDIENTE REVISAR Y CORREGIR 
def listar_pacientes(lista_pacientes):
    print("Listado de pacientes:")
    for paciente in lista_pacientes:
        print(f"Nombre: {paciente.nombre}")
        print(f"Rut: {paciente.rut}")
        print(f"Diagnostico: {paciente.diagnostico}")
        print(f"Medico: {paciente.medico}")
        print(f"Habitacion: {paciente.habitacion}")

listar_pacientes(lista_pacientes)        
