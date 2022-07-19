# Time Weighted Payout Vesting Contract

## Abstract

An UMA-style contract that pays out additional collateral every day that it isn’t redeemed, up to a maximum amount. Base payout amount is the “unvested” YAM payment that can be claimed immediately by settling the contract. Settling returns the unvested collateral to the treasury*. The longer the paid party waits to redeem their tokens the more tokens they get, up to a certain contract defined amount.

## Details

### Creating the Contract

This contract would work just like (and maybe just be) a UMA long-short pair contract. Because each contract would need to be individually expirable, each would need to be it's own LSP contract with individualized parameters. This contract would be created by the paying party and collateral tokens deposited into it, creating equal number of long and short tokens. The paying party would then distribute the "long" token to the payee and keep the short tokens in the treasury.

### Permissions

The contract should be written so that only specific addresses can expire the contract (i.e. the owner, set to the recipient’s address). This could be something only the paid party can do, but governance could be allowed to as well in certain circumstances. The Payee is always assured they will get the lower bound payment, so if the vesting is set right then governance only has limited power to punish or claw back funds.

These contracts could be traded or sold by changing the settling address (owner) to a new address and sending the "long" tokens to that address. The new owner would now have the ability to settle the contract and redeem the funds. 

### Retrieving Funds

Calling `settle()` from the owner address requests a resolution from the Optimistic Oracle, which should only ask for whether the address belongs to the current owner and the current time, and then calculate the value of the token split at that point. This is simple to verify as correct.

Governance could have a separate permission that also allows them to expire the contract but calling this function from governance would create a disputable transaction that gets sent to full DVM mechanism. The voters of the DVM then review the evidence provided that the payee breached the contract. If the dispute fails, the payee receives the full payout. If the dispute succeeds then the price settles at the value from the time of calling settle and returns funds proportionally.

### Collateral Asset

The collateral asset is the asset in which the payee would be paid. It should be able to be any ERC-20 token. Because the contract never needs to know the price of the collateral, only the time, it should be safe to put any asset in this contract (although I'm unsure about rebasing assets and other non-standard tokens).

## Using it for YAM

This contract could be used by the DAO to create an payment model for YAM tokens that has "best of both worlds" properties. It provides vesting but also gives the payee the opportunity to claim payment at any time, in return for giving up their "bonus".

YamDAO has been committed to paying out enough value in stablecoins to (hopefully) allow the payee to not need to sell the YAM to pay expenses. But true vesting has been a contentious issue, and our previous implementation was more like vesting theater than real vesting. This model allows for both, with a built-in incentive for contributors to hold their tokens through the vesting period to maximize their payout.

This mechanism can also be complemented with DAO Controlled Liquidity (DCL) programs by paying out contributors in 80/20 YAM/ETH LP tokens instead of in pure YAM tokens. Unclaimed tokens from early vestings would go back into the treasury to be distributed in the future. While vesting, these tokens would contribute to DCL, and when redeemed could be locked directly into governance contracts, if we switch to an LP based system.

## Specifications

### MVP

New UMA LSP contract creation template for a owner-only settle-able contract that takes in the time of settlement and returns the value of long and short tokens based on starting parameters and amount of time left until full vesting.

### Added Functionality

- Ability for DAO governance address to settle the contract, but not without full DVM resolution on the validity of the settlement.
  - This needs to define the rules for which governance can legitimately settle the contract early and turn them into a form that the UMA DVM can validate and rule on.
  - confirm the game theory around allowing the DAO to settle early. Can someone with enough DAO voting power push through a settlement dispute, have it fail, and then get the full vested amount immediately?

- Use with LP tokens. I don't think this requires any additional contract functionality, but does require that the DAO figure out how it wants to do it.

- If we want to allow vesting tokens to be used in governance while still vesting, then we need to figure out how that would work. Each vesting contract would be unique so this couldn't just be a simple incentivizer.

---

### Footnotes

*Actual mechanism here is that the funds deposited into the contract are divided by a time based function, written into the contract. The paid party receives a token that represents their share at the current time and the treasury gets a token that represents the rest. When the market is settled and these parameters are defined, the respective parties can deposit their tokens for the underlying tokens, together summing to 100%.

---

:heart: :rocket: :sweet_potato:

Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
