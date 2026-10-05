
import math


class Estacionamiento:
    TARIFA_BOLETO_PERDIDO = 300.0

    def calcular_total(self, minutos: int, tipo_cliente: str = "normal",
                       boleto_perdido: bool = False) -> float:
        """
        Calcula el total a pagar de acuerdo con el modelo de la práctica.

        Nota para el alumno:
        trate esta implementación como un sistema que debe verificarse.
        No asuma que todo lo que hace el código es correcto.
        """
         # R1 y R10: los minutos no pueden ser negativos.
        if minutos < 0:
            raise ValueError("Los minutos no pueden ser negativos")

        # R2 y R11: solamente existen estos dos tipos de cliente.
        if tipo_cliente not in ("normal", "frecuente"):
            raise ValueError("Tipo de cliente no válido")

        # R3: boleto perdido = $300.
        # No se aplica descuento.
        if boleto_perdido:
            return self.TARIFA_BOLETO_PERDIDO

        # R4 y R5: de 0 a 15 minutos es gratis.
        if minutos <= 15:
            total = 0.0

        # R6: de 16 a 60 minutos cuesta $20.
        elif minutos <= 60:
            total = 20.0

        # R7: después de 60 minutos se cobra cada hora adicional
        # iniciada.
        else:
            horas_adicionales = math.ceil((minutos - 60) / 60)
            total = 20.0 + (horas_adicionales * 15.0)

        # R8: cliente frecuente obtiene 10% de descuento.
        if tipo_cliente == "frecuente":
            total *= 0.90

        # R9: el costo nunca debe ser negativo.
        return max(0.0, round(total, 2))
