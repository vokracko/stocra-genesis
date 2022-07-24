from typing import ClassVar, cast

from genesis.blockchain.bitcoin.parser import BitcoinParser
from genesis.blockchain.exceptions import UnknownScriptPubKey
from genesis.blockchain.litecoin.adapter import LitecoinNodeAdapter
from genesis.blockchains import Blockchain
from genesis.currencies import Currency
from genesis.logging import get_logger

logger = get_logger(__name__)


class LitecoinParser(BitcoinParser):
    BLOCKCHAIN: ClassVar[Blockchain] = Blockchain.LITECOIN
    CURRENCY: ClassVar[Currency] = Currency.LITECOIN
    node_adapter: LitecoinNodeAdapter

    async def _decode_address_from_script_pub_key(self, script_pub_key: dict) -> str:
        script_type = script_pub_key["type"]

        if script_type in ["multisig", "pubkey", "witness_mweb_pegin", "witness_mweb_hogaddr"]:
            result = await self.node_adapter.decode_script(script_pub_key["hex"])
            segwit_addresses = result.get("segwit", dict()).get("addresses", [])

            if len(segwit_addresses) == 1:
                return segwit_addresses[0]

            assert set(result.keys()).issubset(
                {"asm", "desc", "type", "p2sh", "segwit", "reqSigs", "addresses"}
            ), f"keys are {result.keys()}"
            return cast(str, result["p2sh"])

        raise UnknownScriptPubKey(script_type)
