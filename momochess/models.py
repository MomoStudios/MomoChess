# Create our database model
class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True)

  def __init__(self, email):
    self.email = email

  def __repr__(self):
    return '<E-mail %r>' % self.email

class Board(db.Model):
  __tablename__ = "board"
  id = db.Column(db.Integer, primary_key=True)
  def is_legal(self, x_pos, y_pos):
    if (x_pos < 0 or x_pos > 8):
      return False
    if (y_pos < 0 or y_pos > 8):
      return False
    return True

class Square(db.Model):
  __tablename__ = "square
  id = db.Column(db.Integer, primary_key=True)
  board_id = db.Column(db.Integer, db.ForeignKey(Board.id), nullable = false)
  x_position = db.Column(db.Integer, nullable = false)
  y_position = db.Column(db.Integer, nullable = false)

class Game(db.Model):
  __tablename__ = "game"
  id = db.Column(db.Integer, primary_key=True)
  user1_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable = false)
  user2_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable = false)
  board_id = db.Column(db.Integer, db.ForeignKey(Board.id), nullable = false)
  board = db.relationship('board',
    backref=db.backref('game', lazy=True))

  turn_number = db.Column(db.Integer)
  in_progress = db.Column(db.Boolean, nullable = false)
  current_turn = db.Column(db.Integer, db.ForeignKey(User.id))

  def __init__(self, user1, user2):
    self.user1_id = user1.id
    self.user2_id = user2.id
    turn_number = 0
    in_progress = False #update when game begins
    current_turn = user1.id #just start with user1

  # return true or false if succeeded
  def attempt_move(self, user, from_square, to_square):
    uid = user.id
    if not self.in_progress:
      return False

    if not (uid == self.user1_id or uid == self.user2_id):
      return False
    
    if not (uid == self.current_turn):
      return False
    
    


    



    
