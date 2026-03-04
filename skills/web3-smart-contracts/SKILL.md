---
name: web3-smart-contracts
description: When the user wants to write Solidity smart contracts, use Hardhat/Foundry, test blockchain deployments, or audit token economics. Trigger on "web3", "smart contract", "Solidity", "Hardhat", "Ethereum", "blockchain".
category: backend
profile: dev
---

# Web3 & Smart Contracts

> Methodologies for writing gas-efficient, highly secure Solidity smart contracts and rigorous testing pipelines using Foundry or Hardhat.

## When to Use

- "Write an ERC-20 token contract with a tax mechanism."
- "Review this Solidity code for reentrancy vulnerabilities."
- "Create a Hardhat test suite for an NFT marketplace."
- "How do I upgrade smart contracts using proxy patterns?"
- "Optimize the gas usage of this mapping structure."

## Before Starting

Ask context-gathering questions if not provided:

1. **Toolchain:** Do they prefer Hardhat (JavaScript/TypeScript) or Foundry (Solidity tests)?
2. **Network:** Is this targeting Ethereum mainnet, an L2 (Arbitrum/Optimism), or a custom EVM chain? (Gas strategies differ).
3. **Standards:** Are we modifying standard OpenZeppelin templates (ERC20, ERC721, ERC1155)?

## Core Framework

### 1. Smart Contract Security

| Vulnerability        | Remediation                                                                                             | Anti-Pattern                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Reentrancy**       | Implement the Checks-Effects-Interactions (CEI) pattern; use OpenZeppelin's `ReentrancyGuard` modifier. | Sending Ether before updating the internal balance mapping.                         |
| **Integer Overflow** | Native protection exists in Solidity >=0.8.0. For older versions, use SafeMath.                         | Assuming multiplication will never exceed `uint256`.                                |
| **Access Control**   | Use `Ownable` or `AccessControl` for administrative functions.                                          | Leaving sensitive setter functions `public` without `require(msg.sender == admin)`. |
| **Front-Running**    | Use commit-reveal schemes for sensitive logic or rely on flash-bot protected RPCs.                      | Exposing raw slippage bounds in decentralized exchanges without deadlines.          |

### 2. Gas Optimization

| Optimization           | Do                                                                                               | Don't                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| **Storage (SSTORE)**   | Pack multiple small variables (e.g., `uint8`, `bool`) into a single 256-bit storage slot.        | Declare a `bool`, then a `uint256`, then a `bool` (wastes 2 slots).                         |
| **Memory vs Calldata** | Use `calldata` for read-only function arguments (arrays, strings).                               | Default to `memory` for array inputs that are never modified.                               |
| **Caching State**      | Read a state variable once into a local memory variable if iterating or checking multiple times. | Continually read `stateArray[i]` directly from storage in a `for` loop.                     |
| **Custom Errors**      | Use `error CustomError();` and `revert CustomError();` (Solidity >=0.8.4).                       | Use long string literals in `require(condition, "Very long error message that costs gas")`. |

### 3. Testing Patterns (Hardhat/Foundry)

| Testing Approach      | Best Practice                                                                                | Anti-Pattern                                                            |
| --------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **Unit Tests**        | Write tests for 100% of Happy Paths and all intentional `revert()` paths.                    | Only testing the success scenario.                                      |
| **Fuzzing (Foundry)** | Use `vm.assume()` to bound fuzzing inputs to realistic values and catch edge case overflows. | Manually writing 5 test cases and hoping they cover numeric bounds.     |
| **Mainnet Forking**   | Test against cloned mainnet state when interacting with live protocols (Uniswap, Aave).      | Trying to deploy mock DeFi protocols locally instead of simply forking. |

## Output Format

When generating Solidity code or Web3 advice, structure your response as follows:

1. **Architecture/Rationale**: A brief explanation of the patterns used (e.g., "Using UUPS proxy pattern for upgradeability").
2. **The Contract Code**: The Solidity file(s) adhering to the latest pragmas.
3. **The Test Suite**: The corresponding Hardhat (`.ts`) or Foundry (`.t.sol`) test file.
4. **Security Callout**: Highlight any specific security considerations the user must manually verify.

## Common Mistakes

- ❌ **Inventing crypto primitives**: Writing custom hashing or signature verification instead of using standard, audited OpenZeppelin libraries.
- ❌ **Ignoring the CEI Pattern**: (Checks-Effects-Interactions) Making external calls to untrusted contracts before updating local state variable balances.
- ❌ **Upgradability Traps**: Using constructors `constructor()` in proxy implementations instead of `initialize()` functions.
- ❌ **Floating Pragma**: Pushing production code with `pragma solidity ^0.8.0` instead of a locked version like `pragma solidity 0.8.20`.

## Related Skills

- **tdd-workflow**: Use for general testing concepts and assertions.
- **vulnerability-scanner**: Use when the focus is general application security (OWASP) rather than EVM-specific logic.
