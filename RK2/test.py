import unittest
import main

PLs_test: list[main.PL] = [
    main.PL(1, 'Python'),
    main.PL(2, 'C++'),
    main.PL(3, 'C#'),
    main.PL(4, 'Java')
]
Syntaxes_test = [
    main.Syntax(1, 'do-while', 2, 0.5),
    main.Syntax(2, 'pointer', 2, 2.0),
    main.Syntax(3, 'interface', 3, 2.0),
    main.Syntax(4, 'for', 1, 1.5),
    main.Syntax(5, 'class', 4, 2.0)
]
PL_Syns_test = [
    main.PL_Syn(1, 1),
    main.PL_Syn(1, 4),
    main.PL_Syn(1, 5),
    main.PL_Syn(2, 1),
    main.PL_Syn(2, 2),
    main.PL_Syn(2, 4),
    main.PL_Syn(2, 5),
    main.PL_Syn(3, 1),
    main.PL_Syn(3, 3),
    main.PL_Syn(3, 4),
    main.PL_Syn(3, 5),
    main.PL_Syn(4, 1),
    main.PL_Syn(4, 4),
    main.PL_Syn(4, 5)
]


class MyTestCase(unittest.TestCase):
    request1_expected_result = [('interface', 'C#'),
                                ('do-while', 'C++'),
                                ('pointer', 'C++'),
                                ('class', 'Java'),
                                ('for', 'Python')]
    request2_expected_result = [('C++', 2.5),
                                ('C#', 2.0),
                                ('Java', 2.0),
                                ('Python', 1.5)]
    request3_expected_result = {'C++': ['do-while', 'pointer', 'for', 'class'],
                                'C#': ['do-while', 'interface', 'for', 'class']}

    def test_request1(self):
        result = main.request1(PLs_test, Syntaxes_test)
        self.assertEqual(self.request1_expected_result, result)

    def test_request2(self):
        result = main.request2(PLs_test, Syntaxes_test)
        self.assertEqual(self.request2_expected_result, result)

    def test_request3(self):
        result = main.request3(PLs_test, Syntaxes_test, PL_Syns_test)
        self.assertEqual(self.request3_expected_result, result)

if __name__ == '__main__':
    unittest.main()
