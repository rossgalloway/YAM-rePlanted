# Yambassadors Silo - UMA Voting Counterproposal

| YGP-001.C01          |                                                        |
|------------------- |--------------------------------------------------------|
| Type               | YAM Grant Proposal (YGP)        |
| Purpose            | Allow YAM Treasury UMA to be voted with        |
| Authors            | Ross (ross@yam.finance)                                |
| Status             | Counter-proposal                                           |
| Created            | June 1st, 2022                                   |
| Link to Forum Post | insert                |

---

In the last few days, while doing further due diligence on the Yambassadors Silo and scoping the work to vote with treasury UMA tokens, I have come to the conclusion that the amount of work that is being represented as necessary and the time to do it is not in line with the work that is actually required.

The Scope of work and goals of the grant proposal are drawn from the following 2 posts, including the original grant proposal post. I will quote the relevant information, and the original posts and conversations are located here:
[Yambassadors silo proposal](https://forum.yam.finance/t/yambassadors-silo/1656)
[YIP-99 Delegate the UMA in our treasury to a contributor](https://forum.yam.finance/t/yip-99-delegate-the-uma-in-our-treasury-to-a-contributor/1577)

## YIP-99

To start, let's look at the original post that @Snake made about voting with UMA in [YIP-99](https://forum.yam.finance/t/yip-99-delegate-the-uma-in-our-treasury-to-a-contributor/1577).

In that post, the goals and specifications of the proposal are as follows:

>[quote="Snake, post:1, topic:1577"]
>
>**Abstract - What am I proposing?**
>
>* Utilize a voting 2key contract to delegate UMA to a contributor.
>* Incentivize this contributor to vote by splitting the rewards earned through voting correctly.

>[quote="Snake, post:1, topic:1577"]
>
>**Specifications - How am I proposing it is accomplished?**
>
>What would be required from a technical perspective to execute this proposal? If some work has already been done, detail that here, as well as make clear what will need to be accomplished in the future.
>
>1. Nominate a delegate.
>2. Have the delegate create a DesignatedVoting contract that has the owner set as the YamGovernorAlpha.
>3. On-chain transaction to transfers the UMA to the designated voting contract.

The goal of this proposal is to allow a 3rd party delegate to vote with the treasury UMA tokens. Also note the simplicity of the proposal. Discussion around implementation of the proposal was focused on who the delegate would be and not the creation of the contracts. There was no discussion of the time-frame or cost of doing the work to allow voting but based on the specifications, the effort required seems minimal.

There was positive sentiment at the time around @Snake being this delegate and doing this work but he turned the role down so the proposal was shelved.

## Yambassadors Silo

### Goals

Fast forward 5 months and @Snake proposed the [Yambassadors Silo](https://forum.yam.finance/t/yambassadors-silo/1656) with the following goals:

>[quote="Snake, post:1, topic:1656"]
>
>This is meant to be a long term silo with the mission of empowering yammers to guide the projects that are aligned with Yam to succeed as well. **However, in the short/medium term, the first project will entail getting UMA rewards for the treasury and securing the Optimistic Oracle.**

The grant proposal as written is for the bolded text above; The create the means for the DAO to delegate their UMA voting power to a 3rd party and earn the rewards. This is shown in the scope from the original proposal, as quoted below.

### Scope

The scope and specifications of the project were stated in the initial proposal as:

>[quote="Snake, post:1, topic:1656"]
>
>The scope of this grant is to cover the following.
>
>* Create a proposal contract that allows governance to interact with UMA’s DesignatedVotingFactory and create a new DesignatedVoting contract with governance as owner and me as the initial ambassador. Transfer 500 UMA from treasury to the voting contract.
>* Have the core/infrastructure team review the contract.
>* Deploy proposal contract on Ethereum.
>* Propose the contract to on-chain governance, queue and execute.
>* Participate in at least 1 UMA optimistic oracle vote or dispute.
>* Write a report on said vote and the implications if any to the DAO.
>* Propose governance call to return UMA tokens back to the treasury.


In subsequent posts. snake elaborated on the work to be done:

>**How do you expect the smart contracts to work?**
>
>The smart contract being referred to here is the proposal. The proposal contract would call >“newDesignatedVoting” on Uma’s deployed [DesignatedVotingFactory](https://etherscan.io/address/0xDE7c02aD2b925587Bd16724810f994a2948c4a38#code) setting the governance timelock as the owner, assign me as a voter via [setDesignatedVoting](https://etherscan.io/address/0xDE7c02aD2b925587Bd16724810f994a2948c4a38#writeContract) and tranfer a test amount of UMA.
>
>**What is the general use pattern for these contracts and how does the DAO interact with them?**
>
>It follows a delegation pattern so as the designated voter, I (or any future ambassador selected by the silo) would essentially just have to vote as a regular UMA voter. Whenever the DAO wants or otherwise needs the UMA assets back, then a proposal would go up calling WithdrawErc20 on the delegating contract.

The scope laid out above is very similar to that from YIP-99, with the only change being the language about creating a smart contract to interact with the designated voting factory. We will see later that this change is unnecessary to fulfull the goals of the proposal.

### Deliverables

The following deliverables, timeline, and milestones are from the original post with with added clarifications (in italics) from later posts added to them for clarity.

>The scope encompasses deliverables for the span of about 6 months. I am requesting 80K USD (70% Stable / 30% Yam at prev 30d TWAP of payment date) to be distributed evenly upon reaching the following milestones.
>
>1st milestone ~2 months
>
>* developing, testing and collaborating on the on-chain Yambassador proposal.
>* deploying Yambassador proposal contract on chain and proposing to governance.
>
>2nd milestone ~2 months
>
>* **successfully executing the proposal or reproposing if there is an issue.**
>
>   *To have completed the first milestone, I would have had to propose the transaction to create the designated voting contract, assign myself as the vote and the time lock as the owner, and transferred over a test amount of assets. In the event the proposal gets the votes and past the timelock but is unable to execute or an issue arises that does not allow the project to move forward… I’d have to debug the issue, have the changes reviewed and repropose a new tx to governance. This happened on [proposal 22](https://etherscan.io/address/0x79241fd23f74a5587d22e24795776159f5455569) just 3 months ago.*
>* **participating in governance, researching as needed.**
>
>   *This is referring to being an active participant in UMA’s governance process. This may mean engaging with other voters on UMA’s discord, engaging with proposals on their forums and in the case of disputes engaging with voters to try and assess what the community is leaning towards, and researching [UMIPS](https://docs.umaproject.org/uma-tokenholders/umips) to determine proper answer for disputes. This above and beyond just sitting down when a dispute arises to do the transactions but it includes that as well which could happen at any time during this time frame. While the milestone is to participate in just 1 dispute in order to mark this whole project a success, historically there have been more than just 1 vote a month.*
>* **creating a template for UMA voting disputes.**
>
>   *The template is meant to guide future Yambassadors on recording an opinion on a vote that was either interesting, controversial, purposefully wrong (voted in the minority for the purpose of aligning with the DAO). The most effective Yambassadors will go above and beyond “just voting” by putting out their opinions in which they based their vote on. This will help Yam DAO to evaluate the performance of Yambassadors.*
>
>3rd milestone ~2 months
>
>* developing, testing and collaborating on the on-chain Asset/Reward Retrieval proposal.
>* deploying Asset/Reward Retrieval and proposing to governance.
>* next steps write up for the silo and the silo treasury. Part of the write up will include a few hours to pass down lessons learned to a future Yambasassador.



# Understanding the scope of work

## Goals

In both above proposals, the goal is to **allow a 3rd party delegate to vote in UMA governance and oracle questions/disputes with the UMA tokens in the YAM treasury in order to earn voting rewards paid out by UMA for "correct" voting.** The Yambassadors silo proposal also mentions other future work to participate in other governance actions with treasury funds, but there are no specifics and it is not included in the scope of work for which compensation is requested. Also not included in the scope of work for compensation is ongoing voting with the treasury tokens after the contracts are deployed, tested, etc.

The sub-goals of this proposal as it is written are as follows:

1. Deploy the contracts necessary to allow a third party to vote in UMA governance with YAM treasury UMA tokens.
2. test any interactions with those contracts to assure they work correctly and as intended
3. Write documentation that helps future delegates and YAM governance participants understand and participate in UMA governance and continue to earn money via voting with treasury UMA tokens.

## Scope of Work

In order to complete these goals, the following steps need to be taken:

1. [optional] the DAO should determine who it wants to be its voting delegate for its UMA tokens. (This can be decided later if necessary)
2. An instance of UMA's 2-Key designated voting contract needs to be created with the correct YAM governance contract as the owner. The default parameter when creating this contract is that the contract creator will be set as the voting delegate.

     This is done by calling the newDesignatedVoting() function on the UMA [designatedVotingFactory](https://etherscan.io/address/0xDE7c02aD2b925587Bd16724810f994a2948c4a38#writeContract) contract and entering the [YAM timelock contract](https://etherscan.io/address/0x8b4f1616751117c38a0f84f9a146cca191ea3ec5) in the address field. This can alternately be done using the UMA voting dApp at <https://vote.umaproject.org>

    Once this contract is created, it can be checked according to these instructions: <https://docs.umaproject.org/uma-tokenholders/voting-2key#recommended-verify>

3. The DAO should then send a test transaction to the contract with a test amount of UMA (i.e. 1 UMA) in order to confirm that the contract works. This can be done as part of one of the monthly on-chain transactions.

    The code to be added to the monthly contract is a simple ERC-20 transfer to the 2-key contract and would look like this:

    ```javascript
    IERC20 internal constant UMA = IERC20(0x04Fa0d235C4abf4BcF4787aF4CF447DE572eF828);

    UMA.transfer(TwoKeyContractAddress, testAmount*(10**18));
    ```

    the code used to propose the transaction would look like this:

    ```javascript
    targets[2] = address(reserves);
    signatures[2] = "whitelistWithdrawals(address[],uint256[],address[])";

    address[] memory whos = new address[](1);
    uint256[] memory amounts = new uint256[](1);
    address[] memory tokens = new address[](1);

    whos[0] = address(proposal);
    amounts[0] = testAmount*(10**18);
    tokens[0] = address(UMA);

    calldatas[2] = abi.encode(whos, amounts, tokens);

4. once the UMA has been sent, the delegate should confirm that they can vote with the contract, claim rewards to the contract, etc. This can all be done via the UMA voting dApp at https://vote.umaproject.org.

5. After confirmation that the contract works for the voter, The DAO should submit a new on-chain transaction that confirms that the UMA and rewards can be removed from the contract by the DAO.

   the code used to propose the transaction would look like this:

   ```javascript
   targets[0] = address(TwoKeyContractAddress);
   signatures[0] = "withdrawErc20(address,uint256)";
   calldatas[0] = abi.encode(address(UMA), testAmount*(10**18));
    ```
   
   The DAO could do this more efficiently by sending one amount of UMA over (step 3) and then in the same transaction send back another, smaller amount of UMA to confirm that the withdraw function works as intended. This would remove the need to wait for a second on-chain transaction to test the withdraw function and still allow the delgate to test the contract.

6. The DAO can choose to change the delegate at this point. It would do so by calling a different function on the 2-key contract called resetMember() with the new delegate in the address field and `1`  in the roleId field. The code would look like this:

    ```javascript
   targets[0] = address(TwoKeyContractAddress);
   signatures[0] = "resetMember(uint256, address)";
   calldatas[0] = abi.encode(1, address(newDelegate));

After the above 6 steps, goals 1 and 2 listed above are complete. In the next transaction, the balance of the UMA in the treasury can be transferred to the 2-key contract per step 3. The work then left to do is to complete goal 3 by writing the documentation required to facilitate future voting and use of these contracts in order to earn the treasury UMA.

# Determining the amount of time required to complete the above scope of work

When the above steps are complete, the goals listed in the Yambassador Silo proposal and YIP-99 will have been completed. Considering the code to make the transactions is written above, that leaves the creation of the contract, testing, and the documentation left as the significant scopes of work still to be completed.

## Creating the voting contract

Creating the 2 key voting contract does not take a significant amount of work, and to show this I went ahead and created the contract. You can view it here: <https://etherscan.io/address/0x8348c5ec31d486e6e4207fc0b17a906a0806550d>.

I encourage all readers to confirm that the YAM timelock address is the owner (role 0) and my public wallet (0x88c868b1024ecaefdc648eb152e91c57dea984d0) is the delegate/voter (role 1). The voter role can be changed in the future if the DAO desires.

## Testing the voting contract

Now that the 2-key contract has been created, we can use the code in the scope of work section and send 1 UMA to the contract, and then remove 0.5 UMA as part of the next on-chain proposal. It should be tested with the rest of the proposal.

Once the UMA is in the contract, the delegated voter can test that voting works and retrieve rewards using the UMA voting dApp. In the following on-chain transaction the DAO can test removing the funds and change the voting address if desired. I expect the voting and testing to take a few hours, and adding the code to test removing the funds is part of scope that we already pay a developer for.

## Documentation

That leaves the documentation as the final step of the process that requires completion. How to deploy the contract has been documented above, so we can clean that up and re-use it. I have also written a document [here](https://yamdao.notion.site/UMA-Voting-Process-b7f4fe824ecb4b648457bca2360c9a0b). We still need to include documentation and procedures around voting on UMA votes, but most of this documentation is already made by UMA:

 <https://docs.umaproject.org/uma-tokenholders/voting-2key>
<https://docs.umaproject.org/uma-tokenholders/voter-dApp>
<https://docs.umaproject.org/uma-tokenholders/uma-holders>

I don't expect this document to take more than a day to put together. It can be published to the YAM github repo with the rest of the documentation about using UMA to vote so that it can be found in the future.

### Summing it up

So adding this all up, we have a bunch of work that is already done and took a few hours to complete, the upcoming work that is included in the scope of work that we already pay a dev for, and a few hours of work on my part to test and document. I fail to see how this scope of work could ever be estimated to cost $80,000 or take 6 months to complete. The final ability for the DAO to vote with all the treasury UMA will take a few months to come about if we limit our on-chain votes to the monthly ones, but the scope of work and required working hours are much less than that. It could be completed much faster if we submitted additional on-chain proposals.

Contrary to the assertions made in the Yambassadors proposal, there are no complex smart contracts that need to be written, nor significant engineering work that needs to be done. I have done most of the code work described above and deployed the contracts and I am not a developer. It took me a few hours and some conversations with other developers including @ethe.

YAM has consistently overpaid and under-received for the much of the work that has been done on its behalf and it is time to take a stand against this. The new model that @designer, @chilly, and I are working on is a step forward in building a more robust and accountable DAO. But this new model relies on all of us to be vigilant and vet the proposals that are submitted. We all need to do a better job of looking into these proposals to make sure the DAO is getting good value for the money that it pays.

# A Counter Proposal

*edited 2022.06.02*

While I agree with the overall goals of the Yambassadors Silo, I do not think that YAM should pay $80,000 for the scope of work included in the original grant proposal for it. I strongly recommend that the DAO reconsider the approval of the initial grant to fund the Yambassador Silo and either create a new vote to reject it, or get a significantly changed scope of work.

As a counter-offer, I submit the following proposal to do an equivalent scope of work (detailed in the "understanding the scope of work" section above) with the following next steps:

* I have already created a working 2-key contract and provided the basic code to interact with it via on-chain transactions. I will coordinate with @ethe to will send a test amount of UMA (est. 2 UMA) to the contract in the upcoming on-chain transaction as well as send some of the UMA (est. 1 UMA) back to the treasury. This will test both sending and retrieving.
* With the UMA left in the contract, I will vote on an UMA vote and confirm it works.
* I will create documentation around UMA voting best practices and link to the relevant existing documents. I will publish this to the forum, and coordinate with having it added to github and other documentation resource locations for the DAO.
* Upon completion of the prior steps and barring any issues, we will send the balance of the treasury UMA to the 2-key voting contract in the following on-chain transaction (July)
* I will submits a proposal to be the UMA delegate and to vote on behalf of the DAO as part of my monthly moderation and operational duties. (I will formalize this in the future in my work proposals). If the DAO would prefer someone else to be the delegate then I will coordinate with @ethe to change the voting address to the person who is chosen

All the above work will be completed at no added cost to the DAO beyond our existing commitments and any Ethereum gas costs will be submitted as re-imbursables. While we are still working on determining how to structure compensation moving forward, everything listed generally falls into the current scopes of work for which @ethe and I are paid and or can be rolled into existing duties.

Because the price of "existing duties" is somewhat vague, I will break down what I expect it to take and what it would cost if done as a stand-alone project:

#### My time

- Prior work to deploy 2-key contract and research - 4 hours
* prior general scope of work research - 8 hours
* code writing to include in on-chain transaction - 8 hours
* UMA vote testing - 4 hours
* Documentation - 16 hours

my Estimated Total: 40 hours of work * 70/hr = $2,800.00

#### Other Time

* @ethe code deployment. Not entirely sure on the actual time, but I will guess 8 hrs added to each of the 2 on-chain votes to test.

@ethe Estimated Total: 16 hours of work * 70/hr = $1,120.00

Add in contingencies, and expectations that everything takes longer than expected (~25%) and we come to about **$5,000 in expected cost to do this work in 2 working hour weeks (80 hours)**.

The work is intermittent so the date at which I expect the work to be completed will depend on on-chain transaction timings, but should be done by mid July if we meet the above schedule. Meeting this schedule will require that we include the test send and retrieve in this month's proposal.

<br>

---

Copyright and related rights waived via [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
