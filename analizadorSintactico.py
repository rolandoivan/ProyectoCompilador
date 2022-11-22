import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin
#from analisadorSemantico import *
from codigoIntermedio import *

precedence = (
    ('right','ASSIGN'),
    ('left','EQUALS','NOT_EQUALS'),
    ('left','GT','LT','GTE','LTE'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('left','LPARENTHESIS','RPARENTHESIS')
)

# ------------------ BLOQUES ------------------

def p_program(p):
    '''program : def_vars functions MAIN block'''
    p[0] = program(p[1],p[2],p[4])

def p_functions(p):
    '''functions : DEF type_fun ID LPARENTHESIS param RPARENTHESIS block functions'''
    p[0] = functions(p[2],Id(p[3]),p[5],p[7],p[8])

def p_functionsEmpty(p):
    '''functions : empty'''
    p[0] = Null()

def p_param1(p):
    '''param : type ID COMMA param'''
    p[0] = param1(p[1],Id(p[2]),p[4])

def p_param2(p):
    '''param : type ID'''
    p[0] = param2(p[1],Id(p[2]))

def p_paramEmpty(p):
    '''param : empty'''
    p[0] = Null()

def p_block(p):
    '''block : LCURLY_BRACKET content_block RCURLY_BRACKET'''
    p[0] = block(p[2])

def p_content_block(p):
    '''content_block : statment content_block'''
    p[0] = content_block(p[1],p[2])

def p_content_blockEmprty(p):
    '''content_block :  empty'''
    p[0] = Null()

# ---------------------------- STATMENTS ----------------------------

def p_statment1(p):
    '''statment : def_vars'''
    p[0] = statment1(p[1])

def p_statment2(p):
    '''statment :  assignment SEMICOLON'''
    p[0] = statment2(p[1])

def p_statment3(p):
    '''statment : condition'''
    p[0] = statment3(p[1])

def p_statment4(p):
    '''statment : while_loop'''
    p[0] = statment4(p[1])

def p_statment5(p):
    '''statment : for_loop'''
    p[0] = statment5(p[1])

def p_statment6(p):
    '''statment : function_call SEMICOLON'''
    p[0] = statment6(p[1])

def p_statment7(p):
    '''statment : write_function'''
    p[0] = statment7(p[1])

def p_statment8(p):
    '''statment : RETURN expression SEMICOLON'''
    p[0] = statment8(p[2])

def p_statment9(p):
    '''statment : RETURN SEMICOLON'''
    p[0] = statment9()

def p_statment10(p):
    '''statment : read_function'''
    p[0] = statment10(p[1])

# --------------------------- DEF_VARS ---------------------------

def p_def_vars(p):
    '''def_vars : VAR type vars_n SEMICOLON def_vars'''
    p[0] = def_vars(p[2],p[3],p[5])

def p_def_varsEmpty(p):
    '''def_vars : empty'''
    p[0] = Null()

def p_vars_n1(p):
    '''vars_n : ID COMMA vars_n'''
    p[0] = vars_n1(Id(p[1]),p[3])

def p_vars_n2(p):
    '''vars_n : ID'''
    p[0] = vars_n2(Id(p[1]))

def p_vars_n3(p):
    '''vars_n : ID LSQUARE_BRACKET CONST_INT RSQUARE_BRACKET'''
    p[0] = vars_n3(Id(p[1]),Const_int(p[3]))

def p_vars_n4(p):
    '''vars_n : ID LSQUARE_BRACKET CONST_INT RSQUARE_BRACKET LSQUARE_BRACKET CONST_INT RSQUARE_BRACKET'''
    p[0] = vars_n4(Id(p[1]),Const_int(p[3]),Const_int(p[6]))

# ---------------------------

def p_assignment(p):
    '''assignment : var ASSIGN expression'''
    p[0] = assignment(p[1],Assign(p[2]),p[3])

# --------------------------- CONDITION ---------------------------

def p_condition(p):
    '''condition : IF LPARENTHESIS expression RPARENTHESIS block condition_else'''
    p[0] = condition(p[3],p[5],p[6])

def p_condition_else1(p):
    '''condition_else : ELIF LPARENTHESIS expression RPARENTHESIS block condition_else'''
    p[0] = condition_else1(p[3],p[5],p[6])

def p_condition_else2(p):
    '''condition_else : ELSE block'''
    p[0] = condition_else2(p[2])

def p_condition_elseEmpty(p):
    '''condition_else : empty'''
    p[0] = Null()

# --------------------------- WHILE LOOP ---------------------------

def p_while_loop(p):
    '''while_loop : WHILE LPARENTHESIS expression RPARENTHESIS block'''
    p[0] = while_loop(p[3],p[5])

def p_do_while_loop(p):
    '''while_loop : DO block WHILE LPARENTHESIS expression RPARENTHESIS SEMICOLON'''
    p[0] = do_while_loop(p[2],p[5])


# --------------------------- FOR LOOP ---------------------------

def p_for_loop(p):
    '''for_loop : FOR LPARENTHESIS for_param1 for_param2 for_param3 RPARENTHESIS block'''
    p[0] = for_loop(p[3],p[4],p[5],p[7])

def p_for_param1(p):
    '''for_param1 : assignment SEMICOLON'''
    p[0] = for_param1(p[1])

def p_for_param2(p):
    '''for_param2 : expression SEMICOLON'''
    p[0] = for_param2(p[1])

def p_for_param3(p):
    '''for_param3 : assignment'''
    p[0] = for_param3(p[1])

# --------------------------- FUNCTION CALL ---------------------------

def p_function_call(p):
    '''function_call : ID LPARENTHESIS fun_param RPARENTHESIS'''
    p[0] = function_call(Id(p[1]),p[3])

def p_fun_param1(p):
    '''fun_param : expression COMMA fun_param'''
    p[0] = fun_param1(p[1],p[3])

def p_fun_param2(p):
    '''fun_param : expression'''
    p[0] = fun_param2(p[1])

# --------------------------- WRITE FUNCTION ---------------------------

def p_write_function(p):
    '''write_function : PRINT LPARENTHESIS write RPARENTHESIS SEMICOLON'''
    p[0] = write_function(p[3])

def p_write1(p):
    '''write : expression COMMA write'''
    p[0] = write1(p[1],p[3])
        
def p_write2(p):
    '''write : expression'''
    p[0] = write2(p[1])

# ---------------------------- READ FUNCTION --------------------------

def p_read_function(p):
    '''read_function : READ LPARENTHESIS read RPARENTHESIS SEMICOLON'''
    p[0] = read_function(p[3])

def p_read1(p):
    '''read : expression COMMA read'''
    p[0] = read1(p[1],p[3])
        
def p_read2(p):
    '''read : expression'''
    p[0] = read2(p[1])

# ---------------------------- EXPRESSIONS ----------------------------

def p_expression1(p):
    '''expression : exp_or'''
    p[0] = expression1(p[1])

def p_expression2(p):
    '''expression : expression logical_or exp_or'''
    p[0] = expression2(p[1],p[2],p[3])

def p_exp_or1(p):
    '''exp_or : exp_and'''
    p[0] = exp_or1(p[1])

def p_exp_or2(p):
    '''exp_or : exp_or logical_and exp_and'''
    p[0] = exp_or2(p[1],p[2],p[3])

def p_exp_and1(p):
    '''exp_and : exp_not'''
    p[0] = exp_and1(p[1])

def p_exp_and2(p):
    '''exp_and : exp_and logical_not exp_not'''
    p[0] = exp_and2(p[1],p[2],p[3])

def p_exp_not1(p):
    '''exp_not : exp'''
    p[0] = exp_not1(p[1])
                
def p_exp_not2(p):
    '''exp_not : exp relational_l1 term'''
    p[0] = exp_not2(p[1],p[2],p[3])

def p_exp_not3(p):
    '''exp_not : exp relational_l2 term'''
    p[0] = exp_not3(p[1],p[2],p[3])

def p_exp1(p):
    '''exp : term''' 
    p[0] = exp1(p[1])

def p_exp2(p):
    '''exp : term arithmetic_l1 exp'''
    p[0] = exp2(p[1],p[2],p[3])

def p_term1(p):
    '''term : factor'''
    p[0] = term1(p[1])
                
def p_term2(p):
    '''term : factor arithmetic_l2 term''' 
    p[0] = term2(p[1],p[2],p[3])

def p_factor1(p):
    '''factor : LPARENTHESIS expression RPARENTHESIS'''
    p[0] = factor1(p[2])

def p_factor2(p):
    '''factor : const_var'''
    p[0] = factor2(p[1])

def p_factor3(p):
    '''factor : function_call'''
    p[0] = factor3(p[1])

def p_factor4(p):
    '''factor : var'''
    p[0] = factor4(p[1])

# ---------------------------- OPERATORS ----------------------------

def p_arithmetic_l1_1(p):
    '''arithmetic_l1 : PLUS'''
    p[0] = arithmetic_l1_1(Plus(p[1]))

def p_arithmetic_l1_2(p):
    '''arithmetic_l1 : MINUS'''
    p[0] = arithmetic_l1_2(Minus(p[1]))

def p_arithmetic_l2_1(p):
    '''arithmetic_l2 : TIMES'''
    p[0] = arithmetic_l2_1(Times(p[1]))

def p_arithmetic_l2_2(p):
    '''arithmetic_l2 : DIVIDE'''
    p[0] = arithmetic_l2_2(Divide(p[1]))

def p_relational_l1_1(p):
    '''relational_l1 : EQUALS'''
    p[0] = relational_l1_1(Equals(p[1])) 

def p_relational_l1_2(p):
    '''relational_l1 : NOT_EQUALS'''
    p[0] = relational_l1_2(Not_equals(p[1])) 

def p_relational_l2_1(p):
    '''relational_l2 : LT'''
    p[0] = relational_l2_1(Lt(p[1]))

def p_relational_l2_2(p):
    '''relational_l2 : GT'''
    p[0] = relational_l2_2(Gt(p[1]))

def p_relational_l2_3(p):
    '''relational_l2 : LTE'''
    p[0] = relational_l2_3(Lte(p[1]))

def p_relational_l2_4(p):
    '''relational_l2 : GTE'''
    p[0] = relational_l2_4(Gte(p[1])) 

def p_logical_or(p):
    '''logical_or : BOOL_OR'''
    p[0] = logical_or(Bool_or(p[1]))

def p_logical_and(p):
    '''logical_and : BOOL_AND'''
    p[0] = logical_and(Bool_and(p[1]))

def p_logical_not(p):
    '''logical_not : BOOL_NOT'''
    p[0] = logical_not(Bool_not(p[1]))

# ---------------------------- VARIABLES -------------------------------------

def p_const_var1(p):
    '''const_var : CONST_INT'''
    p[0] = const_var2(Const_int(p[1]))

def p_const_var2(p):
    '''const_var : CONST_FLOAT'''
    p[0] = const_var3(Const_float(p[1]))

def p_const_var3(p):
    '''const_var : CONST_STRING'''
    p[0] = const_var4(Const_string(p[1])) 

#def p_const_var4(p):
#    '''const_var : CONST_BOOL'''
#    p[0] = const_var4(Const_bool(p[1]))

def p_var1(p):
    '''var : ID'''
    p[0] = var1(Id(p[1]))

def p_var2(p):
    '''var : ID LSQUARE_BRACKET expression RSQUARE_BRACKET'''
    p[0] = var2(Id(p[1]),p[3])

def p_var3(p):
    '''var : ID LSQUARE_BRACKET expression RSQUARE_BRACKET LSQUARE_BRACKET expression RSQUARE_BRACKET'''
    p[0] = var3(Id(p[1]),p[3],p[6])

# ---------------------------- TYPES -------------------------------------

def p_type1(p):
    '''type : INT'''
    p[0] = type1(Int(p[1]))

def p_type2(p):
    '''type : FLOAT'''
    p[0] = type2(Float(p[1]))

def p_type3(p):
    '''type : STRING'''
    p[0] = type4(String(p[1]))

#def p_type4(p):
#    '''type : BOOL'''
#    p[0] = type3(Bool(p[1]))

def p_type_fun1(p):
    '''type_fun : type'''
    p[0] = type_fun1(p[1])

def p_type_fun2(p):
    '''type_fun : VOID'''
    p[0] = type_fun2(Void(p[1]))

# ---------------------------- ERROR -------------------------------------

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print("Error de sintaxis en linea " + str(p.lineno))