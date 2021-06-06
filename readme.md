# Message Flashing - Despliegue de Mensajes

- las buenas aplicaciones e interfases de usuarios siempre dan feedback a sus usuarios.

- si los usuarios no tienen suficiente feedback es muy probable que les frustre y terminen odiando la aplicacion.

- flask provee una forma muy sencilla de generar este feedback y es ocupando un sistema interno de despliegue de mensajes.

- este sistema de mensajes, funciona grabando un mensaje en la parte final de un request y luego accederlo en el siguiente request pero solamente en en proximo request.

- este sistema se asocia normalemente con nuestro template base o layout.

- es importante notar que algunos navegadores y servidores web pueden poner limites en los tamanios de las cookies por lo que hay que tratar de no colocar mensajes demasiado largos ya que podria fallar inesperadamente.
