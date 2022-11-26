from more_itertools import random_combination_with_replacement
import ply.lex as lex
import re
import codecs
import os
import sys

reserved = {
    'if'      : 'IF',
    #'elif'    : 'ELIF',
    'else'    : 'ELSE',
    'return'  : 'RETURN',
    'for'     : 'FOR',
    'do'      : 'DO',
    'while'   : 'WHILE',
    'void'    : 'VOID',
    'main'    : 'MAIN',
    'def'     : 'DEF',
    'var'     : 'VAR',
    'print'   : 'PRINT',
    'read'    : 'READ',
    'bool'    : 'BOOL',
    'string'  : 'STRING',
    'float'   : 'FLOAT',
    'int'     : 'INT'
    
}

tokens = ['ID','CONST_INT','CONST_FLOAT','CONST_STRING',
        'EQUALS', 'NOT_EQUALS', 'GT', 'LT', 'GTE', 'LTE',
        'BOOL_OR', 'BOOL_AND', 'BOOL_NOT',
        'PLUS', 'MINUS', 'DIVIDE', 'TIMES', 'ASSIGN',
        'LPARENTHESIS', 'RPARENTHESIS',
        'LCURLY_BRACKET','RCURLY_BRACKET',
        'LSQUARE_BRACKET','RSQUARE_BRACKET',
        'COMMA', 'SEMICOLON'
] + list(reserved.values())

t_ignore = '\t'
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_GT = r'>'
t_LT = r'<'
t_GTE = r'>='
t_LTE = r'<='
t_BOOL_OR = r'\|\|'
t_BOOL_AND = r'&&'
t_BOOL_NOT = r'!'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'/'
t_TIMES = r'\*'
t_ASSIGN = r'='
t_LPARENTHESIS = r'\('
t_RPARENTHESIS = r'\)'
t_LCURLY_BRACKET = r'\{'
t_RCURLY_BRACKET = r'\}'
t_LSQUARE_BRACKET = r'\['
t_RSQUARE_BRACKET = r'\]'
t_COMMA = r','
t_SEMICOLON = r';'
#t_DOT = r'\.'

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_space(t):
    r'[ \f\r\t\v]+'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'
    pass

def t_CONST_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_CONST_INT(t):
    r'[0-9]+'
    t.value = int(t.value)  
    return t

def t_CONST_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t

def t_error(t):
    print("caracter no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

analizador = lex.lex()

