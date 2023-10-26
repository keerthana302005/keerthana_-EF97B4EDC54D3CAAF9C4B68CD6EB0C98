
class player:
  def play(self):
    print ("Theplayerisplayingcricket.")

class Batsman (player):
  def play (self):
    print ("Thebatsmanisbatting.")

class Bowler(player):
  def play(self):
    print ("Thebowlerisbowling.")

batsman=Batsman()
bowler=Bowler()

batsman.play()
bowler.play()
