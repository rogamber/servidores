def menu_inicio():
    import sqlite3
    con = sqlite3.connect('datos.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM menu_inicio" ) 
    datos = cur.fetchall()
    # salvar (commit) los cambios 
    con.commit()
    con.close()
    return(datos)

def menu_temp1():
    import sqlite3
    con = sqlite3.connect('datos.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM menu_temp1" ) 
    datos = cur.fetchall()
    # salvar (commit) los cambios 
    con.commit()
    con.close()
    return(datos)

def menu_temp2():
    import sqlite3
    con = sqlite3.connect('datos.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM menu_temp2" ) 
    datos = cur.fetchall()
    # salvar (commit) los cambios 
    con.commit()
    con.close()
    return(datos)

def menu_temp3():
    import sqlite3
    con = sqlite3.connect('datos.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM menu_temp3" ) 
    datos = cur.fetchall()

def menu_pelis():
    import sqlite3
    con = sqlite3.connect('datos.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM menu_pelis" ) 
    datos = cur.fetchall()

    # salvar (commit) los cambios 
    con.commit()
    con.close()
    return(datos)