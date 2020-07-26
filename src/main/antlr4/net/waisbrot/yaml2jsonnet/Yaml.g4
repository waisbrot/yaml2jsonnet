grammar Yaml;

stream : comment* document stream* | EOF ;

comment : WS* COMMENT_START comment_body ;

comment_body 
 : COMMENT_BODY EOL
 | EOL
 ;

document : document_start? comment* document_body? comment* document_end ;

document_body : list ;

document_start : DOCUMENT_START WS* EOL ;

document_end : DOCUMENT_END? WS* EOL ;

list : LIST_START STRING_CHARS EOL list* ;

COMMENT_START : '#' ;
COMMENT_BODY : [ a-zA-Z]+ ;
EOL : [\n];
DOCUMENT_START : '---' ;
DOCUMENT_END : '...' ;
LIST_START : '-' WS* ;
STRING_CHARS : [a-zA-Z][^\n]* ;
WS : ' ' | '\t' ;