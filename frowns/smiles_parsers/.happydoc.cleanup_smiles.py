(S'77665349dabd7493c77b74acf539d676'
p1
(ihappydoclib.parseinfo.moduleinfo
ModuleInfo
p2
(dp3
S'_namespaces'
p4
((dp5
S'SilentSaveTokens'
p6
(ihappydoclib.parseinfo.classinfo
ClassInfo
p7
(dp8
g4
((dp9
(dp10
tp11
sS'_filename'
p12
S'../python/frowns/smiles_parsers/cleanup_smiles.py'
p13
sS'_docstring'
p14
S''
sS'_class_member_info'
p15
(lp16
sS'_name'
p17
g6
sS'_parent'
p18
g2
sS'_comment_info'
p19
(dp20
sS'_base_class_info'
p21
(lp22
S'Handler.SilentErrors'
p23
aS'Handler.SaveTokens'
p24
asS'_configuration_values'
p25
(dp26
sS'_class_info'
p27
g9
sS'_function_info'
p28
g10
sS'_comments'
p29
S''
sbs(dp30
S'test'
p31
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p32
(dp33
g4
((dp34
(dp35
tp36
sS'_exception_info'
p37
(dp38
sS'_parameter_names'
p39
(tsS'_parameter_info'
p40
(dp41
sg12
g13
sg14
S''
sg17
g31
sg18
g2
sg19
g20
sg25
(dp42
sg27
g34
sg28
g35
sg29
S''
sbsS'test_show'
p43
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p44
(dp45
g4
((dp46
(dp47
tp48
sg37
(dp49
sg39
(S's'
tp50
sg40
(dp51
S's'
(NNNtp52
ssg12
g13
sg14
S''
sg17
g43
sg18
g2
sg19
g20
sg25
(dp53
sg27
g46
sg28
g47
sg29
S''
sbsS'cleanup'
p54
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p55
(dp56
g4
((dp57
(dp58
tp59
sg37
(dp60
sg39
(S's'
tp61
sg40
(dp62
S's'
(NNNtp63
ssg12
g13
sg14
S''
sg17
g54
sg18
g2
sg19
g20
sg25
(dp64
sg27
g57
sg28
g58
sg29
S''
sbsS'cleanup_closure'
p65
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p66
(dp67
g4
((dp68
(dp69
tp70
sg37
(dp71
sg39
(S's'
tp72
sg40
(dp73
S's'
(NNNtp74
ssg12
g13
sg14
S''
sg17
g65
sg18
g2
sg19
g20
sg25
(dp75
sg27
g68
sg28
g69
sg29
S''
sbstp76
sS'_import_info'
p77
(ihappydoclib.parseinfo.imports
ImportInfo
p78
(dp79
S'_named_imports'
p80
(dp81
sS'_straight_imports'
p82
(lp83
S'Smiles'
p84
aS'Handler'
p85
asbsg12
g13
sg14
S'"""Turn incomplete SMILES into something more likely to be valid.\n\nDaylight does not accept SMILES which are not well formed.  Suppose\nyou are typing in a new SMILES string, like "CC(=O)[0-]".  Part way\nthrough you have terms like "CC(=" or "CC(=O)[O".  Daylight doesn\'t\nlike these, so you can\'t, for example, use the depiction code to see\nwhat the partial string looks like.\n\nThis module tries to fix up the string to something Daylight does\naccept.  In the above case, the fixed forms of the partial terms are\n"CC" and "CC(=O)[O]".\n\nIncomplete ring closures are turned into "*" atoms with atomic number\nequal to the ring closure number.  For example, "C5CC" becomes\n"C[5*]CC".\n\n\nBugs:\n\nDaylight doesn\'t accept some aromatic notations like "ccc" but will\naccept others like "cccc".  If that\'s a problem, as a workaround you\nmight try passing the string to the toolkit and if it fails convert\nall the aromatic terms to uppercase and try again.\n\n"""'
p86
sg17
S'cleanup_smiles'
p87
sg18
Nsg19
g20
sg25
(dp88
S'include_comments'
p89
I1
sS'cacheFilePrefix'
p90
S'.happydoc.'
p91
sS'useCache'
p92
I1
sS'docStringFormat'
p93
S'StructuredText'
p94
ssg27
g5
sg28
g30
sg29
S''
sbt.