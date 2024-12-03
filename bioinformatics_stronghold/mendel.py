#!/usr/bin/env python3

import sys

dom = int(sys.argv[1])
het = int(sys.argv[2])
rec = int(sys.argv[3])

tot = dom + het + rec
new_dom = dom-1
new_het = het-1
new_rec = rec-1
new_tot = tot-1


# prob_1 = (dom/tot)
# prob_2 = (het/tot)*((dom/new_tot)+0.75*(new_het)/(new_tot)+0.5*(rec/new_tot))
# prob_3 = (rec/tot)*((dom/new_tot)+0.5*(new_rec/new_tot))

# prob_4 = (het/tot)*((0.25*new_het/new_tot)+(rec/new_tot))
# prob_5 = (rec/tot)*((0.5*het/new_tot)+(new_rec/new_tot))

prob_6 = (rec/tot)*(new_rec/new_tot)
prob_7 = 0.25*(het/tot)*(new_het/new_tot)
prob_8 = 0.5*(rec/tot)*(het/new_tot)
prob_9 = 0.5*(het/tot)*(rec/new_tot)


# F1_prob = prob_1 + prob_2 + prob_3
# F2_prob = 1-(prob_4 + prob_5)
F3_prob = 1-(prob_6 + prob_7 + prob_8 + prob_9)


print(F3_prob)