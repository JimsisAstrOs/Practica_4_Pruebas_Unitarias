
import pytest

from estacionamiento import Estacionamiento


@pytest.fixture
def sistema():
    """Preparación reutilizable para las pruebas."""
    return Estacionamiento()

@pytest.mark.parametrize(
    "minutos, esperado" ,
    [
        (14, 0.0),  # CP04 - R5: dentro del rango gratuito.
        (15, 0.0),   # CP05 - R5: último minuto gratuito.
        (16, 20.0),  # CP06 - R6: primer minuto con cobro.
        (59, 20.0),  # CP07 - R6: dentro de la primera hora.
        (60, 20.0),  # CP08 - R6: último minuto de la primera hora.
        (61, 35.0),  # CP09 - R7: comienza una hora adicional.
    ]
)

def test_limites_tarifa_normal(sistema, minutos, esperado):
    #Arrange
    cliente = "normal"
    boleto_perdido = False

    #Act
    resultado = sistema.calcular_total(
        minutos,
        cliente,
        boleto_perdido 
    )

    #Assert
    assert resultado == esperado

def test_30_minutos_cuestan_20(sistema):
 # CP01 - R6: de 16 a 60 minutos se cobran $20.
    #Arrange
    minutos = 30
    #Act
    resultado = sistema.calcular_total(
        minutos,
        "normal",
        False
    )
    #Assert
    assert resultado == 20.0

def test_90_minutos_cuestan_35(sistema):
# CP02 - R7: después de 60 minutos se inicia una hora adicional.
    # Arrange
    munitos = 90

    # Act
    resultado = sistema.calcular_total(
        munitos,
        "normal",
        False
    )

    # Assert
    assert resultado == 35.0

def test_180_minutos_cuestan_50(sistema):
# CP03 - R7: se cobran dos horas adicionales iniciadas.
    # Arrange
    minutos = 180

    # Act
    resultado = sistema.calcular_total(
        minutos,
        "normal",
        False
    )

    # Assert
    assert resultado == 50.0

def test_minutos_negativos_lanzan_error(sistema):
    # CP10 - R1 y R10:
    # los minutos no pueden ser negativos.
    # Arrange
    minutos = -1

    # Act & Assert
    with pytest.raises(ValueError):
        sistema.calcular_total(
            minutos,
            "normal",
            False
        )

def test_cliente_invalido_lanza_error(sistema):
    # CP11 - R2 y R11:
    # "vip" no es un tipo de cliente válido.
    # Arrange
    cliente = "vip"

    # Act & Assert
    with pytest.raises(ValueError):
        sistema.calcular_total(
            30,
            cliente,
            False
        )

def test_61_minutos_cliente_frecuente_tiene_descuento(sistema):
     # CP12 - R7 y R8:
     # $35 con 10% de descuento = $31.50.
     # También comprueba un resultado decimal.
     # Arrange
    minutos = 61
    cliente = "frecuente"

    # Act
    resultado = sistema.calcular_total(
        minutos,
        cliente,
        False
    )

    # Assert
    assert resultado == pytest.approx(31.50)

def test_boleto_perdido_cliente_cuesta_300(sistema):
    # CP13 - R3 y R8:
    # el boleto perdido cuesta $300 y no recibe descuento.
    # Arrange
    minutos = 500
    cliente = "frecuente"
    boleto_perdido = True

    # Act
    resultado = sistema.calcular_total(
        minutos,
        cliente,
        boleto_perdido
    )

    # Assert
    assert resultado == 300.0

def test_121_minutos_cliente_frecuente_cuesta_45(sistema):
    # CP14 - R7 y R8:
    # $50 con 10% de descuento = $45.
    # Arrange
    minutos = 121

    # Act
    resultado = sistema.calcular_total(
        minutos,
        "frecuente",
        False
    )

    # Assert
    assert resultado == pytest.approx(45.0)

def test_1000_minutos_costo_no_negativo(sistema):
    # CP15 - R7 y R9:
    # caso adicional con muchas horas.
    # $20 + 16($15) = $260.
    # Arrange
    minutos = 1000

    # Act
    resultado = sistema.calcular_total(
        minutos,
        "normal",
        False
    )

    # Assert
    assert resultado == 260.0

def test_costo_nunca_es_negativo(sistema):
    # R9: el costo debe ser mayor o igual que cero.
    # Arrange
    minutos = 10

    # Act
    resultado = sistema.calcular_total(
        minutos,
        "normal",
        False
    )

    # Assert
    assert resultado >= 0.0
     