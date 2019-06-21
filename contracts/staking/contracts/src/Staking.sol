/*

  Copyright 2018 ZeroEx Intl.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

*/

pragma solidity ^0.5.5;

import "./wrappers/MixinStakeWrapper.sol";
import "./wrappers/MixinStakeBalancesWrapper.sol";
import "./wrappers/MixinPoolsWrapper.sol";
import "./wrappers/MixinEpochWrapper.sol";
import "./wrappers/MixinRewardsWrapper.sol";
import "./wrappers/MixinFeesWrapper.sol";
import "./wrappers/MixinExchangeWrapper.sol";
import "./wrappers/MixinZrxVaultWrapper.sol";
import "./wrappers/MixinRewardVaultWrapper.sol";


contract Staking is
    MixinExchangeWrapper,
    MixinZrxVaultWrapper,
    MixinRewardVaultWrapper,
    MixinEpochWrapper,
    MixinRewardsWrapper,
    MixinStakeBalancesWrapper,
    MixinStakeWrapper,
    MixinPoolsWrapper,
    MixinFeesWrapper
{

    // this contract can receive ETH
    function ()
        external
        payable
    {}
}
