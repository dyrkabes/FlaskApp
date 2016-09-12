from models import calc


class BuffService:
    FULL = "FULL"
    HALF_DAY = "CYCLE"
    SECOND = "SECOND"
    HALF_DAY_IN_SECONDS = 43200

    @staticmethod
    def calculate_cost(buff, interval):
        """
        :param buff: buff; interval: string, a set of "SECOND", "HALF_DAY", "FULL"
        :return: buff cost, integer
        """
        components = calc.Component.select().where(calc.Component.buff == buff)
        full_cost = 0
        for component in components:
            full_cost += component.amount * component.resource.cost
        full_cost = full_cost / 10000

        if interval == BuffService.FULL:
            return full_cost
        elif interval == BuffService.HALF_DAY:
            return full_cost * BuffService.HALF_DAY_IN_SECONDS / buff.duration
        elif interval == BuffService.SECOND:
            return full_cost / buff.duration

