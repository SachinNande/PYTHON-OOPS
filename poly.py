
#polymorphism....


class Card:
    def makePayment(self):
        print("payment")

class DebitCard(Card):
    def makePayment(self):
        print("payment by debit card .")

class CreditCard(Card):
    def makePayment(self):
        print("payment by credit card .")

class SwipeMachine:
    def SwipeCard(self,object):
        object.makePayment()

cr = CreditCard()
sm = SwipeMachine()
sm.SwipeCard(cr)

db = DebitCard()
sm.SwipeCard(db)

