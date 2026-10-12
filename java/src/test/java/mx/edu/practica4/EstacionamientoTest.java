
package mx.edu.practica4;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

class EstacionamientoTest {

    private Estacionamiento sistema;

    @BeforeEach
    void setUp() {
        sistema = new Estacionamiento();
    }

    @Test
    void ejemploInicial() {
        // Arrange
        int minutos = 10;

        // Act
        double resultado = sistema.calcularTotal(minutos, "normal", false);

        // Assert
        assertEquals(0.0, resultado, 0.001);
    }

    @Test
    void ceroMinutosClienteNormal() {
        // Arrange
        int minutos = 0;

        // Act
        double resultado = sistema.calcularTotal(minutos, "normal", false);

        // Assert
        assertEquals(0.0, resultado, 0.001);
    }

    @Test
    void treintaMinutosClienteNormal() {

        // Arrange
        int minutos = 30;

        // Act
        double resultado = sistema.calcularTotal(minutos, "normal", false);

        // Assert
        assertEquals(20.0, resultado, 0.001);
    }

    @Test
    void quinceMinutosSiguenSiendoGratuitos() {

        // Arrange
        int minutos = 15;

        // Act
        double resultado = sistema.calcularTotal(minutos, "normal", false);

        // Assert
        assertEquals(0.0, resultado, 0.001);
    }

    @ParameterizedTest

    @CsvSource({

            "14, 0.0",

            "15, 0.0",

            "16, 20.0",

            "59, 20.0",

            "60, 20.0",

            "61, 35.0",

            "119, 35.0",

            "120, 35.0",

            "121, 50.0"

    })

    void tarifasEnFronterasDeTiempo(int minutos, double costoEsperado) {

        // Arrange: cada fila proporciona los minutos y el costo esperado.
        // Act
        double resultado = sistema.calcularTotal(minutos, "normal", false);

        // Assert
        assertEquals(costoEsperado, resultado, 0.001);
    }

    @Test
    void minutosNegativosLanzanExcepcion() {


        // Arrange
        int minutos = -1;

        // Act y Assert
        assertThrows(IllegalArgumentException.class,() -> sistema.calcularTotal(minutos, "normal", false));
    }

    @Test
    void tipoClienteInvalidoLanzaExcepcion() {

        // Arrange
        int minutos = 30;
        String tipoCliente = "estudiante";

        // Act y Assert
        assertThrows(IllegalArgumentException.class,() -> sistema.calcularTotal(minutos, tipoCliente, false));
    }

    @Test
    void clienteFrecuenteRecibeDescuentoEnPrimeraHora() {

        // Arrange
        int minutos = 60;

        // Act
        double resultado = sistema.calcularTotal(minutos, "frecuente", false);

        // Assert
        assertEquals(18.0, resultado, 0.001);

    }

    @Test
    void clienteFrecuenteRecibeDescuentoEnHorasAdicionales() {
        // Arrange
        int minutos = 61;

        // Act
        double resultado = sistema.calcularTotal(minutos, "frecuente", false);

        // Assert
        assertEquals(31.50, resultado, 0.001);
    }

    @Test
    void boletoPerdidoCuestaTrescientosPesos() {
        // Arrange
        int minutos = 180;

        // Act
        double resultado = sistema.calcularTotal(minutos, "normal", true);

        // Assert
        assertEquals(300.0, resultado, 0.001);
    }

    @Test
    void boletoPerdidoNoRecibeDescuentoPorSerClienteFrecuente() {
        // Arrange
        int minutos = 180;

        // Act
        double resultado = sistema.calcularTotal(minutos, "frecuente", true);

        // Assert
        assertEquals(300.0, resultado, 0.001);
    }

    @Test
    void boletoPerdidoSeCobraInclusoConCeroMinutos() {
        // Arrange
        int minutos = 0;

        // Act
        double resultado = sistema.calcularTotal(minutos, "frecuente", true);

        // Assert
        assertEquals(300.0, resultado, 0.001);
    }

    @Test
    void costoCalculadoNuncaEsNegativo() {
        // Arrange
        int minutos = 30;

        // Act
        double resultado = sistema.calcularTotal(minutos, "normal", false);

        // Assert
        assertTrue(resultado >= 0.0);
    }
}
