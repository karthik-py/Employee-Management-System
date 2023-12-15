
from flask import Flask,render_template,url_for,redirect,request,flash
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Angel@6729'
app.config['MYSQL_DB']='crud'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)

@app.route('/')
def hello():
     con=mysql.connection.cursor()
     sql='SELECT * FROM users'
     con.execute(sql)
     res=con.fetchall()
     return render_template('home.html',datas=res)

@app.route('/addusers',methods=['GET','POST'])
def addusers():
     if request.method=='POST':
          name=request.form['name']
          city=request.form['city']
          age=request.form['age']
          number=request.form['number']
          email=request.form['email']
          con=mysql.connection.cursor()
          sql='insert into users(NAME,CITY,AGE,email,mobile_number) VALUES (%s,%s,%s,%s,%s)'
          con.execute(sql,[name,city,age,email,number])
          mysql.connection.commit()
          con.close()
          flash('user detail added')
          return redirect(url_for('hello'))
     return render_template('add.html')

@app.route('/updates/<string:id>',methods=['GET','POST'])
def updates(id):
     con=mysql.connection.cursor()
     if request.method=='POST':
          name=request.form['name']
          city=request.form['city']
          age=request.form['age']
          number=request.form['number']
          email=request.form['email']
          con=mysql.connection.cursor()
          sql='update users set NAME=%s, CITY=%s ,AGE=%s, email=%s ,mobile_number=%s where ID=%s'
          con.execute(sql,[name,city,age,email,number,id])
          mysql.connection.commit()
          con.close()
          flash('user detail updated')
          return redirect(url_for('hello'))
          con=mysql.connection.cursor()
          
     sql='select * from users where ID=%s'
     con.execute(sql,[id])
     res=con.fetchone()
     return render_template('update.html',datas=res)     
          
@app.route('/deletes/<string:id>',methods=['GET','POST'])
def deletes(id):
     con=mysql.connection.cursor()
     sql='delete from users where ID=%s'
     con.execute(sql,[id])
     mysql.connection.commit()
     con.close()
     flash('user detail deleted')
     return redirect(url_for('hello'))

if __name__=='__main__':
    app.secret_key='abc123'
    app.run(debug=True)




 
