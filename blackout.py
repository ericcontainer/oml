# -----------------------------
# Auto Blackout OML - Python
# Author: SIGPB - Eric M
# Date: 06/10/2018
# Version: 0.1
# Updates: -
# ----------------------------
import re

TIMETEMPLATEDATE = """
TIMETEMPLATE "@TIMETEMPLATE"
    DESCRIPTION "@DESCRIPTION"
        TIMETMPLCONDS
            @TIMETMPLCOND
"""
TIMETMPLCONDWEEKDAY = """
            TIMETMPLCOND
                TIMECONDTYPE Match
                WEEKDAY FROM @STARTWEEK TO @ENDWEEK
            @MORETPLCOND
"""
TIMETMPLCONDDATETIME = """
            TIMETMPLCOND
                TIMECONDTYPE Match
                DATE ON @DATE
                TIME FROM @STARTTIME TO @ENDTIME
            @MORETPLCOND
"""
MSGTARGETRULE_HEAD = """
MSGTARGETRULE
    DESCRIPTION "@DESCRIPTION"
MSGTARGETRULECONDS
    @MSGTARGETRULECOND
"""
MSGTARGETRULECONDOBJECT = """
    MSGTARGETRULECOND
    APPLICATION "@APPLICATION"
    MSGGRP "@MSGGRP"
    OBJECT "@OBJECT"
    @MORERULECOND
"""
MSGTARGETRULECONDONODE = """
    MSGTARGETRULECOND
    APPLICATION "@APPLICATION"
    MSGGRP "@MSGGRP"
    NODE "@OBJECT"
    @MORERULECOND
"""
MSGTARGETRULE_BOTTOM = """
MSGOPERATIONS
    MSGOPERATION
        TIMETEMPLATE "@TIMETEMPLATE"
    LOGONLY
"""
WEEKS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
NODES = []

import pdb

class Blackout(object):

    def __init__(self, time_template):
        self.time_template = time_template
               
    def get_cond_template_week(self, description_template, startweek, endweek):
        return TIMETMPLCONDWEEKDAY.replace('@STARTWEEK', startweek)\
                .replace('@ENDWEEK', endweek)
    
    def get_cond_template_day(self, _date, starttime, endtime):
        return TIMETMPLCONDDATETIME.replace('@DATE', _date)\
                .replace('@STARTTIME', starttime)\
                .replace('@ENDTIME', endtime)

    def get_cond_rules_nodes(self, application, object_name, msggrp, nodes):
        return MSGTARGETRULECONDONODE.replace('@APPLICATION', application)\
            .replace('@OBJECT', object_name)\
            .replace('@MSGGRP', msggrp)\
            .replace('@NODE', str(nodes))

    def get_cond_rules_object(self, application, msggrp, object_name):
        return MSGTARGETRULECONDOBJECT.replace('@APPLICATION', application)\
            .replace('@MSGGRP', msggrp)\
            .replace('@OBJECT', object_name)

    def get_header_time_template(self, description_template, time_template_cond):
        return TIMETEMPLATEDATE.replace('@TIMETEMPLATE', self.time_template)\
            .replace('@DESCRIPTION', description_template)\
            .replace('@TIMETMPLCOND', time_template_cond)
    
    def get_header_rule(self, description_rule, rule):
        return MSGTARGETRULE_HEAD.replace('@DESCRIPTION', description_rule)\
            .replace('@MSGTARGETRULECOND', rule)

    def get_bottom_rule(self):
        return MSGTARGETRULE_BOTTOM.replace('@TIMETEMPLATE', self.time_template)
    
    def add_timetmpcond(self, template, template_cond):
        return template.replace('@MORETPLCOND', template_cond)
    
    def add_rule_cond(self, rule, rule_cond):
        return rule.replace('@MORERULECOND', rule_cond)

    def final_result(self, result):
        return result.replace('@MORETPLCOND','').replace('@MORERULECOND', '')



