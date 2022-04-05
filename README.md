# EVM_LLL_Retesteth

EVM testing using the Lisp Like Language (lll) [very low level EVM language].

Tests the following opcodes:
-SSTORE
-ADD
-SUB
-DIV
-MUL
-TIMESTAMP
-XOR
-EQ
-GT
-LT
-OR
-MOD
-SHR
-SHL
-NOT
-EXP (To test the max value for uint slots [(2**256)-1] (256 bits, 32 bytes, 64 hex digits)

Also checks to see if MSG.VALUE Tx from user to smart contract updates balances.

After installing locally [with docker image from: http://retesteth.ethdevops.io/web/], run test with:
1.Copy MathOperatiionsAndMSG_VALUE.yaml and paste into tests/src/GeneralStateTestsFiller/stExample/01_add22Filler.yml
2.Run the following commands: https://ethereum-tests.readthedocs.io/en/latest/state-transition-tutorial.html#compiling-your-first-test
