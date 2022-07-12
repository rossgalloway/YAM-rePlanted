⚠️WIP⚠️

# Treasury and Token

A comprehensive strategy for conceptualizing the interplay between the DAO, treasury, and token in a sane way.

## Different Pieces

### Token

The token is not a financial instrument, even though it may have value, be used in "financial ways." The token is a tool to make decisions in a way that is not determined by any specific set of actors (other than the token holders themselves). Rewards are not paid for owning tokens, but for using those tokens productively within the system with which they live. For YAM, this is either participating in governance or performing some other important function like providing liquidity in an AMM.

The token has value because the organization has value and people need to use it to participate. This is the same reason that an asset like ETH has value. There is an expectation that people will want to use the network in the future and therefor speculators buy it with the intention to sell it to them later.

Buying YAM now is rational for 2 reasons: Use and speculation. If you want to participate in governance then it makes sense that you buy tokens to do so (use). Buying more tokens get you additional say in the system. You can also work and earn tokens. THe other reason is speculation and it is predicated on the fact that there will be more use in the future. Those who are speculating on the token may have no interest in using it, but are instead looking to sell it to people who want to use it in the future.

There is nothing wrong with speculation, but it needs to be accounted for and there are risks that speculators can warp the economics of the system in unpredictable ways.

### Treasury

The main use of the Token is as a communal key to the treasury. This is its core function, even though it can also be used to make decisions on things that do not directly touch the treasury. Its binding functionality is to interact with the treasury.

There is no explicit direction for how token holders should use, deploy, or steward the treasury written into the core contracts of the DAO. Determining this must occur on the social layer first, and then may or may not be implemented on the technical (contract) layer. 

This social layer uses the token to make decisions about how the DAO should operate and how those who participate in the organization should operate. The social layer is as binding as the rules and ability of the operators of the organization choose to make it. The DAO can live with an anything goes attitude (code is law) or a more strict interpretation. Either works, but the interpretation must be understood by all parties. Problems occur when different parties expect the organization to work in different ways.

### DAO

The DAO is simply the combination of the Token holders and the Treasury and the interplay between them. The DAO may use assets (website, discord, etc) to simplify and extend these interactions, but those are tools and not really parts of the DAO itself.

## Treasury as a Common Good

I like to think of the treasury as something that sprung into existence in a sort of immaculate conception. Where did the money come from? Well, that is legitimately complicated. It came from minting and selling tokens during positive rebases in the beginning of the DAO, when there still was a rebase. The sales were with the uniswap AMM pool, so everyone who had tokens in the pool sold to the DAO. This was a truly communal, algorithmic fund raise.

Now, many people didn't like this fund raising mechanism as it had a destabilizing effect on the YAM price, and it was stopped after a few months by turning off the rebasing mechanism. But those funds in the treasury had already been raised and there was no attempt to claim those funds at the time as the economics of a redemption didn't make sense (treasury value was below token market-cap). But this was the point when a treasury redemption could at least have been legitimately proposed.

Now, over a year and a half later, the price of the YAM token is lower, the value of the treasury is higher than the token market cap, and there is discussion of redemptions. But a redemption now would be at the expense of long term holders of YAM tokens. No one who purchased tokens in the last year and a half has played any part in generating the treasury.

### Finding Neutrality

Trying to unravel this knot and find an equitable solution is an impossible task. Someone is going to get screwed no matter what. There is an easy solution though. Token holders can choose to make the treasury non-redeemable and instead function as a common good, controlled by token holders but never directly redeemable outside of work done for the DAO.

Neutrality and Equality are subjective conditions that depend on viewpoint and context. One must declare how one wants to be equal or neutral, and then consider whether that condition impacts equality it other situations.

Using an AMM as the only way to acquire and sell tokens is neutral since the conditions in which different parties can do so is purely determined by market forces.

## implementation

This change would decrease the attack surface of the DAO while clarifying how the treasury should be used. It would equalize all token holders, giving them the same rights and ability to extract value from the DAO. They can either earn some of the treasury by doing work approved by token holders or they can sell their tokens on the open market.

Enforcing non-redeemability would be difficult to do on a code and contract level, but it could be enforced quite easily by the Guardian multi-sig. A signalling vote would express intent to dis-allow redemption indefinitely. This would still only be a socially enforceable initiative, but it would set a precedent put the onus of persuasion on those who wish to redeem.