(S'f925907b8c53cf3af8419dfdbd2277e3'
p1
(ihappydoclib.parseinfo.moduleinfo
ModuleInfo
p2
(dp3
S'_namespaces'
p4
((dp5
(dp6
S'graph_to_connection_table'
p7
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p8
(dp9
g4
((dp10
(dp11
tp12
sS'_exception_info'
p13
(dp14
sS'_parameter_names'
p15
(S'graph'
p16
tp17
sS'_parameter_info'
p18
(dp19
g16
(NNNtp20
ssS'_filename'
p21
S'../python/frowns/extensions/vflib/NetworkGraph/GraphIO.py'
p22
sS'_docstring'
p23
S''
sS'_name'
p24
g7
sS'_parent'
p25
g2
sS'_comment_info'
p26
(dp27
sS'_configuration_values'
p28
(dp29
sS'_class_info'
p30
g10
sS'_function_info'
p31
g11
sS'_comments'
p32
S''
sbsS'read_connection_table'
p33
(ihappydoclib.parseinfo.functioninfo
FunctionInfo
p34
(dp35
g4
((dp36
(dp37
tp38
sg13
(dp39
S'AssertionError( "Too many columns for edge" )'
p40
NsS'AssertionError( "Can\'t parse header into integer values" )'
p41
NsS'AssertionError("%s is not an integer for edge %s" %( index1, line ) )'
p42
NsS'AssertionError( "Format for edge is cable node_index1 node_index2\\ngot %s" % line )'
p43
NsS'AssertionError( "Need %s nodes" % numnodes )'
p44
NsS'AssertionError("%s is not an integer for edge %s" %( index2, line ) )'
p45
NsS'AssertionError( "Header has wrong number of elements" )'
p46
NsS'AssertionError( "Need %s edges!" % numedges )'
p47
Nssg15
(S'file'
p48
tp49
sg18
(dp50
g48
(NNNtp51
ssg21
g22
sg23
S'file->graph'
p52
sg24
g33
sg25
g2
sg26
g27
sg28
(dp53
sg30
g36
sg31
g37
sg32
S''
sbstp54
sS'_import_info'
p55
(ihappydoclib.parseinfo.imports
ImportInfo
p56
(dp57
S'_named_imports'
p58
(dp59
S'Node'
p60
(lp61
S'Node'
p62
asS'Graph'
p63
(lp64
S'Graph'
p65
asS'Edge'
p66
(lp67
S'Edge'
p68
assS'_straight_imports'
p69
(lp70
sbsg21
g22
sg23
S'"""Graph related input and output\n\n Connection table format\n numnodes, numedges\n machine_address\n .\n .\n cable_type node_index1 node_index2\n .\n .\n\nThere should be as many nodes as numnodes and edges as numedges.\n\nAn example of a connection table is:\n3 2\ndarkstar.wi.mit.edu\nfang.harvard.edu\nwww.wi.mit.edu\nt3 1 2\nt2 2 3\n\nNote that the node indices start with 1 and not 0\n"""'
p71
sg24
S'GraphIO'
p72
sg25
Nsg26
g27
sg28
(dp73
S'include_comments'
p74
I1
sS'cacheFilePrefix'
p75
S'.happydoc.'
p76
sS'useCache'
p77
I1
sS'docStringFormat'
p78
S'StructuredText'
p79
ssg30
g5
sg31
g6
sg32
S''
sbt.