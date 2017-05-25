#coding:utf-8

'python unittest 测试用例'

__author__='linguanghui'

import unittest
from  mydict import Dict

class TestDict( unittest.TestCase):

    def setUp( self ):
        print( 'start test .......' )
    #测试类的初始化
    def test_init( self ):
        d = Dict( a=1, b='test' )
        self.assertEqual( d.a, 1 )
        self.assertEqual( d.b, 'test' )
        self.assertTrue( isinstance( d, dict) )
    #测试key
    def test_key( self ):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual( d.key, 'value' )

    def test_attr( self ):
        d = Dict()
        d.key = 'value'
        self.assertTrue( 'key' in d )
        self.assertEqual( d['key'], 'value' )

    def test_keyerror( self ):
        d = Dict()

        with self.assertRaises( KeyError ):
            value = d['empty']

    def test_attrerror( self ):
        d = Dict()

        with self.assertRaises( AttributeError ):

            value = d.empty

    def tearDown( self ):
        print( 'testing over ......' )

