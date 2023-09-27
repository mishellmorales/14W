def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final

# Llamada a la función con solo el monto total de la compra
monto_compra_1 = 1000
descuento_1, monto_final_1 = calcular_descuento(monto_compra_1)
print(f"Monto de la compra: ${monto_compra_1}")
print(f"Descuento aplicado: ${descuento_1}")
print(f"Monto final a pagar: ${monto_final_1}\n")

# Llamada a la función con el monto total de la compra y un porcentaje de descuento personalizado
monto_compra_2 = 1500
porcentaje_descuento_2 = 15
descuento_2, monto_final_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
print(f"Monto de la compra: ${monto_compra_2}")
print(f"Descuento aplicado: ${descuento_2}")
print(f"Monto final a pagar: ${monto_final_2}")