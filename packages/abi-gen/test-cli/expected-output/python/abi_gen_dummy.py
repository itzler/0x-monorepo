"""Generated wrapper for AbiGenDummy Solidity contract."""

# pylint: disable=too-many-arguments

import json
from typing import (  # pylint: disable=unused-import
    List,
    Optional,
    Tuple,
    Union,
)

from mypy_extensions import TypedDict  # pylint: disable=unused-import
from hexbytes import HexBytes
from web3.datastructures import AttributeDict
from web3.providers.base import BaseProvider

from zero_ex.contract_wrappers._base_contract_wrapper import BaseContractWrapper
from zero_ex.contract_wrappers.tx_params import TxParams


class InnerStructDescription(  # noqa: E501 (line too long)
    TypedDict
):
    """Python representation of a tuple or struct."""

    inner_struct: SomeBytesAnIntegerADynamicArrayOfBytesAString  # noqa: E501 (line too long)

    description: str

class SomeBytesAnIntegerADynamicArrayOfBytesAString(  # noqa: E501 (line too long)
    TypedDict
):
    """Python representation of a tuple or struct."""

    some_bytes: bytes

    an_integer: int

    a_dynamic_array_of_bytes: List[bytes]

    a_string: str


# pylint: disable=too-many-public-methods
class AbiGenDummy(BaseContractWrapper):
    """Wrapper class for AbiGenDummy Solidity contract."""

    def __init__(
        self,
        provider: BaseProvider,
        contract_address: str,
        private_key: str = None,
    ):
        """Get an instance of wrapper for smart contract.

        :param provider: instance of :class:`web3.providers.base.BaseProvider`
        :param contract_address: where the contract has been deployed
        :param private_key: If specified, transactions will be signed locally,
            via Web3.py's `eth.account.signTransaction()`:code:, before being
            sent via `eth.sendRawTransaction()`:code:.
        """
        super().__init__(
            provider=provider,
            contract_address=contract_address,
            private_key=private_key,
        )

    def _get_contract_instance(self, token_address):
        """Get an instance of the smart contract at a specific address.

        :returns: contract object
        """
        return self._contract_instance(
            address=token_address, abi=AbiGenDummy.abi()
        )

    def simple_require(
        self,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying, same-named contract method.

        :param tx_params: transaction parameters

        """
        func = self._get_contract_instance(
            self.contract_address
        ).functions.simpleRequire(
        )
        return self._invoke_function_call(
            func=func,
            tx_params=tx_params,
            view_only=True
        )

    def ecrecover_fn(
        self,
        _hash: bytes,
        v: int,
        r: bytes,
        s: bytes,
        tx_params: Optional[TxParams] = None,
    ) -> str:
        """Execute underlying, same-named contract method.

        :param tx_params: transaction parameters

        """
        func = self._get_contract_instance(
            self.contract_address
        ).functions.ecrecoverFn(
            _hash,
            v,
            r,
            s
        )
        return self._invoke_function_call(
            func=func,
            tx_params=tx_params,
            view_only=True
        )

    def revert_with_constant(
        self,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying, same-named contract method.

        :param tx_params: transaction parameters

        """
        func = self._get_contract_instance(
            self.contract_address
        ).functions.revertWithConstant(
        )
        return self._invoke_function_call(
            func=func,
            tx_params=tx_params,
            view_only=True
        )

    def simple_revert(
        self,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying, same-named contract method.

        :param tx_params: transaction parameters

        """
        func = self._get_contract_instance(
            self.contract_address
        ).functions.simpleRevert(
        )
        return self._invoke_function_call(
            func=func,
            tx_params=tx_params,
            view_only=True
        )

    def nested_struct_output(
        self,
        tx_params: Optional[TxParams] = None,
    ) -> InnerStructDescription:
        """Execute underlying, same-named contract method.

        :param tx_params: transaction parameters

        """
        func = self._get_contract_instance(
            self.contract_address
        ).functions.nestedStructOutput(
        )
        return self._invoke_function_call(
            func=func,
            tx_params=tx_params,
            view_only=True
        )

    def require_with_constant(
        self,
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying, same-named contract method.

        :param tx_params: transaction parameters

        """
        func = self._get_contract_instance(
            self.contract_address
        ).functions.requireWithConstant(
        )
        return self._invoke_function_call(
            func=func,
            tx_params=tx_params,
            view_only=True
        )

    def struct_input(
        self,
        s: SomeBytesAnIntegerADynamicArrayOfBytesAString,  # noqa: E501 (line too long)
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying, same-named contract method.

        :param tx_params: transaction parameters

        """
        func = self._get_contract_instance(
            self.contract_address
        ).functions.structInput(
            s
        )
        return self._invoke_function_call(
            func=func,
            tx_params=tx_params,
            view_only=True
        )

    def simple_pure_function_with_input(
        self,
        x: int,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying, same-named contract method.

        :param tx_params: transaction parameters

        """
        # safeguard against fractional inputs
        x = int(x)
        func = self._get_contract_instance(
            self.contract_address
        ).functions.simplePureFunctionWithInput(
            x
        )
        return self._invoke_function_call(
            func=func,
            tx_params=tx_params,
            view_only=True
        )

    def simple_pure_function(
        self,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying, same-named contract method.

        :param tx_params: transaction parameters

        """
        func = self._get_contract_instance(
            self.contract_address
        ).functions.simplePureFunction(
        )
        return self._invoke_function_call(
            func=func,
            tx_params=tx_params,
            view_only=True
        )

    def nested_struct_input(
        self,
        n: InnerStructDescription,  # noqa: E501 (line too long)
        tx_params: Optional[TxParams] = None,
    ) -> None:
        """Execute underlying, same-named contract method.

        :param tx_params: transaction parameters

        """
        func = self._get_contract_instance(
            self.contract_address
        ).functions.nestedStructInput(
            n
        )
        return self._invoke_function_call(
            func=func,
            tx_params=tx_params,
            view_only=True
        )

    def struct_output(
        self,
        tx_params: Optional[TxParams] = None,
    ) -> SomeBytesAnIntegerADynamicArrayOfBytesAString:
        """Execute underlying, same-named contract method.

        :param tx_params: transaction parameters

        """
        func = self._get_contract_instance(
            self.contract_address
        ).functions.structOutput(
        )
        return self._invoke_function_call(
            func=func,
            tx_params=tx_params,
            view_only=True
        )

    def pure_function_with_constant(
        self,
        tx_params: Optional[TxParams] = None,
    ) -> int:
        """Execute underlying, same-named contract method.

        :param tx_params: transaction parameters

        """
        func = self._get_contract_instance(
            self.contract_address
        ).functions.pureFunctionWithConstant(
        )
        return self._invoke_function_call(
            func=func,
            tx_params=tx_params,
            view_only=True
        )
    def get_event_event(
        self, tx_hash: Union[HexBytes, bytes]
    ) -> Tuple[AttributeDict]:
        """Get log entry for Event event.

        :param tx_hash: hash of transaction emitting Event event
        """
        tx_receipt = self._web3_eth.getTransactionReceipt(tx_hash)
        return (
            self._get_contract_instance(self.contract_address)
            .events.Event()
            .processReceipt(tx_receipt)
        )

    @staticmethod
    def abi():
        """Return the ABI to the underlying contract."""
        return json.loads(
            '[{"constant":true,"inputs":[],"name":"simpleRequire","outputs":[],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"hash","type":"bytes32"},{"name":"v","type":"uint8"},{"name":"r","type":"bytes32"},{"name":"s","type":"bytes32"}],"name":"ecrecoverFn","outputs":[{"name":"signerAddress","type":"address"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"revertWithConstant","outputs":[],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"simpleRevert","outputs":[],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"nestedStructOutput","outputs":[{"components":[{"components":[{"name":"someBytes","type":"bytes"},{"name":"anInteger","type":"uint32"},{"name":"aDynamicArrayOfBytes","type":"bytes[]"},{"name":"aString","type":"string"}],"name":"innerStruct","type":"tuple"},{"name":"description","type":"string"}],"name":"","type":"tuple"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"requireWithConstant","outputs":[],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"components":[{"name":"someBytes","type":"bytes"},{"name":"anInteger","type":"uint32"},{"name":"aDynamicArrayOfBytes","type":"bytes[]"},{"name":"aString","type":"string"}],"name":"s","type":"tuple"}],"name":"structInput","outputs":[],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"x","type":"uint256"}],"name":"simplePureFunctionWithInput","outputs":[{"name":"sum","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"simplePureFunction","outputs":[{"name":"result","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"components":[{"components":[{"name":"someBytes","type":"bytes"},{"name":"anInteger","type":"uint32"},{"name":"aDynamicArrayOfBytes","type":"bytes[]"},{"name":"aString","type":"string"}],"name":"innerStruct","type":"tuple"},{"name":"description","type":"string"}],"name":"n","type":"tuple"}],"name":"nestedStructInput","outputs":[],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"structOutput","outputs":[{"components":[{"name":"someBytes","type":"bytes"},{"name":"anInteger","type":"uint32"},{"name":"aDynamicArrayOfBytes","type":"bytes[]"},{"name":"aString","type":"string"}],"name":"s","type":"tuple"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"pureFunctionWithConstant","outputs":[{"name":"someConstant","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"param","type":"uint8"}],"name":"Event","type":"event"}]'  # noqa: E501 (line-too-long)
        )

# pylint: disable=too-many-lines
