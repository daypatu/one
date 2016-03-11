import sys
import argparse

version = "111"

def createParser ():

    parser = argparse.ArgumentParser(prog = 'my program',
            description = '''There are some optioins''',
            epilog = '''The end.''',
            add_help = False
            )
    #create a group of parameters
    parent_group = parser.add_argument_group (title='Parameters')

    #add help
    parent_group.add_argument ('--help', action='help', help='Help')
    
    #add flag
    parent_group.add_argument ('--version',
            action='version',
            help = 'Show version',
            version='%(prog)s {}'.format (version))
    
    #add string parameter
    parent_group.add_argument ('--p1',nargs='+', default=['option1'],
            help = 'String parameter',
            metavar = 'STRING')
    
    #add numerical parameter
    parent_group.add_argument ('--p2', type=int, default=1,
                help = 'Numerical parameter', metavar='N')

    #add required numerical parameter
    parent_group.add_argument ('--p3', type=int, required = True,
                help = 'Numerical parameter', metavar='N')

   
    
    return parser



if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
     
    print (namespace)

    print "You choose option1 equal to {}".format(namespace.p1)
    print "You choose option2 equal to {}".format(namespace.p2)
    print "You choose option3 equal to {}".format(namespace.p3)
    
