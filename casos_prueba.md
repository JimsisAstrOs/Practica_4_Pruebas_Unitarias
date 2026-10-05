# \# ***Casos de prueba definitivos***



|Caso|Entrada<br />(minutos, cliente, perdido)|Esperado|Tipo|Reglas|
|-|-|-|-|-|
|CP01|(30, normal, no)|$20.00|Normal|R6|
|CP02|(90, normal, no)|$35.00|Normal|R7|
|CP03|(180, normal, no)|$50.00|Normal|R7|
|CP04|(14, normal, no)|$0.00|Frontera|R5|
|CP05|(15, normal, no)|$0.00|Frontera|R5|
|CP06|(16, normal, no)|$20.00|Frontera|R6|
|CP07|(59, normal, no)|$20.00|Frontera|R6|
|CP08|(60, normal, no)|$20.00|Frontera|R6|
|CP09|(61, normal, no)|$35.00|Frontera|R7|
|CP10|(-1, normal, no)|Error|Inválido|R1, R10|
|CP11|(30, vip, no)|Error|Inválido|R2, R11|
|CP12|(61, frecuente, no)|$31.50|Interacción + decimal|R7, R8|
|CP13|(500, frecuente, sí)|$300.00|Interacción|R3, R8|
|CP14|(121, frecuente, no)|$45.00|Interacción|R7, R8|
|CP15|(1000, normal, no)|$260.00|Adicional|R7, R9|



