class Cidade():
      def __init__(self):
            self.nome_cidade =  'Sao Jose do Campos'


class Bairro(Cidade):
      def __init__(self):
          super().__init__()
          self.nome_bairro = 'Campus do CTA'

class Rua(Bairro):
      def __init__(self, rua):
          super().__init__()
          self.nome_rua = rua
      
class Casa(Rua):
      def __init__(self, rua, numero):
          super().__init__(rua)
          self.numero = numero
      
      def endereco (self):
            return 'Rua {0}, n {1}, {2} - {3}'.format(self.nome_rua, self.numero, self.nome_bairro, self.nome_cidade)



ap_h8 = Casa('H8B', 208)

print(ap_h8.endereco())