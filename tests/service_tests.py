import unittest
from models.buff_service import BuffService
from models.building_service import BuildingService
from models import calc

class BuffTests(unittest.TestCase):
    def setUp(self):
        self.buff_blank = calc.Buff.get(calc.Buff.name ** "Blank")
        self.buff_test = calc.Buff.get(calc.Buff.name ** "Test")

    def test_buff_cost(self):
        self.assertEqual(BuffService.calculate_cost(self.buff_blank, BuffService.FULL), 0)
        self.assertEqual(BuffService.calculate_cost(self.buff_test, BuffService.FULL), 0.1)
        self.assertEqual(BuffService.calculate_cost(self.buff_test, BuffService.HALF_DAY), 0.05)
        self.assertAlmostEqual(
            BuffService.calculate_cost(self.buff_test, BuffService.SECOND),
            0.0000011,
            delta=0.0000001
        )

class BuildingTests(unittest.TestCase):

    # TODO: Add some Raise exception
    def setUp(self):
        self.building_non_lasting = calc.Building.get(calc.Building.name ** "Test_non_lasting")
        self.building_non_lasting_0_5 = calc.Building.get(calc.Building.name ** "Test_non_lasting_0_5")
        self.building_non_lasting_2 = calc.Building.get(calc.Building.name ** "Test_non_lasting_2")
        self.building_lasting = calc.Building.get(calc.Building.name ** "Test_lasting")
        self.building_lasting_and_not = calc.Building.get(calc.Building.name ** "Test_lasting_and_not")

        self.building_consumer = calc.Building.get(calc.Building.name ** "Test_consumer")
        self.building_improved_farm = calc.Building.get(name="Improved farm")
        self.building_improved_farm_test = calc.Building.get(name="Improved farm test")

        self.buff_blank = calc.Buff.get(calc.Buff.name ** "Blank")
        self.buff_test = calc.Buff.get(calc.Buff.name ** "Test")




    # Testing procedure, that counts amount of cycles for 12 hours of production
    def test_cycles(self):
        self.assertEqual(
            BuildingService.calculate_cycles_amount(self.building_lasting),
            360
        )
        self.assertEqual(
            BuildingService.calculate_cycles_amount(self.building_lasting_and_not),
            720
        )

    def test_lastings(self):
        self.assertEqual(
            BuildingService.calculate_income(
                self.building_lasting,
                1,
                self.buff_blank,
                BuildingService.HALF_DAY
                ),
            3.6
            )

        self.assertEqual(
            BuildingService.calculate_income(
                self.building_lasting,
                2,
                self.buff_blank,
                BuildingService.HALF_DAY
                ),
            7.2
            )

    def test_non_lasting(self):
        with self.subTest():
            self.assertEqual(
                BuildingService.calculate_income(
                    self.building_non_lasting,
                    1,
                    self.buff_blank,
                    BuildingService.HALF_DAY
                    ),
                7.1
                )
            self.assertEqual(
                BuildingService.calculate_income(
                    self.building_non_lasting_0_5,
                    1,
                    self.buff_blank,
                    BuildingService.HALF_DAY
                    ),
                7
                )

            self.assertEqual(
                BuildingService.calculate_income(
                    self.building_non_lasting_2,
                    1,
                    self.buff_blank,
                    BuildingService.HALF_DAY
                    ),
                7.15
                )


    def test_mixed(self):
        self.assertEqual(
            BuildingService.calculate_income(
                self.building_lasting_and_not,
                1,
                self.buff_blank,
                BuildingService.HALF_DAY
                ),
            7.1
            )

    # TODO: Add different types
    def test_with_level(self):
        self.assertEqual(
            BuildingService.calculate_income(
                self.building_non_lasting,
                2,
                self.buff_blank,
                BuildingService.HALF_DAY
                ),
            14.2
            )

        self.assertEqual(
            BuildingService.calculate_income(
                self.building_lasting_and_not,
                2,
                self.buff_blank,
                BuildingService.HALF_DAY
                ),
            14.2
            )

    def test_with_buff_and_level(self):
        self.assertEqual(
            BuildingService.calculate_income(
                        self.building_lasting_and_not,
                        2,
                        self.buff_test,
                        BuildingService.HALF_DAY
                        ),
            42.95
            )

        self.assertEqual(
            BuildingService.calculate_income(
                        self.building_non_lasting,
                        1,
                        self.buff_test,
                        BuildingService.HALF_DAY
                        ),
            14.25
            )

    # Tests for complicated cases with many incoming resources of different type
    def test_mult_incs_and_outs(self):
        self.assertAlmostEqual(
            BuildingService.calculate_income(
                self.building_consumer,
                2,
                self.buff_test,
                BuildingService.HALF_DAY
            ),
            153.55,
            delta=0.001
        )

        self.assertAlmostEqual(
            BuildingService.calculate_income(
                self.building_consumer,
                1,
                self.buff_blank,
                BuildingService.HALF_DAY
            ),
            -2.4,
            delta=0.001
        )

        self.assertEqual(
            BuildingService.calculate_income(
                self.building_consumer,
                1,
                self.buff_blank,
                BuildingService.HALF_DAY
            ),
            -2.4,
        )


    # Tests for computing cost of building upgrade
    def test_upgrade_cost(self):
        self.assertEqual(
            BuildingService.calculate_update_cost(
                self.building_lasting,
                level=1
            ),
            11
        )

        self.assertEqual(
            BuildingService.calculate_update_cost(
                self.building_lasting,
                level=2
            ),
            50
        )

    def test_breakeven_time(self):
        self.assertAlmostEqual(
            BuildingService.calculate_breakeven_time(
                building=self.building_lasting,
                level=1,
                buff=self.buff_blank
            ),
            36.6666,
            delta=0.1
        )


        self.assertAlmostEqual(
            BuildingService.calculate_breakeven_time(
                building=self.building_improved_farm_test,
                level=5,
                buff=self.buff_blank
            ),
            42500,
            delta=0.1
        )

        self.assertAlmostEqual(
            BuildingService.calculate_breakeven_time(
                building=self.building_improved_farm_test,
                level=5,
                buff=self.buff_test
            ),
            21250,
            delta=0.1
        )



if __name__ == "__main__":
    unittest.main()