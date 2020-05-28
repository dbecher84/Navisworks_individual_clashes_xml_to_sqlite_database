

import datetime
import sqlite3
import easygui
from sqlite3 import Error
#import xml.etree.ElementTree as ET

import read_xml_func

from fill_tables_func import fill_test_table
from fill_tables_func import fill_results_table
#from sqlite_create_db import create_clash_table
from choose_date_func import pick_date


db_loc = "C:\\sqlite\\db\\navis_test_individ.db"
#path='C:\\Users\\Derek.Becher\\Desktop\\test\\clashes_in_sql\\00.01 Structural vs Architectural.xml'
path = easygui.diropenbox(msg='Select folder containing clash results.', title='Select Test Folder', default='c:\\')

clash_list = []

clash_date_list = []


#connection to database
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
 
    return conn


tests = [('00.00', 'Structural vs Structural'), ('00.01', 'Structural vs Architectural'), ('00.02', 'Structural vs Equipment'), ('00.03', 'Structural vs Fire Protection'),
         ('00.04', 'Structural vs HVAC'), ('00.05', 'Structural vs Piping Mechanical'), ('00.06', 'Structural vs Plumbing'), ('00.07', 'Structural vs Piping Process'), ('00.08', 'Structural vs Electrical'),
         ('01.02', 'Architectural vs Equipment'), ('01.03', 'Architectural vs Fire Protection'),('01.04', 'Architectural vs HVAC'), ('01.05', 'Architectural vs Piping Mechanical'),
         ('01.06', 'Architectural vs Plumbing'), ('01.07', 'Architectural vs Piping Process'), ('01.08', 'Architectural vs Electrical'),
         ('02.03', 'Equipment vs Fire Protection'), ('02.04', 'Equipment vs HVAC'), ('02.05', 'Equipment vs Piping Mechanical'), ('02.06', 'Equipment vs Plumbing'),
         ('02.07', 'Equipment vs Piping Process'),('02.08', 'Equipment vs Electrical'),
         ('03.03', 'Fire Protection vs Fire Protection'), ('03.04', 'Fire Protection vs HVAC'), ('03.05', 'Fire Protection vs Piping Mechanical'), ('03.06', 'Fire Protection vs Plumbing'),
         ('03.07', 'Fire Protection vs Piping Process'), ('03.08', 'Fire Protection vs Electrical'),
         ('04.04', 'HVAC vs HVAC'), ('04.05', 'HVAC vs Piping Mechanical'), ('04.06', 'HVAC vs Plumbing'), ('04.07', 'HVAC vs Piping Process'), ('04.08', 'HVAC vs Electrical'),
         ('05.05', 'Piping Mechanical vs Piping Mechanical'), ('05.06', 'Piping Mechanical vs Plumbing'), ('05.07', 'Piping Mechanical vs Piping Process'), ('05.08', 'Piping Mechanical vs Electrical'),
         ('06.06', 'Plumbing vs Plumbing'), ('06.07', 'Plumbing vs Piping Process'), ('06.08', 'Plumbing vs Electrical'),
         ('07.07', 'Piping Process vs Piping Process'), ('07.08', 'Piping Process vs Electrical'),
         ('08.08', 'Electrical vs Electrical')]

#tests = [('00.08', 'Structural vs Electrical')]

#populate clash test table
def test_table():
    '''populate table with tests name & id'''
    #create a database connection
    conn = create_connection(db_loc)
    with conn:
        # create a new project
        for item in tests:
            project = (item);
            project_id = fill_test_table(conn, project)
    conn.close()



def clash_table():
    '''populate results table'''
    #create a database connection
    conn = create_connection(db_loc)
    with conn:
        # create a new project
        i = 0
        for item in clash_list:
            #print (item)
            clash = (item);
            clash_id = fill_results_table(conn, clash)
            i =+ 1
            
    conn.close()
    

#def table_name_add_date():
#    '''adds date to end of new table named clash_results'''
#    now = datetime.datetime.now()
#    now2 = now.strftime('%Y_%m_%d')

#    conn = create_connection(db_loc)
    
#    rename_table = "ALTER TABLE clash_results RENAME TO newname"
#    new_name = rename_table.replace('newname', 'clash_results_' + str(now2))
#    cursor = conn.cursor()
#    cursor.execute(new_name)
#    conn.close

def get_tests():
    for item in tests:
        read_xml_func.tests(item[0], path + '\\' + item[0] + ' ' + item[1] + '.xml', results_date)


if __name__ == '__main__':
    user_date_input = input('Is the test date todays date? Y or N: ')
    results_date = pick_date(user_date_input)
    print (results_date)
    
    if results_date == None:
        results_date = pick_date(user_date_input)

    get_tests()
        
    clash_list = read_xml_func.clash_list
    print (len(clash_list))
    test_list = []
    for item in clash_list:
        if len(item) != 9:
            test_list.append(item)
    print (test_list)

    user_input = input('Has the test table already been populated? Y or N: ')
    print (user_input)
    if user_input.lower() == 'y':
        clash_table()
        print ('Results data added successfully.')
    elif user_input.lower() == 'n':
        test_table()
        clash_table()
        print ('Tests & Results data added successfully.')
    else:
        print ('Invalid Input. Must be Y or N')

