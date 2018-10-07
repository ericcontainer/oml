from blackout import Blackout
a = Blackout('meu_time_template')
f = a.get_header_time_template('minha template', a.get_cond_template_week('template week', 'Monday', 'Saturday'))
d = a.add_timetmpcond(f, a.get_cond_template_day('10/07/2018','00:00','01:00'))
l = a.add_timetmpcond(d, a.get_cond_template_day('10/07/2018','00:00', '02:00'))
k = a.get_header_rule('Minha regra', a.get_cond_rules_nodes('Agente', 'Opsware Agent','Operation System','DFCDSRVV0001'))

print(a.final_result(l + k + a.get_bottom_rule()).replace('\n\n','\n'))


#print(a.get_cond_template_week('default','desc_templates', 'Saturday', 'Monday'))
#print(a.get_cond_rules_object('description_rule', 'application', 'msggrp', 'object_name'))