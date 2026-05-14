%{
#include <stdio.h>

FILE *yyin;
%}

%%

(if|else|while|switch|for|return|int|float|char) {
    printf("Keyword: %s\n", yytext);
}

[a-zA-Z_][a-zA-Z0-9_]* {
    printf("Identifier: %s\n", yytext);
}

[0-9]+ {
    printf("Integer: %s\n", yytext);
}

[+\-*/=] {
    printf("Operator: %s\n", yytext);
}

[{}();><] {
    printf("Special Symbol: %s\n", yytext);
}

[ \t\n]+ ;

%%

int main() {
    yyin = fopen("input.c", "r");

    if(yyin == NULL) {
        printf("Cannot open file\n");
        return 1;
    }

    yylex();

    fclose(yyin);

    return 0;
}

int yywrap() {
    return 1;
}
