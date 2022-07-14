# Broad Treasury Framework

## Introduction

Given the creation of a new Treasury Management and Maintenance Silo, it is time to take another look at the way the DAO uses the treasury and how it allocates funds. I strongly believe that the DAO must answer the big questions about how it wants to use the treasury before we can get maximum value out of any rebalancing strategy, no matter how advanced or easy for anyone to use. While I believe that the work that Feddas intends to do on a rebalancing framework is valuable, I do not believe that it can answer all the questions that we need answered to make fully informed decisions about the treasury. His work, as I understand it, creates the infrastructure needed to rebalance the treasury based on a specific risk strategy, but does not define that risk strategy and is not opinionated about the assets the treasury holds outside of what the numbers dictate.

This document will give my thoughts on the direction that the DAO should go in with regard to treasury management and how the treasury should be used to support the mission of the DAO. My [prior work on this topic](https://forum.yam.finance/t/yam-treasury-management-framework/1511) has influenced by thoughts overall, but since writing my prior analysis and [YIP-80](https://forum.yam.finance/t/yip-80-yam-treasury-rebalancing/1512), I have changed some of my thought process. I am aware that as I write this there is going to be a vote on [whether the treasury should be redeemable](https://forum.yam.finance/t/yip-110-treasury-redemption-re-vote/1700), and while that would undoubtedly change the size, and potentially the makeup of the treasury, I hope that the main goals and principles that are laid out below will still hold.

## DAO Goals and Treasury Goals

The YAM Re-Org that I have been working on for the last few months is a change to the operational structure of the DAO, mainly focused on how contributors request funding for projects and then show the work that they have done in order for YAM token holders to determine whether the work should continue. This is a framework for getting work done accountably and efficiently, and while it is neutral in what kind of work can be done using the framework, the design choices for the framework are rooted in very specific needs of the DAO and a desire to keep it open and ultimately directed by YAM token holders.

When I first started working on the Re-Org, I called it Minimal YAM, as the goal was to limit the reliance on any single set of participants, such as a core team, and instead make a minimized DAO in which governance and decision making were the core roles of DAO participants and the actual work done on projects is pushed out to project teams that are funded by the DAO. The impetus of this change is the lack of participation that is evident in YAM and other DAOs and an over-reliance by token holders on a core team to fulfill their wishes. Because YAM has never had a clearly defined and agreed upon mission, this led to confusion among contributors and voters about the roles and responsibilities of each group.

The beauty of this new minimal, Re-organized YAM is that it lets token holders focus on what they want the mission of YAM to be and then execute that vision through the newly created funding mechanism. The Re-Org itself cannot define that and so it needs to be defined separately. This clears up the confusion between voters and contributors as they both add to the conversation about what the vision and mission are, but it is ultimately the voters who decide. If contributors don't agree then they can choose not to participate.

The treasury suffers from a similar confusion. A rebalancing framework will only solve one half of the equation. The other half includes questions that can only be answered by YAM voters:

- What assets should we hold?
- What role do those assets play?
- Why do we hold them?
- If the treasury needs to rebalance and there are multiple ways to do it, which assets do we sell, which do we buy?

While the fact that the treasury has not been rebalanced in a while is partially because parts of the rebalancing process require calculating some parameters that require some specialized knowledge, as well as limitations with our swapping contracts, if the need to rebalance had been clear and imperative, someone would have figured out how to do it. I am not convinced that the treasury asset allocations are still in the best interest of the DAO, and so rebalancing blindly into assets that no longer make sense for the DAO is not something that made sense figuring out how to do. An easier rebalancing plan may not lead to a better outcome in the long run unless we figure out the mission.

## Investment Strategy

### The DAO treasury should not be an investment vehicle

The DAO diversified its treasury into a few different opportunities in the past, and all of them have either been publicly available ones, or have relied on special opportunities unique to the DAO. Examples of the publicly available investment opportunities are farming INDEX with DPI and ETH, and investing funds in Yearn vaults. Anyone could have deployed their own capital in these strategies and done equally well. Examples of special opportunities are the YAM incentivizer which pays out YAM rewards and claims Sushi rewards, and UMA farming and dApp rewards. The incentivizer was built on the DAO's ability to issue tokens,(It has already dried up) and is not long term sustainable. The UMA rewards came from building synths and a partnership with UMA. Without the building side, this opportunity would not exist.

Furthermore, Yam DAO has no track record or history of gaining access to private investment opportunities. I see no reason why this would change in the future. Given this fact, without building, YAM has no edge over the broader market with investments. This makes YAM a poor proxy investment over simply investing individually in the same assets. It also leads to confusion around the DAO's obligations to token holders regarding redemption of the treasury.

### Aggressive Yield Farming is Risky

This probably goes without saying these days, but achieving outsized returns from yield farming without significantly increasing risk requires a lot of research and due diligence on the opportunities to assure that they are safe. In a bull market there was still significant risk, but the high yields potentially offset it. In a bear market the yields have dropped considerably and the risk has not. The risk adjusted return on yield farming, unless you have a significant edge is high. Considering our treasury is also used to support the building side of the DAO, this risk is compounded.

### Building is the best way for YAM to succeed

As I mentioned in the section above, the only investment opportunities that the DAO was able to take advantage of that were no public were those that it built out. This leads to the conclusion that, in the long run, YAM is best suited either focusing on building standalone products or a hybrid where we build products that the treasury can then invest in. The hybrid model is interesting because many of the projects that we have worked on in the past need bootstrapping liquidity and the treasury is able to help with that.

### Designing a Treasury around a 'Building' or Hybrid Model

A treasury strategy focused on building products and/or then investing in those products should look different from one that is focused on generating yield. It should be more conservative and focused on where funds are allocated. Runway requirements should be clearly defined and adhered to. Simplicity and clarity should be prioritized and it should be understood that the high upside long-shots are not coming from financial investments but investments in contributors and DAO funded projects.

Like the Organizational Re-Org, a treasury Re-Org should also focus on making a simple system that fulfills the needs of the DAO. How simple is always a moving target, but I would focus on a few areas:

- Minimize the number of different assets as much as possible to still meet mission requirements. This will help in simplifying rebalancing parameters.
- Minimize complexity of yield strategies for those assets.
- Categorize the different functional parts of the treasury to be able to reason about parts separately from the whole.
- Set up clear guidelines for important metrics like runway.

Making the treasury management strategy simpler will allow for more complex structures to be built on top of it (i.e. yield distribution to voters) and will also make the rebalancing process easier to understand and implement.

## The Current State of the Treasury

### Composition

The current composition and size of the treasury can be seen here: <https://dune.com/ethedev/Yam-Dashboard>
A google sheet of the treasury can also be found here. Numbers are not as current as the dune dashboard, but there is additional granularity: 

For our purposes, the most important information is that the treasury is made up of (In order of $ value):

- USDC (deposited in Yearn) - ~50%
- ETH (some deposited in Yearn, some not) - ~30%
- DPI (some LPing and some in treasury) - ~12%
- UMA, INDEX, SUSHI, GTC - ~8%

The existing treasury rebalancing strategy doesn't target percentages, but generally, a 33% USDC, 33% ETH, 33% Other breakdown comes close to the targets. As you can see by this metric we are heavy on USDC and light on "other"/ Defi Assets.

At the time when the original treasury allocation was done, it made a lot of sense to hold some of these assets:

- DPI, as a Defi basket, originally allowed us to continue to align with the communities that we originally distributed tokens to. It could also be put to use farming INDEX tokens. But over the last year, we have not had any interaction or support from the DeFi products in the index, and the DPI/ETH farm has been retired by IndexCoop. The price correlation between DPI and ETH, while not exact is similar enough that DPI does not add significant diversification to the treasury. The same can be said for WBTC.

- UMA was earned and farmed with the YAM Synths product. This is the closest we have to an actual partnership as we have in the past had a good relationship with UMA and they have supported us. But this is contingent upon the Yam Synths products, which are on hold until someone comes to work on them. Of the DeFi assets, this is the one that I would most support holding on to. I have also been part of a new initiative to [actively use the UMA to vote and earn voting rewards](https://forum.yam.finance/t/report-on-voting-with-uma/1694).

- INDEX was farmed and holding it made sense if we were going to build on set protocol (as envisioned with YAM Treasuries). But that project is on hold and we do not participate in Index governance or Metagovernance. Due to limitations with our swapping contracts, it is difficult for the DAO to sell the INDEX tokens in the treasury without significant (20%+) slippage. It could be sold effectively using the multi-sig or code that calls aggregator contracts from within one of the monthly contracts.

- SUSHI was earned from our incentivizer and at the time was a no-brainer to farm. The DAO essentially traded out YAM for Sushi tokens and have used their AMM platform for almost 2 years. The founding of Sushi was intertwined with YAM and their initial front-end designs were heavily inspired by the first YAM front-end. But in the 2 years since then, the connection between the 2 DAOs has fallen off and they just decided to [liquidate their YAM Treasuries Vault](https://forum.sushi.com/t/sushihouse-funds-redemption/10783). Looking to the future, we may move to a different AMM solution for our liquidity needs as they evolve. I have recently [proposed balancer](https://forum.yam.finance/t/a-more-refined-plan-for-protocol-owned-liquidity/1684) due to the ability to create skewed pools and use those tokens in governance.

- GTC was an airdrop, and while I feel aligned with the mission, it is not being actively used, nor is there any attempt at collaboration with Gitcoin.

### Runway

With $1.75M in USDC, and a rough burn rate of ~30K-35K per month in contributor pay, the DAO has a 50 month (~4 year) runway at current burn rate. This may seem overly generous, but it should be noted that the DAO has significantly reduced its payroll in the last few months. A year ago the burn rate was closer to $60k a month, which would amount to closer to a 2 year runway. While I am not advocating to ramp up the number of contributors we currently pay, I want to note that if things go well, we may have a larger burn rate in the near future.

### Yield Farming

Current and upcoming yield generation comes from Yearn vaults. The rates on the USDC vaults has dropped in the last year and they sit around 1-2%. Some ETH is currently in the stETH Vault , which is yielding around 4% (in ETH), which is historically good for ETH and should be pretty consistent into the future. Other than that the Treasury UMA could earn a 10-20% return (in UMA) from DVM votes, but this will need to be tracked going forward.

## A simplified Treasury Strategy

I propose the following treasury strategy as a starting point for discussion:

### New Composition

Split treasury into 2 broad categories: general funds and partnership funds.

- General funds consist of a simple rebalancing 2 asset allocation of ETH (or stETH) and USD (yvUSDC) held 50:50 with a rebalance that happens any time the skew crosses a certain threshold (i.e. 20% or 60/40). A minimum USDC quantity would be set based on runway needs. This number could be set intermittently based on expected or prior burn rates. ETH would provide exposure to the wider DeFi and NFT ecosystem without requiring decisions about which assets to purchase. On a long timescale, ETH has proven to be generally correlated with DeFi and NFT assets on aggregate and provides the DAO with significant treasury upside while being aligned with the DAO's mission. ETH is the "easy answer".

- Partnership Funds consist of project tokens for which the DAO has a committed relationship. The definition of this partnership would need to be determined and should be done so to err on the side of only investing in projects that we plan to actively build on or with. These funds would have be capped with a maximum % of the whole treasury. If that percentage were exceeded they would be sold for either ETH or USDC in the next rebalance. THese assets would not get bought in rebalances and would not be considered in the calculations. New partnership purchases would need to be voted on by YAM governance.

### New Composition by the Numbers

I propose that we limit the assets in the treasury to (yv)USDC, (yvst)ETH, YAM and YAM LP tokens, and UMA (as a partnership asset). 

In order to reach a roughly 50/50 ETH/USDC ratio in the treasury, we would liquidate our DPI, INDEX, SUSHI, and GTC holdings into ETH. This would bring the treasury ETH percentage into the high 40s%. UMA is only about 3.5% of the treasury and we could set the max allocation to 5% of the total treasury. The UMA would be actively voted with to earn yield.

The treasury would be rebalanced at any point the skew between ETH and USDC passes 20% (60/40) to limit rebalances to save on both trading fees and costs to unwind positions and trade. I am open to more granular or targeted metrics using volatility, beta, etc, but this simpler composition may negate the need for more advanced metrics to rebalance. 

This strategy does not require any particular ratio of funds. I am proposing 50/50 because it feels good to me at a "gut" level. If we wish to keep the existing risk numbers, those could be input for these assets, which would most likely mean we hold more ETH and less USD. I am more interested in simplifying the assets the treasury holds than determining the exactly numbers.

The runway minimum, if calculated at 2 years using the average monthly contributor compensation over the last 6 months would come out to about $1MM USD if we assume a $40k/month in burn. This number would allow for either a more or less risky strategy. I personally would prefer a less risky strategy as I believe the value add for YAM will come from using the funds to build and a more risky strategy increases the risk that we will have less funds in the long run (even if it also increases the risk we will have more).

## Impact on future YAM development (Not in scope)

### Protocol Owned Liquidity

If we go forward with a protocol owned liquidity purchase using ETH, we could do that with the required amount ($200k-$300k) and then rebalance back to 50/50, buying some ETH with USDC. The YAM/ETH LP tokens would be held in the treasury. In the future, if [voting powers are given to 80:20 LP tokens](https://forum.yam.finance/t/a-more-refined-plan-for-protocol-owned-liquidity/1684) then these tokens can be used to pay contributors instead of YAM, but that is a conversation for another time.

### Treasury Yield Distribution

If we go forward with voters or token holders [earning yield from the treasury](https://forum.yam.finance/t/a-roadmap-for-yam-part-3-tokenomics/1570), the yvUSDC and yvstETH could both be deposited into Element Finance to split out the principal and yield tokens. The treasury would then hold the principal tokens and distribute the yield tokens as governance deems appropriate. This treasury strategy allows for a large percentage of the treasury to be used in yield distribution and doesn't require lots of complex accounting in the background.
