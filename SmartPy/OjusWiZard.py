import smartpy as sp

class CoffeeToCode(sp.Contract):
    def __init__(self):
        self.init(code='')

    @sp.entry_point
    def to_code(self, params):
        sp.set_type(params, sp.TRecord(coffee = sp.TString))
        coffee = params.coffee
        self.data.code = sp.slice(coffee, 0, 2).open_some() + 'd' + sp.slice(coffee, 5, 1).open_some()


@sp.add_test(name = "Coffee To Code")
def test():
    scenario = sp.test_scenario()

    scenario.h1("Coffee To Code")
    ctc = CoffeeToCode()
    scenario += ctc
    ctc.to_code(coffee = 'Coffee')
