# # from models import User, initialize
# #import models
# from models import initialize
#
# #
# # models.User.get(models.User.username ** 'testy').change_password('samsung')
# # list = models.User.select()
# #
# # for elem in list:
# #     print(elem.username + ' ' + elem.password)
# #
# # # models.User.create_user(
# # #      username='Rapan',
# # #      email='rapan@black.sea',
# # #      password='samsung'
# # #      )
# # user = models.User.get(models.User.username ** 'testy')
# # models.Post.create_post(
# #     models.Post,
# #     content="MEWO",
# #     user=user
# # )
#
# #models.initialize()
#
# # hands=models.Hand.select()
# #
# # for hand in hands:
# #     print(hand.content + ' ' + hand.user.username)
# # # models.Hand.create_hand(
# # #     models.Hand,
# # #     'SHAAAA',
# # #     models.User.get(username='dyrkabes')
# # # )
# # hands = models.Hand.select().where(models.Hand.user == models.User.get(username='dyrkabes'))
# #
# #
# # for hand in hands:
# #      print(hand.content+ '' + hand.timestamp.strftime('%H-%M'))
# #
# # models.Buff.create_buff(
# #     name="Irm's treat",
# #     image="",
# #     duration=1440,
# #     ingridient_1="Fish",
# #     ingridient_2="Bread",
# #     ingridient_3="Sausages",
# #     amount_1=150,
# #     amount_2=100,
# #     amount_3=50,
# #     cost_1=25,
# #     cost_2=600,
# #     cost_3=1000,
# #     friendly=True
# # )
# #
# # models.Buff.create_buff(
# #     name="Blank",
# #     image="",
# #     duration=720,
# #     ingridient_1="Fish",
# #     ingridient_2="",
# #     ingridient_3="",
# #     amount_1=0,
# #     amount_2=0,
# #     amount_3=0,
# #     friendly=True,
# #     multiplicator=1
# # )
#
#
#
# #
# # models.Resource.create_resource(
# #     'Oak boards',
# #     200
# # )
# #
# # models.Resource.create_resource(
# #     'Gold ore',
# #     4000
# # )
# #
# #
# #
# # try:
# #     models.Buff.create_buff(
# #         name="Badge: Employee of the month",
# #         duration=360,
# #         multiplicator=3,
# #         components=[
# #             {
# #                 "amount":300,
# #                 "resource":models.Resource.get(models.Resource.name**"Oak boards")
# #             },
# #             {
# #                 "amount":300,
# #                 "resource":models.Resource.get(models.Resource.name**"Marble")
# #             },
# #             {
# #                 "amount":50,
# #                 "resource":models.Resource.get(models.Resource.name**"Gold ore")
# #             }
# #         ]
# #     )
# # except: print("Yxists")
#
#
#
#
# #
# # try:
# #     ins_and_outs=[
# #             {
# #                 "resource":models.Resource.get(models.Resource.name ** "Fish"),
# #                 "amount":1,
# #                 "output":True,
# #                 "lasting":True
# #             }
# #         ]
# #
# #     models.Building.create_building(
# #         name="Fisherman",
# #         time_cycle=180,
# #         time_path=36,
# #         ins_and_outs=ins_and_outs
# #
# #     )
# # except: print("Already exists")
# #
#
#
#
#
#
# #
# # buildings = calc.Building.select()
# #
# #
# # for building in buildings:
# #     print(building.name)
# #     #
# #     # i = building.get_ins_and_outs()
# #     # print(
# #     #     "Income with 3x buff: ", building.calculate_12h_income(4, models.Buff.get(models.Buff.name == "Badge: Employee of the month")),
# #     #     "\n",
# #     #     "Income with 2x buff: ", building.calculate_12h_income(4, models.Buff.get(models.Buff.name == "Irm's treat")),
# #     #     "\n",
# #     #     "Income with 1x buff: ", building.calculate_12h_income(4)
# #     # )
# #     # # i buff cost
# #     # print("="*20)
# #
# #
# # for buff in models.Buff.select():
# #     print(buff.name, buff.calculate_full_cost())
# #
#
# # buffs = models.Buff.select()
# #
# #
# #
# # for buff in buffs:
# #     print(buff.name, buff.ingridient_1.cost)
# #     print('-'*20)
# #
# #
# #
# # for buff in buffs:
# #     print(calculate_full_cost(buff))
# #
# # # cost of 12h cycle
# # def calculate_12h_cycle(name):
# #     buff = models.Buff.get(models.Buff.name == name)
# #     return calculate_full_cost(buff)/buff.duration*60*12
# #
# #
# #
# # for buff in buffs:
# #     print(buff.name, ' ', (calculate_12h_cycle(buff.name)), "||| friendly:", calculate_12h_cycle(buff.name)/1.5)
# #
# #
#
# #
#
# #
# #
# # buildings=models.Building.select()
# #
# # buff=models.Buff.select().get()
# # for building in buildings:
# #     print(building.name, building.income.name, calculate_12h_income(building, 4, None), calculate_12h_income(building, 4, buff))
# #
# #
# # models.TestTable.create_test_record(name="sssss")
# #
# # testies = models.TestTable.select()
# #
# # for test in testies:
# #     print(test.name, test.amount, test.amount_1)
#
#

from models import calc, blog
from models.buff_service import BuffService
from models.building_service import BuildingService


calc.initialize()
blog.initialize()



# calc.Buff.create_buff(
#     components=[
#         {"amount":0,
#          "resource":calc.Resource.get(calc.Resource.name ** "Fish")
#          }
#     ],
#     name="Blank",
#     duration=86400
# )

# print(BuffService.calculate_full_cost(calc.Buff.get(calc.Buff.name ** "Fish dish")))
# print(BuffService.calculate_full_cost(calc.Buff.get(calc.Buff.name ** "Irma's Treat")))
#
# print(BuildingService.calculate_cycles_amount(calc.Building.get(calc.Building.name ** "Hunter's Hut")))

# for building in calc.Building.select():
#     print(building.name,
#           BuildingService.calculate_income(building,
#                                            1,
#                                            calc.Buff.get(calc.Buff.name ** "Blank"),
#                                            BuildingService.HALF_DAY)
#           )




# print(BuildingService.calculate_cycles_amount(building))
# print(BuildingService.calculate_cycles_amount_with_limit(building, building.get_limit(), 10))

# print(BuildingService.calculate_12h_income(calc.Building.get(calc.Building.name ** "Hunter's Hut"),
#                                            5,
#                                            calc.Buff.get(calc.Buff.name ** "Irma's treat")))



#

# calc.Resource.create_resource("Test", 100)
# calc.Building.create_building(
#     name= "Test",
#     time_cycle= 60,
#     time_path= 0,
#     limit=720,
#     incomings=[
#         {
#             "resource": calc.Resource.get(calc.Resource.name ** "Fish"),
#             "amount": 20,
#             "lasting": False
#         }
#     ],
#     outcomings=[
#         {
#             "resource": calc.Resource.get(calc.Resource.name ** "Test"),
#             "amount": 1
#         }
#     ]
# )

