from pythonds.basic.stack import Stack

s = Stack()

class Pilha:
      def __init__(self):
          self.p = []
      def push(self, n):
            self.p.append(n)
      def pop(self):
            return self.p.pop()
      def isEmpty(self):
            return self.p == []
      def top(self):
            return self.p[len(self.p - 1)]
            
def binary (n):
      p = Pilha()
      while n > 0:
            if n % 2 == 0:
                  p.push(0)
            else:
                  p.push(1)
            n = int(n/2)
      while (not p.isEmpty()):
            print(p.pop(), end='')

binary(12)