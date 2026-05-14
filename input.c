// Commands to compile and run the lexer:
// flex program.l
// gcc lex.yy.c -lfl -o lexer
// ./lexer
int main(){
    int a = 10;
    if(a>5){
        a=a+1;
        print("a is greater than 5");
    }
    return 0;
}