# use dynamic programming



class sum_dice:

    def __init__(self):
        self.series = []
        self.dice_pool = []

    def mult(self, mult, n = 1):
        # n = how many more dice beyond the self.series calculation
        # so 6d6 would have n = 5 since the first die is self.series
        x = mult
        for i in range(0, n):
            product = []
            for term in x:
                for pterm in self.series:
                    # multinomial expansion
                    product.append([term[0] * pterm[0], term[1] + pterm[1]])
            self.series = product
            self.combine()
        

    def combine(self):
        combination = []
        # sort by deg
        self.series.sort(key = lambda x: x[1])
        first = self.series[0][1] # lowest deg
        coef = 0
        for term in self.series:
            if term[1] == first:
                # add term coef if same deg
                coef += term[0]
            elif term[1] != first:
                # if next deg is found
                # add combined coef with its deg
                combination.append([coef, first])
                # get that coef
                coef = term[0]
                # get that next deg
                first = term[1]
        # missing the last term? oh well it's fixed now.
        combination.append([coef, first])
        self.series = combination

    def chance(self, n = 4):
        total = sum(x[0] for x in self.series)
        for coef in self.series:
            # look at this backaswwardness for precision
            precision = "{:."+ str(n) + "%}"
            print(str(coef[1]) + " : " + precision.format(coef[0]/total))

    def make_die(self, sides = 6):
        die = []
        for i in range(1, sides+1):
            die.append([1,i])
        return die
