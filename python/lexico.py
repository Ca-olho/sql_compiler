#Estados
start_state = 0
error_state = 55
final_state = [1,2,3,4,5,6,7,8,9,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55]

#Caracteres
output_symbol = ['V','V','V','V','V','V','V','V','N','V','V','V','V','V','V','V','V','V','V','V','V','V','V','V','V','V','V','V','D','F','V','O','V','V','V','V','V','V','V','T','V','C','V','I','S','L','V','B','X']
    #Legenda:
        #V = var
        #N = num
        #C = create
        #D = drop
        #T = table
        #B = database
        #I = insert
        #O = into
        #L = values
        #S = select
        #F = from
        #X = erro
separator = [' ','\n','\t',',',';','*','(',')','\'','$']
ignore = [' ','\n','\t']

#Transições
#(estado atual, caracter atual da fita, proximo estado)
transition = [
    (0,'a',1),(0,'b',1),(0,'c',2),(0,'d',3),(0,'e',1),(0,'f',4),(0,'g',1),(0,'h',1),(0,'i',5),(0,'j',1),(0,'k',1),(0,'l',1),(0,'m',1),(0,'n',1),(0,'o',1),(0,'p',1),(0,'q',1),(0,'r',1),(0,'s',6),(0,'t',7),(0,'u',1),(0,'v',8),(0,'w',1),(0,'x',1),(0,'y',1),(0,'z',1),(0,'0',9),(0,'1',9),(0,'2',9),(0,'3',9),(0,'4',9),(0,'5',9),(0,'6',9),(0,'7',9),(0,'8',9),(0,'9',9),(0,'_',1),
    (1,'a',1),(1,'b',1),(1,'c',1),(1,'d',1),(1,'e',1),(1,'f',1),(1,'g',1),(1,'h',1),(1,'i',1),(1,'j',1),(1,'k',1),(1,'l',1),(1,'m',1),(1,'n',1),(1,'o',1),(1,'p',1),(1,'q',1),(1,'r',1),(1,'s',1),(1,'t',1),(1,'u',1),(1,'v',1),(1,'w',1),(1,'x',1),(1,'y',1),(1,'z',1),(1,'0',1),(1,'1',1),(1,'2',1),(1,'3',1),(1,'4',1),(1,'5',1),(1,'6',1),(1,'7',1),(1,'8',1),(1,'9',1),(1,'_',1),
    (2,'a',1),(2,'b',1),(2,'c',1),(2,'d',1),(2,'e',1),(2,'f',1),(2,'g',1),(2,'h',1),(2,'i',1),(2,'j',1),(2,'k',1),(2,'l',1),(2,'m',1),(2,'n',1),(2,'o',1),(2,'p',1),(2,'q',1),(2,'r',16),(2,'s',1),(2,'t',1),(2,'u',1),(2,'v',1),(2,'w',1),(2,'x',1),(2,'y',1),(2,'z',1),(2,'0',1),(2,'1',1),(2,'2',1),(2,'3',1),(2,'4',1),(2,'5',1),(2,'6',1),(2,'7',1),(2,'8',1),(2,'9',1),(2,'_',1),
    (3,'a',17),(3,'b',1),(3,'c',1),(3,'d',1),(3,'e',1),(3,'f',1),(3,'g',1),(3,'h',1),(3,'i',1),(3,'j',1),(3,'k',1),(3,'l',1),(3,'m',1),(3,'n',1),(3,'o',1),(3,'p',1),(3,'q',1),(3,'r',18),(3,'s',1),(3,'t',1),(3,'u',1),(3,'v',1),(3,'w',1),(3,'x',1),(3,'y',1),(3,'z',1),(3,'0',1),(3,'1',1),(3,'2',1),(3,'3',1),(3,'4',1),(3,'5',1),(3,'6',1),(3,'7',1),(3,'8',1),(3,'9',1),(3,'_',1),
    (4,'a',1),(4,'b',1),(4,'c',1),(4,'d',1),(4,'e',1),(4,'f',1),(4,'g',1),(4,'h',1),(4,'i',1),(4,'j',1),(4,'k',1),(4,'l',1),(4,'m',1),(4,'n',1),(4,'o',1),(4,'p',1),(4,'q',1),(4,'r',19),(4,'s',1),(4,'t',1),(4,'u',1),(4,'v',1),(4,'w',1),(4,'x',1),(4,'y',1),(4,'z',1),(4,'0',1),(4,'1',1),(4,'2',1),(4,'3',1),(4,'4',1),(4,'5',1),(4,'6',1),(4,'7',1),(4,'8',1),(4,'9',1),(4,'_',1),
    (5,'a',1),(5,'b',1),(5,'c',1),(5,'d',1),(5,'e',1),(5,'f',1),(5,'g',1),(5,'h',1),(5,'i',1),(5,'j',1),(5,'k',1),(5,'l',1),(5,'m',1),(5,'n',20),(5,'o',1),(5,'p',1),(5,'q',1),(5,'r',1),(5,'s',1),(5,'t',1),(5,'u',1),(5,'v',1),(5,'w',1),(5,'x',1),(5,'y',1),(5,'z',1),(5,'0',1),(5,'1',1),(5,'2',1),(5,'3',1),(5,'4',1),(5,'5',1),(5,'6',1),(5,'7',1),(5,'8',1),(5,'9',1),(5,'_',1),
    (6,'a',1),(6,'b',1),(6,'c',1),(6,'d',1),(6,'e',21),(6,'f',1),(6,'g',1),(6,'h',1),(6,'i',1),(6,'j',1),(6,'k',1),(6,'l',1),(6,'m',1),(6,'n',1),(6,'o',1),(6,'p',1),(6,'q',1),(6,'r',1),(6,'s',1),(6,'t',1),(6,'u',1),(6,'v',1),(6,'w',1),(6,'x',1),(6,'y',1),(6,'z',1),(6,'0',1),(6,'1',1),(6,'2',1),(6,'3',1),(6,'4',1),(6,'5',1),(6,'6',1),(6,'7',1),(6,'8',1),(6,'9',1),(6,'_',1),
    (7,'a',22),(7,'b',1),(7,'c',1),(7,'d',1),(7,'e',1),(7,'f',1),(7,'g',1),(7,'h',1),(7,'i',1),(7,'j',1),(7,'k',1),(7,'l',1),(7,'m',1),(7,'n',1),(7,'o',1),(7,'p',1),(7,'q',1),(7,'r',1),(7,'s',1),(7,'t',1),(7,'u',1),(7,'v',1),(7,'w',1),(7,'x',1),(7,'y',1),(7,'z',1),(7,'0',1),(7,'1',1),(7,'2',1),(7,'3',1),(7,'4',1),(7,'5',1),(7,'6',1),(7,'7',1),(7,'8',1),(7,'9',1),(7,'_',1),
    (8,'a',23),(8,'b',1),(8,'c',1),(8,'d',1),(8,'e',1),(8,'f',1),(8,'g',1),(8,'h',1),(8,'i',1),(8,'j',1),(8,'k',1),(8,'l',1),(8,'m',1),(8,'n',1),(8,'o',1),(8,'p',1),(8,'q',1),(8,'r',1),(8,'s',1),(8,'t',1),(8,'u',1),(8,'v',1),(8,'w',1),(8,'x',1),(8,'y',1),(8,'z',1),(8,'0',1),(8,'1',1),(8,'2',1),(8,'3',1),(8,'4',1),(8,'5',1),(8,'6',1),(8,'7',1),(8,'8',1),(8,'9',1),(8,'_',1),
    (9,'a',1),(9,'b',1),(9,'c',1),(9,'d',1),(9,'e',1),(9,'f',1),(9,'g',1),(9,'h',1),(9,'i',1),(9,'j',1),(9,'k',1),(9,'l',1),(9,'m',1),(9,'n',1),(9,'o',1),(9,'p',1),(9,'q',1),(9,'r',1),(9,'s',1),(9,'t',1),(9,'u',1),(9,'v',1),(9,'w',1),(9,'x',1),(9,'y',1),(9,'z',1),(9,'0',9),(9,'1',9),(9,'2',9),(9,'3',9),(9,'4',9),(9,'5',9),(9,'6',9),(9,'7',9),(9,'8',9),(9,'9',9),(9,'_',1),
    (16,'a',1),(16,'b',1),(16,'c',1),(16,'d',1),(16,'e',24),(16,'f',1),(16,'g',1),(16,'h',1),(16,'i',1),(16,'j',1),(16,'k',1),(16,'l',1),(16,'m',1),(16,'n',1),(16,'o',1),(16,'p',1),(16,'q',1),(16,'r',1),(16,'s',1),(16,'t',1),(16,'u',1),(16,'v',1),(16,'w',1),(16,'x',1),(16,'y',1),(16,'z',1),(16,'0',1),(16,'1',1),(16,'2',1),(16,'3',1),(16,'4',1),(16,'5',1),(16,'6',1),(16,'7',1),(16,'8',1),(16,'9',1),(16,'_',1),
    (17,'a',1),(17,'b',1),(17,'c',1),(17,'d',1),(17,'e',1),(17,'f',1),(17,'g',1),(17,'h',1),(17,'i',1),(17,'j',1),(17,'k',1),(17,'l',1),(17,'m',1),(17,'n',1),(17,'o',1),(17,'p',1),(17,'q',1),(17,'r',1),(17,'s',1),(17,'t',25),(17,'u',1),(17,'v',1),(17,'w',1),(17,'x',1),(17,'y',1),(17,'z',1),(17,'0',1),(17,'1',1),(17,'2',1),(17,'3',1),(17,'4',1),(17,'5',1),(17,'6',1),(17,'7',1),(17,'8',1),(17,'9',1),(17,'_',1),
    (18,'a',1),(18,'b',1),(18,'c',1),(18,'d',1),(18,'e',1),(18,'f',1),(18,'g',1),(18,'h',1),(18,'i',1),(18,'j',1),(18,'k',1),(18,'l',1),(18,'m',1),(18,'n',1),(18,'o',26),(18,'p',1),(18,'q',1),(18,'r',1),(18,'s',1),(18,'t',1),(18,'u',1),(18,'v',1),(18,'w',1),(18,'x',1),(18,'y',1),(18,'z',1),(18,'0',1),(18,'1',1),(18,'2',1),(18,'3',1),(18,'4',1),(18,'5',1),(18,'6',1),(18,'7',1),(18,'8',1),(18,'9',1),(18,'_',1),
    (19,'a',1),(19,'b',1),(19,'c',1),(19,'d',1),(19,'e',1),(19,'f',1),(19,'g',1),(19,'h',1),(19,'i',1),(19,'j',1),(19,'k',1),(19,'l',1),(19,'m',1),(19,'n',1),(19,'o',27),(19,'p',1),(19,'q',1),(19,'r',1),(19,'s',1),(19,'t',1),(19,'u',1),(19,'v',1),(19,'w',1),(19,'x',1),(19,'y',1),(19,'z',1),(19,'0',1),(19,'1',1),(19,'2',1),(19,'3',1),(19,'4',1),(19,'5',1),(19,'6',1),(19,'7',1),(19,'8',1),(19,'9',1),(19,'_',1),
    (20,'a',1),(20,'b',1),(20,'c',1),(20,'d',1),(20,'e',1),(20,'f',1),(20,'g',1),(20,'h',1),(20,'i',1),(20,'j',1),(20,'k',1),(20,'l',1),(20,'m',1),(20,'n',1),(20,'o',1),(20,'p',1),(20,'q',1),(20,'r',1),(20,'s',28),(20,'t',29),(20,'u',1),(20,'v',1),(20,'w',1),(20,'x',1),(20,'y',1),(20,'z',1),(20,'0',1),(20,'1',1),(20,'2',1),(20,'3',1),(20,'4',1),(20,'5',1),(20,'6',1),(20,'7',1),(20,'8',1),(20,'9',1),(20,'_',1),
    (21,'a',1),(21,'b',1),(21,'c',1),(21,'d',1),(21,'e',1),(21,'f',1),(21,'g',1),(21,'h',1),(21,'i',1),(21,'j',1),(21,'k',1),(21,'l',30),(21,'m',1),(21,'n',1),(21,'o',1),(21,'p',1),(21,'q',1),(21,'r',1),(21,'s',1),(21,'t',1),(21,'u',1),(21,'v',1),(21,'w',1),(21,'x',1),(21,'y',1),(21,'z',1),(21,'0',1),(21,'1',1),(21,'2',1),(21,'3',1),(21,'4',1),(21,'5',1),(21,'6',1),(21,'7',1),(21,'8',1),(21,'9',1),(21,'_',1),
    (22,'a',1),(22,'b',31),(22,'c',1),(22,'d',1),(22,'e',1),(22,'f',1),(22,'g',1),(22,'h',1),(22,'i',1),(22,'j',1),(22,'k',1),(22,'l',1),(22,'m',1),(22,'n',1),(22,'o',1),(22,'p',1),(22,'q',1),(22,'r',1),(22,'s',1),(22,'t',1),(22,'u',1),(22,'v',1),(22,'w',1),(22,'x',1),(22,'y',1),(22,'z',1),(22,'0',1),(22,'1',1),(22,'2',1),(22,'3',1),(22,'4',1),(22,'5',1),(22,'6',1),(22,'7',1),(22,'8',1),(22,'9',1),(22,'_',1),
    (23,'a',1),(23,'b',1),(23,'c',1),(23,'d',1),(23,'e',1),(23,'f',1),(23,'g',1),(23,'h',1),(23,'i',1),(23,'j',1),(23,'k',1),(23,'l',32),(23,'m',1),(23,'n',1),(23,'o',1),(23,'p',1),(23,'q',1),(23,'r',1),(23,'s',1),(23,'t',1),(23,'u',1),(23,'v',1),(23,'w',1),(23,'x',1),(23,'y',1),(23,'z',1),(23,'0',1),(23,'1',1),(23,'2',1),(23,'3',1),(23,'4',1),(23,'5',1),(23,'6',1),(23,'7',1),(23,'8',1),(23,'9',1),(23,'_',1),
    (24,'a',33),(24,'b',1),(24,'c',1),(24,'d',1),(24,'e',1),(24,'f',1),(24,'g',1),(24,'h',1),(24,'i',1),(24,'j',1),(24,'k',1),(24,'l',1),(24,'m',1),(24,'n',1),(24,'o',1),(24,'p',1),(24,'q',1),(24,'r',1),(24,'s',1),(24,'t',1),(24,'u',1),(24,'v',1),(24,'w',1),(24,'x',1),(24,'y',1),(24,'z',1),(24,'0',1),(24,'1',1),(24,'2',1),(24,'3',1),(24,'4',1),(24,'5',1),(24,'6',1),(24,'7',1),(24,'8',1),(24,'9',1),(24,'_',1),
    (25,'a',34),(25,'b',1),(25,'c',1),(25,'d',1),(25,'e',1),(25,'f',1),(25,'g',1),(25,'h',1),(25,'i',1),(25,'j',1),(25,'k',1),(25,'l',1),(25,'m',1),(25,'n',1),(25,'o',1),(25,'p',1),(25,'q',1),(25,'r',1),(25,'s',1),(25,'t',1),(25,'u',1),(25,'v',1),(25,'w',1),(25,'x',1),(25,'y',1),(25,'z',1),(25,'0',1),(25,'1',1),(25,'2',1),(25,'3',1),(25,'4',1),(25,'5',1),(25,'6',1),(25,'7',1),(25,'8',1),(25,'9',1),(25,'_',1),
    (26,'a',1),(26,'b',1),(26,'c',1),(26,'d',1),(26,'e',1),(26,'f',1),(26,'g',1),(26,'h',1),(26,'i',1),(26,'j',1),(26,'k',1),(26,'l',1),(26,'m',1),(26,'n',1),(26,'o',1),(26,'p',35),(26,'q',1),(26,'r',1),(26,'s',1),(26,'t',1),(26,'u',1),(26,'v',1),(26,'w',1),(26,'x',1),(26,'y',1),(26,'z',1),(26,'0',1),(26,'1',1),(26,'2',1),(26,'3',1),(26,'4',1),(26,'5',1),(26,'6',1),(26,'7',1),(26,'8',1),(26,'9',1),(26,'_',1),
    (27,'a',1),(27,'b',1),(27,'c',1),(27,'d',1),(27,'e',1),(27,'f',1),(27,'g',1),(27,'h',1),(27,'i',1),(27,'j',1),(27,'k',1),(27,'l',1),(27,'m',36),(27,'n',1),(27,'o',1),(27,'p',1),(27,'q',1),(27,'r',1),(27,'s',1),(27,'t',1),(27,'u',1),(27,'v',1),(27,'w',1),(27,'x',1),(27,'y',1),(27,'z',1),(27,'0',1),(27,'1',1),(27,'2',1),(27,'3',1),(27,'4',1),(27,'5',1),(27,'6',1),(27,'7',1),(27,'8',1),(27,'9',1),(27,'_',1),
    (28,'a',1),(28,'b',1),(28,'c',1),(28,'d',1),(28,'e',37),(28,'f',1),(28,'g',1),(28,'h',1),(28,'i',1),(28,'j',1),(28,'k',1),(28,'l',1),(28,'m',1),(28,'n',1),(28,'o',1),(28,'p',1),(28,'q',1),(28,'r',1),(28,'s',1),(28,'t',1),(28,'u',1),(28,'v',1),(28,'w',1),(28,'x',1),(28,'y',1),(28,'z',1),(28,'0',1),(28,'1',1),(28,'2',1),(28,'3',1),(28,'4',1),(28,'5',1),(28,'6',1),(28,'7',1),(28,'8',1),(28,'9',1),(28,'_',1),
    (29,'a',1),(29,'b',1),(29,'c',1),(29,'d',1),(29,'e',1),(29,'f',1),(29,'g',1),(29,'h',1),(29,'i',1),(29,'j',1),(29,'k',1),(29,'l',1),(29,'m',1),(29,'n',1),(29,'o',38),(29,'p',1),(29,'q',1),(29,'r',1),(29,'s',1),(29,'t',1),(29,'u',1),(29,'v',1),(29,'w',1),(29,'x',1),(29,'y',1),(29,'z',1),(29,'0',1),(29,'1',1),(29,'2',1),(29,'3',1),(29,'4',1),(29,'5',1),(29,'6',1),(29,'7',1),(29,'8',1),(29,'9',1),(29,'_',1),
    (30,'a',1),(30,'b',1),(30,'c',1),(30,'d',1),(30,'e',39),(30,'f',1),(30,'g',1),(30,'h',1),(30,'i',1),(30,'j',1),(30,'k',1),(30,'l',1),(30,'m',1),(30,'n',1),(30,'o',1),(30,'p',1),(30,'q',1),(30,'r',1),(30,'s',1),(30,'t',1),(30,'u',1),(30,'v',1),(30,'w',1),(30,'x',1),(30,'y',1),(30,'z',1),(30,'0',1),(30,'1',1),(30,'2',1),(30,'3',1),(30,'4',1),(30,'5',1),(30,'6',1),(30,'7',1),(30,'8',1),(30,'9',1),(30,'_',1),
    (31,'a',1),(31,'b',1),(31,'c',1),(31,'d',1),(31,'e',1),(31,'f',1),(31,'g',1),(31,'h',1),(31,'i',1),(31,'j',1),(31,'k',1),(31,'l',40),(31,'m',1),(31,'n',1),(31,'o',1),(31,'p',1),(31,'q',1),(31,'r',1),(31,'s',1),(31,'t',1),(31,'u',1),(31,'v',1),(31,'w',1),(31,'x',1),(31,'y',1),(31,'z',1),(31,'0',1),(31,'1',1),(31,'2',1),(31,'3',1),(31,'4',1),(31,'5',1),(31,'6',1),(31,'7',1),(31,'8',1),(31,'9',1),(31,'_',1),
    (32,'a',1),(32,'b',1),(32,'c',1),(32,'d',1),(32,'e',1),(32,'f',1),(32,'g',1),(32,'h',1),(32,'i',1),(32,'j',1),(32,'k',1),(32,'l',1),(32,'m',1),(32,'n',1),(32,'o',1),(32,'p',1),(32,'q',1),(32,'r',1),(32,'s',1),(32,'t',1),(32,'u',41),(32,'v',1),(32,'w',1),(32,'x',1),(32,'y',1),(32,'z',1),(32,'0',1),(32,'1',1),(32,'2',1),(32,'3',1),(32,'4',1),(32,'5',1),(32,'6',1),(32,'7',1),(32,'8',1),(32,'9',1),(32,'_',1),
    (33,'a',1),(33,'b',1),(33,'c',1),(33,'d',1),(33,'e',1),(33,'f',1),(33,'g',1),(33,'h',1),(33,'i',1),(33,'j',1),(33,'k',1),(33,'l',1),(33,'m',1),(33,'n',1),(33,'o',1),(33,'p',1),(33,'q',1),(33,'r',1),(33,'s',1),(33,'t',42),(33,'u',1),(33,'v',1),(33,'w',1),(33,'x',1),(33,'y',1),(33,'z',1),(33,'0',1),(33,'1',1),(33,'2',1),(33,'3',1),(33,'4',1),(33,'5',1),(33,'6',1),(33,'7',1),(33,'8',1),(33,'9',1),(33,'_',1),
    (34,'a',1),(34,'b',43),(34,'c',1),(34,'d',1),(34,'e',1),(34,'f',1),(34,'g',1),(34,'h',1),(34,'i',1),(34,'j',1),(34,'k',1),(34,'l',1),(34,'m',1),(34,'n',1),(34,'o',1),(34,'p',1),(34,'q',1),(34,'r',1),(34,'s',1),(34,'t',1),(34,'u',1),(34,'v',1),(34,'w',1),(34,'x',1),(34,'y',1),(34,'z',1),(34,'0',1),(34,'1',1),(34,'2',1),(34,'3',1),(34,'4',1),(34,'5',1),(34,'6',1),(34,'7',1),(34,'8',1),(34,'9',1),(34,'_',1),
    (35,'a',1),(35,'b',1),(35,'c',1),(35,'d',1),(35,'e',1),(35,'f',1),(35,'g',1),(35,'h',1),(35,'i',1),(35,'j',1),(35,'k',1),(35,'l',1),(35,'m',1),(35,'n',1),(35,'o',1),(35,'p',1),(35,'q',1),(35,'r',1),(35,'s',1),(35,'t',1),(35,'u',1),(35,'v',1),(35,'w',1),(35,'x',1),(35,'y',1),(35,'z',1),(35,'0',1),(35,'1',1),(35,'2',1),(35,'3',1),(35,'4',1),(35,'5',1),(35,'6',1),(35,'7',1),(35,'8',1),(35,'9',1),(35,'_',1),
    (36,'a',1),(36,'b',1),(36,'c',1),(36,'d',1),(36,'e',1),(36,'f',1),(36,'g',1),(36,'h',1),(36,'i',1),(36,'j',1),(36,'k',1),(36,'l',1),(36,'m',1),(36,'n',1),(36,'o',1),(36,'p',1),(36,'q',1),(36,'r',1),(36,'s',1),(36,'t',1),(36,'u',1),(36,'v',1),(36,'w',1),(36,'x',1),(36,'y',1),(36,'z',1),(36,'0',1),(36,'1',1),(36,'2',1),(36,'3',1),(36,'4',1),(36,'5',1),(36,'6',1),(36,'7',1),(36,'8',1),(36,'9',1),(36,'_',1),
    (37,'a',1),(37,'b',1),(37,'c',1),(37,'d',1),(37,'e',1),(37,'f',1),(37,'g',1),(37,'h',1),(37,'i',1),(37,'j',1),(37,'k',1),(37,'l',1),(37,'m',1),(37,'n',1),(37,'o',1),(37,'p',1),(37,'q',1),(37,'r',44),(37,'s',1),(37,'t',1),(37,'u',1),(37,'v',1),(37,'w',1),(37,'x',1),(37,'y',1),(37,'z',1),(37,'0',1),(37,'1',1),(37,'2',1),(37,'3',1),(37,'4',1),(37,'5',1),(37,'6',1),(37,'7',1),(37,'8',1),(37,'9',1),(37,'_',1),
    (38,'a',1),(38,'b',1),(38,'c',1),(38,'d',1),(38,'e',1),(38,'f',1),(38,'g',1),(38,'h',1),(38,'i',1),(38,'j',1),(38,'k',1),(38,'l',1),(38,'m',1),(38,'n',1),(38,'o',1),(38,'p',1),(38,'q',1),(38,'r',1),(38,'s',1),(38,'t',1),(38,'u',1),(38,'v',1),(38,'w',1),(38,'x',1),(38,'y',1),(38,'z',1),(38,'0',1),(38,'1',1),(38,'2',1),(38,'3',1),(38,'4',1),(38,'5',1),(38,'6',1),(38,'7',1),(38,'8',1),(38,'9',1),(38,'_',1),
    (39,'a',1),(39,'b',1),(39,'c',45),(39,'d',1),(39,'e',1),(39,'f',1),(39,'g',1),(39,'h',1),(39,'i',1),(39,'j',1),(39,'k',1),(39,'l',1),(39,'m',1),(39,'n',1),(39,'o',1),(39,'p',1),(39,'q',1),(39,'r',1),(39,'s',1),(39,'t',1),(39,'u',1),(39,'v',1),(39,'w',1),(39,'x',1),(39,'y',1),(39,'z',1),(39,'0',1),(39,'1',1),(39,'2',1),(39,'3',1),(39,'4',1),(39,'5',1),(39,'6',1),(39,'7',1),(39,'8',1),(39,'9',1),(39,'_',1),
    (40,'a',1),(40,'b',1),(40,'c',1),(40,'d',1),(40,'e',46),(40,'f',1),(40,'g',1),(40,'h',1),(40,'i',1),(40,'j',1),(40,'k',1),(40,'l',1),(40,'m',1),(40,'n',1),(40,'o',1),(40,'p',1),(40,'q',1),(40,'r',1),(40,'s',1),(40,'t',1),(40,'u',1),(40,'v',1),(40,'w',1),(40,'x',1),(40,'y',1),(40,'z',1),(40,'0',1),(40,'1',1),(40,'2',1),(40,'3',1),(40,'4',1),(40,'5',1),(40,'6',1),(40,'7',1),(40,'8',1),(40,'9',1),(40,'_',1),
    (41,'a',1),(41,'b',1),(41,'c',1),(41,'d',1),(41,'e',47),(41,'f',1),(41,'g',1),(41,'h',1),(41,'i',1),(41,'j',1),(41,'k',1),(41,'l',1),(41,'m',1),(41,'n',1),(41,'o',1),(41,'p',1),(41,'q',1),(41,'r',1),(41,'s',1),(41,'t',1),(41,'u',1),(41,'v',1),(41,'w',1),(41,'x',1),(41,'y',1),(41,'z',1),(41,'0',1),(41,'1',1),(41,'2',1),(41,'3',1),(41,'4',1),(41,'5',1),(41,'6',1),(41,'7',1),(41,'8',1),(41,'9',1),(41,'_',1),
    (42,'a',1),(42,'b',1),(42,'c',1),(42,'d',1),(42,'e',48),(42,'f',1),(42,'g',1),(42,'h',1),(42,'i',1),(42,'j',1),(42,'k',1),(42,'l',1),(42,'m',1),(42,'n',1),(42,'o',1),(42,'p',1),(42,'q',1),(42,'r',1),(42,'s',1),(42,'t',1),(42,'u',1),(42,'v',1),(42,'w',1),(42,'x',1),(42,'y',1),(42,'z',1),(42,'0',1),(42,'1',1),(42,'2',1),(42,'3',1),(42,'4',1),(42,'5',1),(42,'6',1),(42,'7',1),(42,'8',1),(42,'9',1),(42,'_',1),
    (43,'a',49),(43,'b',1),(43,'c',1),(43,'d',1),(43,'e',1),(43,'f',1),(43,'g',1),(43,'h',1),(43,'i',1),(43,'j',1),(43,'k',1),(43,'l',1),(43,'m',1),(43,'n',1),(43,'o',1),(43,'p',1),(43,'q',1),(43,'r',1),(43,'s',1),(43,'t',1),(43,'u',1),(43,'v',1),(43,'w',1),(43,'x',1),(43,'y',1),(43,'z',1),(43,'0',1),(43,'1',1),(43,'2',1),(43,'3',1),(43,'4',1),(43,'5',1),(43,'6',1),(43,'7',1),(43,'8',1),(43,'9',1),(43,'_',1),
    (44,'a',1),(44,'b',1),(44,'c',1),(44,'d',1),(44,'e',1),(44,'f',1),(44,'g',1),(44,'h',1),(44,'i',1),(44,'j',1),(44,'k',1),(44,'l',1),(44,'m',1),(44,'n',1),(44,'o',1),(44,'p',1),(44,'q',1),(44,'r',1),(44,'s',1),(44,'t',50),(44,'u',1),(44,'v',1),(44,'w',1),(44,'x',1),(44,'y',1),(44,'z',1),(44,'0',1),(44,'1',1),(44,'2',1),(44,'3',1),(44,'4',1),(44,'5',1),(44,'6',1),(44,'7',1),(44,'8',1),(44,'9',1),(44,'_',1),
    (45,'a',1),(45,'b',1),(45,'c',1),(45,'d',1),(45,'e',1),(45,'f',1),(45,'g',1),(45,'h',1),(45,'i',1),(45,'j',1),(45,'k',1),(45,'l',1),(45,'m',1),(45,'n',1),(45,'o',1),(45,'p',1),(45,'q',1),(45,'r',1),(45,'s',1),(45,'t',51),(45,'u',1),(45,'v',1),(45,'w',1),(45,'x',1),(45,'y',1),(45,'z',1),(45,'0',1),(45,'1',1),(45,'2',1),(45,'3',1),(45,'4',1),(45,'5',1),(45,'6',1),(45,'7',1),(45,'8',1),(45,'9',1),(45,'_',1),
    (46,'a',1),(46,'b',1),(46,'c',1),(46,'d',1),(46,'e',1),(46,'f',1),(46,'g',1),(46,'h',1),(46,'i',1),(46,'j',1),(46,'k',1),(46,'l',1),(46,'m',1),(46,'n',1),(46,'o',1),(46,'p',1),(46,'q',1),(46,'r',1),(46,'s',1),(46,'t',1),(46,'u',1),(46,'v',1),(46,'w',1),(46,'x',1),(46,'y',1),(46,'z',1),(46,'0',1),(46,'1',1),(46,'2',1),(46,'3',1),(46,'4',1),(46,'5',1),(46,'6',1),(46,'7',1),(46,'8',1),(46,'9',1),(46,'_',1),
    (47,'a',1),(47,'b',1),(47,'c',1),(47,'d',1),(47,'e',1),(47,'f',1),(47,'g',1),(47,'h',1),(47,'i',1),(47,'j',1),(47,'k',1),(47,'l',1),(47,'m',1),(47,'n',1),(47,'o',1),(47,'p',1),(47,'q',1),(47,'r',1),(47,'s',52),(47,'t',1),(47,'u',1),(47,'v',1),(47,'w',1),(47,'x',1),(47,'y',1),(47,'z',1),(47,'0',1),(47,'1',1),(47,'2',1),(47,'3',1),(47,'4',1),(47,'5',1),(47,'6',1),(47,'7',1),(47,'8',1),(47,'9',1),(47,'_',1),
    (48,'a',1),(48,'b',1),(48,'c',1),(48,'d',1),(48,'e',1),(48,'f',1),(48,'g',1),(48,'h',1),(48,'i',1),(48,'j',1),(48,'k',1),(48,'l',1),(48,'m',1),(48,'n',1),(48,'o',1),(48,'p',1),(48,'q',1),(48,'r',1),(48,'s',1),(48,'t',1),(48,'u',1),(48,'v',1),(48,'w',1),(48,'x',1),(48,'y',1),(48,'z',1),(48,'0',1),(48,'1',1),(48,'2',1),(48,'3',1),(48,'4',1),(48,'5',1),(48,'6',1),(48,'7',1),(48,'8',1),(48,'9',1),(48,'_',1),
    (49,'a',1),(49,'b',1),(49,'c',1),(49,'d',1),(49,'e',1),(49,'f',1),(49,'g',1),(49,'h',1),(49,'i',1),(49,'j',1),(49,'k',1),(49,'l',1),(49,'m',1),(49,'n',1),(49,'o',1),(49,'p',1),(49,'q',1),(49,'r',1),(49,'s',53),(49,'t',1),(49,'u',1),(49,'v',1),(49,'w',1),(49,'x',1),(49,'y',1),(49,'z',1),(49,'0',1),(49,'1',1),(49,'2',1),(49,'3',1),(49,'4',1),(49,'5',1),(49,'6',1),(49,'7',1),(49,'8',1),(49,'9',1),(49,'_',1),
    (50,'a',1),(50,'b',1),(50,'c',1),(50,'d',1),(50,'e',1),(50,'f',1),(50,'g',1),(50,'h',1),(50,'i',1),(50,'j',1),(50,'k',1),(50,'l',1),(50,'m',1),(50,'n',1),(50,'o',1),(50,'p',1),(50,'q',1),(50,'r',1),(50,'s',1),(50,'t',1),(50,'u',1),(50,'v',1),(50,'w',1),(50,'x',1),(50,'y',1),(50,'z',1),(50,'0',1),(50,'1',1),(50,'2',1),(50,'3',1),(50,'4',1),(50,'5',1),(50,'6',1),(50,'7',1),(50,'8',1),(50,'9',1),(50,'_',1),
    (51,'a',1),(51,'b',1),(51,'c',1),(51,'d',1),(51,'e',1),(51,'f',1),(51,'g',1),(51,'h',1),(51,'i',1),(51,'j',1),(51,'k',1),(51,'l',1),(51,'m',1),(51,'n',1),(51,'o',1),(51,'p',1),(51,'q',1),(51,'r',1),(51,'s',1),(51,'t',1),(51,'u',1),(51,'v',1),(51,'w',1),(51,'x',1),(51,'y',1),(51,'z',1),(51,'0',1),(51,'1',1),(51,'2',1),(51,'3',1),(51,'4',1),(51,'5',1),(51,'6',1),(51,'7',1),(51,'8',1),(51,'9',1),(51,'_',1),
    (52,'a',1),(52,'b',1),(52,'c',1),(52,'d',1),(52,'e',1),(52,'f',1),(52,'g',1),(52,'h',1),(52,'i',1),(52,'j',1),(52,'k',1),(52,'l',1),(52,'m',1),(52,'n',1),(52,'o',1),(52,'p',1),(52,'q',1),(52,'r',1),(52,'s',1),(52,'t',1),(52,'u',1),(52,'v',1),(52,'w',1),(52,'x',1),(52,'y',1),(52,'z',1),(52,'0',1),(52,'1',1),(52,'2',1),(52,'3',1),(52,'4',1),(52,'5',1),(52,'6',1),(52,'7',1),(52,'8',1),(52,'9',1),(52,'_',1),
    (53,'a',1),(53,'b',1),(53,'c',1),(53,'d',1),(53,'e',54),(53,'f',1),(53,'g',1),(53,'h',1),(53,'i',1),(53,'j',1),(53,'k',1),(53,'l',1),(53,'m',1),(53,'n',1),(53,'o',1),(53,'p',1),(53,'q',1),(53,'r',1),(53,'s',1),(53,'t',1),(53,'u',1),(53,'v',1),(53,'w',1),(53,'x',1),(53,'y',1),(53,'z',1),(53,'0',1),(53,'1',1),(53,'2',1),(53,'3',1),(53,'4',1),(53,'5',1),(53,'6',1),(53,'7',1),(53,'8',1),(53,'9',1),(53,'_',1),
    (54,'a',1),(54,'b',1),(54,'c',1),(54,'d',1),(54,'e',1),(54,'f',1),(54,'g',1),(54,'h',1),(54,'i',1),(54,'j',1),(54,'k',1),(54,'l',1),(54,'m',1),(54,'n',1),(54,'o',1),(54,'p',1),(54,'q',1),(54,'r',1),(54,'s',1),(54,'t',1),(54,'u',1),(54,'v',1),(54,'w',1),(54,'x',1),(54,'y',1),(54,'z',1),(54,'0',1),(54,'1',1),(54,'2',1),(54,'3',1),(54,'4',1),(54,'5',1),(54,'6',1),(54,'7',1),(54,'8',1),(54,'9',1),(54,'_',1),
]

#Procura o proximo estado
def next_state(state,char): #Estado e caracter da fita atuais
    #Percorre procurando uma regra de transição correspondente
    for t in transition:
        if t[0] == state and t[1] == char:
            #Retorna o proximo estado
            return t[2]
    #Retorna erro se nao encontrar uma transicao
    return error_state

#Passa pelo arquivo de entrada verificando cada caracter
def start(_in,_out,list_t,list_e): #Acesso aos arquivos de input e output
    #Contadores de Linha e Token
    line = 1
    token_num = 0
    #Cadeia atual sendo analizada
    token_str = ''
    #Estado inicial
    state = start_state

    while 1:
        #Procura proxima caracter
        char = _in.read(1).lower()
        #Se separador, salva e recomeça
        if char in separator:
            if state in final_state:
                #add 1 no contador de token
                token_num += 1
                #add caracter ao arquivo de saida
                _out.write(output_symbol[final_state.index(state)])
                #add cadeia, linha e numToken a lista de tokens
                list_t.append((token_num, line, token_str, output_symbol[final_state.index(state)]))
                #Se o stado final é erro, add a lista de erros
                if state == error_state:
                    #print(f"Erro! Linha:{line}, Token:{token_num}")
                    list_e.append((token_num, line, token_str, 'L'))
                #Reseta a cadeia atual
                token_str = ''
            #Se é pra ignorar não salva
            if char not in ignore:
                #add 1 no contador de token
                token_num += 1
                #add caracter ao arquivo de saida
                _out.write(char)
                #add caracter, linha e numToken a lista de tokens
                list_t.append((token_num, line, char, 'P'))
            #Se é '\n', linha+1
            if char == '\n':
                line += 1
                token_num = 0
            #Se final de sentença morre
            if char == '$':
                break
            state = start_state
            continue
        #Procura o proximo estado
        state = next_state(state,char)
        #Adiciona a caracter atual no final da cadeia atual
        token_str += char
    #Escreve todos os erros no arquivo de saida
    for i in list_e:
        _out.write(f'\n - Erro lexico! Linha:{i[1]}, Token:"{i[2]}"\n')