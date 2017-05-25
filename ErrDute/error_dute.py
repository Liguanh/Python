#coding:utf8

'test Error except'
__author__='linguanghui'

import logging

class TestError( object ):

    def testNumZero( self, num1, num2 ):

        return num1 / num2

    def checkData( self, num1, num2 ):

        try:
            print( 'try.....')
            result = self.testNumZero( num1, num2 );

            print( 'test result:',  result )
        except ValueError as e:
            print( 'valueError:', e )

        except ZeroDivisionError as e:
            print( 'ZeroDivisionError:',e )
            logging.exception( e )
            raise
        else:
            print(' no error! ')

        finally:
            print( 'finally...')

        print( 'END' )

test = TestError( )

test.checkData( 10, 0 )


