import csv
import datetime

gastos_personales = "gastos_personales.csv"

print("El sistema esta trabajando, espere un momento")

def archivo_finanzas(fecha, descripcion, metodo_de_pago, categoria, monto):
    gastos = {"fecha": fecha, "descripcion": descripcion, "metodo_de_pago": metodo_de_pago, "categoria": categoria, "monto": monto}
    return gastos

def generar_archivo_gastos ():
    fecha = datetime.datetime.now()
    descripcion = input("Describe brevemente en que gastaste el dinero: ")
    metodo_de_pago = input("Efectivo o tarjeta: ")
    categoria = input("Agrega una categoria: ")
    monto = input("Monto gastado: ")
    return archivo_finanzas(fecha, descripcion, metodo_de_pago, categoria, monto)

with open (gastos_personales, mode = "w", newline= "") as archivo:
    escribir = csv.writer(archivo)
    escribir.writerow(["Fecha", "Descripcion", "Metodo de pago", "Categoria", "Monto"])
    
    for i in range(1):
        contenido = generar_archivo_gastos ()
        escribir.writerow([contenido["fecha"], contenido["descripcion"], contenido["metodo_de_pago"], contenido["categoria"],
                       contenido["monto"]])
