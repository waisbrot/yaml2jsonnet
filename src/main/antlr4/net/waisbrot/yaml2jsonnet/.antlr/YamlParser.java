// Generated from /home/waisbrot/git/yamlToJsonnet/src/main/antlr4/net/waisbrot/yaml2jsonnet/Yaml.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YamlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		COMMENT_START=1, COMMENT_BODY=2, EOL=3, DOCUMENT_START=4, DOCUMENT_END=5, 
		LIST_START=6, STRING_CHARS=7, WS=8;
	public static final int
		RULE_stream = 0, RULE_comment = 1, RULE_comment_body = 2, RULE_document = 3, 
		RULE_document_body = 4, RULE_document_start = 5, RULE_document_end = 6, 
		RULE_list = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"stream", "comment", "comment_body", "document", "document_body", "document_start", 
			"document_end", "list"
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

	@Override
	public String getGrammarFileName() { return "Yaml.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public YamlParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StreamContext extends ParserRuleContext {
		public DocumentContext document() {
			return getRuleContext(DocumentContext.class,0);
		}
		public List<CommentContext> comment() {
			return getRuleContexts(CommentContext.class);
		}
		public CommentContext comment(int i) {
			return getRuleContext(CommentContext.class,i);
		}
		public List<StreamContext> stream() {
			return getRuleContexts(StreamContext.class);
		}
		public StreamContext stream(int i) {
			return getRuleContext(StreamContext.class,i);
		}
		public TerminalNode EOF() { return getToken(YamlParser.EOF, 0); }
		public StreamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stream; }
	}

	public final StreamContext stream() throws RecognitionException {
		StreamContext _localctx = new StreamContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_stream);
		try {
			int _alt;
			setState(30);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMENT_START:
			case EOL:
			case DOCUMENT_START:
			case DOCUMENT_END:
			case LIST_START:
			case WS:
				enterOuterAlt(_localctx, 1);
				{
				setState(19);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(16);
						comment();
						}
						} 
					}
					setState(21);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
				}
				setState(22);
				document();
				setState(26);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(23);
						stream();
						}
						} 
					}
					setState(28);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
				}
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				setState(29);
				match(EOF);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CommentContext extends ParserRuleContext {
		public TerminalNode COMMENT_START() { return getToken(YamlParser.COMMENT_START, 0); }
		public Comment_bodyContext comment_body() {
			return getRuleContext(Comment_bodyContext.class,0);
		}
		public List<TerminalNode> WS() { return getTokens(YamlParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(YamlParser.WS, i);
		}
		public CommentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comment; }
	}

	public final CommentContext comment() throws RecognitionException {
		CommentContext _localctx = new CommentContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_comment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WS) {
				{
				{
				setState(32);
				match(WS);
				}
				}
				setState(37);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(38);
			match(COMMENT_START);
			setState(39);
			comment_body();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Comment_bodyContext extends ParserRuleContext {
		public TerminalNode COMMENT_BODY() { return getToken(YamlParser.COMMENT_BODY, 0); }
		public TerminalNode EOL() { return getToken(YamlParser.EOL, 0); }
		public Comment_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comment_body; }
	}

	public final Comment_bodyContext comment_body() throws RecognitionException {
		Comment_bodyContext _localctx = new Comment_bodyContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_comment_body);
		try {
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMMENT_BODY:
				enterOuterAlt(_localctx, 1);
				{
				setState(41);
				match(COMMENT_BODY);
				setState(42);
				match(EOL);
				}
				break;
			case EOL:
				enterOuterAlt(_localctx, 2);
				{
				setState(43);
				match(EOL);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DocumentContext extends ParserRuleContext {
		public Document_endContext document_end() {
			return getRuleContext(Document_endContext.class,0);
		}
		public Document_startContext document_start() {
			return getRuleContext(Document_startContext.class,0);
		}
		public List<CommentContext> comment() {
			return getRuleContexts(CommentContext.class);
		}
		public CommentContext comment(int i) {
			return getRuleContext(CommentContext.class,i);
		}
		public Document_bodyContext document_body() {
			return getRuleContext(Document_bodyContext.class,0);
		}
		public DocumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_document; }
	}

	public final DocumentContext document() throws RecognitionException {
		DocumentContext _localctx = new DocumentContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_document);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DOCUMENT_START) {
				{
				setState(46);
				document_start();
				}
			}

			setState(52);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(49);
					comment();
					}
					} 
				}
				setState(54);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			setState(56);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LIST_START) {
				{
				setState(55);
				document_body();
				}
			}

			setState(61);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(58);
					comment();
					}
					} 
				}
				setState(63);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			setState(64);
			document_end();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Document_bodyContext extends ParserRuleContext {
		public ListContext list() {
			return getRuleContext(ListContext.class,0);
		}
		public Document_bodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_document_body; }
	}

	public final Document_bodyContext document_body() throws RecognitionException {
		Document_bodyContext _localctx = new Document_bodyContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_document_body);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			list();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Document_startContext extends ParserRuleContext {
		public TerminalNode DOCUMENT_START() { return getToken(YamlParser.DOCUMENT_START, 0); }
		public TerminalNode EOL() { return getToken(YamlParser.EOL, 0); }
		public List<TerminalNode> WS() { return getTokens(YamlParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(YamlParser.WS, i);
		}
		public Document_startContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_document_start; }
	}

	public final Document_startContext document_start() throws RecognitionException {
		Document_startContext _localctx = new Document_startContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_document_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(DOCUMENT_START);
			setState(72);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WS) {
				{
				{
				setState(69);
				match(WS);
				}
				}
				setState(74);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(75);
			match(EOL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Document_endContext extends ParserRuleContext {
		public TerminalNode EOL() { return getToken(YamlParser.EOL, 0); }
		public TerminalNode DOCUMENT_END() { return getToken(YamlParser.DOCUMENT_END, 0); }
		public List<TerminalNode> WS() { return getTokens(YamlParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(YamlParser.WS, i);
		}
		public Document_endContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_document_end; }
	}

	public final Document_endContext document_end() throws RecognitionException {
		Document_endContext _localctx = new Document_endContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_document_end);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DOCUMENT_END) {
				{
				setState(77);
				match(DOCUMENT_END);
				}
			}

			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==WS) {
				{
				{
				setState(80);
				match(WS);
				}
				}
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(86);
			match(EOL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListContext extends ParserRuleContext {
		public TerminalNode LIST_START() { return getToken(YamlParser.LIST_START, 0); }
		public TerminalNode STRING_CHARS() { return getToken(YamlParser.STRING_CHARS, 0); }
		public TerminalNode EOL() { return getToken(YamlParser.EOL, 0); }
		public List<ListContext> list() {
			return getRuleContexts(ListContext.class);
		}
		public ListContext list(int i) {
			return getRuleContext(ListContext.class,i);
		}
		public ListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_list; }
	}

	public final ListContext list() throws RecognitionException {
		ListContext _localctx = new ListContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_list);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(LIST_START);
			setState(89);
			match(STRING_CHARS);
			setState(90);
			match(EOL);
			setState(94);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(91);
					list();
					}
					} 
				}
				setState(96);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\nd\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\3\2\7\2\24\n\2\f\2"+
		"\16\2\27\13\2\3\2\3\2\7\2\33\n\2\f\2\16\2\36\13\2\3\2\5\2!\n\2\3\3\7\3"+
		"$\n\3\f\3\16\3\'\13\3\3\3\3\3\3\3\3\4\3\4\3\4\5\4/\n\4\3\5\5\5\62\n\5"+
		"\3\5\7\5\65\n\5\f\5\16\58\13\5\3\5\5\5;\n\5\3\5\7\5>\n\5\f\5\16\5A\13"+
		"\5\3\5\3\5\3\6\3\6\3\7\3\7\7\7I\n\7\f\7\16\7L\13\7\3\7\3\7\3\b\5\bQ\n"+
		"\b\3\b\7\bT\n\b\f\b\16\bW\13\b\3\b\3\b\3\t\3\t\3\t\3\t\7\t_\n\t\f\t\16"+
		"\tb\13\t\3\t\2\2\n\2\4\6\b\n\f\16\20\2\2\2h\2 \3\2\2\2\4%\3\2\2\2\6.\3"+
		"\2\2\2\b\61\3\2\2\2\nD\3\2\2\2\fF\3\2\2\2\16P\3\2\2\2\20Z\3\2\2\2\22\24"+
		"\5\4\3\2\23\22\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26\30"+
		"\3\2\2\2\27\25\3\2\2\2\30\34\5\b\5\2\31\33\5\2\2\2\32\31\3\2\2\2\33\36"+
		"\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35!\3\2\2\2\36\34\3\2\2\2\37!\7\2"+
		"\2\3 \25\3\2\2\2 \37\3\2\2\2!\3\3\2\2\2\"$\7\n\2\2#\"\3\2\2\2$\'\3\2\2"+
		"\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2()\7\3\2\2)*\5\6\4\2*\5\3\2"+
		"\2\2+,\7\4\2\2,/\7\5\2\2-/\7\5\2\2.+\3\2\2\2.-\3\2\2\2/\7\3\2\2\2\60\62"+
		"\5\f\7\2\61\60\3\2\2\2\61\62\3\2\2\2\62\66\3\2\2\2\63\65\5\4\3\2\64\63"+
		"\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67:\3\2\2\28\66\3\2\2"+
		"\29;\5\n\6\2:9\3\2\2\2:;\3\2\2\2;?\3\2\2\2<>\5\4\3\2=<\3\2\2\2>A\3\2\2"+
		"\2?=\3\2\2\2?@\3\2\2\2@B\3\2\2\2A?\3\2\2\2BC\5\16\b\2C\t\3\2\2\2DE\5\20"+
		"\t\2E\13\3\2\2\2FJ\7\6\2\2GI\7\n\2\2HG\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3"+
		"\2\2\2KM\3\2\2\2LJ\3\2\2\2MN\7\5\2\2N\r\3\2\2\2OQ\7\7\2\2PO\3\2\2\2PQ"+
		"\3\2\2\2QU\3\2\2\2RT\7\n\2\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V"+
		"X\3\2\2\2WU\3\2\2\2XY\7\5\2\2Y\17\3\2\2\2Z[\7\b\2\2[\\\7\t\2\2\\`\7\5"+
		"\2\2]_\5\20\t\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2a\21\3\2\2\2b`"+
		"\3\2\2\2\17\25\34 %.\61\66:?JPU`";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}