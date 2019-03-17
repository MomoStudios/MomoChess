from flask import render_template

def create_routes(app):
  # Set "homepage" to index.html
  @app.route('/')
  def index():
      return render_template('index.html')
  # Save e-mail to database and send to success page
  @app.route('/prereg', methods=['POST'])
  def prereg():
      email = None
      if request.method == 'POST':
          email = request.form['email']
          # Check that email does not already exist (not a great query, but works)
          if not db.session.query(User).filter(User.email == email).count():
              reg = User(email)
              db.session.add(reg)
              db.session.commit()
              return render_template('success.html')
      return render_template('index.html')
  return app
