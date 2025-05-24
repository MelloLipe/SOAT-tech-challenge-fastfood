
class DomainEventDispatcher:
    def __init__(self):
        self._eventos = []

    def registrar(self, evento):
        self._eventos.append(evento)

    def despachar(self):
        for evento in self._eventos:
            print(f"[EVENTO] {evento.__class__.__name__} - {vars(evento)}")
        self._eventos.clear()
