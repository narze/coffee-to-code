pragma solidity >=0.7.0 <0.9.0;

contract Coffee2Code {

    string coffee = "coffee";

    function code() public view returns (string memory) {
        bytes memory _str = bytes(coffee);
        
        // coffee -> code : 6 -> 4
        string memory tmp = new string(_str.length - 2);
        bytes memory _code = bytes(tmp);
        
        uint filled = 0;
        for(uint i = 0; filled < _str.length - 2; i++) {
            if (keccak256(abi.encodePacked(_str[i])) == keccak256(abi.encodePacked("f"))) {
                _code[filled] = "d";
                i+=1;
            } else if (keccak256(abi.encodePacked(_str[i])) == keccak256(abi.encodePacked("e"))) {
                _code[filled] = "e";
                i+=1;
            } else {
                _code[filled] = _str[i];
            }
            filled += 1;
        }

        return string(_code);
    }
}