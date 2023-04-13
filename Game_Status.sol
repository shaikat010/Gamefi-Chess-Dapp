// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract GameStatus{
    uint public Game_Count = 0;
    string current_winner;

    function storeResult(string memory _content) public {
        current_winner = _content;
        Game_Count++;
    }

    function get_status() public view returns(string memory _status){
        return current_winner;
    }
}

