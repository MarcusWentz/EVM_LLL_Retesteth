// SPDX-License-Identifier: MIT
pragma solidity 0.8.15;

contract mixHashEIP4399 {
  
    uint public prevrandaoStorageSolidity;
    uint public prevrandaoStorageAssemblyYul;
    uint public blockNumberStorage;
    uint public minerTipStorageYul;

    constructor() {
        prevrandaoStorageSolidity = block.difficulty;
        assembly{ 
            sstore(prevrandaoStorageAssemblyYul.slot, difficulty() ) 
            sstore(minerTipStorageYul.slot, basefee() ) 
            }
        blockNumberStorage = block.number;
    }

}
