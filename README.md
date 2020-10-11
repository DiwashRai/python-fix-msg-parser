# python-fix-msg-parser
Tired of alt-tabbing to the [onixs FIX dictionary website](https://www.onixs.biz/fix-dictionary.html)?  
Can't memorise all 1000 ish tags + extra custom ones? This script is just for you!

This python script takes fix messages from an input txt file, parses it, adds info from a  data dictionary and outputs it into an output txt file.  
Useful if you don't want to put your message logs into a parsing website or if you need to use a custom data dictionary.

Takes fix strings like this:

```
8=FIX.4.4|9=122|35=D|34=215|49=CLIENT12|52=20100225-19:41:57.316|56=B|1=Marcel|11=13346|21=1|40=2|44=5|54=1|59=0|60=20100225-19:39:52.020|10=072|

8=FIX.4.4|9=229|35=8|34=2835|49=UBE|52=20120329-12:48:45|56=ORD|6=0|11=1333025321|14=0|15=USD|17=E3291248457680|32=0|37=F025051503083|38=1000000|39=0|40=D|44=82.266|54=1|55=USD/JPY|59=3|150=0|151=1000000|461=RXXX|10=008
```

And makes them more human readable and adds info about each field from a data dictionary of your choosing.
Below is with  
print_enums = True  
use_row_separators = False

```
8     | BeginString             | FIX.4.4
9     | BodyLength              | 122
35    | MsgType                 | D                                                  0 : HEARTBEAT, 1 : TEST_REQUEST, 2 : RESEND_REQUEST, 3 : REJECT, 4 : SEQUENCE_RESET, 5 : LOGOUT, 6 : INDICATION_OF_INTEREST, 7 : ADVERTISEMENT, 8 : EXECUTION_REPORT, 9 : ORDER_CANCEL_REJECT, A : LOGON, B : NEWS, C : EMAIL, D : ORDER_SINGLE, E : ORDER_LIST, F : ORDER_CANCEL_REQUEST, G : ORDER_CANCEL_REPLACE_REQUEST, H : ORDER_STATUS_REQUEST, J : ALLOCATION_INSTRUCTION, K : LIST_CANCEL_REQUEST, L : LIST_EXECUTE, M : LIST_STATUS_REQUEST, N : LIST_STATUS, P : ALLOCATION_INSTRUCTION_ACK, Q : DONT_KNOW_TRADE, R : QUOTE_REQUEST, S : QUOTE, T : SETTLEMENT_INSTRUCTIONS, V : MARKET_DATA_REQUEST, W : MARKET_DATA_SNAPSHOT_FULL_REFRESH, X : MARKET_DATA_INCREMENTAL_REFRESH, Y : MARKET_DATA_REQUEST_REJECT, Z : QUOTE_CANCEL, a : QUOTE_STATUS_REQUEST, b : MASS_QUOTE_ACKNOWLEDGEMENT, c : SECURITY_DEFINITION_REQUEST, d : SECURITY_DEFINITION, e : SECURITY_STATUS_REQUEST, f : SECURITY_STATUS, g : TRADING_SESSION_STATUS_REQUEST, h : TRADING_SESSION_STATUS, i : MASS_QUOTE, j : BUSINESS_MESSAGE_REJECT, k : BID_REQUEST, l : BID_RESPONSE, m : LIST_STRIKE_PRICE, n : XML_MESSAGE, o : REGISTRATION_INSTRUCTIONS, p : REGISTRATION_INSTRUCTIONS_RESPONSE, q : ORDER_MASS_CANCEL_REQUEST, r : ORDER_MASS_CANCEL_REPORT, s : NEW_ORDER_s, t : CROSS_ORDER_CANCEL_REPLACE_REQUEST, u : CROSS_ORDER_CANCEL_REQUEST, v : SECURITY_TYPE_REQUEST, w : SECURITY_TYPES, x : SECURITY_LIST_REQUEST, y : SECURITY_LIST, z : DERIVATIVE_SECURITY_LIST_REQUEST, AA : DERIVATIVE_SECURITY_LIST, AB : NEW_ORDER_AB, AC : MULTILEG_ORDER_CANCEL_REPLACE, AD : TRADE_CAPTURE_REPORT_REQUEST, AE : TRADE_CAPTURE_REPORT, AF : ORDER_MASS_STATUS_REQUEST, AG : QUOTE_REQUEST_REJECT, AH : RFQ_REQUEST, AI : QUOTE_STATUS_REPORT, AJ : QUOTE_RESPONSE, AK : CONFIRMATION, AL : POSITION_MAINTENANCE_REQUEST, AM : POSITION_MAINTENANCE_REPORT, AN : REQUEST_FOR_POSITIONS, AO : REQUEST_FOR_POSITIONS_ACK, AP : POSITION_REPORT, AQ : TRADE_CAPTURE_REPORT_REQUEST_ACK, AR : TRADE_CAPTURE_REPORT_ACK, AS : ALLOCATION_REPORT, AT : ALLOCATION_REPORT_ACK, AU : CONFIRMATION_ACK, AV : SETTLEMENT_INSTRUCTION_REQUEST, AW : ASSIGNMENT_REPORT, AX : COLLATERAL_REQUEST, AY : COLLATERAL_ASSIGNMENT, AZ : COLLATERAL_RESPONSE, BA : COLLATERAL_REPORT, BB : COLLATERAL_INQUIRY, BC : NETWORK_BC, BD : NETWORK_BD, BE : USER_REQUEST, BF : USER_RESPONSE, BG : COLLATERAL_INQUIRY_ACK, BH : CONFIRMATION_REQUEST, 
34    | MsgSeqNum               | 215
49    | SenderCompID            | CLIENT12
52    | SendingTime             | 20100225-19:41:57.316
56    | TargetCompID            | B
1     | Account                 | Marcel
11    | ClOrdID                 | 13346
21    | HandlInst               | 1                                                  1 : AUTOMATED_EXECUTION_ORDER_PRIVATE_NO_BROKER_INTERVENTION, 2 : AUTOMATED_EXECUTION_ORDER_PUBLIC_BROKER_INTERVENTION_OK, 3 : MANUAL_ORDER_BEST_EXECUTION, 
40    | OrdType                 | 2                                                  1 : MARKET, 2 : LIMIT, 3 : STOP, 4 : STOP_LIMIT, 6 : WITH_OR_WITHOUT, 7 : LIMIT_OR_BETTER, 8 : LIMIT_WITH_OR_WITHOUT, 9 : ON_BASIS, D : PREVIOUSLY_QUOTED, E : PREVIOUSLY_INDICATED, G : FOREX, I : FUNARI, J : MARKET_IF_TOUCHED, K : MARKET_WITH_LEFTOVER_AS_LIMIT, L : PREVIOUS_FUND_VALUATION_POINT, M : NEXT_FUND_VALUATION_POINT, P : PEGGED, 
44    | Price                   | 5
54    | Side                    | 1                                                  1 : BUY, 2 : SELL, 3 : BUY_MINUS, 4 : SELL_PLUS, 5 : SELL_SHORT, 6 : SELL_SHORT_EXEMPT, 7 : UNDISCLOSED, 8 : CROSS, 9 : CROSS_SHORT, A : CROSS_SHORT_EXEMPT, B : AS_DEFINED, C : OPPOSITE, D : SUBSCRIBE, E : REDEEM, F : LEND, G : BORROW, 
59    | TimeInForce             | 0                                                  0 : DAY, 1 : GOOD_TILL_CANCEL, 2 : AT_THE_OPENING, 3 : IMMEDIATE_OR_CANCEL, 4 : FILL_OR_KILL, 5 : GOOD_TILL_CROSSING, 6 : GOOD_TILL_DATE, 7 : AT_THE_CLOSE, 
60    | TransactTime            | 20100225-19:39:52.020
10    | CheckSum                | 072
####################################################################################################
8     | BeginString             | FIX.4.4
9     | BodyLength              | 229
35    | MsgType                 | 8                                                  0 : HEARTBEAT, 1 : TEST_REQUEST, 2 : RESEND_REQUEST, 3 : REJECT, 4 : SEQUENCE_RESET, 5 : LOGOUT, 6 : INDICATION_OF_INTEREST, 7 : ADVERTISEMENT, 8 : EXECUTION_REPORT, 9 : ORDER_CANCEL_REJECT, A : LOGON, B : NEWS, C : EMAIL, D : ORDER_SINGLE, E : ORDER_LIST, F : ORDER_CANCEL_REQUEST, G : ORDER_CANCEL_REPLACE_REQUEST, H : ORDER_STATUS_REQUEST, J : ALLOCATION_INSTRUCTION, K : LIST_CANCEL_REQUEST, L : LIST_EXECUTE, M : LIST_STATUS_REQUEST, N : LIST_STATUS, P : ALLOCATION_INSTRUCTION_ACK, Q : DONT_KNOW_TRADE, R : QUOTE_REQUEST, S : QUOTE, T : SETTLEMENT_INSTRUCTIONS, V : MARKET_DATA_REQUEST, W : MARKET_DATA_SNAPSHOT_FULL_REFRESH, X : MARKET_DATA_INCREMENTAL_REFRESH, Y : MARKET_DATA_REQUEST_REJECT, Z : QUOTE_CANCEL, a : QUOTE_STATUS_REQUEST, b : MASS_QUOTE_ACKNOWLEDGEMENT, c : SECURITY_DEFINITION_REQUEST, d : SECURITY_DEFINITION, e : SECURITY_STATUS_REQUEST, f : SECURITY_STATUS, g : TRADING_SESSION_STATUS_REQUEST, h : TRADING_SESSION_STATUS, i : MASS_QUOTE, j : BUSINESS_MESSAGE_REJECT, k : BID_REQUEST, l : BID_RESPONSE, m : LIST_STRIKE_PRICE, n : XML_MESSAGE, o : REGISTRATION_INSTRUCTIONS, p : REGISTRATION_INSTRUCTIONS_RESPONSE, q : ORDER_MASS_CANCEL_REQUEST, r : ORDER_MASS_CANCEL_REPORT, s : NEW_ORDER_s, t : CROSS_ORDER_CANCEL_REPLACE_REQUEST, u : CROSS_ORDER_CANCEL_REQUEST, v : SECURITY_TYPE_REQUEST, w : SECURITY_TYPES, x : SECURITY_LIST_REQUEST, y : SECURITY_LIST, z : DERIVATIVE_SECURITY_LIST_REQUEST, AA : DERIVATIVE_SECURITY_LIST, AB : NEW_ORDER_AB, AC : MULTILEG_ORDER_CANCEL_REPLACE, AD : TRADE_CAPTURE_REPORT_REQUEST, AE : TRADE_CAPTURE_REPORT, AF : ORDER_MASS_STATUS_REQUEST, AG : QUOTE_REQUEST_REJECT, AH : RFQ_REQUEST, AI : QUOTE_STATUS_REPORT, AJ : QUOTE_RESPONSE, AK : CONFIRMATION, AL : POSITION_MAINTENANCE_REQUEST, AM : POSITION_MAINTENANCE_REPORT, AN : REQUEST_FOR_POSITIONS, AO : REQUEST_FOR_POSITIONS_ACK, AP : POSITION_REPORT, AQ : TRADE_CAPTURE_REPORT_REQUEST_ACK, AR : TRADE_CAPTURE_REPORT_ACK, AS : ALLOCATION_REPORT, AT : ALLOCATION_REPORT_ACK, AU : CONFIRMATION_ACK, AV : SETTLEMENT_INSTRUCTION_REQUEST, AW : ASSIGNMENT_REPORT, AX : COLLATERAL_REQUEST, AY : COLLATERAL_ASSIGNMENT, AZ : COLLATERAL_RESPONSE, BA : COLLATERAL_REPORT, BB : COLLATERAL_INQUIRY, BC : NETWORK_BC, BD : NETWORK_BD, BE : USER_REQUEST, BF : USER_RESPONSE, BG : COLLATERAL_INQUIRY_ACK, BH : CONFIRMATION_REQUEST, 
34    | MsgSeqNum               | 2835
49    | SenderCompID            | UBE
52    | SendingTime             | 20120329-12:48:45
56    | TargetCompID            | ORD
6     | AvgPx                   | 0
11    | ClOrdID                 | 1333025321
14    | CumQty                  | 0
15    | Currency                | USD
17    | ExecID                  | E3291248457680
32    | LastQty                 | 0
37    | OrderID                 | F025051503083
38    | OrderQty                | 1000000
39    | OrdStatus               | 0                                                  0 : NEW, 1 : PARTIALLY_FILLED, 2 : FILLED, 3 : DONE_FOR_DAY, 4 : CANCELED, 6 : PENDING_CANCEL, 7 : STOPPED, 8 : REJECTED, 9 : SUSPENDED, A : PENDING_NEW, B : CALCULATED, C : EXPIRED, D : ACCEPTED_FOR_BIDDING, E : PENDING_REPLACE, 
40    | OrdType                 | D                                                  1 : MARKET, 2 : LIMIT, 3 : STOP, 4 : STOP_LIMIT, 6 : WITH_OR_WITHOUT, 7 : LIMIT_OR_BETTER, 8 : LIMIT_WITH_OR_WITHOUT, 9 : ON_BASIS, D : PREVIOUSLY_QUOTED, E : PREVIOUSLY_INDICATED, G : FOREX, I : FUNARI, J : MARKET_IF_TOUCHED, K : MARKET_WITH_LEFTOVER_AS_LIMIT, L : PREVIOUS_FUND_VALUATION_POINT, M : NEXT_FUND_VALUATION_POINT, P : PEGGED, 
44    | Price                   | 82.266
54    | Side                    | 1                                                  1 : BUY, 2 : SELL, 3 : BUY_MINUS, 4 : SELL_PLUS, 5 : SELL_SHORT, 6 : SELL_SHORT_EXEMPT, 7 : UNDISCLOSED, 8 : CROSS, 9 : CROSS_SHORT, A : CROSS_SHORT_EXEMPT, B : AS_DEFINED, C : OPPOSITE, D : SUBSCRIBE, E : REDEEM, F : LEND, G : BORROW, 
55    | Symbol                  | USD/JPY
59    | TimeInForce             | 3                                                  0 : DAY, 1 : GOOD_TILL_CANCEL, 2 : AT_THE_OPENING, 3 : IMMEDIATE_OR_CANCEL, 4 : FILL_OR_KILL, 5 : GOOD_TILL_CROSSING, 6 : GOOD_TILL_DATE, 7 : AT_THE_CLOSE, 
150   | ExecType                | 0                                                  0 : NEW, 3 : DONE_FOR_DAY, 4 : CANCELED, 5 : REPLACE, 6 : PENDING_CANCEL, 7 : STOPPED, 8 : REJECTED, 9 : SUSPENDED, A : PENDING_NEW, B : CALCULATED, C : EXPIRED, D : RESTATED, E : PENDING_REPLACE, F : TRADE, G : TRADE_CORRECT, H : TRADE_CANCEL, I : ORDER_STATUS, 
151   | LeavesQty               | 1000000
461   | CFICode                 | RXXX
10    | CheckSum                | 008
####################################################################################################

```

This is with  
print_enums = True  
use_row_separators = False

```
------+-------------------------+---------------------------------------------------
8     | BeginString             | FIX.4.4
------+-------------------------+---------------------------------------------------
9     | BodyLength              | 122
------+-------------------------+---------------------------------------------------
35    | MsgType                 | D
------+-------------------------+---------------------------------------------------
34    | MsgSeqNum               | 215
------+-------------------------+---------------------------------------------------
49    | SenderCompID            | CLIENT12
------+-------------------------+---------------------------------------------------
52    | SendingTime             | 20100225-19:41:57.316
------+-------------------------+---------------------------------------------------
56    | TargetCompID            | B
------+-------------------------+---------------------------------------------------
1     | Account                 | Marcel
------+-------------------------+---------------------------------------------------
11    | ClOrdID                 | 13346
------+-------------------------+---------------------------------------------------
21    | HandlInst               | 1
------+-------------------------+---------------------------------------------------
40    | OrdType                 | 2
------+-------------------------+---------------------------------------------------
44    | Price                   | 5
------+-------------------------+---------------------------------------------------
54    | Side                    | 1
------+-------------------------+---------------------------------------------------
59    | TimeInForce             | 0
------+-------------------------+---------------------------------------------------
60    | TransactTime            | 20100225-19:39:52.020
------+-------------------------+---------------------------------------------------
10    | CheckSum                | 072
------+-------------------------+---------------------------------------------------
####################################################################################################
------+-------------------------+---------------------------------------------------
8     | BeginString             | FIX.4.4
------+-------------------------+---------------------------------------------------
9     | BodyLength              | 229
------+-------------------------+---------------------------------------------------
35    | MsgType                 | 8
------+-------------------------+---------------------------------------------------
34    | MsgSeqNum               | 2835
------+-------------------------+---------------------------------------------------
49    | SenderCompID            | UBE
------+-------------------------+---------------------------------------------------
52    | SendingTime             | 20120329-12:48:45
------+-------------------------+---------------------------------------------------
56    | TargetCompID            | ORD
------+-------------------------+---------------------------------------------------
6     | AvgPx                   | 0
------+-------------------------+---------------------------------------------------
11    | ClOrdID                 | 1333025321
------+-------------------------+---------------------------------------------------
14    | CumQty                  | 0
------+-------------------------+---------------------------------------------------
15    | Currency                | USD
------+-------------------------+---------------------------------------------------
17    | ExecID                  | E3291248457680
------+-------------------------+---------------------------------------------------
32    | LastQty                 | 0
------+-------------------------+---------------------------------------------------
37    | OrderID                 | F025051503083
------+-------------------------+---------------------------------------------------
38    | OrderQty                | 1000000
------+-------------------------+---------------------------------------------------
39    | OrdStatus               | 0
------+-------------------------+---------------------------------------------------
40    | OrdType                 | D
------+-------------------------+---------------------------------------------------
44    | Price                   | 82.266
------+-------------------------+---------------------------------------------------
54    | Side                    | 1
------+-------------------------+---------------------------------------------------
55    | Symbol                  | USD/JPY
------+-------------------------+---------------------------------------------------
59    | TimeInForce             | 3
------+-------------------------+---------------------------------------------------
150   | ExecType                | 0
------+-------------------------+---------------------------------------------------
151   | LeavesQty               | 1000000
------+-------------------------+---------------------------------------------------
461   | CFICode                 | RXXX
------+-------------------------+---------------------------------------------------
10    | CheckSum                | 008
------+-------------------------+---------------------------------------------------
####################################################################################################

```

A fix4.4 dictionary is part of the repo as a sample as well as the two fix sample messages from above in an input text file.
The output text file is also available with the output of the two sample fix messages in it.
