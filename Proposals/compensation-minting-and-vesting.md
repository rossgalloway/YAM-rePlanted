# Minting YAM to Pay Contributors and Vesting Implementation

## Summary

The YAM treasury does not enough YAM to pay contributors for this month. This proposal recommends minting YAM to pay contributors monthly as part of the on-chain transactions. Only the amount of YAM owed to contributors would be minted in these transactions, and a new vesting procedure, using [Sablier](https://sablier.finance/), would be implemented to further align incentives.

## Rationale

As discussed in [this post](https://forum.yam.finance/t/yip-107-vesting-pool-sunset-migration-and-mint/1631) and subsequent snapshot vote, 370,000 new YAM was minted to make up for the YAM trapped in the original Vesting Pool contract. 

The current balance in the treasury is 100,280, which will not cover this upcoming month's payroll obligations of ~130,000 YAM. There are a few options to proceed:

1. Mint as needed to meet payroll on a monthly basis.
2. mint a large lump sum and try to estimate how much is needed to meet a certain time frame.
3. Pay entirely from the treasury (either in USDC or another asset, or my trading an existing treasury asset to YAM).

This proposal puts forward option 1 as the preferred choice. 

Option 1 negates the need to guess as how much YAM needs to be minted (an impossible task to get right) and constrains the maximum quantity to be a function of the treasury size. It focuses the discussion not on whether minting YAM is good or bad, but whether the contributions of contributors is worthwhile (option 3 also has this trait). It allows token holders fine grained control over how much YAM is created via the grants approval process. Unlike option 3, it limits treasury burn. I wrote more about why this is preferable [here](https://forum.yam.finance/t/the-dao-must-mint-more-yam/1680#contributor-compensation-3).

To limit new tokens reaching the market quickly, and also aligning contributor incentives, I recommend adding a vesting component to the contributor compensation packages using [Sablier smart contracts](https://sablier.finance/). These are simple vesting contracts that can have any ERC-20 deposited and will vest the tokens linearly for a predetermined period of time. A 6 month vesting period is proposed.

## Specification

If this proposal is passed, the following process would be carried out:

1. Total YAM contributor compensation amounts would be determined monthly by the Gov-Ops Council based on approved grant proposals and grant payment requests, based on the 30 day TWAP for the month in which the work was carried out. 
2. This amount would be minted in the monthly on-chain transaction by calling the `mint()` function on the YAM token contract for the amount determined in step 1.
3. The newly minted YAM would be sent to the monthly proposal contract, where it would be deposited into new sablier streams for each contributor. Each contributor would receive only 1 stream, even if they have multiple grants. The function to call on the [sablier.sol](https://github.com/sablierhq/sablier/blob/6ccec84f5d61c64dd981aa28b5c831fe491f90ab/packages/protocol/contracts/Sablier.sol#L179) contract is `createStream()` passing through the following parameters:
   - Grant recipient address
   - amount to deposit
   - token address (YAM)
   - start time (set at least 7 days after the expected vote proposal call to the governor so that this timestamp happens after the execution of the contract, in unix time) 
   - end time (set 6 months after the start time, in unix time)

If this proposal is not passed this month then no YAM will be paid this month. The owed amounts will be recorded on github and backpay will be included in the next month's on-chain proposal.

## Out of Scope

The minting of YAM for any purpose other than contributor compensation is out of scope of this proposal.

## Poll to measure sentiment

[insert poll]