# -*- encoding: utf-8 -*-
import unittest

import pilasengine


class TestCamara(unittest.TestCase):

    def setUp(self):
        self.pilas = pilasengine.iniciar()
        

    def testSeLlamaAPylint(self):
        import ipdb ; ipdb.set_trace()

    def testPuedeVibrar(self):
        self.pilas.camara.vibrar()


if __name__ == '__main__':
    unittest.main()