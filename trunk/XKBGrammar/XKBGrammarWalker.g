// XKB Grammar (X.org)
// Written by Simos Xenitellis <simos.lists@googlemail.com>, 2008.
// Version 0.8

tree grammar XKBGrammarWalker;

options
{
        language = Python;
        tokenVocab = XKBGrammar;
        ASTLabelType = CommonTree;
}

layout 		
	: ^(LAYOUT symbols+)
	;
	
symbols 
	: ^(SYMBOLS mapType ^(MAPMATERIAL mapMaterial+))
 	;

mapType
	: ^(MAPTYPE ^(MAPOPTIONS MAPOPTIONS*) ^(MAPNAME DQSTRING))
	;

mapMaterial 
	: ^(TOKEN_INCLUDE DQSTRING)
	| ^(TOKEN_NAME NAME ^(VALUE DQSTRING))
	| ^(TOKEN_KEY_TYPE NAME? ^(VALUE DQSTRING))
	| ^(TOKEN_KEY OVERRIDE? keycode keyelements+)
	| ^(TOKEN_MODIFIER_MAP STATE keycode+)
	| ^(TOKEN_VIRTUAL_MODIFIERS NAME+)
	;

keycode	
	: ^(KEYCODE NAME)
	| ^(KEYCODEX NAME)
	;

keyelements
	: ^(ELEM_KEYSYMS ^(TOKEN_TYPE NAME? DQSTRING))
	| ^(ELEM_KEYSYMGROUP NAME+)
	| ^(ELEM_VIRTUALMODS NAME)
	| ^(ELEM_ACTIONS NAME actions_setmods+)
	| ^(ELEM_OVERLAY NAME keycode)
	;

actions_setmods
	: ^(ACTIONS_SETMODS STATE* NAME*)
	;
