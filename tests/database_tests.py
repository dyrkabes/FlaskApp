import unittest

import peewee
import sqlite3

from models import calc


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        pass

    def test_note(self):
        self.assertEqual(
            calc.Building.get(calc.Building.name=="Test_lasting").note,
            "Note is here"
        )

    def test_cost_change(self):
        calc.Resource.get(calc.Resource.name=="Test_3").set_cost(129)
        print(calc.Resource.get(calc.Resource.name=="Test_3").cost)
        self.assertEqual(
            calc.Resource.get(calc.Resource.name=="Test_3").cost,
            129
        )

    def test_resource_creation(self):
        with calc.DATABASE.transaction():
            calc.Resource.create_resource(
                "Temporary_test_resource",
                555
            )
            self.assertEqual(
                calc.Resource.get(
                    calc.Resource.name=="Temporary_test_resource"
                ).cost,
                555
            )

            # Wow that test is disgusting
            self.assertTrue(
                type(calc.Resource.get(calc.Resource.name=="Temporary_test_resource")) is type(calc.Resource.get())
            )

            with self.assertRaises(peewee.IntegrityError):
                calc.Resource.create_resource(
                    "Temporary_test_resource",
                    555
                )


            calc.DATABASE.rollback()

