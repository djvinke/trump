# -*- coding: utf-8 -*-

from trump.orm import SymbolManager
from trump.templating import fQuandl
from datetime import datetime as dt

sm = SymbolManager()

oil = sm.create(name = "oil_front_month",
                description = "Crude Oil Futures, Continuous Contract #2 (CL2) (Front Month)",
                freq = 'D',
                units = '$ / barrel')

oil.addAlias("OILA")
oil.addTags(['commodity','oil'])

f = fQuandl(r"CHRIS/CME_CL2",fieldname='Settle')

oil.addFeed(f)
oil.addFeed(f)

oil.addOverride(dt(2015,1,6),50.0,user='Jeffor')
oil.addFailSafe(dt(2015,1,6),45.0,user='Jefffs')

oil.cache()

print oil.df.tail()
            