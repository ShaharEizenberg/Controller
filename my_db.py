import sqlite3

class DB:
    def __init__(self, db_name):
        """
        creating DB object and create sql in db_name
        :param db_name: the path to save the file
        """
        # the path of the file
        self.db_name = db_name
        # the name of the table
        self.Teachers_Tbl_name = "Teachers_Table"
        self.students_tbl_name = "Students_Table"
        self.students_status_tbl_name = "Students_Status"
        self.conn = None
        # the object that from it we will be able to resort to the sql
        self.cursor = None
        # create sql table
        self.createDB()

    def createDB(self):
        """
        the function creates sql table with: username, name, gender, birthday, email, password
        :return: None
        """
        # create connection with the sql
        self.conn = sqlite3.connect(self.db_name)
        # creating the object that from it we can resort to the sql
        self.cursor = self.conn.cursor()
        # create sql tables
        sql = []
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.Teachers_Tbl_name} (adminname NVARCHAR(30), password TEXT)")
        # saving changes
        self.conn.commit()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.students_tbl_name} (id TEXT, username NVARCHAR(30))")
        # saving changes
        self.conn.commit()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.students_status_tbl_name} (macaddress TEXT, position INT, internet NVARCHAR(3), computer NVARCHAR(3))")
        # saving changes
        self.conn.commit()
        """
        print(sql[0])
        for i in range(3):
            self.cursor.execute(sql[i])
            # saving changes
            self.conn.commit()
        """



    def _id_exist(self, id):
        """
        :param id: the id to search in the students_table
        :return: true if id exists in the students_table as an id, else, false
        """
        sql = f"SELECT username FROM {self.students_tbl_name} WHERE id='{id}'"
        self.cursor.execute(sql)
        return not len(self.cursor.fetchall()) == 0

    def get_table(self, table_name):
        """

        :return:
        """
        sql = f"SELECT * FROM {table_name}"
        self.cursor.execute(sql)
        print(self.cursor.fetchall())
        return self.cursor.fetchall()

    def get_macAdresses(self):
        """

        :return:
        """
        sql = f"SELECT macaddress FROM {self.students_status_tbl_name}"
        self.cursor.execute(sql)
        print(self.cursor.fetchall())
        return self.cursor.fetchall()

    def _macAddress_exist(self, mac):
        """
        :param id: the mac address of the computer
        :return: true if id exists in the students_table as an id, else, false
        """
        sql = f"SELECT position FROM {self.students_status_tbl_name} WHERE macaddress='{mac}'"
        self.cursor.execute(sql)
        return not len(self.cursor.fetchall()) == 0

    def getName_byId(self, id):
        """
        :param id: the id parameter
        :return: the user name of the student with the received id
        """
        sql = f"SELECT username FROM {self.students_tbl_name} WHERE id='{id}'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getBy_macAdress(self, mac):
        """
        :param mac: the mac address of the computer
        :return: a list of all of the users with the same gender as in {gender}
        """
        sql = f"SELECT * FROM {self.students_status_tbl_name} WHERE macaddress='{mac}'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def set_internet(self, mac, on):
        """
        the function update the internet status of the student with {mac}, to {on}, if mac doesn't exist doesn't do it
        :param mac: the mac address of the computer to check it's internet status
        :param on: True to set the internet status to "on", else change to False
        :return: true if mac exists in the sql as a macaddress, else, false
        """
        retValue = False
        if self._macAddress_exist(mac):
            retValue = True
            # update the internet status where the mac address equals to the mac the function received, and save changes
            sql = f"UPDATE {self.students_status_tbl_name} SET internet ='{on}' WHERE macaddress ='{mac}'"
            self.cursor.execute(sql)
            self.conn.commit()
        return retValue

    def set_comp(self, mac, on):
        """
        the function update the computer status (on or off if the computer is shut down) of the student with {mac}, to {on}, if mac doesn't exist doesn't do it
        :param mac: the mac address of the computer to check it's comp status on or off if the computer is shut down)
        :param on: True to set the comp status to "on", else change to "off"
        :return: true if mac exists in the sql as a macaddress, else, false
        """
        retValue = False
        if self._macAddress_exist(mac):
            retValue = True
            # update the username where it equals to the username the function received, and save changes
            sql = f"UPDATE {self.students_status_tbl_name} SET internet ='{on}' WHERE macaddress ='{mac}'"
            self.cursor.execute(sql)
            self.conn.commit()
        return retValue

    def add_user_to_studentStatus(self, mac, pos, internet, comp):
        """
        the function receives details of student and add this user to the students status sql table, if this user doesn't exist already
        :param mac: the mac address of the students computer
        :param pos: the position of the student's computer
        :param internet: the internet status of the student's computer
        :param comp: the computer status of the student ("on" or "off" for shut down computer)
        :return: true if this user wasn't exist already in the sql, else, return false
        """
        retValue = False
        if not self._macAddress_exist(mac):
            retValue = True
            # insert the new user and save changes
            sql = f"INSERT INTO {self.students_status_tbl_name} VALUES ('{mac}', '{pos}', '{internet}', '{comp}') "
            self.cursor.execute(sql)
            self.conn.commit()
        return retValue

    def add_user_to_student(self, id, username):
        """
        the function receives details of user and add this user to the students_tbl_name sql, if this user doesn't exist already
        :param id: the id of the new user
        :param username: the username of the new user
        :return: true if this user wasn't exist already in the sql, else, return false
        """
        retValue = False
        if not self._id_exist(id):
            retValue = True
            # insert the new user and save changes
            sql = f"INSERT INTO {self.students_tbl_name} VALUES ('{id}', '{username}') "
            self.cursor.execute(sql)
            self.conn.commit()
        return retValue

    def delete_user (self, username):
        """
        the function receives username and delete this user from the sql if this user exist in the sql
        :param username: the username of the user to remove
        :return:
        """
        retValue = False
        if self._username_exist(username):
            retValue = True
            # delete the user with the username the function received and save changes
            sql = f"DELETE FROM {self.tbl_name} WHERE username ='{username}' "
            self.cursor.execute(sql)
            self.conn.commit()
        return retValue

    def set_username(self, pr_username, new_username):
        """
        the function update the username of the user with {pr_username}, to {new_username}, if mac doesn't exist
        :param pr_username: the previous username of a row in the table
        :param new_username: the new username of this row in the table
        :return: true if pr_username exists in the sql as a username, else, false
        """
        retValue = False
        if self._username_exist(pr_username) and not self._username_exist(new_username):
            retValue = True
            # update the username where it equals to the username the function received, and save changes
            sql = f"UPDATE {self.tbl_name} SET username ='{new_username}' WHERE username ='{pr_username}' "
            self.cursor.execute(sql)
            self.conn.commit()
        return retValue

    def set_name(self, username, name):
        """
        the function update the name of the user with the username: {username}, to {name}
        :param username: the username of the row in the table
        :param name: the new name to set
        :return: true if username exists in the sql as a username, else, false
        """
        retValue = False
        if self._username_exist(username):
            retValue = True
            # update the name where the username is the username the function received, and save changes
            sql = f"UPDATE {self.tbl_name} SET name ='{name}' WHERE username ='{username}' "
            self.cursor.execute(sql)
            self.conn.commit()
        return retValue

    def set_gender(self, username, gender):
        """
        the function update the gender of the user with the username: {username}, to {gender}
        :param username: the username of the row in the table
        :param gender: the new gender to set
        :return: true if username exists in the sql as a username, else, false
        """
        retValue = False
        if self._username_exist(username):
            retValue = True
            # update the gender where the username is the username the function received, and save changes
            sql = f"UPDATE {self.tbl_name} SET gender ='{gender}' WHERE username ='{username}' "
            self.cursor.execute(sql)
            self.conn.commit()
        return retValue

    def set_birthday(self, username, birthday):
        """
        the function update the birthday of the user with the username: {username}, to {birthday}
        :param username: the username of the row in the table
        :param birthday: the new username
        :return: true if username exists in the sql as a username, else, false
        """
        retValue = False
        if self._username_exist(username):
            retValue = True
            # update the birthday where the username is the username the function received, and save changes
            sql = f"UPDATE {self.tbl_name} SET birthday ='{birthday}' WHERE username ='{username}' "
            self.cursor.execute(sql)
            self.conn.commit()
        return retValue

    def set_email(self, username, email):
        """
        the function update the email of the user with the username: {username}, to {email}
        :param username: the username of the row in the table
        :param email: the new email to set
        :return: true if username exists in the sql as a username, else, false
        """
        retValue = False
        if self._username_exist(username):
            retValue = True
            # update the email where the username is the username the function received, and save changes
            sql = f"UPDATE {self.tbl_name} SET email ='{email}' WHERE username ='{username}' "
            self.cursor.execute(sql)
            self.conn.commit()
        return retValue

    def set_password(self, username, password):
        """
        the function update the password of the user with the username: {username}, to {password}
        :param username: the username of the row in the table
        :param password: the new password to set
        :return: true if username exists in the sql as a username, else, false
        """
        retValue = False
        if self._username_exist(username):
            retValue = True
            # update the password where the username is the username the function received, and save changes
            sql = f"UPDATE {self.tbl_name} SET password ='{password}' WHERE username ='{username}' "
            self.cursor.execute(sql)
            self.conn.commit()
        return retValue


    def get_byGender(self, gender):
        """
        :param gender: the gender parameter
        :return: a list of all of the users with the same gender as in {gender}
        """
        sql = f"SELECT * FROM {self.tbl_name} WHERE gender ='{gender}'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def get_byAge(self, age):
        """
        :param age: the age of the user
        :return: a list of all of the users with the same age as in {age}
        """
        sql = f"SELECT * FROM {self.tbl_name} WHERE birthday LIKE '%{str(2021 - age)[2:]}'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()



if __name__ == '__main__':

    # create DB object and sql
    my_DB = DB("class_info.db")

    print(my_DB.add_user_to_studentStatus("64:00:6A:42:4D:D1", 0, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:95:CF", 1, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:4A:DC", 2, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:4B:C8", 3, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:93:FE", 4, "on", "on"))
    print(my_DB.add_user_to_studentStatus("50:9A:4C:2A:26:90", 5, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:4A:B4", 6, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:4A:B1", 7, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:4B:4E", 8, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:41:D9:23", 9, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:4A:DE", 10, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:95:DF", 11, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:4B:25", 12, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:95:BE", 13, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:4B:2F", 14, "on", "on"))
    print(my_DB.add_user_to_studentStatus("64:00:6A:42:50:5E", 15, "on", "on"))



    print(my_DB.add_user_to_student("123456789", "Shahar Eizenberg"))
    print(my_DB.add_user_to_student("234567891", "Sha"))
    print(my_DB.add_user_to_student("345678912", "Shahag"))
    print(my_DB.add_user_to_student("456789123", "Shnberg"))
    print(my_DB.add_user_to_student("567891234", "Shahar"))
    print(my_DB.add_user_to_student("678912345", "Shahazenberg"))
    print(my_DB.add_user_to_student("789123456", "Shah"))
    print(my_DB.add_user_to_student("891234567", "moshe"))
    print(my_DB.add_user_to_student("912345678", "idan"))
    print(my_DB.add_user_to_student("987654321", "ben"))
    print(my_DB.add_user_to_student("123123123", "yuval"))
    print(my_DB.add_user_to_student("321321321", "tal"))
    print(my_DB.add_user_to_student("789789789", "shimon"))
    print(my_DB.add_user_to_student("123321123", "dor"))
    print(my_DB.add_user_to_student("987789987", "ron"))
    print(my_DB.add_user_to_student("323456789", "uri"))

    my_DB.conn.close()


    """
    print(my_DB.add_user("moshe", "moshe something", "mkjl", "22.02.04", "moshe12@gamil.com", "m1111"))
    print(my_DB.add_user("shir", "shir something", "f", "29.07.04", "shir12@gamil.com", "s1234"))
    print(my_DB.add_user("dvir", "dvir something", "m", "29.02.04", "dvir12@gamil.com", "d1234"))

    
    # add users to the sql
    print(my_DB.add_user("Shahar", "Shahar Eizenberg", "m", "29.07.04", "shahar12@gamil.com", "s1234"))
    print(my_DB.add_user("moshe", "moshe something", "mkjl", "22.02.04", "moshe12@gamil.com", "m1111"))
    print(my_DB.add_user("shir", "shir something", "f", "29.07.04", "shir12@gamil.com", "s1234"))
    print(my_DB.add_user("dvir", "dvir something", "m", "29.02.04", "dvir12@gamil.com", "d1234"))
    print(my_DB.add_user("stav", "stav something", "m", "21.03.04", "stav12@gamil.com", "s1234"))
    print(my_DB.add_user("idan", "idan something", "m", "22.05.07", "idan12@gamil.com", "i1234"))
    print(my_DB.add_user("agam", "agam something", "f", "29.01.99", "agam12@gamil.com", "a1234"))
    print(my_DB.add_user("adam", "adam something", "m", "22.02.01", "adam12@gamil.com", "a1234"))

    # delete users from the sql
    print(my_DB.delete_user("moshe"))
    print(my_DB.delete_user("stav"))
    print(my_DB.delete_user("dvir"))
    print(my_DB.delete_user("adam"))

    # updating user's data
    print(my_DB.set_username("Shahar", "Shahar1"))
    print(my_DB.set_name("idan", "idan2 other"))
    print(my_DB.set_gender("moshe", "f"))
    print(my_DB.set_birthday("agam", "29.06.03"))
    print(my_DB.set_email("idan", "i22@gmail.com"))

    # printing list of all of the female users
    print("females: ", my_DB.get_byGender("f"))
    # printing list of all of the 17 years old users
    print("17 years old users: ", my_DB.get_byAge(17))
    # close the file
    """
