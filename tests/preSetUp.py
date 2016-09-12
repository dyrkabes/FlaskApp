from models import calc

calc.initialize()

try:
    print("A")

    calc.Building.create_building(
                incomings=[
                ],
                outcomings=[
                    {
                        "resource": calc.Resource.get(calc.Resource.name ** "Wheat"),
                        "amount": 1
                    },
                ],
                time_path=44,
                time_cycle=240,
                name="Improved farm test"
            )



    # building = calc.Building.get(name = "Improved farm")
    # granite = calc.Resource.get(calc.Resource.name ** "Granite")
    # grout = calc.Resource.get(calc.Resource.name ** "Grout")
    # # calc.UpgradeResource.create_upgrade_resource(building, 5, granite, 3300)
    # calc.UpgradeResource.create_upgrade_resource(building, 5, grout, 600)

    # calc.Resource.create_resource('wheat', 200)
    # calc.Resource.create_resource('granite', 25000)
    # calc.Resource.create_resource('grout', 75000)
    #
    # calc.Building.create_building(
    #             incomings=[
    #                 {
    #                     "resource": calc.Resource.get(calc.Resource.name ** "Oak boards"),
    #                     "amount": 20,
    #                     "lasting": False
    #                 },
    #                 {
    #                     "resource": calc.Resource.get(calc.Resource.name ** "Marble"),
    #                     "amount": 5,
    #                     "lasting": False
    #                 }
    #             ],
    #             outcomings=[
    #                 {
    #                     "resource": calc.Resource.get(calc.Resource.name ** "Wheat"),
    #                     "amount": 1
    #                 },
    #             ],
    #             limit=400,
    #             time_path=44,
    #             time_cycle=240,
    #             name="Improved farm"
    #         )
    #
    #

            # calc.Resource.create_resource("Test_2", 1000)

            # -2.4 buff/level = 1
            # calc.Building.create_building(
            #     incomings=[
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test_2"),
            #             "amount": 10,
            #             "lasting": False
            #         },
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
            #             "amount": 20,
            #             "lasting": False
            #         },
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
            #             "amount": 1,
            #             "lasting": True
            #         },
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test_2"),
            #             "amount": 1,
            #             "lasting": True
            #         }
            #     ],
            #     outcomings=[
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
            #             "amount": 1
            #         },
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test_2"),
            #             "amount": 1
            #         }
            #     ],
            #     limit=360,
            #     time_path=0,
            #     time_cycle=60,
            #     name="Test_consumer"
            # )
            # calc.UpgradeResource.create_upgrade_resource(
            #     building=calc.Building.get(calc.Building.name ** "Test_lasting"),
            #     level=1,
            #     resource=calc.Resource.get(calc.Resource.name ** "),
            #     amount=100Test"
            # )
            #
            # calc.UpgradeResource.create_upgrade_resource(
            #     building=calc.Building.get(calc.Building.name ** "Test_lasting"),
            #     level=1,
            #     resource=calc.Resource.get(calc.Resource.name ** "Test_2"),
            #     amount=100
            # )


            # calc.Building.create_building(
            #     incomings=[
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
            #             "amount": 10,
            #             "lasting": False
            #         }
            #     ],
            #     outcomings=[
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
            #             "amount": 1
            #         }
            #     ],
            #     limit=360,
            #     time_path=0,
            #     time_cycle=60,
            #     name="Test_non_lasting_0_5"
            # )
            #
            # calc.Building.create_building(
            #     incomings=[
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
            #             "amount": 10,
            #             "lasting": False
            #         }
            #     ],
            #     outcomings=[
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
            #             "amount": 1
            #         }
            #     ],
            #     limit=1440,
            #     time_path=0,
            #     time_cycle=60,
            #     name="Test_non_lasting_2"
            # )
            #
            # calc.Building.create_building(
            #     incomings=[
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
            #             "amount": 1,
            #             "lasting": True
            #         }
            #     ],
            #     outcomings=[
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
            #             "amount": 2
            #         }
            #     ],
            #     limit=0,
            #     time_path=0,
            #     time_cycle=60,
            #     name="Test_lasting"
            # )
            #
            # calc.Building.create_building(
            #     incomings=[
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
            #             "amount": 1,
            #             "lasting": True
            #         },
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
            #             "amount": 10,
            #             "lasting": False
            #         }
            #     ],
            #     outcomings=[
            #         {
            #             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
            #             "amount": 2
            #         }
            #     ],
            #     limit=720,
            #     time_path=0,
            #     time_cycle=60,
            #     name="Test_lasting_and_not"
            # )
except TypeError:
            print("EEE")