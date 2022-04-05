# EVM_LLL_Retesteth

EVM testing using the Lisp Like Language (lll) [very low level EVM language].

# Tests:
- SSTORE
- ADD
- SUB
- DIV
- MUL
- TIMESTAMP
- XOR
- EQ
- GT
- LT
- OR
- MOD
- SHR
- SHL
- NOT (To test large negative values in hex format)
- EXP (To test the max value for uint slots [(2**256)-1] (256 bits, 32 bytes, 64 hex digits)
- MSG.VALUE Tx from user to smart contract updates balances.

# Run:
After installing locally [with docker image from: http://retesteth.ethdevops.io/web/], run test with:
- 1.Copy MathOperatiionsAndMSG_VALUE.yaml and paste into tests/src/GeneralStateTestsFiller/stExample/01_add22Filler.yml
- 2.Run the following commands: https://ethereum-tests.readthedocs.io/en/latest/state-transition-tutorial.html#compiling-your-first-test

# Output:
<img src="https://github.com/MarcusWentz/EVM_LLL_Retesteth/blob/main/images/EVM_RESULT.png" alt="Output"/>
