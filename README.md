# EVM_LLL_Retesteth

<img src="https://github.com/MarcusWentz/EVM_LLL_Retesteth/blob/main/images/lispLikeLanguageLogo.png" alt="Output"/>

Custom Lisp Like Language (lll) logo (inspired from the Lisp language logo https://en.wikipedia.org/wiki/Lisp_(programming_language) )

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
- NOT (To test large negative values (NOT [1's complement]+1= 2's complement [negative value]) in hex format
- EXP (To test the max value for uint slots [(2**256)-1] (256 bits, 32 bytes, 64 hex digits)
- MSG.VALUE Tx from user to smart contract updates balances.

# Run:
After installing locally [with docker image from: http://retesteth.ethdevops.io/web/], run test with:

## Docker Sudo permission 
    whoami 
    sudo usermod -a -G docker <'whoami' value goes here>

## Docker:
    ./dretesteth.sh -t GeneralStateTests/stExample -- --singletest CalculatorFunding --testpath ~/tests --datadir /tests/config --filltests

## Client Geth (t8ntool) IP and Port [other clients configs in tests/config] (docker sudo ):
            
    ./dretesteth.sh -t GeneralStateTests/stExample -- --singletest CalculatorFunding --testpath ~/tests --datadir /tests/config --clients t8ntool \ --nodes 127.0.0.1:8545

- [Reference: https://ethereum-tests.readthedocs.io/en/latest/state-transition-tutorial.html#compiling-your-first-test]

# Output:
<img src="https://github.com/MarcusWentz/EVM_LLL_Retesteth/blob/main/images/EVM_RESULT_3.png" alt="Output"/>
