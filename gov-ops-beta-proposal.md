# Gov-Ops Council Creation (Beta Test)

## Introduction

Part of the YAM Re-Org that we have been working on in the last few months includes the creation of a new advisory group of contributors who are empowered to help run and streamline the operations and governance of the DAO. This group would have a limited scope of powers intended to make it easier for token holders and grant applicants to perform their required tasks to make the new system run smoothly.

I have put together a full write-up on the scope and responsibilities of this new group, from here on called the Gov-Ops Council, in this document: <https://github.com/rossgalloway/YAM-rePlanted/blob/master/GovOps-Council.md>

Building on this document, I am proposing that the DAO implement an initial beta version of this council to start performing these tasks and working out the kinks and what scope may or may not need to be added. I want to be clear that this would be a temporary measure while the complete specification for the group is worked out. Implementing the grants model with the current contributors while we continue to work it out has been very helpful in understanding where the pain-points are for the process, and I expect similar benefits from this working implementation.

## Beta Implementation

The proposed beta implementation would begin with 3 members: @Ross, @Feddas, and @0xE. They will be responsible for the scope of work laid out in the linked document above (under scope of work). Since we do not have the full nomination and voting model worked out, I propose the following addendum to that document:

Each of the above members will present the scope of work that they intend to fulfill within the Gov-Ops council and the expected amount of time they expect to spend on that work, with a not-to-exceed amount. Initial term to be 2 months (to align with the quarterly periods) and each member will get a separate snapshot vote to ratify their membership.

## Member Roles

### Ross

I expect my roles to be the following, which is an extension of what I already do for the DAO:

- Communicate with applicants and community members to clarify the process to apply for funding from YAM.
- Make recommendations about the completeness of applications for funding. 
- Manage bookkeeping and governance flows. Collate approved consensus actions into one location used as a source of truth for creating on chain execution transactions.
- Communicate with different Silos about their expected needs and outline requirements to get their transactions included within the monthly on-chain proposal contracts.
- Review monthly on-chain transaction and vet them for security and accuracy to the best of my ability. Coordinate with 0xE on what needs to go into them.
- Maintenance and moderation of the following infrastructure
   - Discord server
   - Discourse server (forum)
   - Minor maintenance of the main website (https://yam.finance)

**Time Commitment**: 20 hours a month expected. Not to exceed 40 hours a month. Hours to be recorded and accounted for in monthly transparency reports. 

---

### 0xE

I expect my roles to be the following, which is an extension of what I already do for the DAO:

- Routine, pre-approved interactions with the YAM governance contracts and treasury, including:  

   - paying out approved grants.
   - replenishing multi-signature wallets when approved by governance.
   - depositing and removing treasury assets from Yearn Vaults.
   - swapping treasury assets via existing Uniswap V2 compatible contracts. (Other exchanges and protocols require additional smart contract work.)
   - Interacting with UMA EMP contracts.
   - Depositing and removing UMA tokens from UMA 2-key Escrow Contracts.


- Maintenance of existing YAM infrastructure and systems including:

   - The YAM website and on-chain voting Dapp.
   - The YAM snapshot page.
   - The YAM Discord server
   - The YAM Telegram channel.
   - the YAM github organization, repos, and other infrastructure used to facilitate working with those repos (Netlify, etc).

- High level review of new code and tests, and coordination of how it comes together
- Successful Execution of on-chain contracts, including calling any additional functions on contracts after the governance and proposal contracts are executed.
- [add more as required]


**Time Commitment**: 40 hours a month expected. Not to exceed 80 hours a month. Hours to be recorded and accounted for in monthly transparency reports. [adjust as needed]

---

### Feddas

I expect my roles to be the following:

- Communicate with applicants and community members to clarify the process to apply for funding from YAM.
- Make recommendations about the completeness of applications for funding.
- [add more as required]

**Time Commitment**: 15 hours a month expected. Not to exceed 30 hours a month. Hours to be recorded and accounted for in monthly transparency reports. [adjust as needed]

---

## Not in scope of Gov-Ops Council

- Code that falls outside of the prior "off the shelf" classification is the responsibility of the Silo or Grantee that is requesting its inclusion. They should write and test the required code and either implement it in their own deployed contract that can be called by the monthly on-chain transaction, or they should coordinate with the Gov-Ops silo to include it directly into the main proposal contract.

## Pay

Pay to be set at $85 per hour, split 50/50 between USDC and YAM.

## Specification

This document will be posted publicly on the YAM discourse forum for 1 week before voting begins. Each proposed member will get their own snapshot vote, to be posted and last at least 3 days after the completion of the review period.

Assuming acceptance of all 3 votes, work on the above scope will begin in August.

Simultaneously, @desiger and @ross will be getting feedback on the process and adding this information into new documentation and using it to craft the Gov-Ops Service Agreement, which will enshrine the roles and responsibilities of the council more concretely. Research into voting processes and standing up a voting front-end will also be worked on as part of the Gov-Ops silo work.

After the 2 months are up, we will review the state of the Gov-Ops council and process and adjust as needed in the next implementation.