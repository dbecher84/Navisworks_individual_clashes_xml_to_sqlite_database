

import datetime
import xml.etree.ElementTree as ET

#path='C:\\Users\\Derek.Becher\\Desktop\\test\\clashes_in_sql\\00.01 Structural vs Architectural.xml'
#path='C:\\Users\\Derek.Becher\\Desktop\\test\\clashes_in_sql\\navis_output\\'

#test = ['00.01 Structural vs Architectural.xml', '02.06 Equipment vs Plumbing.xml']

#tree = ET.parse(path)
#root = tree.getroot()

clash_list = []

def tests(number, test_file, results_date):
    '''searches xml file for clash information and adds to a list.
       number: clash test number
       test_file: path to test file'''
    tree = ET.parse(test_file)
    #root = tree.getroot()
    
    for node in tree.iter('clashresult'):
        #print ('\\n')
        clash_info = []
        elem_present = []
        for elem in node.iter():
            #elem_present = []
            if elem.tag=='clashresult':
                clash_items = [elem.get('guid'), elem.get('name'), elem.get('status')]
                for item in clash_items:    
                    clash_info.append(item)
                #print (clash_info)
            if elem.tag=='parentgroup':
                p_group = elem.text
                #clash_info.append(p_group)
                elem_present.append('parent_group')
                #print (p_group)           
            if elem.tag=='date':
                created_date = [elem.get('year'), elem.get('month'), elem.get('day')]
                clean_date = '{}.{}.{}'.format(created_date[0],created_date[1].zfill(2) ,created_date[2].zfill(2))
                #clash_info.append(clean_date)
                elem_present.append('created_date')
                #print (clean_date)
            if elem.tag=='objectattribute':
                for obj in elem:
                    if obj.tag=='value':
                        elem_ids = obj.text
                        clash_info.append(elem_ids)
                        elem_present.append('element_id')
                        #print (elem_ids)
            if elem.tag=='assignedto':
                assign_to=elem.text
                #clash_info.append(assign_to)
                elem_present.append('assigned_to')
                


        #print (elem_present.count('element_id'))
        if elem_present.count('element_id') == 1:
            clash_info.insert(4, 'NO_ID')
            
        if elem_present.count('element_id') == 0:
            clash_info.insert(3, 'NO_ID')
            clash_info.insert(4, 'NO_ID')
                
        if 'parent_group' in elem_present:
            clash_info.append(p_group)
        else:
            clash_info.append('NO_GROUP')

        if 'created_date' in elem_present:
            clash_info.append(clean_date)
        else:
            clash_info.append('No_Date')
            
        if 'assigned_to' in elem_present:
            clash_info.append(assign_to)
        else:
            clash_info.append('NO_Assignee')
        

        
        #now = datetime.datetime.now()
        #clash_report_date = now.strftime('%Y.%m.%d')
        clash_info.append(results_date)

        clash_info.append(number)

        clash_list.append(clash_info)
    
