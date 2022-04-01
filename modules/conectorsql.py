_author_ = "Helder Moura"

import mysql.connector


class Interface_sql:
    """ This connector provide to connect remotely at database,
        and his methods provide a funcional actions to manipulate
        data at the database
        Este conector fornece conexão remota no banco de dados,
        e seus métodos fornecem ações funcionais para manipular
        dados no banco de dados
    """    
    user, password, host, db = "","", "",""

    def __init__(self, user, password, host, db):
        """Class constructor / Construtor da classe
        Args:
            user (string): Username to access database
            password (string): Password to access database
            host (string): ip address to acesse database
            db (string): Database name
        """        
        try:            
            self.user = user            
            self.password = password
            self.host = host
            self.db = db        
        except Exception as e:
            print(str(e))

    def connect(self):
        """ Establishing a connection with the database
            Estabelecendo uma conexão com o banco de dados
        Returns:
            [variables]: Return connection information and cursor
        """
        try:
            con = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.db)
            cursor = con.cursor()
            return con, cursor        
        except Exception as e:
            print(f"Connection error {str(e)}")
    
    def desconnect(self, con, cursor):
        """ Close connection with database
            Fecha a conexão com o banco de dados
        Args:
            con (variable): Return connection information
            cursor (variable): Return cursor information
        """
        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print(f"Desconection error {str(e)}")
    
    def action(self, query):
        """ Establish connection, execute "query" and close connection.
        Args:
            query (string): Receive "query" from function.
        
        """
        try:
            con, cursor = self.connect()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Insert Error {str(e)}")
        finally:
            self.desconnect(con, cursor)