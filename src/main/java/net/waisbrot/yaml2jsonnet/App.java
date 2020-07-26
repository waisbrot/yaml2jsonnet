package net.waisbrot.yaml2jsonnet;

import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.Parser;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.CommonTokenStream;

/**
 * Hello world!
 *
 */
public class App {
    public static void main( String[] args ) throws Exception {
        System.out.println( "Begin parse" );
        CharStream input = new ANTLRInputStream(System.in);
        Lexer lexer = new YamlLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        YamlParser parser = new YamlParser(tokens);
        // YamlParser.StreamContext ctx = parser.stream();
        
        System.out.println(parser.comment().toStringTree());
    }
}
