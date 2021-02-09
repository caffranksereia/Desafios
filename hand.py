from resposta import verificatedResult
from cards import Cards
from suit import suit
from handWin import *

class PokeHand():
    def __init__(self,handWin):
        self.card = []
        self.suit = []
        self.handWin = HandWin
        self.myHand = []

        

    #verifica os pontos
    def verificatedPonts(self):
        if myhand == HandWin.Royal_flush:
            return verificatedResult.win
        elif myHand == HandWin.Flush:
            return verificatedResult.win
        elif myHand == HandWin.Straight:
            return verificatedResult.win
        elif myHand == HandWin.Straight_flush:
            return verificatedResult.win
        else:
            return verificatedResult.lose
