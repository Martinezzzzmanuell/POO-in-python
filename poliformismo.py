#HERENCIA AND POLIFORMISMO

class services:#CLASS Main
    def __init__(self ,connect,To_disconnect):
        self.connect=connect
        self.To_disconnect=To_disconnect

class services_email(services):
    def __init__(self,connect):
      super().__init__(connect,None)

class services_BD(services):
    def __init__(self,connect):
        super().__init__(connect,None)

class services_cache(services):
    def __init__(self,To_disconnect):
        super().__init__( None,To_disconnect)

services_1=services_email("Conectado")
services_2=services_BD("Conectado")
services_3=services_cache("Desconectado")

print(f'The service of Email it was possible {services_1.connect} to the  services SMTP')
print(f'The service of Bases of datos was possible {services_2.connect} to the services PostgreSQL ')
print(f"'The service of cache it wans't possible connect to thw service of Redis state of the services??{services_3.To_disconnect}'")



