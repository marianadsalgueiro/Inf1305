pragma solidity ^0.5.0;

contract RainCoin {
    address payable dono; //dono do contrato
    mapping(address => uint) litros; //quantidade de litros de agua q a pessoa tem
    mapping(address => uint) preco; //preco por litro em wei
    
    constructor(uint _litros, uint _preco) public{
        dono = msg.sender;
        litros[dono] = _litros;
        preco[dono] = _preco;
    }
    
    modifier apenasDono(){
        require (msg.sender == dono, "Apenas o dono do contrato pode fazer isso!");
        _;
    }
    
    //funcao acumulativa; pessoa pode adicionar a quantidade de litros por dia e no contrato vai constar o total
    function setLitros(uint _l) public apenasDono{
        litros[dono] += _l;
    }
    
    //dono pode setar o preco q quiser
    function setPreco(uint _p) public apenasDono{
        preco[dono] = _p;
    }
    
    function getLitrosDono() public view returns (uint){
        return litros[dono];
    }
    
    function getPreco() public view returns (uint){
        return preco[dono];
    }
    
    function getLitrosComprador() public view returns (uint){
        return litros[msg.sender];
    }
    
    function transferir(uint _volume) payable public{
        require (msg.value >= _volume*preco[dono], "O valor enviado não corresponde ao estipulado pelo dono do contrato.");
        require (litros[dono] >= _volume, "O dono não possui esta quantidade de litros disponível.");
        
        //troco
        uint troco = msg.value - _volume*preco[dono];
        if(troco > 0){
            msg.sender.transfer(troco);
        }
        
        litros[dono] -= _volume;
        litros[msg.sender] += _volume;
        
        dono.transfer(address(this).balance);
    }
    
}