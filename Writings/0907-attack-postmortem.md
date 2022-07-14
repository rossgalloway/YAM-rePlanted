# July 9th 2022 Governance Attack Postmortem

## Important Wallets and Actors

### Attacker

- `Attacker wallet A`: [0x4429abbf523bef0f1e934b04cff8584955c72548](https://etherscan.io/address/0x4429abbf523bef0f1e934b04cff8584955c72548)
- `Attacker wallet B`: [0x0DE41bDc58FfAF4A8c1b7084a544fBBe10a9DE56](https://etherscan.io/address/0x0DE41bDc58FfAF4A8c1b7084a544fBBe10a9DE56)
- `Attacker Wallet C`: [0x3C749D3fCE03eE5d7Ff43fF09C9e07E9807E51f0](https://etherscan.io/address/0x0DE41bDc58FfAF4A8c1b7084a544fBBe10a9DE56)
- `Attacker Wallet D`: [0x0946969bc3BE7e9B436a399C55dD3ffb029B0e95](https://etherscan.io/address/0x0946969bc3BE7e9B436a399C55dD3ffb029B0e95)
- `Attacker Contract`: [0x15515330e7C003dD4594b737165F2bf2EE671D82](https://etherscan.io/address/0x15515330e7C003dD4594b737165F2bf2EE671D82)

### YAM Governance

- `Yam Governor Contract`: [0x2da253835967d6e721c6c077157f9c9742934aea](https://etherscan.io/address/0x2da253835967d6e721c6c077157f9c9742934aea)\
This is the main governance conract for the Yam DAO. This contract controls the treasury via YAM Token voting. 
- `Yam Incentivizer Contract`: [0xd67c05523d8ec1c60760fd017ef006b9f6e496d0](https://etherscan.io/address/0xd67c05523d8ec1c60760fd017ef006b9f6e496d0)\
This contract is used to grant voting power to Sushiswap ETH/YAM Liquidity Providers.
- `Yam Treasury Contract`: [0x97990b693835da58a281636296d2bf02787dea17](https://etherscan.io/address/0x97990b693835da58a281636296d2bf02787dea17)
- `Yam Timelock`: [0x8b4f1616751117c38a0f84f9a146cca191ea3ec5](https://etherscan.io/address/0x8b4f1616751117c38a0f84f9a146cca191ea3ec5)

## Background

The Yam Treasury is controlled directly by the Yam governor contract. Successful votes allow access to the treasury via the timelock contract. The governor contracts reads voting power from both the YAM token address and the Yam incentivizer contract. The governance system is based on the Compound Bravo governor contracts.

## Events

### July 7th 2022

1. `Attacker wallet A` was funded with 200 ETH via tornado cash in 2 transactions [17:54 & 18:42 UTC]. It then proceeded to send 135 ETH to `Attacker wallet B` in the 3 transactions [18:48 - 20:41 UTC]:

   - Tornado Cash transfers: <https://etherscan.io/address/0x4429abbf523bef0f1e934b04cff8584955c72548#internaltx>
   - 10 ETH transfer: <https://etherscan.io/tx/0xc56cc7f671694f9f62f00723bf953dc5320c1a561fafcaab6199a5c18c88db18>
   - 50 ETH transfer: <https://etherscan.io/tx/0x765baa68b27f2b52049c51cf7fa23c717d97d542cde7c85cd1108c956b00b50a>
   - 75 ETH Transfer: <https://etherscan.io/tx/0x4b3047d376e9045aee86892616283012d44d1dca99defe016ad4dec50c9c273c>

2. `Attacker Wallet B` then sold 57 ETH for YAM and deposited 57 ETH and an equal amount of YAM into the Sushiswap pool [19:01 - 20:53 UTC]. It then deposited the returned SLP tokens into the Yam Incentivizer [21:12 - 21:28 UTC].  

   - These transactions can be seen here: <https://etherscan.io/txs?a=0x0de41bdc58ffaf4a8c1b7084a544fbbe10a9de56>

### July 8th 2022

`Attacker wallet B` traded some ShibDAO tokens. This seems totally unrelated and it seems to be the only transactions that didn't have something to do with YAM across the wallets studied.

### July 9th 2022

1. `Attacker wallet A` sends 11 ETH and then another 6 ETH to `Attacker wallet C`. It also sends 1 ETH to `Attacker Wallet D` [7:41 ` 8:30 UTC].

   - 11 ETH to `Attacker A`: <https://etherscan.io/tx/0x620ba6732f9a29d556fb2cb8006ed8cf817e6be8f50580083395928260dabc97>
   - 6 ETH to `Attacker A`: <https://etherscan.io/tx/0x60f927e8f8ab1ec9f86f49e168362778c0ad536513e4bf3be5a22141b2708009>
   - 1 ETH to `Attacker D`: <https://etherscan.io/tx/0x40c8964cc7eebaf6f899af288f93d6f28bd3b664f9e1e435c7fb7f49071533d4>

2. `Attacker Wallet C` trades half the 17 ETH for YAM in a 2 trades and deposits the ETH and YAM into the ETH/YAM Sushiswap LP pool [7:46 - 8:49 UTC].

   - <https://etherscan.io/address/0x3c749d3fce03ee5d7ff43ff09c9e07e9807e51f0>

3. `Attacker Wallet D` creates the `Attacker Contract` that is used to interact with the Yam Governor. Its contents are not verified [8:36 UTC].

   - <https://etherscan.io/tx/0x4bdd2ed7b9e560ed1e690ffa7cf9f5467f09460af098bdd970031ec2a3b8769c>

4. `Attacker Wallet B` and `Attacker Wallet C` send their LP tokens to the `Attacker Contract` [8:49 & 8:50 UTC].

   - `Attacker B`: <https://etherscan.io/tx/0xa03a438593495dcce673aa2349b249d3c67c1719b68ee7976a10ef16c29c13bc>
   - `Attacker D`: <https://etherscan.io/tx/0x0040285be4c3f184019e33f503b16f693053f72cef527ad5bf637659f4e4f29b>

5. `Attacker Contract` Deposits LP tokens into the YAM incentivizer contract [9:06 UTC].

   - <https://etherscan.io/tx/0x44c4304bf9f35e9ce71857a91e130bbae3bd6ca77ed1c1dcbabaa65bd78028b6>

6. `Attacker Wallet D` uses the `Attacker Contract` to create a new governor proposal and votes with 224739 BoU* YAM (equal to ~561,847 YAM) for the proposal. This reached quorum, which is 200,000 BoU YAM. The attacker was able to create the proposal and vote on it without these actions showing up as typical transactions on Etherscan, requiring a user to look at the internal transactions to see what was happening [9:08 and 9:09 UTC].

   - Propose: <https://etherscan.io/tx/0xc5e4dcfa927d099ffd12de2d6d5fb6ebb2d6ba2d6522a9adc36b5196e0ca0391/advanced>
   - Vote: <https://etherscan.io/tx/0x60a4f4020bae19044eabfa2be0518a489935d285dddced5c5a01d335fc95caf3/advanced>

7. After voting, the `Attacker Contract` removes its SLP tokens from the contract and sends them to `Attacker Wallet B`. [9:15 - 9:21 UTC]

   - withdrawal: <https://etherscan.io/tx/0xdeec7d26e9bb29282fc79541794a2ce1fe847227981cc845e8084f5d0d1c0dfb>
   - Send: <https://etherscan.io/tx/0x7c517ee1f9a177a7282c3f0c9da27ffd029f8ee373298883811294e69c9d5668>

8. `Attacker Wallet B` unwinds the SLP tokens and sells the YAM for ~50.7 ETH. [9:22 - 9:28]

   - Unwind SLP: <https://etherscan.io/tx/0xa0525aac2ed0c46c2a77c01ed15a88cdfee3dbc53939b6f563c54399eff86262>
   - Swap 1: <https://etherscan.io/tx/0xf5dbd43952c79e991569f3923d4a656d35f1cbc6ea89e6d938b2fc50d6a0ede3>
   - Swap 2: <https://etherscan.io/tx/0xa9261bbcdabb806e1f436e1789e5acc320573cb98f16416f220f05d1fcf8c212>

9. Members of the YAM Guardian multi-sig were alerted to some suspicious activity with the YAM governance contracts by members of the Ethereum Security community on the morning of July 9th (EST time). The both that announces governance proposals on discord also recorded the proposal. Because the proposal contained unverified and unknown code, it was deemed potentially malicious and the options to stop the proposal were reviewed. Because the proposer had removed their LP token (see step 7 above) before the conclusion of the vote, it was now possible to cancel the proposal. Proposers must maintain the proposal threshold amount of voting power (50k BoU YAM) throughout the entire voting process. You can see the code for this here: <https://github.com/yam-finance/yamV3/blob/0f61c94230bf6c44d4d06188a53c45832f84cae7/contracts/governance/YamGovernorAlpha.sol#L346>. The proposal was cancelled at 12:41 UTC in the following transaction:

   - <https://etherscan.io/tx/0x978bfae45894866fae12fa759a4ee9ca8ff8af58e158ada4b2be440cbdcd0a4a>

At this point the governance attack was over. Over the next few hours the attacker proceeded to sell all their YAM for ETH, which they then send to Tornado Cash from `Attacker Wallet B`. 

## Conclusion

This attack was successfully thwarted with the help of the Ethereum Security community, the existing YAM infrastructure, quick work from the YAM Guardians, and with help from mistakes by the attacker. The Guardian Multi-sig has still never needed to be used, but it is ready to protect the YAM treasury if needed.

These attacks are an unfortunate consequence of an open, permissionless, and decentralized system and we should continue to be vigilant and consider all the attack vectors that the DAO faces. This is another datapoint that supports the value of a robust on-chain governance system and as we evolve the system in the future we can use these lessons to make sure the DAO treasury remains safe.

Many thanks to everyone who helps fend off this attack.

:heart: :rocket: :sweet_potato:

---

footnote: BoU stands for Balance of Underlying and was used in rebasing. It is no longer used, but many functions in the contracts still use this number. The ratio of BoU YAM to normal YAM is very close to 1:2.5.