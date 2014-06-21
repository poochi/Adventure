import os;
from xml.dom import minidom
"WhenEver a new object is added update this dictionary  "
"Object passing as a dictionary "

#definedclasses = {'GOLD':'collectibles.GOLD','fly':'Enemies.fly','SILVER':'collectibles.SILVER'}


def parseconfig(listnames):
    """ Parses game config file """
    xmldoc = minidom.parse(os.path.join(os.getcwd(),"..",'GAMECONFIG.xml'))
    loadable = open("loadable.py","w");
    for eachlistname in listnames :
        
        itemlist = xmldoc.getElementsByTagName(eachlistname);
        
        element = eachlistname;
        print element
        loadable.write(str(element)+'= ')
        #Non empty elements in itemlist only
        res=[];
        
        for each in itemlist:
            attr = each.attributes.keys();
            print attr 
            ele = each.attributes['name'].value
            
            itemlist1 = xmldoc.getElementsByTagName(ele);
            for eachp in itemlist1:
                res.append(dict(zip(each.attributes.keys()+eachp.attributes.keys(),[each.attributes[t].value for t in each.attributes.keys()]+
                                    [eachp.attributes[t].value for t in eachp.attributes.keys()])));
        loadable.write(str(res));
        loadable.write('\n\n');
    loadable.close();
            
        
            
            
    
if __name__ == '__main__':
    parseconfig(['collectible','Rocks','FlyingObject','Fly','Movableplatforms','Immovableplatforms','BACKGOUND_PATH_LIST']);
