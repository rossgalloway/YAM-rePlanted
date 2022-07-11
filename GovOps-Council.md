{%hackmd theme-dark %}


# The Governance and Operations Council (GOC)



### ❗ New Name, who dis?


## Role within YAM

The Gov-Ops Council has 3 main roles within the DAO:

1. To facilitate and guide the high level operation of YAM, to help vet and fund Silos, Grants, and other projects. In this role it is not a gatekeeper. It makes recommendations and interpretations of the rules as ratified by the governance process. One could think of it like YAM’s version of a standards compliance body, which does not make standards, but reviews whether they are met and may also interpret and clarify them.
2. The second role is to create and execute on-chain transactions from approved governance proposals. This is a functional and oversight role. Common, simple transactions and actions that the DAO performs on a regular basis are included in this role, as well as reviewing and calling other contracts that may be created by project silos. A preliminary list of pre-approved proposal actions are:

    - paying out approved grants.
    - replenishing multi-signature wallets when approved by governance.
    - depositing and removing treasury assets from Yearn Vaults.
    - swapping treasury assets via existing Uniswap V2 compatible contracts. (Other exchanges and protocols require additional smart contract work.)
    - Interacting with UMA EMP contracts.
    - Depositing and removing UMA tokens from UMA 2-key Escrow Contracts.

    All other proposal actions are subject to a case by case review and should be expected to be out of scope of the Gov-Ops council. As new code is written for specific use cases, the above list may expand.

3. Maintanence of existing YAM infrastructure and systems including, but not limited to:
    - The YAM website and on-chain voting Dapp.
    - The YAM snapshot page.
    - The YAM Discourse server.
    - The YAM Discord server
    - The YAM Telegram channel.
    - YAM documenation repositories.
    - the YAM github organization, repos, and other infrastructure used to facilitate working with those repos (Netlify, etc).
    - Moderation of all of the above.

## Goals

The goals that the Governance council should aim to achieve are:

1. Facilitate the governance process and assure that it is clear, legible, fair, and accessible, and give an opinion one whether that the standards approved by the DAO are being followed in any given proposal.
2. Coordinate on-chain transactions and assure that interactions with the treasury run smoothly. Implement and execute routine monthly proposals.
3. Review code written by Silos that will interact with the treasury and vet for security and accuracy. It is not the responsibility of the Gov-Ops council to provide audits or extensively review code created by others, although they may provide best practices and advice based on their knowledge of the existing YAM codebase and functions.

## Scope of Work

### Code and Smart Contracts

- Routine, pre-approved interactions with the YAM governance contracts and treasury should be the main scope of work for the developers putting together the on-chain transactions. What defines a “routine” transaction should be defined and publicly stated with “off the shelf” code that can be plugged into the contract. Testing the contract also falls into this scope. See the list in the second bullet point of the "role within YAM" section of this document.
- Code that falls outside of the prior "off the shelf" classification is the responsibility of the Silo or Grantee that is requesting its inclusion. They should write and test the required code and either implement it in their own deployed contract that can be called by the monthly on-chain transaction, or they should coordinate with the Gov-Ops silo to include it directly into the main proposal contract.
- High level review of new code and tests, and coordination of how it comes together is part of the scope of the Gov-Ops Council.
- Successful Execution of on-chain contracts, including calling any additional functions on contracts after the governance and proposal contracts are executed.

### Governance Coordination

Communicate with applicants and community members to clarify the process to apply for funding from YAM.

Make recommendations about the completeness of applications for funding. The Council is not empowered to judge the merit of a proposal, but should give guidance on whether the application is complete and follows approved standards.

Manage bookkeeping and governance flows. Collate approved consensus actions into one location used as a source of truth for creating on chain execution transactions.

Communicate with different Silos about their expected needs and outline requirements to get their transactions included within the monthly on-chain proposal contracts.

## Structure

Unlike a typical project or silo, with deliverables and completion parameters, the YAM governance process is ongoing. It is a process that needs to be managed and maintained. The Gov-Ops council is not building the governance process, but stewarding it. If the governance process grinds to a halt then many of the projects or silos that rely on it will be negatively affected. These requirements mean that it needs to be designed to be resilient.

- It should not rely on on any 1 person or group of persons. The information needed to do this work should be available publicly and the expertise to do it should be available in the wider market.
- It should be directly accountable to token holders with term limits and clear mechanisms to remove members.
- It should be accountable to and policed by other members as possible.
- It should be sized to allow for the work to be done effectively and coordination between the different members to happen easily.

An elected set of members with pre-set terms meets these criteria. Given the limited number of qualified applicants, setting limits on terms seems unrealistic at this time, but the requirement to be re-nominated and ratified gives governance an opportunity to move the council in a different direction intermittently.

A 3 or 5 member council seems like a good starting point. It should contain at least 1 developer (2-3 preferable) who can coordinate, write, and review the monthly on-chain transactions. The other members should focus on coordinating the governance process and information as well as communicating to the wider community about what is going on.

Due to the nature of the work, this council should be compensated based on an estimated/expected workload and reference rates. At the start of a term for a new Gov-Ops Council, the scope of work is defined and a baseline amount of time to work on each scope item is defined. The amount determined by the expected hours to be worked and the pay rate will determine the base payout to each member. If members work additional hours to perform their expected duties then they can apply to governance with documentation of the work to be paid for those extra hours worked.

---

:heart: :rocket: :sweet_potato:

Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
