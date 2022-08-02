import pymysql as p

def connect():
    return p.connect(host="localhost",user="root",password="",database="blog")

def insertauth(t):
    db=connect()
    sql="insert into Author values(%s,%s,%s,%s,%s)"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def insertuser(t):
    db=connect()
    sql="insert into User values(%s,%s,%s,%s,%s)"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def logauth(t):
    db=connect()
    sql="select A_UNAME,A_PASSWORD from Author where A_UNAME=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    ulist=cr.fetchall()
    db.commit()
    db.close()
    return ulist

def loguse(t):
    db=connect()
    sql="select U_NAME,U_PASSWORD from User where U_NAME=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    ulist=cr.fetchall()
    db.commit()
    db.close()
    return ulist

def insertauthpost(t):
    db=connect()
    sql="insert into Author_post values(%s,%s,%s,%s)"
    cr=db.cursor()
    cr.execute(sql,t)
    db.commit()
    db.close()

def selectAllPost():
    db=connect()
    sql="select * from Author_post"
    cr=db.cursor()
    cr.execute(sql)
    plist=cr.fetchall()
    db.commit()
    db.close()
    return plist

def selectYourPost(t):
    db=connect()
    sql="select * from Author_post where P_UNAME=%s"
    cr=db.cursor()
    cr.execute(sql,t)
    plist=cr.fetchall()
    db.commit()
    db.close()
    return plist



        
