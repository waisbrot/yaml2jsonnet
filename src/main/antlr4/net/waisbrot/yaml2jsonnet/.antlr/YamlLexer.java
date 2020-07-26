// Generated from /home/waisbrot/git/yamlToJsonnet/src/main/antlr4/net/waisbrot/yaml2jsonnet/Yaml.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YamlLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMMENT_START=1, COMMENT_BODY=2, EOL=3, DOCUMENT_START=4, DOCUMENT_END=5, 
		LIST_START=6, STRING_CHARS=7, WS=8;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"COMMENT_START", "COMMENT_BODY", "EOL", "DOCUMENT_START", "DOCUMENT_END", 
			"LIST_START", "STRING_CHARS", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'#'", null, null, "'---'", "'...'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "COMMENT_START", "COMMENT_BODY", "EOL", "DOCUMENT_START", "DOCUMENT_END", 
			"LIST_START", "STRING_CHARS", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public YamlLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Yaml.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n\64\b\1\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\3\2\3\3\6"+
		"\3\27\n\3\r\3\16\3\30\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7"+
		"\7\7\'\n\7\f\7\16\7*\13\7\3\b\3\b\7\b.\n\b\f\b\16\b\61\13\b\3\t\3\t\2"+
		"\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\3\2\7\5\2\"\"C\\c|\3\2\f\f\4\2"+
		"C\\c|\4\2\f\f``\4\2\13\13\"\"\2\66\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2"+
		"\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3"+
		"\2\2\2\5\26\3\2\2\2\7\32\3\2\2\2\t\34\3\2\2\2\13 \3\2\2\2\r$\3\2\2\2\17"+
		"+\3\2\2\2\21\62\3\2\2\2\23\24\7%\2\2\24\4\3\2\2\2\25\27\t\2\2\2\26\25"+
		"\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\6\3\2\2\2\32\33"+
		"\t\3\2\2\33\b\3\2\2\2\34\35\7/\2\2\35\36\7/\2\2\36\37\7/\2\2\37\n\3\2"+
		"\2\2 !\7\60\2\2!\"\7\60\2\2\"#\7\60\2\2#\f\3\2\2\2$(\7/\2\2%\'\5\21\t"+
		"\2&%\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\16\3\2\2\2*(\3\2\2\2+/\t"+
		"\4\2\2,.\t\5\2\2-,\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\20\3\2"+
		"\2\2\61/\3\2\2\2\62\63\t\6\2\2\63\22\3\2\2\2\6\2\30(/\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}