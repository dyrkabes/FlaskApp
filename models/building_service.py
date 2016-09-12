from models.buff_service import BuffService
from models import calc

class BuildingService:
    HALF_DAY = "HALF_DAY"
    SECOND = "SECOND"
    HALF_DAY_IN_SECONDS = 43200

    # Computes amount of cycles for 12 hours
    @staticmethod
    def calculate_cycles_amount(building):
        return 12 * 60 * 60 / (building.time_cycle+building.time_path)

    @staticmethod
    def calculate_income(building, level, buff, interval):
        cycles = BuildingService.calculate_cycles_amount(building)
        # If the building uses non-recurring resources like for building fields
        if building.get_limit() != 0:
            one_time_resources_multiplyer = cycles * level / building.get_limit()
        incomings = building.get_incomings()
        outcomings = building.get_outcomings()
        income = 0
        # Summing producted resources
        for outcoming in outcomings:
            income += cycles * level * outcoming.amount * outcoming.resource.cost * buff.multiplicator
        # Deducting expenses
        for incoming in incomings:
            if incoming.lasting:
                income -= cycles * level * incoming.amount * incoming.resource.cost
            # Deducting non-lasting, one time expenses
            else:
                income -= (incoming.amount
                           * incoming.resource.cost
                           * one_time_resources_multiplyer)




#TODO: GO ON COMMETNS

        # As it's measured in coins per 10k stack
        income /= 10000







        # Deducting Buff cost
        income -= BuffService.calculate_cost(buff, BuffService.HALF_DAY)
        if interval == BuildingService.HALF_DAY:
            return income
        elif interval == BuildingService.SECOND:
            return income/BuildingService.HALF_DAY_IN_SECONDS

    @staticmethod
    def calculate_update_cost(building, level):
        resources = calc.UpgradeResource.select().where(
            (calc.UpgradeResource.building == building),
             (calc.UpgradeResource.level == level)
        )
        cost = 0
        for resource in resources:
            cost += resource.resource.cost * resource.amount
        return cost / 10000
        # takes resources from the database
        # multiplies them by cost, taken from another database


    # TODO: exception if there're no lvl+1, or no record for it
    @staticmethod
    def calculate_breakeven_time(building, level, buff):
        previous_level_income = BuildingService.calculate_income(building, level, buff, BuildingService.SECOND)
        new_level_income = BuildingService.calculate_income(building, level + 1, buff, BuildingService.SECOND)
        update_cost = BuildingService.calculate_update_cost(building, level)
        income_per_second = new_level_income - previous_level_income
        # returns in hours
        return update_cost / income_per_second / 60 / 60


