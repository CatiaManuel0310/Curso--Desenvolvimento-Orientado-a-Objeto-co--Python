class Cliente:
    def __init__(self, n, fone):

        self._nome = n
        self._telefone = fone

     #método get
    def get_nome(self):
        return self._nome

    #método set
    def __set_name__(self, name):
        self._nome = name

