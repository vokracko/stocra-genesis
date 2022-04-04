# pylint:disable=too-many-lines

from decimal import Decimal

from genesis.models import CurrencyInfo, TokenInfo

TOKENS = {
    "0x0000000000004946c0e9f43f4dee607b0ef1fa1c": TokenInfo(
        currency=CurrencyInfo(symbol="CHI", name="Chi Gastoken"), scaling=Decimal("1e-0")
    ),
    "0x0000000000085d4780b73119b644ae5ecd22b376": TokenInfo(
        currency=CurrencyInfo(symbol="TUSD", name="TrueUSD"), scaling=Decimal("1e-18")
    ),
    "0x0000000000095413afc295d19edeb1ad7b71c952": TokenInfo(
        currency=CurrencyInfo(symbol="LON", name="Tokenlon"), scaling=Decimal("1e-18")
    ),
    "0x0000000000b3f879cb30fe243b4dfee438691c04": TokenInfo(
        currency=CurrencyInfo(symbol="GST2", name="GasToken"), scaling=Decimal("1e-2")
    ),
    "0x00000000441378008ea67f4284a57932b1c000a5": TokenInfo(
        currency=CurrencyInfo(symbol="TGBP", name="TrueGBP"), scaling=Decimal("1e-18")
    ),
    "0x000000085824f23a070c2474442ed014c0e46b58": TokenInfo(
        currency=CurrencyInfo(symbol="NRM", name="Neuromachine Eternal"), scaling=Decimal("1e-18")
    ),
    "0x00000100f2a2bd000715001920eb70d229700085": TokenInfo(
        currency=CurrencyInfo(symbol="TCAD", name="TrueCAD"), scaling=Decimal("1e-18")
    ),
    "0x00006100f7090010005f1bd7ae6122c3c2cf0090": TokenInfo(
        currency=CurrencyInfo(symbol="TAUD", name="TrueAUD"), scaling=Decimal("1e-18")
    ),
    "0x0000852600ceb001e08e00bc008be620d60031f2": TokenInfo(
        currency=CurrencyInfo(symbol="THKD", name="TrueHKD"), scaling=Decimal("1e-18")
    ),
    "0x001f0aa5da15585e5b2305dbab2bac425ea71007": TokenInfo(
        currency=CurrencyInfo(symbol="IPSX", name="IP Exchange"), scaling=Decimal("1e-18")
    ),
    "0x001fc4a7f2f586596308091c7b296d4535a25a90": TokenInfo(
        currency=CurrencyInfo(symbol="HUBS", name="Hubscop"), scaling=Decimal("1e-18")
    ),
    "0x0020d80229877b495d2bf3269a4c13f6f1e1b9d3": TokenInfo(
        currency=CurrencyInfo(symbol="DEXM", name="Dexmex"), scaling=Decimal("1e-18")
    ),
    "0x002f0b1a71c5730cf2f4da1970a889207bdb6d0d": TokenInfo(
        currency=CurrencyInfo(symbol="YD-BTC-MAR21", name="YD-BTC-MAR21"), scaling=Decimal("1e-18")
    ),
    "0x002f2264aeec71041ae5739ecf0a2c80c5ea30fa": TokenInfo(
        currency=CurrencyInfo(symbol="FEX", name="ForesterX"), scaling=Decimal("1e-18")
    ),
    "0x003e0af2916e598fa5ea5cb2da4edfda9aed9fde": TokenInfo(
        currency=CurrencyInfo(symbol="BSD", name="Basis Dollar"), scaling=Decimal("1e-18")
    ),
    "0x003ffefefbc4a6f34a62a3ca7b7937a880065bcb": TokenInfo(
        currency=CurrencyInfo(symbol="RTD", name="Robot Trading Token"), scaling=Decimal("1e-18")
    ),
    "0x005f977f633d1c23748294671b0e69f3512e6702": TokenInfo(
        currency=CurrencyInfo(symbol="TRYL", name="Lirasis TRY"), scaling=Decimal("1e-2")
    ),
    "0x006bea43baa3f7a6f765f14f10a1a1b08334ef45": TokenInfo(
        currency=CurrencyInfo(symbol="STX", name="Stox"), scaling=Decimal("1e-18")
    ),
    "0x0073e5e52e2b4fe218d75d994ee2b3c82f9c87ea": TokenInfo(
        currency=CurrencyInfo(symbol="22X", name="22X Fund"), scaling=Decimal("1e-8")
    ),
    "0x0081220d4feef7c333bb3e8f67f0bc09afba6fcb": TokenInfo(
        currency=CurrencyInfo(symbol="S.CX", name="Sprint"), scaling=Decimal("1e-8")
    ),
    "0x0089659f609933d16a5cd6c2be1a5dca1abe24ad": TokenInfo(
        currency=CurrencyInfo(symbol="DRINK", name="DrinkChain"), scaling=Decimal("1e-18")
    ),
    "0x009c43b42aefac590c719e971020575974122803": TokenInfo(
        currency=CurrencyInfo(symbol="BIX", name="Bibox Token"), scaling=Decimal("1e-18")
    ),
    "0x009e864923b49263c7f10d19b7f8ab7a9a5aad33": TokenInfo(
        currency=CurrencyInfo(symbol="FKX", name="Knoxstertoken"), scaling=Decimal("1e-18")
    ),
    "0x00a8b738e453ffd858a7edf03bccfe20412f0eb0": TokenInfo(
        currency=CurrencyInfo(symbol="ALBT", name="AllianceBlock"), scaling=Decimal("1e-18")
    ),
    "0x00ad22ab1006fc282674887aff1114e5ad14077d": TokenInfo(
        currency=CurrencyInfo(symbol="PRSTX", name="PRESTO"), scaling=Decimal("1e-18")
    ),
    "0x00b8b059f132009e5a812f27cc42733d135915df": TokenInfo(
        currency=CurrencyInfo(symbol="CYBG", name="Cyborg"), scaling=Decimal("1e-18")
    ),
    "0x00c4b398500645eb5da00a1a379a88b11683ba01": TokenInfo(
        currency=CurrencyInfo(symbol="EXC", name="Eximchain"), scaling=Decimal("1e-18")
    ),
    "0x00c83aecc790e8a4453e5dd3b0b4b3680501a7a7": TokenInfo(
        currency=CurrencyInfo(symbol="SKL", name="SKALE"), scaling=Decimal("1e-18")
    ),
    "0x00d1793d7c3aae506257ba985b34c76aaf642557": TokenInfo(
        currency=CurrencyInfo(symbol="TACO", name="Tacos"), scaling=Decimal("1e-18")
    ),
    "0x00e150d741eda1d49d341189cae4c08a73a49c95": TokenInfo(
        currency=CurrencyInfo(symbol="INF", name="Infinitus Token"), scaling=Decimal("1e-18")
    ),
    "0x00ea6f91b00e080e816f1bb2fad71b0fe1528983": TokenInfo(
        currency=CurrencyInfo(symbol="VN", name="VCOIN"), scaling=Decimal("1e-18")
    ),
    "0x00fc270c9cc13e878ab5363d00354bebf6f05c15": TokenInfo(
        currency=CurrencyInfo(symbol="VNXLU", name="VNX Exchange"), scaling=Decimal("1e-18")
    ),
    "0x010c282118aa76174ce5952572ba715cf60a0c9b": TokenInfo(
        currency=CurrencyInfo(symbol="VINX", name="VINX COIN STO"), scaling=Decimal("1e-18")
    ),
    "0x010d14d36c3ea6570d240ae3ac9d660398f7c48e": TokenInfo(
        currency=CurrencyInfo(symbol="XCF", name="Cenfura Token"), scaling=Decimal("1e-18")
    ),
    "0x011a105076791f654282daa392d48cc9b77757af": TokenInfo(
        currency=CurrencyInfo(symbol="V.CX", name="Visa Inc"), scaling=Decimal("1e-8")
    ),
    "0x01217729940055011f17befe6270e6e59b7d0337": TokenInfo(
        currency=CurrencyInfo(symbol="VETH", name="Vether"), scaling=Decimal("1e-18")
    ),
    "0x0128e4fccf5ef86b030b28f0a8a029a3c5397a94": TokenInfo(
        currency=CurrencyInfo(symbol="FSP", name="FlashSwap"), scaling=Decimal("1e-18")
    ),
    "0x012ba3ae1074ae43a34a14bca5c4ed0af01b6e53": TokenInfo(
        currency=CurrencyInfo(symbol="TRUMP", name="YUGE"), scaling=Decimal("1e-18")
    ),
    "0x013ae307648f529aa72c5767a334ddd37aab43c3": TokenInfo(
        currency=CurrencyInfo(symbol="sBNB", name="Synth sBNB"), scaling=Decimal("1e-18")
    ),
    "0x01409455883e2c1c4f7e32e2af85e547b14903c1": TokenInfo(
        currency=CurrencyInfo(symbol="FIV1.CX", name="Five Below Inc"), scaling=Decimal("1e-8")
    ),
    "0x0142c3b2fc51819b5af5dfc4aa52df9722790851": TokenInfo(
        currency=CurrencyInfo(symbol="PYN", name="Paycent"), scaling=Decimal("1e-18")
    ),
    "0x014a543f767b3b06e31a811b0a75483ee8dfd72d": TokenInfo(
        currency=CurrencyInfo(symbol="BNZ", name="BonezYard"), scaling=Decimal("1e-18")
    ),
    "0x014b50466590340d41307cc54dcee990c8d58aa8": TokenInfo(
        currency=CurrencyInfo(symbol="ICOS", name="ICOS"), scaling=Decimal("1e-6")
    ),
    "0x015df42d36bc851c7f15f80bd1d4e8dbf02aed0c": TokenInfo(
        currency=CurrencyInfo(symbol="XCON", name="Connect Coin"), scaling=Decimal("1e-18")
    ),
    "0x016396044709eb3edc69c44f4d5fa6996917e4e8": TokenInfo(
        currency=CurrencyInfo(symbol="KXC", name="KingXChain"), scaling=Decimal("1e-18")
    ),
    "0x0168703872fa06741ecaa9dff7803168e83f7ae0": TokenInfo(
        currency=CurrencyInfo(symbol="MIRO", name="Mirocana"), scaling=Decimal("1e-8")
    ),
    "0x016bf078abcacb987f0589a6d3beadd4316922b0": TokenInfo(
        currency=CurrencyInfo(symbol="RSPT", name="Rari Stable Pool Token"), scaling=Decimal("1e-18")
    ),
    "0x016ee7373248a80bde1fd6baa001311d233b3cfa": TokenInfo(
        currency=CurrencyInfo(symbol="BEAR", name="3X Short Bitcoin Token"), scaling=Decimal("1e-18")
    ),
    "0x017b584acfd16d767541ae9e80cdc702f4527b0b": TokenInfo(
        currency=CurrencyInfo(symbol="ASY", name="ASYAGRO"), scaling=Decimal("1e-18")
    ),
    "0x018d7d179350f1bb9853d04982820e37cce13a92": TokenInfo(
        currency=CurrencyInfo(symbol="INX", name="InMax"), scaling=Decimal("1e-8")
    ),
    "0x0198f46f520f33cd4329bd4be380a25a90536cd5": TokenInfo(
        currency=CurrencyInfo(symbol="PLA", name="PlayChip"), scaling=Decimal("1e-18")
    ),
    "0x01b23286ff60a543ec29366ae8d6b6274ca20541": TokenInfo(
        currency=CurrencyInfo(symbol="BMP", name="Brother Music Platform"), scaling=Decimal("1e-18")
    ),
    "0x01b3ec4aae1b8729529beb4965f27d008788b0eb": TokenInfo(
        currency=CurrencyInfo(symbol="DPP", name="Digital Assets Power Play"), scaling=Decimal("1e-18")
    ),
    "0x01c0987e88f778df6640787226bc96354e1a9766": TokenInfo(
        currency=CurrencyInfo(symbol="UAT", name="UltrAlpha"), scaling=Decimal("1e-18")
    ),
    "0x01c8857057326b8f64dcb5cba6d802dcd132946e": TokenInfo(
        currency=CurrencyInfo(symbol="XAT", name="ShareAt"), scaling=Decimal("1e-18")
    ),
    "0x01da76dea59703578040012357b81ffe62015c2d": TokenInfo(
        currency=CurrencyInfo(symbol="crYETH", name="Cream yETH"), scaling=Decimal("1e-8")
    ),
    "0x01db18f6a474840db3480a6a35227d4d0dfcca37": TokenInfo(
        currency=CurrencyInfo(symbol="BP", name="Backpack Token"), scaling=Decimal("1e-18")
    ),
    "0x01e2087be8c34fb06229aa9e49bf801a89d30d9d": TokenInfo(
        currency=CurrencyInfo(symbol="MILES", name="Miles Coin"), scaling=Decimal("1e-18")
    ),
    "0x01f2acf2914860331c1cb1a9acecda7475e06af8": TokenInfo(
        currency=CurrencyInfo(symbol="MESH", name="MeshBox"), scaling=Decimal("1e-18")
    ),
    "0x01fa555c97d7958fa6f771f3bbd5ccd508f81e22": TokenInfo(
        currency=CurrencyInfo(symbol="CVL", name="Civil"), scaling=Decimal("1e-18")
    ),
    "0x01ff50f8b7f74e4f00580d9596cd3d0d6d6e326f": TokenInfo(
        currency=CurrencyInfo(symbol="BFT", name="BnkToTheFuture"), scaling=Decimal("1e-18")
    ),
    "0x0202be363b8a4820f3f4de7faf5224ff05943ab1": TokenInfo(
        currency=CurrencyInfo(symbol="UFT", name="UniLend Finance"), scaling=Decimal("1e-18")
    ),
    "0x020c710646e23ab868dbe5b88004892797fe4efb": TokenInfo(
        currency=CurrencyInfo(symbol="GOLF", name="Golfcoin"), scaling=Decimal("1e-18")
    ),
    "0x021576770cb3729716ccfb687afdb4c6bf720cb6": TokenInfo(
        currency=CurrencyInfo(symbol="UFFYI", name="Unlimited FiscusFYI"), scaling=Decimal("1e-18")
    ),
    "0x021c9c28970e25623ab426e76a1ff14ae6b8c6e6": TokenInfo(
        currency=CurrencyInfo(symbol="CPP", name="Crypto Price Platform"), scaling=Decimal("1e-18")
    ),
    "0x021ecda86507d0bc0ca1d8e738d78fe303b42cd8": TokenInfo(
        currency=CurrencyInfo(symbol="WMT.CX", name="Wal-Mart Stores Inc"), scaling=Decimal("1e-8")
    ),
    "0x0223fc70574214f65813fe336d870ac47e147fae": TokenInfo(
        currency=CurrencyInfo(symbol="CZR", name="CanonChain"), scaling=Decimal("1e-18")
    ),
    "0x0228528581c01a303d59d8cf6b72bd5a5d219458": TokenInfo(
        currency=CurrencyInfo(symbol="OKNC", name="Ok Node Community Token"), scaling=Decimal("1e-4")
    ),
    "0x02285acaafeb533e03a7306c55ec031297df9224": TokenInfo(
        currency=CurrencyInfo(symbol="DDAI", name="dForce DAI"), scaling=Decimal("1e-18")
    ),
    "0x0235fe624e044a05eed7a43e16e3083bc8a4287a": TokenInfo(
        currency=CurrencyInfo(symbol="OCC", name="Original Crypto Coin"), scaling=Decimal("1e-18")
    ),
    "0x0258f474786ddfd37abce6df6bbb1dd5dfc4434a": TokenInfo(
        currency=CurrencyInfo(symbol="ORN", name="Orion Protocol"), scaling=Decimal("1e-8")
    ),
    "0x025abad9e518516fdaafbdcdb9701b37fb7ef0fa": TokenInfo(
        currency=CurrencyInfo(symbol="GTKT", name="GoldenTickets"), scaling=Decimal("1e-0")
    ),
    "0x026e62dded1a6ad07d93d39f96b9eabd59665e0d": TokenInfo(
        currency=CurrencyInfo(symbol="BIRD", name="BirdCoin"), scaling=Decimal("1e-18")
    ),
    "0x02725836ebf3ecdb1cdf1c7b02fcbbfaa2736af8": TokenInfo(
        currency=CurrencyInfo(symbol="BTCA", name="Bitair"), scaling=Decimal("1e-8")
    ),
    "0x0275e1001e293c46cfe158b3702aade0b99f88a5": TokenInfo(
        currency=CurrencyInfo(symbol="OIL", name="Oiler"), scaling=Decimal("1e-18")
    ),
    "0x028171bca77440897b824ca71d1c56cac55b68a3": TokenInfo(
        currency=CurrencyInfo(symbol="ADAI", name="Aave DAI"), scaling=Decimal("1e-18")
    ),
    "0x028ce5ea3298a50c0d8a27b937b1f48cf0d68b56": TokenInfo(
        currency=CurrencyInfo(symbol="OTO", name="OnTime"), scaling=Decimal("1e-18")
    ),
    "0x029606e5ec44cad1346d6a1273a53b971fa93ad6": TokenInfo(
        currency=CurrencyInfo(symbol="EMPRO", name="Empowr Orange"), scaling=Decimal("1e-18")
    ),
    "0x02ad2f3c1f761db2374626abd8c59ed4e710a13c": TokenInfo(
        currency=CurrencyInfo(symbol="ATVI.CX", name="Activision Blizzard Inc"), scaling=Decimal("1e-8")
    ),
    "0x02b1669bc9ee893edaff3cadfd326a294d643f99": TokenInfo(
        currency=CurrencyInfo(symbol="WLF", name="Wolfs Group"), scaling=Decimal("1e-0")
    ),
    "0x02cc786304ec4d6758cb16a962139870b4d960ce": TokenInfo(
        currency=CurrencyInfo(symbol="CNV", name="Coronavirus Token"), scaling=Decimal("1e-18")
    ),
    "0x02d3a27ac3f55d5d91fb0f52759842696a864217": TokenInfo(
        currency=CurrencyInfo(symbol="IONX", name="Charged Particles"), scaling=Decimal("1e-18")
    ),
    "0x02e88a689fdfb920e7aa6174fb7ab72add3c5694": TokenInfo(
        currency=CurrencyInfo(symbol="BCHHEDGE", name="1X Short Bitcoin Cash Token"), scaling=Decimal("1e-18")
    ),
    "0x02eca910cb3a7d43ebc7e8028652ed5c6b70259b": TokenInfo(
        currency=CurrencyInfo(symbol="PTERIA", name="Pteria"), scaling=Decimal("1e-18")
    ),
    "0x02f2d4a04e6e01ace88bd2cd632875543b2ef577": TokenInfo(
        currency=CurrencyInfo(symbol="PKG", name="PKG Token"), scaling=Decimal("1e-18")
    ),
    "0x02f61fd266da6e8b102d4121f5ce7b992640cf98": TokenInfo(
        currency=CurrencyInfo(symbol="LIKE", name="LikeCoin (ERC-20)"), scaling=Decimal("1e-18")
    ),
    "0x02f7d805f895c8ea3d14f11ba4df3352580cc506": TokenInfo(
        currency=CurrencyInfo(symbol="JCP", name="Jc Penney"), scaling=Decimal("1e-8")
    ),
    "0x02fdd6866333d8cd8b1ca022d382080698060bc2": TokenInfo(
        currency=CurrencyInfo(symbol="69C", name="6ix9ine Chain"), scaling=Decimal("1e-18")
    ),
    "0x03066da434e5264ef0b32f787923f974a5726fdc": TokenInfo(
        currency=CurrencyInfo(symbol="BCS", name="Basis Coin Share"), scaling=Decimal("1e-18")
    ),
    "0x0309c98b1bffa350bcb3f9fb9780970ca32a5060": TokenInfo(
        currency=CurrencyInfo(symbol="BDI", name="BasketDAO DeFi Index"), scaling=Decimal("1e-18")
    ),
    "0x030ba81f1c18d280636f32af80b9aad02cf0854e": TokenInfo(
        currency=CurrencyInfo(symbol="AWETH", name="Aave WETH"), scaling=Decimal("1e-18")
    ),
    "0x0316eb71485b0ab14103307bf65a021042c6d380": TokenInfo(
        currency=CurrencyInfo(symbol="HBTC", name="Huobi BTC"), scaling=Decimal("1e-18")
    ),
    "0x031e0c6a7c91df1bc171d33cccc6988fd2ddeb6f": TokenInfo(
        currency=CurrencyInfo(symbol="TCFX", name="TopCoinFX"), scaling=Decimal("1e-18")
    ),
    "0x0324dd195d0cd53f9f07bee6a48ee7a20bad738f": TokenInfo(
        currency=CurrencyInfo(symbol="SPICE", name="SPiCE VC Token"), scaling=Decimal("1e-8")
    ),
    "0x0327112423f3a68efdf1fcf402f6c5cb9f7c33fd": TokenInfo(
        currency=CurrencyInfo(symbol="BTC++", name="PieDAO BTC++"), scaling=Decimal("1e-18")
    ),
    "0x03282f2d7834a97369cad58f888ada19eec46ab6": TokenInfo(
        currency=CurrencyInfo(symbol="GEX", name="Globex"), scaling=Decimal("1e-8")
    ),
    "0x0329d23fc7b1b1e6cca57afa3f0090f1189069e8": TokenInfo(
        currency=CurrencyInfo(symbol="LINKRSICO", name="LINK RSI Crossover Set"), scaling=Decimal("1e-18")
    ),
    "0x034b0dd380b5f6f8123b8d0d0e42329b67772792": TokenInfo(
        currency=CurrencyInfo(symbol="ADAB", name="ADAB Solutions"), scaling=Decimal("1e-18")
    ),
    "0x035bfe6057e15ea692c0dfdcab3bb41a64dd2ad4": TokenInfo(
        currency=CurrencyInfo(symbol="ULU", name="Universal Liquidity Union"), scaling=Decimal("1e-18")
    ),
    "0x035df12e0f3ac6671126525f1015e47d79dfeddf": TokenInfo(
        currency=CurrencyInfo(symbol="0XMR", name="0xMonero"), scaling=Decimal("1e-18")
    ),
    "0x036407f23d5e1c1486f7488332cf54bf06e5f09f": TokenInfo(
        currency=CurrencyInfo(symbol="ABC", name="Alphabit"), scaling=Decimal("1e-18")
    ),
    "0x0371a82e4a9d0a4312f3ee2ac9c6958512891372": TokenInfo(
        currency=CurrencyInfo(symbol="STU", name="bitJob"), scaling=Decimal("1e-18")
    ),
    "0x0371f7b219fff864b437bcfb564810f323fffcca": TokenInfo(
        currency=CurrencyInfo(symbol="BTCR", name="Bitcurate"), scaling=Decimal("1e-4")
    ),
    "0x037a54aab062628c9bbae1fdb1583c195585fe41": TokenInfo(
        currency=CurrencyInfo(symbol="LCX", name="LCX"), scaling=Decimal("1e-18")
    ),
    "0x03806ce5ef69bd9780edfb04c29da1f23db96294": TokenInfo(
        currency=CurrencyInfo(symbol="TSL", name="Tesla Token"), scaling=Decimal("1e-18")
    ),
    "0x03829f5675f3b51d0f8c2a74417a757625acf22f": TokenInfo(
        currency=CurrencyInfo(symbol="YFIB", name="YFIBALANCER.FINANCE"), scaling=Decimal("1e-18")
    ),
    "0x038a68ff68c393373ec894015816e33ad41bd564": TokenInfo(
        currency=CurrencyInfo(symbol="GLCH", name="Glitch Protocol"), scaling=Decimal("1e-18")
    ),
    "0x0391d2021f89dc339f60fff84546ea23e337750f": TokenInfo(
        currency=CurrencyInfo(symbol="BOND", name="BarnBridge"), scaling=Decimal("1e-18")
    ),
    "0x039b5649a59967e3e936d7471f9c3700100ee1ab": TokenInfo(
        currency=CurrencyInfo(symbol="KCS", name="Kucoin Shares"), scaling=Decimal("1e-6")
    ),
    "0x039f5050de4908f9b5ddf40a4f3aa3f329086387": TokenInfo(
        currency=CurrencyInfo(symbol="ENC", name="Ethernet Cash"), scaling=Decimal("1e-18")
    ),
    "0x03a6d45820edb4e66e41ece0dc96170e875a1d16": TokenInfo(
        currency=CurrencyInfo(symbol="MCB", name="Microbyte"), scaling=Decimal("1e-8")
    ),
    "0x03ab458634910aad20ef5f1c8ee96f1d6ac54919": TokenInfo(
        currency=CurrencyInfo(symbol="RAI", name="Rai Reflex Index"), scaling=Decimal("1e-18")
    ),
    "0x03b10be8aca24879c5d7196163cb0e4ce22c2503": TokenInfo(
        currency=CurrencyInfo(symbol="DHG.CX", name="Delta Air Lines"), scaling=Decimal("1e-8")
    ),
    "0x03b828cca6594dc0a21c814bd8c944104bb03223": TokenInfo(
        currency=CurrencyInfo(symbol="PAN", name="PayChain"), scaling=Decimal("1e-18")
    ),
    "0x03be5c903c727ee2c8c4e9bc0acc860cca4715e2": TokenInfo(
        currency=CurrencyInfo(symbol="CAPS", name="Ternoa"), scaling=Decimal("1e-18")
    ),
    "0x03c780cd554598592b97b7256ddaad759945b125": TokenInfo(
        currency=CurrencyInfo(symbol="BTRN", name="Biotron"), scaling=Decimal("1e-18")
    ),
    "0x03d1e72765545729a035e909edd9371a405f77fb": TokenInfo(
        currency=CurrencyInfo(symbol="NABOX", name="Nabox"), scaling=Decimal("1e-18")
    ),
    "0x03e173ad8d1581a4802d3b532ace27a62c5b81dc": TokenInfo(
        currency=CurrencyInfo(symbol="THALES", name="Thales"), scaling=Decimal("1e-18")
    ),
    "0x03e3f0c25965f13dbbc58246738c183e27b26a56": TokenInfo(
        currency=CurrencyInfo(symbol="DSCP", name="Disciplina Token"), scaling=Decimal("1e-18")
    ),
    "0x03e8f56ad0d759bcfff960863388bfdb2efd1579": TokenInfo(
        currency=CurrencyInfo(symbol="YFI CASH", name="yearn.finance cash"), scaling=Decimal("1e-18")
    ),
    "0x03fb52d4ee633ab0d06c833e32efdd8d388f3e6a": TokenInfo(
        currency=CurrencyInfo(symbol="HOLE", name="Super Black Hole"), scaling=Decimal("1e-18")
    ),
    "0x0417912b3a7af768051765040a55bb0925d4ddcf": TokenInfo(
        currency=CurrencyInfo(symbol="LID", name="Liquidity Dividends Protocol"), scaling=Decimal("1e-18")
    ),
    "0x041a36b015486941ce8d5f2c7ff2e88f97390640": TokenInfo(
        currency=CurrencyInfo(symbol="LED", name="Ledgis"), scaling=Decimal("1e-4")
    ),
    "0x042afd3869a47e2d5d42cc787d5c9e19df32185f": TokenInfo(
        currency=CurrencyInfo(symbol="POT", name="Hotpot Base Token"), scaling=Decimal("1e-18")
    ),
    "0x042f972ac93404f0fcbe4e3a0729f0b395232106": TokenInfo(
        currency=CurrencyInfo(symbol="DYX", name="XCoinPay"), scaling=Decimal("1e-8")
    ),
    "0x044b5b891fe27ec8c155c4de189b90420b4f960e": TokenInfo(
        currency=CurrencyInfo(symbol="ALXN.CX", name="Alexion Pharmaceuticals Inc"), scaling=Decimal("1e-8")
    ),
    "0x045eb7e34e94b28c7a3641bc5e1a1f61f225af9f": TokenInfo(
        currency=CurrencyInfo(symbol="ZPAE", name="ZPAY"), scaling=Decimal("1e-18")
    ),
    "0x0469b5be3d08413de884bae18afb886ee4521c25": TokenInfo(
        currency=CurrencyInfo(symbol="HTP", name="HuoTop"), scaling=Decimal("1e-8")
    ),
    "0x047686fb287e7263a23873dea66b4501015a2226": TokenInfo(
        currency=CurrencyInfo(symbol="CUTE", name="Blockchain Cuties Universe"), scaling=Decimal("1e-18")
    ),
    "0x0488401c3f535193fa8df029d9ffe615a06e74e6": TokenInfo(
        currency=CurrencyInfo(symbol="SRK", name="SparkPoint"), scaling=Decimal("1e-18")
    ),
    "0x048fe49be32adfc9ed68c37d32b5ec9df17b3603": TokenInfo(
        currency=CurrencyInfo(symbol="SKM", name="Skrumble Network"), scaling=Decimal("1e-18")
    ),
    "0x049399a6b048d52971f7d122ae21a1532722285f": TokenInfo(
        currency=CurrencyInfo(symbol="FLOT", name="Fire Lotto"), scaling=Decimal("1e-18")
    ),
    "0x04a020325024f130988782bd5276e53595e8d16e": TokenInfo(
        currency=CurrencyInfo(symbol="HERB", name="Herbalist Token"), scaling=Decimal("1e-8")
    ),
    "0x04aa51bbcb46541455ccf1b8bef2ebc5d3787ec9": TokenInfo(
        currency=CurrencyInfo(symbol="yWTBC", name="iearn wBTC"), scaling=Decimal("1e-8")
    ),
    "0x04abeda201850ac0124161f037efd70c74ddc74c": TokenInfo(
        currency=CurrencyInfo(symbol="NEST", name="Nest Protocol"), scaling=Decimal("1e-18")
    ),
    "0x04ad70466a79dd1251f22ad426248088724ff32b": TokenInfo(
        currency=CurrencyInfo(symbol="THBC", name="Time-Honored Brand Chain"), scaling=Decimal("1e-4")
    ),
    "0x04b0672f1659e6d9cae313415f7bbfe87b678a7c": TokenInfo(
        currency=CurrencyInfo(symbol="SWKS.CX", name="Skyworks Solutions Inc"), scaling=Decimal("1e-8")
    ),
    "0x04bc0ab673d88ae9dbc9da2380cb6b79c4bca9ae": TokenInfo(
        currency=CurrencyInfo(symbol="YBUSD", name="yBUSD"), scaling=Decimal("1e-18")
    ),
    "0x04c7cd246330288a84d2788e8a323cc41206c2eb": TokenInfo(
        currency=CurrencyInfo(symbol="BTCM", name="Bitcoin Monkey"), scaling=Decimal("1e-18")
    ),
    "0x04cc783b450b8d11f3c7d00dd03fdf7fb51fe9f2": TokenInfo(
        currency=CurrencyInfo(symbol="FLMC", name="Filmscoin"), scaling=Decimal("1e-18")
    ),
    "0x04e0af0af1b7f0023c6b12af5a94df59b0e8cf59": TokenInfo(
        currency=CurrencyInfo(symbol="SETS", name="Sensitrust Token"), scaling=Decimal("1e-18")
    ),
    "0x04f2e7221fdb1b52a68169b25793e51478ff0329": TokenInfo(
        currency=CurrencyInfo(symbol="CAPP", name="Cappasity"), scaling=Decimal("1e-2")
    ),
    "0x04fa0d235c4abf4bcf4787af4cf447de572ef828": TokenInfo(
        currency=CurrencyInfo(symbol="UMA", name="UMA"), scaling=Decimal("1e-18")
    ),
    "0x0501e7a02c285b9b520fdbf1badc74ae931ad75d": TokenInfo(
        currency=CurrencyInfo(symbol="WTF", name="Walnut.finance"), scaling=Decimal("1e-18")
    ),
    "0x050508637d2878755cb29b2be4320ac24d5ce4ff": TokenInfo(
        currency=CurrencyInfo(symbol="RBPC", name="Relax Buddy Token"), scaling=Decimal("1e-18")
    ),
    "0x05074b439211739bd952e1092127f17afd0de204": TokenInfo(
        currency=CurrencyInfo(symbol="YFF", name="yefam.finance"), scaling=Decimal("1e-18")
    ),
    "0x05079687d35b93538cbd59fe5596380cae9054a9": TokenInfo(
        currency=CurrencyInfo(symbol="BTSG", name="BitSong"), scaling=Decimal("1e-18")
    ),
    "0x053e5ba7cb9669dcc2feb2d0e1d3d4a0ad6aae39": TokenInfo(
        currency=CurrencyInfo(symbol="OKBBEAR", name="3X Short OKB Token"), scaling=Decimal("1e-18")
    ),
    "0x05462671c05adc39a6521fa60d5e9443e9e9d2b9": TokenInfo(
        currency=CurrencyInfo(symbol="USDF", name="OLD USDf"), scaling=Decimal("1e-9")
    ),
    "0x054c64741dbafdc19784505494029823d89c3b13": TokenInfo(
        currency=CurrencyInfo(symbol="XET", name="Eternal Token"), scaling=Decimal("1e-8")
    ),
    "0x054d64b73d3d8a21af3d764efd76bcaa774f3bb2": TokenInfo(
        currency=CurrencyInfo(symbol="PPAY", name="Plasma Finance"), scaling=Decimal("1e-18")
    ),
    "0x054f76beed60ab6dbeb23502178c52d6c5debe40": TokenInfo(
        currency=CurrencyInfo(symbol="FIN", name="DeFiner"), scaling=Decimal("1e-18")
    ),
    "0x0557df767419296474c3f551bb0a0ed4c2dd3380": TokenInfo(
        currency=CurrencyInfo(symbol="UPXAU", name="Universal Gold"), scaling=Decimal("1e-5")
    ),
    "0x056017c55ae7ae32d12aef7c679df83a85ca75ff": TokenInfo(
        currency=CurrencyInfo(symbol="WYV", name="Project Wyvern Token"), scaling=Decimal("1e-18")
    ),
    "0x0563dce613d559a47877ffd1593549fb9d3510d6": TokenInfo(
        currency=CurrencyInfo(symbol="SUPERBID", name="SuperBid"), scaling=Decimal("1e-18")
    ),
    "0x0568025c55c21bda4bc488f3107ebfc8b3d3ef2d": TokenInfo(
        currency=CurrencyInfo(symbol="ELET", name="Elementium token"), scaling=Decimal("1e-8")
    ),
    "0x056fd409e1d7a124bd7017459dfea2f387b6d5cd": TokenInfo(
        currency=CurrencyInfo(symbol="GUSD", name="Gemini Dollar"), scaling=Decimal("1e-2")
    ),
    "0x0574586d9c3741c638998434cea480c67e4aa88f": TokenInfo(
        currency=CurrencyInfo(symbol="NBT", name="Ninsa B Token"), scaling=Decimal("1e-8")
    ),
    "0x057fb10e3fec001a40e6b75d3a30b99e23e54107": TokenInfo(
        currency=CurrencyInfo(symbol="ALGOBEAR", name="3X Short Algorand Token"), scaling=Decimal("1e-18")
    ),
    "0x05860d453c7974cbf46508c06cba14e211c629ce": TokenInfo(
        currency=CurrencyInfo(symbol="EDN", name="Eden Coin"), scaling=Decimal("1e-18")
    ),
    "0x058ed4edfd0ca7147e34a30fa4dd9907b0c9c4ba": TokenInfo(
        currency=CurrencyInfo(symbol="VIPG", name="VipGo"), scaling=Decimal("1e-18")
    ),
    "0x058ef0ba85e053e55d357c8a95bc6ea7458def8a": TokenInfo(
        currency=CurrencyInfo(symbol="TKX", name="TradeKax"), scaling=Decimal("1e-18")
    ),
    "0x05919a3915462abbdf2cd3c5b42213cc8f596102": TokenInfo(
        currency=CurrencyInfo(symbol="FNXS", name="FinanceX Exchange Token"), scaling=Decimal("1e-8")
    ),
    "0x0598c2fdd3a0564970a86b69c72a6c57077c84bb": TokenInfo(
        currency=CurrencyInfo(symbol="SYCO", name="Syariahcoin"), scaling=Decimal("1e-8")
    ),
    "0x05aaaa829afa407d83315cded1d45eb16025910c": TokenInfo(
        currency=CurrencyInfo(symbol="SPX", name="Sp8de"), scaling=Decimal("1e-18")
    ),
    "0x05b4fb1a630c330feb85980d4bf0e32a96ef16c9": TokenInfo(
        currency=CurrencyInfo(symbol="MRK.CX", name="Merck & Co Inc"), scaling=Decimal("1e-8")
    ),
    "0x05c3617cbf1304b9260aa61ec960f115d67becea": TokenInfo(
        currency=CurrencyInfo(symbol="CBIX", name="Cubrix"), scaling=Decimal("1e-18")
    ),
    "0x05c7065d644096a4e4c3fe24af86e36de021074b": TokenInfo(
        currency=CurrencyInfo(symbol="LCT", name="LendConnect"), scaling=Decimal("1e-18")
    ),
    "0x05d072cbd90c132e2c4cfddd2ad2cbe018ec62fc": TokenInfo(
        currency=CurrencyInfo(symbol="DESC", name="DESCOUNT"), scaling=Decimal("1e-18")
    ),
    "0x05d27cdd23e22ca63e7f9c7c6d1b79ede9c4fcf5": TokenInfo(
        currency=CurrencyInfo(symbol="YFPI", name="Yearn Finance Passive Income"), scaling=Decimal("1e-18")
    ),
    "0x05d412ce18f24040bb3fa45cf2c69e506586d8e8": TokenInfo(
        currency=CurrencyInfo(symbol="MFTU", name="MFTU"), scaling=Decimal("1e-18")
    ),
    "0x05ec93c0365baaeabf7aeffb0972ea7ecdd39cf1": TokenInfo(
        currency=CurrencyInfo(symbol="ABAT", name="Aave BAT"), scaling=Decimal("1e-18")
    ),
    "0x05edffbda103d90d5040829a105f687443e0ca3e": TokenInfo(
        currency=CurrencyInfo(symbol="WYX", name="Woyager"), scaling=Decimal("1e-18")
    ),
    "0x05f4a42e251f2d52b8ed15e9fedaacfcef1fad27": TokenInfo(
        currency=CurrencyInfo(symbol="ZIL", name="Zilliqa"), scaling=Decimal("1e-12")
    ),
    "0x05fb86775fd5c16290f1e838f5caaa7342bd9a63": TokenInfo(
        currency=CurrencyInfo(symbol="HAI", name="Hacken Token"), scaling=Decimal("1e-8")
    ),
    "0x05fcc72cfb4150abae415c885f7a433ff523296f": TokenInfo(
        currency=CurrencyInfo(symbol="YOK", name="YOKcoin"), scaling=Decimal("1e-18")
    ),
    "0x06147110022b768ba8f99a8f385df11a151a9cc8": TokenInfo(
        currency=CurrencyInfo(symbol="ACE", name="ACE"), scaling=Decimal("1e-0")
    ),
    "0x0622769d566b3c4c1c58ca4fabee8e60bb3163e5": TokenInfo(
        currency=CurrencyInfo(symbol="YUSDT", name="Yellow Tether"), scaling=Decimal("1e-6")
    ),
    "0x062e3be6a7c56a395b1881a0cd69a4923ade4fa2": TokenInfo(
        currency=CurrencyInfo(symbol="BAC", name="Bowl A Coin"), scaling=Decimal("1e-18")
    ),
    "0x062f90480551379791fbe2ed74c1fe69821b30d3": TokenInfo(
        currency=CurrencyInfo(symbol="YMAX", name="YMAX"), scaling=Decimal("1e-18")
    ),
    "0x06301057d77d54b6e14c7faffb11ffc7cab4eaa7": TokenInfo(
        currency=CurrencyInfo(symbol="mDAI", name="DMM: DAI"), scaling=Decimal("1e-18")
    ),
    "0x063e49e4f59365711d9218e67314dd98f00d97e5": TokenInfo(
        currency=CurrencyInfo(symbol="THOR", name="THOR Digital Application System"), scaling=Decimal("1e-8")
    ),
    "0x06404399e748cd83f25ab163711f9f4d61cfd0e6": TokenInfo(
        currency=CurrencyInfo(symbol="FNK", name="FunKeyPay"), scaling=Decimal("1e-18")
    ),
    "0x06576eb3b212d605b797dc15523d9dc9f4f66db4": TokenInfo(
        currency=CurrencyInfo(symbol="TCP", name="TCP"), scaling=Decimal("1e-18")
    ),
    "0x066798d9ef0833ccc719076dab77199ecbd178b0": TokenInfo(
        currency=CurrencyInfo(symbol="SAKE", name="SakeToken"), scaling=Decimal("1e-18")
    ),
    "0x0673e08528f4fafa727779c32eea83493b6d3cd5": TokenInfo(
        currency=CurrencyInfo(symbol="COMM.CX", name="CommScope Holding Company Inc"), scaling=Decimal("1e-8")
    ),
    "0x06a01a4d579479dd5d884ebf61a31727a3d8d442": TokenInfo(
        currency=CurrencyInfo(symbol="SKEY", name="SmartKey"), scaling=Decimal("1e-8")
    ),
    "0x06af07097c9eeb7fd685c692751d5c66db49c215": TokenInfo(
        currency=CurrencyInfo(symbol="CHAI", name="Chai"), scaling=Decimal("1e-18")
    ),
    "0x06b179e292f080871825bed5d722162fd96b4c95": TokenInfo(
        currency=CurrencyInfo(symbol="XGG", name="10x.gg"), scaling=Decimal("1e-18")
    ),
    "0x06bead2ead661b51307b646f7419d5284330c135": TokenInfo(
        currency=CurrencyInfo(symbol="ESHIP", name="EliteShipperToken"), scaling=Decimal("1e-8")
    ),
    "0x06e0feb0d74106c7ada8497754074d222ec6bcdf": TokenInfo(
        currency=CurrencyInfo(symbol="BTB", name="Bitball"), scaling=Decimal("1e-18")
    ),
    "0x06f3cdabae564b0546529b4dd8fef1bcd4235753": TokenInfo(
        currency=CurrencyInfo(symbol="TLW", name="TilWiki"), scaling=Decimal("1e-8")
    ),
    "0x06f65b8cfcb13a9fe37d836fe9708da38ecb29b2": TokenInfo(
        currency=CurrencyInfo(symbol="FAME", name="SAINT FAME: Genesis Shirt"), scaling=Decimal("1e-18")
    ),
    "0x06f979e4f04ec565ae8d7479a94c60def8846832": TokenInfo(
        currency=CurrencyInfo(symbol="MOVI", name="MoviToken"), scaling=Decimal("1e-6")
    ),
    "0x06ff1a3b08b63e3b2f98a5124bfc22dc0ae654d3": TokenInfo(
        currency=CurrencyInfo(symbol="KASSIAHOTEL", name="Atlas"), scaling=Decimal("1e-18")
    ),
    "0x0707681f344deb24184037fc0228856f2137b02e": TokenInfo(
        currency=CurrencyInfo(symbol="FNKOS", name="FNKOS"), scaling=Decimal("1e-18")
    ),
    "0x07150e919b4de5fd6a63de1f9384828396f25fdc": TokenInfo(
        currency=CurrencyInfo(symbol="BASE", name="Base Protocol"), scaling=Decimal("1e-9")
    ),
    "0x073af3f70516380654ba7c5812c4ab0255f081bc": TokenInfo(
        currency=CurrencyInfo(symbol="TRUMPWIN", name="Trump Wins Token"), scaling=Decimal("1e-18")
    ),
    "0x07597255910a51509ca469568b048f2597e72504": TokenInfo(
        currency=CurrencyInfo(symbol="1UP", name="Uptrennd"), scaling=Decimal("1e-18")
    ),
    "0x075b1bb99792c9e1041ba13afef80c91a1e70fb3": TokenInfo(
        currency=CurrencyInfo(symbol="SBTCCURVE", name="LP sBTC Curve"), scaling=Decimal("1e-18")
    ),
    "0x0763fdccf1ae541a5961815c0872a8c5bc6de4d7": TokenInfo(
        currency=CurrencyInfo(symbol="SUKU", name="SUKU"), scaling=Decimal("1e-18")
    ),
    "0x076641af1b8f06b7f8c92587156143c109002cbe": TokenInfo(
        currency=CurrencyInfo(symbol="SOP", name="SoPay"), scaling=Decimal("1e-18")
    ),
    "0x0766e79a6fd74469733e8330b3b461c0320ff059": TokenInfo(
        currency=CurrencyInfo(symbol="EXN", name="ExchangeN"), scaling=Decimal("1e-18")
    ),
    "0x076c97e1c869072ee22f8c91978c99b4bcb02591": TokenInfo(
        currency=CurrencyInfo(symbol="CBT", name="CommerceBlock Token"), scaling=Decimal("1e-18")
    ),
    "0x0775c81a273b355e6a5b76e240bf708701f00279": TokenInfo(
        currency=CurrencyInfo(symbol="BUL", name="Bulleon"), scaling=Decimal("1e-18")
    ),
    "0x077dc3c0c9543df1cdd78386df3204e69e0dd274": TokenInfo(
        currency=CurrencyInfo(symbol="PBK", name="Powerbank"), scaling=Decimal("1e-7")
    ),
    "0x0794ce7d4459105926da230f318c1e34bc790517": TokenInfo(
        currency=CurrencyInfo(symbol="RBG", name="RankingBall Gold"), scaling=Decimal("1e-18")
    ),
    "0x07a0ad7a9dfc3854466f8f29a173bf04bba5686e": TokenInfo(
        currency=CurrencyInfo(symbol="SLM", name="Solomon Defi"), scaling=Decimal("1e-18")
    ),
    "0x07a58629aaf3e1a0d07d8f43114b76bd5eee3b91": TokenInfo(
        currency=CurrencyInfo(symbol="GETX", name="Guaranteed Ethurance Token Extra"), scaling=Decimal("1e-18")
    ),
    "0x07a80063d0a47d958a000593c1eb6bdc9c2ebf86": TokenInfo(
        currency=CurrencyInfo(symbol="CTZ", name="CrystalzToken"), scaling=Decimal("1e-18")
    ),
    "0x07ad33ba649bb17acd67ad93a79417fa0039cf1f": TokenInfo(
        currency=CurrencyInfo(symbol="ELE", name="Elevato"), scaling=Decimal("1e-18")
    ),
    "0x07af1f10d749e432fed9c5901dd7d7821267a846": TokenInfo(
        currency=CurrencyInfo(symbol="BC", name="BlockchainCuties"), scaling=Decimal("1e-0")
    ),
    "0x07bac35846e5ed502aa91adf6a9e7aa210f2dcbe": TokenInfo(
        currency=CurrencyInfo(symbol="EROWAN", name="Sifchain"), scaling=Decimal("1e-18")
    ),
    "0x07bcbb61f3f499715185210715c544ead22aa1b2": TokenInfo(
        currency=CurrencyInfo(symbol="GPRO.CX", name="GoPro Inc"), scaling=Decimal("1e-8")
    ),
    "0x07d9e49ea402194bf48a8276dafb16e4ed633317": TokenInfo(
        currency=CurrencyInfo(symbol="DALC", name="Dalecoin"), scaling=Decimal("1e-8")
    ),
    "0x07e3c70653548b04f0a75970c1f81b4cbbfb606f": TokenInfo(
        currency=CurrencyInfo(symbol="DLT", name="Agrello"), scaling=Decimal("1e-18")
    ),
    "0x07ef9e82721ac16809d24dafbe1792ce01654db4": TokenInfo(
        currency=CurrencyInfo(symbol="BNANA", name="Chimpion"), scaling=Decimal("1e-18")
    ),
    "0x07f064e5e36b8b06b4c825233945ec1b61bba09f": TokenInfo(
        currency=CurrencyInfo(symbol="RAD.CX", name="Rite Aid"), scaling=Decimal("1e-8")
    ),
    "0x0809bd190c94f4408e691c410e67bff0df5d225d": TokenInfo(
        currency=CurrencyInfo(symbol="CNP", name="Cryptonia Poker"), scaling=Decimal("1e-2")
    ),
    "0x080aa07e2c7185150d7e4da98838a8d2feac3dfc": TokenInfo(
        currency=CurrencyInfo(symbol="BTT", name="BitEther"), scaling=Decimal("1e-0")
    ),
    "0x080eb7238031f97ff011e273d6cad5ad0c2de532": TokenInfo(
        currency=CurrencyInfo(symbol="KIT", name="Kittoken"), scaling=Decimal("1e-18")
    ),
    "0x081f67afa0ccf8c7b17540767bbe95df2ba8d97f": TokenInfo(
        currency=CurrencyInfo(symbol="CET", name="CoinEx Token"), scaling=Decimal("1e-18")
    ),
    "0x082280b4ae1a9e552555c256124de96fab63159b": TokenInfo(
        currency=CurrencyInfo(symbol="MEQ", name="Meterqubes"), scaling=Decimal("1e-18")
    ),
    "0x0829d2d5cc09d3d341e813c821b0cfae272d9fb2": TokenInfo(
        currency=CurrencyInfo(symbol="ROCKS", name="Social Rocket"), scaling=Decimal("1e-18")
    ),
    "0x082e13494f12ebb7206fbf67e22a6e1975a1a669": TokenInfo(
        currency=CurrencyInfo(symbol="ARTIS", name="Artis Turba"), scaling=Decimal("1e-8")
    ),
    "0x08350dfe9b5bca39599b20e0ed92c5c78dc8a891": TokenInfo(
        currency=CurrencyInfo(symbol="LYFE", name="LyfeToken"), scaling=Decimal("1e-18")
    ),
    "0x08389495d7456e1951ddf7c3a1314a4bfb646d8b": TokenInfo(
        currency=CurrencyInfo(symbol="CRPT", name="Crypterium"), scaling=Decimal("1e-18")
    ),
    "0x08399ab5ebbe96870b289754a7bd21e7ec8c6fcb": TokenInfo(
        currency=CurrencyInfo(symbol="BCZ", name="Becaz"), scaling=Decimal("1e-18")
    ),
    "0x0843971b4ac6e842a518aa184e0271d88b5cb74f": TokenInfo(
        currency=CurrencyInfo(symbol="XCL", name="CLASSIE"), scaling=Decimal("1e-8")
    ),
    "0x084da5a9c0e3f086532b98d8568432349b89d9df": TokenInfo(
        currency=CurrencyInfo(symbol="FPT", name="FUUPAY"), scaling=Decimal("1e-18")
    ),
    "0x0854dcbdcd026c0b534b09608adb3f2bf6baacd0": TokenInfo(
        currency=CurrencyInfo(symbol="HPAY", name="HPAY Coin"), scaling=Decimal("1e-18")
    ),
    "0x08711d3b02c8758f2fb3ab4e80228418a7f8e39c": TokenInfo(
        currency=CurrencyInfo(symbol="EDG", name="Edgeless"), scaling=Decimal("1e-0")
    ),
    "0x0879e0c9822b75f31f0b0ed2a30be9f484a57c2f": TokenInfo(
        currency=CurrencyInfo(symbol="LTG", name="Litecoin Gold"), scaling=Decimal("1e-0")
    ),
    "0x0886949c1b8c412860c4264ceb8083d1365e86cf": TokenInfo(
        currency=CurrencyInfo(symbol="BTCE", name="EthereumBitcoin"), scaling=Decimal("1e-8")
    ),
    "0x089a6d83282fb8988a656189f1e7a73fa6c1cac2": TokenInfo(
        currency=CurrencyInfo(symbol="PGL", name="Prospectors Gold"), scaling=Decimal("1e-18")
    ),
    "0x089b85fa15f72c1088cbbef23a49db80b91dd521": TokenInfo(
        currency=CurrencyInfo(symbol="BIT", name="BlockEstate"), scaling=Decimal("1e-8")
    ),
    "0x08a2e41fb99a7599725190b9c970ad3893fa33cf": TokenInfo(
        currency=CurrencyInfo(symbol="PASTA", name="Spaghetti"), scaling=Decimal("1e-18")
    ),
    "0x08a75dbc7167714ceac1a8e43a8d643a4edd625a": TokenInfo(
        currency=CurrencyInfo(symbol="WILD", name="Wild Credit"), scaling=Decimal("1e-18")
    ),
    "0x08aa0ed0040736dd28d4c8b16ab453b368248d19": TokenInfo(
        currency=CurrencyInfo(symbol="XPT", name="Cryptobuyer Token"), scaling=Decimal("1e-18")
    ),
    "0x08ad83d779bdf2bbe1ad9cc0f78aa0d24ab97802": TokenInfo(
        currency=CurrencyInfo(symbol="RWS", name="Robonomics Web Services"), scaling=Decimal("1e-18")
    ),
    "0x08b4c866ae9d1be56a06e0c302054b4ffe067b43": TokenInfo(
        currency=CurrencyInfo(symbol="BITCAR", name="BitCar"), scaling=Decimal("1e-8")
    ),
    "0x08c32b0726c5684024ea6e141c50ade9690bbdcc": TokenInfo(
        currency=CurrencyInfo(symbol="STOS", name="Stratos"), scaling=Decimal("1e-18")
    ),
    "0x08d32b0da63e2c3bcf8019c9c5d849d7a9d791e6": TokenInfo(
        currency=CurrencyInfo(symbol="DCN", name="Dentacoin"), scaling=Decimal("1e-0")
    ),
    "0x08d8aa3f0011e529cc4be4fda8999c0b01fb6ec3": TokenInfo(
        currency=CurrencyInfo(symbol="VGT.CX", name="Vanguard Information Technology ETF"), scaling=Decimal("1e-8")
    ),
    "0x08d967bb0134f2d07f7cfb6e246680c53927dd30": TokenInfo(
        currency=CurrencyInfo(symbol="MATH", name="MATH"), scaling=Decimal("1e-18")
    ),
    "0x08da69ca2bfe378f384cb76c84d6ded701ec65c7": TokenInfo(
        currency=CurrencyInfo(symbol="LTCMOON", name="10X Long Litecoin Token"), scaling=Decimal("1e-18")
    ),
    "0x08f5a9235b08173b7569f83645d2c7fb55e8ccd8": TokenInfo(
        currency=CurrencyInfo(symbol="TNT", name="Tierion"), scaling=Decimal("1e-8")
    ),
    "0x090185f2135308bad17527004364ebcc2d37e5f6": TokenInfo(
        currency=CurrencyInfo(symbol="SPELL", name="Spell Token"), scaling=Decimal("1e-18")
    ),
    "0x0911d4efeef46726ede1a84e196ee0589fef97a5": TokenInfo(
        currency=CurrencyInfo(symbol="MOMO.CX", name="Momo Inc"), scaling=Decimal("1e-8")
    ),
    "0x0922f1d808adc3a4444bed2f73fac53a1a2a5859": TokenInfo(
        currency=CurrencyInfo(symbol="TIK", name="ChronoBase"), scaling=Decimal("1e-18")
    ),
    "0x0944d2c41fef3088467287e208e5bbb622a0c09c": TokenInfo(
        currency=CurrencyInfo(symbol="STRX", name="sTRX"), scaling=Decimal("1e-18")
    ),
    "0x09463194e7890d226a5fdb226d19ab600b92ee9f": TokenInfo(
        currency=CurrencyInfo(symbol="BST", name="Baas Token"), scaling=Decimal("1e-4")
    ),
    "0x0947b0e6d821378805c9598291385ce7c791a6b2": TokenInfo(
        currency=CurrencyInfo(symbol="LND", name="Lendingblock"), scaling=Decimal("1e-18")
    ),
    "0x0953b746b099b98d59940bd80e94649dc88514ba": TokenInfo(
        currency=CurrencyInfo(symbol="EAUD", name="Australian Currency"), scaling=Decimal("1e-7")
    ),
    "0x0954906da0bf32d5479e25f46056d22f08464cab": TokenInfo(
        currency=CurrencyInfo(symbol="INDEX", name="Index Cooperative"), scaling=Decimal("1e-18")
    ),
    "0x09617f6fd6cf8a71278ec86e23bbab29c04353a7": TokenInfo(
        currency=CurrencyInfo(symbol="ULT", name="Shardus"), scaling=Decimal("1e-18")
    ),
    "0x097a43eb652a4d718d18bea66452b94fabb4944f": TokenInfo(
        currency=CurrencyInfo(symbol="CLVS.CX", name="Clovis Oncology Inc"), scaling=Decimal("1e-8")
    ),
    "0x09843b9137fc5935b7f3832152f9074db5d2d1ee": TokenInfo(
        currency=CurrencyInfo(symbol="YFI3", name="YFI3.money"), scaling=Decimal("1e-18")
    ),
    "0x0996bfb5d057faa237640e2506be7b4f9c46de0b": TokenInfo(
        currency=CurrencyInfo(symbol="RNDR", name="Render Token"), scaling=Decimal("1e-18")
    ),
    "0x09970aec766b6f3223aca9111555e99dc50ff13a": TokenInfo(
        currency=CurrencyInfo(symbol="LEVL", name="Levolution"), scaling=Decimal("1e-18")
    ),
    "0x09a3ecafa817268f77be1283176b946c4ff2e608": TokenInfo(
        currency=CurrencyInfo(symbol="MIR", name="Mirror Protocol"), scaling=Decimal("1e-18")
    ),
    "0x09a981cfdbb37852c7f1d7f3f1ff0ca1ee999080": TokenInfo(
        currency=CurrencyInfo(symbol="DWDP.CX", name="DowDuPont Inc"), scaling=Decimal("1e-8")
    ),
    "0x09ae0c4c34a09875660e681fe1890f3b35175151": TokenInfo(
        currency=CurrencyInfo(symbol="BTCMOON", name="BTC Moonshot Set"), scaling=Decimal("1e-18")
    ),
    "0x09bca6ebab05ee2ae945be4eda51393d94bf7b99": TokenInfo(
        currency=CurrencyInfo(symbol="STB", name="STABLE STB Token"), scaling=Decimal("1e-4")
    ),
    "0x09cb097356fd053f8544abfa2c8a9d4fb2200d62": TokenInfo(
        currency=CurrencyInfo(symbol="BKC", name="Blockchain Knowledge Coin"), scaling=Decimal("1e-18")
    ),
    "0x09d8b66c48424324b25754a873e290cae5dca439": TokenInfo(
        currency=CurrencyInfo(symbol="NVT", name="Nova Token"), scaling=Decimal("1e-18")
    ),
    "0x09df6a5ca936be45f5ae45c7e58c9b4602011fcd": TokenInfo(
        currency=CurrencyInfo(symbol="YFUEL", name="yearn.fuel"), scaling=Decimal("1e-18")
    ),
    "0x09e4bdfb273245063ef5e800d891eff7d04f9b83": TokenInfo(
        currency=CurrencyInfo(symbol="ETHPA", name="ETH Price Action Candlestick Set"), scaling=Decimal("1e-18")
    ),
    "0x09e64c2b61a5f1690ee6fbed9baf5d6990f8dfd0": TokenInfo(
        currency=CurrencyInfo(symbol="GRO", name="GROWTH DeFi"), scaling=Decimal("1e-18")
    ),
    "0x09fe5f0236f0ea5d930197dce254d77b04128075": TokenInfo(
        currency=CurrencyInfo(symbol="WCK", name="Wrapped CryptoKitties"), scaling=Decimal("1e-18")
    ),
    "0x0a0db74ef8b4480cc29b7d68647727feeb1ea4ec": TokenInfo(
        currency=CurrencyInfo(symbol="GLEX", name="GLEX"), scaling=Decimal("1e-18")
    ),
    "0x0a0e3a2973e19d5305a43fafb50935f34f01a55c": TokenInfo(
        currency=CurrencyInfo(symbol="BYND.CX", name="Beyond Meat Inc"), scaling=Decimal("1e-8")
    ),
    "0x0a2a86bb0bee386a11291d5d01e89cdfb565df5d": TokenInfo(
        currency=CurrencyInfo(symbol="BITB", name="Bitcoin Bull"), scaling=Decimal("1e-0")
    ),
    "0x0a2d9370cf74da3fd3df5d764e394ca8205c50b6": TokenInfo(
        currency=CurrencyInfo(symbol="SET", name="Save Environment Token"), scaling=Decimal("1e-18")
    ),
    "0x0a3dc37762f0102175fd43d3871d7fa855626146": TokenInfo(
        currency=CurrencyInfo(symbol="NFLX.CX", name="Netflix"), scaling=Decimal("1e-8")
    ),
    "0x0a425122852ed351946a828b348bfdcda51effd8": TokenInfo(
        currency=CurrencyInfo(symbol="EMC", name="EduMetrix Coin"), scaling=Decimal("1e-18")
    ),
    "0x0a4b2d4b48a63088e0897a3f147ba37f81a27722": TokenInfo(
        currency=CurrencyInfo(symbol="CURA", name="CuraDAI"), scaling=Decimal("1e-18")
    ),
    "0x0a50c93c762fdd6e56d86215c24aaad43ab629aa": TokenInfo(
        currency=CurrencyInfo(symbol="LGO", name="LGO Token"), scaling=Decimal("1e-8")
    ),
    "0x0a5248ff74842600175c3edd7c84cd45257ff0d0": TokenInfo(
        currency=CurrencyInfo(symbol="BGC", name="BitGain Project"), scaling=Decimal("1e-18")
    ),
    "0x0a5dc2204dfc6082ef3bbcfc3a468f16318c4168": TokenInfo(
        currency=CurrencyInfo(symbol="PANDA", name="PandaGold"), scaling=Decimal("1e-18")
    ),
    "0x0a680e503fd9ae14b62444c75ffb4bef1f105666": TokenInfo(
        currency=CurrencyInfo(symbol="GZM", name="Arma Coin"), scaling=Decimal("1e-8")
    ),
    "0x0a76aad21948ea1ef447d26dee91a54370e151e0": TokenInfo(
        currency=CurrencyInfo(symbol="ELITE", name="Ethereum Lite"), scaling=Decimal("1e-18")
    ),
    "0x0a913bead80f321e7ac35285ee10d9d922659cb7": TokenInfo(
        currency=CurrencyInfo(symbol="DOS", name="DOS Network"), scaling=Decimal("1e-18")
    ),
    "0x0a9a9ce600d08bf9b76f49fa4e7b38a67ebeb1e6": TokenInfo(
        currency=CurrencyInfo(symbol="GROW", name="GROWCHAIN"), scaling=Decimal("1e-8")
    ),
    "0x0a9d68886a0d7db83a30ec00d62512483e5ad437": TokenInfo(
        currency=CurrencyInfo(symbol="TRCL", name="Treecle"), scaling=Decimal("1e-0")
    ),
    "0x0a9f693fce6f00a51a8e0db4351b5a8078b4242e": TokenInfo(
        currency=CurrencyInfo(symbol="RES", name="Resfinex Token"), scaling=Decimal("1e-5")
    ),
    "0x0aa7efe4945db24d95ca6e117bba65ed326e291a": TokenInfo(
        currency=CurrencyInfo(symbol="OJA", name="Ojamu"), scaling=Decimal("1e-18")
    ),
    "0x0aacfbec6a24756c20d41914f2caba817c0d8521": TokenInfo(
        currency=CurrencyInfo(symbol="YAM", name="YAM"), scaling=Decimal("1e-18")
    ),
    "0x0abdace70d3790235af448c88547603b945604ea": TokenInfo(
        currency=CurrencyInfo(symbol="DNT", name="district0x"), scaling=Decimal("1e-18")
    ),
    "0x0abefb7611cb3a01ea3fad85f33c3c934f8e2cf4": TokenInfo(
        currency=CurrencyInfo(symbol="FRD", name="Farad"), scaling=Decimal("1e-18")
    ),
    "0x0ae055097c6d159879521c384f1d2123d1f195e6": TokenInfo(
        currency=CurrencyInfo(symbol="STAKE", name="xDAI Stake"), scaling=Decimal("1e-18")
    ),
    "0x0aee8703d34dd9ae107386d3eff22ae75dd616d1": TokenInfo(
        currency=CurrencyInfo(symbol="SLICE", name="Tranche Finance"), scaling=Decimal("1e-18")
    ),
    "0x0aef06dcccc531e581f0440059e6ffcc206039ee": TokenInfo(
        currency=CurrencyInfo(symbol="ITT", name="Intelligent Trading Foundation"), scaling=Decimal("1e-8")
    ),
    "0x0af44e2784637218dd1d32a322d44e603a8f0c6a": TokenInfo(
        currency=CurrencyInfo(symbol="MTX", name="MATRYX"), scaling=Decimal("1e-18")
    ),
    "0x0affa06e7fbe5bc9a764c979aa66e8256a631f02": TokenInfo(
        currency=CurrencyInfo(symbol="PLBT", name="Polybius"), scaling=Decimal("1e-6")
    ),
    "0x0b165b00431927e1392712fb0d7e804041154f7a": TokenInfo(
        currency=CurrencyInfo(symbol="WITT", name="Witoken"), scaling=Decimal("1e-18")
    ),
    "0x0b1724cc9fda0186911ef6a75949e9c0d3f0f2f3": TokenInfo(
        currency=CurrencyInfo(symbol="RIYA", name="Etheriya"), scaling=Decimal("1e-8")
    ),
    "0x0b342c51d1592c41068d5d4b4da4a68c0a04d5a4": TokenInfo(
        currency=CurrencyInfo(symbol="ONES", name="OneSwap DAO Token"), scaling=Decimal("1e-18")
    ),
    "0x0b38210ea11411557c13457d4da7dc6ea731b88a": TokenInfo(
        currency=CurrencyInfo(symbol="API3", name="API3"), scaling=Decimal("1e-18")
    ),
    "0x0b498ff89709d3838a063f1dfa463091f9801c2b": TokenInfo(
        currency=CurrencyInfo(symbol="BTC2X-FLI", name="BTC 2x Flexible Lev"), scaling=Decimal("1e-18")
    ),
    "0x0b4bdc478791897274652dc15ef5c135cae61e60": TokenInfo(
        currency=CurrencyInfo(symbol="DAX", name="DAEX"), scaling=Decimal("1e-18")
    ),
    "0x0b4c2708f052dca413600e237675e4d6778a9375": TokenInfo(
        currency=CurrencyInfo(symbol="CLM", name="CoinClaim"), scaling=Decimal("1e-16")
    ),
    "0x0b63128c40737b13647552e0c926bcfeccc35f93": TokenInfo(
        currency=CurrencyInfo(symbol="WLITI", name="wLITI"), scaling=Decimal("1e-18")
    ),
    "0x0b76544f6c413a555f309bf76260d1e02377c02a": TokenInfo(
        currency=CurrencyInfo(symbol="INT", name="Internet Node Token"), scaling=Decimal("1e-6")
    ),
    "0x0ba45a8b5d5575935b8158a88c631e9f9c95a2e5": TokenInfo(
        currency=CurrencyInfo(symbol="TRB", name="Tellor Tributes"), scaling=Decimal("1e-18")
    ),
    "0x0bb217e40f8a5cb79adf04e1aab60e5abd0dfc1e": TokenInfo(
        currency=CurrencyInfo(symbol="SWFTC", name="SWFTCOIN"), scaling=Decimal("1e-8")
    ),
    "0x0bba19f02b9fbdca23d783ccc3f78c0a06544073": TokenInfo(
        currency=CurrencyInfo(symbol="MGC", name="Myanmar Gold Coin"), scaling=Decimal("1e-18")
    ),
    "0x0bc2149d073f62510c99d908f52d0d703da1f135": TokenInfo(
        currency=CurrencyInfo(symbol="CCC", name="Ciupek Capital Coin"), scaling=Decimal("1e-18")
    ),
    "0x0bc529c00c6401aef6d220be8c6ea1667f6ad93e": TokenInfo(
        currency=CurrencyInfo(symbol="YFI", name="yearn.finance"), scaling=Decimal("1e-18")
    ),
    "0x0bc61dded5f6710c637cf8288eb6058766ce1921": TokenInfo(
        currency=CurrencyInfo(symbol="CEN", name="Coinsuper Ecosystem Network"), scaling=Decimal("1e-18")
    ),
    "0x0be4a987fd8dcbd2fff64ba4131d3a208307f667": TokenInfo(
        currency=CurrencyInfo(symbol="WIT", name="Wealth in Token"), scaling=Decimal("1e-18")
    ),
    "0x0bef619cf38cf0c22967289b8419720fbd1db9f7": TokenInfo(
        currency=CurrencyInfo(symbol="AEN", name="Aenco"), scaling=Decimal("1e-8")
    ),
    "0x0bf54992649c19bd8db4080078a32383827352f3": TokenInfo(
        currency=CurrencyInfo(symbol="ASETH", name="Asian ETH Sentiment Set"), scaling=Decimal("1e-18")
    ),
    "0x0bf6261297198d91d4fa460242c69232146a5703": TokenInfo(
        currency=CurrencyInfo(symbol="LIB", name="Libera"), scaling=Decimal("1e-18")
    ),
    "0x0c04d4f331da8df75f9e2e271e3f3f1494c66c36": TokenInfo(
        currency=CurrencyInfo(symbol="PRSP", name="Prosper"), scaling=Decimal("1e-9")
    ),
    "0x0c2c5e2b677dea43025b5da5061fece445f0295b": TokenInfo(
        currency=CurrencyInfo(symbol="COVID", name="Corona Coin"), scaling=Decimal("1e-18")
    ),
    "0x0c37bcf456bc661c14d596683325623076d7e283": TokenInfo(
        currency=CurrencyInfo(symbol="ARNX", name="Aeron"), scaling=Decimal("1e-18")
    ),
    "0x0c3ef32f802967db75b9d49fe1e76620151ccb81": TokenInfo(
        currency=CurrencyInfo(symbol="NODE", name="Whole Network"), scaling=Decimal("1e-5")
    ),
    "0x0c6144c16af288948c8fdb37fd8fec94bff3d1d9": TokenInfo(
        currency=CurrencyInfo(symbol="NUSD", name="Neutral Dollar"), scaling=Decimal("1e-6")
    ),
    "0x0c6f5f7d555e7518f6841a79436bd2b1eef03381": TokenInfo(
        currency=CurrencyInfo(symbol="COCOS", name="CocosToken"), scaling=Decimal("1e-18")
    ),
    "0x0c7d5ae016f806603cb1782bea29ac69471cab9c": TokenInfo(
        currency=CurrencyInfo(symbol="BFC", name="Bifrost"), scaling=Decimal("1e-18")
    ),
    "0x0c91b015aba6f7b4738dcd36e7410138b29adc29": TokenInfo(
        currency=CurrencyInfo(symbol="COIL", name="CoinOil"), scaling=Decimal("1e-8")
    ),
    "0x0c963a1b52eb97c5e457c7d76696f8b95c3087ed": TokenInfo(
        currency=CurrencyInfo(symbol="TOKO", name="Tokoin"), scaling=Decimal("1e-18")
    ),
    "0x0ca8e31a9058bd0d3db73758ff36e74159a542cb": TokenInfo(
        currency=CurrencyInfo(symbol="SPK", name="Spike Token"), scaling=Decimal("1e-0")
    ),
    "0x0cae9e4d663793c2a2a0b211c1cf4bbca2b9caa7": TokenInfo(
        currency=CurrencyInfo(symbol="MAMZN", name="Mirrored Amazon"), scaling=Decimal("1e-18")
    ),
    "0x0cb20b77adbe5cd58fcecc4f4069d04b327862e5": TokenInfo(
        currency=CurrencyInfo(symbol="MGT", name="Mystery Ghost Token"), scaling=Decimal("1e-8")
    ),
    "0x0cbc9b02b8628ae08688b5cc8134dc09e36c443b": TokenInfo(
        currency=CurrencyInfo(symbol="TRAT", name="Tratok"), scaling=Decimal("1e-5")
    ),
    "0x0cc9fccff81252f4bd8c5c6b359b14ae2ed851cf": TokenInfo(
        currency=CurrencyInfo(symbol="INNBCL", name="InnovativeBioresearchClassic"), scaling=Decimal("1e-6")
    ),
    "0x0ccd5dd52dee42b171a623478e5261c1eaae092a": TokenInfo(
        currency=CurrencyInfo(symbol="DFM", name="DeFi on MCW"), scaling=Decimal("1e-18")
    ),
    "0x0cd022dde27169b20895e0e2b2b8a33b25e63579": TokenInfo(
        currency=CurrencyInfo(symbol="RISE", name="EverRise"), scaling=Decimal("1e-18")
    ),
    "0x0cd1b0e93ebaad374752af74fe44f877dd0438c0": TokenInfo(
        currency=CurrencyInfo(symbol="TCS", name="TCS Token"), scaling=Decimal("1e-18")
    ),
    "0x0cd6c8161f1638485a1a2f5bf1a0127e45913c2f": TokenInfo(
        currency=CurrencyInfo(symbol="USDTBEAR", name="3X Short Tether Token"), scaling=Decimal("1e-18")
    ),
    "0x0cda1454bda46df7f8593286c4aab856be803518": TokenInfo(
        currency=CurrencyInfo(symbol="NEE.CX", name="Nextera Energy"), scaling=Decimal("1e-8")
    ),
    "0x0cdf9acd87e940837ff21bb40c9fd55f68bba059": TokenInfo(
        currency=CurrencyInfo(symbol="MINT", name="Public Mint"), scaling=Decimal("1e-18")
    ),
    "0x0ce6d5a093d4166237c7a9ff8e0553b0293214a1": TokenInfo(
        currency=CurrencyInfo(symbol="DCNT", name="Decenturion"), scaling=Decimal("1e-18")
    ),
    "0x0cec1a9154ff802e7934fc916ed7ca50bde6844e": TokenInfo(
        currency=CurrencyInfo(symbol="POOL", name="PoolTogether"), scaling=Decimal("1e-18")
    ),
    "0x0cf0ee63788a0849fe5297f3407f701e122cc023": TokenInfo(
        currency=CurrencyInfo(symbol="DATA", name="Streamr"), scaling=Decimal("1e-18")
    ),
    "0x0cf58006b2400ebec3eb8c05b73170138a340563": TokenInfo(
        currency=CurrencyInfo(symbol="GBP", name="Good Boy Points"), scaling=Decimal("1e-18")
    ),
    "0x0cf713b11c9b986ec40d65bd4f7fbd50f6ff2d64": TokenInfo(
        currency=CurrencyInfo(symbol="IST34", name="IST34 Token"), scaling=Decimal("1e-18")
    ),
    "0x0d262e5dc4a06a0f1c90ce79c7a60c09dfc884e4": TokenInfo(
        currency=CurrencyInfo(symbol="J8T", name="JET8"), scaling=Decimal("1e-8")
    ),
    "0x0d268c105e1c5bda54adfd811f8010eb11525fa0": TokenInfo(
        currency=CurrencyInfo(symbol="AIU", name="Artificial Intelligence Union"), scaling=Decimal("1e-8")
    ),
    "0x0d2bb9d68dd4451a09ec94c05e20bd395022bd8e": TokenInfo(
        currency=CurrencyInfo(symbol="CBUCKS", name="CRYPTOBUCKS"), scaling=Decimal("1e-2")
    ),
    "0x0d438f3b5175bebc262bf23753c1e53d03432bde": TokenInfo(
        currency=CurrencyInfo(symbol="WNXM", name="Wrapped NXM"), scaling=Decimal("1e-18")
    ),
    "0x0d4b4da5fb1a7d55e85f8e22f728701ceb6e44c9": TokenInfo(
        currency=CurrencyInfo(symbol="DGMT", name="DigiMax"), scaling=Decimal("1e-18")
    ),
    "0x0d5bb28972e0b2d63732f558b4af265aa5407467": TokenInfo(
        currency=CurrencyInfo(symbol="VII", name="7Chain"), scaling=Decimal("1e-4")
    ),
    "0x0d5e2681d2aadc91f7da4146740180a2190f0c79": TokenInfo(
        currency=CurrencyInfo(symbol="HTBULL", name="3X Long Huobi Token Token"), scaling=Decimal("1e-18")
    ),
    "0x0d6dd9f68d24ec1d5fe2174f3ec8dab52b52baf5": TokenInfo(
        currency=CurrencyInfo(symbol="KC", name="KMCC"), scaling=Decimal("1e-18")
    ),
    "0x0d8775f648430679a709e98d2b0cb6250d2887ef": TokenInfo(
        currency=CurrencyInfo(symbol="BAT", name="Basic Attention Token"), scaling=Decimal("1e-18")
    ),
    "0x0d88ed6e74bbfd96b831231638b66c05571e824f": TokenInfo(
        currency=CurrencyInfo(symbol="AVT", name="Aventus"), scaling=Decimal("1e-18")
    ),
    "0x0d9a10a0466b7e9ad693e24993f5105bfdb240e3": TokenInfo(
        currency=CurrencyInfo(symbol="CR1", name="Cryptoland1"), scaling=Decimal("1e-18")
    ),
    "0x0d9a653f681168f410d14d19b7743c041eafc58a": TokenInfo(
        currency=CurrencyInfo(symbol="EXE", name="EinsteinCash"), scaling=Decimal("1e-8")
    ),
    "0x0db03b6cde0b2d427c64a04feafd825938368f1f": TokenInfo(
        currency=CurrencyInfo(symbol="PDATA", name="PDATA"), scaling=Decimal("1e-18")
    ),
    "0x0db8d8b76bc361bacbb72e2c491e06085a97ab31": TokenInfo(
        currency=CurrencyInfo(symbol="IQN", name="IQeon"), scaling=Decimal("1e-18")
    ),
    "0x0dd83b5013b2ad7094b1a7783d96ae0168f82621": TokenInfo(
        currency=CurrencyInfo(symbol="FIC", name="Florafic"), scaling=Decimal("1e-18")
    ),
    "0x0de05f6447ab4d22c8827449ee4ba2d5c288379b": TokenInfo(
        currency=CurrencyInfo(symbol="OOKI", name="Ooki"), scaling=Decimal("1e-18")
    ),
    "0x0def8d8adde14c9ef7c2a986df3ea4bd65826767": TokenInfo(
        currency=CurrencyInfo(symbol="CLIQ", name="DefiCliq"), scaling=Decimal("1e-18")
    ),
    "0x0df721639ca2f7ff0e1f618b918a65ffb199ac4e": TokenInfo(
        currency=CurrencyInfo(symbol="uDOO", name="uDOO"), scaling=Decimal("1e-18")
    ),
    "0x0dfdd839cde95dabf56f0b5c5698e0159138930d": TokenInfo(
        currency=CurrencyInfo(symbol="MYFI", name="MyFiChain"), scaling=Decimal("1e-18")
    ),
    "0x0e0989b1f9b8a38983c2ba8053269ca62ec9b195": TokenInfo(
        currency=CurrencyInfo(symbol="POE", name="Po.et"), scaling=Decimal("1e-8")
    ),
    "0x0e192d382a36de7011f795acc4391cd302003606": TokenInfo(
        currency=CurrencyInfo(symbol="FST", name="Futureswap"), scaling=Decimal("1e-18")
    ),
    "0x0e22734e078d6e399bcee40a549db591c4ea46cb": TokenInfo(
        currency=CurrencyInfo(symbol="STM", name="Streamity"), scaling=Decimal("1e-18")
    ),
    "0x0e2298e3b3390e3b945a5456fbf59ecc3f55da16": TokenInfo(
        currency=CurrencyInfo(symbol="YAMV1", name="YAM v1"), scaling=Decimal("1e-18")
    ),
    "0x0e29e5abbb5fd88e28b2d355774e73bd47de3bcd": TokenInfo(
        currency=CurrencyInfo(symbol="HAKKA", name="Hakka Finance"), scaling=Decimal("1e-18")
    ),
    "0x0e2b2855e7674d61286e105b57fe280fbb67137b": TokenInfo(
        currency=CurrencyInfo(symbol="BTRD", name="BTrade Coin"), scaling=Decimal("1e-18")
    ),
    "0x0e2ec54fc0b509f445631bf4b91ab8168230c752": TokenInfo(
        currency=CurrencyInfo(symbol="LINKUSD", name="LINKUSD"), scaling=Decimal("1e-18")
    ),
    "0x0e3129b3fde4a458b7910a2602e92ac533b9400e": TokenInfo(
        currency=CurrencyInfo(symbol="ROTO", name="Roto"), scaling=Decimal("1e-18")
    ),
    "0x0e3abf45855fbaa1afcc3b33cf08b3915bdcda96": TokenInfo(
        currency=CurrencyInfo(symbol="XRB", name="Rainbow"), scaling=Decimal("1e-8")
    ),
    "0x0e3de3b0e3d617fd8d1d8088639ba877feb4d742": TokenInfo(
        currency=CurrencyInfo(symbol="Rock2Pay", name="Rock2Pay"), scaling=Decimal("1e-18")
    ),
    "0x0e3ef895c59e7db27214ab5bbf56347ce115a3f4": TokenInfo(
        currency=CurrencyInfo(symbol="RLR", name="Relayer Network"), scaling=Decimal("1e-18")
    ),
    "0x0e536b7831c7a7527fad55da433986853d21a0c7": TokenInfo(
        currency=CurrencyInfo(symbol="HARP", name="Harpoon"), scaling=Decimal("1e-8")
    ),
    "0x0e5c8c387c5eba2ecbc137ad012aed5fe729e251": TokenInfo(
        currency=CurrencyInfo(symbol="RPG", name="Rangers Protocol"), scaling=Decimal("1e-18")
    ),
    "0x0e69d0a2bbb30abcb7e5cfea0e4fde19c00a8d47": TokenInfo(
        currency=CurrencyInfo(symbol="IOV", name="Carlive Chain"), scaling=Decimal("1e-8")
    ),
    "0x0e8d6b471e332f140e7d9dbb99e5e3822f728da6": TokenInfo(
        currency=CurrencyInfo(symbol="ABYSS", name="Abyss"), scaling=Decimal("1e-18")
    ),
    "0x0e9b56d2233ea2b5883861754435f9c51dbca141": TokenInfo(
        currency=CurrencyInfo(symbol="RPEPE", name="Rare Pepe"), scaling=Decimal("1e-18")
    ),
    "0x0ea20e7ffb006d4cfe84df2f72d8c7bd89247db0": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNICRVWETH", name="Aave AMM UniCRVWETH"), scaling=Decimal("1e-18")
    ),
    "0x0ea984e789302b7b612147e4e4144e64f21425eb": TokenInfo(
        currency=CurrencyInfo(symbol="WTN", name="Waletoken"), scaling=Decimal("1e-8")
    ),
    "0x0eb6e56aacae6a21bde99c826ac798d225488c3d": TokenInfo(
        currency=CurrencyInfo(symbol="CRVT", name="Crypto Revolution"), scaling=Decimal("1e-18")
    ),
    "0x0ebb614204e47c09b6c3feb9aaecad8ee060e23e": TokenInfo(
        currency=CurrencyInfo(symbol="CPAY", name="Cryptopay"), scaling=Decimal("1e-0")
    ),
    "0x0ec623c98a0014d67b0a0e411b80a45f2cd6c29d": TokenInfo(
        currency=CurrencyInfo(symbol="SRPT.CX", name="Sarepta Therapeutics Inc"), scaling=Decimal("1e-8")
    ),
    "0x0ec9f76202a7061eb9b3a7d6b59d36215a7e37da": TokenInfo(
        currency=CurrencyInfo(symbol="BPT", name="BlackPool Token"), scaling=Decimal("1e-18")
    ),
    "0x0ecdd783dc7bf820614044b51862ed29714d2ba5": TokenInfo(
        currency=CurrencyInfo(symbol="MDZA", name="Medooza Ecosystem"), scaling=Decimal("1e-18")
    ),
    "0x0ed8343dfdee32e38b4c4ce15a3b00a59e90f3db": TokenInfo(
        currency=CurrencyInfo(symbol="CLM", name="Claymore"), scaling=Decimal("1e-18")
    ),
    "0x0ee815f8be0b0259e2657c8b8d1e57bd3d60f26b": TokenInfo(
        currency=CurrencyInfo(symbol="TRUST", name="Harmony Block Capital"), scaling=Decimal("1e-6")
    ),
    "0x0ef3b2024ae079e6dbc2b37435ce30d2731f0101": TokenInfo(
        currency=CurrencyInfo(symbol="UNIFI", name="UNIFI DeFi"), scaling=Decimal("1e-18")
    ),
    "0x0eff3e0d75872c44b1c70fee12fdfb88430059f4": TokenInfo(
        currency=CurrencyInfo(symbol="XDC", name="XueDaoCoin"), scaling=Decimal("1e-18")
    ),
    "0x0f00f1696218eaefa2d2330df3d6d1f94813b38f": TokenInfo(
        currency=CurrencyInfo(symbol="SEDO", name="SEDO POW TOKEN"), scaling=Decimal("1e-8")
    ),
    "0x0f02e27745e3b6e9e1310d19469e2b5d7b5ec99a": TokenInfo(
        currency=CurrencyInfo(symbol="PCL", name="Peculium"), scaling=Decimal("1e-8")
    ),
    "0x0f237d5ea7876e0e2906034d98fdb20d43666ad4": TokenInfo(
        currency=CurrencyInfo(symbol="XCON", name="Connect coin(XCON)"), scaling=Decimal("1e-18")
    ),
    "0x0f2d719407fdbeff09d87557abb7232601fd9f29": TokenInfo(
        currency=CurrencyInfo(symbol="SYN", name="Synapse"), scaling=Decimal("1e-18")
    ),
    "0x0f33bb20a282a7649c7b3aff644f084a9348e933": TokenInfo(
        currency=CurrencyInfo(symbol="YUP", name="YUPIE"), scaling=Decimal("1e-18")
    ),
    "0x0f3adc247e91c3c50bc08721355a41037e89bc20": TokenInfo(
        currency=CurrencyInfo(symbol="ANC", name="Anchor Protocol"), scaling=Decimal("1e-18")
    ),
    "0x0f4ca92660efad97a9a70cb0fe969c755439772c": TokenInfo(
        currency=CurrencyInfo(symbol="LEV", name="Leverj"), scaling=Decimal("1e-9")
    ),
    "0x0f513ffb4926ff82d7f60a05069047aca295c413": TokenInfo(
        currency=CurrencyInfo(symbol="XSC", name="Crowdstart Coin"), scaling=Decimal("1e-18")
    ),
    "0x0f51bb10119727a7e5ea3538074fb341f56b09ad": TokenInfo(
        currency=CurrencyInfo(symbol="DAO", name="DAO Maker"), scaling=Decimal("1e-18")
    ),
    "0x0f598112679b78e17a4a9febc83703710d33489c": TokenInfo(
        currency=CurrencyInfo(symbol="XMRG", name="Monero Gold"), scaling=Decimal("1e-8")
    ),
    "0x0f5d2fb29fb7d3cfee444a200298f468908cc942": TokenInfo(
        currency=CurrencyInfo(symbol="MANA", name="Decentraland"), scaling=Decimal("1e-18")
    ),
    "0x0f612a09ead55bb81b6534e80ed5a21bf0a27b16": TokenInfo(
        currency=CurrencyInfo(symbol="ENTS", name="EUNOMIA"), scaling=Decimal("1e-8")
    ),
    "0x0f71b8de197a1c84d31de0f1fa7926c365f052b3": TokenInfo(
        currency=CurrencyInfo(symbol="ARCONA", name="Arcona"), scaling=Decimal("1e-18")
    ),
    "0x0f72714b35a366285df85886a2ee174601292a17": TokenInfo(
        currency=CurrencyInfo(symbol="1SG", name="1SG"), scaling=Decimal("1e-18")
    ),
    "0x0f775ad69e3c93d599d3315a130bd82a0cdda397": TokenInfo(
        currency=CurrencyInfo(symbol="APEUSD-LINK-DEC21", name="apeUSD-LINK Synthetic USD (Dec 2021)"),
        scaling=Decimal("1e-18"),
    ),
    "0x0f7f961648ae6db43c75663ac7e5414eb79b5704": TokenInfo(
        currency=CurrencyInfo(symbol="XIO", name="Blockzero Labs"), scaling=Decimal("1e-18")
    ),
    "0x0f83287ff768d1c1e17a42f44d644d7f22e8ee1d": TokenInfo(
        currency=CurrencyInfo(symbol="SCHF", name="sCHF"), scaling=Decimal("1e-18")
    ),
    "0x0f86b24da64e16d9b21585a8734b8b0c94a43c18": TokenInfo(
        currency=CurrencyInfo(symbol="FDT", name="Fidelity Token"), scaling=Decimal("1e-8")
    ),
    "0x0f8794f66c7170c4f9163a8498371a747114f6c4": TokenInfo(
        currency=CurrencyInfo(symbol="FMA", name="Flama"), scaling=Decimal("1e-18")
    ),
    "0x0f8b6440a1f7be3354fe072638a5c0f500b044be": TokenInfo(
        currency=CurrencyInfo(symbol="KTH", name="Katerium"), scaling=Decimal("1e-18")
    ),
    "0x0f8c45b896784a1e408526b9300519ef8660209c": TokenInfo(
        currency=CurrencyInfo(symbol="XMX", name="XMax"), scaling=Decimal("1e-8")
    ),
    "0x0fd10b9899882a6f2fcb5c371e17e70fdee00c38": TokenInfo(
        currency=CurrencyInfo(symbol="PUNDIX", name="Pundi X"), scaling=Decimal("1e-18")
    ),
    "0x0fdc3b843d26f4290597223bbaf24c460091b0c8": TokenInfo(
        currency=CurrencyInfo(symbol="NKE.CX", name="NIKE Inc"), scaling=Decimal("1e-8")
    ),
    "0x0fdc5313333533cc0c00c22792bff7383d3055f2": TokenInfo(
        currency=CurrencyInfo(symbol="YFPRO", name="YFPRO Finance"), scaling=Decimal("1e-18")
    ),
    "0x0fe156436f203b114c6c562cb1a2a81aa2801090": TokenInfo(
        currency=CurrencyInfo(symbol="SKC", name="SKINCHAIN"), scaling=Decimal("1e-18")
    ),
    "0x0fe629d1e84e171f8ff0c1ded2cc2221caa48a3f": TokenInfo(
        currency=CurrencyInfo(symbol="MASK", name="NFTX Hashmasks Index"), scaling=Decimal("1e-18")
    ),
    "0x0ff161071e627a0e6de138105c73970f86ca7922": TokenInfo(
        currency=CurrencyInfo(symbol="PIT", name="Paypite v2"), scaling=Decimal("1e-18")
    ),
    "0x0ff5a8451a839f5f0bb3562689d9a44089738d11": TokenInfo(
        currency=CurrencyInfo(symbol="RDPX", name="Dopex Rebate Token"), scaling=Decimal("1e-18")
    ),
    "0x0ff69c20206d644331e6b6ca5262eeb8d6ccf7af": TokenInfo(
        currency=CurrencyInfo(symbol="UFAC", name="UFAC"), scaling=Decimal("1e-6")
    ),
    "0x0ff6ffcfda92c53f615a4a75d982f399c989366b": TokenInfo(
        currency=CurrencyInfo(symbol="LAYER", name="UniLayer"), scaling=Decimal("1e-18")
    ),
    "0x0ffe606f8a0f13c815ac5686241ab2bf3c9e5cff": TokenInfo(
        currency=CurrencyInfo(symbol="BABA.CX", name="Alibaba Group Holding"), scaling=Decimal("1e-8")
    ),
    "0x0fff95d5ab18c763c42c209f137c47354af104a8": TokenInfo(
        currency=CurrencyInfo(symbol="HXY", name="HEX Money"), scaling=Decimal("1e-8")
    ),
    "0x10010078a54396f62c96df8532dc2b4847d47ed3": TokenInfo(
        currency=CurrencyInfo(symbol="HND", name="Hundred Finance"), scaling=Decimal("1e-18")
    ),
    "0x1003ec54f51565ff86ac611184ea23d6310cae71": TokenInfo(
        currency=CurrencyInfo(symbol="ETA", name="ETH Trending Alpha LT Set II"), scaling=Decimal("1e-18")
    ),
    "0x10086399dd8c1e3de736724af52587a2044c9fa2": TokenInfo(
        currency=CurrencyInfo(symbol="TMTG", name="The Midas Touch Gold"), scaling=Decimal("1e-18")
    ),
    "0x1014613e2b3cbc4d575054d4982e580d9b99d7b1": TokenInfo(
        currency=CurrencyInfo(symbol="BCV", name="BitCapitalVendor"), scaling=Decimal("1e-8")
    ),
    "0x1017b147b05942ead495e2ad6d606ef3c94b8fd0": TokenInfo(
        currency=CurrencyInfo(symbol="VNL", name="Vanilla"), scaling=Decimal("1e-12")
    ),
    "0x101cc05f4a51c0319f570d5e146a8c625198e636": TokenInfo(
        currency=CurrencyInfo(symbol="ATUSD", name="Aave TUSD"), scaling=Decimal("1e-18")
    ),
    "0x1022a16994230272763d801cca849d4d122c814b": TokenInfo(
        currency=CurrencyInfo(symbol="LKOD.CX", name="Lukoil PJSC ADR"), scaling=Decimal("1e-8")
    ),
    "0x103c3a209da59d3e7c4a89307e66521e081cfdf0": TokenInfo(
        currency=CurrencyInfo(symbol="GVT", name="Genesis Vision"), scaling=Decimal("1e-18")
    ),
    "0x1051a014e4b3f2bd08e5a7e52522f0f71628162b": TokenInfo(
        currency=CurrencyInfo(symbol="OGODS", name="GOTOGODS"), scaling=Decimal("1e-18")
    ),
    "0x10633216e7e8281e33c86f02bf8e565a635d9770": TokenInfo(
        currency=CurrencyInfo(symbol="DVI", name="Dvision Network"), scaling=Decimal("1e-18")
    ),
    "0x1063ce524265d5a3a624f4914acd573dd89ce988": TokenInfo(
        currency=CurrencyInfo(symbol="AIX", name="Aigang"), scaling=Decimal("1e-18")
    ),
    "0x106538cc16f938776c7c180186975bca23875287": TokenInfo(
        currency=CurrencyInfo(symbol="BAS", name="Basis Share"), scaling=Decimal("1e-18")
    ),
    "0x106aa49295b525fcf959aa75ec3f7dcbf5352f1c": TokenInfo(
        currency=CurrencyInfo(symbol="RKT", name="Rock Token"), scaling=Decimal("1e-18")
    ),
    "0x106d8fb5775a57ae38a2ffb1441eb0963e09dba7": TokenInfo(
        currency=CurrencyInfo(symbol="TGBP", name="TrueGBP"), scaling=Decimal("1e-18")
    ),
    "0x1071ba8ada384c2b9b87f808e19dbb9aa4f0f88a": TokenInfo(
        currency=CurrencyInfo(symbol="SCTK", name="SharesChain"), scaling=Decimal("1e-18")
    ),
    "0x107c4504cd79c5d2696ea0030a8dd4e92601b82e": TokenInfo(
        currency=CurrencyInfo(symbol="BLT", name="Bloom"), scaling=Decimal("1e-18")
    ),
    "0x108d27f9c4b2a98c025c94c76ca78c6ce6c7a4eb": TokenInfo(
        currency=CurrencyInfo(symbol="METP", name="Metaprediction"), scaling=Decimal("1e-18")
    ),
    "0x10a34bbe9b3c5ad536ca23d5eefa81ca448e92ff": TokenInfo(
        currency=CurrencyInfo(symbol="DSYS", name="DSYS"), scaling=Decimal("1e-18")
    ),
    "0x10b123fddde003243199aad03522065dc05827a0": TokenInfo(
        currency=CurrencyInfo(symbol="SYN", name="Synapse"), scaling=Decimal("1e-18")
    ),
    "0x10ba8c420e912bf07bedac03aa6908720db04e0c": TokenInfo(
        currency=CurrencyInfo(symbol="RAISE", name="Raise Token"), scaling=Decimal("1e-18")
    ),
    "0x10bae51262490b4f4af41e12ed52a0e744c1137a": TokenInfo(
        currency=CurrencyInfo(symbol="SLINK", name="Soft Link"), scaling=Decimal("1e-9")
    ),
    "0x10bc518c32fbae5e38ecb50a612160571bd81e44": TokenInfo(
        currency=CurrencyInfo(symbol="VRO", name="VeraOne"), scaling=Decimal("1e-8")
    ),
    "0x10be9a8dae441d276a5027936c3aaded2d82bc15": TokenInfo(
        currency=CurrencyInfo(symbol="UMX", name="UniMex Network"), scaling=Decimal("1e-18")
    ),
    "0x10c71515602429c19d53011ea7040b87a4894838": TokenInfo(
        currency=CurrencyInfo(symbol="DPT", name="Diamond Platform Token"), scaling=Decimal("1e-18")
    ),
    "0x10d88d7495ca381df1391229bdb82d015b9ad17d": TokenInfo(
        currency=CurrencyInfo(symbol="BVA", name="Bavala"), scaling=Decimal("1e-18")
    ),
    "0x10ef64cb79fd4d75d4aa7e8502d95c42124e434b": TokenInfo(
        currency=CurrencyInfo(symbol="NCOV", name="NCOV"), scaling=Decimal("1e-18")
    ),
    "0x111111111117dc0aa78b770fa6a738034120c302": TokenInfo(
        currency=CurrencyInfo(symbol="1INCH", name="1inch"), scaling=Decimal("1e-18")
    ),
    "0x1122b6a0e00dce0563082b6e2953f3a943855c1f": TokenInfo(
        currency=CurrencyInfo(symbol="CENNZ", name="Centrality"), scaling=Decimal("1e-18")
    ),
    "0x1138d8b876bb048b72ec7cd222f6a282384b505a": TokenInfo(
        currency=CurrencyInfo(symbol="BRX", name="BEEREX"), scaling=Decimal("1e-18")
    ),
    "0x1148661869d30e095ff4aa48aa8b5eadedc75f2a": TokenInfo(
        currency=CurrencyInfo(symbol="BTC3S", name="Amun Bitcoin 3x Daily Short"), scaling=Decimal("1e-18")
    ),
    "0x114a86d31b8cb3867040b48e7c17d5d04d886ce0": TokenInfo(
        currency=CurrencyInfo(symbol="UPB", name="UPBTC Token"), scaling=Decimal("1e-8")
    ),
    "0x115ec79f1de567ec68b7ae7eda501b406626478e": TokenInfo(
        currency=CurrencyInfo(symbol="CRE", name="Carry"), scaling=Decimal("1e-18")
    ),
    "0x1183f92a5624d68e85ffb9170f16bf0443b4c242": TokenInfo(
        currency=CurrencyInfo(symbol="QVT", name="Qvolta"), scaling=Decimal("1e-18")
    ),
    "0x11905b73cc08c6d96a9012b4edf45b03243503b8": TokenInfo(
        currency=CurrencyInfo(symbol="PXU", name="Planemo Xchange Utility"), scaling=Decimal("1e-2")
    ),
    "0x11a2ab94ade17e96197c78f9d5f057332a19a0b9": TokenInfo(
        currency=CurrencyInfo(symbol="ORBI", name="Orbicular"), scaling=Decimal("1e-9")
    ),
    "0x11afe7fa792589dd1236257f99ba09f510460ad9": TokenInfo(
        currency=CurrencyInfo(symbol="LNKO", name="LNKO Token"), scaling=Decimal("1e-8")
    ),
    "0x11b0a8c0fa626627601ed518c3538a39d92d609e": TokenInfo(
        currency=CurrencyInfo(symbol="YGY", name="Generation of Yield"), scaling=Decimal("1e-6")
    ),
    "0x11b79147ab4af4c6c1785cf23672a2e3e5ba24a4": TokenInfo(
        currency=CurrencyInfo(symbol="NTR", name="Neutritium"), scaling=Decimal("1e-18")
    ),
    "0x11bf1d3b4d4700ae43b3839ab0d8a218dd15c707": TokenInfo(
        currency=CurrencyInfo(symbol="CHK.CX", name="Chesapeake Energy Corp"), scaling=Decimal("1e-8")
    ),
    "0x11dd5dddd1bd9b2df6ff908fbcf8db09cefed29b": TokenInfo(
        currency=CurrencyInfo(symbol="TPP", name="Trusted Property Protocol"), scaling=Decimal("1e-12")
    ),
    "0x11e0b97730a67e6dfb8a917ce9a464bf6fb1abe0": TokenInfo(
        currency=CurrencyInfo(symbol="IZB", name="IzerBlack"), scaling=Decimal("1e-8")
    ),
    "0x11eef04c884e24d9b7b4760e7476d06ddf797f36": TokenInfo(
        currency=CurrencyInfo(symbol="MX", name="MX Token"), scaling=Decimal("1e-18")
    ),
    "0x11f4c6b3e8f50c50935c7889edc56c96f41b5399": TokenInfo(
        currency=CurrencyInfo(symbol="YBREE", name="Yield Breeder DAO"), scaling=Decimal("1e-18")
    ),
    "0x121c6e0613317a98cc14a9d379e2abe546ba980c": TokenInfo(
        currency=CurrencyInfo(symbol="PELO", name="Pelo Coin"), scaling=Decimal("1e-18")
    ),
    "0x122a86b5dff2d085afb49600b4cd7375d0d94a5f": TokenInfo(
        currency=CurrencyInfo(symbol="ITL", name="Italian Lira"), scaling=Decimal("1e-8")
    ),
    "0x123151402076fc819b7564510989e475c9cd93ca": TokenInfo(
        currency=CurrencyInfo(symbol="WDGLD", name="Wrapped-DGLD"), scaling=Decimal("1e-8")
    ),
    "0x1234567461d3f8db7496581774bd869c83d51c93": TokenInfo(
        currency=CurrencyInfo(symbol="CAT", name="BitClave"), scaling=Decimal("1e-18")
    ),
    "0x1239562abe89ff62016ae23d4e6eef12b915295c": TokenInfo(
        currency=CurrencyInfo(symbol="APX", name="Apex"), scaling=Decimal("1e-18")
    ),
    "0x123ab195dd38b1b40510d467a6a359b201af056f": TokenInfo(
        currency=CurrencyInfo(symbol="LGO", name="LGO Token"), scaling=Decimal("1e-8")
    ),
    "0x12419eea0b053ffea92f9afcd7986a495e2cf0dd": TokenInfo(
        currency=CurrencyInfo(symbol="ONEZ", name="The Nifty ONEz"), scaling=Decimal("1e-18")
    ),
    "0x1245712fb154f7233e496e21edb61f89c63e7878": TokenInfo(
        currency=CurrencyInfo(symbol="INTC.CX", name="Intel Corporation"), scaling=Decimal("1e-8")
    ),
    "0x1245ef80f4d9e02ed9425375e8f649b9221b31d8": TokenInfo(
        currency=CurrencyInfo(symbol="ARCT", name="ArbitrageCT"), scaling=Decimal("1e-8")
    ),
    "0x1254e59712e6e727dc71e0e3121ae952b2c4c3b6": TokenInfo(
        currency=CurrencyInfo(symbol="MRS", name="Marginless"), scaling=Decimal("1e-18")
    ),
    "0x125f9d5daa039bdb79d36baff667e9e0bbcea998": TokenInfo(
        currency=CurrencyInfo(symbol="FIRE", name="FireToken"), scaling=Decimal("1e-18")
    ),
    "0x12683dc9eec95a5f742d40206e73319e6b9d8a91": TokenInfo(
        currency=CurrencyInfo(symbol="FAB", name="FABRK Token"), scaling=Decimal("1e-18")
    ),
    "0x126c121f99e1e211df2e5f8de2d96fa36647c855": TokenInfo(
        currency=CurrencyInfo(symbol="DEGEN", name="DEGEN Index"), scaling=Decimal("1e-18")
    ),
    "0x12759512d326303b45f1cec8f7b6fd96f387778e": TokenInfo(
        currency=CurrencyInfo(symbol="TRAK", name="TrakInvest"), scaling=Decimal("1e-18")
    ),
    "0x1279c15969bb2007ec075c7d19f55de3e3da3807": TokenInfo(
        currency=CurrencyInfo(symbol="SOLM", name="Solereum"), scaling=Decimal("1e-18")
    ),
    "0x1295b55fa04fbac6d9e7c351ecb3486e88129027": TokenInfo(
        currency=CurrencyInfo(symbol="LIGHT", name="LightChain"), scaling=Decimal("1e-8")
    ),
    "0x12b19d3e2ccc14da04fae33e63652ce469b3f2fd": TokenInfo(
        currency=CurrencyInfo(symbol="GRID", name="GridPlus"), scaling=Decimal("1e-12")
    ),
    "0x12b2b2331a72d375c453c160b2c8a7010eea510a": TokenInfo(
        currency=CurrencyInfo(symbol="GUBI", name="GUBI"), scaling=Decimal("1e-18")
    ),
    "0x12b306fa98f4cbb8d4457fdff3a0a0a56f07ccdf": TokenInfo(
        currency=CurrencyInfo(symbol="SXDT", name="Spectre.ai Dividend Token"), scaling=Decimal("1e-18")
    ),
    "0x12b98c621e8754ae70d0fdbbc73d6208bc3e3ca6": TokenInfo(
        currency=CurrencyInfo(symbol="idleUSDCYield", name="IdleUSDC v3 [Max yield]"), scaling=Decimal("1e-18")
    ),
    "0x12bb890508c125661e03b09ec06e404bc9289040": TokenInfo(
        currency=CurrencyInfo(symbol="RACA", name="Radio Caca"), scaling=Decimal("1e-18")
    ),
    "0x12c5e73ddb44cd70225669b9f6f0d9de5455bc31": TokenInfo(
        currency=CurrencyInfo(symbol="IDON", name="Idoneus Token"), scaling=Decimal("1e-18")
    ),
    "0x12c8b0914e6dee22c7557a0a8b928ae6cacfbcf7": TokenInfo(
        currency=CurrencyInfo(symbol="STRX", name="Storex"), scaling=Decimal("1e-18")
    ),
    "0x12dc767728105aa415dd720dfbd0ea1d85841172": TokenInfo(
        currency=CurrencyInfo(symbol="ERD", name="ELDORADO TOKEN"), scaling=Decimal("1e-2")
    ),
    "0x12e51e77daaa58aa0e9247db7510ea4b46f9bead": TokenInfo(
        currency=CurrencyInfo(symbol="AYFI", name="Aave YFI"), scaling=Decimal("1e-18")
    ),
    "0x12f649a9e821f90bb143089a6e56846945892ffb": TokenInfo(
        currency=CurrencyInfo(symbol="UDOO", name="Hyprr (Howdoo)"), scaling=Decimal("1e-18")
    ),
    "0x12fcd6463e66974cf7bbc24ffc4d40d6be458283": TokenInfo(
        currency=CurrencyInfo(symbol="GBX", name="Globitex"), scaling=Decimal("1e-8")
    ),
    "0x12fef5e57bf45873cd9b62e9dbd7bfb99e32d73e": TokenInfo(
        currency=CurrencyInfo(symbol="CFI", name="Cofound.it"), scaling=Decimal("1e-18")
    ),
    "0x130914e1b240a7f4c5d460b7d3a2fd3846b576fa": TokenInfo(
        currency=CurrencyInfo(symbol="ANG", name="Aureus Nummus Gold"), scaling=Decimal("1e-18")
    ),
    "0x13119e34e140097a507b07a5564bde1bc375d9e6": TokenInfo(
        currency=CurrencyInfo(symbol="IMT", name="MoneyToken"), scaling=Decimal("1e-18")
    ),
    "0x1320c8c64b9f2eaa851f70702e6c9fc1ee4e8ce4": TokenInfo(
        currency=CurrencyInfo(symbol="MSRM", name="MegaSerum"), scaling=Decimal("1e-6")
    ),
    "0x1321f1f1aa541a56c31682c57b80ecfccd9bb288": TokenInfo(
        currency=CurrencyInfo(symbol="ARCX", name="ARC Governance"), scaling=Decimal("1e-18")
    ),
    "0x13339fd07934cd674269726edf3b5ccee9dd93de": TokenInfo(
        currency=CurrencyInfo(symbol="CUR", name="Curio"), scaling=Decimal("1e-18")
    ),
    "0x1337def16f9b486faed0293eb623dc8395dfe46a": TokenInfo(
        currency=CurrencyInfo(symbol="ARMOR", name="ARMOR"), scaling=Decimal("1e-18")
    ),
    "0x1337def18c680af1f9f45cbcab6309562975b1dd": TokenInfo(
        currency=CurrencyInfo(symbol="ARNXM", name="Armor NXM"), scaling=Decimal("1e-18")
    ),
    "0x135093731f61dd5cbfd7744751bf3ced3aaa69b1": TokenInfo(
        currency=CurrencyInfo(symbol="HNTC", name="HNT Chain"), scaling=Decimal("1e-18")
    ),
    "0x1351e42b173061168e7fbc6c032820fa4eaf3170": TokenInfo(
        currency=CurrencyInfo(symbol="PRMI", name="PrmiChain"), scaling=Decimal("1e-18")
    ),
    "0x13526d323373f4ebfcc71ffb4177efead651c051": TokenInfo(
        currency=CurrencyInfo(symbol="ACH", name="Automatic Clearing High Speed"), scaling=Decimal("1e-18")
    ),
    "0x13550b383cb73b1731fced06c5aa86ed7800adb9": TokenInfo(
        currency=CurrencyInfo(symbol="SHOP.CX", name="Shopify Cl A Sub Vtg"), scaling=Decimal("1e-8")
    ),
    "0x135bacd9261b9b5d2aae6645168fee45d8e57547": TokenInfo(
        currency=CurrencyInfo(symbol="BMAX", name="BitcoinMax"), scaling=Decimal("1e-18")
    ),
    "0x136723300aef2aab4b7cf52c3eaac6f997e12a68": TokenInfo(
        currency=CurrencyInfo(symbol="HAI", name="Hai Chain"), scaling=Decimal("1e-8")
    ),
    "0x136fae4333ea36a24bb751e2d505d6ca4fd9f00b": TokenInfo(
        currency=CurrencyInfo(symbol="ETHRSIAPY", name="ETH RSI 60/40 Yield Set"), scaling=Decimal("1e-18")
    ),
    "0x1378ec93ab2b07ba5a0eaef19cf354a33f64b9fd": TokenInfo(
        currency=CurrencyInfo(symbol="YFDT", name="Yearn Finance Diamond Token"), scaling=Decimal("1e-18")
    ),
    "0x137cee63f06ca413ca51d485fe98b0d12bacfa14": TokenInfo(
        currency=CurrencyInfo(symbol="TGBP", name="TrueGBP"), scaling=Decimal("1e-18")
    ),
    "0x138537ddba70ab69c05497b89ee2e34f9201dcec": TokenInfo(
        currency=CurrencyInfo(symbol="SML", name="ShahinMedical"), scaling=Decimal("1e-18")
    ),
    "0x138a8752093f4f9a79aaedf48d4b9248fab93c9c": TokenInfo(
        currency=CurrencyInfo(symbol="MCI", name="Musiconomi"), scaling=Decimal("1e-18")
    ),
    "0x138d02c0c59c6d6ac480218e5585cd97f54e3516": TokenInfo(
        currency=CurrencyInfo(symbol="BMX", name="BMX Token"), scaling=Decimal("1e-18")
    ),
    "0x138fd9a2b4b283676109d5e76cf3b83de7d15f25": TokenInfo(
        currency=CurrencyInfo(symbol="ZNT", name="Zero Protocol Token"), scaling=Decimal("1e-8")
    ),
    "0x1397688ec12d9e556529008d88723d7c6c58e152": TokenInfo(
        currency=CurrencyInfo(symbol="LKB", name="Lab Keyboard Business"), scaling=Decimal("1e-18")
    ),
    "0x139d9397274bb9e2c29a9aa8aa0b5874d30d62e3": TokenInfo(
        currency=CurrencyInfo(symbol="BOUTS", name="BoutsPro"), scaling=Decimal("1e-18")
    ),
    "0x13b02c8de71680e71f0820c996e4be43c2f57d15": TokenInfo(
        currency=CurrencyInfo(symbol="MQQQ", name="Mirrored Invesco QQQ Trust"), scaling=Decimal("1e-18")
    ),
    "0x13b2f6928d7204328b0e8e4bcd0379aa06ea21fa": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMWBTC", name="Aave AMM WBTC"), scaling=Decimal("1e-8")
    ),
    "0x13c2fab6354d3790d8ece4f0f1a3280b4a25ad96": TokenInfo(
        currency=CurrencyInfo(symbol="PHI", name="PHI TOKEN"), scaling=Decimal("1e-18")
    ),
    "0x13ca8eb6405cfbe2eae5d00207651002083fbc9d": TokenInfo(
        currency=CurrencyInfo(symbol="C2O", name="CryptoWater"), scaling=Decimal("1e-2")
    ),
    "0x13cb835c47782dad075ce7faa1f8439b548b712d": TokenInfo(
        currency=CurrencyInfo(symbol="LENS", name="LENS Platform"), scaling=Decimal("1e-8")
    ),
    "0x13cb85823f78cff38f0b0e90d3e975b8cb3aad64": TokenInfo(
        currency=CurrencyInfo(symbol="REMI", name="REMIIT"), scaling=Decimal("1e-18")
    ),
    "0x13cea0680b3ffecb835758046cc1dfe9080dbad5": TokenInfo(
        currency=CurrencyInfo(symbol="YFN", name="YearnFinanceNetwork"), scaling=Decimal("1e-18")
    ),
    "0x13d0bf45e5f319fa0b58900807049f23cae7c40d": TokenInfo(
        currency=CurrencyInfo(symbol="READ", name="Read"), scaling=Decimal("1e-8")
    ),
    "0x13d71cfc90a83cd1cc0e59675c3f4b90d4162a8b": TokenInfo(
        currency=CurrencyInfo(symbol="SWIPE", name="SWIPE Network"), scaling=Decimal("1e-8")
    ),
    "0x13db74b3cf512f65c4b91683940b4f3955e05085": TokenInfo(
        currency=CurrencyInfo(symbol="SKE", name="Super Keep Token"), scaling=Decimal("1e-8")
    ),
    "0x13de0b0c1507d424fad4c6212830a0b2e59587c5": TokenInfo(
        currency=CurrencyInfo(symbol="WISH", name="WishChain"), scaling=Decimal("1e-18")
    ),
    "0x13df4d4521a09f45554475bb086c099e3732cb99": TokenInfo(
        currency=CurrencyInfo(symbol="XN35", name="Projecton"), scaling=Decimal("1e-18")
    ),
    "0x13f11c9905a08ca76e3e853be63d4f0944326c72": TokenInfo(
        currency=CurrencyInfo(symbol="DIVX", name="Divi Exchange Token"), scaling=Decimal("1e-18")
    ),
    "0x13f1b7fdfbe1fc66676d56483e21b1ecb40b58e2": TokenInfo(
        currency=CurrencyInfo(symbol="ACC", name="Accelerator Network"), scaling=Decimal("1e-18")
    ),
    "0x13f25cd52b21650caa8225c9942337d914c9b030": TokenInfo(
        currency=CurrencyInfo(symbol="RCT", name="RealChain"), scaling=Decimal("1e-18")
    ),
    "0x14094949152eddbfcd073717200da82fed8dc960": TokenInfo(
        currency=CurrencyInfo(symbol="IDAI", name="bZx DAI iToken"), scaling=Decimal("1e-18")
    ),
    "0x1410434b0346f5be678d0fb554e5c7ab620f8f4a": TokenInfo(
        currency=CurrencyInfo(symbol="KAN", name="BitKan"), scaling=Decimal("1e-18")
    ),
    "0x1412f6aa5adc77c620715bb2a020aa690b85f68a": TokenInfo(
        currency=CurrencyInfo(symbol="MGX", name="MargiX"), scaling=Decimal("1e-18")
    ),
    "0x141abb03f001deded9a0223d4ff26d929117b72e": TokenInfo(
        currency=CurrencyInfo(symbol="HV", name="HighVibe Token"), scaling=Decimal("1e-18")
    ),
    "0x14409b0fc5c7f87b5dad20754fe22d29a3de8217": TokenInfo(
        currency=CurrencyInfo(symbol="PYRO", name="PYRO Network"), scaling=Decimal("1e-18")
    ),
    "0x14449de7937fe1c1207006e92f89dee17bbe418a": TokenInfo(
        currency=CurrencyInfo(symbol="MLC", name="Melecoin"), scaling=Decimal("1e-18")
    ),
    "0x14468ff6b324f1c5a869e62b9c442846e7d0baf1": TokenInfo(
        currency=CurrencyInfo(symbol="MAYA", name="Maya Coin"), scaling=Decimal("1e-18")
    ),
    "0x1453dbb8a29551ade11d89825ca812e05317eaeb": TokenInfo(
        currency=CurrencyInfo(symbol="TEND", name="Tendies"), scaling=Decimal("1e-18")
    ),
    "0x1456688345527be1f37e9e627da0837d6f08c925": TokenInfo(
        currency=CurrencyInfo(symbol="USDP", name="USDP Stablecoin"), scaling=Decimal("1e-18")
    ),
    "0x145b4467b2fa0faf4296f165bca214691a5e08d6": TokenInfo(
        currency=CurrencyInfo(symbol="IDD", name="Indian Digital Dollar"), scaling=Decimal("1e-8")
    ),
    "0x1460a58096d80a50a2f1f956dda497611fa4f165": TokenInfo(
        currency=CurrencyInfo(symbol="CHX", name="WeOwn"), scaling=Decimal("1e-18")
    ),
    "0x146d8d942048ad517479c9bab1788712af180fde": TokenInfo(
        currency=CurrencyInfo(symbol="MIB", name="MIB Coin"), scaling=Decimal("1e-18")
    ),
    "0x147faf8de9d8d8daae129b187f0d02d819126750": TokenInfo(
        currency=CurrencyInfo(symbol="GEO", name="GeoDB"), scaling=Decimal("1e-18")
    ),
    "0x148fabfe726359fa8eb5d72eb270773e3f5c507d": TokenInfo(
        currency=CurrencyInfo(symbol="BITW", name="Bitwires"), scaling=Decimal("1e-18")
    ),
    "0x14903ad104da65729b99bbd64c47fb7d75f8548a": TokenInfo(
        currency=CurrencyInfo(symbol="DZC", name="D-ZONE COIN"), scaling=Decimal("1e-8")
    ),
    "0x149088326be49ca948988f44fcf65c0c4d248b16": TokenInfo(
        currency=CurrencyInfo(symbol="PBR.CX", name="Petroleo Brasileiro SA"), scaling=Decimal("1e-8")
    ),
    "0x1494ca1f11d487c2bbe4543e90080aeba4ba3c2b": TokenInfo(
        currency=CurrencyInfo(symbol="DPI", name="DeFiPulse Index"), scaling=Decimal("1e-18")
    ),
    "0x14aa9c36d76901fe1ebcc860038aee9318596103": TokenInfo(
        currency=CurrencyInfo(symbol="JBC", name="Junk Bond Capital"), scaling=Decimal("1e-8")
    ),
    "0x14c926f2290044b647e1bf2072e67b495eff1905": TokenInfo(
        currency=CurrencyInfo(symbol="BETHER", name="Bethereum"), scaling=Decimal("1e-18")
    ),
    "0x14ca41eecd7d81d5d13098586c0d2314eba285be": TokenInfo(
        currency=CurrencyInfo(symbol="JUS", name="JUST NETWORK"), scaling=Decimal("1e-18")
    ),
    "0x14d10003807ac60d07bb0ba82caeac8d2087c157": TokenInfo(
        currency=CurrencyInfo(symbol="IDEFI", name="iDeFi"), scaling=Decimal("1e-18")
    ),
    "0x14d9444f6b9d55caba5d73f15bea947695c11c82": TokenInfo(
        currency=CurrencyInfo(symbol="LP", name="LeoPard Coin"), scaling=Decimal("1e-9")
    ),
    "0x14da230d6726c50f759bc1838717f8ce6373509c": TokenInfo(
        currency=CurrencyInfo(symbol="KAT", name="Kambria"), scaling=Decimal("1e-18")
    ),
    "0x14ddda446688b73161aa1382f4e4343353af6fc8": TokenInfo(
        currency=CurrencyInfo(symbol="FXP", name="FXPay"), scaling=Decimal("1e-8")
    ),
    "0x14dffd4f515d4c43493c6c512c78fbc59a8af254": TokenInfo(
        currency=CurrencyInfo(symbol="AFC", name="Anti-Fraud Chain"), scaling=Decimal("1e-18")
    ),
    "0x14eb60f5f270b059b0c788de0ddc51da86f8a06d": TokenInfo(
        currency=CurrencyInfo(symbol="KCAL", name="Phantasma Energy"), scaling=Decimal("1e-10")
    ),
    "0x14f0a12a43c36c49d4b403dd6e1a9b8222be456c": TokenInfo(
        currency=CurrencyInfo(symbol="VXC", name="VINX COIN"), scaling=Decimal("1e-18")
    ),
    "0x14f37b574242d366558db61f3335289a5035c506": TokenInfo(
        currency=CurrencyInfo(symbol="HKG", name="Hacker Gold"), scaling=Decimal("1e-3")
    ),
    "0x150b0b96933b75ce27af8b92441f8fb683bf9739": TokenInfo(
        currency=CurrencyInfo(symbol="GOLD", name="Dragonereum GOLD"), scaling=Decimal("1e-18")
    ),
    "0x151202c9c18e495656f372281f493eb7698961d5": TokenInfo(
        currency=CurrencyInfo(symbol="DEB", name="Debitum Network"), scaling=Decimal("1e-18")
    ),
    "0x15223c63a203731db1a2ebfe5277a55f77a453b9": TokenInfo(
        currency=CurrencyInfo(symbol="IQF", name="IQF Token"), scaling=Decimal("1e-8")
    ),
    "0x152687bc4a7fcc89049cf119f9ac3e5acf2ee7ef": TokenInfo(
        currency=CurrencyInfo(symbol="DHC", name="DeltaHub Community"), scaling=Decimal("1e-18")
    ),
    "0x15334dcb171e8b65d6650321581dca83be870115": TokenInfo(
        currency=CurrencyInfo(symbol="WBIND", name="Wrapped BIND"), scaling=Decimal("1e-8")
    ),
    "0x153ed9cc1b792979d2bde0bbf45cc2a7e436a5f9": TokenInfo(
        currency=CurrencyInfo(symbol="XOV", name="XOVBank"), scaling=Decimal("1e-18")
    ),
    "0x1543d0f83489e82a1344df6827b23d541f235a50": TokenInfo(
        currency=CurrencyInfo(symbol="ATH", name="AIgatha Token"), scaling=Decimal("1e-18")
    ),
    "0x155040625d7ae3e9cada9a73e3e44f76d3ed1409": TokenInfo(
        currency=CurrencyInfo(symbol="REVO", name="Revomon"), scaling=Decimal("1e-18")
    ),
    "0x155085e375f53ec2a15c6f372804abf7dbcd11da": TokenInfo(
        currency=CurrencyInfo(symbol="TRIP.CX", name="TripAdvisor, Inc."), scaling=Decimal("1e-8")
    ),
    "0x1559fa1b8f28238fd5d76d9f434ad86fd20d1559": TokenInfo(
        currency=CurrencyInfo(symbol="EDEN", name="EDEN"), scaling=Decimal("1e-18")
    ),
    "0x1563d521ba309e2ad9f4affd6f4de9759e8d4f21": TokenInfo(
        currency=CurrencyInfo(symbol="VNX", name="VisionX"), scaling=Decimal("1e-18")
    ),
    "0x15771207d92b34f585bae076dcf3fb34418afdcd": TokenInfo(
        currency=CurrencyInfo(symbol="RRW", name="RRW"), scaling=Decimal("1e-5")
    ),
    "0x158079ee67fce2f58472a96584a73c7ab9ac95c1": TokenInfo(
        currency=CurrencyInfo(symbol="CREP", name="cREP"), scaling=Decimal("1e-8")
    ),
    "0x159751323a9e0415dd3d6d42a1212fe9f4a0848c": TokenInfo(
        currency=CurrencyInfo(symbol="INFI", name="Insured Finance"), scaling=Decimal("1e-18")
    ),
    "0x159a1dfae19057de57dfffcbb3da1ae784678965": TokenInfo(
        currency=CurrencyInfo(symbol="RFX", name="Reflex"), scaling=Decimal("1e-8")
    ),
    "0x15b7c0c907e4c6b9adaaaabc300c08991d6cea05": TokenInfo(
        currency=CurrencyInfo(symbol="GEL", name="Gelato"), scaling=Decimal("1e-18")
    ),
    "0x15bcdfad12498de8a922e62442ae4cc4bd33bd25": TokenInfo(
        currency=CurrencyInfo(symbol="WALT", name="Walletreum"), scaling=Decimal("1e-18")
    ),
    "0x15bda08c3afbf5955d6e9b235fd55a1fd0dbc829": TokenInfo(
        currency=CurrencyInfo(symbol="APC", name="Alpha Coin"), scaling=Decimal("1e-6")
    ),
    "0x15c303b84045f67156acf6963954e4247b526717": TokenInfo(
        currency=CurrencyInfo(symbol="GCBN", name="Gas Cash Back"), scaling=Decimal("1e-18")
    ),
    "0x15d4c048f83bd7e37d49ea4c83a07267ec4203da": TokenInfo(
        currency=CurrencyInfo(symbol="GALA", name="Gala"), scaling=Decimal("1e-8")
    ),
    "0x15eabb7500e44b7fdb6e4051ca8deca430cf9fb8": TokenInfo(
        currency=CurrencyInfo(symbol="DXF", name="Dexfin"), scaling=Decimal("1e-18")
    ),
    "0x15ef5b9447710eab904e63e6233ff540400d603f": TokenInfo(
        currency=CurrencyInfo(symbol="BTC2X", name="Bitcoin2x"), scaling=Decimal("1e-8")
    ),
    "0x1602af2c782cc03f9241992e243290fccf73bb13": TokenInfo(
        currency=CurrencyInfo(symbol="QBIT", name="Qubitica"), scaling=Decimal("1e-18")
    ),
    "0x1614f18fc94f47967a3fbe5ffcd46d4e7da3d787": TokenInfo(
        currency=CurrencyInfo(symbol="PAID", name="PAID Network"), scaling=Decimal("1e-18")
    ),
    "0x163733bcc28dbf26b41a8cfa83e369b5b3af741b": TokenInfo(
        currency=CurrencyInfo(symbol="PRS", name="Persian"), scaling=Decimal("1e-18")
    ),
    "0x1640bd2898eee4c36f369836a067dea8725ac0cc": TokenInfo(
        currency=CurrencyInfo(symbol="DFO", name="DeFiato"), scaling=Decimal("1e-8")
    ),
    "0x16484d73ac08d2355f466d448d2b79d2039f6ebb": TokenInfo(
        currency=CurrencyInfo(symbol="FKX", name="FortKnoxster"), scaling=Decimal("1e-18")
    ),
    "0x165440036ce972c5f8ebef667086707e48b2623e": TokenInfo(
        currency=CurrencyInfo(symbol="GRAPH", name="UniGraph"), scaling=Decimal("1e-18")
    ),
    "0x16558553e4647ca500c3718c56c356edb6f9b11c": TokenInfo(
        currency=CurrencyInfo(symbol="MKT", name="Monkey King Token"), scaling=Decimal("1e-6")
    ),
    "0x16662f73df3e79e54c6c5938b4313f92c524c120": TokenInfo(
        currency=CurrencyInfo(symbol="IIC", name="Ibiscoin"), scaling=Decimal("1e-18")
    ),
    "0x1673a63aa0047294d75954226f3f2f98de77b16f": TokenInfo(
        currency=CurrencyInfo(symbol="GENES", name="GENES Chain"), scaling=Decimal("1e-18")
    ),
    "0x1680cfdad75da2bb56ded4f36bb9423c86ffa7b7": TokenInfo(
        currency=CurrencyInfo(symbol="WTP", name="Web Token Pay"), scaling=Decimal("1e-18")
    ),
    "0x168296bb09e24a88805cb9c33356536b980d3fc5": TokenInfo(
        currency=CurrencyInfo(symbol="RHOC", name="RHOC"), scaling=Decimal("1e-8")
    ),
    "0x1695936d6a953df699c38ca21c2140d497c08bd9": TokenInfo(
        currency=CurrencyInfo(symbol="SYN", name="SynLev"), scaling=Decimal("1e-18")
    ),
    "0x16980b3b4a3f9d89e33311b5aa8f80303e5ca4f8": TokenInfo(
        currency=CurrencyInfo(symbol="KEX", name="KIRA Network"), scaling=Decimal("1e-6")
    ),
    "0x16987c021c14ca1045cd0afebb33c124a58bf16c": TokenInfo(
        currency=CurrencyInfo(symbol="VGR", name="Voyager"), scaling=Decimal("1e-2")
    ),
    "0x16af5bfb4ae7e475b9adc3bf5cb2f1e6a50d7940": TokenInfo(
        currency=CurrencyInfo(symbol="XFS", name="Fanship"), scaling=Decimal("1e-8")
    ),
    "0x16b00b9d7b54406625eed1044e009b5a4b3ad710": TokenInfo(
        currency=CurrencyInfo(symbol="PTS", name="Protogonos"), scaling=Decimal("1e-18")
    ),
    "0x16b0a1a87ae8af5c792fabc429c4fe248834842b": TokenInfo(
        currency=CurrencyInfo(symbol="ALG", name="Algory"), scaling=Decimal("1e-18")
    ),
    "0x16b0e62ac13a2faed36d18bce2356d25ab3cfad3": TokenInfo(
        currency=CurrencyInfo(symbol="BTQ", name="Bitcoin Boutique"), scaling=Decimal("1e-18")
    ),
    "0x16b1eb8b8e9058800bf0ba3684f805a6711a1d2c": TokenInfo(
        currency=CurrencyInfo(symbol="RFCTR", name="Reflector.Finance"), scaling=Decimal("1e-9")
    ),
    "0x16bc74c21420b377cef9e03defae8beef647bee9": TokenInfo(
        currency=CurrencyInfo(symbol="SNP", name="security prime"), scaling=Decimal("1e-18")
    ),
    "0x16be21c08eb27953273608629e4397556c561d26": TokenInfo(
        currency=CurrencyInfo(symbol="YMF20", name="Yearn20Moon.Finance"), scaling=Decimal("1e-8")
    ),
    "0x16c1e5baf21b9fa4bc9f2c374e4dc19fab5ac5dc": TokenInfo(
        currency=CurrencyInfo(symbol="APOT", name="APOT"), scaling=Decimal("1e-18")
    ),
    "0x16c9cf62d8dac4a38fb50ae5fa5d51e9170f3179": TokenInfo(
        currency=CurrencyInfo(symbol="DUSDC", name="dForce USDC"), scaling=Decimal("1e-6")
    ),
    "0x16cda4028e9e872a38acb903176719299beaed87": TokenInfo(
        currency=CurrencyInfo(symbol="MARS4", name="MARS4"), scaling=Decimal("1e-18")
    ),
    "0x16d1b0c11a2ed71ea430c3dc1201f66444531536": TokenInfo(
        currency=CurrencyInfo(symbol="BLUE.CX", name="Bluebird Bio Inc"), scaling=Decimal("1e-8")
    ),
    "0x16de59092dae5ccf4a1e6439d611fd0653f0bd01": TokenInfo(
        currency=CurrencyInfo(symbol="yDAI", name="iearn DAI"), scaling=Decimal("1e-18")
    ),
    "0x16ea01acb4b0bca2000ee5473348b6937ee6f72f": TokenInfo(
        currency=CurrencyInfo(symbol="ENQ", name="Enecuum"), scaling=Decimal("1e-10")
    ),
    "0x16eccfdbb4ee1a85a33f3a9b21175cd7ae753db4": TokenInfo(
        currency=CurrencyInfo(symbol="ROUTE", name="Router Protocol"), scaling=Decimal("1e-18")
    ),
    "0x16f22eed5dcced8bf57d28834a75a76ff5520206": TokenInfo(
        currency=CurrencyInfo(symbol="DNX", name="Den-X"), scaling=Decimal("1e-18")
    ),
    "0x16f812be7fff02caf662b85d5d58a5da6572d4df": TokenInfo(
        currency=CurrencyInfo(symbol="UTT", name="United Traders Token"), scaling=Decimal("1e-8")
    ),
    "0x17052d51e954592c1046320c2371abab6c73ef10": TokenInfo(
        currency=CurrencyInfo(symbol="ATH", name="Athenian Warrior Elite Token"), scaling=Decimal("1e-18")
    ),
    "0x1706c33b9a5b12aeb85b862215378dee9480eb95": TokenInfo(
        currency=CurrencyInfo(symbol="YBAN", name="BananoDOS"), scaling=Decimal("1e-18")
    ),
    "0x170b275ced089fffaebfe927f445a350ed9160dc": TokenInfo(
        currency=CurrencyInfo(symbol="OWN", name="OWNDATA"), scaling=Decimal("1e-8")
    ),
    "0x171d750d42d661b62c277a6b486adb82348c3eca": TokenInfo(
        currency=CurrencyInfo(symbol="ECOM", name="Omnitude"), scaling=Decimal("1e-18")
    ),
    "0x171f9cfc136f2b2aaa148fcc6b660a2029bab048": TokenInfo(
        currency=CurrencyInfo(symbol="AUS", name="Gold Standard"), scaling=Decimal("1e-4")
    ),
    "0x1736fae428eb944a4f0c22016fb60b7ec3a93d41": TokenInfo(
        currency=CurrencyInfo(symbol="DSPC", name="DongDongChain"), scaling=Decimal("1e-18")
    ),
    "0x174897edd3ce414084a009d22db31c7b7826400d": TokenInfo(
        currency=CurrencyInfo(symbol="JOON", name="JOON"), scaling=Decimal("1e-4")
    ),
    "0x174bea2cb8b20646681e855196cf34fcecec2489": TokenInfo(
        currency=CurrencyInfo(symbol="FTT", name="FreeTip"), scaling=Decimal("1e-18")
    ),
    "0x174bfa6600bf90c885c7c01c7031389ed1461ab9": TokenInfo(
        currency=CurrencyInfo(symbol="MGC", name="MGC Token"), scaling=Decimal("1e-18")
    ),
    "0x17525e4f4af59fbc29551bc4ece6ab60ed49ce31": TokenInfo(
        currency=CurrencyInfo(symbol="YPIE", name="PieDAO Yearn Ecosystem Pie"), scaling=Decimal("1e-18")
    ),
    "0x17540494ad5e39aefd49901774528e9ff17fe40b": TokenInfo(
        currency=CurrencyInfo(symbol="PRIVATE", name="Buccaneer"), scaling=Decimal("1e-3")
    ),
    "0x175ab41e2cedf3919b2e4426c19851223cf51046": TokenInfo(
        currency=CurrencyInfo(symbol="BACON", name="BaconSwap"), scaling=Decimal("1e-18")
    ),
    "0x1776e1f26f98b1a5df9cd347953a26dd3cb46671": TokenInfo(
        currency=CurrencyInfo(symbol="NMR", name="Numeraire"), scaling=Decimal("1e-18")
    ),
    "0x1778fffbd431be2ac3d69e64d1d819c786b2bee0": TokenInfo(
        currency=CurrencyInfo(symbol="GCG", name="Global Crypto Gate"), scaling=Decimal("1e-8")
    ),
    "0x177ba0cac51bfc7ea24bad39d81dcefd59d74faa": TokenInfo(
        currency=CurrencyInfo(symbol="KIF", name="KittenFinance"), scaling=Decimal("1e-18")
    ),
    "0x177d39ac676ed1c67a2b268ad7f1e58826e5b0af": TokenInfo(
        currency=CurrencyInfo(symbol="CDT", name="Blox"), scaling=Decimal("1e-18")
    ),
    "0x1788430620960f9a70e3dc14202a3a35dde1a316": TokenInfo(
        currency=CurrencyInfo(symbol="OAP", name="OpenAlexa Protocol"), scaling=Decimal("1e-18")
    ),
    "0x178bf8fd04b47d2de3ef3f6b3d112106375ad584": TokenInfo(
        currency=CurrencyInfo(symbol="UUSDT", name="Unagii Tether USD"), scaling=Decimal("1e-6")
    ),
    "0x178c820f862b14f316509ec36b13123da19a6054": TokenInfo(
        currency=CurrencyInfo(symbol="EWTB", name="Energy Web Token Bridged"), scaling=Decimal("1e-18")
    ),
    "0x1796ae0b0fa4862485106a0de9b654efe301d0b2": TokenInfo(
        currency=CurrencyInfo(symbol="PMON", name="Polychain Monsters"), scaling=Decimal("1e-18")
    ),
    "0x179e31fb25e433441a2839389a7b8ec9c4654b7b": TokenInfo(
        currency=CurrencyInfo(symbol="SNB", name="SynchroBitcoin"), scaling=Decimal("1e-18")
    ),
    "0x17a79792fe6fe5c95dfe95fe3fcee3caf4fe4cb7": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUSDT", name="Aave AMM USDT"), scaling=Decimal("1e-6")
    ),
    "0x17aa18a4b64a55abed7fa543f2ba4e91f2dce482": TokenInfo(
        currency=CurrencyInfo(symbol="INB", name="Insight Chain"), scaling=Decimal("1e-18")
    ),
    "0x17ac188e09a7890a1844e5e65471fe8b0ccfadf3": TokenInfo(
        currency=CurrencyInfo(symbol="CC10", name="Cryptocurrency Top 10 Index"), scaling=Decimal("1e-18")
    ),
    "0x17b0c6658944b11325e1fe2a723f0349eff6550a": TokenInfo(
        currency=CurrencyInfo(symbol="CPRT.CX", name="Copart Inc"), scaling=Decimal("1e-8")
    ),
    "0x17b26400621695c2d8c2d8869f6259e82d7544c4": TokenInfo(
        currency=CurrencyInfo(symbol="CCN", name="Custom contract network"), scaling=Decimal("1e-18")
    ),
    "0x17c8d8b7659141273a1c2223030c89b96713a44a": TokenInfo(
        currency=CurrencyInfo(symbol="XPS", name="Xpense"), scaling=Decimal("1e-18")
    ),
    "0x17d8cbb6bce8cee970a4027d1198f6700a7a6c24": TokenInfo(
        currency=CurrencyInfo(symbol="imBTC", name="mStable Interest Bearing mBTC"), scaling=Decimal("1e-18")
    ),
    "0x17e6616c45d267bc20a9892b58a01621c592b72d": TokenInfo(
        currency=CurrencyInfo(symbol="EMS", name="Ethereum Message Search"), scaling=Decimal("1e-18")
    ),
    "0x17e67d1cb4e349b9ca4bc3e17c7df2a397a7bb64": TokenInfo(
        currency=CurrencyInfo(symbol="FREC", name="Freyrchain"), scaling=Decimal("1e-18")
    ),
    "0x17ef75aa22dd5f6c2763b8304ab24f40ee54d48a": TokenInfo(
        currency=CurrencyInfo(symbol="RVP", name="Revolution Populi"), scaling=Decimal("1e-18")
    ),
    "0x17f8afb63dfcdcc90ebe6e84f060cc306a98257d": TokenInfo(
        currency=CurrencyInfo(symbol="NBAI", name="Nebula AI"), scaling=Decimal("1e-18")
    ),
    "0x17f93475d2a978f527c3f7c44abf44adfba60d5c": TokenInfo(
        currency=CurrencyInfo(symbol="ECO2", name="EtherCO2"), scaling=Decimal("1e-2")
    ),
    "0x17fd666fa0784885fa1afec8ac624d9b7e72b752": TokenInfo(
        currency=CurrencyInfo(symbol="FLIK", name="FLiK"), scaling=Decimal("1e-14")
    ),
    "0x180dae91d6d56235453a892d2e56a3e40ba81df8": TokenInfo(
        currency=CurrencyInfo(symbol="DOJO", name="DOJO"), scaling=Decimal("1e-18")
    ),
    "0x180e5087935a94fd5bbab00fd2249c5be0473381": TokenInfo(
        currency=CurrencyInfo(symbol="ZCG", name="ZCash Gold"), scaling=Decimal("1e-8")
    ),
    "0x181a63746d3adcf356cbc73ace22832ffbb1ee5a": TokenInfo(
        currency=CurrencyInfo(symbol="ALCO", name="Alaricoin"), scaling=Decimal("1e-8")
    ),
    "0x1822126feedb4c7d61eecdbe3682fe61e91383d6": TokenInfo(
        currency=CurrencyInfo(symbol="XTX", name="Xtock"), scaling=Decimal("1e-18")
    ),
    "0x1829aa045e21e0d59580024a951db48096e01782": TokenInfo(
        currency=CurrencyInfo(symbol="FXT", name="FuzeX"), scaling=Decimal("1e-18")
    ),
    "0x182a603541a4483c308475147d621bbb4e2587c6": TokenInfo(
        currency=CurrencyInfo(symbol="ZB", name="ZeroBank"), scaling=Decimal("1e-18")
    ),
    "0x1844b21593262668b7248d0f57a220caaba46ab9": TokenInfo(
        currency=CurrencyInfo(symbol="PRL", name="Oyster"), scaling=Decimal("1e-18")
    ),
    "0x1846bdfdb6a0f5c473dec610144513bd071999fb": TokenInfo(
        currency=CurrencyInfo(symbol="idleDAISafe", name="IdleDAI v3 [Risk Adjusted]"), scaling=Decimal("1e-18")
    ),
    "0x184c280e3450bd59b0df35ba7fce3aae3f353b83": TokenInfo(
        currency=CurrencyInfo(symbol="NSC", name="North Star Chain"), scaling=Decimal("1e-8")
    ),
    "0x1852e5f5a9a6933dc236fb226d4b197f5b1f279c": TokenInfo(
        currency=CurrencyInfo(symbol="SNE.CX", name="Sony Corporation"), scaling=Decimal("1e-8")
    ),
    "0x1864ce27e9f7517047933caae530674e8c70b8a7": TokenInfo(
        currency=CurrencyInfo(symbol="PIB", name="Pibble"), scaling=Decimal("1e-18")
    ),
    "0x186a33d4dbcd700086a26188dcb74e69be463665": TokenInfo(
        currency=CurrencyInfo(symbol="7E", name="7ELEVEN"), scaling=Decimal("1e-8")
    ),
    "0x186af393bf9ceef31ce7eae2b468c46231163cc7": TokenInfo(
        currency=CurrencyInfo(symbol="YLFi", name="Yearn Loans Finance"), scaling=Decimal("1e-18")
    ),
    "0x188e817b02e635d482ae4d81e25dda98a97c4a42": TokenInfo(
        currency=CurrencyInfo(symbol="LITH", name="Lithium Finance"), scaling=Decimal("1e-18")
    ),
    "0x18a4979bbb4c88275d4575d66b9c9cd6bea0cd5e": TokenInfo(
        currency=CurrencyInfo(symbol="IDXT", name="IdexTools"), scaling=Decimal("1e-18")
    ),
    "0x18aa7c90d3ae4c5bb219d0a2813f441704084625": TokenInfo(
        currency=CurrencyInfo(symbol="DCA", name="Decentralize Currency"), scaling=Decimal("1e-18")
    ),
    "0x18aaa7115705e8be94bffebde57af9bfc265b998": TokenInfo(
        currency=CurrencyInfo(symbol="AUDIO", name="Audius"), scaling=Decimal("1e-18")
    ),
    "0x18c525cce3ad9a48d82f91b874754be78e9d0f85": TokenInfo(
        currency=CurrencyInfo(symbol="DOOH", name="Bidooh"), scaling=Decimal("1e-18")
    ),
    "0x18f5b4908e8861e3114ba9a0a9a4e84c5f180cc0": TokenInfo(
        currency=CurrencyInfo(symbol="EST", name="ESports Token"), scaling=Decimal("1e-9")
    ),
    "0x18f865d0fc2c82e787cc2bebc5f7652a3f600df7": TokenInfo(
        currency=CurrencyInfo(symbol="SHARK", name="SharkTrade"), scaling=Decimal("1e-18")
    ),
    "0x19037b591ce06e7cd1b990146697466a23b165bf": TokenInfo(
        currency=CurrencyInfo(symbol="PYC", name="PrivacyChain"), scaling=Decimal("1e-18")
    ),
    "0x19055b944806fba2717dc694cf0173a1eb2d1604": TokenInfo(
        currency=CurrencyInfo(symbol="C3W", name="C3 Wallet"), scaling=Decimal("1e-8")
    ),
    "0x19062190b1925b5b6689d7073fdfc8c2976ef8cb": TokenInfo(
        currency=CurrencyInfo(symbol="BZZ", name="Swarm"), scaling=Decimal("1e-16")
    ),
    "0x190e569be071f40c704e15825f285481cb74b6cc": TokenInfo(
        currency=CurrencyInfo(symbol="FAM", name="Fame"), scaling=Decimal("1e-12")
    ),
    "0x190fb342aa6a15eb82903323ae78066ff8616746": TokenInfo(
        currency=CurrencyInfo(symbol="UMC", name="Umbrella Coin"), scaling=Decimal("1e-6")
    ),
    "0x19131a8ae42e32c747c1ead318fadb98b0be45b7": TokenInfo(
        currency=CurrencyInfo(symbol="QTC", name="Quality Tracing Chain"), scaling=Decimal("1e-18")
    ),
    "0x191557728e4d8caa4ac94f86af842148c0fa8f7e": TokenInfo(
        currency=CurrencyInfo(symbol="ECO", name="Ormeus Ecosystem"), scaling=Decimal("1e-8")
    ),
    "0x193408ca0576b73156ed42a2ea7d6fd3f6507162": TokenInfo(
        currency=CurrencyInfo(symbol="INFS", name="Infinity Esaham"), scaling=Decimal("1e-1")
    ),
    "0x1955d744f9435522be508d1ba60e3c12d0690b6a": TokenInfo(
        currency=CurrencyInfo(symbol="WPP", name="WPP Token"), scaling=Decimal("1e-18")
    ),
    "0x1961b3331969ed52770751fc718ef530838b6dee": TokenInfo(
        currency=CurrencyInfo(symbol="BDG", name="BitDegree"), scaling=Decimal("1e-18")
    ),
    "0x1966d718a565566e8e202792658d7b5ff4ece469": TokenInfo(
        currency=CurrencyInfo(symbol="NDX", name="nDEX"), scaling=Decimal("1e-18")
    ),
    "0x1969442391737025812c2215e77e676d7fa84847": TokenInfo(
        currency=CurrencyInfo(symbol="ISL", name="Islamic Bank"), scaling=Decimal("1e-18")
    ),
    "0x196c81385bc536467433014042788eb707703934": TokenInfo(
        currency=CurrencyInfo(symbol="CTASK", name="CryptoTask"), scaling=Decimal("1e-18")
    ),
    "0x196f4727526ea7fb1e17b2071b3d8eaa38486988": TokenInfo(
        currency=CurrencyInfo(symbol="RSV", name="Reserve"), scaling=Decimal("1e-18")
    ),
    "0x1977c795b5f52bf6f8150136b07822d1f00704f3": TokenInfo(
        currency=CurrencyInfo(symbol="MST", name="Mysterious Sound"), scaling=Decimal("1e-18")
    ),
    "0x19810559df63f19cfe88923313250550edadb743": TokenInfo(
        currency=CurrencyInfo(symbol="HOUSE", name="Toast.finance"), scaling=Decimal("1e-0")
    ),
    "0x1985365e9f78359a9b6ad760e32412f4a445e862": TokenInfo(
        currency=CurrencyInfo(symbol="REP", name="Reputation"), scaling=Decimal("1e-18")
    ),
    "0x198a87b3114143913d4229fb0f6d4bcb44aa8aff": TokenInfo(
        currency=CurrencyInfo(symbol="SNBL", name="Snowball_old"), scaling=Decimal("1e-8")
    ),
    "0x199911cba391c79bd10d7ae9892b090eb6510b98": TokenInfo(
        currency=CurrencyInfo(symbol="ALNY.CX", name="Alnylam Pharmaceuticals Inc"), scaling=Decimal("1e-8")
    ),
    "0x199c3ddedb0e91db3897039af27c23286269f088": TokenInfo(
        currency=CurrencyInfo(symbol="DCX", name="DecenTradex"), scaling=Decimal("1e-8")
    ),
    "0x19c9872640ec38c2cf36c0f04d1365ef067869b3": TokenInfo(
        currency=CurrencyInfo(symbol="OATH", name="Oath Protocol"), scaling=Decimal("1e-18")
    ),
    "0x19ca83a13b4c4be43fa82c5e415e16f1d86f57f7": TokenInfo(
        currency=CurrencyInfo(symbol="BCEO", name="bitCEO"), scaling=Decimal("1e-18")
    ),
    "0x19ddc3605052554a1ac2b174ae745c911456841f": TokenInfo(
        currency=CurrencyInfo(symbol="PON", name="Proof of Nature Token"), scaling=Decimal("1e-18")
    ),
    "0x19e98c4921aab7e3f5fd2adca36cfb669c63e926": TokenInfo(
        currency=CurrencyInfo(symbol="COLA", name="Cola Token"), scaling=Decimal("1e-18")
    ),
    "0x19ea630bcbc1a511a16e65b6ecd447c92e1c087c": TokenInfo(
        currency=CurrencyInfo(symbol="CARAT", name="CARAT"), scaling=Decimal("1e-18")
    ),
    "0x19edfbe9814af6eee88289fdd789bc473e84f8f7": TokenInfo(
        currency=CurrencyInfo(symbol="METH", name="MINI ETHEREUM"), scaling=Decimal("1e-18")
    ),
    "0x19f3e6521f73a0184cc171c8ccbe1e21f93f4b3b": TokenInfo(
        currency=CurrencyInfo(symbol="NFX", name="Nimfex Token"), scaling=Decimal("1e-18")
    ),
    "0x19f4a2f8e21915376f1429c26a3a9b9b1db5ff5a": TokenInfo(
        currency=CurrencyInfo(symbol="CHADLINK", name="Chad Link Set"), scaling=Decimal("1e-18")
    ),
    "0x19fd4c760a7d4a38aee9f226035cbc9fdf434ffe": TokenInfo(
        currency=CurrencyInfo(symbol="CVP", name="CVP Token"), scaling=Decimal("1e-18")
    ),
    "0x19fffd124cd9089e21026d10da97f8cd6b442bff": TokenInfo(
        currency=CurrencyInfo(symbol="ZFL", name="Zuflo Coin"), scaling=Decimal("1e-8")
    ),
    "0x1a04cfe90fb72ed884977dbb8f77b59d95fedbb3": TokenInfo(
        currency=CurrencyInfo(symbol="MSV", name="MSV Chain"), scaling=Decimal("1e-18")
    ),
    "0x1a0c31837edb132a9312841b9527e6307db13509": TokenInfo(
        currency=CurrencyInfo(symbol="HPC", name="Hash Power Capital"), scaling=Decimal("1e-18")
    ),
    "0x1a0f2ab46ec630f9fd638029027b552afa64b94c": TokenInfo(
        currency=CurrencyInfo(symbol="ATX", name="Aston"), scaling=Decimal("1e-18")
    ),
    "0x1a2277c83930b7a64c3e3d5544eaa8c4f946b1b7": TokenInfo(
        currency=CurrencyInfo(symbol="ECHT", name="e-Chat"), scaling=Decimal("1e-18")
    ),
    "0x1a231e75538a931c395785ef5d1a5581ec622b0e": TokenInfo(
        currency=CurrencyInfo(symbol="ZOM", name="Zoom Protocol"), scaling=Decimal("1e-18")
    ),
    "0x1a23a6bfbadb59fa563008c0fb7cf96dfcf34ea1": TokenInfo(
        currency=CurrencyInfo(symbol="COFI", name="CoFiX"), scaling=Decimal("1e-18")
    ),
    "0x1a2933fba0c6e959c9a2d2c933f3f8ad4aa9f06e": TokenInfo(
        currency=CurrencyInfo(symbol="PARMA", name="PARMA"), scaling=Decimal("1e-18")
    ),
    "0x1a3496c18d558bd9c6c8f609e1b129f67ab08163": TokenInfo(
        currency=CurrencyInfo(symbol="DEP", name="DEAPCOIN"), scaling=Decimal("1e-18")
    ),
    "0x1a3564852d8ede7c8249805e71718bd7aa93dd6d": TokenInfo(
        currency=CurrencyInfo(symbol="XPO", name="X-power Chain"), scaling=Decimal("1e-2")
    ),
    "0x1a4743cf1af4c289351390a2b3fe7c13d2f7c235": TokenInfo(
        currency=CurrencyInfo(symbol="CTT", name="Castweet"), scaling=Decimal("1e-18")
    ),
    "0x1a4b46696b2bb4794eb3d4c26f1c55f9170fa4c5": TokenInfo(
        currency=CurrencyInfo(symbol="BIT", name="BitDAO"), scaling=Decimal("1e-18")
    ),
    "0x1a5f9352af8af974bfc03399e3767df6370d82e4": TokenInfo(
        currency=CurrencyInfo(symbol="OWL", name="OWL"), scaling=Decimal("1e-18")
    ),
    "0x1a66e09f7dccc10eae46e27cfa6b8d44a50df1e7": TokenInfo(
        currency=CurrencyInfo(symbol="PSM", name="PRASM"), scaling=Decimal("1e-18")
    ),
    "0x1a7a8bd9106f2b8d977e08582dc7d24c723ab0db": TokenInfo(
        currency=CurrencyInfo(symbol="APPC", name="AppCoins"), scaling=Decimal("1e-18")
    ),
    "0x1a7e4e63778b4f12a199c062f3efdd288afcbce8": TokenInfo(
        currency=CurrencyInfo(symbol="AGEUR", name="agEUR"), scaling=Decimal("1e-18")
    ),
    "0x1a95b271b0535d15fa49932daba31ba612b52946": TokenInfo(
        currency=CurrencyInfo(symbol="MNE", name="minereum"), scaling=Decimal("1e-8")
    ),
    "0x1a986f1659e11e2ae7cc6543f307bae5cde1c761": TokenInfo(
        currency=CurrencyInfo(symbol="UNY", name="Unity Ingot"), scaling=Decimal("1e-2")
    ),
    "0x1aa0dd2faada457d467a1c426b63c6bf8c176663": TokenInfo(
        currency=CurrencyInfo(symbol="TST", name="TuneStarTV"), scaling=Decimal("1e-18")
    ),
    "0x1aa61c196e76805fcbe394ea00e4ffced24fc469": TokenInfo(
        currency=CurrencyInfo(symbol="SAFE", name="yieldfarming.insure"), scaling=Decimal("1e-18")
    ),
    "0x1abc429a9e0a6bb21cac418e876f2ba608556836": TokenInfo(
        currency=CurrencyInfo(symbol="EPWR", name="Ethereum Power"), scaling=Decimal("1e-18")
    ),
    "0x1ad606adde97c0c28bd6ac85554176bc55783c01": TokenInfo(
        currency=CurrencyInfo(symbol="MOONDAY", name="Moonday Finance"), scaling=Decimal("1e-18")
    ),
    "0x1aee70cf78587ddc593dedb311bc87851b16b914": TokenInfo(
        currency=CurrencyInfo(symbol="NOW.CX", name="ServiceNow"), scaling=Decimal("1e-8")
    ),
    "0x1af20b8d1ede928f437b3a86801796b167840d2b": TokenInfo(
        currency=CurrencyInfo(symbol="HKDX", name="eToro Hong Kong Dollar"), scaling=Decimal("1e-18")
    ),
    "0x1af97824a7ccd3963b9385e37ecbf44ece0c73e4": TokenInfo(
        currency=CurrencyInfo(symbol="ADDC", name="Aladdin"), scaling=Decimal("1e-18")
    ),
    "0x1afe191601c0c7095c995bd6875f94a89fa5d71b": TokenInfo(
        currency=CurrencyInfo(symbol="SNAP", name="THANOS"), scaling=Decimal("1e-18")
    ),
    "0x1b073382e63411e3bcffe90ac1b9a43fefa1ec6f": TokenInfo(
        currency=CurrencyInfo(symbol="BEST", name="Bitpanda Ecosystem Token"), scaling=Decimal("1e-8")
    ),
    "0x1b22c32cd936cb97c28c5690a0695a82abf688e6": TokenInfo(
        currency=CurrencyInfo(symbol="WISH", name="MyWish Token"), scaling=Decimal("1e-18")
    ),
    "0x1b40183efb4dd766f11bda7a7c3ad8982e998421": TokenInfo(
        currency=CurrencyInfo(symbol="VSP", name="Vesper Finance"), scaling=Decimal("1e-18")
    ),
    "0x1b4052d98fb1888c2bf3b8d3b930e0aff8a910df": TokenInfo(
        currency=CurrencyInfo(symbol="COM", name="Community Token"), scaling=Decimal("1e-18")
    ),
    "0x1b5f21ee98eed48d292e8e2d3ed82b40a9728a22": TokenInfo(
        currency=CurrencyInfo(symbol="DATA", name="DataBroker DAO Token"), scaling=Decimal("1e-18")
    ),
    "0x1b6c5864375b34af3ff5bd2e5f40bc425b4a8d79": TokenInfo(
        currency=CurrencyInfo(symbol="TOPC", name="TopChain"), scaling=Decimal("1e-6")
    ),
    "0x1b76d0364e803fb94c1d5ca9faf55f05ee494731": TokenInfo(
        currency=CurrencyInfo(symbol="UCN", name="Uniswap Community Network"), scaling=Decimal("1e-18")
    ),
    "0x1b793e49237758dbd8b752afc9eb4b329d5da016": TokenInfo(
        currency=CurrencyInfo(symbol="VITE", name="ViteToken"), scaling=Decimal("1e-18")
    ),
    "0x1b7c4d4f226ccf3211b0f99c4fdfb84a2606bf8e": TokenInfo(
        currency=CurrencyInfo(symbol="ORB", name="Orb V2"), scaling=Decimal("1e-18")
    ),
    "0x1b80eeeadcc590f305945bcc258cfa770bbe1890": TokenInfo(
        currency=CurrencyInfo(symbol="BQQQ", name="Bitsdaq Token"), scaling=Decimal("1e-18")
    ),
    "0x1b879d3812f2ade1214264655b473910e0caf1e6": TokenInfo(
        currency=CurrencyInfo(symbol="VERSI", name="VersiCoin"), scaling=Decimal("1e-18")
    ),
    "0x1b890fd37cd50bea59346fc2f8ddb7cd9f5fabd5": TokenInfo(
        currency=CurrencyInfo(symbol="NEWO", name="New Order"), scaling=Decimal("1e-18")
    ),
    "0x1b957dc4aefeed3b4a2351a6a6d5cbfbba0cecfa": TokenInfo(
        currency=CurrencyInfo(symbol="HQX", name="HOQU"), scaling=Decimal("1e-18")
    ),
    "0x1b9743f556d65e757c4c650b4555baf354cb8bd3": TokenInfo(
        currency=CurrencyInfo(symbol="ETBS", name="Ethbits"), scaling=Decimal("1e-12")
    ),
    "0x1b980e05943de3db3a459c72325338d327b6f5a9": TokenInfo(
        currency=CurrencyInfo(symbol="GEAR", name="Bitgear"), scaling=Decimal("1e-18")
    ),
    "0x1b991b6a41bf3bbc5cbd3b60000f26a8ea9ff9e9": TokenInfo(
        currency=CurrencyInfo(symbol="VNM", name="Venom Shards"), scaling=Decimal("1e-18")
    ),
    "0x1bbe271d15bb64df0bc6cd28df9ff322f2ebd847": TokenInfo(
        currency=CurrencyInfo(symbol="TBTC", name="tBTC"), scaling=Decimal("1e-18")
    ),
    "0x1bc7c1de0ac6ef4fdec35c053030d90cf54c7e9a": TokenInfo(
        currency=CurrencyInfo(symbol="YNN", name="YANG"), scaling=Decimal("1e-18")
    ),
    "0x1bc9f31c327ce04b6fa9d56fd84c14cc0b0a4f47": TokenInfo(
        currency=CurrencyInfo(symbol="HG", name="Hygenercoin"), scaling=Decimal("1e-18")
    ),
    "0x1bcbc54166f6ba149934870b60506199b6c9db6d": TokenInfo(
        currency=CurrencyInfo(symbol="ROC", name="Rasputin Online Coin"), scaling=Decimal("1e-10")
    ),
    "0x1bcca39ae82e53dede8ec5500c3bcd76cd1e0072": TokenInfo(
        currency=CurrencyInfo(symbol="ETHBTCPA", name="ETH/BTC Price Action Candlestick Set"), scaling=Decimal("1e-18")
    ),
    "0x1be7cfd61aa8daaa9ff2f3b8820888f09462d037": TokenInfo(
        currency=CurrencyInfo(symbol="GGC", name="GramGold Coin"), scaling=Decimal("1e-8")
    ),
    "0x1beef31946fbbb40b877a72e4ae04a8d1a5cee06": TokenInfo(
        currency=CurrencyInfo(symbol="PAR", name="Parachute"), scaling=Decimal("1e-18")
    ),
    "0x1bf7fd22709733ccd7c45ab27dd02c7ec8e50078": TokenInfo(
        currency=CurrencyInfo(symbol="QTCON", name="Quiztok"), scaling=Decimal("1e-18")
    ),
    "0x1c153badb7e54abcdcb65f0a09fcd6f10de36aa3": TokenInfo(
        currency=CurrencyInfo(symbol="TMC", name="TMC"), scaling=Decimal("1e-18")
    ),
    "0x1c1c14a6b5074905ce5d367b0a7e098b58ebfd47": TokenInfo(
        currency=CurrencyInfo(symbol="FEX", name="FIDEX Exchange"), scaling=Decimal("1e-8")
    ),
    "0x1c3bb10de15c31d5dbe48fbb7b87735d1b7d8c32": TokenInfo(
        currency=CurrencyInfo(symbol="BLO", name="BLONDCOIN"), scaling=Decimal("1e-18")
    ),
    "0x1c4481750daa5ff521a2a7490d9981ed46465dbd": TokenInfo(
        currency=CurrencyInfo(symbol="BCPT", name="Blockmason Credit Protocol"), scaling=Decimal("1e-18")
    ),
    "0x1c48f86ae57291f7686349f12601910bd8d470bb": TokenInfo(
        currency=CurrencyInfo(symbol="USDK", name="USDK"), scaling=Decimal("1e-18")
    ),
    "0x1c4b7d0e1885bd7667af3378e0c538f74e712006": TokenInfo(
        currency=CurrencyInfo(symbol="IOG", name="Playgroundz"), scaling=Decimal("1e-18")
    ),
    "0x1c5857e110cd8411054660f60b5de6a6958cfae2": TokenInfo(
        currency=CurrencyInfo(symbol="RSV", name="Reserve"), scaling=Decimal("1e-18")
    ),
    "0x1c5b760f133220855340003b43cc9113ec494823": TokenInfo(
        currency=CurrencyInfo(symbol="OROX", name="Cointorox"), scaling=Decimal("1e-18")
    ),
    "0x1c5db575e2ff833e46a2e9864c22f4b22e0b37c2": TokenInfo(
        currency=CurrencyInfo(symbol="RENZEC", name="renZEC"), scaling=Decimal("1e-8")
    ),
    "0x1c5f43710a1776b0ea7191b7ead75d4b98d69858": TokenInfo(
        currency=CurrencyInfo(symbol="PSK", name="Pool of Stake"), scaling=Decimal("1e-18")
    ),
    "0x1c62aca2b7605db3606eacda7bc67a1857ddb8ff": TokenInfo(
        currency=CurrencyInfo(symbol="SONIQ", name="Soniq"), scaling=Decimal("1e-18")
    ),
    "0x1c65c261cb89178b02cf2aee20058b992787d770": TokenInfo(
        currency=CurrencyInfo(symbol="TORQ", name="TORQ Coin"), scaling=Decimal("1e-18")
    ),
    "0x1c79ab32c66acaa1e9e81952b8aaa581b43e54e7": TokenInfo(
        currency=CurrencyInfo(symbol="TEAM", name="TEAM"), scaling=Decimal("1e-4")
    ),
    "0x1c7bbadc81e18f7177a95eb1593e5f5f35861b10": TokenInfo(
        currency=CurrencyInfo(symbol="AUSCM", name="Auric Network"), scaling=Decimal("1e-18")
    ),
    "0x1c83501478f1320977047008496dacbd60bb15ef": TokenInfo(
        currency=CurrencyInfo(symbol="DGTX", name="DigitexFutures"), scaling=Decimal("1e-18")
    ),
    "0x1c9491865a1de77c5b6e19d2e6a5f1d7a6f2b25f": TokenInfo(
        currency=CurrencyInfo(symbol="MATTER", name="AntiMatter"), scaling=Decimal("1e-18")
    ),
    "0x1c95b093d6c236d3ef7c796fe33f9cc6b8606714": TokenInfo(
        currency=CurrencyInfo(symbol="BOMB", name="BOMB"), scaling=Decimal("1e-0")
    ),
    "0x1c9922314ed1415c95b9fd453c3818fd41867d0b": TokenInfo(
        currency=CurrencyInfo(symbol="TOWER", name="Tower"), scaling=Decimal("1e-18")
    ),
    "0x1c9db47ee8abad20d28f9bbe2363ca0c8c9ab9b8": TokenInfo(
        currency=CurrencyInfo(symbol="BINS", name="Bitsense"), scaling=Decimal("1e-8")
    ),
    "0x1c9e21a437b9e98a6bb66c0ff862864523513135": TokenInfo(
        currency=CurrencyInfo(symbol="BANG", name="The Big Bang"), scaling=Decimal("1e-18")
    ),
    "0x1ca43a170bad619322e6f54d46b57e504db663aa": TokenInfo(
        currency=CurrencyInfo(symbol="AKC", name="ARTWOOK Coin"), scaling=Decimal("1e-18")
    ),
    "0x1cb3209d45b2a60b7fbca1ccdbf87f674237a4aa": TokenInfo(
        currency=CurrencyInfo(symbol="THR", name="ThoreCoin"), scaling=Decimal("1e-4")
    ),
    "0x1cbb83ebcd552d5ebf8131ef8c9cd9d9bab342bc": TokenInfo(
        currency=CurrencyInfo(symbol="NFY", name="Non-Fungible Yearn"), scaling=Decimal("1e-18")
    ),
    "0x1ccaa0f2a7210d76e1fdec740d5f323e2e1b1672": TokenInfo(
        currency=CurrencyInfo(symbol="FACE", name="Faceter"), scaling=Decimal("1e-18")
    ),
    "0x1ceb5cb57c4d4e2b2433641b95dd330a33185a44": TokenInfo(
        currency=CurrencyInfo(symbol="KP3R", name="Keep3rV1"), scaling=Decimal("1e-18")
    ),
    "0x1cf402135d7bd27dc9d21c03ae2d8375bc43e9ec": TokenInfo(
        currency=CurrencyInfo(symbol="ZDC", name="Zodiac"), scaling=Decimal("1e-18")
    ),
    "0x1cf4592ebffd730c7dc92c1bdffdfc3b9efcf29a": TokenInfo(
        currency=CurrencyInfo(symbol="WAVES", name="Waves"), scaling=Decimal("1e-18")
    ),
    "0x1d086b868d78040635cb8600ba733f12db48cb42": TokenInfo(
        currency=CurrencyInfo(symbol="XLX", name="XLXPay"), scaling=Decimal("1e-18")
    ),
    "0x1d09144f3479bb805cb7c92346987420bcbdc10c": TokenInfo(
        currency=CurrencyInfo(symbol="cyUSD", name="CreamY USD"), scaling=Decimal("1e-18")
    ),
    "0x1d2662efae81adf192a9f8cd5286bed3d3987bbf": TokenInfo(
        currency=CurrencyInfo(symbol="HOST", name="Hosting Token"), scaling=Decimal("1e-8")
    ),
    "0x1d287cc25dad7ccaf76a26bc660c5f7c8e2a05bd": TokenInfo(
        currency=CurrencyInfo(symbol="FET", name="Fetch"), scaling=Decimal("1e-18")
    ),
    "0x1d350417d9787e000cc1b95d70e9536dcd91f373": TokenInfo(
        currency=CurrencyInfo(symbol="MIAU", name="Mirrored iShares Gold Trust"), scaling=Decimal("1e-18")
    ),
    "0x1d35c42e9dcb5c5343fbd70fe73b2284d042d082": TokenInfo(
        currency=CurrencyInfo(symbol="HUG", name="Hugcoin"), scaling=Decimal("1e-18")
    ),
    "0x1d37986f252d0e349522ea6c3b98cb935495e63e": TokenInfo(
        currency=CurrencyInfo(symbol="CHART", name="ChartEx"), scaling=Decimal("1e-18")
    ),
    "0x1d462414fe14cf489c7a21cac78509f4bf8cd7c0": TokenInfo(
        currency=CurrencyInfo(symbol="CAN", name="CanYaCoin"), scaling=Decimal("1e-6")
    ),
    "0x1d464ac5e046e5fe280c9588edf8eb681b07008f": TokenInfo(
        currency=CurrencyInfo(symbol="GMB", name="GMB"), scaling=Decimal("1e-18")
    ),
    "0x1d4abd5e28ef311ea114fd4756fbcf9b7d568e1f": TokenInfo(
        currency=CurrencyInfo(symbol="EDS", name="Electronic Data Systems"), scaling=Decimal("1e-6")
    ),
    "0x1d4ccc31dab6ea20f461d329a0562c1c58412515": TokenInfo(
        currency=CurrencyInfo(symbol="TALAO", name="TALAO"), scaling=Decimal("1e-18")
    ),
    "0x1d9a3cef66b01d44003b9db0e00ec3fd44746988": TokenInfo(
        currency=CurrencyInfo(symbol="WSS", name="ETHWSS Coin"), scaling=Decimal("1e-18")
    ),
    "0x1d9cd2180fd4e9771fca28681034d02390b14e4c": TokenInfo(
        currency=CurrencyInfo(symbol="HEDGESHIT", name="1X Short Shitcoin Index Token"), scaling=Decimal("1e-18")
    ),
    "0x1da01e84f3d4e6716f274c987ae4bee5dc3c8288": TokenInfo(
        currency=CurrencyInfo(symbol="BID", name="DeFi Bids"), scaling=Decimal("1e-18")
    ),
    "0x1da4858ad385cc377165a298cc2ce3fce0c5fd31": TokenInfo(
        currency=CurrencyInfo(symbol="CCS", name="CLOUTCONTRACTS"), scaling=Decimal("1e-0")
    ),
    "0x1da87b114f35e1dc91f72bf57fc07a768ad40bb0": TokenInfo(
        currency=CurrencyInfo(symbol="EQZ", name="Equalizer"), scaling=Decimal("1e-18")
    ),
    "0x1dabf6ab0eb8e4208e7e9302cec7a014068952e4": TokenInfo(
        currency=CurrencyInfo(symbol="CURA", name="Curate"), scaling=Decimal("1e-8")
    ),
    "0x1dcdeba9522072f8ac5b7f2e8ccacb40b864d739": TokenInfo(
        currency=CurrencyInfo(symbol="GD.CX", name="General Dynamics"), scaling=Decimal("1e-8")
    ),
    "0x1dd0df760eb950083c1925da19fc7ac1356a190b": TokenInfo(
        currency=CurrencyInfo(symbol="AMA", name="AmaCoin"), scaling=Decimal("1e-18")
    ),
    "0x1dd7b2878b6d5671ed602e60818b0d9a0cd1cdf7": TokenInfo(
        currency=CurrencyInfo(symbol="FIN", name="Fuel Injection Network"), scaling=Decimal("1e-18")
    ),
    "0x1dd80016e3d4ae146ee2ebb484e8edd92dacc4ce": TokenInfo(
        currency=CurrencyInfo(symbol="LEAD", name="Lead Token"), scaling=Decimal("1e-18")
    ),
    "0x1de09690e0d3c75c22cd19acc1aebde46bbc7d25": TokenInfo(
        currency=CurrencyInfo(symbol="TMB", name="TemboCoin"), scaling=Decimal("1e-0")
    ),
    "0x1de5e000c41c8d35b9f1f4985c23988f05831057": TokenInfo(
        currency=CurrencyInfo(symbol="BNF", name="BonFi"), scaling=Decimal("1e-18")
    ),
    "0x1dea979ae76f26071870f824088da78979eb91c8": TokenInfo(
        currency=CurrencyInfo(symbol="SPD", name="SPINDLE"), scaling=Decimal("1e-18")
    ),
    "0x1df6f1bb7454e5e4ba3bca882d3148fbf9b5697a": TokenInfo(
        currency=CurrencyInfo(symbol="YFSI", name="Yfscience"), scaling=Decimal("1e-18")
    ),
    "0x1dfec1cf1336c572c2d2e34fe8f6aa2f409c8251": TokenInfo(
        currency=CurrencyInfo(symbol="MTBK", name="Metalblock"), scaling=Decimal("1e-18")
    ),
    "0x1e15abf152067e9fe4a48bbf094a71f5bb16325d": TokenInfo(
        currency=CurrencyInfo(symbol="SFI", name="socket.finance"), scaling=Decimal("1e-18")
    ),
    "0x1e18821e69b9faa8e6e75dffe54e7e25754beda0": TokenInfo(
        currency=CurrencyInfo(symbol="KIMCHI", name="KIMCHI.finance"), scaling=Decimal("1e-18")
    ),
    "0x1e26b3d07e57f453cae30f7ddd2f945f5bf3ef33": TokenInfo(
        currency=CurrencyInfo(symbol="XCLR", name="ClearCoin"), scaling=Decimal("1e-8")
    ),
    "0x1e29ca8c874b4dff828297cc2e9856819eea0933": TokenInfo(
        currency=CurrencyInfo(symbol="TOU", name="TOURISTOKEN"), scaling=Decimal("1e-18")
    ),
    "0x1e3a2446c729d34373b87fd2c9cbb39a93198658": TokenInfo(
        currency=CurrencyInfo(symbol="DSD", name="DeFi Nation Signals DAO"), scaling=Decimal("1e-18")
    ),
    "0x1e3fe98d1c89865b6b819bbfd532dadab3b34d2d": TokenInfo(
        currency=CurrencyInfo(symbol="DET", name="Digital Economic Token"), scaling=Decimal("1e-18")
    ),
    "0x1e41a55030e0d0794abfb6dced22e6c7d18d8247": TokenInfo(
        currency=CurrencyInfo(symbol="ADC", name="Android chain"), scaling=Decimal("1e-18")
    ),
    "0x1e49ff77c355a3e38d6651ce8404af0e48c5395f": TokenInfo(
        currency=CurrencyInfo(symbol="MTRC", name="ModulTrade"), scaling=Decimal("1e-18")
    ),
    "0x1e4e36b3f011d862fd70006804da8fcefe89d3d8": TokenInfo(
        currency=CurrencyInfo(symbol="VNST", name="Venus Token"), scaling=Decimal("1e-18")
    ),
    "0x1e6063b7b3a1c1952ed2c4087fd528998db69ec7": TokenInfo(
        currency=CurrencyInfo(symbol="FXC", name="FUTUREXCRYPTO"), scaling=Decimal("1e-18")
    ),
    "0x1e71034c89dd191accb27dc35f18a3d8b6f91311": TokenInfo(
        currency=CurrencyInfo(symbol="FTB", name="Free Tool Box"), scaling=Decimal("1e-18")
    ),
    "0x1e797ce986c3cff4472f7d38d5c4aba55dfefe40": TokenInfo(
        currency=CurrencyInfo(symbol="BCDN", name="BlockCDN"), scaling=Decimal("1e-15")
    ),
    "0x1e8c423b2e8aae409280c696c5acda62f7e6f23c": TokenInfo(
        currency=CurrencyInfo(symbol="QTB", name="Quant Treasure Backup Chain"), scaling=Decimal("1e-18")
    ),
    "0x1e9421331f19e6c4ba79bce22582e3f34c4cf506": TokenInfo(
        currency=CurrencyInfo(symbol="AMU", name="Amazing Unit"), scaling=Decimal("1e-18")
    ),
    "0x1e999ee452eafbcfd6b8f038bb6cabbb533dc1b9": TokenInfo(
        currency=CurrencyInfo(symbol="HUBBS", name="Myhubb"), scaling=Decimal("1e-8")
    ),
    "0x1ebd8d3ca115451b9b6bbaa7ee2f7b0f96e49fd8": TokenInfo(
        currency=CurrencyInfo(symbol="NGOT", name="ngot"), scaling=Decimal("1e-5")
    ),
    "0x1ec52a7a6048c1ca8b8afd8ef97051acfe755e35": TokenInfo(
        currency=CurrencyInfo(symbol="GCPH", name="GoldenHand"), scaling=Decimal("1e-18")
    ),
    "0x1ec8fe51a9b6a3a6c427d17d9ecc3060fbc4a45c": TokenInfo(
        currency=CurrencyInfo(symbol="S-A-PAT", name="smartillions.io A ETH"), scaling=Decimal("1e-18")
    ),
    "0x1ed7ae1f0e2fa4276dd7ddc786334a3df81d50c0": TokenInfo(
        currency=CurrencyInfo(symbol="FSBT", name="FSBT API"), scaling=Decimal("1e-18")
    ),
    "0x1edc9ba729ef6fb017ef9c687b1a37d48b6a166c": TokenInfo(
        currency=CurrencyInfo(symbol="STARK", name="Stark Chain"), scaling=Decimal("1e-18")
    ),
    "0x1eddee3fa21591a9637f88dab9615c33ee636b9d": TokenInfo(
        currency=CurrencyInfo(symbol="WON", name="WeBlock"), scaling=Decimal("1e-18")
    ),
    "0x1efb2286bf89f01488c6b2a22b2556c0f45e972b": TokenInfo(
        currency=CurrencyInfo(symbol="MYFI", name="Moon YFI"), scaling=Decimal("1e-18")
    ),
    "0x1efc4dfd580df95426a0f04848870bd8cb5a338e": TokenInfo(
        currency=CurrencyInfo(symbol="ACAD", name="Academy Token"), scaling=Decimal("1e-18")
    ),
    "0x1f0f468ee03a6d99cd8a09dd071494a83dc1c0e5": TokenInfo(
        currency=CurrencyInfo(symbol="SAT", name="SmartX"), scaling=Decimal("1e-4")
    ),
    "0x1f21d8395655fb262251897df7cb3c9358bec6a2": TokenInfo(
        currency=CurrencyInfo(symbol="IRC", name="IronCoin"), scaling=Decimal("1e-8")
    ),
    "0x1f2910b0d423bbc4271af083b17fb2837f215c36": TokenInfo(
        currency=CurrencyInfo(symbol="CR", name="EOS Chrome"), scaling=Decimal("1e-18")
    ),
    "0x1f35a281036be57e64e7e7a2a556b4f888a1b829": TokenInfo(
        currency=CurrencyInfo(symbol="MZK", name="Muzika Network"), scaling=Decimal("1e-18")
    ),
    "0x1f3f677ecc58f6a1f9e2cf410df4776a8546b5de": TokenInfo(
        currency=CurrencyInfo(symbol="VNDC", name="VNDC"), scaling=Decimal("1e-0")
    ),
    "0x1f3f9d3068568f8040775be2e8c03c103c61f3af": TokenInfo(
        currency=CurrencyInfo(symbol="ARCH", name="Archer DAO Governance Token"), scaling=Decimal("1e-18")
    ),
    "0x1f41e42d0a9e3c0dd3ba15b527342783b43200a9": TokenInfo(
        currency=CurrencyInfo(symbol="BCAP", name="BCAP"), scaling=Decimal("1e-0")
    ),
    "0x1f4cb968b76931c494ff92ed80ccb169ad641cb1": TokenInfo(
        currency=CurrencyInfo(symbol="STF", name="Structure Finance"), scaling=Decimal("1e-18")
    ),
    "0x1f54638b7737193ffd86c19ec51907a7c41755d8": TokenInfo(
        currency=CurrencyInfo(symbol="SOL", name="Sola Token"), scaling=Decimal("1e-6")
    ),
    "0x1f573d6fb3f13d689ff844b4ce37794d79a7ff1c": TokenInfo(
        currency=CurrencyInfo(symbol="BNT", name="Bancor Network Token"), scaling=Decimal("1e-18")
    ),
    "0x1f6324f07e452c4c63c14844f0aa9d235167fe72": TokenInfo(
        currency=CurrencyInfo(symbol="SYT", name="Syndicate Token"), scaling=Decimal("1e-18")
    ),
    "0x1f6deadcb526c4710cf941872b86dcdfbbbd9211": TokenInfo(
        currency=CurrencyInfo(symbol="RTK", name="Ruletka"), scaling=Decimal("1e-18")
    ),
    "0x1f6deaddc2a81704a206fd587d8e3643bd2d449c": TokenInfo(
        currency=CurrencyInfo(symbol="RTK", name="Ruletka"), scaling=Decimal("1e-18")
    ),
    "0x1f8f123bf24849443a56ed9fc42b9265b7f3a39a": TokenInfo(
        currency=CurrencyInfo(symbol="UTO", name="UniTopia Token"), scaling=Decimal("1e-18")
    ),
    "0x1f9232e7f1318abf91366e6081d57fa3c1bcde88": TokenInfo(
        currency=CurrencyInfo(symbol="LEML", name="Energy Source"), scaling=Decimal("1e-18")
    ),
    "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984": TokenInfo(
        currency=CurrencyInfo(symbol="UNI", name="Uniswap"), scaling=Decimal("1e-18")
    ),
    "0x1fa21b20222076d7465fb901e5f459289c95f66a": TokenInfo(
        currency=CurrencyInfo(symbol="XFII", name="XFII"), scaling=Decimal("1e-18")
    ),
    "0x1fa3bc860bf823d792f04f662f3aa3a500a68814": TokenInfo(
        currency=CurrencyInfo(symbol="HEDGE", name="1X Short Bitcoin Token"), scaling=Decimal("1e-18")
    ),
    "0x1fb6bccc7da51aa32e96118b8a33226d2ae16517": TokenInfo(
        currency=CurrencyInfo(symbol="GRT", name="Global Rental Token"), scaling=Decimal("1e-8")
    ),
    "0x1fbbcfcfe97f27dea1b5e97fbfeb488b8b63e478": TokenInfo(
        currency=CurrencyInfo(symbol="XPERL", name="Perlin IOU"), scaling=Decimal("1e-18")
    ),
    "0x1fc31488f28ac846588ffa201cde0669168471bd": TokenInfo(
        currency=CurrencyInfo(symbol="UAX", name="UAX"), scaling=Decimal("1e-2")
    ),
    "0x1fc5ef0337aea85c5f9198853a6e3a579a7a6987": TokenInfo(
        currency=CurrencyInfo(symbol="REAP", name="ReapChain"), scaling=Decimal("1e-18")
    ),
    "0x1fcdce58959f536621d76f5b7ffb955baa5a672f": TokenInfo(
        currency=CurrencyInfo(symbol="FOR", name="ForTube"), scaling=Decimal("1e-18")
    ),
    "0x1fd154b4d0e3753b714b511a53fe1fb72dc7ae1c": TokenInfo(
        currency=CurrencyInfo(symbol="SWD", name="SW DAO"), scaling=Decimal("1e-18")
    ),
    "0x1fdab294eda5112b7d066ed8f2e4e562d5bcc664": TokenInfo(
        currency=CurrencyInfo(symbol="SPICE", name="SPICE"), scaling=Decimal("1e-18")
    ),
    "0x1fe24f25b1cf609b9c4e7e12d802e3640dfa5e43": TokenInfo(
        currency=CurrencyInfo(symbol="CGG", name="Chain Guardians"), scaling=Decimal("1e-18")
    ),
    "0x1fe70be734e473e5721ea57c8b5b01e6caa52686": TokenInfo(
        currency=CurrencyInfo(symbol="RNTB", name="BitRent"), scaling=Decimal("1e-18")
    ),
    "0x1fff4dd33105054e853955c6d0dba82859c01cff": TokenInfo(
        currency=CurrencyInfo(symbol="UNOC", name="Unochain"), scaling=Decimal("1e-18")
    ),
    "0x2001f2a0cf801ecfda622f6c28fb6e10d803d969": TokenInfo(
        currency=CurrencyInfo(symbol="CLT", name="CoinLoan"), scaling=Decimal("1e-8")
    ),
    "0x2008e3057bd734e10ad13c9eae45ff132abc1722": TokenInfo(
        currency=CurrencyInfo(symbol="ZCO", name="Zebi"), scaling=Decimal("1e-8")
    ),
    "0x2023dcf7c438c8c8c0b0f28dbae15520b4f3ee20": TokenInfo(
        currency=CurrencyInfo(symbol="FTR", name="FutouristToken"), scaling=Decimal("1e-18")
    ),
    "0x202507992e29f29bb417b0281c067e91061b07d3": TokenInfo(
        currency=CurrencyInfo(symbol="BPAK9", name="Bitpakcoin9"), scaling=Decimal("1e-8")
    ),
    "0x20649d97b1393105cf92a5083fd2aff7c99ebe56": TokenInfo(
        currency=CurrencyInfo(symbol="BTCLOVOL", name="BTC Range Bond Low Volatility Set"), scaling=Decimal("1e-18")
    ),
    "0x208bbb6bcea22ef2011789331405347394ebaa51": TokenInfo(
        currency=CurrencyInfo(symbol="1AI", name="1AI"), scaling=Decimal("1e-18")
    ),
    "0x208d174775dc39fe18b1b374972f77ddec6c0f73": TokenInfo(
        currency=CurrencyInfo(symbol="UUSDRBTC-OCT", name="uUSDrBTC Synthetic Token Expiring 1 October 2020"),
        scaling=Decimal("1e-18"),
    ),
    "0x20900587e569e3d0b2609bca6fb3469765ed0920": TokenInfo(
        currency=CurrencyInfo(symbol="BTP", name="Bitpoint"), scaling=Decimal("1e-18")
    ),
    "0x20910e5b5f087f6439dfcb0dda4e27d1014ac2b8": TokenInfo(
        currency=CurrencyInfo(symbol="BNA", name="BananaTok"), scaling=Decimal("1e-18")
    ),
    "0x20945ca1df56d237fd40036d47e866c7dccd2114": TokenInfo(
        currency=CurrencyInfo(symbol="NSURE", name="Nsure Network"), scaling=Decimal("1e-18")
    ),
    "0x2098253aa66ec0510816ca5e5de9e2657bf01224": TokenInfo(
        currency=CurrencyInfo(symbol="EU50.CX", name="Euro Stoxx 50"), scaling=Decimal("1e-8")
    ),
    "0x20a8cec5fffea65be7122bcab2ffe32ed4ebf03a": TokenInfo(
        currency=CurrencyInfo(symbol="DNXC", name="DinoX"), scaling=Decimal("1e-18")
    ),
    "0x20ae0ca9d42e6ffeb1188f341a7d63450452def6": TokenInfo(
        currency=CurrencyInfo(symbol="CPR", name="CIPHER"), scaling=Decimal("1e-18")
    ),
    "0x20bc832ca081b91433ff6c17f85701b6e92486c5": TokenInfo(
        currency=CurrencyInfo(symbol="RETH2", name="rETH2"), scaling=Decimal("1e-18")
    ),
    "0x20bcae16a8ba95d8e8363e265de4ecfc36ec5cd9": TokenInfo(
        currency=CurrencyInfo(symbol="HYBN", name="HEY-BITCOIN"), scaling=Decimal("1e-18")
    ),
    "0x20c36f062a31865bed8a5b1e512d9a1a20aa333a": TokenInfo(
        currency=CurrencyInfo(symbol="DFD", name="DefiDollar DAO"), scaling=Decimal("1e-18")
    ),
    "0x20d236d3d74b90c00aba0fe0d7ed7d57e8b769a3": TokenInfo(
        currency=CurrencyInfo(symbol="USUB", name="U-Shares/Ubets"), scaling=Decimal("1e-4")
    ),
    "0x20e94867794dba030ee287f1406e100d03c84cd3": TokenInfo(
        currency=CurrencyInfo(symbol="DEW", name="DEW"), scaling=Decimal("1e-18")
    ),
    "0x20f7a3ddf244dc9299975b4da1c39f8d5d75f05a": TokenInfo(
        currency=CurrencyInfo(symbol="SPN", name="Sapien"), scaling=Decimal("1e-6")
    ),
    "0x2121a1b68e9c2cc8ff4bfd8bcd0f891ece331c51": TokenInfo(
        currency=CurrencyInfo(symbol="TANTAN", name="Tantan Token"), scaling=Decimal("1e-8")
    ),
    "0x2129ff6000b95a973236020bcd2b2006b0d8e019": TokenInfo(
        currency=CurrencyInfo(symbol="MYX", name="MYX Network"), scaling=Decimal("1e-18")
    ),
    "0x212dd60d4bf0da8372fe8116474602d429e5735f": TokenInfo(
        currency=CurrencyInfo(symbol="STBU", name="Stobox Token"), scaling=Decimal("1e-18")
    ),
    "0x2134057c0b461f898d375cead652acae62b59541": TokenInfo(
        currency=CurrencyInfo(symbol="CXC", name="CoxxxCoin"), scaling=Decimal("1e-18")
    ),
    "0x213c53c96a01a89e6dcc5683cf16473203e17513": TokenInfo(
        currency=CurrencyInfo(symbol="DSS", name="Defi Shopping Stake"), scaling=Decimal("1e-18")
    ),
    "0x21686f8ce003a95c99acd297e302faacf742f7d4": TokenInfo(
        currency=CurrencyInfo(symbol="WCCX", name="Wrapped Conceal"), scaling=Decimal("1e-6")
    ),
    "0x217ddead61a42369a266f1fb754eb5d3ebadc88a": TokenInfo(
        currency=CurrencyInfo(symbol="DON", name="Don key"), scaling=Decimal("1e-18")
    ),
    "0x217f96737b39f9b9211767cb6aef5dbae2fe9402": TokenInfo(
        currency=CurrencyInfo(symbol="WAY", name="Bazaar Gift Token"), scaling=Decimal("1e-8")
    ),
    "0x21839a7f7e88c19a6089adbfb3fb52606ac6f0dd": TokenInfo(
        currency=CurrencyInfo(symbol="FTO", name="FiveToken"), scaling=Decimal("1e-18")
    ),
    "0x2186ecb39f1b765ba7d78f1c43c2e9d7fc0c1eca": TokenInfo(
        currency=CurrencyInfo(symbol="MCP", name="My Crypto Play"), scaling=Decimal("1e-18")
    ),
    "0x218f1de2ea9ae3e9fdea347b6e707ebfda2d6233": TokenInfo(
        currency=CurrencyInfo(symbol="MPL", name="M+Plus"), scaling=Decimal("1e-18")
    ),
    "0x219218f117dc9348b358b8471c55a073e5e0da0b": TokenInfo(
        currency=CurrencyInfo(symbol="GRX", name="GOLD Reward Token"), scaling=Decimal("1e-18")
    ),
    "0x219f4a1d142dfc564bd6e80c022cd29f3394a999": TokenInfo(
        currency=CurrencyInfo(symbol="WXLM", name="Wrapped Stellar"), scaling=Decimal("1e-18")
    ),
    "0x21ab6c9fac80c59d401b37cb43f81ea9dde7fe34": TokenInfo(
        currency=CurrencyInfo(symbol="BRC", name="Baer Chain"), scaling=Decimal("1e-8")
    ),
    "0x21ad647b8f4fe333212e735bfc1f36b4941e6ad2": TokenInfo(
        currency=CurrencyInfo(symbol="SQUID", name="SquidDao"), scaling=Decimal("1e-9")
    ),
    "0x21ae23b882a340a22282162086bc98d3e2b73018": TokenInfo(
        currency=CurrencyInfo(symbol="LOK", name="LookRev"), scaling=Decimal("1e-18")
    ),
    "0x21bfbda47a0b4b5b1248c767ee49f7caa9b23697": TokenInfo(
        currency=CurrencyInfo(symbol="OVR", name="Ovr"), scaling=Decimal("1e-18")
    ),
    "0x21ca39943e91d704678f5d00b6616650f066fd63": TokenInfo(
        currency=CurrencyInfo(symbol="MTSLA", name="Mirrored Tesla"), scaling=Decimal("1e-18")
    ),
    "0x21d5678a62dfe63a47062469ebb2fac2817d8832": TokenInfo(
        currency=CurrencyInfo(symbol="YLC", name="YOLOCash"), scaling=Decimal("1e-8")
    ),
    "0x21e13cb3f3f26f92a62ac7adab4093e8997d1fb1": TokenInfo(
        currency=CurrencyInfo(symbol="OIKOS", name="OIKOS"), scaling=Decimal("1e-2")
    ),
    "0x21efe20be784ac5da569f72070e64525f95ccab6": TokenInfo(
        currency=CurrencyInfo(symbol="AZBI", name="AZBI core"), scaling=Decimal("1e-18")
    ),
    "0x21f0f0fd3141ee9e11b3d7f13a1028cd515f459c": TokenInfo(
        currency=CurrencyInfo(symbol="MRP", name="Money Rebel"), scaling=Decimal("1e-18")
    ),
    "0x21f15966e07a10554c364b988e91dab01d32794a": TokenInfo(
        currency=CurrencyInfo(symbol="SMT", name="SmartMesh"), scaling=Decimal("1e-18")
    ),
    "0x21f54372c07b930b79c5c2d9bb0eaaca86c3b298": TokenInfo(
        currency=CurrencyInfo(symbol="BANANA", name="Banana Finance"), scaling=Decimal("1e-18")
    ),
    "0x221535cbced4c264e53373d81b73c29d010832a5": TokenInfo(
        currency=CurrencyInfo(symbol="XMOO", name="Cloud Moolah"), scaling=Decimal("1e-18")
    ),
    "0x221657776846890989a759ba2973e427dff5c9bb": TokenInfo(
        currency=CurrencyInfo(symbol="REP", name="Augur"), scaling=Decimal("1e-18")
    ),
    "0x2216e873ea4282ebef7a02ac5aea220be6391a7c": TokenInfo(
        currency=CurrencyInfo(symbol="SMOL", name="smol"), scaling=Decimal("1e-18")
    ),
    "0x221c64c978d98bc34e49219e921e2ec8f318b05a": TokenInfo(
        currency=CurrencyInfo(symbol="ETD", name="EtherDiamond"), scaling=Decimal("1e-8")
    ),
    "0x221f7d0f2fa0bfbd5f8b0d0340425906f2f9968c": TokenInfo(
        currency=CurrencyInfo(symbol="SRC", name="Super Running Coin"), scaling=Decimal("1e-18")
    ),
    "0x222139425bcb172721dd4c22c29dd841d4358f69": TokenInfo(
        currency=CurrencyInfo(symbol="XOXO", name="Bitxoxo"), scaling=Decimal("1e-18")
    ),
    "0x22314b3d1375548c969eaae65e43203b51f9e9e9": TokenInfo(
        currency=CurrencyInfo(symbol="PLST", name="Philosafe Token"), scaling=Decimal("1e-2")
    ),
    "0x2233799ee2683d75dfefacbcd2a26c78d34b470d": TokenInfo(
        currency=CurrencyInfo(symbol="NTWK", name="Network Token"), scaling=Decimal("1e-18")
    ),
    "0x223b6e268eea352572c3d081039daf00c822a4c5": TokenInfo(
        currency=CurrencyInfo(symbol="CRC", name="Crypto Chain"), scaling=Decimal("1e-18")
    ),
    "0x223fb5c14c00cfb70cf56bb63c2eef2d74fe1a78": TokenInfo(
        currency=CurrencyInfo(symbol="DRGNBEAR", name="3X Short Dragon Index Token"), scaling=Decimal("1e-18")
    ),
    "0x224db5e6180761df4c3d8936585f6b8b83879770": TokenInfo(
        currency=CurrencyInfo(symbol="OML", name="OM Lira"), scaling=Decimal("1e-18")
    ),
    "0x2255dd4df9b6692fdff39f2924aaa679717b168c": TokenInfo(
        currency=CurrencyInfo(symbol="BKF", name="BKEX Finance"), scaling=Decimal("1e-18")
    ),
    "0x225927f8fa71d16ee07968b8746364d1d9f839bd": TokenInfo(
        currency=CurrencyInfo(symbol="BTCF", name="Bitcoin Fast BTCF"), scaling=Decimal("1e-8")
    ),
    "0x22602469d704bffb0936c7a7cfcd18f7aa269375": TokenInfo(
        currency=CurrencyInfo(symbol="SETC", name="sETC"), scaling=Decimal("1e-18")
    ),
    "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599": TokenInfo(
        currency=CurrencyInfo(symbol="WBTC", name="Wrapped Bitcoin"), scaling=Decimal("1e-8")
    ),
    "0x226bb599a12c826476e3a771454697ea52e9e220": TokenInfo(
        currency=CurrencyInfo(symbol="PRO", name="Propy"), scaling=Decimal("1e-8")
    ),
    "0x226f15cdbaa36814ce3cb287563069c32cc1a293": TokenInfo(
        currency=CurrencyInfo(symbol="CFX", name="CRYPTOFOREX"), scaling=Decimal("1e-2")
    ),
    "0x226f7b842e0f0120b7e194d05432b3fd14773a9d": TokenInfo(
        currency=CurrencyInfo(symbol="UNN", name="UNION Protocol Governance Token"), scaling=Decimal("1e-18")
    ),
    "0x228ba514309ffdf03a81a205a6d040e429d6e80c": TokenInfo(
        currency=CurrencyInfo(symbol="GSC", name="Global Social Chain"), scaling=Decimal("1e-18")
    ),
    "0x228e009ab91491880adb0eda6ed1bcd640ffd020": TokenInfo(
        currency=CurrencyInfo(symbol="GUS", name="GuessChain"), scaling=Decimal("1e-5")
    ),
    "0x2297af5e7e48be46c61a9e6164f64bd44ddc6ca3": TokenInfo(
        currency=CurrencyInfo(symbol="SPYA", name="SPY AGENTS"), scaling=Decimal("1e-18")
    ),
    "0x229a569b673d908cee8920658ae7bcad68e7d01d": TokenInfo(
        currency=CurrencyInfo(symbol="KRS", name="KORIS"), scaling=Decimal("1e-18")
    ),
    "0x229d1ed07310a9aaaf7bda570825b0c4089b88ad": TokenInfo(
        currency=CurrencyInfo(symbol="DEMA", name="Demetracoin"), scaling=Decimal("1e-18")
    ),
    "0x22acaee85ddb83a3a33b7f0928a0e2c3bfdb6a4f": TokenInfo(
        currency=CurrencyInfo(symbol="PRXY", name="Proxy"), scaling=Decimal("1e-18")
    ),
    "0x22c8ecf727c23422f47093b562ec53c139805301": TokenInfo(
        currency=CurrencyInfo(
            symbol="REALTOKEN-16200-FULLERTON-AVE-DETROIT-MI", name="RealToken16200 Fullerton Avenue Detroit MI"
        ),
        scaling=Decimal("1e-18"),
    ),
    "0x22cabb38295eaeccfede4e99af508052e3b74ca0": TokenInfo(
        currency=CurrencyInfo(
            symbol="REALTOKEN-18900-MANSFIELD-ST-DETROIT-MI", name="RealToken 18900 Mansfield St Detroit MI"
        ),
        scaling=Decimal("1e-18"),
    ),
    "0x22e3c3a3bda39c897a48257bc822e7466f171729": TokenInfo(
        currency=CurrencyInfo(symbol="NOIA", name="METANOIA"), scaling=Decimal("1e-18")
    ),
    "0x22e5f62d0fa19974749faa194e3d3ef6d89c08d7": TokenInfo(
        currency=CurrencyInfo(symbol="IMT", name="Immortal"), scaling=Decimal("1e-0")
    ),
    "0x22f098f08c4eda4be4ad6b4ba59866f3e98cef92": TokenInfo(
        currency=CurrencyInfo(symbol="FFF", name="Force For Fast"), scaling=Decimal("1e-18")
    ),
    "0x22f0af8d78851b72ee799e05f54a77001586b18a": TokenInfo(
        currency=CurrencyInfo(symbol="GXVC", name="Genevieve VC"), scaling=Decimal("1e-10")
    ),
    "0x22f39b18d17665177f1ac88d6da4861b13be07df": TokenInfo(
        currency=CurrencyInfo(symbol="LEODOOM", name="10X Short LEO Token"), scaling=Decimal("1e-18")
    ),
    "0x23348160d7f5aca21195df2b70f28fce2b0be9fc": TokenInfo(
        currency=CurrencyInfo(symbol="sFTSE", name="Synth sFTSE"), scaling=Decimal("1e-18")
    ),
    "0x23352036e911a22cfc692b5e2e196692658aded9": TokenInfo(
        currency=CurrencyInfo(symbol="FDZ", name="Friendz"), scaling=Decimal("1e-18")
    ),
    "0x2344871f523cbb28a4f60045531184cf1f03ad24": TokenInfo(
        currency=CurrencyInfo(symbol="ROBET", name="RoBet Coin"), scaling=Decimal("1e-18")
    ),
    "0x2352858080a45d776609b5449a1b8dcb1ae549c8": TokenInfo(
        currency=CurrencyInfo(symbol="TLC", name="True Life Coin"), scaling=Decimal("1e-18")
    ),
    "0x2365a4890ed8965e564b7e2d27c38ba67fec4c6f": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNIWBTCUSDC", name="Aave AMM UniWBTCUSD"), scaling=Decimal("1e-16")
    ),
    "0x2367012ab9c3da91290f71590d5ce217721eefe4": TokenInfo(
        currency=CurrencyInfo(symbol="XSNXA", name="xSNXa"), scaling=Decimal("1e-18")
    ),
    "0x23935765cdf2f7548f86042ff053d16a22c4e240": TokenInfo(
        currency=CurrencyInfo(symbol="TRZ", name="TRADEZ"), scaling=Decimal("1e-18")
    ),
    "0x2396fbc0e2e3ae4b7206ebdb5706e2a5920349cb": TokenInfo(
        currency=CurrencyInfo(symbol="CLR", name="Color Platform"), scaling=Decimal("1e-18")
    ),
    "0x239836e951dd75fea01bef8ba039119dc8d5352f": TokenInfo(
        currency=CurrencyInfo(symbol="BPC", name="Boostedpro Coin"), scaling=Decimal("1e-18")
    ),
    "0x239b0fa917d85c21cf6435464c2c6aa3d45f6720": TokenInfo(
        currency=CurrencyInfo(symbol="ETH3L", name="Amun Ether 3x Daily Long"), scaling=Decimal("1e-18")
    ),
    "0x23a86b3c53e7c7878d6b908f53c8fd31596cde7b": TokenInfo(
        currency=CurrencyInfo(symbol="RNO", name="SmartRhino"), scaling=Decimal("1e-18")
    ),
    "0x23ae3c5b39b12f0693e05435eeaa1e51d8c61530": TokenInfo(
        currency=CurrencyInfo(symbol="APT", name="Aigang Pre-Launch Token"), scaling=Decimal("1e-18")
    ),
    "0x23aeff664c1b2bba98422a0399586e96cc8a1c92": TokenInfo(
        currency=CurrencyInfo(symbol="FACT", name="Fee Active Collateral Token"), scaling=Decimal("1e-18")
    ),
    "0x23b608675a2b2fb1890d3abbd85c5775c51691d5": TokenInfo(
        currency=CurrencyInfo(symbol="SOCKS", name="Unisocks"), scaling=Decimal("1e-18")
    ),
    "0x23b75bc7aaf28e2d6628c3f424b3882f8f072a3c": TokenInfo(
        currency=CurrencyInfo(symbol="VIT", name="Vice Industry Token"), scaling=Decimal("1e-18")
    ),
    "0x23ccc43365d9dd3882eab88f43d515208f832430": TokenInfo(
        currency=CurrencyInfo(symbol="MAS", name="Midas Protocol"), scaling=Decimal("1e-18")
    ),
    "0x23f043426b2336e723b32fb3bf4a1ca410f7c49a": TokenInfo(
        currency=CurrencyInfo(symbol="RON", name="RON"), scaling=Decimal("1e-18")
    ),
    "0x24083bb30072643c3bb90b44b7285860a755e687": TokenInfo(
        currency=CurrencyInfo(symbol="GELD", name="SGelderGER"), scaling=Decimal("1e-18")
    ),
    "0x2409d6059e2a8130c099e49f3cb418fd6c3d9aff": TokenInfo(
        currency=CurrencyInfo(symbol="BTCFUND", name="BTC Fund Active Trading Set"), scaling=Decimal("1e-18")
    ),
    "0x241ba672574a78a3a604cdd0a94429a73a84a324": TokenInfo(
        currency=CurrencyInfo(symbol="KWATT", name="4New"), scaling=Decimal("1e-18")
    ),
    "0x24456f2786d975973a0905fd53236c8311cc3006": TokenInfo(
        currency=CurrencyInfo(symbol="COSHIB", name="Shiba Inu VS COVID"), scaling=Decimal("1e-8")
    ),
    "0x2449224f42ce230c5b67e1d48bdceb224b0f72d7": TokenInfo(
        currency=CurrencyInfo(symbol="DIVM", name="DIVM"), scaling=Decimal("1e-18")
    ),
    "0x245392ee7ce736ec6a0908b67dc5d0a218230005": TokenInfo(
        currency=CurrencyInfo(symbol="YAP", name="Yap Stone"), scaling=Decimal("1e-18")
    ),
    "0x245ef47d4d0505ecf3ac463f4d81f41ade8f1fd1": TokenInfo(
        currency=CurrencyInfo(symbol="NUG", name="Nuggets"), scaling=Decimal("1e-18")
    ),
    "0x2467aa6b5a2351416fd4c3def8462d841feeecec": TokenInfo(
        currency=CurrencyInfo(symbol="QBX", name="qiibee"), scaling=Decimal("1e-18")
    ),
    "0x24692791bc444c5cd0b81e3cbcaba4b04acd1f3b": TokenInfo(
        currency=CurrencyInfo(symbol="UKG", name="Unikoin Gold"), scaling=Decimal("1e-18")
    ),
    "0x24700a297960e8477ce3ca6c58b70a7af3410398": TokenInfo(
        currency=CurrencyInfo(symbol="OSC", name="Oasis City"), scaling=Decimal("1e-18")
    ),
    "0x2474ca2e5a1ce0ca904ca512530c2555048603be": TokenInfo(
        currency=CurrencyInfo(symbol="OKBDOOM", name="10X Short OKB Token"), scaling=Decimal("1e-18")
    ),
    "0x247551f2eb3362e222c742e9c788b8957d9bc87e": TokenInfo(
        currency=CurrencyInfo(symbol="GNY", name="GNY"), scaling=Decimal("1e-18")
    ),
    "0x248ade18435f7b5e39d855cc98c42d8f6840a386": TokenInfo(
        currency=CurrencyInfo(symbol="ORBIT", name="Orbit"), scaling=Decimal("1e-3")
    ),
    "0x248c27f814ef2c9c51c26398d09715cd35142fc4": TokenInfo(
        currency=CurrencyInfo(symbol="CPL", name="Copylock"), scaling=Decimal("1e-18")
    ),
    "0x2494a68c1484376fef880b4c24d91f049d29b02a": TokenInfo(
        currency=CurrencyInfo(symbol="TTT", name="The Transfer Token"), scaling=Decimal("1e-18")
    ),
    "0x24982f160803daca0233661d1860de77046519a4": TokenInfo(
        currency=CurrencyInfo(symbol="MIDMOON", name="10X Long Midcap Index Token"), scaling=Decimal("1e-18")
    ),
    "0x249e38ea4102d0cf8264d3701f1a0e39c4f2dc3b": TokenInfo(
        currency=CurrencyInfo(symbol="UFO", name="UFO Gaming"), scaling=Decimal("1e-18")
    ),
    "0x249f71f8d9da86c60f485e021b509a206667a079": TokenInfo(
        currency=CurrencyInfo(symbol="SNGJ", name="Singular J"), scaling=Decimal("1e-18")
    ),
    "0x24a6a37576377f63f194caa5f518a60f45b42921": TokenInfo(
        currency=CurrencyInfo(symbol="BANK", name="Float Protocol"), scaling=Decimal("1e-18")
    ),
    "0x24a77c1f17c547105e14813e517be06b0040aa76": TokenInfo(
        currency=CurrencyInfo(symbol="LIVE", name="Live Stars"), scaling=Decimal("1e-18")
    ),
    "0x24aef3bf1a47561500f9430d74ed4097c47f51f2": TokenInfo(
        currency=CurrencyInfo(symbol="SPARTA", name="Sparta"), scaling=Decimal("1e-4")
    ),
    "0x24bbac3a6148320cf9ee20d9abeb8dd5a4800b52": TokenInfo(
        currency=CurrencyInfo(symbol="AR.CX", name="Antero Resources"), scaling=Decimal("1e-8")
    ),
    "0x24d77c210a014b1e123a0878f6c903df74a2317b": TokenInfo(
        currency=CurrencyInfo(symbol="BXT", name="Bitfxt Coin"), scaling=Decimal("1e-8")
    ),
    "0x24dcc881e7dd730546834452f21872d5cb4b5293": TokenInfo(
        currency=CurrencyInfo(symbol="XD", name="Data Transaction Token"), scaling=Decimal("1e-18")
    ),
    "0x24ddff6d8b8a42d835af3b440de91f3386554aa4": TokenInfo(
        currency=CurrencyInfo(symbol="ING", name="Iungo"), scaling=Decimal("1e-18")
    ),
    "0x24e3794605c84e580eea4972738d633e8a7127c8": TokenInfo(
        currency=CurrencyInfo(symbol="KTLYO", name="Katalyo"), scaling=Decimal("1e-18")
    ),
    "0x24e96809b4e720ea911bc3de8341400e26d6e994": TokenInfo(
        currency=CurrencyInfo(symbol="VRTN", name="VINYL RECORDS TOKEN"), scaling=Decimal("1e-18")
    ),
    "0x24ec2ca132abf8f6f8a6e24a1b97943e31f256a7": TokenInfo(
        currency=CurrencyInfo(symbol="MOOV", name="dotmoovs"), scaling=Decimal("1e-18")
    ),
    "0x24fb4c36a83cbdbcd670856406f622e09a643d4d": TokenInfo(
        currency=CurrencyInfo(symbol="HNT", name="Hinto"), scaling=Decimal("1e-5")
    ),
    "0x2509b1a5ff82ab94172cfc527676acf45c2a0d08": TokenInfo(
        currency=CurrencyInfo(symbol="GMD", name="The Geoma DAO"), scaling=Decimal("1e-16")
    ),
    "0x250a3500f48666561386832f1f1f1019b89a2699": TokenInfo(
        currency=CurrencyInfo(symbol="SAFE2", name="SAFE2"), scaling=Decimal("1e-18")
    ),
    "0x2516ac5db37df788f8f6ef69ecaa7cd76652eae2": TokenInfo(
        currency=CurrencyInfo(symbol="LOM", name="Ltconlinemarkets"), scaling=Decimal("1e-18")
    ),
    "0x25200235ca7113c2541e70de737c41f5e9acd1f6": TokenInfo(
        currency=CurrencyInfo(symbol="PHV", name="PATHHIVE"), scaling=Decimal("1e-18")
    ),
    "0x252f830448d8890ca06a3ff78823db8d23587037": TokenInfo(
        currency=CurrencyInfo(symbol="BBOMB", name="BIGBOMB"), scaling=Decimal("1e-18")
    ),
    "0x2534409daa29b07682020d07eac9ae01c34acec0": TokenInfo(
        currency=CurrencyInfo(symbol="MRCL", name="Miracle Token"), scaling=Decimal("1e-18")
    ),
    "0x253444bd9ecf11e5516d6d00974e91c9f0857ccb": TokenInfo(
        currency=CurrencyInfo(symbol="EBLOAP", name="ETH/BTC Long-Only Alpha Portfolio"), scaling=Decimal("1e-18")
    ),
    "0x25377ddb16c79c93b0cbf46809c8de8765f03fcd": TokenInfo(
        currency=CurrencyInfo(symbol="SBREE", name="Synthetic CBDAO"), scaling=Decimal("1e-18")
    ),
    "0x253c7dd074f4bacb305387f922225a4f737c08bd": TokenInfo(
        currency=CurrencyInfo(symbol="LOOK", name="LookRev"), scaling=Decimal("1e-18")
    ),
    "0x254bca53a17a1c6e1ada05c06aff042684e846c2": TokenInfo(
        currency=CurrencyInfo(symbol="CGN", name="Cygnity"), scaling=Decimal("1e-8")
    ),
    "0x255aa6df07540cb5d3d297f0d0d4d84cb52bc8e6": TokenInfo(
        currency=CurrencyInfo(symbol="RDN", name="Raiden Network Token"), scaling=Decimal("1e-18")
    ),
    "0x2564c4df85bbccef04b870d42f96bcc627b24957": TokenInfo(
        currency=CurrencyInfo(symbol="CTA", name="Culture Travel Agriculture"), scaling=Decimal("1e-18")
    ),
    "0x2565ae0385659badcada1031db704442e1b69982": TokenInfo(
        currency=CurrencyInfo(symbol="ASM", name="Assemble Protocol"), scaling=Decimal("1e-18")
    ),
    "0x25677657e70694c79f64c3d477796acb43a6f1c0": TokenInfo(
        currency=CurrencyInfo(symbol="TMP", name="TeleMart Pro"), scaling=Decimal("1e-5")
    ),
    "0x2567c677473d110d75a8360c35309e63b1d52429": TokenInfo(
        currency=CurrencyInfo(symbol="SEXC", name="ShareX"), scaling=Decimal("1e-8")
    ),
    "0x256845e721c0c46d54e6afbd4fa3b52cb72353ea": TokenInfo(
        currency=CurrencyInfo(symbol="UNIUSD", name="UniDollar"), scaling=Decimal("1e-18")
    ),
    "0x2578a20a07e8761d91d0961d3ea92e14510885aa": TokenInfo(
        currency=CurrencyInfo(symbol="CVR", name="COVIR"), scaling=Decimal("1e-18")
    ),
    "0x2579bb08387f0de7ab135edd6c2a985a3f577b6b": TokenInfo(
        currency=CurrencyInfo(symbol="SBX", name="Sports Betting Marketplace"), scaling=Decimal("1e-18")
    ),
    "0x258fec90b7788e60da3bc6f81d5839dc5b36a110": TokenInfo(
        currency=CurrencyInfo(symbol="ALTHEDGE", name="1X Short Altcoin Index Token"), scaling=Decimal("1e-18")
    ),
    "0x259059f137cb9b8f60ae27bd199d97abb69e539b": TokenInfo(
        currency=CurrencyInfo(symbol="SPEC", name="SpectrumNetwork"), scaling=Decimal("1e-18")
    ),
    "0x25a3dcabbf0070cb8e5baaa62d576cf6643afb5b": TokenInfo(
        currency=CurrencyInfo(symbol="ALMX", name="Almace Shards"), scaling=Decimal("1e-18")
    ),
    "0x25b6325f5bb1c1e03cfbc3e53f470e1f1ca022e3": TokenInfo(
        currency=CurrencyInfo(symbol="LML", name="Lisk Machine Learning"), scaling=Decimal("1e-18")
    ),
    "0x25c7b64a93eb1261e130ec21a3e9918caa38b611": TokenInfo(
        currency=CurrencyInfo(symbol="WVG0", name="Wrapped Virgin Gen-0 CryptoKittties"), scaling=Decimal("1e-18")
    ),
    "0x25ce333b325f02c9720da526a01b5f5be889b4e3": TokenInfo(
        currency=CurrencyInfo(symbol="BMJ", name="BMJ Coin"), scaling=Decimal("1e-18")
    ),
    "0x25cef4fb106e76080e88135a0e4059276fa9be87": TokenInfo(
        currency=CurrencyInfo(symbol="UNITS", name="Imperial"), scaling=Decimal("1e-5")
    ),
    "0x25d9bef26b6f7018d24d18144fe3c8bfd0d48a53": TokenInfo(
        currency=CurrencyInfo(symbol="AGN", name="Agrichainx"), scaling=Decimal("1e-18")
    ),
    "0x25e1474170c4c0aa64fa98123bdc8db49d7802fa": TokenInfo(
        currency=CurrencyInfo(symbol="BID", name="Bidao"), scaling=Decimal("1e-18")
    ),
    "0x25f735b108b4273fb0aceb87599ed8bba10065de": TokenInfo(
        currency=CurrencyInfo(symbol="TILE", name="Loomia"), scaling=Decimal("1e-18")
    ),
    "0x25f8087ead173b73d6e8b84329989a8eea16cf73": TokenInfo(
        currency=CurrencyInfo(symbol="YGG", name="Yield Guild Games"), scaling=Decimal("1e-18")
    ),
    "0x2602278ee1882889b946eb11dc0e810075650983": TokenInfo(
        currency=CurrencyInfo(symbol="VADER", name="Vader Protocol"), scaling=Decimal("1e-18")
    ),
    "0x2604fa406be957e542beb89e6754fcde6815e83f": TokenInfo(
        currency=CurrencyInfo(symbol="PKT", name="PlayKey"), scaling=Decimal("1e-18")
    ),
    "0x260e63d91fccc499606bae3fe945c4ed1cf56a56": TokenInfo(
        currency=CurrencyInfo(symbol="MOONS", name="MoonTools"), scaling=Decimal("1e-18")
    ),
    "0x261638ec8ee8100484130ebd2febfdadc0d8742a": TokenInfo(
        currency=CurrencyInfo(symbol="LVX", name="LVX"), scaling=Decimal("1e-18")
    ),
    "0x261b45d85ccfeabb11f022eba346ee8d1cd488c0": TokenInfo(
        currency=CurrencyInfo(symbol="RDAI", name="rDAI"), scaling=Decimal("1e-18")
    ),
    "0x261efcdd24cea98652b9700800a13dfbca4103ff": TokenInfo(
        currency=CurrencyInfo(symbol="SXAU", name="sXAU"), scaling=Decimal("1e-18")
    ),
    "0x263c618480dbe35c300d8d5ecda19bbb986acaed": TokenInfo(
        currency=CurrencyInfo(symbol="MOT", name="Olympus Labs"), scaling=Decimal("1e-18")
    ),
    "0x264dc2dedcdcbb897561a57cba5085ca416fb7b4": TokenInfo(
        currency=CurrencyInfo(symbol="QUN", name="QunQun"), scaling=Decimal("1e-18")
    ),
    "0x26548041e3a78fdc60f3cce21977e1f5e46561b7": TokenInfo(
        currency=CurrencyInfo(symbol="ZCC", name="ZuCoinChain"), scaling=Decimal("1e-18")
    ),
    "0x26587f4d672876e61a91b887f83ced591be1cba4": TokenInfo(
        currency=CurrencyInfo(symbol="SKR", name="Staking"), scaling=Decimal("1e-8")
    ),
    "0x265ba42daf2d20f3f358a7361d9f69cb4e28f0e6": TokenInfo(
        currency=CurrencyInfo(symbol="UBOMB", name="Unibomb"), scaling=Decimal("1e-18")
    ),
    "0x26607ac599266b21d13c7acf7942c7701a8b699c": TokenInfo(
        currency=CurrencyInfo(symbol="PIPT", name="Power Index Pool Token"), scaling=Decimal("1e-18")
    ),
    "0x267ba09fe3a8a16c7dc8a9b07b5f2c4ac0adf1c0": TokenInfo(
        currency=CurrencyInfo(symbol="BTE", name="BitEnergy"), scaling=Decimal("1e-8")
    ),
    "0x26946ada5ecb57f3a1f91605050ce45c482c9eb1": TokenInfo(
        currency=CurrencyInfo(symbol="BSOV", name="BitcoinSoV"), scaling=Decimal("1e-8")
    ),
    "0x26a604dffe3ddab3bee816097f81d3c4a2a4cf97": TokenInfo(
        currency=CurrencyInfo(symbol="CORX", name="CorionX"), scaling=Decimal("1e-8")
    ),
    "0x26ac29dc25806199373cb4884aa9e077a0587c5b": TokenInfo(
        currency=CurrencyInfo(symbol="ftc", name="free trade chain"), scaling=Decimal("1e-18")
    ),
    "0x26b3038a7fc10b36c426846a9086ef87328da702": TokenInfo(
        currency=CurrencyInfo(symbol="YFT", name="Yield Farming Token"), scaling=Decimal("1e-18")
    ),
    "0x26c0e6f69b18125f68ac55f439b1e10c2a2e5c03": TokenInfo(
        currency=CurrencyInfo(symbol="CROWD", name="Crowdvilla Point"), scaling=Decimal("1e-8")
    ),
    "0x26c8afbbfe1ebaca03c2bb082e69d0476bffe099": TokenInfo(
        currency=CurrencyInfo(symbol="CELL", name="Cellframe"), scaling=Decimal("1e-18")
    ),
    "0x26cb3641aaa43911f1d4cb2ce544eb652aac7c47": TokenInfo(
        currency=CurrencyInfo(symbol="CYL", name="Crystal Token"), scaling=Decimal("1e-18")
    ),
    "0x26ce25148832c04f3d7f26f32478a9fe55197166": TokenInfo(
        currency=CurrencyInfo(symbol="DEXT", name="DexTools"), scaling=Decimal("1e-18")
    ),
    "0x26cf82e4ae43d31ea51e72b663d26e26a75af729": TokenInfo(
        currency=CurrencyInfo(symbol="MBBASED", name="Moonbase"), scaling=Decimal("1e-18")
    ),
    "0x26db5439f651caf491a87d48799da81f191bdb6b": TokenInfo(
        currency=CurrencyInfo(symbol="CBC", name="CBC.network"), scaling=Decimal("1e-8")
    ),
    "0x26ddf6cabadcbf4f013841bd8d914830beb0d984": TokenInfo(
        currency=CurrencyInfo(symbol="KT", name="Kuai Token"), scaling=Decimal("1e-8")
    ),
    "0x26e43759551333e57f073bb0772f50329a957b30": TokenInfo(
        currency=CurrencyInfo(symbol="DGVC", name="DegenVC"), scaling=Decimal("1e-18")
    ),
    "0x26e75307fc0c021472feb8f727839531f112f317": TokenInfo(
        currency=CurrencyInfo(symbol="C20", name="CRYPTO20"), scaling=Decimal("1e-18")
    ),
    "0x26ea73221553a1a1cc07cb8f351839b299dcc9f8": TokenInfo(
        currency=CurrencyInfo(symbol="PYPL.CX", name="PayPal Holdings"), scaling=Decimal("1e-8")
    ),
    "0x26ea744e5b887e5205727f55dfbe8685e3b21951": TokenInfo(
        currency=CurrencyInfo(symbol="YUSDC", name="yUSDC (BUSD pool)"), scaling=Decimal("1e-6")
    ),
    "0x26fb86579e371c7aedc461b2ddef0a8628c93d3b": TokenInfo(
        currency=CurrencyInfo(symbol="BORA", name="BORA"), scaling=Decimal("1e-18")
    ),
    "0x27054b13b1b798b345b591a4d22e6562d47ea75a": TokenInfo(
        currency=CurrencyInfo(symbol="AST", name="AirSwap"), scaling=Decimal("1e-4")
    ),
    "0x270d09cb4be817c98e84feffde03d5cd45e30a27": TokenInfo(
        currency=CurrencyInfo(symbol="MAKI", name="Maki Finance"), scaling=Decimal("1e-18")
    ),
    "0x271220fbefd584a6b0a6ad457721c076321646a1": TokenInfo(
        currency=CurrencyInfo(symbol="FEX", name="FEX Token"), scaling=Decimal("1e-18")
    ),
    "0x27269b3e45a4d3e79a3d6bfee0c8fb13d0d711a6": TokenInfo(
        currency=CurrencyInfo(symbol="IXRP", name="iXRP"), scaling=Decimal("1e-18")
    ),
    "0x272f97b7a56a387ae942350bbc7df5700f8a4576": TokenInfo(
        currency=CurrencyInfo(symbol="ABAL", name="Aave BAL"), scaling=Decimal("1e-18")
    ),
    "0x2730d6fdc86c95a74253beffaa8306b40fedecbb": TokenInfo(
        currency=CurrencyInfo(symbol="UNI", name="UNICORN Token"), scaling=Decimal("1e-8")
    ),
    "0x2745822d171cc9de5717c2b9d3313a2bfaf1b149": TokenInfo(
        currency=CurrencyInfo(symbol="EXEL.CX", name="Exelixis Inc"), scaling=Decimal("1e-8")
    ),
    "0x27695e09149adc738a978e9a678f99e4c39e9eb9": TokenInfo(
        currency=CurrencyInfo(symbol="KICK", name="KickCoin"), scaling=Decimal("1e-8")
    ),
    "0x27702a26126e0b3702af63ee09ac4d1a084ef628": TokenInfo(
        currency=CurrencyInfo(symbol="ALEPH", name="Aleph.im"), scaling=Decimal("1e-18")
    ),
    "0x2775f2a3c83bee1541d1d1bc308b3bb432b45151": TokenInfo(
        currency=CurrencyInfo(symbol="PLANETAGRO", name="MEMBERSHIP"), scaling=Decimal("1e-18")
    ),
    "0x27778e14ce36d3b85e1effeb43816a17bbb7088a": TokenInfo(
        currency=CurrencyInfo(symbol="LGOLD", name="Lyfe Gold"), scaling=Decimal("1e-18")
    ),
    "0x2781246fe707bb15cee3e5ea354e2154a2877b16": TokenInfo(
        currency=CurrencyInfo(symbol="EL", name="ELYSIA"), scaling=Decimal("1e-18")
    ),
    "0x278a83b64c3e3e1139f8e8a52d96360ca3c69a3d": TokenInfo(
        currency=CurrencyInfo(symbol="NEXXO", name="Nexxo"), scaling=Decimal("1e-18")
    ),
    "0x2791bfd60d232150bff86b39b7146c0eaaa2ba81": TokenInfo(
        currency=CurrencyInfo(symbol="BIFI", name="BiFi"), scaling=Decimal("1e-18")
    ),
    "0x2793a23341012e0970cf478bab08606b56504c3e": TokenInfo(
        currency=CurrencyInfo(symbol="HBX", name="Hyperbridge"), scaling=Decimal("1e-18")
    ),
    "0x2799d90c6d44cb9aa5fbc377177f16c33e056b82": TokenInfo(
        currency=CurrencyInfo(symbol="DRP", name="Dripcoin"), scaling=Decimal("1e-0")
    ),
    "0x27b681934215dda5c4debf5b59f23eab9a8261cc": TokenInfo(
        currency=CurrencyInfo(symbol="VAL", name="Valora"), scaling=Decimal("1e-10")
    ),
    "0x27c1ba4f85b8dc1c150157816623a6ce80b7f187": TokenInfo(
        currency=CurrencyInfo(symbol="XRPBULL", name="3X Long XRP Token"), scaling=Decimal("1e-18")
    ),
    "0x27c743954bce1bfaef8bcbd685527531001d88d7": TokenInfo(
        currency=CurrencyInfo(symbol="BOK", name="Blockium Token"), scaling=Decimal("1e-18")
    ),
    "0x27d0e0da86da893053704dad1c9cc6e6b1ee37b0": TokenInfo(
        currency=CurrencyInfo(symbol="AA.CX", name="Alcoa"), scaling=Decimal("1e-8")
    ),
    "0x27d16a670bec2e2db9e0ca367aaee6758d2cb3c7": TokenInfo(
        currency=CurrencyInfo(symbol="QCSS", name="Quality Control Safety System"), scaling=Decimal("1e-18")
    ),
    "0x27dce1ec4d3f72c3e457cc50354f1f975ddef488": TokenInfo(
        currency=CurrencyInfo(symbol="AIR", name="AirToken"), scaling=Decimal("1e-8")
    ),
    "0x27e627d032593fe2a8ebbb30f3b1264b3b51a707": TokenInfo(
        currency=CurrencyInfo(symbol="PTC", name="PropertyCoin"), scaling=Decimal("1e-18")
    ),
    "0x27ed129c298c5df130364083f491e2920e5a2f29": TokenInfo(
        currency=CurrencyInfo(symbol="GBPU", name="Upper Pound"), scaling=Decimal("1e-18")
    ),
    "0x27f610bf36eca0939093343ac28b1534a721dbb4": TokenInfo(
        currency=CurrencyInfo(symbol="WAND", name="WandX"), scaling=Decimal("1e-18")
    ),
    "0x281f5b914b0d589f8193cd5e711c6920874e00c8": TokenInfo(
        currency=CurrencyInfo(symbol="MBM", name="MBM Token"), scaling=Decimal("1e-18")
    ),
    "0x2822f6d1b2f41f93f33d937bc7d84a8dfa4f4c21": TokenInfo(
        currency=CurrencyInfo(symbol="QQQ", name="Poseidon Network"), scaling=Decimal("1e-18")
    ),
    "0x282417b21236ac01a3a3d7ba304ed8d284f48b4d": TokenInfo(
        currency=CurrencyInfo(symbol="SCV", name="Super CoinView Token"), scaling=Decimal("1e-18")
    ),
    "0x282cb0a611280ff5887ca122911a0ca6b841cb03": TokenInfo(
        currency=CurrencyInfo(symbol="UWTC", name="UP Wallet"), scaling=Decimal("1e-6")
    ),
    "0x28317d822b6ac5a9f5b374536eb157e3f424c8d0": TokenInfo(
        currency=CurrencyInfo(symbol="BLT1", name="BILLIONS"), scaling=Decimal("1e-18")
    ),
    "0x2840ad41cf25ad58303ba24c416e79dce4161b4f": TokenInfo(
        currency=CurrencyInfo(symbol="BNBHEDGE", name="1X Short BNB Token"), scaling=Decimal("1e-18")
    ),
    "0x28577a6d31559bd265ce3adb62d0458550f7b8a7": TokenInfo(
        currency=CurrencyInfo(symbol="CCC", name="Crypto Crash Course"), scaling=Decimal("1e-18")
    ),
    "0x2859021ee7f2cb10162e67f33af2d22764b31aff": TokenInfo(
        currency=CurrencyInfo(symbol="SNTR", name="Silent Notary"), scaling=Decimal("1e-4")
    ),
    "0x2863916c6ebdbbf0c6f02f87b7eb478509299868": TokenInfo(
        currency=CurrencyInfo(symbol="SST", name="SIMBA Storage Token"), scaling=Decimal("1e-18")
    ),
    "0x286708f069225905194673755f12359e6aff6fe1": TokenInfo(
        currency=CurrencyInfo(symbol="STACS", name="STACS Token"), scaling=Decimal("1e-18")
    ),
    "0x286bda1413a2df81731d4930ce2f862a35a609fe": TokenInfo(
        currency=CurrencyInfo(symbol="WABI", name="Wabi"), scaling=Decimal("1e-18")
    ),
    "0x287609a15a683640a5bbc4d93d4d5f4ed6bad3a0": TokenInfo(
        currency=CurrencyInfo(symbol="PICK", name="PICK"), scaling=Decimal("1e-18")
    ),
    "0x289925d08b07e73dd0dd02d1407c877942215082": TokenInfo(
        currency=CurrencyInfo(symbol="AVY", name="AVY Token"), scaling=Decimal("1e-18")
    ),
    "0x28b5e12cce51f15594b0b91d5b5adaa70f684a02": TokenInfo(
        currency=CurrencyInfo(symbol="NPX", name="Napoleon X"), scaling=Decimal("1e-2")
    ),
    "0x28b94f58b11ac945341329dbf2e5ef7f8bd44225": TokenInfo(
        currency=CurrencyInfo(symbol="EMB", name="Emblem"), scaling=Decimal("1e-8")
    ),
    "0x28c391fbf3f5e10fb3fb8d6b2728419d3037409b": TokenInfo(
        currency=CurrencyInfo(symbol="KCH", name="King Cash"), scaling=Decimal("1e-18")
    ),
    "0x28c6a58c2a5d8c5f6681e07bfa0ada4bea14c9ee": TokenInfo(
        currency=CurrencyInfo(symbol="LONG", name="High Conviction / Fundamentals Set"), scaling=Decimal("1e-18")
    ),
    "0x28c8d01ff633ea9cd8fc6a451d7457889e698de6": TokenInfo(
        currency=CurrencyInfo(symbol="ETG", name="Ethereum Gold"), scaling=Decimal("1e-0")
    ),
    "0x28cb7e841ee97947a86b06fa4090c8451f64c0be": TokenInfo(
        currency=CurrencyInfo(symbol="YFL", name="YF Link"), scaling=Decimal("1e-18")
    ),
    "0x28d3e409bb9bc58f1ca6e009f8fc78a1db85e6b7": TokenInfo(
        currency=CurrencyInfo(symbol="GXT", name="Gem Exchange And Trading"), scaling=Decimal("1e-18")
    ),
    "0x28d7f432d24ba6020d1cbd4f28bedc5a82f24320": TokenInfo(
        currency=CurrencyInfo(symbol="TCNX", name="Tercet Network"), scaling=Decimal("1e-18")
    ),
    "0x28dee01d53fed0edf5f6e310bf8ef9311513ae40": TokenInfo(
        currency=CurrencyInfo(symbol="XBP", name="BlitzPredict"), scaling=Decimal("1e-18")
    ),
    "0x2904b9b16652d7d0408eccfa23a19d4a3358230f": TokenInfo(
        currency=CurrencyInfo(symbol="PURE", name="Puriever"), scaling=Decimal("1e-18")
    ),
    "0x29257908879c5792f1bb25449a7209205434dc3f": TokenInfo(
        currency=CurrencyInfo(symbol="ZBK", name="Zbank Token"), scaling=Decimal("1e-18")
    ),
    "0x293989bb8b44c73b59f3e1f379bc861a33bd6aea": TokenInfo(
        currency=CurrencyInfo(symbol="XRRT", name="XchangeRate"), scaling=Decimal("1e-18")
    ),
    "0x293b0cd0991db07c8529febb01bc7d052315c5ab": TokenInfo(
        currency=CurrencyInfo(symbol="ITO", name="InTime"), scaling=Decimal("1e-18")
    ),
    "0x29428639d889fa989405ee9baf3ba088e6994edc": TokenInfo(
        currency=CurrencyInfo(symbol="$BASED", name="$BASED"), scaling=Decimal("1e-18")
    ),
    "0x294caec1e7c1b674f409514af529af02e67cdb56": TokenInfo(
        currency=CurrencyInfo(symbol="MAYA", name="Maya Token"), scaling=Decimal("1e-18")
    ),
    "0x29536b7ca7029b5cddeb03c0451715615aca35ba": TokenInfo(
        currency=CurrencyInfo(symbol="NEWOS", name="NewsToken"), scaling=Decimal("1e-8")
    ),
    "0x296b3fc8e3cc768f834152586e5ad708bfe8f163": TokenInfo(
        currency=CurrencyInfo(symbol="FET", name="FirstEnergy Token"), scaling=Decimal("1e-18")
    ),
    "0x296ec7b2b224ea122f8f8f9be2a824df092fc82c": TokenInfo(
        currency=CurrencyInfo(symbol="SCAL", name="Scaltinof"), scaling=Decimal("1e-8")
    ),
    "0x2974963051f3a3237e16841dea7126250098d8f5": TokenInfo(
        currency=CurrencyInfo(symbol="SEL", name="STEM CELL PLATFORM"), scaling=Decimal("1e-0")
    ),
    "0x2976ac3d0bb67c6307a73df852c61c14cdda9863": TokenInfo(
        currency=CurrencyInfo(symbol="BTCN", name="Bitcoin Neo"), scaling=Decimal("1e-18")
    ),
    "0x297e4e5e59ad72b1b0a2fd446929e76117be0e0a": TokenInfo(
        currency=CurrencyInfo(symbol="VALOR", name="Smart Valor"), scaling=Decimal("1e-18")
    ),
    "0x298d492e8c1d909d3f63bc4a36c66c64acb3d695": TokenInfo(
        currency=CurrencyInfo(symbol="PBR", name="PolkaBridge"), scaling=Decimal("1e-18")
    ),
    "0x29bed564a9b1361c413a032fcb7bc196df8b213e": TokenInfo(
        currency=CurrencyInfo(symbol="BBBY.CX", name="Bed Bath & Beyond Inc"), scaling=Decimal("1e-8")
    ),
    "0x29cbd0510eec0327992cd6006e63f9fa8e7f33b7": TokenInfo(
        currency=CurrencyInfo(symbol="TIDAL", name="Tidal Finance"), scaling=Decimal("1e-18")
    ),
    "0x29d75277ac7f0335b2165d0895e8725cbf658d73": TokenInfo(
        currency=CurrencyInfo(symbol="CSNO", name="BitDice"), scaling=Decimal("1e-8")
    ),
    "0x29d84dd4559ff6d5a09596b549cc01b3af8f1e9e": TokenInfo(
        currency=CurrencyInfo(symbol="MCD.CX", name="McDonald's"), scaling=Decimal("1e-8")
    ),
    "0x29d9aac5ee0b954690cce0007a87adad129fe2e2": TokenInfo(
        currency=CurrencyInfo(symbol="TRI", name="Triward"), scaling=Decimal("1e-10")
    ),
    "0x29e9fdf5933824ad21bc6dbb8bf156efa3735e32": TokenInfo(
        currency=CurrencyInfo(symbol="EMTR", name="Meter Stable mapped by Meter.io"), scaling=Decimal("1e-18")
    ),
    "0x29ec3ff4e1dcad5a207dbd5d14e48073abba0bd3": TokenInfo(
        currency=CurrencyInfo(symbol="ZARX", name="eToro South African Rand"), scaling=Decimal("1e-18")
    ),
    "0x29ff774b920b8ff581108d0c12e5073df5158e8a": TokenInfo(
        currency=CurrencyInfo(symbol="TITAN", name="TitanSwap"), scaling=Decimal("1e-18")
    ),
    "0x2a05d22db079bc40c2f77a1d1ff703a56e631cc1": TokenInfo(
        currency=CurrencyInfo(symbol="BAS", name="BitAsean"), scaling=Decimal("1e-8")
    ),
    "0x2a093bcf0c98ef744bb6f69d74f2f85605324290": TokenInfo(
        currency=CurrencyInfo(symbol="FOOD", name="FoodCoin"), scaling=Decimal("1e-8")
    ),
    "0x2a1dbabe65c595b0022e75208c34014139d5d357": TokenInfo(
        currency=CurrencyInfo(symbol="TDH", name="TrustedHealth"), scaling=Decimal("1e-18")
    ),
    "0x2a22e5cca00a3d63308fa39f29202eb1b39eef52": TokenInfo(
        currency=CurrencyInfo(symbol="EDU", name="EDU Token"), scaling=Decimal("1e-18")
    ),
    "0x2a3bff78b79a009976eea096a51a948a3dc00e34": TokenInfo(
        currency=CurrencyInfo(symbol="WILD", name="Wilder World"), scaling=Decimal("1e-18")
    ),
    "0x2a4246c318b5ecdc3ead2d61ea0839bf88f7727b": TokenInfo(
        currency=CurrencyInfo(symbol="HLOB", name="High Low Bit Token"), scaling=Decimal("1e-8")
    ),
    "0x2a543f929e9d5afda0324889873afb513ff2811c": TokenInfo(
        currency=CurrencyInfo(symbol="FCHI.CX", name="France 40"), scaling=Decimal("1e-8")
    ),
    "0x2a6aac80905912ac1e769e28cda3807a4d20b3b6": TokenInfo(
        currency=CurrencyInfo(symbol="TPD", name="Tripedia"), scaling=Decimal("1e-18")
    ),
    "0x2a73cb91ed8983398f83082c093ac306cac209ff": TokenInfo(
        currency=CurrencyInfo(symbol="FIG", name="Fanboys Interactive"), scaling=Decimal("1e-18")
    ),
    "0x2a7f709ee001069771ceb6d42e85035f7d18e736": TokenInfo(
        currency=CurrencyInfo(symbol="OWL", name="OWL Token"), scaling=Decimal("1e-18")
    ),
    "0x2a8e1e676ec238d8a992307b495b45b3feaa5e86": TokenInfo(
        currency=CurrencyInfo(symbol="OUSD", name="Origin Dollar"), scaling=Decimal("1e-18")
    ),
    "0x2a8e98e256f32259b5e5cb55dd63c8e891950666": TokenInfo(
        currency=CurrencyInfo(symbol="PTC", name="ParrotCoin"), scaling=Decimal("1e-18")
    ),
    "0x2a9bdcff37ab68b95a53435adfd8892e86084f93": TokenInfo(
        currency=CurrencyInfo(symbol="AQT", name="Alpha Quark Token"), scaling=Decimal("1e-18")
    ),
    "0x2aad9dbc82611485a52325923e1187734e951b78": TokenInfo(
        currency=CurrencyInfo(symbol="BYTZ", name="BYTZ"), scaling=Decimal("1e-8")
    ),
    "0x2ab05b915c30093679165bcdba9c26d8cd8bee99": TokenInfo(
        currency=CurrencyInfo(symbol="BCHC", name="BitCherry"), scaling=Decimal("1e-18")
    ),
    "0x2ab6bb8408ca3199b8fa6c92d5b455f820af03c4": TokenInfo(
        currency=CurrencyInfo(symbol="TONE", name="TE FOOD"), scaling=Decimal("1e-18")
    ),
    "0x2ac22ebc138ff127566f68db600addad7df38d38": TokenInfo(
        currency=CurrencyInfo(symbol="SLC", name="Selenium"), scaling=Decimal("1e-18")
    ),
    "0x2ac8172d8ce1c5ad3d869556fd708801a42c1c0e": TokenInfo(
        currency=CurrencyInfo(symbol="VOY", name="enVoy Token"), scaling=Decimal("1e-18")
    ),
    "0x2accab9cb7a48c3e82286f0b2f8798d201f4ec3f": TokenInfo(
        currency=CurrencyInfo(symbol="BTL", name="Battle"), scaling=Decimal("1e-18")
    ),
    "0x2ad180cbaffbc97237f572148fc1b283b68d8861": TokenInfo(
        currency=CurrencyInfo(symbol="IZX", name="IZX"), scaling=Decimal("1e-18")
    ),
    "0x2adba23cf1252de095aced801e758b369ec10426": TokenInfo(
        currency=CurrencyInfo(symbol="UCBI", name="UCBI Banking"), scaling=Decimal("1e-8")
    ),
    "0x2aec18c5500f21359ce1bea5dc1777344df4c0dc": TokenInfo(
        currency=CurrencyInfo(symbol="FTT", name="FarmaTrust"), scaling=Decimal("1e-18")
    ),
    "0x2af1df3ab0ab157e1e2ad8f88a7d04fbea0c7dc6": TokenInfo(
        currency=CurrencyInfo(symbol="BED", name="Bankless BED Index"), scaling=Decimal("1e-18")
    ),
    "0x2af5d2ad76741191d15dfe7bf6ac92d4bd912ca3": TokenInfo(
        currency=CurrencyInfo(symbol="LEO", name="LEO Token"), scaling=Decimal("1e-18")
    ),
    "0x2af65d46fdecbba6f49209ff3ace031080da0bee": TokenInfo(
        currency=CurrencyInfo(symbol="CTLT.CX", name="Catalent Inc"), scaling=Decimal("1e-8")
    ),
    "0x2b0ef43e0111c8acaeaa26d93fa77048ef2a2cbf": TokenInfo(
        currency=CurrencyInfo(symbol="SPYCE", name="SPYCE"), scaling=Decimal("1e-18")
    ),
    "0x2b143041a6f8be9dcc66e9110178a264a223a3bd": TokenInfo(
        currency=CurrencyInfo(symbol="iBTC", name="Synth iBTC"), scaling=Decimal("1e-18")
    ),
    "0x2b2b0559081c41e962777b5049632fdb30f7e652": TokenInfo(
        currency=CurrencyInfo(symbol="BFI", name="BitDefi"), scaling=Decimal("1e-8")
    ),
    "0x2b4200a8d373d484993c37d63ee14aee0096cd12": TokenInfo(
        currency=CurrencyInfo(symbol="USDFL", name="USDFreeLiquidity"), scaling=Decimal("1e-18")
    ),
    "0x2b591e99afe9f32eaa6214f7b7629768c40eeb39": TokenInfo(
        currency=CurrencyInfo(symbol="HEX", name="HEX"), scaling=Decimal("1e-8")
    ),
    "0x2b67d1a87a8d8b280a23e97bc55095215ee0ec53": TokenInfo(
        currency=CurrencyInfo(symbol="CPI", name="Crypto Price Index"), scaling=Decimal("1e-18")
    ),
    "0x2b6ff53fc2493ccd5202d80a6c439741414c5ff2": TokenInfo(
        currency=CurrencyInfo(symbol="TWEE", name="TWEEBAA"), scaling=Decimal("1e-18")
    ),
    "0x2b78c26973545f9fd7ebdb01922966628382e6ba": TokenInfo(
        currency=CurrencyInfo(symbol="YEFAM", name="yefam.finance"), scaling=Decimal("1e-18")
    ),
    "0x2b7922fdf76fb3466902c7b702a20ea6a450a0a0": TokenInfo(
        currency=CurrencyInfo(symbol="FTCOIN", name="Fund Token Coin"), scaling=Decimal("1e-18")
    ),
    "0x2b85cea4e0ee23468b54e0bfe8284f4c308cfe37": TokenInfo(
        currency=CurrencyInfo(symbol="CCS", name="Crypto Copyright System"), scaling=Decimal("1e-18")
    ),
    "0x2b959ef258370c7a554d2bb052b3bc062d17e758": TokenInfo(
        currency=CurrencyInfo(symbol="OW", name="OW Pay"), scaling=Decimal("1e-18")
    ),
    "0x2ba592f78db6436527729929aaf6c908497cb200": TokenInfo(
        currency=CurrencyInfo(symbol="CREAM", name="Cream"), scaling=Decimal("1e-18")
    ),
    "0x2ba6b1e4424e19816382d15937739959f7da5fd8": TokenInfo(
        currency=CurrencyInfo(symbol="MEX", name="MEX"), scaling=Decimal("1e-18")
    ),
    "0x2ba8349123de45e931a8c8264c332e6e9cf593f9": TokenInfo(
        currency=CurrencyInfo(symbol="BCMC", name="Blockchain Monster "), scaling=Decimal("1e-18")
    ),
    "0x2baac9330cf9ac479d819195794d79ad0c7616e3": TokenInfo(
        currency=CurrencyInfo(symbol="ADB", name="adbank"), scaling=Decimal("1e-18")
    ),
    "0x2baecdf43734f22fd5c152db08e3c27233f0c7d2": TokenInfo(
        currency=CurrencyInfo(symbol="OM", name="OM Token"), scaling=Decimal("1e-18")
    ),
    "0x2bba3cf6de6058cc1b4457ce00deb359e2703d7f": TokenInfo(
        currency=CurrencyInfo(symbol="HSC", name="HashCoin"), scaling=Decimal("1e-18")
    ),
    "0x2bc8b955f6a0ed5a9d4146ded61aec0bb74ecf67": TokenInfo(
        currency=CurrencyInfo(symbol="LGC", name="Logistics Coin"), scaling=Decimal("1e-18")
    ),
    "0x2bdbf15d055899a767f5459a151bed15fb8fd2f6": TokenInfo(
        currency=CurrencyInfo(symbol="UST", name="Ultra Salescloud"), scaling=Decimal("1e-18")
    ),
    "0x2bdc0d42996017fce214b21607a515da41a9e0c5": TokenInfo(
        currency=CurrencyInfo(symbol="SKIN", name="SkinCoin"), scaling=Decimal("1e-6")
    ),
    "0x2bdd6c9bf1bf396a37501aae53751b9946b503da": TokenInfo(
        currency=CurrencyInfo(symbol="KMTBA", name="Korea Medical TBA"), scaling=Decimal("1e-18")
    ),
    "0x2be5e8c109e2197d077d13a82daead6a9b3433c5": TokenInfo(
        currency=CurrencyInfo(symbol="TON", name="Tokamak Network"), scaling=Decimal("1e-18")
    ),
    "0x2bf417fda6e73b8ea605df0f33ad029f8d4b795a": TokenInfo(
        currency=CurrencyInfo(symbol="ETHMOONX2", name="ETH Moonshot X Discretionary Yield Set"),
        scaling=Decimal("1e-18"),
    ),
    "0x2bf91c18cd4ae9c2f2858ef9fe518180f7b5096d": TokenInfo(
        currency=CurrencyInfo(symbol="KIWI", name="KIWI Token"), scaling=Decimal("1e-8")
    ),
    "0x2c2f7e7c5604d162d75641256b80f1bf6f4dc796": TokenInfo(
        currency=CurrencyInfo(symbol="PRARE", name="Polkarare"), scaling=Decimal("1e-18")
    ),
    "0x2c31b10ca416b82cec4c5e93c615ca851213d48d": TokenInfo(
        currency=CurrencyInfo(symbol="FORCE", name="Force DAO"), scaling=Decimal("1e-18")
    ),
    "0x2c31c747e0d1eb1f662b619461dced4ce5ca22ea": TokenInfo(
        currency=CurrencyInfo(symbol="FSCP", name="Five Star Coin Pro"), scaling=Decimal("1e-8")
    ),
    "0x2c36204a0712a2a50e54a62f7c4f01867e78cb53": TokenInfo(
        currency=CurrencyInfo(symbol="TAN", name="Taklimakan Network"), scaling=Decimal("1e-18")
    ),
    "0x2c3c1f05187dba7a5f2dd47dca57281c4d4f183f": TokenInfo(
        currency=CurrencyInfo(symbol="QTQ", name="Q"), scaling=Decimal("1e-18")
    ),
    "0x2c4e8f2d746113d0696ce89b35f0d8bf88e0aeca": TokenInfo(
        currency=CurrencyInfo(symbol="OST", name="OST"), scaling=Decimal("1e-18")
    ),
    "0x2c50ba1ed5e4574c1b613b044bd1876f0b0b87a9": TokenInfo(
        currency=CurrencyInfo(symbol="KASH", name="Kids Cash"), scaling=Decimal("1e-18")
    ),
    "0x2c537e5624e4af88a7ae4060c022609376c8d0eb": TokenInfo(
        currency=CurrencyInfo(symbol="TRYB", name="BiLira"), scaling=Decimal("1e-6")
    ),
    "0x2c594e1cb006e86c3879b1d8191a8b059af52be7": TokenInfo(
        currency=CurrencyInfo(symbol="EXC", name="Excaliburcoin"), scaling=Decimal("1e-8")
    ),
    "0x2c5a9980b41861d91d30d0e0271d1c093452dca5": TokenInfo(
        currency=CurrencyInfo(symbol="ETH12EMACO", name="ETH 12 Day EMA Crossover Set"), scaling=Decimal("1e-18")
    ),
    "0x2c7f4cca29a4627a7a8e20440abf107acc3e42eb": TokenInfo(
        currency=CurrencyInfo(symbol="TON", name="TomaInfo"), scaling=Decimal("1e-2")
    ),
    "0x2c82c73d5b34aa015989462b2948cd616a37641f": TokenInfo(
        currency=CurrencyInfo(symbol="SXUT", name="Spectre.ai Utility Token"), scaling=Decimal("1e-18")
    ),
    "0x2c9023bbc572ff8dc1228c7858a280046ea8c9e5": TokenInfo(
        currency=CurrencyInfo(symbol="VID", name="VideoCoin"), scaling=Decimal("1e-18")
    ),
    "0x2c949199cff14aeaf1b33d64db01f48fb57f592f": TokenInfo(
        currency=CurrencyInfo(symbol="CONI", name="CoinBene Coin"), scaling=Decimal("1e-8")
    ),
    "0x2c974b2d0ba1716e644c1fc59982a89ddd2ff724": TokenInfo(
        currency=CurrencyInfo(symbol="VIB", name="Viberate"), scaling=Decimal("1e-18")
    ),
    "0x2ca76b74c148ce6c4f51f47278ef089030e03178": TokenInfo(
        currency=CurrencyInfo(symbol="LOC", name="loopycoin"), scaling=Decimal("1e-6")
    ),
    "0x2cad4991f62fc6fcd8ec219f37e7de52b688b75a": TokenInfo(
        currency=CurrencyInfo(symbol="SCHA", name="Schain Wallet"), scaling=Decimal("1e-0")
    ),
    "0x2cae31d2ca104a951654456f46168bc9f88fdc65": TokenInfo(
        currency=CurrencyInfo(symbol="JUI", name="JUIICE"), scaling=Decimal("1e-18")
    ),
    "0x2cb101d7da0ebaa57d3f2fef46d7ffb7bb64592b": TokenInfo(
        currency=CurrencyInfo(symbol="CDX", name="Carbon Dollar X"), scaling=Decimal("1e-0")
    ),
    "0x2cc114bbe7b551d62b15c465c7bdcccd9125b182": TokenInfo(
        currency=CurrencyInfo(symbol="IDOL", name="IDOLCOIN"), scaling=Decimal("1e-8")
    ),
    "0x2cc71c048a804da930e28e93f3211dc03c702995": TokenInfo(
        currency=CurrencyInfo(symbol="LPK", name="Kripton"), scaling=Decimal("1e-8")
    ),
    "0x2ccbff3a042c68716ed2a2cb0c544a9f1d1935e1": TokenInfo(
        currency=CurrencyInfo(symbol="DMT", name="DMarket"), scaling=Decimal("1e-8")
    ),
    "0x2cf2f4e07ecc54740293df6d6fb4150d725a919f": TokenInfo(
        currency=CurrencyInfo(symbol="WST", name="Winsor Token"), scaling=Decimal("1e-18")
    ),
    "0x2cf618c19041d9db330d8222b860a624021f30fb": TokenInfo(
        currency=CurrencyInfo(symbol="CRBT", name="CRUISEBIT"), scaling=Decimal("1e-18")
    ),
    "0x2cfd4c10c075fa51649744245ec1d0aa3d567e23": TokenInfo(
        currency=CurrencyInfo(symbol="IPY", name="Infinity Pay"), scaling=Decimal("1e-8")
    ),
    "0x2d0e95bd4795d7ace0da3c0ff7b706a5970eb9d3": TokenInfo(
        currency=CurrencyInfo(symbol="SOC", name="All Sports"), scaling=Decimal("1e-18")
    ),
    "0x2d184014b5658c453443aa87c8e9c4d57285620b": TokenInfo(
        currency=CurrencyInfo(symbol="JSE", name="JSECOIN"), scaling=Decimal("1e-18")
    ),
    "0x2d2501dcc897ad69a12090ca6b59ab33018eab97": TokenInfo(
        currency=CurrencyInfo(symbol="XTEM", name="Tweet Empire"), scaling=Decimal("1e-18")
    ),
    "0x2d39ec4da54329d28d230b4973f5aa27886c3aee": TokenInfo(
        currency=CurrencyInfo(symbol="NFXC", name="NFX Coin"), scaling=Decimal("1e-18")
    ),
    "0x2d3e7d4870a51b918919e7b851fe19983e4c38d5": TokenInfo(
        currency=CurrencyInfo(symbol="UBC", name="Ubcoin Market"), scaling=Decimal("1e-18")
    ),
    "0x2d4de3c744d43cf77cb12399921faf0d78b7415b": TokenInfo(
        currency=CurrencyInfo(symbol="BOLD", name="Boldman Capital"), scaling=Decimal("1e-18")
    ),
    "0x2d5bed63b0fe325ed3b865ae2cdaa3649eb25461": TokenInfo(
        currency=CurrencyInfo(symbol="TESLF", name="Teslafan"), scaling=Decimal("1e-18")
    ),
    "0x2d71983e810b9e95258966b9c164c4d61a829ba9": TokenInfo(
        currency=CurrencyInfo(symbol="ICT", name="ICOCalendar.Today"), scaling=Decimal("1e-6")
    ),
    "0x2d77f5b3efa51821ad6483adaf38ea4cb1824cc5": TokenInfo(
        currency=CurrencyInfo(symbol="MANA", name="Genesis Mana"), scaling=Decimal("1e-18")
    ),
    "0x2d7ac061fc3db53c39fe1607fb8cec1b2c162b01": TokenInfo(
        currency=CurrencyInfo(symbol="ILINK", name="iLINK"), scaling=Decimal("1e-18")
    ),
    "0x2d80f5f5328fdcb6eceb7cacf5dd8aedaec94e20": TokenInfo(
        currency=CurrencyInfo(symbol="AGA", name="AGA Token"), scaling=Decimal("1e-4")
    ),
    "0x2d8e1dd483008c6843b9cf644bad7fb25bf52b84": TokenInfo(
        currency=CurrencyInfo(symbol="DCB", name="Digital Coin"), scaling=Decimal("1e-18")
    ),
    "0x2d94aa3e47d9d5024503ca8491fce9a2fb4da198": TokenInfo(
        currency=CurrencyInfo(symbol="BANK", name="Bankless DAO"), scaling=Decimal("1e-18")
    ),
    "0x2d9765a94ff22e0ca3afc3e3f4b116de2b67582a": TokenInfo(
        currency=CurrencyInfo(symbol="CGC", name="CGC Token"), scaling=Decimal("1e-16")
    ),
    "0x2daee1aa61d60a252dc80564499a69802853583a": TokenInfo(
        currency=CurrencyInfo(symbol="ATS", name="Authorship"), scaling=Decimal("1e-4")
    ),
    "0x2dbd330bc9b7f3a822a9173ab52172bdddcace2a": TokenInfo(
        currency=CurrencyInfo(symbol="YFED", name="YFED.Finance"), scaling=Decimal("1e-8")
    ),
    "0x2dca19e944453e46d9130950ca135461b3bc0c30": TokenInfo(
        currency=CurrencyInfo(symbol="EYES", name="EYES Protocol"), scaling=Decimal("1e-18")
    ),
    "0x2dcfaac11c9eebd8c6c42103fe9e2a6ad237af27": TokenInfo(
        currency=CurrencyInfo(symbol="SMT", name="Smart Node"), scaling=Decimal("1e-18")
    ),
    "0x2dd0e4a0dba20e1c823d65fe7b2b93bff8fa6d42": TokenInfo(
        currency=CurrencyInfo(symbol="SNAP.CX", name="Snap"), scaling=Decimal("1e-8")
    ),
    "0x2df43e6826cf24bb844cc78611b0036eea3671b4": TokenInfo(
        currency=CurrencyInfo(symbol="SCT", name="SCT Token"), scaling=Decimal("1e-8")
    ),
    "0x2dff4c3a62cd46b692d654ef733f06e4ef704d6d": TokenInfo(
        currency=CurrencyInfo(symbol="MNJ", name="Minanjo Token"), scaling=Decimal("1e-18")
    ),
    "0x2e071d2966aa7d8decb1005885ba1977d6038a65": TokenInfo(
        currency=CurrencyInfo(symbol="DICE", name="Etheroll"), scaling=Decimal("1e-16")
    ),
    "0x2e0c40beb655a988e087ad71ca191a2806ac55ef": TokenInfo(
        currency=CurrencyInfo(symbol="CARM", name="Carnomic"), scaling=Decimal("1e-18")
    ),
    "0x2e185ef6684d2d0fe9d311782e0ef738d63861e0": TokenInfo(
        currency=CurrencyInfo(symbol="BCHDOOM", name="10X Short Bitcoin Cash Token"), scaling=Decimal("1e-18")
    ),
    "0x2e1e15c44ffe4df6a0cb7371cd00d5028e571d14": TokenInfo(
        currency=CurrencyInfo(symbol="MTLX", name="Mettalex"), scaling=Decimal("1e-18")
    ),
    "0x2e2e0a28f6585e895dd646a363bae29b77b88a31": TokenInfo(
        currency=CurrencyInfo(symbol="VOL", name="Volume Network"), scaling=Decimal("1e-18")
    ),
    "0x2e2f3246b6c65ccc4239c9ee556ec143a7e5de2c": TokenInfo(
        currency=CurrencyInfo(symbol="YFIM", name="Yfi.mobi"), scaling=Decimal("1e-18")
    ),
    "0x2e3c062e16c1a3a04ddc5003c62e294305d83684": TokenInfo(
        currency=CurrencyInfo(symbol="LIT", name="LITonium"), scaling=Decimal("1e-2")
    ),
    "0x2e42e8da119315881748b140e69a0343dacab4ea": TokenInfo(
        currency=CurrencyInfo(symbol="M.CX", name="Macys"), scaling=Decimal("1e-8")
    ),
    "0x2e59005c5c0f0a4d77cca82653d48b46322ee5cd": TokenInfo(
        currency=CurrencyInfo(symbol="sXTZ", name="Synth sXTZ"), scaling=Decimal("1e-18")
    ),
    "0x2e6539edc3b76f1e21b71d214527faba875f70f3": TokenInfo(
        currency=CurrencyInfo(symbol="YFDOT", name="Yearn Finance DOT"), scaling=Decimal("1e-18")
    ),
    "0x2e65e12b5f0fd1d58738c6f38da7d57f5f183d1c": TokenInfo(
        currency=CurrencyInfo(symbol="TEP", name="Tepleton"), scaling=Decimal("1e-8")
    ),
    "0x2e68dfb3f50ea302c88f8db74096d57565d9970a": TokenInfo(
        currency=CurrencyInfo(symbol="AMIO", name="Amino Network"), scaling=Decimal("1e-18")
    ),
    "0x2e6c1c08ef1173d2be02165f91cc8e604ec5a1c3": TokenInfo(
        currency=CurrencyInfo(symbol="CRT", name="CRTCoin"), scaling=Decimal("1e-18")
    ),
    "0x2e6e152d29053b6337e434bc9be17504170f8a5b": TokenInfo(
        currency=CurrencyInfo(symbol="YFIEC", name="Yearn Finance Ecosystem"), scaling=Decimal("1e-8")
    ),
    "0x2e7b0d4f9b2eaf782ed3d160e3a0a4b1a7930ada": TokenInfo(
        currency=CurrencyInfo(symbol="CERES", name="Ceres"), scaling=Decimal("1e-18")
    ),
    "0x2e85ae1c47602f7927bcabc2ff99c40aa222ae15": TokenInfo(
        currency=CurrencyInfo(symbol="KATA", name="Katana Inu"), scaling=Decimal("1e-18")
    ),
    "0x2e8c6bbe8e3aa834ef5a851b2cdfc52403d61b87": TokenInfo(
        currency=CurrencyInfo(symbol="STM", name="Streamity"), scaling=Decimal("1e-18")
    ),
    "0x2e93fe8d550a7b7e7b2e561cd45cebccbaa79358": TokenInfo(
        currency=CurrencyInfo(symbol="GXC", name="GXChain Core Asset"), scaling=Decimal("1e-5")
    ),
    "0x2e95cea14dd384429eb3c4331b776c4cfbb6fcd9": TokenInfo(
        currency=CurrencyInfo(symbol="THN", name="Throne"), scaling=Decimal("1e-18")
    ),
    "0x2e98a6804e4b6c832ed0ca876a943abd3400b224": TokenInfo(
        currency=CurrencyInfo(symbol="BELA", name="Belacoin"), scaling=Decimal("1e-18")
    ),
    "0x2e9d63788249371f1dfc918a52f8d799f4a38c94": TokenInfo(
        currency=CurrencyInfo(symbol="TOKE", name="Tokemak"), scaling=Decimal("1e-18")
    ),
    "0x2e9ef342f50a10e87ddad06d0fc6d3f0223726c9": TokenInfo(
        currency=CurrencyInfo(symbol="GMC", name="Geimcoin"), scaling=Decimal("1e-18")
    ),
    "0x2eb86e8fc520e0f6bb5d9af08f924fe70558ab89": TokenInfo(
        currency=CurrencyInfo(symbol="LGR", name="Logarithm"), scaling=Decimal("1e-8")
    ),
    "0x2ecb13a8c458c379c4d9a7259e202de03c8f3d19": TokenInfo(
        currency=CurrencyInfo(symbol="BC", name="Block-chain.com"), scaling=Decimal("1e-18")
    ),
    "0x2edf094db69d6dcd487f1b3db9febe2eec0dd4c5": TokenInfo(
        currency=CurrencyInfo(symbol="ZEE", name="ZeroSwap"), scaling=Decimal("1e-18")
    ),
    "0x2ef1ab8a26187c58bb8aaeb11b2fc6d25c5c0716": TokenInfo(
        currency=CurrencyInfo(symbol="TWN", name="TWN Shares"), scaling=Decimal("1e-18")
    ),
    "0x2ef52ed7de8c5ce03a4ef0efbe9b7450f2d7edc9": TokenInfo(
        currency=CurrencyInfo(symbol="REV", name="Revain"), scaling=Decimal("1e-6")
    ),
    "0x2f01d47c239b7eaccd746604fdba49a84367d2da": TokenInfo(
        currency=CurrencyInfo(symbol="FIC", name="FinCredit Protocol"), scaling=Decimal("1e-8")
    ),
    "0x2f102963f61acf1ca4badfe82057b440f2fc722c": TokenInfo(
        currency=CurrencyInfo(symbol="EAI", name="EthereumAI"), scaling=Decimal("1e-6")
    ),
    "0x2f109021afe75b949429fe30523ee7c0d5b27207": TokenInfo(
        currency=CurrencyInfo(symbol="OCC", name="OccamFi"), scaling=Decimal("1e-18")
    ),
    "0x2f141ce366a2462f02cea3d12cf93e4dca49e4fd": TokenInfo(
        currency=CurrencyInfo(symbol="FREE", name="FREE coin"), scaling=Decimal("1e-18")
    ),
    "0x2f25d402829ca4085b8ea4d3bc68bf203f5a9fab": TokenInfo(
        currency=CurrencyInfo(symbol="EAGON", name="EagonSwap Token"), scaling=Decimal("1e-18")
    ),
    "0x2f34dd3d46855277eee79a1d724c2249f770054b": TokenInfo(
        currency=CurrencyInfo(symbol="GOI", name="GoForIt Walk&Win"), scaling=Decimal("1e-18")
    ),
    "0x2f4efc52b8aa56f18df95b1472c664d3762cd4b6": TokenInfo(
        currency=CurrencyInfo(symbol="CTO", name="Cherry Cube"), scaling=Decimal("1e-18")
    ),
    "0x2f5cdc81a729b750f3b733cb95660e788441c71e": TokenInfo(
        currency=CurrencyInfo(symbol="XLDZ", name="LD2.Zero"), scaling=Decimal("1e-18")
    ),
    "0x2f6d747528654e489cb0282a51dc08fd3a7b2a85": TokenInfo(
        currency=CurrencyInfo(symbol="RDT", name="Rush Digital Tether"), scaling=Decimal("1e-18")
    ),
    "0x2f75113b13d136f861d212fa9b572f2c79ac81c4": TokenInfo(
        currency=CurrencyInfo(symbol="EKTA", name="Ekta"), scaling=Decimal("1e-18")
    ),
    "0x2f7b88458f4e6d9abb19396b5a08b8ba7f3d4b20": TokenInfo(
        currency=CurrencyInfo(symbol="WAE", name="Wave Platform"), scaling=Decimal("1e-6")
    ),
    "0x2f8472dd7ecf7ca760c8f6b45db20ca7cf52f8d7": TokenInfo(
        currency=CurrencyInfo(symbol="BSTN", name="BitStation"), scaling=Decimal("1e-18")
    ),
    "0x2f85e502a988af76f7ee6d83b7db8d6c0a823bf9": TokenInfo(
        currency=CurrencyInfo(symbol="LATX", name="LatiumX"), scaling=Decimal("1e-8")
    ),
    "0x2f90599ab7d47a7eeb25017b5429d7305794257b": TokenInfo(
        currency=CurrencyInfo(symbol="KTETH", name="Kino Token ETH"), scaling=Decimal("1e-8")
    ),
    "0x2f9b6779c37df5707249eeb3734bbfc94763fbe2": TokenInfo(
        currency=CurrencyInfo(symbol="WIZ", name="CrowdWiz"), scaling=Decimal("1e-18")
    ),
    "0x2fa32a39fc1c399e0cc7b2935868f5165de7ce97": TokenInfo(
        currency=CurrencyInfo(symbol="PFR", name="PayFair Token"), scaling=Decimal("1e-8")
    ),
    "0x2fb12bccf6f5dd338b76be784a93ade072425690": TokenInfo(
        currency=CurrencyInfo(symbol="BEAT", name="BEAT"), scaling=Decimal("1e-18")
    ),
    "0x2fb3d7f7dd7027f7e7ef32fe09e4c94ca3cc6e9c": TokenInfo(
        currency=CurrencyInfo(symbol="DGC", name="Dogecoin Gold Classic"), scaling=Decimal("1e-0")
    ),
    "0x2fd61567c29e7adb4ca17e60e1f4a3fcfe68acb8": TokenInfo(
        currency=CurrencyInfo(symbol="SYM", name="SymVerse"), scaling=Decimal("1e-18")
    ),
    "0x2ff0a6868e80e0177295a3ebfca75f9bae074499": TokenInfo(
        currency=CurrencyInfo(symbol="RC", name="Racecoin"), scaling=Decimal("1e-18")
    ),
    "0x3008186fe6e3bca6d1362105a48ec618672ce5b3": TokenInfo(
        currency=CurrencyInfo(symbol="HTHEDGE", name="1X Short Huobi Token Token"), scaling=Decimal("1e-18")
    ),
    "0x301c755ba0fca00b1923768fffb3df7f4e63af31": TokenInfo(
        currency=CurrencyInfo(symbol="GDC", name="Global Digital Content"), scaling=Decimal("1e-18")
    ),
    "0x302ce6674a16b54ba1b8a49fed64c471ede6c174": TokenInfo(
        currency=CurrencyInfo(symbol="STM", name="StmToken"), scaling=Decimal("1e-0")
    ),
    "0x303d396bb1e2a73b1536665964aa9f5aa0f7f9ca": TokenInfo(
        currency=CurrencyInfo(symbol="NUMA", name="Numisma Coin"), scaling=Decimal("1e-0")
    ),
    "0x304281f3d1023a2039ea930c65f8f721d7c746c8": TokenInfo(
        currency=CurrencyInfo(symbol="AXN", name="AXNET Token"), scaling=Decimal("1e-18")
    ),
    "0x304e9847104b14628a56cfb3366cf9e94718b036": TokenInfo(
        currency=CurrencyInfo(symbol="PSC", name="PSC Token"), scaling=Decimal("1e-18")
    ),
    "0x305f8157c1f841fbd378f636abf390c5b4c0e330": TokenInfo(
        currency=CurrencyInfo(symbol="BTCGW", name="Bitcoin Galaxy Warp"), scaling=Decimal("1e-8")
    ),
    "0x30647a72dc82d7fbb1123ea74716ab8a317eac19": TokenInfo(
        currency=CurrencyInfo(symbol="imUSD", name="mStable Interest Bearing mUSD"), scaling=Decimal("1e-18")
    ),
    "0x30680ac0a8a993088223925265fd7a76beb87e7f": TokenInfo(
        currency=CurrencyInfo(symbol="ARAW", name="ARAW Token"), scaling=Decimal("1e-18")
    ),
    "0x3071a55a0f7916d796b54a2d095db85df693d956": TokenInfo(
        currency=CurrencyInfo(symbol="EUM", name="Walleteum"), scaling=Decimal("1e-13")
    ),
    "0x307d45afbb7e84f82ef3d251a6bb0f00edf632e4": TokenInfo(
        currency=CurrencyInfo(symbol="PLA", name="PLANET"), scaling=Decimal("1e-18")
    ),
    "0x3080ec2a6960432f179c66d388099a48e82e2047": TokenInfo(
        currency=CurrencyInfo(symbol="CORN", name="Popcorn Token"), scaling=Decimal("1e-18")
    ),
    "0x308564dc5217c39386f5eae96545159e1d396661": TokenInfo(
        currency=CurrencyInfo(symbol="HLP", name="HLP Token"), scaling=Decimal("1e-18")
    ),
    "0x309013d55fb0e8c17363bcc79f25d92f711a5802": TokenInfo(
        currency=CurrencyInfo(symbol="SBTC", name="Soft Bitcoin"), scaling=Decimal("1e-9")
    ),
    "0x309627af60f0926daa6041b8279484312f2bf060": TokenInfo(
        currency=CurrencyInfo(symbol="USDB", name="USD Bancor"), scaling=Decimal("1e-18")
    ),
    "0x30cecb5461a449a90081f5a5f55db4e048397bab": TokenInfo(
        currency=CurrencyInfo(symbol="TRCT", name="Tracto"), scaling=Decimal("1e-8")
    ),
    "0x30dfd1e3ba2919d1337512a9f3cf83050fa7b84b": TokenInfo(
        currency=CurrencyInfo(symbol="UXET", name="Unity ETH token"), scaling=Decimal("1e-0")
    ),
    "0x30e00b4af68acd6b779f9c0ac82fa07f05ba94d0": TokenInfo(
        currency=CurrencyInfo(symbol="BTCD", name="Bitcoin Diamond Token"), scaling=Decimal("1e-4")
    ),
    "0x30e193bd3f52713d5562cf316f35115034525f44": TokenInfo(
        currency=CurrencyInfo(symbol="GTEC", name="Green Tech Coin "), scaling=Decimal("1e-18")
    ),
    "0x30e5ced3aa9148036116baf816fec8363691a5e8": TokenInfo(
        currency=CurrencyInfo(symbol="ACAR", name="AlphaCar"), scaling=Decimal("1e-18")
    ),
    "0x30ecfa6f6d1cf830a76d8652dda9cc5a4b1a99e2": TokenInfo(
        currency=CurrencyInfo(symbol="WBA.CX", name="Walgreen Boots Alliance"), scaling=Decimal("1e-8")
    ),
    "0x30f271c9e86d2b7d00a6376cd96a1cfbd5f0b9b3": TokenInfo(
        currency=CurrencyInfo(symbol="DEC", name="Decentr"), scaling=Decimal("1e-18")
    ),
    "0x30f4a3e0ab7a76733d8b60b89dd93c3d0b4c9e2f": TokenInfo(
        currency=CurrencyInfo(symbol="XGT", name="CryptogeneToken"), scaling=Decimal("1e-18")
    ),
    "0x30fef258d2728f9d1edf038059c725faf785697e": TokenInfo(
        currency=CurrencyInfo(symbol="PESO", name="PESOTOKEN"), scaling=Decimal("1e-2")
    ),
    "0x31024a4c3e9aeeb256b825790f5cb7ac645e7cd5": TokenInfo(
        currency=CurrencyInfo(symbol="XIOT", name="Xiotri"), scaling=Decimal("1e-3")
    ),
    "0x310c93dfc1c5e34cdf51678103f63c41762089cd": TokenInfo(
        currency=CurrencyInfo(symbol="FST", name="1irstcoin"), scaling=Decimal("1e-6")
    ),
    "0x31141dc226c214d40b1f77feb532741d8f893c6f": TokenInfo(
        currency=CurrencyInfo(symbol="PNC", name="Parallel network"), scaling=Decimal("1e-18")
    ),
    "0x31274db8b609df99e5988ee527071643b5160fc3": TokenInfo(
        currency=CurrencyInfo(symbol="BCS", name="Business Credit Substitute"), scaling=Decimal("1e-18")
    ),
    "0x3136ef851592acf49ca4c825131e364170fa32b3": TokenInfo(
        currency=CurrencyInfo(symbol="COFI", name="CoinFi"), scaling=Decimal("1e-18")
    ),
    "0x3137619705b5fc22a3048989f983905e456b59ab": TokenInfo(
        currency=CurrencyInfo(symbol="EVR", name="Everus"), scaling=Decimal("1e-8")
    ),
    "0x31429d1856ad1377a8a0079410b297e1a9e214c2": TokenInfo(
        currency=CurrencyInfo(symbol="ANGLE", name="ANGLE"), scaling=Decimal("1e-18")
    ),
    "0x3142dad33b1c6e1371d8627365f2ee2095eb6b37": TokenInfo(
        currency=CurrencyInfo(symbol="HAUT", name="Hauteclere Shards"), scaling=Decimal("1e-18")
    ),
    "0x314bd765cab4774b2e547eb0aa15013e03ff74d2": TokenInfo(
        currency=CurrencyInfo(symbol="PARTY", name="MONEY PARTY"), scaling=Decimal("1e-6")
    ),
    "0x314dc48e17e904afd13927cb2a5cb7dc46d88a1a": TokenInfo(
        currency=CurrencyInfo(symbol="WGC", name="WeGen Platform"), scaling=Decimal("1e-18")
    ),
    "0x3154da898943fc7151bc77f16e43c0c47b5e452d": TokenInfo(
        currency=CurrencyInfo(symbol="STB", name="STB Chain"), scaling=Decimal("1e-18")
    ),
    "0x3155ba85d5f96b2d030a4966af206230e46849cb": TokenInfo(
        currency=CurrencyInfo(symbol="RUNE", name="THORChain (ERC20)"), scaling=Decimal("1e-18")
    ),
    "0x315ce59fafd3a8d562b7ec1c8542382d2710b06c": TokenInfo(
        currency=CurrencyInfo(symbol="CCS", name="Cacao Shares"), scaling=Decimal("1e-18")
    ),
    "0x3166c570935a7d8554c8f4ea792ff965d2efe1f2": TokenInfo(
        currency=CurrencyInfo(symbol="QDAO", name="Q DAO Governance token v1.0"), scaling=Decimal("1e-18")
    ),
    "0x316b13b951efe25aad1cb565385b23869a7d4c48": TokenInfo(
        currency=CurrencyInfo(symbol="ETHEMAAPY", name="ETH 26 EMA Crossover Yield Set"), scaling=Decimal("1e-18")
    ),
    "0x316e7d7f3d9584b276fb68028b74fcdbaec56481": TokenInfo(
        currency=CurrencyInfo(symbol="BSHORT", name="Bitcoin Short"), scaling=Decimal("1e-18")
    ),
    "0x31735f0292d42801dce3b0f83b0d9a09bff75b07": TokenInfo(
        currency=CurrencyInfo(symbol="WEFI", name="Wolfage Finance Governance Token"), scaling=Decimal("1e-18")
    ),
    "0x317dc3f08f7947f363dfc7cb008048a5a5ea1840": TokenInfo(
        currency=CurrencyInfo(symbol="VRES", name="Virtual Reality Electronic Sports"), scaling=Decimal("1e-18")
    ),
    "0x318d4410d824dbfdcac8c49d21e1edaf4e4931dc": TokenInfo(
        currency=CurrencyInfo(symbol="BHOT", name="BUYING HOUSES OVERSEAS"), scaling=Decimal("1e-8")
    ),
    "0x31910aff5545784755970ae1fbe7fe65d5f0eea2": TokenInfo(
        currency=CurrencyInfo(symbol="CPAL", name="CreatorPAL"), scaling=Decimal("1e-8")
    ),
    "0x319ad3ff82bedddb3bc85fd7943002d25cdb3cb9": TokenInfo(
        currency=CurrencyInfo(symbol="CNYX", name="eToro Chinese Yuan"), scaling=Decimal("1e-18")
    ),
    "0x31a217b8065b376b192388b877d26e682044b82b": TokenInfo(
        currency=CurrencyInfo(symbol="EPS", name="Epsilon"), scaling=Decimal("1e-8")
    ),
    "0x31b595e7cfdb624d10a3e7a562ed98c3567e3865": TokenInfo(
        currency=CurrencyInfo(symbol="stZEN", name="stakedZEN"), scaling=Decimal("1e-8")
    ),
    "0x31c63146a635eb7465e5853020b39713ac356991": TokenInfo(
        currency=CurrencyInfo(symbol="MUSO", name="Mirrored United States Oil Fund"), scaling=Decimal("1e-18")
    ),
    "0x31c8eacbffdd875c74b94b077895bd78cf1e64a3": TokenInfo(
        currency=CurrencyInfo(symbol="RAD", name="Radicle"), scaling=Decimal("1e-18")
    ),
    "0x31cbf205e26ba63296fdbd254a6b1be3ed28ce47": TokenInfo(
        currency=CurrencyInfo(symbol="XAUTBEAR", name="3X Short Tether Gold Token"), scaling=Decimal("1e-18")
    ),
    "0x31d457e7bcff5bc9a5ef86e6a5ea1db5b5c3bfb0": TokenInfo(
        currency=CurrencyInfo(symbol="FOXX", name="FOXX"), scaling=Decimal("1e-18")
    ),
    "0x31ddd688d6cda430aad84142b2cd8c019d88094d": TokenInfo(
        currency=CurrencyInfo(symbol="PBC", name="Pray Bless Coin"), scaling=Decimal("1e-18")
    ),
    "0x31e15a071a5340f0393ea98dde3a095d64206a02": TokenInfo(
        currency=CurrencyInfo(symbol="LTCDOOM", name="10X Short Litecoin Token"), scaling=Decimal("1e-18")
    ),
    "0x31ed1bc96fa75ee33d513a0cef4b65c2500b320b": TokenInfo(
        currency=CurrencyInfo(symbol="OEC", name="Our Earth Coin"), scaling=Decimal("1e-18")
    ),
    "0x31f3d9d1bece0c033ff78fa6da60a6048f3e13c5": TokenInfo(
        currency=CurrencyInfo(symbol="EBC", name="EBCoin"), scaling=Decimal("1e-18")
    ),
    "0x31f69de127c8a0ff10819c0955490a4ae46fcc2a": TokenInfo(
        currency=CurrencyInfo(symbol="GBYTE", name="Obyte"), scaling=Decimal("1e-18")
    ),
    "0x31fd1a50c467ae7986e26c72e8650a28940e11de": TokenInfo(
        currency=CurrencyInfo(symbol="BTR", name="BitRice"), scaling=Decimal("1e-18")
    ),
    "0x31fdd1c6607f47c14a2821f599211c67ac20fa96": TokenInfo(
        currency=CurrencyInfo(symbol="BUY", name="Burency"), scaling=Decimal("1e-18")
    ),
    "0x3204dcde0c50b7b2e606587663a0fe2ee8dfb6bf": TokenInfo(
        currency=CurrencyInfo(symbol="THEX", name="Thore Exchange Token"), scaling=Decimal("1e-0")
    ),
    "0x32054526df40fbb08b733abe256a8d21de58432d": TokenInfo(
        currency=CurrencyInfo(symbol="TRT", name="Taurus Chain"), scaling=Decimal("1e-18")
    ),
    "0x3209f98bebf0149b769ce26d71f7aea8e435efea": TokenInfo(
        currency=CurrencyInfo(symbol="TMT", name="Traxia"), scaling=Decimal("1e-18")
    ),
    "0x320e2231d13f58be6fd1bb71ccf460be61aaa80b": TokenInfo(
        currency=CurrencyInfo(symbol="ECOIN", name="ECOIN"), scaling=Decimal("1e-18")
    ),
    "0x3212b29e33587a00fb1c83346f5dbfa69a458923": TokenInfo(
        currency=CurrencyInfo(symbol="IMBTC", name="The Tokenized Bitcoin"), scaling=Decimal("1e-8")
    ),
    "0x321c2fe4446c7c963dc41dd58879af648838f98d": TokenInfo(
        currency=CurrencyInfo(symbol="CTX", name="Cryptex Finance"), scaling=Decimal("1e-18")
    ),
    "0x322124122df407b0d0d902cb713b3714fb2e2e1f": TokenInfo(
        currency=CurrencyInfo(symbol="SYFI", name="Soft Yearn"), scaling=Decimal("1e-9")
    ),
    "0x32353a6c91143bfd6c7d363b546e62a9a2489a20": TokenInfo(
        currency=CurrencyInfo(symbol="AGLD", name="Adventure Gold"), scaling=Decimal("1e-18")
    ),
    "0x324a48ebcbb46e61993931ef9d35f6697cd2901b": TokenInfo(
        currency=CurrencyInfo(symbol="SKRP", name="Skraps"), scaling=Decimal("1e-18")
    ),
    "0x324af2d5353f2dd138e234b359d30d67c64b1b20": TokenInfo(
        currency=CurrencyInfo(symbol="ORC", name="Oracle System"), scaling=Decimal("1e-18")
    ),
    "0x327673ae6b33bd3d90f0096870059994f30dc8af": TokenInfo(
        currency=CurrencyInfo(symbol="LMT", name="Lympo Market Token"), scaling=Decimal("1e-18")
    ),
    "0x327682779bab2bf4d1337e8974ab9de8275a7ca8": TokenInfo(
        currency=CurrencyInfo(symbol="BPT", name="Blockport Token"), scaling=Decimal("1e-18")
    ),
    "0x3277dd536471a3cbeb0c9486acad494c95a31e73": TokenInfo(
        currency=CurrencyInfo(symbol="CHT", name="CoinHe Token"), scaling=Decimal("1e-18")
    ),
    "0x328c4c80bc7aca0834db37e6600a6c49e12da4de": TokenInfo(
        currency=CurrencyInfo(symbol="ASNX", name="Aave SNX v1"), scaling=Decimal("1e-18")
    ),
    "0x3299842aa08b85c5c68dd432f2e7922eef60eee8": TokenInfo(
        currency=CurrencyInfo(symbol="NDXM.CX", name="Nasdaq 100 Index"), scaling=Decimal("1e-8")
    ),
    "0x32a18b15985a290604dd9b2ebc39a1035b1a6b9c": TokenInfo(
        currency=CurrencyInfo(symbol="YFST", name="YFST.Protocol"), scaling=Decimal("1e-18")
    ),
    "0x32a7c02e79c4ea1008dd6564b35f131428673c41": TokenInfo(
        currency=CurrencyInfo(symbol="CRU", name="Crust Network"), scaling=Decimal("1e-18")
    ),
    "0x32a8cd4d04d5f2e5de30ad73ef0a377eca2fdd98": TokenInfo(
        currency=CurrencyInfo(symbol="KRG", name="Karaganda Token"), scaling=Decimal("1e-18")
    ),
    "0x32b666599411f4721de6724c968ed9b3d1cabd79": TokenInfo(
        currency=CurrencyInfo(symbol="YAP", name="Yaapoo"), scaling=Decimal("1e-8")
    ),
    "0x32c4adb9cf57f972bc375129de91c897b4f364f1": TokenInfo(
        currency=CurrencyInfo(symbol="FLC", name="Flowchain"), scaling=Decimal("1e-18")
    ),
    "0x32c868f6318d6334b2250f323d914bc2239e4eee": TokenInfo(
        currency=CurrencyInfo(symbol="N3RDZ", name="N3RD Finance"), scaling=Decimal("1e-18")
    ),
    "0x32eb7fa944ad61b0cf093499af12f35a479315a2": TokenInfo(
        currency=CurrencyInfo(symbol="PUN", name="PunchToken"), scaling=Decimal("1e-18")
    ),
    "0x32f3b8a00b6912d0314be212fe9538b7b9430c12": TokenInfo(
        currency=CurrencyInfo(symbol="SRX", name="SiriusX"), scaling=Decimal("1e-8")
    ),
    "0x3310f5acb5df71da3b15a27230122bfbf3f7b9a0": TokenInfo(
        currency=CurrencyInfo(symbol="PATS", name="PatexShares"), scaling=Decimal("1e-18")
    ),
    "0x331a4589516eae384ea5f557853af6af73b9534e": TokenInfo(
        currency=CurrencyInfo(symbol="TCP", name="Token CashPay"), scaling=Decimal("1e-18")
    ),
    "0x331fa6c97c64e47475164b9fc8143b533c5ef529": TokenInfo(
        currency=CurrencyInfo(symbol="EXMR", name="EXMR FDN."), scaling=Decimal("1e-18")
    ),
    "0x33349b282065b0284d756f0577fb39c158f935e6": TokenInfo(
        currency=CurrencyInfo(symbol="MPL", name="Maple"), scaling=Decimal("1e-18")
    ),
    "0x3335f16af9008bfd32f1ee6c2be5d4f84fa0b9da": TokenInfo(
        currency=CurrencyInfo(symbol="DRGNBULL", name="3X Long Dragon Index Token"), scaling=Decimal("1e-18")
    ),
    "0x33384af34b03eaca63fd153f59589f504772b570": TokenInfo(
        currency=CurrencyInfo(symbol="ONLEXPA", name="onLEXpa Token"), scaling=Decimal("1e-18")
    ),
    "0x336213e1ddfc69f4701fc3f86f4ef4a160c1159d": TokenInfo(
        currency=CurrencyInfo(symbol="ICEX", name="iCEX"), scaling=Decimal("1e-18")
    ),
    "0x336492a0601cc85e08c14d390bf07d960328aaf4": TokenInfo(
        currency=CurrencyInfo(symbol="BST1", name="Blueshare Token"), scaling=Decimal("1e-18")
    ),
    "0x3366adfcd676463e2f5387d07649f227fcc5c15e": TokenInfo(
        currency=CurrencyInfo(symbol="SCSC", name="Smart Contract Scheme Coin"), scaling=Decimal("1e-9")
    ),
    "0x3366fdfc98a98e0d7af48c0641d5126f7d4324d5": TokenInfo(
        currency=CurrencyInfo(symbol="YNDX.CX", name="Yandex N.V."), scaling=Decimal("1e-8")
    ),
    "0x336f646f87d9f6bc6ed42dd46e8b3fd9dbd15c22": TokenInfo(
        currency=CurrencyInfo(symbol="CCT", name="Crystal Clear"), scaling=Decimal("1e-18")
    ),
    "0x33811d4edbcaed10a685254eb5d3c4e4398520d2": TokenInfo(
        currency=CurrencyInfo(symbol="YFE", name="YFE Money"), scaling=Decimal("1e-18")
    ),
    "0x3383c5a8969dc413bfddc9656eb80a1408e4ba20": TokenInfo(
        currency=CurrencyInfo(symbol="WANATHA", name="Wrapped ANATHA"), scaling=Decimal("1e-18")
    ),
    "0x3395167319297a0806260e87a329885f20e13da2": TokenInfo(
        currency=CurrencyInfo(symbol="FBEE", name="FBEE"), scaling=Decimal("1e-18")
    ),
    "0x339989c3d77a57d1abf1209af3ce8bb6cac53875": TokenInfo(
        currency=CurrencyInfo(symbol="JPM.CX", name="JPMorgan Chase"), scaling=Decimal("1e-8")
    ),
    "0x33afa6514ad44594b1886859165b9aa641bdaba9": TokenInfo(
        currency=CurrencyInfo(symbol="L9", name="LOTTO9"), scaling=Decimal("1e-18")
    ),
    "0x33b919f54692ddbf702065763ea2b50ca02e6bff": TokenInfo(
        currency=CurrencyInfo(symbol="MCW", name="Mocrow"), scaling=Decimal("1e-18")
    ),
    "0x33bfd20660eeaf952e8d5bc3236e1918701f17d0": TokenInfo(
        currency=CurrencyInfo(symbol="RCCC", name="RCCC"), scaling=Decimal("1e-18")
    ),
    "0x33c623a2baafeb8d15dfaf3ce44095efec83d72c": TokenInfo(
        currency=CurrencyInfo(symbol="SGP", name="SGPay"), scaling=Decimal("1e-18")
    ),
    "0x33cf48debdcf255b689a7b1d6be5661ec832cc30": TokenInfo(
        currency=CurrencyInfo(symbol="HUSWP", name="Hugeswap"), scaling=Decimal("1e-2")
    ),
    "0x33d0568941c0c64ff7e0fb4fba0b11bd37deed9f": TokenInfo(
        currency=CurrencyInfo(symbol="RAMP", name="RAMP"), scaling=Decimal("1e-18")
    ),
    "0x33d63ba1e57e54779f7ddaeaa7109349344cf5f1": TokenInfo(
        currency=CurrencyInfo(symbol="DATA", name="Data Economy Index"), scaling=Decimal("1e-18")
    ),
    "0x33d8e28949eb784556064ed095a18c0e66219860": TokenInfo(
        currency=CurrencyInfo(symbol="INA", name="INNOVA"), scaling=Decimal("1e-18")
    ),
    "0x33f90dee07c6e8b9682dd20f73e6c358b2ed0f03": TokenInfo(
        currency=CurrencyInfo(symbol="TRDT", name="Trident Group"), scaling=Decimal("1e-0")
    ),
    "0x3402e15b3ea0f1aec2679c4be4c6d051cef93953": TokenInfo(
        currency=CurrencyInfo(symbol="127760", name="QAO"), scaling=Decimal("1e-18")
    ),
    "0x34031510cb586733050f25c9888f685f4b084c66": TokenInfo(
        currency=CurrencyInfo(symbol="XNG.CX", name="US Natural Gas Spot"), scaling=Decimal("1e-8")
    ),
    "0x340d2bde5eb28c1eed91b2f790723e3b160613b7": TokenInfo(
        currency=CurrencyInfo(symbol="VEE", name="BLOCKv"), scaling=Decimal("1e-18")
    ),
    "0x340ef83ec8560892168d4062720f030460468656": TokenInfo(
        currency=CurrencyInfo(symbol="ETHM", name="Ethereum Meta"), scaling=Decimal("1e-18")
    ),
    "0x342ba159f988f24f0b033f3cc5232377ee500543": TokenInfo(
        currency=CurrencyInfo(symbol="RAC", name="RoboAdvisorCoin"), scaling=Decimal("1e-18")
    ),
    "0x3431f91b3a388115f00c5ba9fdb899851d005fb5": TokenInfo(
        currency=CurrencyInfo(symbol="GERO", name="GeroWallet"), scaling=Decimal("1e-18")
    ),
    "0x3432b6a60d23ca0dfca7761b7ab56459d9c964d0": TokenInfo(
        currency=CurrencyInfo(symbol="FXS", name="Frax Share"), scaling=Decimal("1e-18")
    ),
    "0x34364bee11607b1963d66bca665fde93fca666a8": TokenInfo(
        currency=CurrencyInfo(symbol="YOU", name="YOU Chain"), scaling=Decimal("1e-18")
    ),
    "0x3449fc1cd036255ba1eb19d65ff4ba2b8903a69a": TokenInfo(
        currency=CurrencyInfo(symbol="BAC", name="Basis Cash"), scaling=Decimal("1e-18")
    ),
    "0x3453769b660b7ee4261aaa043479aa3ca02243bf": TokenInfo(
        currency=CurrencyInfo(symbol="LZR", name="LaserCoin"), scaling=Decimal("1e-18")
    ),
    "0x345e0a3a19c54f8cd46de0d5a0eb897930223f65": TokenInfo(
        currency=CurrencyInfo(symbol="SESG.CX", name="Ses Fdr"), scaling=Decimal("1e-8")
    ),
    "0x34612903db071e888a4dadcaa416d3ee263a87b9": TokenInfo(
        currency=CurrencyInfo(symbol="ARTE", name="Items"), scaling=Decimal("1e-18")
    ),
    "0x3472a5a71965499acd81997a54bba8d852c6e53d": TokenInfo(
        currency=CurrencyInfo(symbol="BADGER", name="Badger DAO"), scaling=Decimal("1e-18")
    ),
    "0x3479b0acf875405d7853f44142fe06470a40f6cc": TokenInfo(
        currency=CurrencyInfo(symbol="VUSD", name="Value USD"), scaling=Decimal("1e-18")
    ),
    "0x347a29ea126a746c70e1ead570fddf438e66231a": TokenInfo(
        currency=CurrencyInfo(symbol="CUR", name="CurrentCoin"), scaling=Decimal("1e-18")
    ),
    "0x347a39127ae0730817b0caf177c4684e16a038fc": TokenInfo(
        currency=CurrencyInfo(symbol="XTRL", name="TurkeyEnergyToken"), scaling=Decimal("1e-8")
    ),
    "0x347c099f110ca6761779329d2879957b606b6ace": TokenInfo(
        currency=CurrencyInfo(symbol="JOINT", name="Joint Ventures"), scaling=Decimal("1e-18")
    ),
    "0x34950ff2b487d9e5282c5ab342d08a2f712eb79f": TokenInfo(
        currency=CurrencyInfo(symbol="WOZX", name="Efforce"), scaling=Decimal("1e-18")
    ),
    "0x3496b523e5c00a4b4150d6721320cddb234c3079": TokenInfo(
        currency=CurrencyInfo(symbol="NUM", name="Numbers Protocol"), scaling=Decimal("1e-18")
    ),
    "0x34bdf48a8f753de4822a6cfb1fee275f9b4d662e": TokenInfo(
        currency=CurrencyInfo(symbol="BKC", name="FACTS"), scaling=Decimal("1e-18")
    ),
    "0x34d18aac981d3c93e649814a5eca79e296411b65": TokenInfo(
        currency=CurrencyInfo(symbol="NEET", name="Neo Ether"), scaling=Decimal("1e-18")
    ),
    "0x34dd5edfed51c632d1d4d2502bc901efb5fdfcd4": TokenInfo(
        currency=CurrencyInfo(symbol="JURM", name="Juriseum"), scaling=Decimal("1e-18")
    ),
    "0x3503be8049ff6ce3235a4c9087f4f6f5da63eac6": TokenInfo(
        currency=CurrencyInfo(symbol="SVT", name="SVTChain"), scaling=Decimal("1e-18")
    ),
    "0x3505f494c3f0fed0b594e01fa41dd3967645ca39": TokenInfo(
        currency=CurrencyInfo(symbol="SWM", name="Swarm Network"), scaling=Decimal("1e-18")
    ),
    "0x3506424f91fd33084466f402d5d97f05f8e3b4af": TokenInfo(
        currency=CurrencyInfo(symbol="CHZ", name="Chiliz"), scaling=Decimal("1e-18")
    ),
    "0x350a6a30c79df3600c4e0e67deab0a64b645e2c2": TokenInfo(
        currency=CurrencyInfo(symbol="STRNG", name="StrongHold"), scaling=Decimal("1e-18")
    ),
    "0x35101c731b1548b5e48bb23f99edbc2f5c341935": TokenInfo(
        currency=CurrencyInfo(symbol="BHSC", name="BlackHoleSwap-Compound DAI/USDC"), scaling=Decimal("1e-18")
    ),
    "0x3516415161c478df10adbb8bb884cc83fbd5f11a": TokenInfo(
        currency=CurrencyInfo(symbol="DEX", name="AlphaDex"), scaling=Decimal("1e-18")
    ),
    "0x352c0f76cfd34ab3a2724ef67f46cf4d3f61192b": TokenInfo(
        currency=CurrencyInfo(symbol="WLEO", name="Wrapped Leo"), scaling=Decimal("1e-3")
    ),
    "0x35401c8ca3e994d627d1610777877e5abee932dc": TokenInfo(
        currency=CurrencyInfo(symbol="PAHOO", name="Pahoo"), scaling=Decimal("1e-18")
    ),
    "0x3543638ed4a9006e4840b105944271bcea15605d": TokenInfo(
        currency=CurrencyInfo(symbol="UUU", name="U Network"), scaling=Decimal("1e-18")
    ),
    "0x354e514c135c8603f840ffadb4c33cde6d2a37e0": TokenInfo(
        currency=CurrencyInfo(symbol="UNL", name="Unilock.Network"), scaling=Decimal("1e-18")
    ),
    "0x355376d6471e09a4ffca8790f50da625630c5270": TokenInfo(
        currency=CurrencyInfo(symbol="LST", name="Libartysharetoken"), scaling=Decimal("1e-18")
    ),
    "0x355a458d555151d3b27f94227960ade1504e526a": TokenInfo(
        currency=CurrencyInfo(symbol="SCC", name="StockChain"), scaling=Decimal("1e-18")
    ),
    "0x355c665e101b9da58704a8fddb5feef210ef20c0": TokenInfo(
        currency=CurrencyInfo(symbol="GOLDX", name="dForce GOLDx"), scaling=Decimal("1e-18")
    ),
    "0x3564ad35b9e95340e5ace2d6251dbfc76098669b": TokenInfo(
        currency=CurrencyInfo(symbol="mUSDC", name="DMM: USDC"), scaling=Decimal("1e-6")
    ),
    "0x3593d125a4f7849a1b059e64f4517a86dd60c95d": TokenInfo(
        currency=CurrencyInfo(symbol="OM", name="MANTRA DAO"), scaling=Decimal("1e-18")
    ),
    "0x3597bfd533a99c9aa083587b074434e61eb0a258": TokenInfo(
        currency=CurrencyInfo(symbol="DENT", name="Dent"), scaling=Decimal("1e-8")
    ),
    "0x35a18000230da775cac24873d00ff85bccded550": TokenInfo(
        currency=CurrencyInfo(symbol="CUNI", name="cUNI"), scaling=Decimal("1e-8")
    ),
    "0x35a4e77ae040afc9743157911d39d1451cf2f05d": TokenInfo(
        currency=CurrencyInfo(symbol="TWDT", name="Taiwan Digital Token"), scaling=Decimal("1e-6")
    ),
    "0x35a69642857083ba2f30bfab735dacc7f0bac969": TokenInfo(
        currency=CurrencyInfo(symbol="BBN", name="Banyan Network"), scaling=Decimal("1e-18")
    ),
    "0x35a735b7d1d811887966656855f870c05fd0a86d": TokenInfo(
        currency=CurrencyInfo(symbol="THRN", name="Thorncoin"), scaling=Decimal("1e-18")
    ),
    "0x35a79fceb867ee3392ed0c8dedd8dc2f6124c9cd": TokenInfo(
        currency=CurrencyInfo(symbol="ESPI", name="SPIDER ECOLOGY"), scaling=Decimal("1e-18")
    ),
    "0x35b08722aa26be119c1608029ccbc976ac5c1082": TokenInfo(
        currency=CurrencyInfo(symbol="EM", name="Eminer"), scaling=Decimal("1e-8")
    ),
    "0x35baa72038f127f9f8c8f9b491049f64f377914d": TokenInfo(
        currency=CurrencyInfo(symbol="EPX", name="ethPoker.io"), scaling=Decimal("1e-4")
    ),
    "0x35bd01fc9d6d5d81ca9e055db88dc49aa2c699a8": TokenInfo(
        currency=CurrencyInfo(symbol="FWB", name="Friends With Benefi"), scaling=Decimal("1e-18")
    ),
    "0x35c896b1700e344a81b95b6bc1d4d95b4503699c": TokenInfo(
        currency=CurrencyInfo(symbol="XPST", name="PokerSports"), scaling=Decimal("1e-18")
    ),
    "0x35d9ff00fbd73f2e73ba3e1e99c0a0c5f967518d": TokenInfo(
        currency=CurrencyInfo(symbol="XBR.CX", name="Brent Crude Oil Spot"), scaling=Decimal("1e-8")
    ),
    "0x35e3a8658d87fa71ba349bac7f3aed948f6ebc0c": TokenInfo(
        currency=CurrencyInfo(symbol="ZYR", name="Zyrri"), scaling=Decimal("1e-18")
    ),
    "0x35e78b3982e87ecfd5b3f3265b601c046cdbe232": TokenInfo(
        currency=CurrencyInfo(symbol="XAI", name="SideShift Token"), scaling=Decimal("1e-18")
    ),
    "0x35ea6342189b9b9d0103ec8d4e185a2c38847b68": TokenInfo(
        currency=CurrencyInfo(symbol="MIRCO", name="MIRCOLO"), scaling=Decimal("1e-18")
    ),
    "0x35f6b052c598d933d69a4eec4d04c73a191fe6c2": TokenInfo(
        currency=CurrencyInfo(symbol="ASNX", name="Aave SNX"), scaling=Decimal("1e-18")
    ),
    "0x35f82caa11c2459e179bc8102cce439d77c8ef25": TokenInfo(
        currency=CurrencyInfo(symbol="FC007", name="Friendcoin007"), scaling=Decimal("1e-18")
    ),
    "0x3611bc1a02e79bd50124edc138389f1f72bae143": TokenInfo(
        currency=CurrencyInfo(symbol="ADPT.CX", name="Adaptive Biotechnologies Corporation"), scaling=Decimal("1e-8")
    ),
    "0x36151737b45017234e9570cf9a1cac97138953c2": TokenInfo(
        currency=CurrencyInfo(symbol="NOIZ", name="Noiz Chain"), scaling=Decimal("1e-18")
    ),
    "0x3618516f45cd3c913f81f9987af41077932bc40d": TokenInfo(
        currency=CurrencyInfo(symbol="PCL", name="Peculium"), scaling=Decimal("1e-8")
    ),
    "0x361887c1d1b73557018c47c8001711168128cf69": TokenInfo(
        currency=CurrencyInfo(symbol="FDO", name="Firdaos"), scaling=Decimal("1e-18")
    ),
    "0x36232b1328e49a043434e71c02c0dc2be278e975": TokenInfo(
        currency=CurrencyInfo(symbol="XTS", name="Xaviera Tech"), scaling=Decimal("1e-18")
    ),
    "0x362bc847a3a9637d3af6624eec853618a43ed7d2": TokenInfo(
        currency=CurrencyInfo(symbol="PRQ", name="PARSIQ"), scaling=Decimal("1e-18")
    ),
    "0x3635e381c67252405c1c0e550973155832d5e490": TokenInfo(
        currency=CurrencyInfo(symbol="NJBC", name="Japan Brand Coin"), scaling=Decimal("1e-18")
    ),
    "0x3685ee91777e3ed4ba4122c429c504df833c3b26": TokenInfo(
        currency=CurrencyInfo(symbol="BZH", name="BZH TOKEN"), scaling=Decimal("1e-8")
    ),
    "0x368e5b38ec4b605f3607c09f3952cb996ad50f34": TokenInfo(
        currency=CurrencyInfo(symbol="GOOG.CX", name="Alphabet Inc"), scaling=Decimal("1e-8")
    ),
    "0x36905fc93280f52362a1cbab151f25dc46742fb5": TokenInfo(
        currency=CurrencyInfo(symbol="BTO", name="Bottos"), scaling=Decimal("1e-18")
    ),
    "0x369760ebf89d577a734d927a9599c1921397a152": TokenInfo(
        currency=CurrencyInfo(symbol="ESB", name="E-Shipp Block"), scaling=Decimal("1e-8")
    ),
    "0x369c8ff27da9fb53c6d971385d2f602c45ff79c2": TokenInfo(
        currency=CurrencyInfo(symbol="JKS.CX", name="JinkoSolar Holding Co Ltd"), scaling=Decimal("1e-8")
    ),
    "0x36a2422a863d5b950882190ff5433e513413343a": TokenInfo(
        currency=CurrencyInfo(symbol="SBCH", name="sBCH"), scaling=Decimal("1e-18")
    ),
    "0x36a73557f5bde5195ec39eca82d28b8a36d21141": TokenInfo(
        currency=CurrencyInfo(symbol="FRX", name="Forex Coin"), scaling=Decimal("1e-18")
    ),
    "0x36aba3ddd8b17c01e73ee174ca5d308703a203a5": TokenInfo(
        currency=CurrencyInfo(symbol="ABGS", name="All Bit Gambling Shares Chain"), scaling=Decimal("1e-8")
    ),
    "0x36ac219f90f5a6a3c77f2a7b660e3cc701f68e25": TokenInfo(
        currency=CurrencyInfo(symbol="XCM", name="CoinMetro"), scaling=Decimal("1e-18")
    ),
    "0x36b60a425b82483004487abc7adcb0002918fc56": TokenInfo(
        currency=CurrencyInfo(symbol="TICO", name="TICOEX Token (Formerly TopInvestmentCoin)"), scaling=Decimal("1e-8")
    ),
    "0x36dcffe069a3f2878fab2a46d81e83d462d0cbf7": TokenInfo(
        currency=CurrencyInfo(symbol="TCFX", name="Tcbcoin"), scaling=Decimal("1e-18")
    ),
    "0x36dd88a0a0f53c90555087e57f758383978e64b5": TokenInfo(
        currency=CurrencyInfo(symbol="PPL", name="Qripplex"), scaling=Decimal("1e-18")
    ),
    "0x36ed7baad9a571b5dad55d096c0ed902188d6d3c": TokenInfo(
        currency=CurrencyInfo(symbol="IPAD", name="Infinity Pad"), scaling=Decimal("1e-18")
    ),
    "0x36f3fd68e7325a35eb768f1aedaae9ea0689d723": TokenInfo(
        currency=CurrencyInfo(symbol="ESD", name="Empty Set Dollar"), scaling=Decimal("1e-18")
    ),
    "0x3705f7bf96ba50ed12533642f60a20904bcbde0a": TokenInfo(
        currency=CurrencyInfo(symbol="SBUX.CX", name="Starbucks Corp"), scaling=Decimal("1e-8")
    ),
    "0x3709ae438e0557976296051f431256f386de370c": TokenInfo(
        currency=CurrencyInfo(symbol="YFN", name="Yearn Finance Network"), scaling=Decimal("1e-18")
    ),
    "0x370adc71f67f581158dc56f539df5f399128ddf9": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNIMKRWETH", name="Aave AMM UniMKRWETH"), scaling=Decimal("1e-18")
    ),
    "0x37236cd05b34cc79d3715af2383e96dd7443dcf1": TokenInfo(
        currency=CurrencyInfo(symbol="SLP", name="Small Love Potion"), scaling=Decimal("1e-0")
    ),
    "0x37427576324fe1f3625c9102674772d7cf71377d": TokenInfo(
        currency=CurrencyInfo(symbol="SGT", name="SelfieYo Gold Token"), scaling=Decimal("1e-18")
    ),
    "0x374cb8c27130e2c9e04f44303f3c8351b9de61c1": TokenInfo(
        currency=CurrencyInfo(symbol="BAO", name="Bao Finance"), scaling=Decimal("1e-18")
    ),
    "0x3758e00b100876c854636ef8db61988931bb8025": TokenInfo(
        currency=CurrencyInfo(symbol="UNIQ", name="Uniqly"), scaling=Decimal("1e-18")
    ),
    "0x375abb85c329753b1ba849a601438ae77eec9893": TokenInfo(
        currency=CurrencyInfo(symbol="PDT", name="ParagonsDAO"), scaling=Decimal("1e-18")
    ),
    "0x3779d960261f882750b39c622527822c88c98e13": TokenInfo(
        currency=CurrencyInfo(symbol="BFT", name="Bitget DeFi Token"), scaling=Decimal("1e-18")
    ),
    "0x377d552914e7a104bc22b4f3b6268ddc69615be7": TokenInfo(
        currency=CurrencyInfo(symbol="NEXT", name="NEXT"), scaling=Decimal("1e-18")
    ),
    "0x378903a03fb2c3ac76bb52773e3ce11340377a32": TokenInfo(
        currency=CurrencyInfo(symbol="CCC", name="Clipper Coin"), scaling=Decimal("1e-18")
    ),
    "0x37c430c2b5f9ff85e534873c715871818ab1623e": TokenInfo(
        currency=CurrencyInfo(symbol="AXC", name="AXIA Coin"), scaling=Decimal("1e-18")
    ),
    "0x37d404a072056eda0cd10cb714d35552329f8500": TokenInfo(
        currency=CurrencyInfo(symbol="XRT", name="XRTFoundation"), scaling=Decimal("1e-18")
    ),
    "0x37d40510a2f5bc98aa7a0f7bf4b3453bcfb90ac1": TokenInfo(
        currency=CurrencyInfo(symbol="BBI", name="BelugaPay"), scaling=Decimal("1e-18")
    ),
    "0x37d6e7f287200c740012747d2a79295caed2db35": TokenInfo(
        currency=CurrencyInfo(symbol="ALP", name="ALP Coin"), scaling=Decimal("1e-8")
    ),
    "0x37db56e0fba0be2cbf96e3de3bff8096b6d59179": TokenInfo(
        currency=CurrencyInfo(symbol="ETY", name="EthereumCloud"), scaling=Decimal("1e-18")
    ),
    "0x37e1160184f7dd29f00b78c050bf13224780b0b0": TokenInfo(
        currency=CurrencyInfo(symbol="YCC", name="Yuan Chain Coin"), scaling=Decimal("1e-8")
    ),
    "0x37e8789bb9996cac9156cd5f5fd32599e6b91289": TokenInfo(
        currency=CurrencyInfo(symbol="AID", name="AidCoin"), scaling=Decimal("1e-18")
    ),
    "0x37ee79e0b44866876de2fb7f416d0443dd5ae481": TokenInfo(
        currency=CurrencyInfo(symbol="TAT", name="Tatcoin"), scaling=Decimal("1e-18")
    ),
    "0x37f04d2c3ae075fad5483bb918491f656b12bdb6": TokenInfo(
        currency=CurrencyInfo(symbol="VEST", name="VestChain"), scaling=Decimal("1e-8")
    ),
    "0x37f6f8eb409deb9feaf032c109a72319f665c79d": TokenInfo(
        currency=CurrencyInfo(symbol="GCR", name="Gold Coin Reserve"), scaling=Decimal("1e-18")
    ),
    "0x37fe0f067fa808ffbdd12891c0858532cfe7361d": TokenInfo(
        currency=CurrencyInfo(symbol="CIV", name="Civilization"), scaling=Decimal("1e-18")
    ),
    "0x3810a4ddf41e586fa0dba1463a7951b748cecfca": TokenInfo(
        currency=CurrencyInfo(symbol="MPAY", name="Menapay"), scaling=Decimal("1e-18")
    ),
    "0x38118bdb3b480f570837a4c2e88fac6e83be6689": TokenInfo(
        currency=CurrencyInfo(symbol="WWC", name="Werewolf Coin"), scaling=Decimal("1e-18")
    ),
    "0x382f0160c24f5c515a19f155bac14d479433a407": TokenInfo(
        currency=CurrencyInfo(symbol="KLEE", name="KleeKai"), scaling=Decimal("1e-9")
    ),
    "0x3833dda0aeb6947b98ce454d89366cba8cc55528": TokenInfo(
        currency=CurrencyInfo(symbol="SPHTX", name="SophiaTX"), scaling=Decimal("1e-18")
    ),
    "0x383518188c0c6d7730d91b2c03a03c837814a899": TokenInfo(
        currency=CurrencyInfo(symbol="OHM", name="Olympus"), scaling=Decimal("1e-9")
    ),
    "0x3839d8ba312751aa0248fed6a8bacb84308e20ed": TokenInfo(
        currency=CurrencyInfo(symbol="BEZ", name="Bezop"), scaling=Decimal("1e-18")
    ),
    "0x38405fa410c6eba342f9eb5ac66b2aaf6498c8e9": TokenInfo(
        currency=CurrencyInfo(symbol="VT", name="Vectoraic"), scaling=Decimal("1e-18")
    ),
    "0x3845badade8e6dff049820680d1f14bd3903a5d0": TokenInfo(
        currency=CurrencyInfo(symbol="SAND", name="The Sandbox"), scaling=Decimal("1e-18")
    ),
    "0x386358639244ed385ecee3f46dae26e6ab616031": TokenInfo(
        currency=CurrencyInfo(symbol="XAGM.CX", name="Silver Spot"), scaling=Decimal("1e-8")
    ),
    "0x386467f1f3ddbe832448650418311a479eecfc57": TokenInfo(
        currency=CurrencyInfo(symbol="MBRS", name="Embers"), scaling=Decimal("1e-0")
    ),
    "0x386cabc0b14a507a4e024dea15554342865b20de": TokenInfo(
        currency=CurrencyInfo(symbol="DAPPT", name="Dapp Token"), scaling=Decimal("1e-18")
    ),
    "0x386faa4703a34a7fdb19bec2e14fd427c9638416": TokenInfo(
        currency=CurrencyInfo(symbol="DCA", name="DoBetAcceptBet"), scaling=Decimal("1e-18")
    ),
    "0x3883f5e181fccaf8410fa61e12b59bad963fb645": TokenInfo(
        currency=CurrencyInfo(symbol="THETA", name="Theta Token"), scaling=Decimal("1e-18")
    ),
    "0x38894302a6eabea6f2b29b508031d2ed75f0be22": TokenInfo(
        currency=CurrencyInfo(symbol="FEAR", name="FEARLESS"), scaling=Decimal("1e-18")
    ),
    "0x388fd8a5145d6ef85aae14d494f93df9d1c7c00c": TokenInfo(
        currency=CurrencyInfo(symbol="BTRL", name="BitcoinRegular"), scaling=Decimal("1e-8")
    ),
    "0x3893b9422cd5d70a81edeffe3d5a1c6a978310bb": TokenInfo(
        currency=CurrencyInfo(symbol="MITH", name="Mithril"), scaling=Decimal("1e-18")
    ),
    "0x389999216860ab8e0175387a0c90e5c52522c945": TokenInfo(
        currency=CurrencyInfo(symbol="FEG", name="FEG Token"), scaling=Decimal("1e-9")
    ),
    "0x38a0df9a08d18dc06cd91fc7ec94a0acdf28d994": TokenInfo(
        currency=CurrencyInfo(symbol="HTX", name="Huptex"), scaling=Decimal("1e-2")
    ),
    "0x38a19ba829f192a30ec7e03cda1368c50dad9785": TokenInfo(
        currency=CurrencyInfo(symbol="THPC", name="Texas Hold'em Poker Chain"), scaling=Decimal("1e-8")
    ),
    "0x38a2fdc11f526ddd5a607c1f251c065f40fbf2f7": TokenInfo(
        currency=CurrencyInfo(symbol="PHNX", name="PhoenixDAO"), scaling=Decimal("1e-18")
    ),
    "0x38acefad338b870373fb8c810fe705569e1c7225": TokenInfo(
        currency=CurrencyInfo(symbol="YF4", name="Yearn4 Finance"), scaling=Decimal("1e-18")
    ),
    "0x38c4102d11893351ced7ef187fcf43d33eb1abe6": TokenInfo(
        currency=CurrencyInfo(symbol="SHRIMP", name="Shrimp Finance"), scaling=Decimal("1e-18")
    ),
    "0x38c6a68304cdefb9bec48bbfaaba5c5b47818bb2": TokenInfo(
        currency=CurrencyInfo(symbol="HPB", name="High Performance Blockchain"), scaling=Decimal("1e-18")
    ),
    "0x38c87aa89b2b8cd9b95b736e1fa7b612ea972169": TokenInfo(
        currency=CurrencyInfo(symbol="AMO", name="AMO Coin"), scaling=Decimal("1e-18")
    ),
    "0x38d1b0d157529bd5d936719a8a5f8379afb24faa": TokenInfo(
        currency=CurrencyInfo(symbol="DKYC", name="DataKYC"), scaling=Decimal("1e-18")
    ),
    "0x38d389c300357a26beec198f3893fba54fde69c5": TokenInfo(
        currency=CurrencyInfo(symbol="PUSD", name="PayUSD"), scaling=Decimal("1e-18")
    ),
    "0x38e491a71291cd43e8de63b7253e482622184894": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNISNXWETH", name="Aave AMM UniSNXWETH"), scaling=Decimal("1e-18")
    ),
    "0x38e4adb44ef08f22f5b5b76a8f0c2d0dcbe7dca1": TokenInfo(
        currency=CurrencyInfo(symbol="CVP", name="PowerPool Concentrated Voting Power"), scaling=Decimal("1e-18")
    ),
    "0x38f22479795a1a51ccd1e5a41f09c7525fb27318": TokenInfo(
        currency=CurrencyInfo(symbol="TTP", name="Trent"), scaling=Decimal("1e-15")
    ),
    "0x38f7cd43662d1cff4cc3c2c4b749f7cfed1d1db3": TokenInfo(
        currency=CurrencyInfo(symbol="NVA", name="Neeva Defi"), scaling=Decimal("1e-18")
    ),
    "0x38fc9f9db961dc455ac0b3aec65ed2db8b958b03": TokenInfo(
        currency=CurrencyInfo(symbol="SQ.CX", name="Square Cl A"), scaling=Decimal("1e-8")
    ),
    "0x39013f961c378f02c2b82a6e1d31e9812786fd9d": TokenInfo(
        currency=CurrencyInfo(symbol="SMS", name="Speed Mining Service"), scaling=Decimal("1e-3")
    ),
    "0x39043aae9c48a628f5184af7a5bb925137757b15": TokenInfo(
        currency=CurrencyInfo(symbol="YATX", name="Yattaqi Pro"), scaling=Decimal("1e-8")
    ),
    "0x390d6673c1fa9dbb8000db1ae89252b7d531ab75": TokenInfo(
        currency=CurrencyInfo(symbol="KEA", name="KEA Coin"), scaling=Decimal("1e-8")
    ),
    "0x3917e933bd430c08304cae2aa6d9746b806406c2": TokenInfo(
        currency=CurrencyInfo(symbol="BTV", name="Bitcoin EVO"), scaling=Decimal("1e-8")
    ),
    "0x3918c42f14f2eb1168365f911f63e540e5a306b5": TokenInfo(
        currency=CurrencyInfo(symbol="NRP", name="Neural Protocol"), scaling=Decimal("1e-8")
    ),
    "0x391e86e2c002c70dee155eaceb88f7a3c38f5976": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNIUSDCWETH", name="Aave AMM UniUSDCWET"), scaling=Decimal("1e-18")
    ),
    "0x3930e4ddb4d24ef2f4cb54c1f009a3694b708428": TokenInfo(
        currency=CurrencyInfo(symbol="GFN", name="Game Fanz"), scaling=Decimal("1e-8")
    ),
    "0x3936ad01cf109a36489d93cabda11cf062fd3d48": TokenInfo(
        currency=CurrencyInfo(symbol="COIL", name="Coil"), scaling=Decimal("1e-9")
    ),
    "0x393fac0773c765c80dc887451377d553c46f83b1": TokenInfo(
        currency=CurrencyInfo(symbol="RAS", name="RAKSUR"), scaling=Decimal("1e-18")
    ),
    "0x39405a9cee35331dfe835fd6b0e7a9fa6f2cf48d": TokenInfo(
        currency=CurrencyInfo(symbol="WTB", name="WORLD TRADE BASE"), scaling=Decimal("1e-18")
    ),
    "0x394594b06adb8f54e393bfaf13ca5786bcd3f9bb": TokenInfo(
        currency=CurrencyInfo(symbol="FCT", name="Africa Chain"), scaling=Decimal("1e-18")
    ),
    "0x39550dc5919a990a5786fcdc1d5b7c392d362dde": TokenInfo(
        currency=CurrencyInfo(symbol="DTOX", name="DeTox The World"), scaling=Decimal("1e-8")
    ),
    "0x395c47a421c254ae42253764a7f56e0ee0cddac5": TokenInfo(
        currency=CurrencyInfo(
            symbol="REALTOKEN-20200-LESURE-ST-DETROIT-MI", name="RealToken 20200 Lesure Street Detroit MI"
        ),
        scaling=Decimal("1e-18"),
    ),
    "0x395f7bc771db53732025547458f96ee217af6ad1": TokenInfo(
        currency=CurrencyInfo(symbol="IEOS", name="Ieo Service"), scaling=Decimal("1e-18")
    ),
    "0x39795344cbcc76cc3fb94b9d1b15c23c2070c66d": TokenInfo(
        currency=CurrencyInfo(symbol="SHARE", name="Seigniorage Shares"), scaling=Decimal("1e-9")
    ),
    "0x398656d0bdb435d1032decfc2d2d87852262bb19": TokenInfo(
        currency=CurrencyInfo(symbol="HE", name="House Edge"), scaling=Decimal("1e-5")
    ),
    "0x399a0e6fbeb3d74c85357439f4c8aed9678a5cbf": TokenInfo(
        currency=CurrencyInfo(symbol="DCL", name="DISLEDGER"), scaling=Decimal("1e-3")
    ),
    "0x399f9a95305114efacb91d1d6c02cbe234dd36af": TokenInfo(
        currency=CurrencyInfo(symbol="BIZ", name="BIZAIN Token"), scaling=Decimal("1e-18")
    ),
    "0x39aa39c021dfbae8fac545936693ac917d5e7563": TokenInfo(
        currency=CurrencyInfo(symbol="CUSDC", name="cUSDC"), scaling=Decimal("1e-8")
    ),
    "0x39ab32006afe65a0b4d6a9a89877c2c33ad19eb5": TokenInfo(
        currency=CurrencyInfo(symbol="CUSDT", name="Ctether USD"), scaling=Decimal("1e-6")
    ),
    "0x39b23f14528fb000e8c46ad75df2db9a3ee49422": TokenInfo(
        currency=CurrencyInfo(symbol="TIX", name="Lottery Tickets"), scaling=Decimal("1e-8")
    ),
    "0x39bb259f66e1c59d5abef88375979b4d20d98022": TokenInfo(
        currency=CurrencyInfo(symbol="WAX", name="Wax Token"), scaling=Decimal("1e-8")
    ),
    "0x39c6b3e42d6a679d7d776778fe880bc9487c2eda": TokenInfo(
        currency=CurrencyInfo(symbol="AKNC", name="Aave KNC"), scaling=Decimal("1e-18")
    ),
    "0x39eae99e685906ff1c11a962a743440d0a1a6e09": TokenInfo(
        currency=CurrencyInfo(symbol="HOLY", name="Holyheld (OLD)"), scaling=Decimal("1e-18")
    ),
    "0x3a0d746b3ea1d8ccdf19ad915913bd68391133ca": TokenInfo(
        currency=CurrencyInfo(symbol="SYSX", name="SyscoinToken"), scaling=Decimal("1e-8")
    ),
    "0x3a10b7a22ae98e0f53276923f19f99b259f61778": TokenInfo(
        currency=CurrencyInfo(symbol="SOZ", name="Secrets of Zurich Token"), scaling=Decimal("1e-18")
    ),
    "0x3a1237d38d0fb94513f85d61679cad7f38507242": TokenInfo(
        currency=CurrencyInfo(symbol="MIC", name="Mindexcoin"), scaling=Decimal("1e-18")
    ),
    "0x3a1bda28adb5b0a812a7cf10a1950c920f79bcd3": TokenInfo(
        currency=CurrencyInfo(symbol="FLP", name="Gameflip"), scaling=Decimal("1e-18")
    ),
    "0x3a26746ddb79b1b8e4450e3f4ffe3285a307387e": TokenInfo(
        currency=CurrencyInfo(symbol="ETHB", name="ETHERBTC"), scaling=Decimal("1e-8")
    ),
    "0x3a3a65aab0dd2a17e3f1947ba16138cd37d08c04": TokenInfo(
        currency=CurrencyInfo(symbol="AETH", name="Aave ETH v1"), scaling=Decimal("1e-18")
    ),
    "0x3a43a04d80f9881d88080bf9fa8bb720afb6c966": TokenInfo(
        currency=CurrencyInfo(symbol="XLMBULL", name="3X Long Stellar Token"), scaling=Decimal("1e-18")
    ),
    "0x3a4a0d5b8dfacd651ee28ed4ffebf91500345489": TokenInfo(
        currency=CurrencyInfo(symbol="BRX", name="BerryX"), scaling=Decimal("1e-18")
    ),
    "0x3a4f40631a4f906c2bad353ed06de7a5d3fcb430": TokenInfo(
        currency=CurrencyInfo(symbol="PLA", name="PlayDapp"), scaling=Decimal("1e-18")
    ),
    "0x3a50bd419e88b07d7a27eb0b79e691c7350fc54c": TokenInfo(
        currency=CurrencyInfo(symbol="MA.CX", name="Mastercard Inc"), scaling=Decimal("1e-8")
    ),
    "0x3a68b8ff75723134f8e59bddf7a7e17bdb46da91": TokenInfo(
        currency=CurrencyInfo(symbol="CHT", name="Cultural Heritage Token"), scaling=Decimal("1e-18")
    ),
    "0x3a6dbec0218284037e8364121a5b79883d5d6f94": TokenInfo(
        currency=CurrencyInfo(symbol="MCHP.CX", name="Microchip Technology Incorporated"), scaling=Decimal("1e-8")
    ),
    "0x3a73f6156c4fbc71b8fdf38090a9d99401163644": TokenInfo(
        currency=CurrencyInfo(symbol="LNT", name="Lottonation"), scaling=Decimal("1e-18")
    ),
    "0x3a856d4effa670c54585a5d523e96513e148e95d": TokenInfo(
        currency=CurrencyInfo(symbol="TRIAS", name="Trias Token"), scaling=Decimal("1e-18")
    ),
    "0x3a880652f47bfaa771908c07dd8673a787daed3a": TokenInfo(
        currency=CurrencyInfo(symbol="DDX", name="DerivaDAO"), scaling=Decimal("1e-18")
    ),
    "0x3a8cccb969a61532d1e6005e2ce12c200caece87": TokenInfo(
        currency=CurrencyInfo(symbol="TITAN", name="TitanSwap"), scaling=Decimal("1e-18")
    ),
    "0x3a92bd396aef82af98ebc0aa9030d25a23b11c6b": TokenInfo(
        currency=CurrencyInfo(symbol="TBX", name="Tokenbox"), scaling=Decimal("1e-18")
    ),
    "0x3a9fff453d50d4ac52a6890647b823379ba36b9e": TokenInfo(
        currency=CurrencyInfo(symbol="SHUF", name="Shuffle Monster"), scaling=Decimal("1e-18")
    ),
    "0x3aa5f749d4a6bcf67dac1091ceb69d1f5d86fa53": TokenInfo(
        currency=CurrencyInfo(symbol="DEFLCT", name="Deflect"), scaling=Decimal("1e-9")
    ),
    "0x3aada3e213abf8529606924d8d1c55cbdc70bf74": TokenInfo(
        currency=CurrencyInfo(symbol="XMON", name="XMON"), scaling=Decimal("1e-18")
    ),
    "0x3aba9f23e857e6dbc4062a2ed4dbb041025b59b0": TokenInfo(
        currency=CurrencyInfo(symbol="TOKIO", name="TOKIO Coin"), scaling=Decimal("1e-18")
    ),
    "0x3abdff32f76b42e7635bdb7e425f0231a5f3ab17": TokenInfo(
        currency=CurrencyInfo(symbol="CJT", name="ConnectJob"), scaling=Decimal("1e-18")
    ),
    "0x3aca71c508e06dc6b2758dab6eb20f7654572fb7": TokenInfo(
        currency=CurrencyInfo(symbol="DREP", name="DREP"), scaling=Decimal("1e-18")
    ),
    "0x3adfc4999f77d04c8341bac5f3a76f58dff5b37a": TokenInfo(
        currency=CurrencyInfo(symbol="PRIX", name="Privatix"), scaling=Decimal("1e-8")
    ),
    "0x3af33bef05c2dcb3c7288b77fe1c8d2aeba4d789": TokenInfo(
        currency=CurrencyInfo(symbol="KROM", name="Kromatika"), scaling=Decimal("1e-18")
    ),
    "0x3af375d9f77ddd4f16f86a5d51a9386b7b4493fa": TokenInfo(
        currency=CurrencyInfo(symbol="YTRUMP", name="YES Trump Augur Prediction Token"), scaling=Decimal("1e-15")
    ),
    "0x3af5ba94c29a8407785f5f6d90ef5d69a8eb2436": TokenInfo(
        currency=CurrencyInfo(symbol="UWBTC", name="Unagii Wrapped Bitcoin"), scaling=Decimal("1e-8")
    ),
    "0x3afa1902b1f8a802abc18e5ad982d1bcd34afe22": TokenInfo(
        currency=CurrencyInfo(symbol="GST", name="GrEarn"), scaling=Decimal("1e-18")
    ),
    "0x3afe25a2739b5c2e08cfec439f9621d91ff7fbfb": TokenInfo(
        currency=CurrencyInfo(symbol="BLVD", name="BULVRD"), scaling=Decimal("1e-18")
    ),
    "0x3affcca64c2a6f4e3b6bd9c64cd2c969efd1ecbe": TokenInfo(
        currency=CurrencyInfo(symbol="DSLA", name="DSLA Protocol"), scaling=Decimal("1e-18")
    ),
    "0x3b16fb80ab6ac8562203f3913f58ee0c4dfc08b8": TokenInfo(
        currency=CurrencyInfo(symbol="AVT", name="Advertising Token"), scaling=Decimal("1e-2")
    ),
    "0x3b1ee4e6df767434fa576a2e9b62e071fb169e83": TokenInfo(
        currency=CurrencyInfo(symbol="CPB.CX", name="Campbell Soup"), scaling=Decimal("1e-8")
    ),
    "0x3b3801f0fc76528e42390df701f513fc62cbf154": TokenInfo(
        currency=CurrencyInfo(symbol="MCM", name="MONEY CASH MINER"), scaling=Decimal("1e-18")
    ),
    "0x3b3a5557f119106270017a7662488c1ff6312a6b": TokenInfo(
        currency=CurrencyInfo(symbol="LGC", name="LOGISTICS"), scaling=Decimal("1e-18")
    ),
    "0x3b3ac5386837dc563660fb6a0937dfaa5924333b": TokenInfo(
        currency=CurrencyInfo(symbol="BCURVE", name="LP-bCurve"), scaling=Decimal("1e-18")
    ),
    "0x3b484b82567a09e2588a13d54d032153f0c0aee0": TokenInfo(
        currency=CurrencyInfo(symbol="SOS", name="OpenDAO"), scaling=Decimal("1e-18")
    ),
    "0x3b4b29c4c1872a60d09937686bd2b358db9dee8a": TokenInfo(
        currency=CurrencyInfo(symbol="TCH", name="Teacher Coin"), scaling=Decimal("1e-18")
    ),
    "0x3b4c65f1e16cb0e50552c08a495035b97ab00d07": TokenInfo(
        currency=CurrencyInfo(symbol="EXPE.CX", name="Expedia Inc"), scaling=Decimal("1e-8")
    ),
    "0x3b4caaaf6f3ce5bee2871c89987cbd825ac30822": TokenInfo(
        currency=CurrencyInfo(symbol="ON", name="OFIN TOKEN"), scaling=Decimal("1e-18")
    ),
    "0x3b544e6fcf6c8dce9d8b45a4fdf21c9b02f9fda9": TokenInfo(
        currency=CurrencyInfo(symbol="GHD", name="Giftedhands"), scaling=Decimal("1e-18")
    ),
    "0x3b58c52c03ca5eb619eba171091c86c34d603e5f": TokenInfo(
        currency=CurrencyInfo(symbol="MCI", name="MCI Coin"), scaling=Decimal("1e-9")
    ),
    "0x3b5f11dbac1476af17957c6e5991f21c826743dd": TokenInfo(
        currency=CurrencyInfo(symbol="BAK", name="BaconCoin"), scaling=Decimal("1e-8")
    ),
    "0x3b62f3820e0b035cc4ad602dece6d796bc325325": TokenInfo(
        currency=CurrencyInfo(symbol="DEUS", name="DEUS Finance"), scaling=Decimal("1e-18")
    ),
    "0x3b78dc5736a49bd297dd2e4d62daa83d35a22749": TokenInfo(
        currency=CurrencyInfo(symbol="FNSP", name="Finswap"), scaling=Decimal("1e-18")
    ),
    "0x3b7ac088c0d56d1fcb890a510a4a911ce4fe363a": TokenInfo(
        currency=CurrencyInfo(symbol="IBM.CX", name="International Business Machines Corp"), scaling=Decimal("1e-8")
    ),
    "0x3b834a620751a811f65d8f599b3b72617a4418d0": TokenInfo(
        currency=CurrencyInfo(symbol="ATOMBEAR", name="3X Short Cosmos Token"), scaling=Decimal("1e-18")
    ),
    "0x3b9be07d622accaed78f479bc0edabfd6397e320": TokenInfo(
        currency=CurrencyInfo(symbol="LSS", name="Lossless"), scaling=Decimal("1e-18")
    ),
    "0x3b9e094d56103611f0acefdab43182347ba60df4": TokenInfo(
        currency=CurrencyInfo(symbol="XPN", name="PANTHEON X"), scaling=Decimal("1e-18")
    ),
    "0x3bd88a550d5953431cf3fd933bce574758046e3a": TokenInfo(
        currency=CurrencyInfo(symbol="EDS", name="E-Dome Standard"), scaling=Decimal("1e-0")
    ),
    "0x3be6e7bf2cd8e1a0a95597e72ca6d3709bbeff76": TokenInfo(
        currency=CurrencyInfo(symbol="DMTC", name="Demeter Chain"), scaling=Decimal("1e-18")
    ),
    "0x3be90f3ac213a730d9091bdda45a2f69ad98892b": TokenInfo(
        currency=CurrencyInfo(symbol="HEX", name="Health Evolution on X.blockchain"), scaling=Decimal("1e-18")
    ),
    "0x3c03b4ec9477809072ff9cc9292c9b25d4a8e6c6": TokenInfo(
        currency=CurrencyInfo(symbol="CVR", name="Polkacover"), scaling=Decimal("1e-18")
    ),
    "0x3c04ff86492ce16ccb306acb9226a1064cafad07": TokenInfo(
        currency=CurrencyInfo(symbol="NCA", name="Nuclear"), scaling=Decimal("1e-6")
    ),
    "0x3c20d67b6b1ae0985f913abb7397babc2fbb1a1f": TokenInfo(
        currency=CurrencyInfo(symbol="ICD", name="ICEDIUM"), scaling=Decimal("1e-18")
    ),
    "0x3c45b24359fb0e107a4eaa56bd0f2ce66c99a0e5": TokenInfo(
        currency=CurrencyInfo(symbol="ANK", name="Apple Network"), scaling=Decimal("1e-18")
    ),
    "0x3c4a3ffd813a107febd57b2f01bc344264d90fde": TokenInfo(
        currency=CurrencyInfo(symbol="ETK", name="Energi Token"), scaling=Decimal("1e-2")
    ),
    "0x3c4a46f0c075a7f191a7459bb51eb1f81ac36f8a": TokenInfo(
        currency=CurrencyInfo(symbol="PAXGBEAR", name="3X Short PAX Gold Token"), scaling=Decimal("1e-18")
    ),
    "0x3c4b6e6e1ea3d4863700d7f76b36b7f3d3f13e3d": TokenInfo(
        currency=CurrencyInfo(symbol="VGX", name="Voyager Token"), scaling=Decimal("1e-8")
    ),
    "0x3c4bea627039f0b7e7d21e34bb9c9fe962977518": TokenInfo(
        currency=CurrencyInfo(symbol="UCT", name="Ubique Chain of Things (UCOT)"), scaling=Decimal("1e-18")
    ),
    "0x3c6da7763caa0e4b684bbc733f04a8ec08af3762": TokenInfo(
        currency=CurrencyInfo(symbol="MODX", name="MODEL-X-coin"), scaling=Decimal("1e-8")
    ),
    "0x3c6ff50c9ec362efa359317009428d52115fe643": TokenInfo(
        currency=CurrencyInfo(symbol="PERX", name="PeerEx Network"), scaling=Decimal("1e-18")
    ),
    "0x3c75226555fc496168d48b88df83b95f16771f37": TokenInfo(
        currency=CurrencyInfo(symbol="DROP", name="Droplex Token"), scaling=Decimal("1e-0")
    ),
    "0x3c7b464376db7c9927930cf50eefdea2eff3a66a": TokenInfo(
        currency=CurrencyInfo(symbol="USDA", name="USDA"), scaling=Decimal("1e-8")
    ),
    "0x3c8d2fce49906e11e71cb16fa0ffeb2b16c29638": TokenInfo(
        currency=CurrencyInfo(symbol="NFTL", name="Nifty League"), scaling=Decimal("1e-18")
    ),
    "0x3c955e35b6da1ff623d38d750c85b3aed89a10c1": TokenInfo(
        currency=CurrencyInfo(symbol="LEOBEAR", name="3X Short LEO Token"), scaling=Decimal("1e-18")
    ),
    "0x3c9d6c1c73b31c837832c72e04d3152f051fc1a9": TokenInfo(
        currency=CurrencyInfo(symbol="BOR", name="BoringDAO [OLD]"), scaling=Decimal("1e-18")
    ),
    "0x3ca660b3200a89641abf895cf051eb42dafb01ef": TokenInfo(
        currency=CurrencyInfo(symbol="PAY", name="Pay Chain"), scaling=Decimal("1e-18")
    ),
    "0x3cc5eb07e0e1227613f1df58f38b549823d11cb9": TokenInfo(
        currency=CurrencyInfo(symbol="EER", name="Ethereum eRush"), scaling=Decimal("1e-18")
    ),
    "0x3ccb1fe6d628444fb1c823a3ee3573ed0a21f338": TokenInfo(
        currency=CurrencyInfo(symbol="BNTE", name="Bountie"), scaling=Decimal("1e-18")
    ),
    "0x3cf9e0c385a5abec9fd2a71790aa344c4e8e3570": TokenInfo(
        currency=CurrencyInfo(symbol="BKRX", name="BlockRx"), scaling=Decimal("1e-18")
    ),
    "0x3d193bd867d00439edcbd2b8f7684e5151bdad5a": TokenInfo(
        currency=CurrencyInfo(symbol="FP.CX", name="Total"), scaling=Decimal("1e-8")
    ),
    "0x3d1ba9be9f66b8ee101911bc36d3fb562eac2244": TokenInfo(
        currency=CurrencyInfo(symbol="RVT", name="Rivetz"), scaling=Decimal("1e-18")
    ),
    "0x3d207d98e762fb64e163abddcb25a913eeb741cd": TokenInfo(
        currency=CurrencyInfo(symbol="APT", name="Ad Pay Token"), scaling=Decimal("1e-18")
    ),
    "0x3d26dcd840fcc8e4b2193ace8a092e4a65832f9f": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNIUNIWETH", name="Aave AMM UniUNIWETH"), scaling=Decimal("1e-18")
    ),
    "0x3d3560279b7a4e57af202c285305d8f761ccb60a": TokenInfo(
        currency=CurrencyInfo(symbol="SFC", name="Silver Fabric Coin"), scaling=Decimal("1e-4")
    ),
    "0x3d371413dd5489f3a04c07c0c2ce369c20986ceb": TokenInfo(
        currency=CurrencyInfo(symbol="YOUC", name="YOUcash"), scaling=Decimal("1e-10")
    ),
    "0x3d3ab800d105fbd2f97102675a412da3dc934357": TokenInfo(
        currency=CurrencyInfo(symbol="MSV", name="Marvrodi Salute Vison"), scaling=Decimal("1e-18")
    ),
    "0x3d3d35bb9bec23b06ca00fe472b50e7a4c692c30": TokenInfo(
        currency=CurrencyInfo(symbol="VIDYA", name="Vidya"), scaling=Decimal("1e-18")
    ),
    "0x3d46454212c61ecb7b31248047fa033120b88668": TokenInfo(
        currency=CurrencyInfo(symbol="MVT", name="The Movement"), scaling=Decimal("1e-18")
    ),
    "0x3d61e677944204cd1002202912a2b7a43a8e2823": TokenInfo(
        currency=CurrencyInfo(symbol="USDF", name="New USDf"), scaling=Decimal("1e-9")
    ),
    "0x3d658390460295fb963f54dc0899cfb1c30776df": TokenInfo(
        currency=CurrencyInfo(symbol="COVAL", name="Circuits of Value"), scaling=Decimal("1e-8")
    ),
    "0x3d6826939286211d1e0e20351f669c642ff64d47": TokenInfo(
        currency=CurrencyInfo(symbol="NLOK.CX", name="Symantec Corp"), scaling=Decimal("1e-8")
    ),
    "0x3d6f0dea3ac3c607b3998e6ce14b6350721752d9": TokenInfo(
        currency=CurrencyInfo(symbol="CARDS", name="Cardstarter"), scaling=Decimal("1e-18")
    ),
    "0x3d90d2818cd6570e31ccc1db5e9fbd7289988173": TokenInfo(
        currency=CurrencyInfo(symbol="ICPT.CX", name="Intercept Pharmaceuticals Inc"), scaling=Decimal("1e-8")
    ),
    "0x3d995510f8d82c2ea341845932b5ddde0bead9a3": TokenInfo(
        currency=CurrencyInfo(symbol="UGAS-JAN21", name="uLABS synthetic Gas Futures Token"), scaling=Decimal("1e-18")
    ),
    "0x3d9ac8e7a9c9be11dfac1677dda901e28d44527f": TokenInfo(
        currency=CurrencyInfo(symbol="PAA", name="Palace"), scaling=Decimal("1e-8")
    ),
    "0x3db1678170418d1014012f855e2dda492f35c289": TokenInfo(
        currency=CurrencyInfo(symbol="ISP", name="ISHOP PLUS"), scaling=Decimal("1e-18")
    ),
    "0x3db6ba6ab6f95efed1a6e794cad492faaabf294d": TokenInfo(
        currency=CurrencyInfo(symbol="LTO", name="LTO Network"), scaling=Decimal("1e-8")
    ),
    "0x3db99ab08006aefcc9600972eca8c202396b4300": TokenInfo(
        currency=CurrencyInfo(symbol="VINCI", name="Vinci"), scaling=Decimal("1e-18")
    ),
    "0x3dc0501c32bee0cc1e629d590302a4b909797474": TokenInfo(
        currency=CurrencyInfo(symbol="TVND", name="TrueVND"), scaling=Decimal("1e-18")
    ),
    "0x3dc7b06dd0b1f08ef9acbbd2564f8605b4868eea": TokenInfo(
        currency=CurrencyInfo(symbol="SPACE", name="Space"), scaling=Decimal("1e-18")
    ),
    "0x3dc9a42fa7afe57be03c58fd7f4411b1e466c508": TokenInfo(
        currency=CurrencyInfo(symbol="CLL", name="Attention Mining"), scaling=Decimal("1e-18")
    ),
    "0x3dd12d935cfa82fbb4ede9523c552240f2058c0b": TokenInfo(
        currency=CurrencyInfo(symbol="PCOIN", name="Plumecoin"), scaling=Decimal("1e-18")
    ),
    "0x3dd66732113af9981a861cf489431533aeba33b8": TokenInfo(
        currency=CurrencyInfo(symbol="YFN", name="Yearn Finance Network"), scaling=Decimal("1e-18")
    ),
    "0x3dfeaf13a6615e560aecc5648ace8fa50d7cf6bf": TokenInfo(
        currency=CurrencyInfo(symbol="NTS", name="Nerthus"), scaling=Decimal("1e-12")
    ),
    "0x3e083d08ada591fe5356c52fbb89fe725fd9d670": TokenInfo(
        currency=CurrencyInfo(symbol="CTE", name="CryptoTrust Token"), scaling=Decimal("1e-0")
    ),
    "0x3e1d5a855ad9d948373ae68e4fe1f094612b1322": TokenInfo(
        currency=CurrencyInfo(symbol="HQT", name="HyperQuant"), scaling=Decimal("1e-18")
    ),
    "0x3e1e15afd5d50b090adcc88160dd84a48ea1b80e": TokenInfo(
        currency=CurrencyInfo(symbol="VSPY", name="vSPY"), scaling=Decimal("1e-18")
    ),
    "0x3e370a6c8255b065bd42bc0ac9255b269cfcc172": TokenInfo(
        currency=CurrencyInfo(symbol="UNI", name="Unipot"), scaling=Decimal("1e-8")
    ),
    "0x3e522d144814bd6149c1f3e0c6cd19d0941372ac": TokenInfo(
        currency=CurrencyInfo(symbol="GBK", name="Goldblock"), scaling=Decimal("1e-18")
    ),
    "0x3e65e1eefde5ea7ccfc9a9a1634abe90f32262f8": TokenInfo(
        currency=CurrencyInfo(symbol="BAAS", name="BaaSid"), scaling=Decimal("1e-18")
    ),
    "0x3e6941521c85c7233632bf76e3adb05db8e2f1db": TokenInfo(
        currency=CurrencyInfo(symbol="MFCK", name="MoFlux - Clash of Kings"), scaling=Decimal("1e-18")
    ),
    "0x3e780920601d61cedb860fe9c4a90c9ea6a35e78": TokenInfo(
        currency=CurrencyInfo(symbol="BOOST", name="Boosted Finance"), scaling=Decimal("1e-18")
    ),
    "0x3e991dbec296e00626e58c33b62e53bec9d54636": TokenInfo(
        currency=CurrencyInfo(symbol="USDL", name="USDL"), scaling=Decimal("1e-18")
    ),
    "0x3e9bc21c9b189c09df3ef1b824798658d5011937": TokenInfo(
        currency=CurrencyInfo(symbol="LINA", name="Linear"), scaling=Decimal("1e-18")
    ),
    "0x3e9e371f8d2e9fca315fb0a747533ced8a3fcbcb": TokenInfo(
        currency=CurrencyInfo(symbol="BIXCPRO", name="BIXCPRO"), scaling=Decimal("1e-4")
    ),
    "0x3ea8a7425eeb8c768489c91941b2ab1720a34515": TokenInfo(
        currency=CurrencyInfo(symbol="HCA.CX", name="HCA Healthcare"), scaling=Decimal("1e-8")
    ),
    "0x3ea8ea4237344c9931214796d9417af1a1180770": TokenInfo(
        currency=CurrencyInfo(symbol="FLX", name="Flux Token"), scaling=Decimal("1e-18")
    ),
    "0x3ea9fb5d766458e8eec3c2d6434e14c484d03db7": TokenInfo(
        currency=CurrencyInfo(symbol="NET.CX", name="Cloudflare Inc"), scaling=Decimal("1e-8")
    ),
    "0x3eb91d237e491e0dee8582c402d85cb440fb6b54": TokenInfo(
        currency=CurrencyInfo(symbol="S-ETH", name="Smartillions.ch-ETH"), scaling=Decimal("1e-18")
    ),
    "0x3ebb4a4e91ad83be51f8d596533818b246f4bee1": TokenInfo(
        currency=CurrencyInfo(symbol="SATA", name="Signata"), scaling=Decimal("1e-18")
    ),
    "0x3ec8798b81485a254928b70cda1cf0a2bb0b74d7": TokenInfo(
        currency=CurrencyInfo(symbol="GRO", name="Gro DAO Token"), scaling=Decimal("1e-18")
    ),
    "0x3ed3b47dd13ec9a98b44e6204a523e766b225811": TokenInfo(
        currency=CurrencyInfo(symbol="AUSDT", name="Aave USDT"), scaling=Decimal("1e-6")
    ),
    "0x3edd235c3e840c1f29286b2e39370a255c7b6fdb": TokenInfo(
        currency=CurrencyInfo(symbol="CMBT", name="CMB Token"), scaling=Decimal("1e-8")
    ),
    "0x3ee2fd8e38a16f06ab85d684e062c0cf7d0e9a8b": TokenInfo(
        currency=CurrencyInfo(symbol="EFT", name="EasyFeedback Token"), scaling=Decimal("1e-18")
    ),
    "0x3f06b5d78406cd97bdf10f5c420b241d32759c80": TokenInfo(
        currency=CurrencyInfo(symbol="CYFM", name="CYBERFM"), scaling=Decimal("1e-18")
    ),
    "0x3f09400313e83d53366147e3ea0e4e2279d80850": TokenInfo(
        currency=CurrencyInfo(symbol="KSEED", name="Kush Finance"), scaling=Decimal("1e-18")
    ),
    "0x3f17dd476faf0a4855572f0b6ed5115d9bba22ad": TokenInfo(
        currency=CurrencyInfo(symbol="WIB", name="WIBSON"), scaling=Decimal("1e-9")
    ),
    "0x3f1844917418cade330f938093cf6f23f0ed5093": TokenInfo(
        currency=CurrencyInfo(symbol="LYFT.CX", name="LYFT"), scaling=Decimal("1e-8")
    ),
    "0x3f2b9e1ae008aa43e68b882f8d0440d25432c7e4": TokenInfo(
        currency=CurrencyInfo(symbol="WIAC", name="WaldenGoton International Asset Chain"), scaling=Decimal("1e-18")
    ),
    "0x3f2d8861e8ca9a7649d211dbaa3f3d998c6a254a": TokenInfo(
        currency=CurrencyInfo(symbol="BLCC", name="Bullers Coin"), scaling=Decimal("1e-18")
    ),
    "0x3f344c88d823f180fb8b44a3c7cfc4edc92dfa35": TokenInfo(
        currency=CurrencyInfo(symbol="DSWAP", name="Definex"), scaling=Decimal("1e-6")
    ),
    "0x3f382dbd960e3a9bbceae22651e88158d2791550": TokenInfo(
        currency=CurrencyInfo(symbol="GHST", name="Aavegotchi"), scaling=Decimal("1e-18")
    ),
    "0x3f4b726668da46f5e0e75aa5d478acec9f38210f": TokenInfo(
        currency=CurrencyInfo(symbol="M-ETH", name="MostExclusive.com-ETH"), scaling=Decimal("1e-18")
    ),
    "0x3f5b26b0fa3e9d8547b7cf6725871f96ee91313a": TokenInfo(
        currency=CurrencyInfo(symbol="SCOI", name="SprinkleCoin"), scaling=Decimal("1e-18")
    ),
    "0x3f63e135346c97bc1b3388ba7f1185af7d5df0e6": TokenInfo(
        currency=CurrencyInfo(symbol="TFX.CX", name="Teleflex"), scaling=Decimal("1e-8")
    ),
    "0x3f84c4184b35c488f7fe4a12469610c9b1cb03c9": TokenInfo(
        currency=CurrencyInfo(symbol="PSK", name="PoolStake"), scaling=Decimal("1e-18")
    ),
    "0x3f8a2f7bcd70e7f7bdd3fbb079c11d073588dea2": TokenInfo(
        currency=CurrencyInfo(symbol="FIRE", name="FIRE"), scaling=Decimal("1e-18")
    ),
    "0x3fa400483487a489ec9b1db29c4129063eec4654": TokenInfo(
        currency=CurrencyInfo(symbol="KEK", name="CryptoKek"), scaling=Decimal("1e-18")
    ),
    "0x3fa729b4548becbad4eab6ef18413470e6d5324c": TokenInfo(
        currency=CurrencyInfo(symbol="MOVE", name="Mover"), scaling=Decimal("1e-18")
    ),
    "0x3fb8d8a28aff053ccf446bc075eecb7a0ef65d0c": TokenInfo(
        currency=CurrencyInfo(symbol="STPC", name="StarPlay"), scaling=Decimal("1e-18")
    ),
    "0x3fd2e747cea0e8a78f1827ea2ffd3334628a600b": TokenInfo(
        currency=CurrencyInfo(symbol="LIB", name="Banklife"), scaling=Decimal("1e-18")
    ),
    "0x3fd8f39a962efda04956981c31ab89fab5fb8bc8": TokenInfo(
        currency=CurrencyInfo(symbol="RTH", name="Rotharium"), scaling=Decimal("1e-18")
    ),
    "0x3fe2ef1dfb1595195768627d16751d552586dce8": TokenInfo(
        currency=CurrencyInfo(symbol="OPA", name="OptaToken"), scaling=Decimal("1e-10")
    ),
    "0x3fe856e55c4076682400f23d6be7dd737ee7e947": TokenInfo(
        currency=CurrencyInfo(symbol="NAER", name="Naer Chain"), scaling=Decimal("1e-8")
    ),
    "0x3ff9cebbeaa7bcc48a952a011a02a22a1fdd1c62": TokenInfo(
        currency=CurrencyInfo(symbol="OR", name="ORDER"), scaling=Decimal("1e-18")
    ),
    "0x40284109c3309a7c3439111bfd93bf5e0fbb706c": TokenInfo(
        currency=CurrencyInfo(symbol="MOV", name="MOTIV Protocol"), scaling=Decimal("1e-18")
    ),
    "0x40395044ac3c0c57051906da938b54bd6557f212": TokenInfo(
        currency=CurrencyInfo(symbol="MGO", name="MobileGo"), scaling=Decimal("1e-8")
    ),
    "0x403d512ab96103562dcafe4635545e8ee2753f6e": TokenInfo(
        currency=CurrencyInfo(symbol="WILD", name="Wild Credit"), scaling=Decimal("1e-18")
    ),
    "0x405dd8fca636282ab5ee47b88036a7256fd29b31": TokenInfo(
        currency=CurrencyInfo(symbol="NDIO", name="NDIO"), scaling=Decimal("1e-18")
    ),
    "0x406ab55c0bab2d4a3361f87f251211c3090d80bc": TokenInfo(
        currency=CurrencyInfo(symbol="ECDF", name="EasyCoinDigitalFreedom"), scaling=Decimal("1e-18")
    ),
    "0x406ae253fb0aa898f9912fb192c1e6deb9623a07": TokenInfo(
        currency=CurrencyInfo(symbol="TOROCUS", name="TOROCUS Token"), scaling=Decimal("1e-18")
    ),
    "0x40803cea2b2a32bda1be61d3604af6a814e70976": TokenInfo(
        currency=CurrencyInfo(symbol="SPOOL", name="Spool DAO Token"), scaling=Decimal("1e-18")
    ),
    "0x40821cd074dfecb1524286923bc69315075b5c89": TokenInfo(
        currency=CurrencyInfo(symbol="QUAI", name="Quai Dao"), scaling=Decimal("1e-18")
    ),
    "0x4086692d53262b2be0b13909d804f0491ff6ec3e": TokenInfo(
        currency=CurrencyInfo(symbol="YFKA", name="Yield Farming Known as Ash"), scaling=Decimal("1e-18")
    ),
    "0x408ceb38c21826d25e1ebc8a6588a38b836b19a9": TokenInfo(
        currency=CurrencyInfo(symbol="MC.CX", name="Lvmh Moet Hennessy Louis Vuitton Se"), scaling=Decimal("1e-8")
    ),
    "0x408e41876cccdc0f92210600ef50372656052a38": TokenInfo(
        currency=CurrencyInfo(symbol="REN", name="REN"), scaling=Decimal("1e-18")
    ),
    "0x4092678e4e78230f46a1534c0fbc8fa39780892b": TokenInfo(
        currency=CurrencyInfo(symbol="OCN", name="Odyssey"), scaling=Decimal("1e-18")
    ),
    "0x40b5ccf92f9c980fbc6f2f0c0af7a4afff0f7c48": TokenInfo(
        currency=CurrencyInfo(symbol="FIDE", name="FidelityToken"), scaling=Decimal("1e-18")
    ),
    "0x40b92fce37cefa03baf7603e7913c1d34dd1a4ec": TokenInfo(
        currency=CurrencyInfo(symbol="YEA", name="YeaFinance"), scaling=Decimal("1e-8")
    ),
    "0x40c6f861a08f97dfbc3c0931485bff4921975a56": TokenInfo(
        currency=CurrencyInfo(symbol="HGH", name="HGH Token"), scaling=Decimal("1e-18")
    ),
    "0x40c836982788dca47d11024b1fa3e01fd4661766": TokenInfo(
        currency=CurrencyInfo(symbol="BNX", name="BTCNEXT Coin"), scaling=Decimal("1e-18")
    ),
    "0x40ce0a1d8f4999807b92ec266a025f071814b15d": TokenInfo(
        currency=CurrencyInfo(symbol="NOTRUMP", name="Dai If Trump Loses The 2020 Election"), scaling=Decimal("1e-18")
    ),
    "0x40d52577830e01aaefa80659aa90ee8b34685f4e": TokenInfo(
        currency=CurrencyInfo(symbol="BIA", name="Bilaxy Token"), scaling=Decimal("1e-18")
    ),
    "0x40fd72257597aa14c7231a7b1aaa29fce868f677": TokenInfo(
        currency=CurrencyInfo(symbol="XOR", name="Sora"), scaling=Decimal("1e-18")
    ),
    "0x4104b135dbc9609fc1a9490e61369036497660c8": TokenInfo(
        currency=CurrencyInfo(symbol="APW", name="APWine"), scaling=Decimal("1e-18")
    ),
    "0x410e731c2970dce3add351064acf5ce9e33fdbf0": TokenInfo(
        currency=CurrencyInfo(symbol="ONIT", name="ONBUFF"), scaling=Decimal("1e-18")
    ),
    "0x4123a133ae3c521fd134d7b13a2dec35b56c2463": TokenInfo(
        currency=CurrencyInfo(symbol="QRDO", name="Qredo"), scaling=Decimal("1e-8")
    ),
    "0x41523a22144f3d129dddf1e9a549333148d0c37d": TokenInfo(
        currency=CurrencyInfo(symbol="COZOM", name="CryptoPunk #3831 Shards"), scaling=Decimal("1e-18")
    ),
    "0x4156d3342d5c385a87d264f90653733592000581": TokenInfo(
        currency=CurrencyInfo(symbol="SALT", name="SALT"), scaling=Decimal("1e-8")
    ),
    "0x415f07c7c57b1a213767ed8e3eb4b321fa04bb7c": TokenInfo(
        currency=CurrencyInfo(symbol="GHC", name="GameHub"), scaling=Decimal("1e-6")
    ),
    "0x4161725d019690a3e0de50f6be67b07a86a9fae1": TokenInfo(
        currency=CurrencyInfo(symbol="TPT", name="Token Pocket"), scaling=Decimal("1e-4")
    ),
    "0x4162178b78d6985480a308b2190ee5517460406d": TokenInfo(
        currency=CurrencyInfo(symbol="CLN", name="Colu Local Network"), scaling=Decimal("1e-18")
    ),
    "0x417d6feeae8b2fcb73d14d64be7f192e49431978": TokenInfo(
        currency=CurrencyInfo(symbol="SKILL", name="Skillcoin"), scaling=Decimal("1e-18")
    ),
    "0x4185cf99745b2a20727b37ee798193dd4a56cdfa": TokenInfo(
        currency=CurrencyInfo(symbol="WCOINBASE-IOU", name="DEUS Synthetic Coinbase IOU"), scaling=Decimal("1e-18")
    ),
    "0x41875c2332b0877cdfaa699b641402b7d4642c32": TokenInfo(
        currency=CurrencyInfo(symbol="FTXT", name="FUTURAX"), scaling=Decimal("1e-8")
    ),
    "0x419b8ed155180a8c9c64145e76dad49c0a4efb97": TokenInfo(
        currency=CurrencyInfo(symbol="ALT", name="AltEstate Token"), scaling=Decimal("1e-18")
    ),
    "0x419c4db4b9e25d6db2ad9691ccb832c8d9fda05e": TokenInfo(
        currency=CurrencyInfo(symbol="DRGN", name="Dragonchain"), scaling=Decimal("1e-18")
    ),
    "0x419d0d8bdd9af5e606ae2232ed285aff190e711b": TokenInfo(
        currency=CurrencyInfo(symbol="FUN", name="FUNToken"), scaling=Decimal("1e-8")
    ),
    "0x41a03e41ef555392c9f0ad60f4f61e263078bf10": TokenInfo(
        currency=CurrencyInfo(symbol="USDU", name="Upper Dollar"), scaling=Decimal("1e-18")
    ),
    "0x41a3dba3d677e573636ba691a70ff2d606c29666": TokenInfo(
        currency=CurrencyInfo(symbol="BLANK", name="Blank"), scaling=Decimal("1e-18")
    ),
    "0x41ab1b6fcbb2fa9dced81acbdec13ea6315f2bf2": TokenInfo(
        currency=CurrencyInfo(symbol="XDCE", name="XinFin XDCE"), scaling=Decimal("1e-18")
    ),
    "0x41ab75435668919bb507f871dd01e9762c2d173a": TokenInfo(
        currency=CurrencyInfo(symbol="NXCT", name="XChain Token"), scaling=Decimal("1e-18")
    ),
    "0x41ad4093349c8a60de591a3c37dcd184558eaae3": TokenInfo(
        currency=CurrencyInfo(symbol="BITN", name="Bitcoin and Company Network"), scaling=Decimal("1e-18")
    ),
    "0x41b3f18c6384dc9a39c33afeca60d9b8e61eaa9f": TokenInfo(
        currency=CurrencyInfo(symbol="NOAHP", name="Noah Decentralized State Coin"), scaling=Decimal("1e-18")
    ),
    "0x41bbcf4f8f0e8a0a3cce4287d1c0c3d27c65ba0d": TokenInfo(
        currency=CurrencyInfo(symbol="MALL", name="MBC Block"), scaling=Decimal("1e-18")
    ),
    "0x41bbedd7286daab5910a1f15d12cbda839852bd7": TokenInfo(
        currency=CurrencyInfo(symbol="MMSFT", name="Mirrored Microsoft"), scaling=Decimal("1e-18")
    ),
    "0x41bc0913ed789428e107c4ea9ed007815c5a8230": TokenInfo(
        currency=CurrencyInfo(symbol="KOMP", name="Kompass"), scaling=Decimal("1e-18")
    ),
    "0x41d3cee04b3e6a00d506309ba6008f7add1bc94e": TokenInfo(
        currency=CurrencyInfo(symbol="YSDT", name="YSDT"), scaling=Decimal("1e-8")
    ),
    "0x41d5d79431a913c4ae7d69a668ecdfe5ff9dfb68": TokenInfo(
        currency=CurrencyInfo(symbol="INV", name="Inverse Finance"), scaling=Decimal("1e-18")
    ),
    "0x41dbecc1cdc5517c6f76f6a6e836adbee2754de3": TokenInfo(
        currency=CurrencyInfo(symbol="MTN", name="Medicalchain"), scaling=Decimal("1e-18")
    ),
    "0x41e5560054824ea6b0732e656e3ad64e20e94e45": TokenInfo(
        currency=CurrencyInfo(symbol="CVC", name="Civic"), scaling=Decimal("1e-8")
    ),
    "0x41efc0253ee7ea44400abb5f907fdbfdebc82bec": TokenInfo(
        currency=CurrencyInfo(symbol="$AAPL", name="$AAPL"), scaling=Decimal("1e-18")
    ),
    "0x41f3b2b6d4d122e81834582a3f3367388def95cf": TokenInfo(
        currency=CurrencyInfo(symbol="MFSN", name="MoFlux - Safety Net Set"), scaling=Decimal("1e-18")
    ),
    "0x41f723448433367be140d528d35efecd3e023db6": TokenInfo(
        currency=CurrencyInfo(symbol="FARM", name="Farm Partner"), scaling=Decimal("1e-18")
    ),
    "0x420167d87d35c3a249b32ef6225872fbd9ab85d2": TokenInfo(
        currency=CurrencyInfo(symbol="MESG", name="MESG"), scaling=Decimal("1e-18")
    ),
    "0x4206931337dc273a630d328da6441786bfad668f": TokenInfo(
        currency=CurrencyInfo(symbol="DOGE", name="DOGE"), scaling=Decimal("1e-8")
    ),
    "0x420ab548b18911717ed7c4ccbf46371ea758458c": TokenInfo(
        currency=CurrencyInfo(symbol="NOODLE", name="NOODLE.Finance"), scaling=Decimal("1e-18")
    ),
    "0x421291c62344278642a1ea917cdca23effd01416": TokenInfo(
        currency=CurrencyInfo(symbol="MB", name="My BabyPet Chain"), scaling=Decimal("1e-2")
    ),
    "0x4212fea9fec90236ecc51e41e2096b16ceb84555": TokenInfo(
        currency=CurrencyInfo(symbol="SDC", name="SDChain"), scaling=Decimal("1e-18")
    ),
    "0x422866a8f0b032c5cf1dfbdef31a20f4509562b0": TokenInfo(
        currency=CurrencyInfo(symbol="ADST", name="Adshares Token"), scaling=Decimal("1e-0")
    ),
    "0x4234f63b1d202f6c016ca3b6a0d41d7d85f17716": TokenInfo(
        currency=CurrencyInfo(symbol="QNTU", name="Quanta"), scaling=Decimal("1e-18")
    ),
    "0x42382f39e7c9f1add5fa5f0c6e24aa62f50be3b3": TokenInfo(
        currency=CurrencyInfo(symbol="ZOM", name="ZOM"), scaling=Decimal("1e-18")
    ),
    "0x423b5f62b328d0d6d44870f4eee316befa0b2df5": TokenInfo(
        currency=CurrencyInfo(symbol="GOT", name="GoNetwork"), scaling=Decimal("1e-18")
    ),
    "0x423e4322cdda29156b49a17dfbd2acc4b280600d": TokenInfo(
        currency=CurrencyInfo(symbol="CARS", name="Car Sharing"), scaling=Decimal("1e-9")
    ),
    "0x42476f744292107e34519f9c357927074ea3f75d": TokenInfo(
        currency=CurrencyInfo(symbol="LOOM", name="Loom Network (NEW)"), scaling=Decimal("1e-18")
    ),
    "0x42566cfefc853c232117eba4413e45782a72715d": TokenInfo(
        currency=CurrencyInfo(symbol="KRI", name="Krios"), scaling=Decimal("1e-18")
    ),
    "0x4257d36df231dc71f7b7a6e1be3ef9c99b9181fd": TokenInfo(
        currency=CurrencyInfo(symbol="SST", name="SuperStar"), scaling=Decimal("1e-8")
    ),
    "0x426567f78e74577f8a6233b635970eb729631e05": TokenInfo(
        currency=CurrencyInfo(symbol="STR", name="Staker Token"), scaling=Decimal("1e-18")
    ),
    "0x426ca1ea2406c07d75db9585f22781c096e3d0e0": TokenInfo(
        currency=CurrencyInfo(symbol="MNE", name="Minereum"), scaling=Decimal("1e-8")
    ),
    "0x426fc8be95573230f6e6bc4af91873f0c67b21b4": TokenInfo(
        currency=CurrencyInfo(symbol="BPLC", name="BlackPearl Token"), scaling=Decimal("1e-18")
    ),
    "0x4270bb238f6dd8b1c3ca01f96ca65b2647c06d3c": TokenInfo(
        currency=CurrencyInfo(symbol="FOTA", name="Fortuna"), scaling=Decimal("1e-18")
    ),
    "0x42726d074bba68ccc15200442b72afa2d495a783": TokenInfo(
        currency=CurrencyInfo(symbol="ISIKC", name="Isiklar Coin"), scaling=Decimal("1e-4")
    ),
    "0x42740698959761baf1b06baa51efbd88cb1d862b": TokenInfo(
        currency=CurrencyInfo(symbol="idleUSDTSafe", name="IdleUSDT v3 [Risk Adjusted]"), scaling=Decimal("1e-18")
    ),
    "0x4289c043a12392f1027307fb58272d8ebd853912": TokenInfo(
        currency=CurrencyInfo(symbol="ALI", name="AiLink Token"), scaling=Decimal("1e-18")
    ),
    "0x428d941e0a014bb5cdeb09bb00bc7b245221bdb0": TokenInfo(
        currency=CurrencyInfo(symbol="LVE", name="LVECoin"), scaling=Decimal("1e-18")
    ),
    "0x428dc22668e6f3468273634067e5545ed5417a3e": TokenInfo(
        currency=CurrencyInfo(symbol="MQL", name="MiraQle"), scaling=Decimal("1e-18")
    ),
    "0x4290563c2d7c255b5eec87f2d3bd10389f991d68": TokenInfo(
        currency=CurrencyInfo(symbol="UIP", name="UnlimitedIP"), scaling=Decimal("1e-18")
    ),
    "0x4297394c20800e8a38a619a243e9bbe7681ff24e": TokenInfo(
        currency=CurrencyInfo(symbol="HOTCROSS", name="Hot Cross"), scaling=Decimal("1e-18")
    ),
    "0x429881672b9ae42b8eba0e26cd9c73711b891ca5": TokenInfo(
        currency=CurrencyInfo(symbol="PICKLE", name="Pickle Finance"), scaling=Decimal("1e-18")
    ),
    "0x429d83bb0dcb8cdd5311e34680adc8b12070a07f": TokenInfo(
        currency=CurrencyInfo(symbol="PLTC", name="PlatonCoin"), scaling=Decimal("1e-18")
    ),
    "0x42bbfa2e77757c645eeaad1655e0911a7553efbc": TokenInfo(
        currency=CurrencyInfo(symbol="BOBA", name="Boba Network"), scaling=Decimal("1e-18")
    ),
    "0x42bedd647e387dabec65a7dc3a3babcc68bb664d": TokenInfo(
        currency=CurrencyInfo(symbol="BLINK", name="BlockMason Link"), scaling=Decimal("1e-18")
    ),
    "0x42d6622dece394b54999fbd73d108123806f6a18": TokenInfo(
        currency=CurrencyInfo(symbol="SPANK", name="SpankChain"), scaling=Decimal("1e-18")
    ),
    "0x430241368c1d293fda21dba8bb7af32007c59109": TokenInfo(
        currency=CurrencyInfo(symbol="3LT", name="TrillionToken"), scaling=Decimal("1e-8")
    ),
    "0x43044f861ec040db59a7e324c40507addb673142": TokenInfo(
        currency=CurrencyInfo(symbol="CAP", name="Cap"), scaling=Decimal("1e-18")
    ),
    "0x430aca35d154fa19b0a679044241cddbf89b1c90": TokenInfo(
        currency=CurrencyInfo(symbol="UBER.CX", name="Uber Technologies Inc"), scaling=Decimal("1e-8")
    ),
    "0x430bd07726423a54f6d82ab0f578ce62a3b8054d": TokenInfo(
        currency=CurrencyInfo(symbol="UOS", name="U°OS Network"), scaling=Decimal("1e-4")
    ),
    "0x430ef9263e76dae63c84292c3409d61c598e9682": TokenInfo(
        currency=CurrencyInfo(symbol="PYR", name="Vulcan Forged"), scaling=Decimal("1e-18")
    ),
    "0x430fee8ea3df2a9a34fa6621dac5a9d5ccac355a": TokenInfo(
        currency=CurrencyInfo(symbol="CTIC3", name="Coimatic 3.0"), scaling=Decimal("1e-18")
    ),
    "0x43110d4f2113d50574412e852ebd96f1593179e4": TokenInfo(
        currency=CurrencyInfo(symbol="ADA", name="ADA"), scaling=Decimal("1e-4")
    ),
    "0x431ad2ff6a9c365805ebad47ee021148d6f7dbe0": TokenInfo(
        currency=CurrencyInfo(symbol="DF", name="dForce Token"), scaling=Decimal("1e-18")
    ),
    "0x432bf73443909c33b545efed536a5246c9a722ca": TokenInfo(
        currency=CurrencyInfo(symbol="PEC", name="Poverty Eradication Coin"), scaling=Decimal("1e-18")
    ),
    "0x4355fc160f74328f9b383df2ec589bb3dfd82ba0": TokenInfo(
        currency=CurrencyInfo(symbol="OPT", name="Opus"), scaling=Decimal("1e-18")
    ),
    "0x43567eb78638a55bbe51e9f9fb5b2d7ad1f125aa": TokenInfo(
        currency=CurrencyInfo(symbol="HAC", name="Hackspace Capital"), scaling=Decimal("1e-4")
    ),
    "0x435d664f72d6f194ef67d63b5f3936650187b131": TokenInfo(
        currency=CurrencyInfo(symbol="NODE", name="Pocket Node"), scaling=Decimal("1e-18")
    ),
    "0x4360c56dcb5a549531971433cac8e7d0e68d19e1": TokenInfo(
        currency=CurrencyInfo(symbol="SDC", name="SDCOIN"), scaling=Decimal("1e-18")
    ),
    "0x4363e1485764d206b01ddc9ca121030585259f6f": TokenInfo(
        currency=CurrencyInfo(symbol="ADDR", name="Address"), scaling=Decimal("1e-18")
    ),
    "0x43688910273f199b8ae2ca018c13918fb3d37b58": TokenInfo(
        currency=CurrencyInfo(
            symbol="REALTOKEN-5942-AUDUBON-RD-DETROIT-MI", name="RealToken 5942 Audubon Road Detroit MI"
        ),
        scaling=Decimal("1e-18"),
    ),
    "0x436f0f3a982074c4a05084485d421466a994fe53": TokenInfo(
        currency=CurrencyInfo(symbol="RTE", name="Rate3"), scaling=Decimal("1e-18")
    ),
    "0x4375e7ad8a01b8ec3ed041399f62d9cd120e0063": TokenInfo(
        currency=CurrencyInfo(symbol="BZ", name="BitZ Token"), scaling=Decimal("1e-18")
    ),
    "0x43a96962254855f16b925556f9e97be436a43448": TokenInfo(
        currency=CurrencyInfo(symbol="HORD", name="Hord"), scaling=Decimal("1e-18")
    ),
    "0x43de1145cd22f0a9cc99e51c205e6e81161df6b9": TokenInfo(
        currency=CurrencyInfo(symbol="ADABULL", name="3X Long Cardano Token"), scaling=Decimal("1e-18")
    ),
    "0x43dfc4159d86f3a37a5a4b3d4580b888ad7d4ddd": TokenInfo(
        currency=CurrencyInfo(symbol="DODO", name="DODO"), scaling=Decimal("1e-18")
    ),
    "0x43e577338d6c07bc92a06c8ca4b781470515dfa8": TokenInfo(
        currency=CurrencyInfo(symbol="OBC", name="Oblichain"), scaling=Decimal("1e-18")
    ),
    "0x43e5f59247b235449e16ec84c46ba43991ef6093": TokenInfo(
        currency=CurrencyInfo(symbol="CBI", name="Coin Bank International"), scaling=Decimal("1e-18")
    ),
    "0x43f6a1be992dee408721748490772b15143ce0a7": TokenInfo(
        currency=CurrencyInfo(symbol="POIN", name="Potatoin"), scaling=Decimal("1e-0")
    ),
    "0x44086035439e676c02d411880fccb9837ce37c57": TokenInfo(
        currency=CurrencyInfo(symbol="USD", name="unified Stable Dollar"), scaling=Decimal("1e-18")
    ),
    "0x441761326490cacf7af299725b6292597ee822c2": TokenInfo(
        currency=CurrencyInfo(symbol="UNFI", name="Unifi Protocol DAO"), scaling=Decimal("1e-18")
    ),
    "0x44197a4c44d6a059297caf6be4f7e172bd56caaf": TokenInfo(
        currency=CurrencyInfo(symbol="ELTCOIN", name="Eltcoin"), scaling=Decimal("1e-8")
    ),
    "0x442bc47357919446eabc18c7211e57a13d983469": TokenInfo(
        currency=CurrencyInfo(symbol="CHAT", name="BeeChat"), scaling=Decimal("1e-18")
    ),
    "0x442be638c626a77eb5d86c0fa2b441ba1cc97f3a": TokenInfo(
        currency=CurrencyInfo(symbol="FWC", name="Future World VR"), scaling=Decimal("1e-18")
    ),
    "0x442d985efebc633b8bfd14ff99e860a5609a6484": TokenInfo(
        currency=CurrencyInfo(symbol="EVO", name="Ethavo"), scaling=Decimal("1e-18")
    ),
    "0x4441306a9a611fd6c6305dbf5182466655942cd6": TokenInfo(
        currency=CurrencyInfo(symbol="NDA.CX", name="Aurubis AG"), scaling=Decimal("1e-8")
    ),
    "0x44449fa4d607f807d1ed4a69ad942971728391c8": TokenInfo(
        currency=CurrencyInfo(symbol="XMCT", name="XMED Chain Token"), scaling=Decimal("1e-18")
    ),
    "0x444997b7e7fc830e20089afea3078cd518fcf2a2": TokenInfo(
        currency=CurrencyInfo(symbol="EWO", name="EWO Token"), scaling=Decimal("1e-18")
    ),
    "0x4457dc5a9e71b975a8e0f855bbe795f5cbdcc10f": TokenInfo(
        currency=CurrencyInfo(symbol="VAIP", name="VEHICLE DATA ARTIFICIAL INTELLIGENCE PLATFORM"),
        scaling=Decimal("1e-18"),
    ),
    "0x445f51299ef3307dbd75036dd896565f5b4bf7a5": TokenInfo(
        currency=CurrencyInfo(symbol="VIDT", name="V-ID Token"), scaling=Decimal("1e-18")
    ),
    "0x446c9033e7516d820cc9a2ce2d0b7328b579406f": TokenInfo(
        currency=CurrencyInfo(symbol="SOLVE", name="SOLVE"), scaling=Decimal("1e-8")
    ),
    "0x44709a920fccf795fbc57baa433cc3dd53c44dbe": TokenInfo(
        currency=CurrencyInfo(symbol="RADAR", name="DappRadar"), scaling=Decimal("1e-18")
    ),
    "0x4470bb87d77b963a013db939be332f927f2b992e": TokenInfo(
        currency=CurrencyInfo(symbol="ADX", name="AdEx"), scaling=Decimal("1e-4")
    ),
    "0x4485561db76614ff727f8e0a3ea95690b8b16022": TokenInfo(
        currency=CurrencyInfo(symbol="INVOX", name="Invox Finance Token"), scaling=Decimal("1e-18")
    ),
    "0x448a47359833b26e5aa988ddb7a72099f6242170": TokenInfo(
        currency=CurrencyInfo(symbol="RIT", name="Real Estate Investment Token"), scaling=Decimal("1e-18")
    ),
    "0x449c640b6c7fce4f8ad2e3dcd900d13be40174af": TokenInfo(
        currency=CurrencyInfo(symbol="IGI", name="IGICOIN"), scaling=Decimal("1e-18")
    ),
    "0x449efe48ad7cd423bab056276639f8120cd4f9a3": TokenInfo(
        currency=CurrencyInfo(symbol="LIBREF", name="LibreFreelencer"), scaling=Decimal("1e-18")
    ),
    "0x44a41d8fec3877297edc40122f3de783861cd9af": TokenInfo(
        currency=CurrencyInfo(symbol="IST", name="Intelligent Strategic Transaction"), scaling=Decimal("1e-8")
    ),
    "0x44a67c8570a61a28bafd0035042f2f0a73a64428": TokenInfo(
        currency=CurrencyInfo(symbol="GCX", name="GermanCoin"), scaling=Decimal("1e-6")
    ),
    "0x44b6e3e85561ce054ab13affa0773358d795d36d": TokenInfo(
        currency=CurrencyInfo(symbol="ARTE", name="ethArt"), scaling=Decimal("1e-18")
    ),
    "0x44bf22949f9cc84b61b9328a9d885d1b5c806b41": TokenInfo(
        currency=CurrencyInfo(symbol="MOZO", name="Mozo Token"), scaling=Decimal("1e-2")
    ),
    "0x44e28f2acc84c36373badcd681749d38e01e2cc4": TokenInfo(
        currency=CurrencyInfo(symbol="VSPACEX", name="vSpaceX"), scaling=Decimal("1e-18")
    ),
    "0x44e2ca91cea1147f1b503e669f06cd11fb0c5490": TokenInfo(
        currency=CurrencyInfo(symbol="XCM", name="CoinMetro Token"), scaling=Decimal("1e-18")
    ),
    "0x44e4963f9012e7a7aeee05b7f2caae3419557aea": TokenInfo(
        currency=CurrencyInfo(symbol="AIPE", name="AI Prediction Ecosystem"), scaling=Decimal("1e-18")
    ),
    "0x44e9ab4a3af1ccc8c1cfce6fc7d3e650373fc507": TokenInfo(
        currency=CurrencyInfo(symbol="CNAB", name="Cannabium"), scaling=Decimal("1e-18")
    ),
    "0x44ea84a85616f8e9cd719fc843de31d852ad7240": TokenInfo(
        currency=CurrencyInfo(symbol="NTRUMP", name="NO Trump Augur Prediction Token"), scaling=Decimal("1e-15")
    ),
    "0x44f00918a540774b422a1a340b75e055ff816d83": TokenInfo(
        currency=CurrencyInfo(symbol="HXY", name="HEX Money"), scaling=Decimal("1e-8")
    ),
    "0x44f262622248027f8e2a8fb1090c4cf85072392c": TokenInfo(
        currency=CurrencyInfo(symbol="XIV", name="Project Inverse"), scaling=Decimal("1e-18")
    ),
    "0x44f588aeeb8c44471439d1270b3603c66a9262f1": TokenInfo(
        currency=CurrencyInfo(symbol="SNIP", name="SnipCoin"), scaling=Decimal("1e-18")
    ),
    "0x44fd55aeb7420b4fd275e19d6f0674a6f91ad356": TokenInfo(
        currency=CurrencyInfo(symbol="LIQ", name="Liquidity Bot Token"), scaling=Decimal("1e-8")
    ),
    "0x45088e0838d1d55491ebea1b2648f6f5f378aaf1": TokenInfo(
        currency=CurrencyInfo(symbol="TUG", name="TRUSTGRID"), scaling=Decimal("1e-8")
    ),
    "0x45245bc59219eeaaf6cd3f382e078a461ff9de7b": TokenInfo(
        currency=CurrencyInfo(symbol="BKX", name="BANKEX"), scaling=Decimal("1e-18")
    ),
    "0x4527a3b4a8a150403090a99b87effc96f2195047": TokenInfo(
        currency=CurrencyInfo(symbol="P2PS", name="P2P solutions foundation"), scaling=Decimal("1e-8")
    ),
    "0x4534492034a2cd3eab34c8f357cd139c95b09f52": TokenInfo(
        currency=CurrencyInfo(symbol="MLGC", name="Marshal Lion Group Coin"), scaling=Decimal("1e-0")
    ),
    "0x4545750f39af6be4f237b6869d4ecca928fd5a85": TokenInfo(
        currency=CurrencyInfo(symbol="CTF", name="Cyrptotaskz"), scaling=Decimal("1e-18")
    ),
    "0x454b9f249bc1492ee995793bbc3e57b830f1a5e9": TokenInfo(
        currency=CurrencyInfo(symbol="ALP", name="Alphacon"), scaling=Decimal("1e-18")
    ),
    "0x454cb9d0845bb4a28462f98c21a4fafd16ceb25f": TokenInfo(
        currency=CurrencyInfo(symbol="YLAB", name="Yearn-finance Infrastructure Labs"), scaling=Decimal("1e-18")
    ),
    "0x45526c392009cf7020ac10a10c1979e340a8a9dc": TokenInfo(
        currency=CurrencyInfo(symbol="XRPGSW", name="Ripple Gold Token SW"), scaling=Decimal("1e-8")
    ),
    "0x456ae45c0ce901e2e7c99c0718031cec0a7a59ff": TokenInfo(
        currency=CurrencyInfo(symbol="VSN", name="Vision Network"), scaling=Decimal("1e-18")
    ),
    "0x456bd836910b3853dc22529dbc2cbe072d967141": TokenInfo(
        currency=CurrencyInfo(symbol="EXCHMOON", name="10X Long Exchange Token Index Token"), scaling=Decimal("1e-18")
    ),
    "0x4575f41308ec1483f3d399aa9a2826d74da13deb": TokenInfo(
        currency=CurrencyInfo(symbol="OXT", name="Orchid Protocol"), scaling=Decimal("1e-18")
    ),
    "0x45804880de22913dafe09f4980848ece6ecbaf78": TokenInfo(
        currency=CurrencyInfo(symbol="PAXG", name="PAX Gold"), scaling=Decimal("1e-18")
    ),
    "0x4588c3c165a5c66c020997d89c2162814aec9cd6": TokenInfo(
        currency=CurrencyInfo(symbol="BTCWH", name="Bitcoin Wheelchair"), scaling=Decimal("1e-8")
    ),
    "0x459086f2376525bdceba5bdda135e4e9d3fef5bf": TokenInfo(
        currency=CurrencyInfo(symbol="RENBCH", name="renBCH"), scaling=Decimal("1e-8")
    ),
    "0x45af324f53a8d7da1752dad74adc1748126d7978": TokenInfo(
        currency=CurrencyInfo(symbol="MYTV", name="MyTVchain"), scaling=Decimal("1e-18")
    ),
    "0x45d0251bc82b0d383006ca536fc580db113eb4d7": TokenInfo(
        currency=CurrencyInfo(symbol="SKEIN", name="Skein"), scaling=Decimal("1e-18")
    ),
    "0x45d0bdfdfbfd62e14b64b0ea67dc6eac75f95d4d": TokenInfo(
        currency=CurrencyInfo(symbol="ELT", name="Ethereum Lendo Token"), scaling=Decimal("1e-8")
    ),
    "0x45e42d659d9f9466cd5df622506033145a9b89bc": TokenInfo(
        currency=CurrencyInfo(symbol="NXC", name="Nexium"), scaling=Decimal("1e-3")
    ),
    "0x45edb535942a8c84d9f4b5d37e1b25f91ea4804c": TokenInfo(
        currency=CurrencyInfo(symbol="RAO", name="RadioYo Coin"), scaling=Decimal("1e-18")
    ),
    "0x45f24baeef268bb6d63aee5129015d69702bcdfa": TokenInfo(
        currency=CurrencyInfo(symbol="YFV", name="YFValue"), scaling=Decimal("1e-18")
    ),
    "0x45f2ab0ca2116b2e1a70bf5e13293947b25d0272": TokenInfo(
        currency=CurrencyInfo(symbol="GLOB", name="Global Reserve System"), scaling=Decimal("1e-18")
    ),
    "0x4612021c75809160be60db21fbc9d6add0b32def": TokenInfo(
        currency=CurrencyInfo(symbol="BCP", name="Block Commerce Prot"), scaling=Decimal("1e-18")
    ),
    "0x461733c17b0755ca5649b6db08b3e213fcf22546": TokenInfo(
        currency=CurrencyInfo(symbol="ATN", name="ATN"), scaling=Decimal("1e-18")
    ),
    "0x4618519de4c304f3444ffa7f812dddc2971cc688": TokenInfo(
        currency=CurrencyInfo(symbol="KIND", name="Kind Ads Token"), scaling=Decimal("1e-8")
    ),
    "0x462edaa6c1339f98bcb59582af782326603df5f2": TokenInfo(
        currency=CurrencyInfo(symbol="NTER", name="NTerprise"), scaling=Decimal("1e-18")
    ),
    "0x4639cd8cd52ec1cf2e496a606ce28d8afb1c792f": TokenInfo(
        currency=CurrencyInfo(symbol="BREE", name="CBDAO"), scaling=Decimal("1e-18")
    ),
    "0x46492473755e8df960f8034877f61732d718ce96": TokenInfo(
        currency=CurrencyInfo(symbol="STRC", name="StarCredits"), scaling=Decimal("1e-8")
    ),
    "0x464ebe77c293e473b48cfe96ddcf88fcf7bfdac0": TokenInfo(
        currency=CurrencyInfo(symbol="KRL", name="KRYLL"), scaling=Decimal("1e-18")
    ),
    "0x464fdb8affc9bac185a7393fd4298137866dcfb8": TokenInfo(
        currency=CurrencyInfo(symbol="REALM", name="Realm"), scaling=Decimal("1e-18")
    ),
    "0x4672bad527107471cb5067a887f4656d585a8a31": TokenInfo(
        currency=CurrencyInfo(symbol="DROP", name="Dropil"), scaling=Decimal("1e-18")
    ),
    "0x4674672bcddda2ea5300f5207e1158185c944bc0": TokenInfo(
        currency=CurrencyInfo(symbol="GXT", name="Gem Exchange And Tr"), scaling=Decimal("1e-18")
    ),
    "0x4674a4f24c5f63d53f22490fb3a08eaaad739ff8": TokenInfo(
        currency=CurrencyInfo(symbol="BRKL", name="Brokoli"), scaling=Decimal("1e-18")
    ),
    "0x46760d2bf2f4dd5405646d9b2ce7b723efe74a48": TokenInfo(
        currency=CurrencyInfo(symbol="PFB", name="Penny For Bit"), scaling=Decimal("1e-18")
    ),
    "0x467bccd9d29f223bce8043b84e8c8b282827790f": TokenInfo(
        currency=CurrencyInfo(symbol="TEL", name="Telcoin"), scaling=Decimal("1e-2")
    ),
    "0x4688a8b1f292fdab17e9a90c8bc379dc1dbd8713": TokenInfo(
        currency=CurrencyInfo(symbol="COVER", name="Cover Protocol"), scaling=Decimal("1e-18")
    ),
    "0x4689a4e169eb39cc9078c0940e21ff1aa8a39b9c": TokenInfo(
        currency=CurrencyInfo(symbol="PTT", name="Proton Token"), scaling=Decimal("1e-18")
    ),
    "0x468ab3b1f63a1c14b361bc367c3cc92277588da1": TokenInfo(
        currency=CurrencyInfo(symbol="YELD", name="Yeld Finance"), scaling=Decimal("1e-18")
    ),
    "0x468d58d6a52249844a166d0ef045dbdd7ce0c751": TokenInfo(
        currency=CurrencyInfo(symbol="RAX", name="RAX Token"), scaling=Decimal("1e-18")
    ),
    "0x4690d8f53e0d367f5b68f7f571e6eb4b72d39ace": TokenInfo(
        currency=CurrencyInfo(symbol="WNRZ", name="WinPlay"), scaling=Decimal("1e-18")
    ),
    "0x4691937a7508860f876c9c0a2a617e7d9e945d4b": TokenInfo(
        currency=CurrencyInfo(symbol="WOO", name="Wootrade Network"), scaling=Decimal("1e-18")
    ),
    "0x469e66e06fec34839e5eb1273ba85a119b8d702f": TokenInfo(
        currency=CurrencyInfo(symbol="DEGOV", name="Degov"), scaling=Decimal("1e-18")
    ),
    "0x469eda64aed3a3ad6f868c44564291aa415cb1d9": TokenInfo(
        currency=CurrencyInfo(symbol="FLUX", name="Datamine FLUX"), scaling=Decimal("1e-18")
    ),
    "0x46ae264bf6d9dc6dd84c31064551f961c67a755c": TokenInfo(
        currency=CurrencyInfo(symbol="HTX", name="HOT"), scaling=Decimal("1e-18")
    ),
    "0x46b9ad944d1059450da1163511069c718f699d31": TokenInfo(
        currency=CurrencyInfo(symbol="CS", name="CREDITS"), scaling=Decimal("1e-6")
    ),
    "0x46c76f8be43fd8aa7ce59d649a76728323b30214": TokenInfo(
        currency=CurrencyInfo(symbol="MCTK", name="Mine Chat Token"), scaling=Decimal("1e-18")
    ),
    "0x46d0dac0926fa16707042cadc23f1eb4141fe86b": TokenInfo(
        currency=CurrencyInfo(symbol="SNM", name="SONM"), scaling=Decimal("1e-18")
    ),
    "0x46d473a0b3eeec9f55fade641bc576d5bc0b2246": TokenInfo(
        currency=CurrencyInfo(symbol="SURF", name="SurfExUtilityToken"), scaling=Decimal("1e-18")
    ),
    "0x46d886887b6908183032c75dee1b731b26d653c6": TokenInfo(
        currency=CurrencyInfo(symbol="GRC", name="GreenCoin AI"), scaling=Decimal("1e-18")
    ),
    "0x46ee7d0e5080b0fe3d16701c0dbbc6916e3c77c5": TokenInfo(
        currency=CurrencyInfo(symbol="CAN", name="COINWAYCOIN"), scaling=Decimal("1e-10")
    ),
    "0x470ebf5f030ed85fc1ed4c2d36b9dd02e77cf1b7": TokenInfo(
        currency=CurrencyInfo(symbol="TEMPLE", name="TempleDAO"), scaling=Decimal("1e-18")
    ),
    "0x47110d43175f7f2c2425e7d15792acc5817eb44f": TokenInfo(
        currency=CurrencyInfo(symbol="GMI", name="Bankless DeFi Innov"), scaling=Decimal("1e-18")
    ),
    "0x471daee6e481b2ab7d2f2f64b8f9b083daae29da": TokenInfo(
        currency=CurrencyInfo(symbol="HOPS", name="LORDLESS HOPS"), scaling=Decimal("1e-18")
    ),
    "0x4730fb1463a6f1f44aeb45f6c5c422427f37f4d0": TokenInfo(
        currency=CurrencyInfo(symbol="FOUR", name="4thpillar technologies"), scaling=Decimal("1e-18")
    ),
    "0x474021845c4643113458ea4414bdb7fb74a01a77": TokenInfo(
        currency=CurrencyInfo(symbol="UNO", name="Uno Re"), scaling=Decimal("1e-18")
    ),
    "0x4760e7a401558aa59639161454bb2a41a3c5a90b": TokenInfo(
        currency=CurrencyInfo(symbol="CRD", name="Crowd One"), scaling=Decimal("1e-18")
    ),
    "0x47632da9227e322eda59f9e7691eacc6430ac87c": TokenInfo(
        currency=CurrencyInfo(symbol="YFIB", name="YFI Business"), scaling=Decimal("1e-18")
    ),
    "0x476c5e26a75bd202a9683ffd34359c0cc15be0ff": TokenInfo(
        currency=CurrencyInfo(symbol="SRM", name="Serum"), scaling=Decimal("1e-6")
    ),
    "0x47935edfb3cdd358c50f6c0add1cc24662e30f5f": TokenInfo(
        currency=CurrencyInfo(symbol="SUP8EME", name="SUP8EME"), scaling=Decimal("1e-6")
    ),
    "0x479a315bdafda5e7e66c7aeef228477a0535a2ef": TokenInfo(
        currency=CurrencyInfo(symbol="BFFI", name="BFFI OPTIONS"), scaling=Decimal("1e-18")
    ),
    "0x47af9fd69adc231e674140c81811a640dd92dc51": TokenInfo(
        currency=CurrencyInfo(symbol="MBC", name="MobaCoin"), scaling=Decimal("1e-8")
    ),
    "0x47b28f365bf4cb38db4b6356864bde7bc4b35129": TokenInfo(
        currency=CurrencyInfo(symbol="FNB", name="FNB Protocol"), scaling=Decimal("1e-18")
    ),
    "0x47b9f01b16e9c9cb99191dca68c9cc5bf6403957": TokenInfo(
        currency=CurrencyInfo(symbol="ONSTON", name="Onston"), scaling=Decimal("1e-18")
    ),
    "0x47ba0689fbd72936749b007d18dfb75d34bf241b": TokenInfo(
        currency=CurrencyInfo(symbol="NZE", name="Nagezeni"), scaling=Decimal("1e-8")
    ),
    "0x47bc01597798dcd7506dcca36ac4302fc93a8cfb": TokenInfo(
        currency=CurrencyInfo(symbol="CMCT", name="Crowd Machine"), scaling=Decimal("1e-8")
    ),
    "0x47da42696a866cdc61a4c809a515500a242909c1": TokenInfo(
        currency=CurrencyInfo(symbol="BIT", name="BitRewards Token"), scaling=Decimal("1e-18")
    ),
    "0x47dd62d4d075dead71d0e00299fc56a2d747bebb": TokenInfo(
        currency=CurrencyInfo(symbol="EQL", name="EQUAL"), scaling=Decimal("1e-18")
    ),
    "0x47e67ba66b0699500f18a53f94e2b9db3d47437e": TokenInfo(
        currency=CurrencyInfo(symbol="PXG", name="PlayGame"), scaling=Decimal("1e-18")
    ),
    "0x47e820df943170b0e31f9e18ecd5bdd67b77ff1f": TokenInfo(
        currency=CurrencyInfo(symbol="PIGX", name="PIGX"), scaling=Decimal("1e-18")
    ),
    "0x47eb79217f42f92dbd741add1b1a6783a2c873cf": TokenInfo(
        currency=CurrencyInfo(symbol="BAST", name="Bast"), scaling=Decimal("1e-18")
    ),
    "0x4824a7b64e3966b0133f4f4ffb1b9d6beb75fff7": TokenInfo(
        currency=CurrencyInfo(symbol="TCT", name="TokenClub"), scaling=Decimal("1e-18")
    ),
    "0x4846239fdf4d4c1aeb26729fa064b0205aca90e1": TokenInfo(
        currency=CurrencyInfo(symbol="TSD", name="True Seigniorage Dollar"), scaling=Decimal("1e-18")
    ),
    "0x485715b5e3114e254069ca9e72701cc9239fa4cc": TokenInfo(
        currency=CurrencyInfo(symbol="IIOTT", name="Intelligent Internet of Things Token"), scaling=Decimal("1e-8")
    ),
    "0x485c540b5a299eaeb7307f21f5bc3def6a920b5c": TokenInfo(
        currency=CurrencyInfo(symbol="ALTT", name="Altcoins Talks Token"), scaling=Decimal("1e-1")
    ),
    "0x485d17a6f1b8780392d53d64751824253011a260": TokenInfo(
        currency=CurrencyInfo(symbol="TIME", name="chrono.tech"), scaling=Decimal("1e-8")
    ),
    "0x486a72811ae65c4c814ba929d6da35497d21296f": TokenInfo(
        currency=CurrencyInfo(symbol="GC", name="Galaxy Wallet"), scaling=Decimal("1e-18")
    ),
    "0x48783486ddd7fa85eca6b0c4ae8920bc25dfbcd7": TokenInfo(
        currency=CurrencyInfo(symbol="GOM2", name="GoMoney2"), scaling=Decimal("1e-0")
    ),
    "0x4889f721f80c5e9fade6ea9b85835d405d79a4f4": TokenInfo(
        currency=CurrencyInfo(symbol="MAFI", name="Mafia.Network"), scaling=Decimal("1e-18")
    ),
    "0x488e0369f9bc5c40c002ea7c1fe4fd01a198801c": TokenInfo(
        currency=CurrencyInfo(symbol="GOF", name="Golff"), scaling=Decimal("1e-18")
    ),
    "0x488e4c2dc6696a04286eb204a7bdb7f99aa48d69": TokenInfo(
        currency=CurrencyInfo(symbol="MUX", name="Manutax"), scaling=Decimal("1e-18")
    ),
    "0x48ac44f4e29e602f851b84c271c22b85b9447251": TokenInfo(
        currency=CurrencyInfo(symbol="BHY", name="Bitcoin High Yield Set"), scaling=Decimal("1e-18")
    ),
    "0x48c1b2f3efa85fbafb2ab951bf4ba860a08cdbb7": TokenInfo(
        currency=CurrencyInfo(symbol="HAND", name="ShowHand"), scaling=Decimal("1e-0")
    ),
    "0x48c276e8d03813224bb1e55f953adb6d02fd3e02": TokenInfo(
        currency=CurrencyInfo(symbol="KUMA", name="Kuma Inu"), scaling=Decimal("1e-18")
    ),
    "0x48c3399719b582dd63eb5aadf12a40b4c3f52fa2": TokenInfo(
        currency=CurrencyInfo(symbol="SWISE", name="StakeWise"), scaling=Decimal("1e-18")
    ),
    "0x48c589f9734289d8862a245cf9884631a315696f": TokenInfo(
        currency=CurrencyInfo(symbol="COK", name="Coin Of King"), scaling=Decimal("1e-8")
    ),
    "0x48cf0e2eca22eae0ad33fee16a5cb6e62207a8ab": TokenInfo(
        currency=CurrencyInfo(symbol="YTHO", name="YTHO Online"), scaling=Decimal("1e-18")
    ),
    "0x48dee19c81b89a9ab473361bae7a19210f2deaa4": TokenInfo(
        currency=CurrencyInfo(symbol="BEARSHIT", name="3X Short Shitcoin Index Token"), scaling=Decimal("1e-18")
    ),
    "0x48df4e0296f908ceab0428a5182d19b31fc037d6": TokenInfo(
        currency=CurrencyInfo(symbol="FRV", name="Fitrova"), scaling=Decimal("1e-8")
    ),
    "0x48e234d2ddcb32d780971c0df7fdde25bba192de": TokenInfo(
        currency=CurrencyInfo(symbol="NLD", name="NEWLAND"), scaling=Decimal("1e-18")
    ),
    "0x48e5413b73add2434e47504e2a22d14940dbfe78": TokenInfo(
        currency=CurrencyInfo(symbol="INRM", name="Integrated Money"), scaling=Decimal("1e-3")
    ),
    "0x48f3726c787bdc36bb00c978e701879ceed185a4": TokenInfo(
        currency=CurrencyInfo(symbol="LT", name="Loctite Assets Token"), scaling=Decimal("1e-4")
    ),
    "0x48f775efbe4f5ece6e0df2f7b5932df56823b990": TokenInfo(
        currency=CurrencyInfo(symbol="R", name="R token"), scaling=Decimal("1e-0")
    ),
    "0x48fb253446873234f2febbf9bdeaa72d9d387f94": TokenInfo(
        currency=CurrencyInfo(symbol="VBNT", name="Bancor Governance Token"), scaling=Decimal("1e-18")
    ),
    "0x48ff53777f747cfb694101222a944de070c15d36": TokenInfo(
        currency=CurrencyInfo(symbol="IMP", name="Ether Kingdoms Token"), scaling=Decimal("1e-7")
    ),
    "0x490c95be16384e1f28b9e864e98ffecfcbff386d": TokenInfo(
        currency=CurrencyInfo(symbol="RPM", name="Repme"), scaling=Decimal("1e-18")
    ),
    "0x490dbf7884b8e13c2161448b83dd2d8909db48ed": TokenInfo(
        currency=CurrencyInfo(symbol="CUR8", name="Curate"), scaling=Decimal("1e-8")
    ),
    "0x491604c0fdf08347dd1fa4ee062a822a5dd06b5d": TokenInfo(
        currency=CurrencyInfo(symbol="CTSI", name="Cartesi"), scaling=Decimal("1e-18")
    ),
    "0x49184e6dae8c8ecd89d8bdc1b950c597b8167c90": TokenInfo(
        currency=CurrencyInfo(symbol="LIBERTAS", name="LIBERTAS"), scaling=Decimal("1e-2")
    ),
    "0x491c9a23db85623eed455a8efdd6aba9b911c5df": TokenInfo(
        currency=CurrencyInfo(symbol="HER", name="Hero Node Token"), scaling=Decimal("1e-18")
    ),
    "0x491e136ff7ff03e6ab097e54734697bb5802fc1c": TokenInfo(
        currency=CurrencyInfo(symbol="KTN", name="Kattana"), scaling=Decimal("1e-18")
    ),
    "0x49229c3902d49be6443e01c0251b02780397ab1a": TokenInfo(
        currency=CurrencyInfo(symbol="MAP", name="MAP Protocol"), scaling=Decimal("1e-18")
    ),
    "0x4922a015c4407f87432b179bb209e125432e4a2a": TokenInfo(
        currency=CurrencyInfo(symbol="XAUT", name="Tether Gold"), scaling=Decimal("1e-6")
    ),
    "0x493c57c4763932315a328269e1adad09653b9081": TokenInfo(
        currency=CurrencyInfo(symbol="iDAI", name="Fulcrum DAI iToken"), scaling=Decimal("1e-18")
    ),
    "0x493c8d6a973246a7b26aa8ef4b1494867a825de5": TokenInfo(
        currency=CurrencyInfo(symbol="NLINK", name="NuLINK"), scaling=Decimal("1e-3")
    ),
    "0x4946583c5b86e01ccd30c71a05617d06e3e73060": TokenInfo(
        currency=CurrencyInfo(symbol="PTON", name="Foresting"), scaling=Decimal("1e-18")
    ),
    "0x4946fcea7c692606e8908002e55a582af44ac121": TokenInfo(
        currency=CurrencyInfo(symbol="FOAM", name="FOAM"), scaling=Decimal("1e-18")
    ),
    "0x4954db6391f4feb5468b6b943d4935353596aec9": TokenInfo(
        currency=CurrencyInfo(symbol="USDQ", name="USDQ"), scaling=Decimal("1e-18")
    ),
    "0x49614661737efbfc6a102efaeefdc8e197f7cc0e": TokenInfo(
        currency=CurrencyInfo(symbol="ESCE", name="Escroco Emerald"), scaling=Decimal("1e-8")
    ),
    "0x497baef294c11a5f0f5bea3f2adb3073db448b56": TokenInfo(
        currency=CurrencyInfo(symbol="DEX", name="DEX"), scaling=Decimal("1e-18")
    ),
    "0x49849c98ae39fff122806c06791fa73784fb3675": TokenInfo(
        currency=CurrencyInfo(symbol="RENBTCCURVE", name="LP renBTC Curve"), scaling=Decimal("1e-18")
    ),
    "0x498d99de4268cebca264887f591c4ba8fac042e4": TokenInfo(
        currency=CurrencyInfo(symbol="EMB", name="Euler Money Blockchain"), scaling=Decimal("1e-18")
    ),
    "0x4993cb95c7443bdc06155c5f5688be9d8f6999a5": TokenInfo(
        currency=CurrencyInfo(symbol="ROUND", name="Round"), scaling=Decimal("1e-18")
    ),
    "0x4994e81897a920c0fea235eb8cedeed3c6fff697": TokenInfo(
        currency=CurrencyInfo(symbol="SKO1", name="Sikoba Continuous Sale"), scaling=Decimal("1e-18")
    ),
    "0x499a6b77bc25c26bcf8265e2102b1b3dd1617024": TokenInfo(
        currency=CurrencyInfo(symbol="BTR", name="Bitether"), scaling=Decimal("1e-18")
    ),
    "0x499f434458f62a1e76974fce5efce9dd6b31d4f2": TokenInfo(
        currency=CurrencyInfo(symbol="BNTX", name="BINTEX FUTURES"), scaling=Decimal("1e-8")
    ),
    "0x49a2e9be4e06c7106c5708bfcabb9322d0ba33db": TokenInfo(
        currency=CurrencyInfo(symbol="MAK", name="MAKCOIN"), scaling=Decimal("1e-18")
    ),
    "0x49aec0752e68d0282db544c677f6ba407ba17ed7": TokenInfo(
        currency=CurrencyInfo(symbol="XBL", name="Billionaire Token"), scaling=Decimal("1e-18")
    ),
    "0x49b127bc33ce7e1586ec28cec6a65b112596c822": TokenInfo(
        currency=CurrencyInfo(symbol="ALX", name="ALAX"), scaling=Decimal("1e-18")
    ),
    "0x49bd2da75b1f7af1e4dfd6b1125fecde59dbec58": TokenInfo(
        currency=CurrencyInfo(symbol="LKY", name="Linkey"), scaling=Decimal("1e-18")
    ),
    "0x49d09cda1deb8a1680f1270c5ed15218fc4b18f0": TokenInfo(
        currency=CurrencyInfo(symbol="OVC", name="OVCODE"), scaling=Decimal("1e-18")
    ),
    "0x49de436ea25be263cb3e8ff1401931c6f9b70660": TokenInfo(
        currency=CurrencyInfo(symbol="NXY", name="NEXY"), scaling=Decimal("1e-18")
    ),
    "0x49e833337ece7afe375e44f4e3e8481029218e5c": TokenInfo(
        currency=CurrencyInfo(symbol="VALUE", name="Value DeFi"), scaling=Decimal("1e-18")
    ),
    "0x49e90537d5ef6778fd000d1f05be20134f9f6dc6": TokenInfo(
        currency=CurrencyInfo(symbol="ODC", name="ODDO coin"), scaling=Decimal("1e-8")
    ),
    "0x4a0eedf6e95581cda46a767e612e83731c0cd418": TokenInfo(
        currency=CurrencyInfo(symbol="WNS", name="WINSSHI"), scaling=Decimal("1e-18")
    ),
    "0x4a220e6096b25eadb88358cb44068a3248254675": TokenInfo(
        currency=CurrencyInfo(symbol="QNT", name="Quant"), scaling=Decimal("1e-18")
    ),
    "0x4a37a91eec4c97f9090ce66d21d3b3aadf1ae5ad": TokenInfo(
        currency=CurrencyInfo(symbol="LCT", name="LiquorChain Token"), scaling=Decimal("1e-18")
    ),
    "0x4a42d2c580f83dce404acad18dab26db11a1750e": TokenInfo(
        currency=CurrencyInfo(symbol="RLX", name="Relex"), scaling=Decimal("1e-18")
    ),
    "0x4a527d8fc13c5203ab24ba0944f4cb14658d1db6": TokenInfo(
        currency=CurrencyInfo(symbol="MITX", name="Morpheus Labs"), scaling=Decimal("1e-18")
    ),
    "0x4a57e687b9126435a9b19e4a802113e266adebde": TokenInfo(
        currency=CurrencyInfo(symbol="FXC", name="Flexacoin"), scaling=Decimal("1e-18")
    ),
    "0x4a6058666cf1057eac3cd3a5a614620547559fc9": TokenInfo(
        currency=CurrencyInfo(symbol="BBK", name="BrickBlock"), scaling=Decimal("1e-18")
    ),
    "0x4a615bb7166210cce20e6642a6f8fb5d4d044496": TokenInfo(
        currency=CurrencyInfo(symbol="NAOS", name="NAOS Finance"), scaling=Decimal("1e-18")
    ),
    "0x4a64515e5e1d1073e83f30cb97bed20400b66e10": TokenInfo(
        currency=CurrencyInfo(symbol="WZEC", name="Wrapped Zcash"), scaling=Decimal("1e-18")
    ),
    "0x4a7397b0b86bb0f9482a3f4f16de942f04e88702": TokenInfo(
        currency=CurrencyInfo(symbol="FWT", name="Freeway Token"), scaling=Decimal("1e-18")
    ),
    "0x4a7babfafe46456bc4e965d6fbeaff7f01c8b330": TokenInfo(
        currency=CurrencyInfo(symbol="BRN", name="Burn Coin"), scaling=Decimal("1e-8")
    ),
    "0x4a8f44be523580a11cdb20e2c7c470adf44ec9bb": TokenInfo(
        currency=CurrencyInfo(symbol="BTMC", name="Bit Miner Chain"), scaling=Decimal("1e-18")
    ),
    "0x4a8f5f96d5436e43112c2fbc6a9f70da9e4e16d4": TokenInfo(
        currency=CurrencyInfo(symbol="INXT", name="Internxt"), scaling=Decimal("1e-8")
    ),
    "0x4a9f00de5d8a244944313faee23849ff725e680d": TokenInfo(
        currency=CurrencyInfo(symbol="SCC", name="Science Chain"), scaling=Decimal("1e-18")
    ),
    "0x4aac461c86abfa71e9d00d9a2cde8d74e4e1aeea": TokenInfo(
        currency=CurrencyInfo(symbol="ZINC", name="ZINC"), scaling=Decimal("1e-18")
    ),
    "0x4aaff81cfe81523b1c4f6b6c075ebf9bbdb094c9": TokenInfo(
        currency=CurrencyInfo(symbol="EOSMOON", name="10X Long EOS Token"), scaling=Decimal("1e-18")
    ),
    "0x4ab30b965a8ef0f512da064b5e574d9ad73c0e79": TokenInfo(
        currency=CurrencyInfo(symbol="USDG", name="Gluwacoin"), scaling=Decimal("1e-18")
    ),
    "0x4ac00f287f36a6aad655281fe1ca6798c9cb727b": TokenInfo(
        currency=CurrencyInfo(symbol="GZE", name="GazeCoin"), scaling=Decimal("1e-18")
    ),
    "0x4ac84f878b331e0a60423d25665eba7f33f346fe": TokenInfo(
        currency=CurrencyInfo(symbol="SHE", name="Sternium Huge Elligence"), scaling=Decimal("1e-8")
    ),
    "0x4ad0b81f92b16624bbcf46fc0030cfbbf8d02376": TokenInfo(
        currency=CurrencyInfo(symbol="UDAI", name="Unagii Dai"), scaling=Decimal("1e-18")
    ),
    "0x4ad72841eea8cd10db1d2aeb8e2c59064126c83d": TokenInfo(
        currency=CurrencyInfo(symbol="UAA.CX", name="Under Armour Cl A"), scaling=Decimal("1e-8")
    ),
    "0x4adf728e2df4945082cdd6053869f51278fae196": TokenInfo(
        currency=CurrencyInfo(symbol="IXMR", name="iXMR"), scaling=Decimal("1e-18")
    ),
    "0x4af328c52921706dcb739f25786210499169afe6": TokenInfo(
        currency=CurrencyInfo(symbol="SKB", name="Sakura Bloom"), scaling=Decimal("1e-8")
    ),
    "0x4afb0aac9b862946837b2444566b8a914d6d0d97": TokenInfo(
        currency=CurrencyInfo(symbol="SIFI", name="Simian Finance"), scaling=Decimal("1e-9")
    ),
    "0x4b1e80cac91e2216eeb63e29b957eb91ae9c2be8": TokenInfo(
        currency=CurrencyInfo(symbol="JUP", name="Jupiter"), scaling=Decimal("1e-18")
    ),
    "0x4b317864a05c91225ab8f401ec7be0aeb87e9c12": TokenInfo(
        currency=CurrencyInfo(symbol="BOC", name="BingoCoin"), scaling=Decimal("1e-18")
    ),
    "0x4b34c0cbeef271f895d339c5f76322d71a60782b": TokenInfo(
        currency=CurrencyInfo(symbol="YEFIM", name="Yearn Finance Management"), scaling=Decimal("1e-18")
    ),
    "0x4b3a0c6d668b43f3f07904e124328659b90bb4ca": TokenInfo(
        currency=CurrencyInfo(symbol="AceD", name="AceD"), scaling=Decimal("1e-18")
    ),
    "0x4b3c89e986b12f83eed896f02410429a7289526e": TokenInfo(
        currency=CurrencyInfo(symbol="CPL", name="CoinPlace"), scaling=Decimal("1e-9")
    ),
    "0x4b3eacb500955d22ee8bcdd8dd3d9009e29f2d24": TokenInfo(
        currency=CurrencyInfo(symbol="KMC", name="KemCredit"), scaling=Decimal("1e-8")
    ),
    "0x4b4701f3f827e1331fb22ff8e2beac24b17eb055": TokenInfo(
        currency=CurrencyInfo(symbol="DISTX", name="DistX"), scaling=Decimal("1e-18")
    ),
    "0x4b4b1d389d4f4e082b30f75c6319c0ce5acbd619": TokenInfo(
        currency=CurrencyInfo(symbol="HTN", name="Heart Number"), scaling=Decimal("1e-18")
    ),
    "0x4b4d2e899658fb59b1d518b68fe836b100ee8958": TokenInfo(
        currency=CurrencyInfo(symbol="MIS", name="MIS"), scaling=Decimal("1e-18")
    ),
    "0x4b4f5286e0f93e965292b922b9cd1677512f1222": TokenInfo(
        currency=CurrencyInfo(symbol="YUNO", name="YUNo Finance"), scaling=Decimal("1e-18")
    ),
    "0x4b520c812e8430659fc9f12f6d0c39026c83588d": TokenInfo(
        currency=CurrencyInfo(symbol="DG", name="Decentral Games"), scaling=Decimal("1e-18")
    ),
    "0x4b7265d153886a7dc717e815862acde6ff7b5bc8": TokenInfo(
        currency=CurrencyInfo(symbol="DENCH", name="DENCHCOIN"), scaling=Decimal("1e-18")
    ),
    "0x4b742b5bdb1d252907ae7f399a891d4a178dbc24": TokenInfo(
        currency=CurrencyInfo(symbol="B1P", name="B ONE PAYMENT"), scaling=Decimal("1e-18")
    ),
    "0x4b7ad3a56810032782afce12d7d27122bdb96eff": TokenInfo(
        currency=CurrencyInfo(symbol="SPRKL", name="Sparkle Loyalty"), scaling=Decimal("1e-8")
    ),
    "0x4b969c8c382953e18976bf9211b0fe7a28e12172": TokenInfo(
        currency=CurrencyInfo(symbol="MJA", name="Majatoken"), scaling=Decimal("1e-2")
    ),
    "0x4ba6ddd7b89ed838fed25d208d4f644106e34279": TokenInfo(
        currency=CurrencyInfo(symbol="VETH", name="Vether"), scaling=Decimal("1e-18")
    ),
    "0x4ba8c6ce0e855c051e65dfc37883360efaf7c82b": TokenInfo(
        currency=CurrencyInfo(symbol="OCRV", name="Opyn yCurve Insurance"), scaling=Decimal("1e-15")
    ),
    "0x4bbbc57af270138ef2ff2c50dbfad684e9e0e604": TokenInfo(
        currency=CurrencyInfo(symbol="WAB", name="Wab Network"), scaling=Decimal("1e-18")
    ),
    "0x4bcea5e4d0f6ed53cf45e7a28febb2d3621d7438": TokenInfo(
        currency=CurrencyInfo(symbol="MODEX", name="Modex"), scaling=Decimal("1e-18")
    ),
    "0x4bcee5d00528dd367594e44a743a4c8ccf92b3f5": TokenInfo(
        currency=CurrencyInfo(symbol="FMT", name="Free Market Token"), scaling=Decimal("1e-18")
    ),
    "0x4bd70556ae3f8a6ec6c4080a0c327b24325438f3": TokenInfo(
        currency=CurrencyInfo(symbol="HXRO", name="Hxro"), scaling=Decimal("1e-18")
    ),
    "0x4bdab8164d77608294335be695e01ab3d77de3ab": TokenInfo(
        currency=CurrencyInfo(symbol="IFX.CX", name="Infineon Technologies AG"), scaling=Decimal("1e-8")
    ),
    "0x4be10da47a07716af28ad199fbe020501bddd7af": TokenInfo(
        currency=CurrencyInfo(symbol="XT", name="XT.com Token"), scaling=Decimal("1e-18")
    ),
    "0x4be40bc9681d0a7c24a99b4c92f85b9053fc2a45": TokenInfo(
        currency=CurrencyInfo(symbol="YFIII", name="Dify.Finance"), scaling=Decimal("1e-18")
    ),
    "0x4bffc9b4d4dcf730820a2edcad48ff5d7e0ae807": TokenInfo(
        currency=CurrencyInfo(symbol="INC", name="Influence Chain"), scaling=Decimal("1e-18")
    ),
    "0x4c09ba2a7e6c0acbda559e60b8cd5d651b56436c": TokenInfo(
        currency=CurrencyInfo(symbol="BNT", name="BitFlexo Native Token"), scaling=Decimal("1e-18")
    ),
    "0x4c0fbe1bb46612915e7967d2c3213cd4d87257ad": TokenInfo(
        currency=CurrencyInfo(symbol="APIS", name="APIS"), scaling=Decimal("1e-18")
    ),
    "0x4c11249814f11b9346808179cf06e71ac328c1b5": TokenInfo(
        currency=CurrencyInfo(symbol="ORAI", name="Oraichain Token"), scaling=Decimal("1e-18")
    ),
    "0x4c133e081dfb5858e39cca74e69bf603d409e57a": TokenInfo(
        currency=CurrencyInfo(symbol="BCHBULL", name="3X Long Bitcoin Cash Token"), scaling=Decimal("1e-18")
    ),
    "0x4c14114c107d6374ec31981f5f6cc27a13e22f9a": TokenInfo(
        currency=CurrencyInfo(symbol="STS", name="SBank"), scaling=Decimal("1e-18")
    ),
    "0x4c19596f5aaff459fa38b0f7ed92f11ae6543784": TokenInfo(
        currency=CurrencyInfo(symbol="TRU", name="TrueFi"), scaling=Decimal("1e-8")
    ),
    "0x4c1c4957d22d8f373aed54d0853b090666f6f9de": TokenInfo(
        currency=CurrencyInfo(symbol="SLV", name="Silverway"), scaling=Decimal("1e-18")
    ),
    "0x4c1e085d8c2d2a8377834d0d7b38f12cc5b86898": TokenInfo(
        currency=CurrencyInfo(symbol="SILK", name="SilkChain"), scaling=Decimal("1e-18")
    ),
    "0x4c2e59d098df7b6cbae0848d66de2f8a4889b9c3": TokenInfo(
        currency=CurrencyInfo(symbol="FODL", name="Fodl Finance"), scaling=Decimal("1e-18")
    ),
    "0x4c327471c44b2dacd6e90525f9d629bd2e4f662c": TokenInfo(
        currency=CurrencyInfo(symbol="GHOST", name="GHOST"), scaling=Decimal("1e-18")
    ),
    "0x4c382f8e09615ac86e08ce58266cc227e7d4d913": TokenInfo(
        currency=CurrencyInfo(symbol="SKR", name="Skrilla Token"), scaling=Decimal("1e-6")
    ),
    "0x4c383bdcae52a6e1cb810c76c70d6f31a249ec9b": TokenInfo(
        currency=CurrencyInfo(symbol="RGS", name="RusGas"), scaling=Decimal("1e-8")
    ),
    "0x4c38d0e726b6c86f64c1b281348e725973542043": TokenInfo(
        currency=CurrencyInfo(symbol="SAS", name="Stand Share"), scaling=Decimal("1e-18")
    ),
    "0x4c5601164e2048a4154de91fa5e0b07e626cab7f": TokenInfo(
        currency=CurrencyInfo(symbol="FNL", name="Funnel Token"), scaling=Decimal("1e-3")
    ),
    "0x4c567c3363cc42c5a42c6d8bf01503fd1d0b91cd": TokenInfo(
        currency=CurrencyInfo(symbol="EEE", name="Elementh"), scaling=Decimal("1e-18")
    ),
    "0x4c6584ddcdfab7110c7b1be47749bde8edc9c0c9": TokenInfo(
        currency=CurrencyInfo(symbol="INF", name="Infinity Token"), scaling=Decimal("1e-18")
    ),
    "0x4c6719bf85903d18c295da44216f862b01b36f43": TokenInfo(
        currency=CurrencyInfo(symbol="ALH", name="AlloHash"), scaling=Decimal("1e-18")
    ),
    "0x4c6e796bbfe5eb37f9e3e0f66c009c8bf2a5f428": TokenInfo(
        currency=CurrencyInfo(symbol="FCBTC", name="FC Bitcoin"), scaling=Decimal("1e-8")
    ),
    "0x4c6ec08cf3fc987c6c4beb03184d335a2dfc4042": TokenInfo(
        currency=CurrencyInfo(symbol="PAINT", name="MurAll"), scaling=Decimal("1e-18")
    ),
    "0x4c9a72fb706084a58653bd8bd74f8aee0316ff5a": TokenInfo(
        currency=CurrencyInfo(symbol="MLC", name="Mele Coin"), scaling=Decimal("1e-18")
    ),
    "0x4ca74185532dc1789527194e5b9c866dd33f4e82": TokenInfo(
        currency=CurrencyInfo(symbol="sense", name="sensatori"), scaling=Decimal("1e-18")
    ),
    "0x4cac2515716ab2531402ca8f992e235189f29c5a": TokenInfo(
        currency=CurrencyInfo(symbol="WIN", name="Winstex"), scaling=Decimal("1e-18")
    ),
    "0x4cb10f4df4bf4f64d4797d00d468181ef731be9a": TokenInfo(
        currency=CurrencyInfo(symbol="EON", name="Dimension"), scaling=Decimal("1e-8")
    ),
    "0x4cb925ec5e2c52269c1a4f91cc3cb4bf5671b71f": TokenInfo(
        currency=CurrencyInfo(symbol="CSCO.CX", name="Cisco Systems"), scaling=Decimal("1e-8")
    ),
    "0x4cc19356f2d37338b9802aa8e8fc58b0373296e7": TokenInfo(
        currency=CurrencyInfo(symbol="KEY", name="SelfKey"), scaling=Decimal("1e-18")
    ),
    "0x4cc8486f2f3dce2d3b5e27057cf565e16906d12d": TokenInfo(
        currency=CurrencyInfo(symbol="KRW-G", name="KRW Gluwacoin"), scaling=Decimal("1e-18")
    ),
    "0x4cc84b41ececc387244512242eec226eb7948a92": TokenInfo(
        currency=CurrencyInfo(symbol="KASSIAHOME", name="Kassia Home"), scaling=Decimal("1e-18")
    ),
    "0x4ccc3759eb48faf1c6cfadad2619e7038db6b212": TokenInfo(
        currency=CurrencyInfo(symbol="ECT", name="SuperEdge"), scaling=Decimal("1e-8")
    ),
    "0x4cd0c43b0d53bc318cc5342b77eb6f124e47f526": TokenInfo(
        currency=CurrencyInfo(symbol="FREE", name="FreeRossDAO"), scaling=Decimal("1e-18")
    ),
    "0x4cd988afbad37289baaf53c13e98e2bd46aaea8c": TokenInfo(
        currency=CurrencyInfo(symbol="KEY", name="Key"), scaling=Decimal("1e-18")
    ),
    "0x4ce6b362bc77a24966dda9078f9cef81b3b886a7": TokenInfo(
        currency=CurrencyInfo(symbol="NPER", name="NPER"), scaling=Decimal("1e-18")
    ),
    "0x4ceda7906a5ed2179785cd3a40a69ee8bc99c466": TokenInfo(
        currency=CurrencyInfo(symbol="AION", name="AION"), scaling=Decimal("1e-8")
    ),
    "0x4cef5a02c36253cfb06825ace2a356e78000145f": TokenInfo(
        currency=CurrencyInfo(symbol="AHT", name="Bowhead Health"), scaling=Decimal("1e-18")
    ),
    "0x4cf488387f035ff08c371515562cba712f9015d4": TokenInfo(
        currency=CurrencyInfo(symbol="WPR", name="WePower"), scaling=Decimal("1e-18")
    ),
    "0x4cf89ca06ad997bc732dc876ed2a7f26a9e7f361": TokenInfo(
        currency=CurrencyInfo(symbol="MYST", name="Mysterium"), scaling=Decimal("1e-18")
    ),
    "0x4d09c5e758ca68be27240f29fb681e5a5341ca98": TokenInfo(
        currency=CurrencyInfo(symbol="HOTC", name="HOTchain"), scaling=Decimal("1e-18")
    ),
    "0x4d13d624a87baa278733c068a174412afa9ca6c8": TokenInfo(
        currency=CurrencyInfo(symbol="XBASE", name="Eterbase Coin"), scaling=Decimal("1e-18")
    ),
    "0x4d224452801aced8b2f0aebe155379bb5d594381": TokenInfo(
        currency=CurrencyInfo(symbol="APE", name="ApeCoin"), scaling=Decimal("1e-18")
    ),
    "0x4d28ebe3c79b682b9870cf68b31bff4d8a133e91": TokenInfo(
        currency=CurrencyInfo(symbol="RTX", name="R2X"), scaling=Decimal("1e-18")
    ),
    "0x4d2c05109a1309c6de0d3b7f06f397c9c41b8fae": TokenInfo(
        currency=CurrencyInfo(symbol="VPP", name="Value Promise Protocol"), scaling=Decimal("1e-18")
    ),
    "0x4d2ee5dae46c86da2ff521f7657dad98834f97b8": TokenInfo(
        currency=CurrencyInfo(symbol="PPBLZ", name="Pepemon Pepeballs"), scaling=Decimal("1e-18")
    ),
    "0x4d31200e6d7854c2f664af7fc38a21600960f74d": TokenInfo(
        currency=CurrencyInfo(symbol="BFC", name="Bit Financial"), scaling=Decimal("1e-18")
    ),
    "0x4d7fd9f3fecb85e4cd68ffda1ef3015e3d3b8dfe": TokenInfo(
        currency=CurrencyInfo(symbol="OFBC", name="OneFinBank Coin"), scaling=Decimal("1e-2")
    ),
    "0x4d807509aece24c0fa5a102b6a3b059ec6e14392": TokenInfo(
        currency=CurrencyInfo(symbol="ONE", name="Menlo One"), scaling=Decimal("1e-18")
    ),
    "0x4d829f8c92a6691c56300d020c9e0db984cfe2ba": TokenInfo(
        currency=CurrencyInfo(symbol="XCC", name="CoinCrowd"), scaling=Decimal("1e-18")
    ),
    "0x4d8fc1453a0f359e99c9675954e656d80d996fbf": TokenInfo(
        currency=CurrencyInfo(symbol="BEE", name="Bee Token"), scaling=Decimal("1e-18")
    ),
    "0x4d953cf077c0c95ba090226e59a18fcf97db44ec": TokenInfo(
        currency=CurrencyInfo(symbol="MINI", name="Mini"), scaling=Decimal("1e-18")
    ),
    "0x4d9e23a3842fe7eb7682b9725cf6c507c424a41b": TokenInfo(
        currency=CurrencyInfo(symbol="CAR", name="CarBlock"), scaling=Decimal("1e-18")
    ),
    "0x4d9f37e79723a3bb910e1b2fc7b1ef851261b1d9": TokenInfo(
        currency=CurrencyInfo(symbol="TMUS.CX", name="T-Mobile US Inc"), scaling=Decimal("1e-8")
    ),
    "0x4da0c48376c277cdbd7fc6fdc6936dee3e4adf75": TokenInfo(
        currency=CurrencyInfo(symbol="EPIK", name="Epik Prime"), scaling=Decimal("1e-18")
    ),
    "0x4da9b813057d04baef4e5800e36083717b4a0341": TokenInfo(
        currency=CurrencyInfo(symbol="ATUSD", name="Aave TUSD v1"), scaling=Decimal("1e-18")
    ),
    "0x4dae3ed84d32f015ca6e5c94beaf56203c7e46ba": TokenInfo(
        currency=CurrencyInfo(symbol="ADNT.CX", name="Adient"), scaling=Decimal("1e-8")
    ),
    "0x4dc3643dbc642b72c158e7f3d2ff232df61cb6ce": TokenInfo(
        currency=CurrencyInfo(symbol="AMB", name="Ambrosus"), scaling=Decimal("1e-18")
    ),
    "0x4dcadd9adfd450c2ef997bb71888c2995e2d33a0": TokenInfo(
        currency=CurrencyInfo(symbol="UNC", name="UniGame"), scaling=Decimal("1e-0")
    ),
    "0x4ddc2d193948926d02f9b1fe9e1daa0718270ed5": TokenInfo(
        currency=CurrencyInfo(symbol="CETH", name="cETH"), scaling=Decimal("1e-8")
    ),
    "0x4de2573e27e648607b50e1cfff921a33e4a34405": TokenInfo(
        currency=CurrencyInfo(symbol="LST", name="Lendroid Support Token"), scaling=Decimal("1e-18")
    ),
    "0x4df2c7ec048f69bba12098bf71a15afeeaaf0c4b": TokenInfo(
        currency=CurrencyInfo(symbol="XSC", name="SmartChain Protocol"), scaling=Decimal("1e-18")
    ),
    "0x4df47b4969b2911c966506e3592c41389493953b": TokenInfo(
        currency=CurrencyInfo(symbol="FND", name="FundRequest"), scaling=Decimal("1e-18")
    ),
    "0x4df812f6064def1e5e029f1ca858777cc98d2d81": TokenInfo(
        currency=CurrencyInfo(symbol="XAUR", name="Xaurum"), scaling=Decimal("1e-8")
    ),
    "0x4dfd148b532e934a2a26ea65689cf6268753e130": TokenInfo(
        currency=CurrencyInfo(symbol="MDT", name="governance token MonolithosDAO"), scaling=Decimal("1e-18")
    ),
    "0x4e0603e2a27a30480e5e3a4fe548e29ef12f64be": TokenInfo(
        currency=CurrencyInfo(symbol="CREDO", name="Credo"), scaling=Decimal("1e-18")
    ),
    "0x4e085036a1b732cbe4ffb1c12ddfdd87e7c3664d": TokenInfo(
        currency=CurrencyInfo(symbol="PRDZ", name="Predictz"), scaling=Decimal("1e-18")
    ),
    "0x4e15361fd6b4bb609fa63c81a2be19d873717870": TokenInfo(
        currency=CurrencyInfo(symbol="FTM", name="Fantom"), scaling=Decimal("1e-18")
    ),
    "0x4e352cf164e64adcbad318c3a1e222e9eba4ce42": TokenInfo(
        currency=CurrencyInfo(symbol="MCB", name="MCDEX"), scaling=Decimal("1e-18")
    ),
    "0x4e3856c37b2fe7ff2fe34510cda82a1dffd63cd0": TokenInfo(
        currency=CurrencyInfo(symbol="USDEX", name="eToro US Dollar"), scaling=Decimal("1e-18")
    ),
    "0x4e3bddd468abfc6c88bc25daa5d894380ced5bc8": TokenInfo(
        currency=CurrencyInfo(symbol="NSS", name="NSS Coin"), scaling=Decimal("1e-18")
    ),
    "0x4e3fbd56cd56c3e72c1403e103b45db9da5b9d2b": TokenInfo(
        currency=CurrencyInfo(symbol="CVX", name="Convex Finance"), scaling=Decimal("1e-18")
    ),
    "0x4e594479fa417a1e9c5790a413575802d393010f": TokenInfo(
        currency=CurrencyInfo(symbol="FER", name="Ferret Coin"), scaling=Decimal("1e-8")
    ),
    "0x4e676548d262ea27825aa9c5150121af65dfa304": TokenInfo(
        currency=CurrencyInfo(symbol="TKO", name="TakeOff Centre"), scaling=Decimal("1e-18")
    ),
    "0x4e6c19aa53f0e4f8e1c53d8cb14cd81767dff5cd": TokenInfo(
        currency=CurrencyInfo(symbol="QCOM.CX", name="QUALCOMM Inc"), scaling=Decimal("1e-8")
    ),
    "0x4e84a65b5664d33b67750771f8beaec458bd6729": TokenInfo(
        currency=CurrencyInfo(symbol="ORX", name="Orionix"), scaling=Decimal("1e-18")
    ),
    "0x4e84e9e5fb0a972628cf4568c403167ef1d40431": TokenInfo(
        currency=CurrencyInfo(symbol="FFC", name="Fluzcoin"), scaling=Decimal("1e-18")
    ),
    "0x4e8a9d0bf525d78fd9e0c88710099f227f6924cf": TokenInfo(
        currency=CurrencyInfo(symbol="SKING", name="SKING"), scaling=Decimal("1e-9")
    ),
    "0x4e8e8eb5a4ed17170b646d33b8ef3e7352585607": TokenInfo(
        currency=CurrencyInfo(symbol="PDRY", name="Pandroyty Token"), scaling=Decimal("1e-18")
    ),
    "0x4e9a46ea6a22f3894abee2302ad42fd3b69e21e2": TokenInfo(
        currency=CurrencyInfo(symbol="BSCGIRL", name="Binance Smart Chain"), scaling=Decimal("1e-8")
    ),
    "0x4eac6df4b1d8e2faa125d10ba2531b491114c6b6": TokenInfo(
        currency=CurrencyInfo(symbol="TLC", name="TrueLoveChain"), scaling=Decimal("1e-18")
    ),
    "0x4ec2efb9cbd374786a03261e46ffce1a67756f3b": TokenInfo(
        currency=CurrencyInfo(symbol="DEFL", name="Deflacoin"), scaling=Decimal("1e-18")
    ),
    "0x4ecb692b0fedecd7b486b4c99044392784877e8c": TokenInfo(
        currency=CurrencyInfo(symbol="CHERRY", name="Cherry"), scaling=Decimal("1e-4")
    ),
    "0x4edd66235349e353eb8cb8e40596599644bfe91c": TokenInfo(
        currency=CurrencyInfo(symbol="VANY", name="Vanywhere"), scaling=Decimal("1e-18")
    ),
    "0x4ee15f44c6f0d8d1136c83efd2e8e4ac768954c6": TokenInfo(
        currency=CurrencyInfo(symbol="crYYCRV", name="Cream yyCRV"), scaling=Decimal("1e-8")
    ),
    "0x4ee6e959d460de47dfe58e5e6fbab330ce8484b6": TokenInfo(
        currency=CurrencyInfo(symbol="QURA", name="QURA GLOBAL"), scaling=Decimal("1e-18")
    ),
    "0x4eeea7b48b9c3ac8f70a9c932a8b1e8a5cb624c7": TokenInfo(
        currency=CurrencyInfo(symbol="MBN", name="Membrana"), scaling=Decimal("1e-18")
    ),
    "0x4efe8665e564bf454ccf5c90ee16817f7485d5cf": TokenInfo(
        currency=CurrencyInfo(symbol="BDT", name="BlackDragon Token"), scaling=Decimal("1e-18")
    ),
    "0x4f01ecbe8d6882ffaee47fe23a9677a96aabed07": TokenInfo(
        currency=CurrencyInfo(symbol="MTUSD", name="MythicUSD"), scaling=Decimal("1e-18")
    ),
    "0x4f22310c27ef39feaa4a756027896dc382f0b5e2": TokenInfo(
        currency=CurrencyInfo(symbol="SPIN", name="SPIN Protocol"), scaling=Decimal("1e-18")
    ),
    "0x4f27053f32eda8af84956437bc00e5ffa7003287": TokenInfo(
        currency=CurrencyInfo(symbol="THRT", name="Thrive"), scaling=Decimal("1e-18")
    ),
    "0x4f34adfff48ceb4af2f3b2253cdfdcc99c9053f4": TokenInfo(
        currency=CurrencyInfo(symbol="GFCS", name="Global Funeral Care"), scaling=Decimal("1e-0")
    ),
    "0x4f3afec4e5a3f2a6a1a411def7d7dfe50ee057bf": TokenInfo(
        currency=CurrencyInfo(symbol="DGX", name="Digix Gold"), scaling=Decimal("1e-9")
    ),
    "0x4f4f0db4de903b88f2b1a2847971e231d54f8fd3": TokenInfo(
        currency=CurrencyInfo(symbol="GEE", name="Geens Platform Token"), scaling=Decimal("1e-8")
    ),
    "0x4f4f0ef7978737ce928bff395529161b44e27ad9": TokenInfo(
        currency=CurrencyInfo(symbol="YFD", name="Your Finance Decentralized"), scaling=Decimal("1e-18")
    ),
    "0x4f5f2eea4ed3485e5e23a39704d5fd9d0a423886": TokenInfo(
        currency=CurrencyInfo(symbol="TOR", name="Torchain"), scaling=Decimal("1e-18")
    ),
    "0x4f5fa8f2d12e5eb780f6082dd656c565c48e0f24": TokenInfo(
        currency=CurrencyInfo(symbol="GUM", name="Gourmet Galaxy"), scaling=Decimal("1e-18")
    ),
    "0x4f76e85d067e219779a863ff18577846b3152f1f": TokenInfo(
        currency=CurrencyInfo(symbol="KUBO", name="KuboCoin"), scaling=Decimal("1e-8")
    ),
    "0x4f7c5bd3f7d62a9c984e265d73a86f5515f3e92b": TokenInfo(
        currency=CurrencyInfo(symbol="BURN", name="The Burn Token"), scaling=Decimal("1e-0")
    ),
    "0x4f7d5a7588771e7889b599dbcb67c63a28129732": TokenInfo(
        currency=CurrencyInfo(symbol="GERC", name="Game Eternal Role Chain"), scaling=Decimal("1e-3")
    ),
    "0x4f818a843580a16a1c3df50bc4c059c027f60701": TokenInfo(
        currency=CurrencyInfo(symbol="PTC", name="PetDia"), scaling=Decimal("1e-18")
    ),
    "0x4f81c790581b240a5c948afd173620ecc8c71c8d": TokenInfo(
        currency=CurrencyInfo(symbol="XDG", name="Decentral Games Gov"), scaling=Decimal("1e-18")
    ),
    "0x4f878c0852722b0976a955d68b376e4cd4ae99e5": TokenInfo(
        currency=CurrencyInfo(symbol="WIC", name="WaykiCoin"), scaling=Decimal("1e-8")
    ),
    "0x4f9254c83eb525f9fcf346490bbb3ed28a81c667": TokenInfo(
        currency=CurrencyInfo(symbol="CELR", name="Celer Network"), scaling=Decimal("1e-18")
    ),
    "0x4fab740779c73aa3945a5cf6025bf1b0e7f6349c": TokenInfo(
        currency=CurrencyInfo(symbol="DIRTY", name="dirty.finance"), scaling=Decimal("1e-18")
    ),
    "0x4fabb145d64652a948d72533023f6e7a623c7c53": TokenInfo(
        currency=CurrencyInfo(symbol="BUSD", name="Binance USD"), scaling=Decimal("1e-18")
    ),
    "0x4fac0ccd9e2ed9fd462d42b66fb81ba9a1f6f25e": TokenInfo(
        currency=CurrencyInfo(symbol="AXL", name="AXiaL"), scaling=Decimal("1e-18")
    ),
    "0x4fbb0b4cd8f960ac3428194f1c94c805d5b35836": TokenInfo(
        currency=CurrencyInfo(symbol="BBGC", name="BigBang Game"), scaling=Decimal("1e-8")
    ),
    "0x4fbb350052bca5417566f188eb2ebce5b19bc964": TokenInfo(
        currency=CurrencyInfo(symbol="GRG", name="RigoBlock"), scaling=Decimal("1e-18")
    ),
    "0x4fcfce2cddd8114f5ddff23f8869337197b27e1f": TokenInfo(
        currency=CurrencyInfo(symbol="XTM", name="Torum"), scaling=Decimal("1e-18")
    ),
    "0x4fe5851c9af07df9e5ad8217afae1ea72737ebda": TokenInfo(
        currency=CurrencyInfo(symbol="OPT", name="OpenPredict Token"), scaling=Decimal("1e-18")
    ),
    "0x4fe83213d56308330ec302a8bd641f1d0113a4cc": TokenInfo(
        currency=CurrencyInfo(symbol="NU", name="NuCypher"), scaling=Decimal("1e-18")
    ),
    "0x4fe9f52ec23f6805f2fd0332a34da4f1c135b024": TokenInfo(
        currency=CurrencyInfo(symbol="CAI", name="Cai Token"), scaling=Decimal("1e-18")
    ),
    "0x4fecc0f0630dc13b6986420d623a017df7ac8916": TokenInfo(
        currency=CurrencyInfo(symbol="GE.CX", name="General Electric Co"), scaling=Decimal("1e-8")
    ),
    "0x4ffe33e525042cc84c503db5842ecda280f4a805": TokenInfo(
        currency=CurrencyInfo(symbol="GWP", name="Green World Project"), scaling=Decimal("1e-18")
    ),
    "0x50026ad58b338cf3eccc2b422deb8faa725f377f": TokenInfo(
        currency=CurrencyInfo(symbol="STEP", name="1Step.finance"), scaling=Decimal("1e-8")
    ),
    "0x5003b168b457b663c3c18ffcf5b6a24bee8f59c7": TokenInfo(
        currency=CurrencyInfo(symbol="MUSK", name="Musk"), scaling=Decimal("1e-18")
    ),
    "0x500df47e1df0ef06039218dcf0960253d89d6658": TokenInfo(
        currency=CurrencyInfo(symbol="AUPC", name="Authpaper Coin"), scaling=Decimal("1e-18")
    ),
    "0x501262281b2ba043e2fbf14904980689cddb0c78": TokenInfo(
        currency=CurrencyInfo(symbol="MORE", name="Mithril Ore"), scaling=Decimal("1e-2")
    ),
    "0x5046e860ff274fb8c66106b0ffb8155849fb0787": TokenInfo(
        currency=CurrencyInfo(symbol="JS", name="JavaScript Token"), scaling=Decimal("1e-8")
    ),
    "0x50625b636dab619bf6af75f693dc486e56c2a694": TokenInfo(
        currency=CurrencyInfo(symbol="GHT", name="GroovyHooman"), scaling=Decimal("1e-10")
    ),
    "0x5062946b19c0f01467ad1e6ae8d792395078a7c8": TokenInfo(
        currency=CurrencyInfo(symbol="TRUEBIT", name="TrueBit"), scaling=Decimal("1e-18")
    ),
    "0x506de580ecdba535eb0a7e61d3fa3dd8f7c8b6b9": TokenInfo(
        currency=CurrencyInfo(symbol="BCHNRBTC-JAN-2021", name="BCHNrBTC Synthetic Token Expiring 5 January 2021"),
        scaling=Decimal("1e-18"),
    ),
    "0x508325285114821151a18e148f4299ea09a9ca05": TokenInfo(
        currency=CurrencyInfo(symbol="HKDT", name="HKD Tether"), scaling=Decimal("1e-18")
    ),
    "0x508f36baac673fe9e213e69f0f75cbcfeb015917": TokenInfo(
        currency=CurrencyInfo(symbol="MKT", name="Meimei Token"), scaling=Decimal("1e-18")
    ),
    "0x50987e6be405ebac691f8988304562e5efc3b2ea": TokenInfo(
        currency=CurrencyInfo(symbol="MYO", name="Mycro"), scaling=Decimal("1e-18")
    ),
    "0x509a38b7a1cc0dcd83aa9d06214663d9ec7c7f4a": TokenInfo(
        currency=CurrencyInfo(symbol="BST", name="BlocksquareToken"), scaling=Decimal("1e-18")
    ),
    "0x50bc2ecc0bfdf5666640048038c1aba7b7525683": TokenInfo(
        currency=CurrencyInfo(symbol="CV", name="carVertical"), scaling=Decimal("1e-18")
    ),
    "0x50c77402380cce836cf5515eab44ecad1a5e0d0a": TokenInfo(
        currency=CurrencyInfo(symbol="BIIB.CX", name="Biogen Inc"), scaling=Decimal("1e-8")
    ),
    "0x50d1c9771902476076ecfc8b2a83ad6b9355a4c9": TokenInfo(
        currency=CurrencyInfo(symbol="FTT", name="FTX Token"), scaling=Decimal("1e-18")
    ),
    "0x50de6856358cc35f3a9a57eaaa34bd4cb707d2cd": TokenInfo(
        currency=CurrencyInfo(symbol="RAZOR", name="Razor Network"), scaling=Decimal("1e-18")
    ),
    "0x50eb346fc29a80d97563a50146c3fcf9423b5538": TokenInfo(
        currency=CurrencyInfo(symbol="CANDY", name="Skull Candy Shards"), scaling=Decimal("1e-18")
    ),
    "0x50ec35d1e18d439f02fa895746fc3e1bef311780": TokenInfo(
        currency=CurrencyInfo(symbol="EPS", name="Epanus"), scaling=Decimal("1e-18")
    ),
    "0x50ee674689d75c0f88e8f83cfe8c4b69e8fd590d": TokenInfo(
        currency=CurrencyInfo(symbol="EPY", name="Emphy"), scaling=Decimal("1e-8")
    ),
    "0x50f09629d0afdf40398a3f317cc676ca9132055c": TokenInfo(
        currency=CurrencyInfo(symbol="EVAI", name="Evai"), scaling=Decimal("1e-8")
    ),
    "0x50fff411f4e22e79857ff9ad3475b50d6df195f0": TokenInfo(
        currency=CurrencyInfo(symbol="PHTM", name="Phantom Matter"), scaling=Decimal("1e-18")
    ),
    "0x5102791ca02fc3595398400bfe0e33d7b6c82267": TokenInfo(
        currency=CurrencyInfo(symbol="LDC", name="LeadCoin"), scaling=Decimal("1e-18")
    ),
    "0x511ef917ec95c8b2642f88444539e7821764614e": TokenInfo(
        currency=CurrencyInfo(symbol="XLV.CX", name="Health Care Select Sector SPDR Fund"), scaling=Decimal("1e-8")
    ),
    "0x5121e348e897daef1eef23959ab290e5557cf274": TokenInfo(
        currency=CurrencyInfo(symbol="AI", name="POLY AI"), scaling=Decimal("1e-18")
    ),
    "0x512630dc263fd4c71dbe81fec68cf61156d79e80": TokenInfo(
        currency=CurrencyInfo(symbol="WWT", name="WorldWideTrade"), scaling=Decimal("1e-18")
    ),
    "0x5136c98a80811c3f46bdda8b5c4555cfd9f812f0": TokenInfo(
        currency=CurrencyInfo(symbol="IDH", name="indaHash"), scaling=Decimal("1e-6")
    ),
    "0x5137a403dd25e48de528912a4af62881e625d801": TokenInfo(
        currency=CurrencyInfo(symbol="HUDDL", name="Huddl"), scaling=Decimal("1e-18")
    ),
    "0x514910771af9ca656af840dff83e8264ecf986ca": TokenInfo(
        currency=CurrencyInfo(symbol="LINK", name="Chainlink"), scaling=Decimal("1e-18")
    ),
    "0x5150956e082c748ca837a5dfa0a7c10ca4697f9c": TokenInfo(
        currency=CurrencyInfo(symbol="ZDEX", name="Zeedex"), scaling=Decimal("1e-18")
    ),
    "0x515669d308f887fd83a471c7764f5d084886d34d": TokenInfo(
        currency=CurrencyInfo(symbol="MUXE", name="MUXE"), scaling=Decimal("1e-18")
    ),
    "0x515ba0a2e286af10115284f151cf398688a69170": TokenInfo(
        currency=CurrencyInfo(symbol="TENX", name="TENX"), scaling=Decimal("1e-18")
    ),
    "0x515d7e9d75e2b76db60f8a051cd890eba23286bc": TokenInfo(
        currency=CurrencyInfo(symbol="GDAO", name="Governor DAO"), scaling=Decimal("1e-18")
    ),
    "0x5165d24277cd063f5ac44efd447b27025e888f37": TokenInfo(
        currency=CurrencyInfo(symbol="AYFI", name="Aave YFI"), scaling=Decimal("1e-18")
    ),
    "0x51726fd6e6d264370114d15df83da1e13063fb0f": TokenInfo(
        currency=CurrencyInfo(symbol="MTG", name="Mall Token Gold"), scaling=Decimal("1e-5")
    ),
    "0x519083fc539f23131c3b7046992584592772d12a": TokenInfo(
        currency=CurrencyInfo(symbol="YFIV", name="Yearn Finance Value"), scaling=Decimal("1e-18")
    ),
    "0x519475b31653e46d20cd09f9fdcf3b12bdacb4f5": TokenInfo(
        currency=CurrencyInfo(symbol="VIU", name="Viuly"), scaling=Decimal("1e-18")
    ),
    "0x519c1001d550c0a1dae7d1fc220f7d14c2a521bb": TokenInfo(
        currency=CurrencyInfo(symbol="PSWAP", name="Polkaswap"), scaling=Decimal("1e-18")
    ),
    "0x51a4f65463597ca4609c9a90ea3d5ab219fbc85d": TokenInfo(
        currency=CurrencyInfo(symbol="BWN", name="BITWINGS TOKEN"), scaling=Decimal("1e-18")
    ),
    "0x51bb3ab03ab49ec5cb3883705949657838a015fd": TokenInfo(
        currency=CurrencyInfo(symbol="CRYN", name="CRYNCOIN"), scaling=Decimal("1e-8")
    ),
    "0x51bb9c623226ce781f4a54fc8f4a530a47142b6b": TokenInfo(
        currency=CurrencyInfo(symbol="PTE", name="Peet ERC20"), scaling=Decimal("1e-18")
    ),
    "0x51bc0deaf7bbe82bc9006b0c3531668a4206d27f": TokenInfo(
        currency=CurrencyInfo(symbol="RAKU", name="RAKUN"), scaling=Decimal("1e-18")
    ),
    "0x51c77689a9c2e8ccbecd4ec9770a1fa5fa83eef1": TokenInfo(
        currency=CurrencyInfo(symbol="idleTUSDYield", name="IdleTUSD v3 [Max yield]"), scaling=Decimal("1e-18")
    ),
    "0x51d01615f8d5af8f64c3d754f156e03d988f7771": TokenInfo(
        currency=CurrencyInfo(symbol="XDFT", name="xDeFi Token"), scaling=Decimal("1e-18")
    ),
    "0x51db5ad35c671a87207d88fc11d593ac0c8415bd": TokenInfo(
        currency=CurrencyInfo(symbol="MDA", name="Moeda Loyalty Points"), scaling=Decimal("1e-18")
    ),
    "0x51f14d64435d9c1099a6fea383d26646f931825b": TokenInfo(
        currency=CurrencyInfo(symbol="SOHU.CX", name="Sohu.com Limited"), scaling=Decimal("1e-8")
    ),
    "0x51fb3da8a67861361281ac56fe2ad8c3b4539ffa": TokenInfo(
        currency=CurrencyInfo(symbol="INSUR", name="InsurChain"), scaling=Decimal("1e-18")
    ),
    "0x5206186997fec1951482c2304a246bef34dcee12": TokenInfo(
        currency=CurrencyInfo(symbol="VEEN", name="LIVEEN"), scaling=Decimal("1e-18")
    ),
    "0x52132a43d7cae69b23abe77b226fa1a5bc66b839": TokenInfo(
        currency=CurrencyInfo(symbol="TMPL", name="Truample"), scaling=Decimal("1e-9")
    ),
    "0x5218e472cfcfe0b64a064f055b43b4cdc9efd3a6": TokenInfo(
        currency=CurrencyInfo(symbol="ERSDL", name="unFederalReserve"), scaling=Decimal("1e-18")
    ),
    "0x5228a22e72ccc52d415ecfd199f99d0665e7733b": TokenInfo(
        currency=CurrencyInfo(symbol="PBTC", name="pTokens BTC"), scaling=Decimal("1e-18")
    ),
    "0x52494fbffe10f8c29411521040ae8618c334981e": TokenInfo(
        currency=CurrencyInfo(symbol="HDR", name="Hedger"), scaling=Decimal("1e-18")
    ),
    "0x526664ca8ff5e5b924270bd6bd89bf5d58fc79cd": TokenInfo(
        currency=CurrencyInfo(symbol="XRPDOOM", name="10X Short XRP Token"), scaling=Decimal("1e-18")
    ),
    "0x5269ed15edd821df35b5434ecbebf7460f4e917b": TokenInfo(
        currency=CurrencyInfo(symbol="CVDA", name="CRYPTOCVDA"), scaling=Decimal("1e-18")
    ),
    "0x526ccc90191a9472299323816bd2c784c0a1bcde": TokenInfo(
        currency=CurrencyInfo(symbol="DBLK", name="DataOnBlock"), scaling=Decimal("1e-18")
    ),
    "0x52956cd6f9d5d8a0ffdce1e9b68ef72cd9d64655": TokenInfo(
        currency=CurrencyInfo(symbol="IZA", name="Inzura"), scaling=Decimal("1e-18")
    ),
    "0x5299d6f7472dcc137d7f3c4bcfbbb514babf341a": TokenInfo(
        currency=CurrencyInfo(symbol="SXMR", name="sXMR"), scaling=Decimal("1e-18")
    ),
    "0x52a7a5b50a567ca6c0a4f85e74b98142eba43f49": TokenInfo(
        currency=CurrencyInfo(symbol="YAB", name="Yet Another Bomb"), scaling=Decimal("1e-0")
    ),
    "0x52a7cb918c11a16958be40cba7e31e32a499a465": TokenInfo(
        currency=CurrencyInfo(symbol="FDX", name="FidentiaX"), scaling=Decimal("1e-18")
    ),
    "0x52ab3e06a566aecb7559aba03a0228f416bd7b26": TokenInfo(
        currency=CurrencyInfo(symbol="BILI.CX", name="Bilibili Inc"), scaling=Decimal("1e-8")
    ),
    "0x52db8ebf894036ec997da693c5fa237a4fb69d10": TokenInfo(
        currency=CurrencyInfo(symbol="CVH", name="Curriculum Vitae"), scaling=Decimal("1e-18")
    ),
    "0x52e30201f31283dc5f7928b4198896083f604416": TokenInfo(
        currency=CurrencyInfo(symbol="MLD", name="MOLD"), scaling=Decimal("1e-18")
    ),
    "0x52ed883e23a22fb0ace4629f0dc5c6348580d1ce": TokenInfo(
        currency=CurrencyInfo(symbol="KRC", name="Kineticex"), scaling=Decimal("1e-18")
    ),
    "0x52fb36c83ad33c1824912fc81071ca5eeb8ab390": TokenInfo(
        currency=CurrencyInfo(symbol="FID", name="Fidelium"), scaling=Decimal("1e-18")
    ),
    "0x5301e9f1b9156e600af0e08ad57a6e725a6cd479": TokenInfo(
        currency=CurrencyInfo(symbol="ROMTV", name="ROMTV"), scaling=Decimal("1e-18")
    ),
    "0x53066cddbc0099eb6c96785d9b3df2aaeede5da3": TokenInfo(
        currency=CurrencyInfo(symbol="PNT", name="Penta Network Token"), scaling=Decimal("1e-18")
    ),
    "0x530ad8376e292b5b17f4c95aab8767cd4e90de06": TokenInfo(
        currency=CurrencyInfo(symbol="OSTK.CX", name="Overstock.com inc"), scaling=Decimal("1e-8")
    ),
    "0x5319e86f0e41a06e49eb37046b8c11d78bcad68c": TokenInfo(
        currency=CurrencyInfo(symbol="ZLW", name="Zelwin"), scaling=Decimal("1e-18")
    ),
    "0x5322a3556f979ce2180b30e689a9436fddcb1021": TokenInfo(
        currency=CurrencyInfo(symbol="YTSLA", name="yTSLA Finance"), scaling=Decimal("1e-18")
    ),
    "0x532843f66375d5257ea34f723c6c2723ccf7b7a2": TokenInfo(
        currency=CurrencyInfo(symbol="KYT", name="KEYRPTO"), scaling=Decimal("1e-18")
    ),
    "0x5330a5805b9db68ebcf5247bbc9097163c1c2442": TokenInfo(
        currency=CurrencyInfo(symbol="EXP", name="Exchange Payment Coin"), scaling=Decimal("1e-18")
    ),
    "0x53352e7d6620cc931c0c9318166ae2a92c1a4666": TokenInfo(
        currency=CurrencyInfo(symbol="AIM", name="AI Mining"), scaling=Decimal("1e-18")
    ),
    "0x533ef0984b2faa227acc620c67cce12aa39cd8cd": TokenInfo(
        currency=CurrencyInfo(symbol="XGM", name="XaurumGamma"), scaling=Decimal("1e-8")
    ),
    "0x534479d1f4e31bc8f3265009b2b05f89dc3b9af1": TokenInfo(
        currency=CurrencyInfo(symbol="OA", name="Open Aurum"), scaling=Decimal("1e-8")
    ),
    "0x534546c490a4ed2a9d0c3555447bb9b4b01bcb9e": TokenInfo(
        currency=CurrencyInfo(symbol="YTRO", name="Yotro"), scaling=Decimal("1e-17")
    ),
    "0x5347bfbec9803c6850dfd55d797e9ecf8689b688": TokenInfo(
        currency=CurrencyInfo(symbol="BRC", name="Bisercoin"), scaling=Decimal("1e-18")
    ),
    "0x536381a8628dbcc8c70ac9a30a7258442eab4c92": TokenInfo(
        currency=CurrencyInfo(symbol="PAN", name="Pantos"), scaling=Decimal("1e-8")
    ),
    "0x5378a8bfe52592fcf436dfbe3cd389c494706c5f": TokenInfo(
        currency=CurrencyInfo(symbol="NKCL", name="NKCL"), scaling=Decimal("1e-18")
    ),
    "0x5378ae149e06a6a6367e1e65332e4680dde53e07": TokenInfo(
        currency=CurrencyInfo(symbol="XPAY", name="XPAY Token"), scaling=Decimal("1e-8")
    ),
    "0x53884b61963351c283118a8e1fc05ba464a11959": TokenInfo(
        currency=CurrencyInfo(symbol="MNS", name="Monnos"), scaling=Decimal("1e-18")
    ),
    "0x53893a4a67d4392ebebdf1a683e98e1c577ab6c1": TokenInfo(
        currency=CurrencyInfo(symbol="MBS", name="MicroBloodScience"), scaling=Decimal("1e-18")
    ),
    "0x5394794be8b6ed5572fcd6b27103f46b5f390e8f": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNIYFIWETH", name="Aave AMM UniYFIWETH"), scaling=Decimal("1e-18")
    ),
    "0x539efe69bcdd21a83efd9122571a64cc25e0282b": TokenInfo(
        currency=CurrencyInfo(symbol="BLUE", name="Blue Protocol"), scaling=Decimal("1e-8")
    ),
    "0x539f3615c1dbafa0d008d87504667458acbd16fa": TokenInfo(
        currency=CurrencyInfo(symbol="FERA", name="Fera"), scaling=Decimal("1e-18")
    ),
    "0x53db6b7fee89383435e424764a8478acda4dd2cd": TokenInfo(
        currency=CurrencyInfo(symbol="VIBS", name="Vibz8"), scaling=Decimal("1e-18")
    ),
    "0x53f32fe62e432a43a61dfd0e23f4991d0f4bba0a": TokenInfo(
        currency=CurrencyInfo(symbol="EDC", name="Africa Development Chain"), scaling=Decimal("1e-18")
    ),
    "0x540e5fff293f523acd26291b5bc7ac5713991feb": TokenInfo(
        currency=CurrencyInfo(symbol="PTS", name="Pitiscoin"), scaling=Decimal("1e-8")
    ),
    "0x542156d51d10db5accb99f9db7e7c91b74e80a2c": TokenInfo(
        currency=CurrencyInfo(symbol="LINKETHPA", name="ETH/LINK Price Action Candlestick Set"),
        scaling=Decimal("1e-18"),
    ),
    "0x54325e3946c3f558162f8a7e79a5dc89e3fbb2f4": TokenInfo(
        currency=CurrencyInfo(symbol="GCD", name="Global Currency Development"), scaling=Decimal("1e-2")
    ),
    "0x5432c580e34f590f4dd901b825ddeb92e905e826": TokenInfo(
        currency=CurrencyInfo(symbol="TXH", name="TradeX Token"), scaling=Decimal("1e-18")
    ),
    "0x54355ae0485f9420e6ce4c00c10172dc8e5728a3": TokenInfo(
        currency=CurrencyInfo(symbol="100WETH", name="100 Waves ETH/USD Ether Hoard Set"), scaling=Decimal("1e-18")
    ),
    "0x543ff227f64aa17ea132bf9886cab5db55dcaddf": TokenInfo(
        currency=CurrencyInfo(symbol="GEN", name="DAOstack"), scaling=Decimal("1e-18")
    ),
    "0x544c42fbb96b39b21df61cf322b5edc285ee7429": TokenInfo(
        currency=CurrencyInfo(symbol="INSUR", name="InsurAce"), scaling=Decimal("1e-18")
    ),
    "0x5456bc77dd275c45c3c15f0cf936b763cf57c3b5": TokenInfo(
        currency=CurrencyInfo(symbol="ANCT", name="Anchor"), scaling=Decimal("1e-8")
    ),
    "0x54672394026d16f223fdcd912973218adb4b0e6d": TokenInfo(
        currency=CurrencyInfo(symbol="G4B", name="Game4Bitcoin"), scaling=Decimal("1e-2")
    ),
    "0x54a9ed327f2614316914c3f3a782a77d0aa47aee": TokenInfo(
        currency=CurrencyInfo(symbol="CNCT", name="Connect"), scaling=Decimal("1e-18")
    ),
    "0x54ad74edeab48e09ccc43ee324f2603071dad72b": TokenInfo(
        currency=CurrencyInfo(symbol="DTOP", name="DTOP Token"), scaling=Decimal("1e-18")
    ),
    "0x54b293226000ccbfc04df902eec567cb4c35a903": TokenInfo(
        currency=CurrencyInfo(symbol="RTN", name="RiderToken"), scaling=Decimal("1e-18")
    ),
    "0x54b8c98268da0055971652a95f2bfd3a9349a38c": TokenInfo(
        currency=CurrencyInfo(symbol="PRINT", name="Printer.Finance"), scaling=Decimal("1e-18")
    ),
    "0x54c9ea2e9c9e8ed865db4a4ce6711c2a0d5063ba": TokenInfo(
        currency=CurrencyInfo(symbol="BART", name="BarterTrade"), scaling=Decimal("1e-18")
    ),
    "0x54e8371c1ec43e58fb53d4ef4ed463c17ba8a6be": TokenInfo(
        currency=CurrencyInfo(symbol="ETHEMAAPY", name="ETH 26 EMA Crossover Yield II"), scaling=Decimal("1e-18")
    ),
    "0x54ee01beb60e745329e6a8711ad2d6cb213e38d7": TokenInfo(
        currency=CurrencyInfo(symbol="DFSOCIAL", name="DefiSocial"), scaling=Decimal("1e-18")
    ),
    "0x5512e1d6a7be424b4323126b4f9e86d023f95764": TokenInfo(
        currency=CurrencyInfo(symbol="PTWO", name="PornTokenV2"), scaling=Decimal("1e-18")
    ),
    "0x5515950f7bf8d6acdf4ae98c33bf996bd0ed6f6f": TokenInfo(
        currency=CurrencyInfo(symbol="FNX", name="FinanceX token"), scaling=Decimal("1e-18")
    ),
    "0x55296f69f40ea6d20e478533c15a6b08b654e758": TokenInfo(
        currency=CurrencyInfo(symbol="XYO", name="XYO Network"), scaling=Decimal("1e-18")
    ),
    "0x5547136b913b68881596275ace01e9a589c5b16b": TokenInfo(
        currency=CurrencyInfo(symbol="BTCHG", name="BITCOINHEDGE"), scaling=Decimal("1e-18")
    ),
    "0x554c20b7c486beee439277b4540a434566dc4c02": TokenInfo(
        currency=CurrencyInfo(symbol="HST", name="Decision Token"), scaling=Decimal("1e-18")
    ),
    "0x554ce35a973a1317f71885696cbe4ddf8af177ab": TokenInfo(
        currency=CurrencyInfo(symbol="WATB", name="WhaleChain"), scaling=Decimal("1e-18")
    ),
    "0x554ffc77f4251a9fb3c0e3590a6a205f8d4e067d": TokenInfo(
        currency=CurrencyInfo(symbol="ZMN", name="ZMINE Token"), scaling=Decimal("1e-18")
    ),
    "0x5554e04e76533e1d14c52f05beef6c9d329e1e30": TokenInfo(
        currency=CurrencyInfo(symbol="NIO", name="Autonio"), scaling=Decimal("1e-0")
    ),
    "0x5559bbafab7fbec1fd0f5db5b71f042520fde9a3": TokenInfo(
        currency=CurrencyInfo(symbol="AIR.CX", name="Airbus SE"), scaling=Decimal("1e-8")
    ),
    "0x555d051538c7a13712f1f590fa6b4c176ca4529f": TokenInfo(
        currency=CurrencyInfo(symbol="IOWN", name="iOWN Token"), scaling=Decimal("1e-18")
    ),
    "0x556148562d5ddeb72545d7ec4b3ec8edc8f55ba7": TokenInfo(
        currency=CurrencyInfo(symbol="PRDX", name="Predix Network"), scaling=Decimal("1e-18")
    ),
    "0x55648de19836338549130b1af587f16bea46f66b": TokenInfo(
        currency=CurrencyInfo(symbol="PBL", name="Pebbles"), scaling=Decimal("1e-18")
    ),
    "0x55675e0d2551a34c2e3c68fa83b5108527957fdd": TokenInfo(
        currency=CurrencyInfo(symbol="IST34", name="IST34 Token"), scaling=Decimal("1e-18")
    ),
    "0x556ea1fe7cb0964e7de8dfe6cde63f1e40908541": TokenInfo(
        currency=CurrencyInfo(symbol="DUSD", name="DigitalUSD"), scaling=Decimal("1e-18")
    ),
    "0x557b933a7c2c45672b610f8954a3deb39a51a8ca": TokenInfo(
        currency=CurrencyInfo(symbol="REVV", name="REVV"), scaling=Decimal("1e-18")
    ),
    "0x5580894f975ff049857147c8410d9b0db00d9c5e": TokenInfo(
        currency=CurrencyInfo(symbol="ASCC", name="All Star Community Coin"), scaling=Decimal("1e-18")
    ),
    "0x5580ab97f226c324c671746a1787524aef42e415": TokenInfo(
        currency=CurrencyInfo(symbol="JUL", name="JustLiquidity"), scaling=Decimal("1e-18")
    ),
    "0x5581c0bc21a762e43d148b06d310f088b6cf97b3": TokenInfo(
        currency=CurrencyInfo(symbol="SE", name="Swift Express Token"), scaling=Decimal("1e-18")
    ),
    "0x558a069a3a1a1e72398607b9e3577fce1c67ea63": TokenInfo(
        currency=CurrencyInfo(symbol="JPYQ", name="JPYQ Stablecoin by Q DAO v1.0"), scaling=Decimal("1e-18")
    ),
    "0x558ec3152e2eb2174905cd19aea4e34a23de9ad6": TokenInfo(
        currency=CurrencyInfo(symbol="BRD", name="Bread"), scaling=Decimal("1e-18")
    ),
    "0x55a290f08bb4cae8dcf1ea5635a3fcfd4da60456": TokenInfo(
        currency=CurrencyInfo(symbol="BITTO", name="BITTO"), scaling=Decimal("1e-18")
    ),
    "0x55a34e043fe779a2db61400a5ec72131d372afcb": TokenInfo(
        currency=CurrencyInfo(symbol="ETE", name="Elite Token"), scaling=Decimal("1e-18")
    ),
    "0x55af5865807b196bd0197e0902746f31fbccfa58": TokenInfo(
        currency=CurrencyInfo(symbol="BOO", name="Spookyswap"), scaling=Decimal("1e-18")
    ),
    "0x55b54d8fb1640d1321d5164590e7b020ba43def2": TokenInfo(
        currency=CurrencyInfo(symbol="XRPHEDGE", name="1X Short XRP Token"), scaling=Decimal("1e-18")
    ),
    "0x55b9a11c2e8351b4ffc7b11561148bfac9977855": TokenInfo(
        currency=CurrencyInfo(symbol="DIGIX", name="Digix"), scaling=Decimal("1e-0")
    ),
    "0x55c2a0c171d920843560594de3d6eecc09efc098": TokenInfo(
        currency=CurrencyInfo(symbol="PEXT", name="PEX-Token"), scaling=Decimal("1e-4")
    ),
    "0x55cd673c21f0c5d8244aced99f874614a0a83de9": TokenInfo(
        currency=CurrencyInfo(symbol="EBAY.CX", name="eBay"), scaling=Decimal("1e-8")
    ),
    "0x55d0bb8d7e7fbf5b863c7923c4645ff83c3d0033": TokenInfo(
        currency=CurrencyInfo(symbol="GWIT", name="Global Women Investment Token"), scaling=Decimal("1e-18")
    ),
    "0x55eb5288c9b65037a4cd2289637f38a4f9db3a6b": TokenInfo(
        currency=CurrencyInfo(symbol="KGW", name="KAWANGGAWA"), scaling=Decimal("1e-18")
    ),
    "0x55f93985431fc9304077687a35a1ba103dc1e081": TokenInfo(
        currency=CurrencyInfo(symbol="SMT", name="SmartMesh Token"), scaling=Decimal("1e-18")
    ),
    "0x56015bbe3c01fe05bc30a8a9a9fd9a88917e7db3": TokenInfo(
        currency=CurrencyInfo(symbol="CAT", name="Cat Token"), scaling=Decimal("1e-18")
    ),
    "0x562952c749d05dca4cd004489a153c7ee7e58240": TokenInfo(
        currency=CurrencyInfo(symbol="PAL", name="Pally"), scaling=Decimal("1e-18")
    ),
    "0x565ac8639e53a4bff4afb34ac63a49d7bf01500e": TokenInfo(
        currency=CurrencyInfo(symbol="XPAYPRO", name="XPAY Pro Token"), scaling=Decimal("1e-18")
    ),
    "0x56687cf29ac9751ce2a4e764680b6ad7e668942e": TokenInfo(
        currency=CurrencyInfo(symbol="JAMM", name="FlynnJamm"), scaling=Decimal("1e-4")
    ),
    "0x566fd7999b1fc3988022bd38507a48f0bcf22c77": TokenInfo(
        currency=CurrencyInfo(symbol="TRCN", name="The Real Coin"), scaling=Decimal("1e-18")
    ),
    "0x566ff8d8bd6de69d2af4e3cf9153e2cc77c7972f": TokenInfo(
        currency=CurrencyInfo(symbol="VIXG", name="VianeXGold"), scaling=Decimal("1e-18")
    ),
    "0x567287d4f42086beab4b36de9af21c70adec6760": TokenInfo(
        currency=CurrencyInfo(symbol="LATINO", name="Latino Token"), scaling=Decimal("1e-4")
    ),
    "0x567300e14f8d67e1f6720a95291dce2511a86723": TokenInfo(
        currency=CurrencyInfo(symbol="HSN", name="Helper Search Token"), scaling=Decimal("1e-18")
    ),
    "0x567d297d0cbb66195b268162a4547f220ef49c51": TokenInfo(
        currency=CurrencyInfo(symbol="SERUM", name="VaccinaCoin"), scaling=Decimal("1e-18")
    ),
    "0x56a86d648c435dc707c8405b78e2ae8eb4e60ba4": TokenInfo(
        currency=CurrencyInfo(symbol="STACK", name="StackOS"), scaling=Decimal("1e-18")
    ),
    "0x56aa298a19c93c6801fdde870fa63ef75cc0af72": TokenInfo(
        currency=CurrencyInfo(symbol="MBABA", name="Mirrored Alibaba"), scaling=Decimal("1e-18")
    ),
    "0x56b6431f45d08eed55f34371386326c739eacbcc": TokenInfo(
        currency=CurrencyInfo(symbol="ETHM", name="Ethereum Meta"), scaling=Decimal("1e-18")
    ),
    "0x56ba2ee7890461f463f7be02aac3099f6d5811a8": TokenInfo(
        currency=CurrencyInfo(symbol="CAT", name="BlockCAT"), scaling=Decimal("1e-18")
    ),
    "0x56be94d29e1125d2d61d06629c1b251d72c1b3b3": TokenInfo(
        currency=CurrencyInfo(symbol="HUSL", name="Hustle Token"), scaling=Decimal("1e-18")
    ),
    "0x56d1ae30c97288da4b58bc39f026091778e4e316": TokenInfo(
        currency=CurrencyInfo(symbol="DAGT", name="Digital Asset Guarantee Token"), scaling=Decimal("1e-18")
    ),
    "0x56d811088235f11c8920698a204a5010a788f4b3": TokenInfo(
        currency=CurrencyInfo(symbol="BZRX", name="bZx Protocol"), scaling=Decimal("1e-18")
    ),
    "0x56e0b2c7694e6e10391e870774daa45cf6583486": TokenInfo(
        currency=CurrencyInfo(symbol="DUO", name="DUO Network"), scaling=Decimal("1e-18")
    ),
    "0x56f71ce60b10192901e97f281d2f230eb5ab27aa": TokenInfo(
        currency=CurrencyInfo(symbol="ONEM.CX", name="1Life Healthcare Inc"), scaling=Decimal("1e-8")
    ),
    "0x572e6f318056ba0c5d47a422653113843d250691": TokenInfo(
        currency=CurrencyInfo(symbol="XNT", name="EXANTE Token"), scaling=Decimal("1e-0")
    ),
    "0x5732046a883704404f284ce41ffadd5b007fd668": TokenInfo(
        currency=CurrencyInfo(symbol="BLZ", name="Bluzelle"), scaling=Decimal("1e-18")
    ),
    "0x574a37b7244dabb08ce1618193f818f1c85180e6": TokenInfo(
        currency=CurrencyInfo(symbol="XRPMOON", name="10X Long XRP Token"), scaling=Decimal("1e-18")
    ),
    "0x574b36bced443338875d171cc377e691f7d4f887": TokenInfo(
        currency=CurrencyInfo(symbol="CO2", name="Co2Bit"), scaling=Decimal("1e-18")
    ),
    "0x574f84108a98c575794f75483d801d1d5dc861a5": TokenInfo(
        currency=CurrencyInfo(symbol="ROX", name="Robotina"), scaling=Decimal("1e-18")
    ),
    "0x57652fc91f522f9eff0b38cdf1d51f5fb5764215": TokenInfo(
        currency=CurrencyInfo(symbol="BUD", name="Buddy"), scaling=Decimal("1e-18")
    ),
    "0x57700244b20f84799a31c6c96dadff373ca9d6c5": TokenInfo(
        currency=CurrencyInfo(symbol="TRUST", name="TrustDAO"), scaling=Decimal("1e-18")
    ),
    "0x57838ff342f36a1ec18224981ea8715a4667fb3a": TokenInfo(
        currency=CurrencyInfo(symbol="QUBE", name="Qube"), scaling=Decimal("1e-18")
    ),
    "0x578b49c45961f98d8df92854b53f1641af0a5036": TokenInfo(
        currency=CurrencyInfo(symbol="LINKA", name="LINKA"), scaling=Decimal("1e-18")
    ),
    "0x579353231f3540b218239774422962c64a3693e7": TokenInfo(
        currency=CurrencyInfo(symbol="BCTR", name="Bitcratic Revenue"), scaling=Decimal("1e-18")
    ),
    "0x579cea1889991f68acc35ff5c3dd0621ff29b0c9": TokenInfo(
        currency=CurrencyInfo(symbol="IQ", name="IQ"), scaling=Decimal("1e-18")
    ),
    "0x57a2bcba1902696b08b93c87451be71b024d2a4c": TokenInfo(
        currency=CurrencyInfo(symbol="wNXM", name="Wrapped NXM"), scaling=Decimal("1e-18")
    ),
    "0x57ab1e02fee23774580c119740129eac7081e9d3": TokenInfo(
        currency=CurrencyInfo(symbol="sUSD", name="Synth USD"), scaling=Decimal("1e-18")
    ),
    "0x57ab1ec28d129707052df4df418d58a2d46d5f51": TokenInfo(
        currency=CurrencyInfo(symbol="SUSD", name="sUSD"), scaling=Decimal("1e-18")
    ),
    "0x57b1b057330d428199477b463f93a1fc9e61f94f": TokenInfo(
        currency=CurrencyInfo(symbol="TXT.CX", name="Textron"), scaling=Decimal("1e-8")
    ),
    "0x57b946008913b82e4df85f501cbaed910e58d26c": TokenInfo(
        currency=CurrencyInfo(symbol="POND", name="Marlin"), scaling=Decimal("1e-18")
    ),
    "0x57c75eccc8557136d32619a191fbcdc88560d711": TokenInfo(
        currency=CurrencyInfo(symbol="VDG", name="VeriDocGlobal"), scaling=Decimal("1e-0")
    ),
    "0x57c8d5d5b87a1580fdaf996cef674bb0d7f14c98": TokenInfo(
        currency=CurrencyInfo(symbol="ODIN", name="OdinBrowser"), scaling=Decimal("1e-18")
    ),
    "0x57e2b08e74b2b2c041e8b7bbb48bf1cdc6b8afb6": TokenInfo(
        currency=CurrencyInfo(symbol="ETCHEDGE", name="1X Short Ethereum Classic Token"), scaling=Decimal("1e-18")
    ),
    "0x57e83505827788c9f92bcfd398a51a7b0c83dd8e": TokenInfo(
        currency=CurrencyInfo(symbol="CTS", name="ChainLink Trading Set"), scaling=Decimal("1e-18")
    ),
    "0x5807ca447851c98569c567963b25b1c83d41bebc": TokenInfo(
        currency=CurrencyInfo(
            symbol="REALTOKEN-10024-10028-APPOLINE-ST-DETROIT-MI", name="RealToken 10024 10028 Appoline St Detroit MI"
        ),
        scaling=Decimal("1e-18"),
    ),
    "0x580c8520deda0a441522aeae0f9f7a5f29629afa": TokenInfo(
        currency=CurrencyInfo(symbol="DAWN", name="Dawn Protocol"), scaling=Decimal("1e-18")
    ),
    "0x581911b360b6eb3a14ef295a83a91dc2bce2d6f7": TokenInfo(
        currency=CurrencyInfo(symbol="MVC", name="MileVerse"), scaling=Decimal("1e-18")
    ),
    "0x584936357d68f5143f12e2e64f0089db93814dad": TokenInfo(
        currency=CurrencyInfo(symbol="ALGOBULL", name="3X Long Algorand Token"), scaling=Decimal("1e-18")
    ),
    "0x584b44853680ee34a0f337b712a8f66d816df151": TokenInfo(
        currency=CurrencyInfo(symbol="AIDOC", name="AI Doctor"), scaling=Decimal("1e-18")
    ),
    "0x584bc13c7d411c00c01a62e8019472de68768430": TokenInfo(
        currency=CurrencyInfo(symbol="HEGIC", name="Hegic"), scaling=Decimal("1e-18")
    ),
    "0x5850700e214c16c73d1778b2886c01639e69faa3": TokenInfo(
        currency=CurrencyInfo(symbol="RGC", name="ROGANCOIN"), scaling=Decimal("1e-18")
    ),
    "0x585c2cf94c41b528ec7329cbc3cde3c4f8d268db": TokenInfo(
        currency=CurrencyInfo(symbol="ETHLOVOL", name="ETH Range Bound Low Volatility Set"), scaling=Decimal("1e-18")
    ),
    "0x588047365df5ba589f923604aac23d673555c623": TokenInfo(
        currency=CurrencyInfo(symbol="NAVI", name="Naviaddress"), scaling=Decimal("1e-18")
    ),
    "0x5881da4527bcdc44a100f8ba2efc4039243d2c07": TokenInfo(
        currency=CurrencyInfo(symbol="LGBTQ", name="Pride"), scaling=Decimal("1e-1")
    ),
    "0x5884969ec0480556e11d119980136a4c17edded1": TokenInfo(
        currency=CurrencyInfo(symbol="PET", name="Pethereum"), scaling=Decimal("1e-18")
    ),
    "0x58959e0c71080434f237bd42d07cd84b74cef438": TokenInfo(
        currency=CurrencyInfo(symbol="TSR", name="Tesra"), scaling=Decimal("1e-5")
    ),
    "0x589891a198195061cb8ad1a75357a3b7dbadd7bc": TokenInfo(
        currency=CurrencyInfo(symbol="COS", name="Contentos"), scaling=Decimal("1e-18")
    ),
    "0x58a2263f77e1b23a74a3d99b9d01506da308800b": TokenInfo(
        currency=CurrencyInfo(symbol="NTP", name="NETWORK TOKEN PAYMENT"), scaling=Decimal("1e-8")
    ),
    "0x58a28b87fd6112ee43262c80ad1098f1709350eb": TokenInfo(
        currency=CurrencyInfo(symbol="VNET.CX", name="21Vianet Group, Inc."), scaling=Decimal("1e-8")
    ),
    "0x58a3520d738b268c2353ecee518a1ad8e28e4ae5": TokenInfo(
        currency=CurrencyInfo(symbol="HDI", name="HEIDI"), scaling=Decimal("1e-2")
    ),
    "0x58a4884182d9e835597f405e5f258290e46ae7c2": TokenInfo(
        currency=CurrencyInfo(symbol="NOAH", name="NOAHCOIN"), scaling=Decimal("1e-18")
    ),
    "0x58a5d3e4873a75b07fb3c7cf477eebc44ea73b3b": TokenInfo(
        currency=CurrencyInfo(symbol="KAIJU", name="Kaiju"), scaling=Decimal("1e-4")
    ),
    "0x58b6a8a3302369daec383334672404ee733ab239": TokenInfo(
        currency=CurrencyInfo(symbol="LPT", name="Livepeer"), scaling=Decimal("1e-18")
    ),
    "0x58bf7df57d9da7113c4ccb49d8463d4908c735cb": TokenInfo(
        currency=CurrencyInfo(symbol="SPARC", name="Science Power and Research Coin"), scaling=Decimal("1e-18")
    ),
    "0x58c69ed6cd6887c0225d1fccecc055127843c69b": TokenInfo(
        currency=CurrencyInfo(symbol="HLC", name="HalalChain"), scaling=Decimal("1e-9")
    ),
    "0x58ca3065c0f24c7c96aee8d6056b5b5decf9c2f8": TokenInfo(
        currency=CurrencyInfo(symbol="GXC", name="GXC"), scaling=Decimal("1e-10")
    ),
    "0x59061b6f26bb4a9ce5828a19d35cfd5a4b80f056": TokenInfo(
        currency=CurrencyInfo(symbol="LGD", name="Legends"), scaling=Decimal("1e-8")
    ),
    "0x5913d0f34615923552ee913dbe809f9f348e706e": TokenInfo(
        currency=CurrencyInfo(symbol="BMJ", name="BMJ Master Nodes"), scaling=Decimal("1e-18")
    ),
    "0x59165e15026dd0712380cffe71e4f5d1ef5f6af0": TokenInfo(
        currency=CurrencyInfo(symbol="YFU", name="yfiu.finance"), scaling=Decimal("1e-18")
    ),
    "0x592ef68c18f05a22c5890263dea5d952dd140d2a": TokenInfo(
        currency=CurrencyInfo(symbol="EXCHBULL", name="3X Long Exchange Token Index Token"), scaling=Decimal("1e-18")
    ),
    "0x593114f03a0a575aece9ed675e52ed68d2172b8c": TokenInfo(
        currency=CurrencyInfo(symbol="BDP", name="BidiPass"), scaling=Decimal("1e-18")
    ),
    "0x5935ffc231e93ac04daa089c0f1b94d0fb2449de": TokenInfo(
        currency=CurrencyInfo(symbol="KNV", name="Kanva"), scaling=Decimal("1e-8")
    ),
    "0x59416a25628a76b4730ec51486114c32e0b582a1": TokenInfo(
        currency=CurrencyInfo(symbol="☀️ PLASMA", name="☀️ PLASMA TOKEN"), scaling=Decimal("1e-6")
    ),
    "0x595832f8fc6bf59c85c527fec3740a1b7a361269": TokenInfo(
        currency=CurrencyInfo(symbol="POWR", name="Power Ledger"), scaling=Decimal("1e-6")
    ),
    "0x5963fd7ca9b17b85768476019f81cb43d9d1818e": TokenInfo(
        currency=CurrencyInfo(symbol="YESTRUMP", name="Dai If Trump Wins The 2020 Election"), scaling=Decimal("1e-18")
    ),
    "0x5978708d6cce1cc9640eed47422d64c91bbd5171": TokenInfo(
        currency=CurrencyInfo(symbol="LOL", name="LOLTOKEN"), scaling=Decimal("1e-18")
    ),
    "0x5979f50f1d4c08f9a53863c2f39a7b0492c38d0f": TokenInfo(
        currency=CurrencyInfo(symbol="PLTC", name="pTokens LTC"), scaling=Decimal("1e-18")
    ),
    "0x597cd1b89f4114dc8d59b0598d15d023d873a006": TokenInfo(
        currency=CurrencyInfo(symbol="EMET", name="Ecometh Token"), scaling=Decimal("1e-8")
    ),
    "0x599346779e90fc3f5f997b5ea715349820f91571": TokenInfo(
        currency=CurrencyInfo(symbol="STN", name="Saturn"), scaling=Decimal("1e-4")
    ),
    "0x59a17c58daaee299b39a060b9de67bf7c829e4d3": TokenInfo(
        currency=CurrencyInfo(symbol="SHEL", name="shelterDAO"), scaling=Decimal("1e-18")
    ),
    "0x59a2eb1675f31406e3bc00262a6dc0d98e0376b1": TokenInfo(
        currency=CurrencyInfo(symbol="XUSB", name="XUSB"), scaling=Decimal("1e-2")
    ),
    "0x59a921db27dd6d4d974745b7ffc5c33932653442": TokenInfo(
        currency=CurrencyInfo(symbol="MGOOGL", name="Mirrored Google"), scaling=Decimal("1e-18")
    ),
    "0x59ad6061a0be82155e7acce9f0c37bf59f9c1e3c": TokenInfo(
        currency=CurrencyInfo(symbol="LIQLO", name="Liquid Lottery RTC"), scaling=Decimal("1e-18")
    ),
    "0x59af0356cdebd1fa23ae5dadff9170bbfc31278c": TokenInfo(
        currency=CurrencyInfo(symbol="FF1", name="Two Prime FF1 Token"), scaling=Decimal("1e-18")
    ),
    "0x59b8d11d50ab6615f9cd430743baf646fb8966c6": TokenInfo(
        currency=CurrencyInfo(symbol="LAMBO", name="Lambo Coin"), scaling=Decimal("1e-18")
    ),
    "0x59be937f05cf2c406b61c42c6c82a093fa54edfe": TokenInfo(
        currency=CurrencyInfo(symbol="PLX", name="PlayX"), scaling=Decimal("1e-9")
    ),
    "0x59c337ef937d0ba9cb1cc47d4e6ded632d22d623": TokenInfo(
        currency=CurrencyInfo(symbol="TCH", name="Tchain"), scaling=Decimal("1e-18")
    ),
    "0x59c3ba7a0a4c26955037710654f60d368303b3e1": TokenInfo(
        currency=CurrencyInfo(symbol="ZNA", name="Zenome"), scaling=Decimal("1e-18")
    ),
    "0x59db60bd41bbc8ca4c1efee6ea2a97eae1e30cf5": TokenInfo(
        currency=CurrencyInfo(symbol="MIDBULL", name="3X Long Midcap Index Token"), scaling=Decimal("1e-18")
    ),
    "0x59db9fde270b39a07f38fa3106a760829074c7d9": TokenInfo(
        currency=CurrencyInfo(symbol="PIPS", name="PIPSCHAIN"), scaling=Decimal("1e-18")
    ),
    "0x59e7b5db9be0bdd26fa048d39e01fee456ab674e": TokenInfo(
        currency=CurrencyInfo(symbol="YFB2", name="Yearn Finance Bit2"), scaling=Decimal("1e-18")
    ),
    "0x59ebb83b72d735ac1ecb824cb3f8253fa5d49d00": TokenInfo(
        currency=CurrencyInfo(symbol="DPST", name="DPS Chain"), scaling=Decimal("1e-0")
    ),
    "0x5a143f78bb66294ff37c47b5164584475b932bab": TokenInfo(
        currency=CurrencyInfo(symbol="YHFI", name="Yearn Hold Finance"), scaling=Decimal("1e-18")
    ),
    "0x5a246a981d61d8bc5c254c6eba1340796fb97e5f": TokenInfo(
        currency=CurrencyInfo(symbol="VNC", name="VNC"), scaling=Decimal("1e-18")
    ),
    "0x5a386eb0fcbfee3f0d759e263053c09162ff102d": TokenInfo(
        currency=CurrencyInfo(symbol="WOONK", name="Woonkly"), scaling=Decimal("1e-18")
    ),
    "0x5a3c9a1725aa82690ee0959c89abe96fd1b527ee": TokenInfo(
        currency=CurrencyInfo(symbol="PPI", name="PiedPiperCoin"), scaling=Decimal("1e-18")
    ),
    "0x5a40724dcc5ac476f189cdf1b45bdb166287df5f": TokenInfo(
        currency=CurrencyInfo(symbol="EBIRD", name="Ether Bird"), scaling=Decimal("1e-8")
    ),
    "0x5a42991621d2fe5f9fea02143e25e6f79b0e090f": TokenInfo(
        currency=CurrencyInfo(symbol="WR", name="World Referendums"), scaling=Decimal("1e-18")
    ),
    "0x5a4623f305a8d7904ed68638af3b4328678eddbf": TokenInfo(
        currency=CurrencyInfo(symbol="DART", name="dART Insurance"), scaling=Decimal("1e-18")
    ),
    "0x5a4b14aea23a605abc463f04a6b8aaf52dd3e7c6": TokenInfo(
        currency=CurrencyInfo(symbol="HP", name="HeartBout Pay"), scaling=Decimal("1e-18")
    ),
    "0x5a567e28dbfa2bbd3ef13c0a01be114745349657": TokenInfo(
        currency=CurrencyInfo(symbol="HAPPY", name="Happiness"), scaling=Decimal("1e-2")
    ),
    "0x5a666c7d92e5fa7edcb6390e4efd6d0cdd69cf37": TokenInfo(
        currency=CurrencyInfo(symbol="MARSH", name="Unmarshal"), scaling=Decimal("1e-18")
    ),
    "0x5a84969bb663fb64f6d015dcf9f622aedc796750": TokenInfo(
        currency=CurrencyInfo(symbol="IDCE", name="iDice"), scaling=Decimal("1e-18")
    ),
    "0x5a98fcbea516cf06857215779fd812ca3bef1b32": TokenInfo(
        currency=CurrencyInfo(symbol="LDO", name="Lido DAO"), scaling=Decimal("1e-18")
    ),
    "0x5a9bf6badcd24fe0d58e1087290c2fe2c728736a": TokenInfo(
        currency=CurrencyInfo(symbol="18C", name="Block 18"), scaling=Decimal("1e-18")
    ),
    "0x5a9f5992085e8a25a45716cb6f8ff5b57a05d332": TokenInfo(
        currency=CurrencyInfo(symbol="CDR", name="Communication Development Resources Token"), scaling=Decimal("1e-8")
    ),
    "0x5aa485e6b794bcf5f834bf5c7ff43b9b83322764": TokenInfo(
        currency=CurrencyInfo(symbol="MANDI", name="Mandi Token"), scaling=Decimal("1e-8")
    ),
    "0x5aaa2182459377b6ca18b10712f9f602140764af": TokenInfo(
        currency=CurrencyInfo(symbol="EVT", name="Elevation Token"), scaling=Decimal("1e-8")
    ),
    "0x5aaefe84e0fb3dd1f0fcff6fa7468124986b91bd": TokenInfo(
        currency=CurrencyInfo(symbol="EVED", name="Evedo"), scaling=Decimal("1e-18")
    ),
    "0x5ab55ec290beacae98f54c3eb70860460b167c3c": TokenInfo(
        currency=CurrencyInfo(symbol="RM", name="RiverMount"), scaling=Decimal("1e-18")
    ),
    "0x5ab793e36070f0fac928ea15826b0c1bc5365119": TokenInfo(
        currency=CurrencyInfo(symbol="YUKI", name="YUKI COIN"), scaling=Decimal("1e-8")
    ),
    "0x5abaff0b83f81dc061c590aadcba013c69237fd7": TokenInfo(
        currency=CurrencyInfo(symbol="JADE", name="Jade Token"), scaling=Decimal("1e-18")
    ),
    "0x5abfd418adb35e89c68313574eb16bdffc15e607": TokenInfo(
        currency=CurrencyInfo(symbol="TMV", name="Timvi"), scaling=Decimal("1e-18")
    ),
    "0x5acd07353106306a6530ac4d49233271ec372963": TokenInfo(
        currency=CurrencyInfo(symbol="ETY", name="Ethereum Cloud"), scaling=Decimal("1e-18")
    ),
    "0x5acd19b9c91e596b1f062f18e3d02da7ed8d1e50": TokenInfo(
        currency=CurrencyInfo(symbol="BTCL", name="BTC Lite"), scaling=Decimal("1e-8")
    ),
    "0x5ad616a2dde10daf9a4dfeeeb2cbba59661f1390": TokenInfo(
        currency=CurrencyInfo(symbol="DG.CX", name="Dollar General"), scaling=Decimal("1e-8")
    ),
    "0x5adc961d6ac3f7062d2ea45fefb8d8167d44b190": TokenInfo(
        currency=CurrencyInfo(symbol="DTH", name="Dether"), scaling=Decimal("1e-18")
    ),
    "0x5ade7ae8660293f2ebfcefaba91d141d72d221e8": TokenInfo(
        currency=CurrencyInfo(symbol="EMN", name="Eminence"), scaling=Decimal("1e-18")
    ),
    "0x5adfbdf9b6db65c71b7f44376549da6798470e1a": TokenInfo(
        currency=CurrencyInfo(symbol="VTM", name="Commercial Vitamins Token"), scaling=Decimal("1e-18")
    ),
    "0x5af2be193a6abca9c8817001f45744777db30756": TokenInfo(
        currency=CurrencyInfo(symbol="VGX", name="Voyager Token"), scaling=Decimal("1e-8")
    ),
    "0x5b0751713b2527d7f002c0c4e2a37e1219610a6b": TokenInfo(
        currency=CurrencyInfo(symbol="HORSE", name="Ethorse"), scaling=Decimal("1e-18")
    ),
    "0x5b09a0371c1da44a8e24d36bf5deb1141a84d875": TokenInfo(
        currency=CurrencyInfo(symbol="MAD", name="MADNetwork"), scaling=Decimal("1e-18")
    ),
    "0x5b11aacb6bddb9ffab908fdce739bf4aed554327": TokenInfo(
        currency=CurrencyInfo(symbol="TDP", name="TrueDeck"), scaling=Decimal("1e-18")
    ),
    "0x5b135d7e2774c801a73208f258123d7623e07784": TokenInfo(
        currency=CurrencyInfo(symbol="SFU", name="Saifu"), scaling=Decimal("1e-18")
    ),
    "0x5b202f04786e6e9c0a689b1506af229f095d2d0e": TokenInfo(
        currency=CurrencyInfo(symbol="BENZI", name="Ben Zi Token"), scaling=Decimal("1e-18")
    ),
    "0x5b26c5d0772e5bbac8b3182ae9a13f9bb2d03765": TokenInfo(
        currency=CurrencyInfo(symbol="LEDU", name="Education Ecosystem"), scaling=Decimal("1e-8")
    ),
    "0x5b2e4a700dfbc560061e957edec8f6eeeb74a320": TokenInfo(
        currency=CurrencyInfo(symbol="INS", name="INS Token"), scaling=Decimal("1e-10")
    ),
    "0x5b3f693efd5710106eb2eac839368364acb5a70f": TokenInfo(
        currency=CurrencyInfo(symbol="RLR", name="Relayer Network (OLD)"), scaling=Decimal("1e-18")
    ),
    "0x5b52b324fc10cb43b9eeadaf9bd15afb98867942": TokenInfo(
        currency=CurrencyInfo(symbol="NYN", name="NYNJACoin"), scaling=Decimal("1e-18")
    ),
    "0x5b5a353fc217ebef77bc7686ea05a003ebdb7d1a": TokenInfo(
        currency=CurrencyInfo(symbol="HGC", name="HiGameCoin"), scaling=Decimal("1e-18")
    ),
    "0x5b5bb9765eff8d26c24b9ff0daa09838a3cd78e9": TokenInfo(
        currency=CurrencyInfo(symbol="BI", name="Bitanium"), scaling=Decimal("1e-4")
    ),
    "0x5b71bee9d961b1b848f8485eec8d8787f80217f5": TokenInfo(
        currency=CurrencyInfo(symbol="BF", name="Bitforex Token"), scaling=Decimal("1e-18")
    ),
    "0x5b7533812759b45c2b44c19e320ba2cd2681b542": TokenInfo(
        currency=CurrencyInfo(symbol="AGIX", name="SingularityNET"), scaling=Decimal("1e-8")
    ),
    "0x5b86b0d1c304c246282dea0e0f21db2baa429b31": TokenInfo(
        currency=CurrencyInfo(symbol="RAI", name="RealAssetChain"), scaling=Decimal("1e-8")
    ),
    "0x5b8d43ffde4a2982b9a5387cdf21d54ead64ac8d": TokenInfo(
        currency=CurrencyInfo(symbol="MEST", name="Monaco Estate"), scaling=Decimal("1e-18")
    ),
    "0x5bb1632fa0023e1aa76a1ae92b4635c8dba49fa2": TokenInfo(
        currency=CurrencyInfo(symbol="FORK", name="GastroAdvisor"), scaling=Decimal("1e-18")
    ),
    "0x5bb29c33c4a3c29f56f8aca40b4db91d8a5fe2c5": TokenInfo(
        currency=CurrencyInfo(symbol="ONS", name="One Share"), scaling=Decimal("1e-18")
    ),
    "0x5bc25f649fc4e26069ddf4cf4010f9f706c23831": TokenInfo(
        currency=CurrencyInfo(symbol="DUSD", name="DefiDollar"), scaling=Decimal("1e-18")
    ),
    "0x5bc7e5f0ab8b2e10d2d0a3f21739fce62459aef3": TokenInfo(
        currency=CurrencyInfo(symbol="ENTRP", name="Hut34 Entropy"), scaling=Decimal("1e-18")
    ),
    "0x5bdc00b6676579b301b276198db1ea9affb94329": TokenInfo(
        currency=CurrencyInfo(symbol="XBASE", name="Eterbase Utility Token"), scaling=Decimal("1e-18")
    ),
    "0x5beabaebb3146685dd74176f68a0721f91297d37": TokenInfo(
        currency=CurrencyInfo(symbol="BOT", name="Bounce [old]"), scaling=Decimal("1e-18")
    ),
    "0x5befbb272290dd5b8521d4a938f6c4757742c430": TokenInfo(
        currency=CurrencyInfo(symbol="XFI", name="Xfinance"), scaling=Decimal("1e-18")
    ),
    "0x5bfc1ff7f9e087c64fefb34f2e7cf24e5570919f": TokenInfo(
        currency=CurrencyInfo(symbol="HABS", name="Habitus "), scaling=Decimal("1e-18")
    ),
    "0x5c0bc243fb13632c4d247f4f0bc27f2f58982c39": TokenInfo(
        currency=CurrencyInfo(symbol="ORYX", name="ORYX"), scaling=Decimal("1e-18")
    ),
    "0x5c248af2fafdffa820a3f54bfc35bef9b5879b5c": TokenInfo(
        currency=CurrencyInfo(symbol="GHST", name="GHOST by McAfee"), scaling=Decimal("1e-18")
    ),
    "0x5c2aafdbbb24da45c48dd4d74b2252a44a6be6d7": TokenInfo(
        currency=CurrencyInfo(symbol="NEXE", name="Nexeum Protocol"), scaling=Decimal("1e-18")
    ),
    "0x5c39bc68e58a242a624e4fc96be77a383c52002d": TokenInfo(
        currency=CurrencyInfo(symbol="BKB", name="BKB"), scaling=Decimal("1e-18")
    ),
    "0x5c3a228510d246b78a3765c20221cbf3082b44a4": TokenInfo(
        currency=CurrencyInfo(symbol="STQ", name="Storiqa"), scaling=Decimal("1e-18")
    ),
    "0x5c406d99e04b8494dc253fcc52943ef82bca7d75": TokenInfo(
        currency=CurrencyInfo(symbol="CUSD", name="cUSD Currency"), scaling=Decimal("1e-6")
    ),
    "0x5c4ac68aac56ebe098d621cd8ce9f43270aaa355": TokenInfo(
        currency=CurrencyInfo(symbol="BXIOT", name="bXIOT"), scaling=Decimal("1e-6")
    ),
    "0x5c543e7ae0a1104f78406c340e9c64fd9fce5170": TokenInfo(
        currency=CurrencyInfo(symbol="VSL", name="vSlice"), scaling=Decimal("1e-18")
    ),
    "0x5c583018358339adbfcc46410c346d52606bf70d": TokenInfo(
        currency=CurrencyInfo(symbol="JNJ.CX", name="Johnson & Johnson"), scaling=Decimal("1e-8")
    ),
    "0x5c6183d10a00cd747a6dbb5f658ad514383e9419": TokenInfo(
        currency=CurrencyInfo(symbol="NXX", name="Nexxus"), scaling=Decimal("1e-8")
    ),
    "0x5c64031c62061865e5fd0f53d3cdaef80f72e99d": TokenInfo(
        currency=CurrencyInfo(symbol="GARD", name="HASHGARD"), scaling=Decimal("1e-18")
    ),
    "0x5c679a0a79d495affe049c02483519d51e37f32b": TokenInfo(
        currency=CurrencyInfo(symbol="DMHCO", name="Daniel Mark Harrison & Company"), scaling=Decimal("1e-18")
    ),
    "0x5c6adf78ea74f057a2e0783ed9d52dba11b225a0": TokenInfo(
        currency=CurrencyInfo(symbol="WLL.CX", name="Whiting Petroleum"), scaling=Decimal("1e-8")
    ),
    "0x5c6af72cbd740b90528c8fe226125413b6bd7e5a": TokenInfo(
        currency=CurrencyInfo(symbol="APEUSD-SNX-DEC21", name="apeUSD-SNX Synthetic USD (Dec 2021)"),
        scaling=Decimal("1e-18"),
    ),
    "0x5c743a35e903f6c584514ec617acee0611cf44f3": TokenInfo(
        currency=CurrencyInfo(symbol="EXY", name="Experty"), scaling=Decimal("1e-18")
    ),
    "0x5c8118fc0237697422ced89a448dce2c8e34b4ef": TokenInfo(
        currency=CurrencyInfo(symbol="LTH", name="LutherChain"), scaling=Decimal("1e-8")
    ),
    "0x5c84bc60a796534bfec3439af0e6db616a966335": TokenInfo(
        currency=CurrencyInfo(symbol="BONE", name="Bone"), scaling=Decimal("1e-18")
    ),
    "0x5c872500c00565505f3624ab435c222e558e9ff8": TokenInfo(
        currency=CurrencyInfo(symbol="COT", name="CoTrader"), scaling=Decimal("1e-18")
    ),
    "0x5c89736e9454200141b80c37eb28eaceca2ce8cb": TokenInfo(
        currency=CurrencyInfo(symbol="YT", name="Cherry Token"), scaling=Decimal("1e-8")
    ),
    "0x5ca381bbfb58f0092df149bd3d243b08b9a8386e": TokenInfo(
        currency=CurrencyInfo(symbol="MXC", name="MXC"), scaling=Decimal("1e-18")
    ),
    "0x5ca9a71b1d01849c0a95490cc00559717fcf0d1d": TokenInfo(
        currency=CurrencyInfo(symbol="AE", name="Aeternity"), scaling=Decimal("1e-18")
    ),
    "0x5caf454ba92e6f2c929df14667ee360ed9fd5b26": TokenInfo(
        currency=CurrencyInfo(symbol="DEV", name="Dev Protocol"), scaling=Decimal("1e-18")
    ),
    "0x5cbb89b03534d82692b183882c2a2a9ff7fdeb44": TokenInfo(
        currency=CurrencyInfo(symbol="BGT", name="BGT"), scaling=Decimal("1e-18")
    ),
    "0x5cc00cca0692b9b34af816e5439cdb47d3b63691": TokenInfo(
        currency=CurrencyInfo(symbol="XWO", name="WooshCoin"), scaling=Decimal("1e-18")
    ),
    "0x5cd487ce4db7091292f2e914f7b31445bd4a5e1b": TokenInfo(
        currency=CurrencyInfo(symbol="IETH20SMACO", name="Inverse ETH 20 Day MA Crossover Set"),
        scaling=Decimal("1e-18"),
    ),
    "0x5ceb8c7f189e694b326310694ac6df98e5ced66e": TokenInfo(
        currency=CurrencyInfo(symbol="YAT", name="Yattaqi"), scaling=Decimal("1e-18")
    ),
    "0x5cf04716ba20127f1e2297addcf4b5035000c9eb": TokenInfo(
        currency=CurrencyInfo(symbol="NKN", name="NKN"), scaling=Decimal("1e-18")
    ),
    "0x5cf501e64786444e025c5b24025f98399538ea5d": TokenInfo(
        currency=CurrencyInfo(symbol="GPO", name="Galaxy Pool Coin"), scaling=Decimal("1e-18")
    ),
    "0x5d1b1019d0afa5e6cc047b9e78081d44cc579fc4": TokenInfo(
        currency=CurrencyInfo(symbol="YFRB", name="yfrb.Finance"), scaling=Decimal("1e-18")
    ),
    "0x5d21ef5f25a985380b65c8e943a0082feda0db84": TokenInfo(
        currency=CurrencyInfo(symbol="ECASH", name="Ethereum Cash"), scaling=Decimal("1e-18")
    ),
    "0x5d285f735998f36631f678ff41fb56a10a4d0429": TokenInfo(
        currency=CurrencyInfo(symbol="MIX", name="MixMarvel"), scaling=Decimal("1e-18")
    ),
    "0x5d3a536e4d6dbd6114cc1ead35777bab948e3643": TokenInfo(
        currency=CurrencyInfo(symbol="CDAI", name="cDAI"), scaling=Decimal("1e-8")
    ),
    "0x5d45aa01b73c971c65f3df409c9b3627b8fe2726": TokenInfo(
        currency=CurrencyInfo(symbol="TMCN", name="Timecoin Protocol"), scaling=Decimal("1e-18")
    ),
    "0x5d48f293baed247a2d0189058ba37aa238bd4725": TokenInfo(
        currency=CurrencyInfo(symbol="NCC", name="NeuroChain"), scaling=Decimal("1e-18")
    ),
    "0x5d4abc77b8405ad177d8ac6682d584ecbfd46cec": TokenInfo(
        currency=CurrencyInfo(symbol="PST", name="Primas Token"), scaling=Decimal("1e-18")
    ),
    "0x5d4d57cd06fa7fe99e26fdc481b468f77f05073c": TokenInfo(
        currency=CurrencyInfo(symbol="NTK", name="Netkoin"), scaling=Decimal("1e-18")
    ),
    "0x5d51fcced3114a8bb5e90cdd0f9d682bcbcc5393": TokenInfo(
        currency=CurrencyInfo(symbol="B2B", name="B2BX"), scaling=Decimal("1e-18")
    ),
    "0x5d551fa77ec2c7dd1387b626c4f33235c3885199": TokenInfo(
        currency=CurrencyInfo(symbol="BSP", name="Blocksports Network"), scaling=Decimal("1e-18")
    ),
    "0x5d5d4962621b24547fec4a5161cb1a07ebd9e556": TokenInfo(
        currency=CurrencyInfo(symbol="TOC", name="Tobigca"), scaling=Decimal("1e-18")
    ),
    "0x5d60d8d7ef6d37e16ebabc324de3be57f135e0bc": TokenInfo(
        currency=CurrencyInfo(symbol="MYB", name="MyBit Token"), scaling=Decimal("1e-18")
    ),
    "0x5d64d850c8368008afb39224e92ad0dceff3cf38": TokenInfo(
        currency=CurrencyInfo(symbol="MIN", name="MINDOL"), scaling=Decimal("1e-18")
    ),
    "0x5d65d971895edc438f465c17db6992698a52318d": TokenInfo(
        currency=CurrencyInfo(symbol="NAS", name="Nebulas"), scaling=Decimal("1e-18")
    ),
    "0x5d762f76b9e91f71cc4f94391bdfe6333db8519c": TokenInfo(
        currency=CurrencyInfo(symbol="IYF", name="IYF.finance"), scaling=Decimal("1e-18")
    ),
    "0x5d843fa9495d23de997c394296ac7b4d721e841c": TokenInfo(
        currency=CurrencyInfo(symbol="RELAY", name="Relay Token"), scaling=Decimal("1e-18")
    ),
    "0x5d858bcd53e085920620549214a8b27ce2f04670": TokenInfo(
        currency=CurrencyInfo(symbol="POP", name="POP Network"), scaling=Decimal("1e-18")
    ),
    "0x5d8d9f5b96f4438195be9b99eee6118ed4304286": TokenInfo(
        currency=CurrencyInfo(symbol="COVER", name="Cover Protocol [old]"), scaling=Decimal("1e-18")
    ),
    "0x5d9776472483ee2c2b204775547bff6db5a30fed": TokenInfo(
        currency=CurrencyInfo(symbol="599GTO1", name="Ferrari 599 GTO 1"), scaling=Decimal("1e-8")
    ),
    "0x5dba63c221d7a584795431ce01ecd641a1798416": TokenInfo(
        currency=CurrencyInfo(symbol="ORT", name="Oratium"), scaling=Decimal("1e-18")
    ),
    "0x5dbac24e98e2a4f43adc0dc82af403fca063ce2c": TokenInfo(
        currency=CurrencyInfo(symbol="ENGT", name="Engagement Token"), scaling=Decimal("1e-18")
    ),
    "0x5dbcf33d8c2e976c6b560249878e6f1491bca25c": TokenInfo(
        currency=CurrencyInfo(symbol="YVAULT-LP-YCURVE", name="yUSD"), scaling=Decimal("1e-18")
    ),
    "0x5dbe296f97b23c4a6aa6183d73e574d02ba5c719": TokenInfo(
        currency=CurrencyInfo(symbol="LUC", name="Level-Up Coin"), scaling=Decimal("1e-18")
    ),
    "0x5dc02ea99285e17656b8350722694c35154db1e8": TokenInfo(
        currency=CurrencyInfo(symbol="BOND", name="Bonded Finance"), scaling=Decimal("1e-8")
    ),
    "0x5dc60c4d5e75d22588fa17ffeb90a63e535efce0": TokenInfo(
        currency=CurrencyInfo(symbol="DKA", name="dKargo"), scaling=Decimal("1e-18")
    ),
    "0x5dc74029509752f4ed9a609c2bb52216275e4c1d": TokenInfo(
        currency=CurrencyInfo(symbol="GMCI", name="Game City"), scaling=Decimal("1e-8")
    ),
    "0x5dcfa62f81b43ce7a3632454d327dee1f1d93b28": TokenInfo(
        currency=CurrencyInfo(symbol="ETHMOON", name="10X Long Ethereum Token"), scaling=Decimal("1e-18")
    ),
    "0x5dd0815a4cf119ad91ba045bbbf879f3f7de3c68": TokenInfo(
        currency=CurrencyInfo(symbol="SKYFT", name="SKYFchain"), scaling=Decimal("1e-18")
    ),
    "0x5df94780f00140fe72d239d0d261f7797e3fbd1b": TokenInfo(
        currency=CurrencyInfo(symbol="QHC", name="QChi Chain"), scaling=Decimal("1e-18")
    ),
    "0x5dff89a2caa4d76bc286f74d67bd718eb834da61": TokenInfo(
        currency=CurrencyInfo(symbol="CFC", name="CryptFillCoin"), scaling=Decimal("1e-18")
    ),
    "0x5e0ed77611560aff6c0fd9e15b7a66c430dc1e72": TokenInfo(
        currency=CurrencyInfo(symbol="ZGK", name="ZGPoker"), scaling=Decimal("1e-8")
    ),
    "0x5e3002dff591c5e75bb9dedae268049742e6b13a": TokenInfo(
        currency=CurrencyInfo(symbol="TUDA", name="Tutor's Diary"), scaling=Decimal("1e-8")
    ),
    "0x5e3346444010135322268a4630d2ed5f8d09446c": TokenInfo(
        currency=CurrencyInfo(symbol="LOC", name="LockTrip"), scaling=Decimal("1e-18")
    ),
    "0x5e36f2272f650d92c3f0bf503462dbd074b841f1": TokenInfo(
        currency=CurrencyInfo(symbol="SBER.CX", name="Sberbank of Russia GDR"), scaling=Decimal("1e-8")
    ),
    "0x5e4abe6419650ca839ce5bb7db422b881a6064bb": TokenInfo(
        currency=CurrencyInfo(symbol="WIC", name="Wi Coin"), scaling=Decimal("1e-18")
    ),
    "0x5e6016ae7d7c49d347dcf834860b9f3ee282812b": TokenInfo(
        currency=CurrencyInfo(symbol="EZT", name="EZToken"), scaling=Decimal("1e-8")
    ),
    "0x5e6b6d9abad9093fdc861ea1600eba1b355cd940": TokenInfo(
        currency=CurrencyInfo(symbol="ITC", name="IoT Chain"), scaling=Decimal("1e-18")
    ),
    "0x5e74c9036fb86bd7ecdcb084a0673efc32ea31cb": TokenInfo(
        currency=CurrencyInfo(symbol="SETH", name="sETH"), scaling=Decimal("1e-18")
    ),
    "0x5e888b83b7287eed4fb7da7b7d0a0d4c735d94b3": TokenInfo(
        currency=CurrencyInfo(symbol="OAK", name="Acorn Collective Token"), scaling=Decimal("1e-18")
    ),
    "0x5eaa69b29f99c84fe5de8200340b4e9b4ab38eac": TokenInfo(
        currency=CurrencyInfo(symbol="RAZE", name="Raze Network"), scaling=Decimal("1e-18")
    ),
    "0x5eb87caa0105a63aa87a36c7bd2573bd13e84fae": TokenInfo(
        currency=CurrencyInfo(symbol="BQT", name="Blockchain Quotations Index Token"), scaling=Decimal("1e-18")
    ),
    "0x5ebe6a342a93102393edd9d2e458c689e5ac0bb3": TokenInfo(
        currency=CurrencyInfo(symbol="PCT", name="PerksCoin"), scaling=Decimal("1e-8")
    ),
    "0x5ec598ee5838e1d786b6ac9e4adeb6bd5dde1a87": TokenInfo(
        currency=CurrencyInfo(symbol="TGBP", name="TrueGBP"), scaling=Decimal("1e-18")
    ),
    "0x5ecd84482176db90bb741ddc8c2f9ccc290e29ce": TokenInfo(
        currency=CurrencyInfo(symbol="BTL", name="Bitlong"), scaling=Decimal("1e-6")
    ),
    "0x5edc1a266e8b2c5e8086d373725df0690af7e3ea": TokenInfo(
        currency=CurrencyInfo(symbol="YTA", name="YottaChain"), scaling=Decimal("1e-18")
    ),
    "0x5ef227f7ce4e96c9ce90e32d4850545a6c5d099b": TokenInfo(
        currency=CurrencyInfo(symbol="BCHIP", name="BLUECHIPS Token"), scaling=Decimal("1e-8")
    ),
    "0x5f02cf3c7ada49dfc4a3645fc85c8ae86808dd9b": TokenInfo(
        currency=CurrencyInfo(symbol="AKM", name="COST COIN+"), scaling=Decimal("1e-18")
    ),
    "0x5f038e82bb69b6a52fec7a4a38163340b98fb1e4": TokenInfo(
        currency=CurrencyInfo(symbol="BTP", name="Bitpaid"), scaling=Decimal("1e-18")
    ),
    "0x5f0bc16d50f72d10b719dbf6845de2e599eb5624": TokenInfo(
        currency=CurrencyInfo(symbol="VENT", name="Vent Finance"), scaling=Decimal("1e-18")
    ),
    "0x5f0e628b693018f639d10e4a4f59bd4d8b2b6b44": TokenInfo(
        currency=CurrencyInfo(symbol="WHITE", name="Whiteheart"), scaling=Decimal("1e-18")
    ),
    "0x5f12f33d0a36fd369e4fffae3d82eff9160013ce": TokenInfo(
        currency=CurrencyInfo(symbol="XRX", name="X-REIS"), scaling=Decimal("1e-8")
    ),
    "0x5f1df88d5c354006dff74d1b72a40e8c4afc0c37": TokenInfo(
        currency=CurrencyInfo(symbol="LTT", name="Live Telecast Token"), scaling=Decimal("1e-18")
    ),
    "0x5f236f062f16a9b19819c535127398df9a01d762": TokenInfo(
        currency=CurrencyInfo(symbol="IPUX", name="Initial Point Unit X"), scaling=Decimal("1e-18")
    ),
    "0x5f2ec9cf1ec1c0e2c880b6584921e812a4225395": TokenInfo(
        currency=CurrencyInfo(symbol="BTCUI", name="Bitcoin Unicorn"), scaling=Decimal("1e-8")
    ),
    "0x5f33d158ca7275848f70a3f149b421190df85b32": TokenInfo(
        currency=CurrencyInfo(symbol="PDX", name="PDX"), scaling=Decimal("1e-18")
    ),
    "0x5f4506db5b568e103532f84d32a285cdd5aa5751": TokenInfo(
        currency=CurrencyInfo(symbol="OGK", name="Organik"), scaling=Decimal("1e-10")
    ),
    "0x5f53f7a8075614b699baad0bc2c899f4bad8fbbf": TokenInfo(
        currency=CurrencyInfo(symbol="REBL", name="Rebellious"), scaling=Decimal("1e-18")
    ),
    "0x5f5f8a9c9775499b783171ac1979b4327ab60447": TokenInfo(
        currency=CurrencyInfo(symbol="XFRC", name="Fructus"), scaling=Decimal("1e-18")
    ),
    "0x5f64ab1544d28732f0a24f4713c2c8ec0da089f0": TokenInfo(
        currency=CurrencyInfo(symbol="DEXTF", name="DEXTF"), scaling=Decimal("1e-18")
    ),
    "0x5f6e7fb7fe92ea7822472bb0e8f1be60d6a4ea50": TokenInfo(
        currency=CurrencyInfo(symbol="ARTE", name="Artemine"), scaling=Decimal("1e-18")
    ),
    "0x5f75112bbb4e1af516fbe3e21528c63da2b6a1a5": TokenInfo(
        currency=CurrencyInfo(symbol="CHESS", name="Chess Coin"), scaling=Decimal("1e-18")
    ),
    "0x5f778ec4b31a506c1dfd8b06f131e9b451a61d39": TokenInfo(
        currency=CurrencyInfo(symbol="UPX", name="UDAP"), scaling=Decimal("1e-18")
    ),
    "0x5f7fa1a0ae94b5dd6bb6bd1708b5f3af01b57908": TokenInfo(
        currency=CurrencyInfo(symbol="YFIKING", name="YFIKing Finance"), scaling=Decimal("1e-18")
    ),
    "0x5f85c60187ab233ca6e750731d15e7efd061fbde": TokenInfo(
        currency=CurrencyInfo(symbol="PSDN", name="Poseidon"), scaling=Decimal("1e-18")
    ),
    "0x5f88889c7466212e85bb9a720952abe56f6acc95": TokenInfo(
        currency=CurrencyInfo(symbol="LLY.CX", name="Eli Lilly & Co"), scaling=Decimal("1e-8")
    ),
    "0x5f98805a4e8be255a32880fdec7f6728c6568ba0": TokenInfo(
        currency=CurrencyInfo(symbol="LUSD", name="Liquity USD"), scaling=Decimal("1e-18")
    ),
    "0x5f9b347cdd2b35b346ba98ad35a9f367432a41b9": TokenInfo(
        currency=CurrencyInfo(symbol="PTEN.CX", name="Patterson-UTI Energy Inc"), scaling=Decimal("1e-8")
    ),
    "0x5fb1bbfbdbbb26e4d51a47b1765cc6272ebb31e4": TokenInfo(
        currency=CurrencyInfo(symbol="OKG", name="OKGUESS"), scaling=Decimal("1e-18")
    ),
    "0x5fb9e9c359cc7191b0293d2faf1cc41ce3688d75": TokenInfo(
        currency=CurrencyInfo(symbol="AUS", name="Gold Standard"), scaling=Decimal("1e-4")
    ),
    "0x5feee18d8ba20be1fbfad89b2b793e03c8bb3b95": TokenInfo(
        currency=CurrencyInfo(symbol="GIVES", name="Gives Token"), scaling=Decimal("1e-8")
    ),
    "0x6006fc2a849fedaba8330ce36f5133de01f96189": TokenInfo(
        currency=CurrencyInfo(symbol="SHAKE", name="Spaceswap SHAKE"), scaling=Decimal("1e-18")
    ),
    "0x600e156b5d158033648c5963a2ed7042d5d240ba": TokenInfo(
        currency=CurrencyInfo(symbol="PRN", name="Proteania"), scaling=Decimal("1e-18")
    ),
    "0x601a0ee18e9dcdc70658d8b87a748e11344d3a45": TokenInfo(
        currency=CurrencyInfo(symbol="APXP", name="APEX Protocol"), scaling=Decimal("1e-18")
    ),
    "0x6020da0f7c1857dbe4431ec92a15cc318d933eaa": TokenInfo(
        currency=CurrencyInfo(symbol="ETM", name="En-Tan-Mo"), scaling=Decimal("1e-18")
    ),
    "0x6028d881eea57c18255a85809cdd7f212688d946": TokenInfo(
        currency=CurrencyInfo(symbol="RT", name="Resource Token"), scaling=Decimal("1e-18")
    ),
    "0x604026696fdb3c6720ae3049c46d59ac604dea0a": TokenInfo(
        currency=CurrencyInfo(symbol="XJP", name="eXciting Japan Coin"), scaling=Decimal("1e-18")
    ),
    "0x6051c1354ccc51b4d561e43b02735deae64768b8": TokenInfo(
        currency=CurrencyInfo(symbol="YRISE", name="yRise Finance"), scaling=Decimal("1e-18")
    ),
    "0x60571e95e12c78cba5223042692908f0649435a5": TokenInfo(
        currency=CurrencyInfo(symbol="PLAAS", name="PLAAS FARMERS TOKEN"), scaling=Decimal("1e-18")
    ),
    "0x605ec235c045915f7e18051697c9530659df8757": TokenInfo(
        currency=CurrencyInfo(symbol="DTE", name="Data Exchange"), scaling=Decimal("1e-8")
    ),
    "0x6069c9223e8a5da1ec49ac5525d4bb757af72cd8": TokenInfo(
        currency=CurrencyInfo(symbol="MUSK", name="MUSK Gold"), scaling=Decimal("1e-18")
    ),
    "0x60715e436c37444e29772c0d26a98ae1e8e1a989": TokenInfo(
        currency=CurrencyInfo(symbol="VOLTZ", name="Voltz"), scaling=Decimal("1e-18")
    ),
    "0x607415cb26756d5d0e6ae56adc06fbe29edf79d9": TokenInfo(
        currency=CurrencyInfo(symbol="IECT", name="IENETChain"), scaling=Decimal("1e-8")
    ),
    "0x6076361202cd4d4abaaf95f48823fe0ab7763eb0": TokenInfo(
        currency=CurrencyInfo(symbol="GPC", name="Global-Pay Coin"), scaling=Decimal("1e-18")
    ),
    "0x607c794cda77efb21f8848b7910ecf27451ae842": TokenInfo(
        currency=CurrencyInfo(symbol="PIE", name="DeFiPie"), scaling=Decimal("1e-18")
    ),
    "0x607f4c5bb672230e8672085532f7e901544a7375": TokenInfo(
        currency=CurrencyInfo(symbol="RLC", name="iExec RLC"), scaling=Decimal("1e-9")
    ),
    "0x608f006b6813f97097372d0d31fb0f11d1ca3e4e": TokenInfo(
        currency=CurrencyInfo(symbol="CRAD", name="CryptoAds Marketplace"), scaling=Decimal("1e-18")
    ),
    "0x6096d2460cf5177e40b515223428dc005ad35123": TokenInfo(
        currency=CurrencyInfo(symbol="PCM", name="Precium"), scaling=Decimal("1e-18")
    ),
    "0x60a640e2d10e020fee94217707bfa9543c8b59e0": TokenInfo(
        currency=CurrencyInfo(symbol="OSC", name="iOscar"), scaling=Decimal("1e-18")
    ),
    "0x60b3bc37593853c04410c4f07fe4d6748245bf77": TokenInfo(
        currency=CurrencyInfo(symbol="SHIELD", name="SHIELD"), scaling=Decimal("1e-18")
    ),
    "0x60b4b0c6a1c518be1f7f68a8ced6af510fd21b4b": TokenInfo(
        currency=CurrencyInfo(symbol="BITC", name="Bit Token Economy"), scaling=Decimal("1e-18")
    ),
    "0x60b5aa3334185d72eed79ac5ffc9870e98f502eb": TokenInfo(
        currency=CurrencyInfo(symbol="BKU", name="Blocktek University"), scaling=Decimal("1e-18")
    ),
    "0x60c24407d01782c2175d32fe7c8921ed732371d1": TokenInfo(
        currency=CurrencyInfo(symbol="LEMO", name="LemoChain"), scaling=Decimal("1e-18")
    ),
    "0x60d9564303c70d3f040ea9393d98d94f767d020c": TokenInfo(
        currency=CurrencyInfo(symbol="DAI.CX", name="Daimler AG"), scaling=Decimal("1e-8")
    ),
    "0x60e7f0518102a4e70431960f88c1ebc98f994159": TokenInfo(
        currency=CurrencyInfo(symbol="EXNX", name="Exenox Mobile"), scaling=Decimal("1e-6")
    ),
    "0x60eb57d085c59932d5faa6c6026268a4386927d0": TokenInfo(
        currency=CurrencyInfo(symbol="LOCG", name="LOCGame"), scaling=Decimal("1e-18")
    ),
    "0x60f5672a271c7e39e787427a18353ba59a4a3578": TokenInfo(
        currency=CurrencyInfo(symbol="PIKA", name="Pika"), scaling=Decimal("1e-18")
    ),
    "0x6100dd79fcaa88420750dcee3f735d168abcb771": TokenInfo(
        currency=CurrencyInfo(symbol="OS", name="Ethereans"), scaling=Decimal("1e-18")
    ),
    "0x6103c7873cde5f0f63dba9fac33a2049cd8a2680": TokenInfo(
        currency=CurrencyInfo(symbol="FB.CX", name="Facebook"), scaling=Decimal("1e-8")
    ),
    "0x6123a0cbc95cb157995a0795187a60995b85e0a9": TokenInfo(
        currency=CurrencyInfo(symbol="BTCHIVOL", name="BTC Range Bound High Volatility Set"), scaling=Decimal("1e-18")
    ),
    "0x6123b0049f904d730db3c36a31167d9d4121fa6b": TokenInfo(
        currency=CurrencyInfo(symbol="RBN", name="Ribbon Finance"), scaling=Decimal("1e-18")
    ),
    "0x61242546ea93d851a2e606f03a2593645e92734b": TokenInfo(
        currency=CurrencyInfo(symbol="BVS", name="BTC Vol Switching Set"), scaling=Decimal("1e-18")
    ),
    "0x61266424b904d65ceb2945a1413ac322185187d5": TokenInfo(
        currency=CurrencyInfo(symbol="YFID", name="YFIDapp"), scaling=Decimal("1e-18")
    ),
    "0x613fa2a6e6daa70c659060e86ba1443d2679c9d7": TokenInfo(
        currency=CurrencyInfo(symbol="GOT", name="ParkinGo"), scaling=Decimal("1e-18")
    ),
    "0x614348d080835adcbbdee121af077024e27eccc6": TokenInfo(
        currency=CurrencyInfo(symbol="LDG", name="Ledgit"), scaling=Decimal("1e-18")
    ),
    "0x614857c755739354d68ae0abd53849cf45d6a41d": TokenInfo(
        currency=CurrencyInfo(symbol="ETH26EMACO", name="ETH 26 Day EMA Crossover Set"), scaling=Decimal("1e-18")
    ),
    "0x6149c26cd2f7b5ccdb32029af817123f6e37df5b": TokenInfo(
        currency=CurrencyInfo(symbol="LPOOL", name="Launchpool"), scaling=Decimal("1e-18")
    ),
    "0x614b9802d45aa1bc2282651dc1408632f9027a6e": TokenInfo(
        currency=CurrencyInfo(symbol="TIC", name="TrustInvest"), scaling=Decimal("1e-18")
    ),
    "0x614fd8f06ce4d93aa2361b342c86554eb5cb39f1": TokenInfo(
        currency=CurrencyInfo(symbol="TYT", name="Tianya Token"), scaling=Decimal("1e-6")
    ),
    "0x61630fd1f65a7b72af8e9faa6e2646080131f501": TokenInfo(
        currency=CurrencyInfo(symbol="PEP", name="PesaPepe"), scaling=Decimal("1e-18")
    ),
    "0x616c281cd8efff8c0354723be399c809e97a7bf4": TokenInfo(
        currency=CurrencyInfo(symbol="SGT", name="SelfieYo Gold Token"), scaling=Decimal("1e-18")
    ),
    "0x61725f3db4004afe014745b21dab1e1677cc328b": TokenInfo(
        currency=CurrencyInfo(symbol="DAXT", name="Digital  Asset Exchange Token"), scaling=Decimal("1e-18")
    ),
    "0x617aecb6137b5108d1e7d4918e3725c8cebdb848": TokenInfo(
        currency=CurrencyInfo(symbol="SBNB", name="sBNB"), scaling=Decimal("1e-18")
    ),
    "0x618679df9efcd19694bb1daa8d00718eacfa2883": TokenInfo(
        currency=CurrencyInfo(symbol="XYZ", name="XYZ"), scaling=Decimal("1e-18")
    ),
    "0x618e75ac90b12c6049ba3b27f5d5f8651b0037f6": TokenInfo(
        currency=CurrencyInfo(symbol="QASH", name="QASH"), scaling=Decimal("1e-6")
    ),
    "0x619ff65f38474989959c707b2144ebd2cbe58d1c": TokenInfo(
        currency=CurrencyInfo(symbol="TOT", name="TIME OUT TOKEN"), scaling=Decimal("1e-8")
    ),
    "0x61b2d3ea9f1c6b387c985c73d40e8fbfb284e5c7": TokenInfo(
        currency=CurrencyInfo(symbol="RC20", name="RoboCalls"), scaling=Decimal("1e-18")
    ),
    "0x61bc1f530ac6193d73af1e1a6a14cb44b9c3f915": TokenInfo(
        currency=CurrencyInfo(symbol="PJM", name="Pajama.Finance"), scaling=Decimal("1e-18")
    ),
    "0x61bfc979ea8160ede9b862798b7833a97bafa02a": TokenInfo(
        currency=CurrencyInfo(symbol="REL", name="RELEASE"), scaling=Decimal("1e-18")
    ),
    "0x61cdb66e56fad942a7b5ce3f419ffe9375e31075": TokenInfo(
        currency=CurrencyInfo(symbol="RAIN", name="RAIN Network"), scaling=Decimal("1e-18")
    ),
    "0x61d24aabb3e5e800d8f3d3d43dcbd66ae6cab51e": TokenInfo(
        currency=CurrencyInfo(symbol="BRB", name="Rabbit Coin"), scaling=Decimal("1e-18")
    ),
    "0x61d71973a6ffd07d5f1095aed53b06e5673e64bc": TokenInfo(
        currency=CurrencyInfo(symbol="MIMA", name="Mima"), scaling=Decimal("1e-18")
    ),
    "0x61fef6246a010e601843477a90eb54f8f97a91d9": TokenInfo(
        currency=CurrencyInfo(symbol="PANCHO", name="Pancho Villa Network"), scaling=Decimal("1e-7")
    ),
    "0x620fa2993046a53df1f365fa3fdc9e6c7763af96": TokenInfo(
        currency=CurrencyInfo(symbol="GRT", name="Global Rental Token"), scaling=Decimal("1e-8")
    ),
    "0x621d78f2ef2fd937bfca696cabaf9a779f59b3ed": TokenInfo(
        currency=CurrencyInfo(symbol="DRP", name="DCORP"), scaling=Decimal("1e-2")
    ),
    "0x621e3b71d07b51242bcca167928e184235a4bb87": TokenInfo(
        currency=CurrencyInfo(symbol="MAVC", name="Mountains and Valleys ETH/BTC Set"), scaling=Decimal("1e-18")
    ),
    "0x6226caa1857afbc6dfb6ca66071eb241228031a1": TokenInfo(
        currency=CurrencyInfo(symbol="LAR", name="LinkArt"), scaling=Decimal("1e-18")
    ),
    "0x6226e00bcac68b0fe55583b90a1d727c14fab77f": TokenInfo(
        currency=CurrencyInfo(symbol="MTV", name="MultiVAC"), scaling=Decimal("1e-18")
    ),
    "0x622cd54deb2bb7a051515192417109bcf3fe098f": TokenInfo(
        currency=CurrencyInfo(symbol="IPC", name="IPChain"), scaling=Decimal("1e-8")
    ),
    "0x622dffcc4e83c64ba959530a5a5580687a57581b": TokenInfo(
        currency=CurrencyInfo(symbol="AUTO", name="Cube"), scaling=Decimal("1e-18")
    ),
    "0x622f2962ae78e8686ecc1e30cf2f9a6e5ac35626": TokenInfo(
        currency=CurrencyInfo(symbol="POLIS", name="Wrapped Polis"), scaling=Decimal("1e-18")
    ),
    "0x62359ed7505efc61ff1d56fef82158ccaffa23d7": TokenInfo(
        currency=CurrencyInfo(symbol="CORE", name="cVault.finance"), scaling=Decimal("1e-18")
    ),
    "0x623b925b0a57a24ea8de301f2e3e692ce903f0c3": TokenInfo(
        currency=CurrencyInfo(symbol="MOVI", name="MOVI"), scaling=Decimal("1e-0")
    ),
    "0x6243d8cea23066d098a15582d81a598b4e8391f4": TokenInfo(
        currency=CurrencyInfo(symbol="FLX", name="Reflexer Ungovernance Token"), scaling=Decimal("1e-18")
    ),
    "0x6247c86b016bc4d9ae141849c0a9eb38c004b742": TokenInfo(
        currency=CurrencyInfo(symbol="HTL", name="Hotelium"), scaling=Decimal("1e-18")
    ),
    "0x624d520bab2e4ad83935fa503fb130614374e850": TokenInfo(
        currency=CurrencyInfo(symbol="SSP", name="Smartshare"), scaling=Decimal("1e-4")
    ),
    "0x6251e725cd45fb1af99354035a414a2c0890b929": TokenInfo(
        currency=CurrencyInfo(symbol="MXT", name="MixTrust"), scaling=Decimal("1e-18")
    ),
    "0x625687081ba9fcbffb0ae6bfe8d7fad6f616f494": TokenInfo(
        currency=CurrencyInfo(symbol="MDTL", name="Medalte"), scaling=Decimal("1e-18")
    ),
    "0x625ae63000f46200499120b906716420bd059240": TokenInfo(
        currency=CurrencyInfo(symbol="ASUSD", name="Aave SUSD v1"), scaling=Decimal("1e-18")
    ),
    "0x6265bcd2ca8e8ee077cb9a9c66a851f18216022e": TokenInfo(
        currency=CurrencyInfo(symbol="ETCR", name="EtherCare"), scaling=Decimal("1e-6")
    ),
    "0x626e8036deb333b408be468f951bdb42433cbf18": TokenInfo(
        currency=CurrencyInfo(symbol="AIOZ", name="AIOZ Network"), scaling=Decimal("1e-18")
    ),
    "0x627974847450c45b60b3fe3598f4e6e4cf945b9a": TokenInfo(
        currency=CurrencyInfo(symbol="TBC", name="THUNDERBOLT COIN"), scaling=Decimal("1e-18")
    ),
    "0x627e2ee3dbda546e168eaaff25a2c5212e4a95a0": TokenInfo(
        currency=CurrencyInfo(symbol="IBVOL", name="Inverse Bitcoin Volatility Token"), scaling=Decimal("1e-18")
    ),
    "0x6286a9e6f7e745a6d884561d88f94542d6715698": TokenInfo(
        currency=CurrencyInfo(symbol="TECH", name="Cryptomeda"), scaling=Decimal("1e-18")
    ),
    "0x6288014d6ba425d71f5fdc1dbfb01378241d78db": TokenInfo(
        currency=CurrencyInfo(symbol="TCO", name="ThinkCoin"), scaling=Decimal("1e-18")
    ),
    "0x6295ab2be04a617747481b292c390bfca592cf28": TokenInfo(
        currency=CurrencyInfo(symbol="TDS", name="TokenDesk"), scaling=Decimal("1e-18")
    ),
    "0x629aee55ed49581c33ab27f9403f7992a289ffd5": TokenInfo(
        currency=CurrencyInfo(symbol="STC", name="StrikeCoin Token"), scaling=Decimal("1e-18")
    ),
    "0x62a56a4a2ef4d355d34d10fbf837e747504d38d4": TokenInfo(
        currency=CurrencyInfo(symbol="PAYX", name="Paypex"), scaling=Decimal("1e-2")
    ),
    "0x62b9c7356a2dc64a1969e19c23e4f579f9810aa7": TokenInfo(
        currency=CurrencyInfo(symbol="CVXCRV", name="Convex CRV"), scaling=Decimal("1e-18")
    ),
    "0x62cd07d414ec50b68c7ecaa863a23d344f2d062f": TokenInfo(
        currency=CurrencyInfo(symbol="WIC", name="WickNote"), scaling=Decimal("1e-0")
    ),
    "0x62d4c04644314f35868ba4c65cc27a77681de7a9": TokenInfo(
        currency=CurrencyInfo(symbol="DRVH", name="Driveholic Token"), scaling=Decimal("1e-18")
    ),
    "0x62d75a2a10f755104bd1024d997141ce793cf585": TokenInfo(
        currency=CurrencyInfo(symbol="520", name="520"), scaling=Decimal("1e-18")
    ),
    "0x62dc4817588d53a056cbbd18231d91ffccd34b2a": TokenInfo(
        currency=CurrencyInfo(symbol="DHV", name="DeHive"), scaling=Decimal("1e-18")
    ),
    "0x62e9ce974213c04bbf97dee1e15f1a0b9df7274c": TokenInfo(
        currency=CurrencyInfo(symbol="WIDE", name="Wide Energy"), scaling=Decimal("1e-0")
    ),
    "0x6307b25a665efc992ec1c1bc403c38f3ddd7c661": TokenInfo(
        currency=CurrencyInfo(symbol="GCR", name="Global Coin Researc"), scaling=Decimal("1e-4")
    ),
    "0x630bc7dd0abfc2d196289ce09db947dd2cafae7c": TokenInfo(
        currency=CurrencyInfo(symbol="NABOX", name="Nabox"), scaling=Decimal("1e-18")
    ),
    "0x630d98424efe0ea27fb1b3ab7741907dffeaad78": TokenInfo(
        currency=CurrencyInfo(symbol="PEAK", name="PEAKDEFI"), scaling=Decimal("1e-8")
    ),
    "0x6339784d9478da43106a429196772a029c2f177d": TokenInfo(
        currency=CurrencyInfo(symbol="ATTN", name="Attention Token"), scaling=Decimal("1e-18")
    ),
    "0x633ee3fbe5ffc05bd44ecd8240732ff9ef9dee1d": TokenInfo(
        currency=CurrencyInfo(symbol="PEAK", name="MarketPeak"), scaling=Decimal("1e-8")
    ),
    "0x6353eadf8d1d4421002332bb9074222b14d54881": TokenInfo(
        currency=CurrencyInfo(symbol="PFR", name="Payfair"), scaling=Decimal("1e-8")
    ),
    "0x6368a6bcebe2db1a850f87650dabd29cc642e2da": TokenInfo(
        currency=CurrencyInfo(symbol="CNZ", name="CryptoNationZ"), scaling=Decimal("1e-18")
    ),
    "0x6368e1e18c4c419ddfc608a0bed1ccb87b9250fc": TokenInfo(
        currency=CurrencyInfo(symbol="XTP", name="Tap"), scaling=Decimal("1e-18")
    ),
    "0x6369c3dadfc00054a42ba8b2c09c48131dd4aa38": TokenInfo(
        currency=CurrencyInfo(symbol="MPH", name="Morpher"), scaling=Decimal("1e-18")
    ),
    "0x6380ebe960aa587164b07e58ed04077ce64279c0": TokenInfo(
        currency=CurrencyInfo(symbol="DGT", name="DagonToken"), scaling=Decimal("1e-18")
    ),
    "0x638ac149ea8ef9a1286c41b977017aa7359e6cfa": TokenInfo(
        currency=CurrencyInfo(symbol="ALTS", name="Altcoins Talks"), scaling=Decimal("1e-18")
    ),
    "0x6399c842dd2be3de30bf99bc7d1bbf6fa3650e70": TokenInfo(
        currency=CurrencyInfo(symbol="PREMIA", name="Premia"), scaling=Decimal("1e-18")
    ),
    "0x63a18bc38d1101db7f0efcbcbdcbe927a5879039": TokenInfo(
        currency=CurrencyInfo(symbol="EARN", name="Yearn Classic"), scaling=Decimal("1e-18")
    ),
    "0x63b4f3e3fa4e438698ce330e365e831f7ccd1ef4": TokenInfo(
        currency=CurrencyInfo(symbol="CFI", name="CyberFi"), scaling=Decimal("1e-18")
    ),
    "0x63b8b7d4a3efd0735c4bffbd95b332a55e4eb851": TokenInfo(
        currency=CurrencyInfo(symbol="DGCL", name="DigiCol Token"), scaling=Decimal("1e-18")
    ),
    "0x63b992e6246d88f07fc35a056d2c365e6d441a3d": TokenInfo(
        currency=CurrencyInfo(symbol="SCT", name="Soma"), scaling=Decimal("1e-18")
    ),
    "0x63bf0126c6c4d17bb33c362151759ec21b36537b": TokenInfo(
        currency=CurrencyInfo(symbol="MACPO", name="Master Coin Point"), scaling=Decimal("1e-18")
    ),
    "0x63d27b3da94a9e871222cb0a32232674b02d2f2d": TokenInfo(
        currency=CurrencyInfo(symbol="idleUSDTYield", name="IdleUSDT v3 [Max yield]"), scaling=Decimal("1e-18")
    ),
    "0x63d958d765f5bd88efdbd8afd32445393b24907f": TokenInfo(
        currency=CurrencyInfo(symbol="ACA", name="Acash Coin"), scaling=Decimal("1e-8")
    ),
    "0x63e634330a20150dbb61b15648bc73855d6ccf07": TokenInfo(
        currency=CurrencyInfo(symbol="LNC", name="Blocklancer"), scaling=Decimal("1e-18")
    ),
    "0x63e66571a6936b23e03b82a44306409d9f0afe32": TokenInfo(
        currency=CurrencyInfo(symbol="NXZ", name="Nexy Zero"), scaling=Decimal("1e-18")
    ),
    "0x63f584fa56e60e4d0fe8802b27c7e6e3b33e007f": TokenInfo(
        currency=CurrencyInfo(symbol="BOX", name="ContentBox"), scaling=Decimal("1e-18")
    ),
    "0x63f88a2298a5c4aee3c216aa6d926b184a4b2437": TokenInfo(
        currency=CurrencyInfo(symbol="GAME", name="GameCredits"), scaling=Decimal("1e-18")
    ),
    "0x6400b5522f8d448c0803e6245436dd1c81df09ce": TokenInfo(
        currency=CurrencyInfo(symbol="CVNT", name="Content Value Network"), scaling=Decimal("1e-8")
    ),
    "0x6425c6be902d692ae2db752b3c268afadb099d3b": TokenInfo(
        currency=CurrencyInfo(symbol="MWAT", name="Restart Energy"), scaling=Decimal("1e-18")
    ),
    "0x642f4be6da9d9daa9076f8d161b15a166e966069": TokenInfo(
        currency=CurrencyInfo(symbol="JAC", name="Joint Admissions Chain"), scaling=Decimal("1e-8")
    ),
    "0x646707246d7d5c2a86d7206f41ca8199ea9ced69": TokenInfo(
        currency=CurrencyInfo(symbol="CHOP", name="Porkchop"), scaling=Decimal("1e-18")
    ),
    "0x6468e79a80c0eab0f9a2b574c8d5bc374af59414": TokenInfo(
        currency=CurrencyInfo(symbol="EXRD", name="e-Radix"), scaling=Decimal("1e-18")
    ),
    "0x646cec6ee42d258336165cbbd5deb4af14f0f476": TokenInfo(
        currency=CurrencyInfo(symbol="SDAO", name="Solar DAO"), scaling=Decimal("1e-4")
    ),
    "0x64786063a352b399d44de2875909d1229f120ebe": TokenInfo(
        currency=CurrencyInfo(symbol="TAUR", name="TAUR"), scaling=Decimal("1e-18")
    ),
    "0x647f274b3a7248d6cf51b35f08e7e7fd6edfb271": TokenInfo(
        currency=CurrencyInfo(symbol="MAG", name="Maggie"), scaling=Decimal("1e-0")
    ),
    "0x6489006b7d23b15c777c8690d01d46d98ae8dce3": TokenInfo(
        currency=CurrencyInfo(symbol="RMD.CX", name="Resmed"), scaling=Decimal("1e-8")
    ),
    "0x648d19d775a8d4bafba09e189090bdcbf8ef31c1": TokenInfo(
        currency=CurrencyInfo(symbol="SFR", name="Safari"), scaling=Decimal("1e-8")
    ),
    "0x64944c83481ed0228e7500c013e4c23ab825bb6d": TokenInfo(
        currency=CurrencyInfo(symbol="IAT", name="Instant Asset Token"), scaling=Decimal("1e-18")
    ),
    "0x649ebf73043ffcc70a59855ecd8a568fd996415a": TokenInfo(
        currency=CurrencyInfo(symbol="YFIII", name="YFIII"), scaling=Decimal("1e-18")
    ),
    "0x64a16ec57cca09556cc259d86886eec73493bc1e": TokenInfo(
        currency=CurrencyInfo(symbol="LHA.CX", name="Deutsche Lufthansa AG"), scaling=Decimal("1e-8")
    ),
    "0x64a31c2f28e194e670666711117314784fdc5c6c": TokenInfo(
        currency=CurrencyInfo(symbol="ROLC", name="Renewal of Life Chain"), scaling=Decimal("1e-18")
    ),
    "0x64a60493d888728cf42616e034a0dfeae38efcf0": TokenInfo(
        currency=CurrencyInfo(symbol="OLT", name="OneLedger"), scaling=Decimal("1e-18")
    ),
    "0x64aa3364f17a4d01c6f1751fd97c2bd3d7e7f1d5": TokenInfo(
        currency=CurrencyInfo(symbol="OHM", name="Olympus"), scaling=Decimal("1e-9")
    ),
    "0x64c5572e7a100af9901c148d75d72c619a7f1e9d": TokenInfo(
        currency=CurrencyInfo(symbol="UNICRAP", name="UniCrapToken.xyz"), scaling=Decimal("1e-18")
    ),
    "0x64cdf819d3e75ac8ec217b3496d7ce167be42e80": TokenInfo(
        currency=CurrencyInfo(symbol="IPL", name="InsurePal"), scaling=Decimal("1e-18")
    ),
    "0x64e65d352f6a2949463b3a7595911b61bbafc63e": TokenInfo(
        currency=CurrencyInfo(symbol="KIP", name="Khipu Token"), scaling=Decimal("1e-18")
    ),
    "0x64ea2c6104f1cf3035e28be0f781b6286d50934d": TokenInfo(
        currency=CurrencyInfo(symbol="SVC", name="Satoshivision Coin"), scaling=Decimal("1e-18")
    ),
    "0x64fa5d4fafa693d4b9f4e16fbdd1ac0e30b048b2": TokenInfo(
        currency=CurrencyInfo(symbol="THO", name="Athero"), scaling=Decimal("1e-18")
    ),
    "0x6523203bd28d399068acc14db6b7f31d9bf43f1a": TokenInfo(
        currency=CurrencyInfo(symbol="BALO", name="Balloon Coin"), scaling=Decimal("1e-18")
    ),
    "0x65292eeadf1426cd2df1c4793a3d7519f253913b": TokenInfo(
        currency=CurrencyInfo(symbol="COSS", name="COSS"), scaling=Decimal("1e-18")
    ),
    "0x6531f133e6deebe7f2dce5a0441aa7ef330b4e53": TokenInfo(
        currency=CurrencyInfo(symbol="TIME", name="Chronobank TIME"), scaling=Decimal("1e-8")
    ),
    "0x654eebac62240e6c56bab5f6adf7cfa74a894510": TokenInfo(
        currency=CurrencyInfo(symbol="ZELDA SPRING NUTS CASH", name="Zelda Spring Nuts Cash"), scaling=Decimal("1e-18")
    ),
    "0x6556d2ec4d96da39cf75cbe50d58fae90079800a": TokenInfo(
        currency=CurrencyInfo(symbol="LOT", name="Lukki Operating Token"), scaling=Decimal("1e-18")
    ),
    "0x6561a9519581e98c8e0fced50ddd419fc0e3028a": TokenInfo(
        currency=CurrencyInfo(symbol="AC3", name="AC3"), scaling=Decimal("1e-18")
    ),
    "0x658bbe318260ab879af701043b18f7e8c4daf448": TokenInfo(
        currency=CurrencyInfo(symbol="AETH", name="AnarchETH"), scaling=Decimal("1e-18")
    ),
    "0x6595b8fd9c920c81500dca94e53cdc712513fb1f": TokenInfo(
        currency=CurrencyInfo(symbol="OLY", name="Olyseum"), scaling=Decimal("1e-18")
    ),
    "0x65a15014964f2102ff58647e16a16a6b9e14bcf6": TokenInfo(
        currency=CurrencyInfo(symbol="OX", name="OX Fina"), scaling=Decimal("1e-3")
    ),
    "0x65ad6a2288b2dd23e466226397c8f5d1794e58fc": TokenInfo(
        currency=CurrencyInfo(symbol="GFX", name="GamyFi Token"), scaling=Decimal("1e-18")
    ),
    "0x65adb08beb7454c2cd5dffc271adee9fbf69632b": TokenInfo(
        currency=CurrencyInfo(symbol="ZOZ", name="ZozToken"), scaling=Decimal("1e-18")
    ),
    "0x65be44c747988fbf606207698c944df4442efe19": TokenInfo(
        currency=CurrencyInfo(symbol="FUCK", name="Finally Usable Crypto Karma"), scaling=Decimal("1e-4")
    ),
    "0x65def5029a0e7591e46b38742bfedd1fb7b24436": TokenInfo(
        currency=CurrencyInfo(symbol="KAE", name="Kanpeki"), scaling=Decimal("1e-18")
    ),
    "0x65ef703f5594d2573eb71aaf55bc0cb548492df4": TokenInfo(
        currency=CurrencyInfo(symbol="MULTI", name="Multichain"), scaling=Decimal("1e-18")
    ),
    "0x65f68e5771bde2e128232fd8fba9fa0247f1fedf": TokenInfo(
        currency=CurrencyInfo(symbol="PFD", name="PlaceFinder"), scaling=Decimal("1e-18")
    ),
    "0x660e71483785f66133548b10f6926dc332b06e61": TokenInfo(
        currency=CurrencyInfo(symbol="ADL", name="Adelphoi"), scaling=Decimal("1e-18")
    ),
    "0x6613876533bc69b9dd628611a4d5dd2ccd8c7638": TokenInfo(
        currency=CurrencyInfo(symbol="TQN", name="Toqqn"), scaling=Decimal("1e-18")
    ),
    "0x66142b81db17d7c0bd91f502d00382e326a24c2a": TokenInfo(
        currency=CurrencyInfo(symbol="GEX", name="GLOBEX"), scaling=Decimal("1e-8")
    ),
    "0x66149b85cbd202eaf4a93713702a7e94fc1121a7": TokenInfo(
        currency=CurrencyInfo(symbol="OXY2", name="Cryptoxygen"), scaling=Decimal("1e-5")
    ),
    "0x66186008c1050627f979d464eabb258860563dbe": TokenInfo(
        currency=CurrencyInfo(symbol="MDS", name="MediShares"), scaling=Decimal("1e-18")
    ),
    "0x66208d03526fc7435caa36fc4fe698c9c02a4aed": TokenInfo(
        currency=CurrencyInfo(symbol="PET", name="Allpet"), scaling=Decimal("1e-18")
    ),
    "0x6628606c321faf52b7230a57b26c01b19aa68e82": TokenInfo(
        currency=CurrencyInfo(symbol="BT", name="BitHash Token"), scaling=Decimal("1e-18")
    ),
    "0x662abcad0b7f345ab7ffb1b1fbb9df7894f18e66": TokenInfo(
        currency=CurrencyInfo(symbol="CTX", name="CarTaxi"), scaling=Decimal("1e-18")
    ),
    "0x662b67d00a13faf93254714dd601f5ed49ef2f51": TokenInfo(
        currency=CurrencyInfo(symbol="ORC", name="Orbit Chain"), scaling=Decimal("1e-18")
    ),
    "0x66497a283e0a007ba3974e837784c6ae323447de": TokenInfo(
        currency=CurrencyInfo(symbol="PT", name="PornToken"), scaling=Decimal("1e-18")
    ),
    "0x6649bcd43767a6fd7b7a10dfc98abeaa40f9141d": TokenInfo(
        currency=CurrencyInfo(symbol="ETHBTC26EMACO", name="ETH/BTC Ratio 26 EMA Crossover"), scaling=Decimal("1e-18")
    ),
    "0x6653c0d21507573cc39ead1e609d74d5e0ca16e2": TokenInfo(
        currency=CurrencyInfo(symbol="EFK", name="ReFork"), scaling=Decimal("1e-18")
    ),
    "0x6667a56d8fcb35448ee8514936e6d6c4ccc86e97": TokenInfo(
        currency=CurrencyInfo(symbol="GFC", name="GlobfoneCoin"), scaling=Decimal("1e-8")
    ),
    "0x666a64f5567c3145fba7ca9ef73648cd4fa2008f": TokenInfo(
        currency=CurrencyInfo(symbol="TFG1", name="Energoncoin"), scaling=Decimal("1e-8")
    ),
    "0x666d875c600aa06ac1cf15641361dec3b00432ef": TokenInfo(
        currency=CurrencyInfo(symbol="BTSE", name="BTSE Token"), scaling=Decimal("1e-8")
    ),
    "0x666ea3276460bd6358b49965dd336ea244174d5e": TokenInfo(
        currency=CurrencyInfo(symbol="XCPS", name="Cryphos"), scaling=Decimal("1e-8")
    ),
    "0x667088b212ce3d06a1b553a7221e1fd19000d9af": TokenInfo(
        currency=CurrencyInfo(symbol="WINGS", name="Wings"), scaling=Decimal("1e-18")
    ),
    "0x667102bd3413bfeaa3dffb48fa8288819e480a88": TokenInfo(
        currency=CurrencyInfo(symbol="TKX", name="Tokenize Xchange"), scaling=Decimal("1e-8")
    ),
    "0x6671c24dd5b8e4ced34033991418e4bc0cca05af": TokenInfo(
        currency=CurrencyInfo(symbol="ESTATE", name="AgentMile Estate"), scaling=Decimal("1e-8")
    ),
    "0x66761fa41377003622aee3c7675fc7b5c1c2fac5": TokenInfo(
        currency=CurrencyInfo(symbol="CPOOL", name="Clearpool"), scaling=Decimal("1e-18")
    ),
    "0x6682195e2a0048ce38b727a3711802d58244606e": TokenInfo(
        currency=CurrencyInfo(symbol="BTKC", name="BeautyK"), scaling=Decimal("1e-18")
    ),
    "0x668dbf100635f593a3847c0bdaf21f0a09380188": TokenInfo(
        currency=CurrencyInfo(symbol="BNSD", name="BNSD Finance"), scaling=Decimal("1e-18")
    ),
    "0x66a0f676479cee1d7373f3dc2e2952778bff5bd6": TokenInfo(
        currency=CurrencyInfo(symbol="WISE", name="Wise"), scaling=Decimal("1e-18")
    ),
    "0x66ad96678a8f9f2e91dff81457ddf2654ae22183": TokenInfo(
        currency=CurrencyInfo(symbol="CRON.CX", name="Cronos Group Inc"), scaling=Decimal("1e-8")
    ),
    "0x66af49ebaeefed6f0f43df48142341391f3f25c1": TokenInfo(
        currency=CurrencyInfo(symbol="MNGUZ", name="Mangu"), scaling=Decimal("1e-18")
    ),
    "0x66bad545596fb17a0b4ebdc003a85def10e8f6ae": TokenInfo(
        currency=CurrencyInfo(symbol="WIKI", name="Wiki Token"), scaling=Decimal("1e-18")
    ),
    "0x66d28cb58487a7609877550e1a34691810a6b9fc": TokenInfo(
        currency=CurrencyInfo(symbol="KOIN", name="Koinos"), scaling=Decimal("1e-8")
    ),
    "0x66d9c4d19b4c8e23a54c6dc4ceed141f66b8111c": TokenInfo(
        currency=CurrencyInfo(symbol="FTN", name="Fountain"), scaling=Decimal("1e-18")
    ),
    "0x66e247de1f61da1cc3e2c6e74ac15d1ba741b76f": TokenInfo(
        currency=CurrencyInfo(symbol="HI", name="Hi Friends Coin"), scaling=Decimal("1e-18")
    ),
    "0x66eb65d7ab8e9567ba0fa6e37c305956c5341574": TokenInfo(
        currency=CurrencyInfo(symbol="HLX", name="HELEX"), scaling=Decimal("1e-5")
    ),
    "0x66fd97a78d8854fec445cd1c80a07896b0b4851f": TokenInfo(
        currency=CurrencyInfo(symbol="LMY", name="Lunch Money"), scaling=Decimal("1e-18")
    ),
    "0x6704b673c70de9bf74c8fba4b4bd748f0e2190e1": TokenInfo(
        currency=CurrencyInfo(symbol="UBEX", name="Ubex"), scaling=Decimal("1e-18")
    ),
    "0x6710c63432a2de02954fc0f851db07146a6c0312": TokenInfo(
        currency=CurrencyInfo(symbol="MFG", name="Smart MFG"), scaling=Decimal("1e-18")
    ),
    "0x671abbe5ce652491985342e85428eb1b07bc6c64": TokenInfo(
        currency=CurrencyInfo(symbol="QAU", name="Quantum"), scaling=Decimal("1e-8")
    ),
    "0x672a1ad4f667fb18a333af13667aa0af1f5b5bdd": TokenInfo(
        currency=CurrencyInfo(symbol="CRED", name="Verify"), scaling=Decimal("1e-18")
    ),
    "0x6733d909e10ddedb8d6181b213de32a30ceac7ed": TokenInfo(
        currency=CurrencyInfo(symbol="BTE", name="BitSerial"), scaling=Decimal("1e-18")
    ),
    "0x6737fe98389ffb356f64ebb726aa1a92390d94fb": TokenInfo(
        currency=CurrencyInfo(symbol="ZCC", name="Zero Carbon Project"), scaling=Decimal("1e-18")
    ),
    "0x6745fab6801e376cd24f03572b9c9b0d4edddccf": TokenInfo(
        currency=CurrencyInfo(symbol="SENSE", name="Sense"), scaling=Decimal("1e-8")
    ),
    "0x674c6ad92fd080e4004b2312b45f796a192d27a0": TokenInfo(
        currency=CurrencyInfo(symbol="USDN", name="Neutrino USD"), scaling=Decimal("1e-18")
    ),
    "0x6750d0f2ba5f7f3a3ea555f734d5c109975df1c7": TokenInfo(
        currency=CurrencyInfo(symbol="RAYAX", name="RAYAX Token"), scaling=Decimal("1e-18")
    ),
    "0x6758b7d441a9739b98552b373703d8d3d14f9e62": TokenInfo(
        currency=CurrencyInfo(symbol="POA20", name="POA ERC20 on Foundation"), scaling=Decimal("1e-18")
    ),
    "0x675e7d927af7e6d0082e0153dc3485b687a6f0ad": TokenInfo(
        currency=CurrencyInfo(symbol="CREED", name="Creed Finance"), scaling=Decimal("1e-18")
    ),
    "0x677294c0e019145f595914be0ea5e5dc27974cc6": TokenInfo(
        currency=CurrencyInfo(symbol="PLA", name="SmartPlay"), scaling=Decimal("1e-18")
    ),
    "0x677a3f5d699c70c606220382c41fa473f7e2f6bb": TokenInfo(
        currency=CurrencyInfo(symbol="KOC", name="KING OF CATERING"), scaling=Decimal("1e-18")
    ),
    "0x6781a0f84c7e9e846dcb84a9a5bd49333067b104": TokenInfo(
        currency=CurrencyInfo(symbol="ZAP", name="Zap"), scaling=Decimal("1e-18")
    ),
    "0x678e840c640f619e17848045d23072844224dd37": TokenInfo(
        currency=CurrencyInfo(symbol="CRTS", name="Cratos"), scaling=Decimal("1e-18")
    ),
    "0x679131f591b4f369acb8cd8c51e68596806c3916": TokenInfo(
        currency=CurrencyInfo(symbol="TLN", name="Trustlines Network"), scaling=Decimal("1e-18")
    ),
    "0x679badc551626e01b23ceecefbc9b877ea18fc46": TokenInfo(
        currency=CurrencyInfo(symbol="CCO", name="Ccore"), scaling=Decimal("1e-18")
    ),
    "0x67a1ca08e580af9f54dc9b03fd59ec2388ad7c6c": TokenInfo(
        currency=CurrencyInfo(symbol="TIEN", name="TiEN Blockchain"), scaling=Decimal("1e-18")
    ),
    "0x67a9099f0008c35c61c00042cd9fb03684451097": TokenInfo(
        currency=CurrencyInfo(symbol="GST", name="Game Stars"), scaling=Decimal("1e-18")
    ),
    "0x67ab11058ef23d0a19178f61a050d3c38f81ae21": TokenInfo(
        currency=CurrencyInfo(symbol="SELF", name="SELF TOKEN"), scaling=Decimal("1e-18")
    ),
    "0x67b6d479c7bb412c54e03dca8e1bc6740ce6b99c": TokenInfo(
        currency=CurrencyInfo(symbol="KYL", name="Kylin Network"), scaling=Decimal("1e-18")
    ),
    "0x67c597624b17b16fb77959217360b7cd18284253": TokenInfo(
        currency=CurrencyInfo(symbol="MARK", name="Benchmark Protocol"), scaling=Decimal("1e-9")
    ),
    "0x68037790a0229e9ce6eaa8a99ea92964106c4703": TokenInfo(
        currency=CurrencyInfo(symbol="PAR", name="Parallel Protocol"), scaling=Decimal("1e-18")
    ),
    "0x6810e776880c02933d47db1b9fc05908e5386b96": TokenInfo(
        currency=CurrencyInfo(symbol="GNO", name="Gnosis"), scaling=Decimal("1e-18")
    ),
    "0x681724368d052a4e29fc226ed5085082d74fe716": TokenInfo(
        currency=CurrencyInfo(symbol="SRM", name="SOLARMINING"), scaling=Decimal("1e-18")
    ),
    "0x681ecc5a0bfd18c308a1138ff607f818bac5e417": TokenInfo(
        currency=CurrencyInfo(symbol="LST", name="Luckstar"), scaling=Decimal("1e-18")
    ),
    "0x681f1a3761384109e5bc52f7d479ef27540a5641": TokenInfo(
        currency=CurrencyInfo(symbol="TRXMOON", name="10X Long TRX Token"), scaling=Decimal("1e-18")
    ),
    "0x68350d30d9f58c81aaaa41929f1bfc52fff4ea49": TokenInfo(
        currency=CurrencyInfo(symbol="RPZX", name="Rapidz"), scaling=Decimal("1e-18")
    ),
    "0x68496ee825dafe1cf66d4083f776b9eaab31e447": TokenInfo(
        currency=CurrencyInfo(symbol="RAUX", name="ErcauX"), scaling=Decimal("1e-18")
    ),
    "0x684e2dcb12bb755237e07242529c82f78a84ea61": TokenInfo(
        currency=CurrencyInfo(symbol="WELL", name="WELL"), scaling=Decimal("1e-18")
    ),
    "0x685aea4f02e39e5a5bb7f7117e88db1151f38364": TokenInfo(
        currency=CurrencyInfo(symbol="POSH", name="Shill"), scaling=Decimal("1e-18")
    ),
    "0x6863be0e7cf7ce860a574760e9020d519a8bdc47": TokenInfo(
        currency=CurrencyInfo(symbol="ONL", name="On.Live"), scaling=Decimal("1e-18")
    ),
    "0x686f2404e77ab0d9070a46cdfb0b7fecdd2318b0": TokenInfo(
        currency=CurrencyInfo(symbol="LORDS", name="LORDS"), scaling=Decimal("1e-18")
    ),
    "0x687174f8c49ceb7729d925c3a961507ea4ac7b28": TokenInfo(
        currency=CurrencyInfo(symbol="GAT", name="Gatcoin"), scaling=Decimal("1e-18")
    ),
    "0x6871799a4866bb9068b36b7a9bb93475ac77ac5d": TokenInfo(
        currency=CurrencyInfo(symbol="NZDX", name="eToro New Zealand Dollar"), scaling=Decimal("1e-18")
    ),
    "0x6872cdcbaed6edd4f319842917173e0ab8617fef": TokenInfo(
        currency=CurrencyInfo(symbol="CIEN.CX", name="Ciena"), scaling=Decimal("1e-8")
    ),
    "0x68749665ff8d2d112fa859aa293f07a622782f38": TokenInfo(
        currency=CurrencyInfo(symbol="XAUT", name="Tether Gold"), scaling=Decimal("1e-6")
    ),
    "0x6876eba317272fe221c67405c5e8eb3b24535547": TokenInfo(
        currency=CurrencyInfo(symbol="MCT", name="Micro Tuber"), scaling=Decimal("1e-18")
    ),
    "0x687a790e4e94a8abf9952aed635c80a5540d7e5c": TokenInfo(
        currency=CurrencyInfo(symbol="WMPRO", name="WM PROFESSIONAL"), scaling=Decimal("1e-18")
    ),
    "0x687bfc3e73f6af55f0ccca8450114d107e781a0e": TokenInfo(
        currency=CurrencyInfo(symbol="QCH", name="QChi"), scaling=Decimal("1e-18")
    ),
    "0x6888a16ea9792c15a4dcf2f6c623d055c8ede792": TokenInfo(
        currency=CurrencyInfo(symbol="SIG", name="Signal Token"), scaling=Decimal("1e-18")
    ),
    "0x688ff43c3c19e4714f0beb76df8ee394207ab411": TokenInfo(
        currency=CurrencyInfo(symbol="R2R", name="RoboAi Coin R2R"), scaling=Decimal("1e-18")
    ),
    "0x68909e586eeac8f47315e84b4c9788dd54ef65bb": TokenInfo(
        currency=CurrencyInfo(symbol="EVN", name="EvenCoin"), scaling=Decimal("1e-18")
    ),
    "0x68a118ef45063051eac49c7e647ce5ace48a68a5": TokenInfo(
        currency=CurrencyInfo(symbol="$BASED", name="Based Money"), scaling=Decimal("1e-18")
    ),
    "0x68a3637ba6e75c0f66b61a42639c4e9fcd3d4824": TokenInfo(
        currency=CurrencyInfo(symbol="MOON", name="MoonSwap"), scaling=Decimal("1e-18")
    ),
    "0x68aa3f232da9bdc2343465545794ef3eea5209bd": TokenInfo(
        currency=CurrencyInfo(symbol="MSP", name="Mothership"), scaling=Decimal("1e-18")
    ),
    "0x68c5e456f4156e8500ea7ea0218b84b1749fb2d8": TokenInfo(
        currency=CurrencyInfo(symbol="CAG.CX", name="Conagra Brands Inc"), scaling=Decimal("1e-8")
    ),
    "0x68cbc28321666cf93d933c495631e81051fe656e": TokenInfo(
        currency=CurrencyInfo(symbol="ADS.CX", name="Adidas AG"), scaling=Decimal("1e-8")
    ),
    "0x68d53441c0e253f76c500e551bdea3d102206c9a": TokenInfo(
        currency=CurrencyInfo(symbol="DST", name="Dimensions Strike Token"), scaling=Decimal("1e-18")
    ),
    "0x68d57c9a1c35f63e2c83ee8e49a64e9d70528d25": TokenInfo(
        currency=CurrencyInfo(symbol="SRN", name="Sirin Labs Token"), scaling=Decimal("1e-18")
    ),
    "0x68e0a48d3bff6633a31d1d100b70f93c3859218b": TokenInfo(
        currency=CurrencyInfo(symbol="BNFI", name="Blaze DeFi"), scaling=Decimal("1e-18")
    ),
    "0x68e14bb5a45b9681327e16e528084b9d962c1a39": TokenInfo(
        currency=CurrencyInfo(symbol="CAT", name="BitClave - Consumer Activity Token"), scaling=Decimal("1e-18")
    ),
    "0x68eb95dc9934e19b86687a10df8e364423240e94": TokenInfo(
        currency=CurrencyInfo(symbol="BULL", name="3X Long Bitcoin Token"), scaling=Decimal("1e-18")
    ),
    "0x68fec0bcc61727ddec5cece2683027a383492710": TokenInfo(
        currency=CurrencyInfo(symbol="GMC", name="GemmyCoin"), scaling=Decimal("1e-18")
    ),
    "0x6913ccabbc337f0ea7b4109dd8200d61c704d332": TokenInfo(
        currency=CurrencyInfo(symbol="ASAC", name="Asac Coin"), scaling=Decimal("1e-8")
    ),
    "0x6927c69fb4daf2043fbb1cb7b86c5661416bea29": TokenInfo(
        currency=CurrencyInfo(symbol="ETR", name="Etheruem Risen"), scaling=Decimal("1e-18")
    ),
    "0x69428bb4272e3181de9e3cab461e19b0131855c8": TokenInfo(
        currency=CurrencyInfo(symbol="SYBC", name="SYBC Coin"), scaling=Decimal("1e-8")
    ),
    "0x694404595e3075a942397f466aacd462ff1a7bd0": TokenInfo(
        currency=CurrencyInfo(symbol="PATENTS", name="smartillions.io Class 1 ETH"), scaling=Decimal("1e-18")
    ),
    "0x6944d3e38973c4831da24e954fbd790c7e688bdd": TokenInfo(
        currency=CurrencyInfo(symbol="IZE", name="IZE"), scaling=Decimal("1e-18")
    ),
    "0x695106ad73f506f9d0a9650a78019a93149ae07c": TokenInfo(
        currency=CurrencyInfo(symbol="BNS", name="BNS Token"), scaling=Decimal("1e-8")
    ),
    "0x6956983f8b3ce173b4ab84361aa0ad52f38d936f": TokenInfo(
        currency=CurrencyInfo(symbol="CFTY", name="Crafty"), scaling=Decimal("1e-8")
    ),
    "0x69692d3345010a207b759a7d1af6fc7f38b35c5e": TokenInfo(
        currency=CurrencyInfo(symbol="CHADS", name="CHADS VC"), scaling=Decimal("1e-18")
    ),
    "0x696a846252e7d19cae1ca30dd918768c0623ed6c": TokenInfo(
        currency=CurrencyInfo(symbol="SMP", name="THESMP"), scaling=Decimal("1e-18")
    ),
    "0x697beac28b09e122c4332d163985e8a73121b97f": TokenInfo(
        currency=CurrencyInfo(symbol="QRL", name="QRL"), scaling=Decimal("1e-8")
    ),
    "0x697ef32b4a3f5a4c39de1cb7563f24ca7bfc5947": TokenInfo(
        currency=CurrencyInfo(symbol="ISLA", name="Insula"), scaling=Decimal("1e-18")
    ),
    "0x69948cc03f478b95283f7dbf1ce764d0fc7ec54c": TokenInfo(
        currency=CurrencyInfo(symbol="AREN", name="Aave REN v1"), scaling=Decimal("1e-18")
    ),
    "0x69a57832540c00b7647a9643b8014930cfabd4cc": TokenInfo(
        currency=CurrencyInfo(symbol="ESR", name="ESR Wallet"), scaling=Decimal("1e-6")
    ),
    "0x69a95185ee2a045cdc4bcd1b1df10710395e4e23": TokenInfo(
        currency=CurrencyInfo(symbol="POOLZ", name="Poolz Finance"), scaling=Decimal("1e-18")
    ),
    "0x69af81e73a73b40adf4f3d4223cd9b1ece623074": TokenInfo(
        currency=CurrencyInfo(symbol="MASK", name="Mask Network"), scaling=Decimal("1e-18")
    ),
    "0x69b148395ce0015c13e36bffbad63f49ef874e03": TokenInfo(
        currency=CurrencyInfo(symbol="DTA", name="DATA"), scaling=Decimal("1e-18")
    ),
    "0x69beab403438253f13b6e92db91f7fb849258263": TokenInfo(
        currency=CurrencyInfo(symbol="NTK", name="Neurotoken"), scaling=Decimal("1e-18")
    ),
    "0x69c4bb240cf05d51eeab6985bab35527d04a8c64": TokenInfo(
        currency=CurrencyInfo(symbol="OPEN", name="OPEN"), scaling=Decimal("1e-8")
    ),
    "0x69cf3091c91eb72db05e45c76e58225177dea742": TokenInfo(
        currency=CurrencyInfo(symbol="ZOOM", name="CoinZoom Token"), scaling=Decimal("1e-18")
    ),
    "0x69d2779533a4d2c780639713558b2cc98c46a9b7": TokenInfo(
        currency=CurrencyInfo(symbol="VNT", name="VNT Chain"), scaling=Decimal("1e-8")
    ),
    "0x69d9905b2e5f6f5433212b7f3c954433f23c1572": TokenInfo(
        currency=CurrencyInfo(symbol="OOKS", name="Onooks"), scaling=Decimal("1e-18")
    ),
    "0x69dc5556a91dfab39f8d50f6fe552296f2268dda": TokenInfo(
        currency=CurrencyInfo(symbol="WND", name="Wonder"), scaling=Decimal("1e-5")
    ),
    "0x69e8b9528cabda89fe846c67675b5d73d463a916": TokenInfo(
        currency=CurrencyInfo(symbol="OPEN", name="OPEN Governance Token"), scaling=Decimal("1e-18")
    ),
    "0x69f64d814aa278825997e71738120392993973a4": TokenInfo(
        currency=CurrencyInfo(symbol="CRV", name="Crowdvilla Ownership"), scaling=Decimal("1e-8")
    ),
    "0x69fa0fee221ad11012bab0fdb45d444d3d2ce71c": TokenInfo(
        currency=CurrencyInfo(symbol="XRUNE", name="Thorstarter"), scaling=Decimal("1e-18")
    ),
    "0x69fa8e7f6bf1ca1fb0de61e1366f7412b827cc51": TokenInfo(
        currency=CurrencyInfo(symbol="NRCH", name="EnreachDAO"), scaling=Decimal("1e-9")
    ),
    "0x6a09e1b7cc5cb52ffdfc585a8df51ced7063915c": TokenInfo(
        currency=CurrencyInfo(symbol="RAVE", name="Ravelous"), scaling=Decimal("1e-18")
    ),
    "0x6a0a97e47d15aad1d132a1ac79a480e3f2079063": TokenInfo(
        currency=CurrencyInfo(symbol="WCT", name="WePower Contribution Token"), scaling=Decimal("1e-18")
    ),
    "0x6a0ae448da83d73b291a199b798d13bb2e7d664d": TokenInfo(
        currency=CurrencyInfo(symbol="WWW", name="World Wide Web Coin"), scaling=Decimal("1e-18")
    ),
    "0x6a22e5e94388464181578aa7a6b869e00fe27846": TokenInfo(
        currency=CurrencyInfo(symbol="SXAG", name="sXAG"), scaling=Decimal("1e-18")
    ),
    "0x6a27348483d59150ae76ef4c0f3622a78b0ca698": TokenInfo(
        currency=CurrencyInfo(symbol="BKBT", name="BeeKan / Beenews"), scaling=Decimal("1e-18")
    ),
    "0x6a36a309acb68d7fb3605bc627c3ae68de3d2961": TokenInfo(
        currency=CurrencyInfo(symbol="ETL.CX", name="Eutelsat Communications"), scaling=Decimal("1e-8")
    ),
    "0x6a404a3386655bd8b63e584f2efd2e3fb60e70f8": TokenInfo(
        currency=CurrencyInfo(symbol="LXC", name="Latex Chain"), scaling=Decimal("1e-18")
    ),
    "0x6a4c76874e686a7d080d173987a35a9c48905583": TokenInfo(
        currency=CurrencyInfo(symbol="LPNT", name="Luxurious Pro Network Token"), scaling=Decimal("1e-18")
    ),
    "0x6a532b08c654a1a86069b74c560d8fa0ff842218": TokenInfo(
        currency=CurrencyInfo(symbol="PKP", name="Pikto Group"), scaling=Decimal("1e-18")
    ),
    "0x6a5a44f3c814b064dec0465ad97500ab255922c2": TokenInfo(
        currency=CurrencyInfo(symbol="ALLY.CX", name="Ally Financial"), scaling=Decimal("1e-8")
    ),
    "0x6a6c2ada3ce053561c2fbc3ee211f23d9b8c520a": TokenInfo(
        currency=CurrencyInfo(symbol="TON", name="TONToken"), scaling=Decimal("1e-18")
    ),
    "0x6a6d430573d3f070aeab97b3a189d698ea130454": TokenInfo(
        currency=CurrencyInfo(symbol="WBCD", name="Wrapped Bitcoin Diamond"), scaling=Decimal("1e-7")
    ),
    "0x6a7ef4998eb9d0f706238756949f311a59e05745": TokenInfo(
        currency=CurrencyInfo(symbol="KEN", name="Keysians Network"), scaling=Decimal("1e-18")
    ),
    "0x6a8c66cab4f766e5e30b4e9445582094303cc322": TokenInfo(
        currency=CurrencyInfo(symbol="PFARM", name="Farm Defi"), scaling=Decimal("1e-18")
    ),
    "0x6aa27b3a8aab51745b7eaf53e61aba833b0f9400": TokenInfo(
        currency=CurrencyInfo(symbol="PCC", name="Pcore"), scaling=Decimal("1e-8")
    ),
    "0x6aac8cb9861e42bf8259f5abdc6ae3ae89909e11": TokenInfo(
        currency=CurrencyInfo(symbol="BTCRED", name="Bitcoin Red"), scaling=Decimal("1e-8")
    ),
    "0x6ab4a7d75b0a42b6bc83e852dab9e121f9c610aa": TokenInfo(
        currency=CurrencyInfo(symbol="EUM", name="Elitium"), scaling=Decimal("1e-18")
    ),
    "0x6aba1623ea906d1164cbb007e764ebde2514a2ba": TokenInfo(
        currency=CurrencyInfo(symbol="AAA", name="AAAchain"), scaling=Decimal("1e-10")
    ),
    "0x6abd8652564093de6f28e13cdfbf976300fa0c72": TokenInfo(
        currency=CurrencyInfo(symbol="C.CX", name="Citigroup Inc"), scaling=Decimal("1e-8")
    ),
    "0x6adb2e268de2aa1abf6578e4a8119b960e02928f": TokenInfo(
        currency=CurrencyInfo(symbol="SHIBDOGE", name="ShibaDoge"), scaling=Decimal("1e-9")
    ),
    "0x6aeb95f06cda84ca345c2de0f3b7f96923a44f4c": TokenInfo(
        currency=CurrencyInfo(symbol="BERRY", name="Rentberry"), scaling=Decimal("1e-14")
    ),
    "0x6aedbf8dff31437220df351950ba2a3362168d1b": TokenInfo(
        currency=CurrencyInfo(symbol="DGS", name="Dragonglass"), scaling=Decimal("1e-8")
    ),
    "0x6af406c781dba39f71184a53155e94393a0dafc8": TokenInfo(
        currency=CurrencyInfo(symbol="MBMT", name="MessengerBank Metals Token"), scaling=Decimal("1e-18")
    ),
    "0x6afde9e8732eb8fe6376ae98347e64e2895299d4": TokenInfo(
        currency=CurrencyInfo(symbol="$BASED", name="$BASED"), scaling=Decimal("1e-18")
    ),
    "0x6b048d884188895eba104645ee6ffa093fe80a07": TokenInfo(
        currency=CurrencyInfo(symbol="ERAZ", name="Erazer"), scaling=Decimal("1e-18")
    ),
    "0x6b0d7b8357bb851de9f1953199c39c7bc4675796": TokenInfo(
        currency=CurrencyInfo(symbol="SUNC", name="Sunchain"), scaling=Decimal("1e-18")
    ),
    "0x6b175474e89094c44da98b954eedeac495271d0f": TokenInfo(
        currency=CurrencyInfo(symbol="DAI", name="Dai"), scaling=Decimal("1e-18")
    ),
    "0x6b193e107a773967bd821bcf8218f3548cfa2503": TokenInfo(
        currency=CurrencyInfo(symbol="POSS", name="Posscoin"), scaling=Decimal("1e-18")
    ),
    "0x6b2bab5e4b9bc9592636c16bc4e5e07ef076cd6d": TokenInfo(
        currency=CurrencyInfo(symbol="SLD", name="MP Shield"), scaling=Decimal("1e-18")
    ),
    "0x6b3595068778dd592e39a122f4f5a5cf09c90fe2": TokenInfo(
        currency=CurrencyInfo(symbol="SUSHI", name="Sushi"), scaling=Decimal("1e-18")
    ),
    "0x6b40089e6cba08696d9ae48f38e2b06faff81765": TokenInfo(
        currency=CurrencyInfo(symbol="SKO", name="Sikoba Network Token"), scaling=Decimal("1e-18")
    ),
    "0x6b40d317bc1de4b0938519ac707ae36464f49171": TokenInfo(
        currency=CurrencyInfo(symbol="EVEO", name="EVERY ORIGINAL"), scaling=Decimal("1e-18")
    ),
    "0x6b4389afb3e243a65668b7311fa9ef092a8a3b64": TokenInfo(
        currency=CurrencyInfo(symbol="REAL", name="Real Coin"), scaling=Decimal("1e-18")
    ),
    "0x6b466b0232640382950c45440ea5b630744eca99": TokenInfo(
        currency=CurrencyInfo(symbol="CVD", name="Covid19"), scaling=Decimal("1e-0")
    ),
    "0x6b4689e4514957699edeb2ee91c947f18e439806": TokenInfo(
        currency=CurrencyInfo(symbol="ZUC", name="ZeuxCoin"), scaling=Decimal("1e-18")
    ),
    "0x6b4c7a5e3f0b99fcd83e9c089bddd6c7fce5c611": TokenInfo(
        currency=CurrencyInfo(symbol="MM", name="Million"), scaling=Decimal("1e-18")
    ),
    "0x6b60d7285504d73dd88547cf1289c3b5528827d3": TokenInfo(
        currency=CurrencyInfo(symbol="MFT", name="MaskFactory"), scaling=Decimal("1e-18")
    ),
    "0x6b785a0322126826d8226d77e173d75dafb84d11": TokenInfo(
        currency=CurrencyInfo(symbol="VLT", name="Bankroll Vault"), scaling=Decimal("1e-18")
    ),
    "0x6b87999be87358065bbde41e8a0fe0b7b1cd2514": TokenInfo(
        currency=CurrencyInfo(symbol="TSW", name="TeslaWatt"), scaling=Decimal("1e-18")
    ),
    "0x6b9f031d718dded0d681c20cb754f97b3bb81b78": TokenInfo(
        currency=CurrencyInfo(symbol="GEEQ", name="GEEQ"), scaling=Decimal("1e-18")
    ),
    "0x6b9f1f092e0b10015a4391a80cd3e6b6cefd1728": TokenInfo(
        currency=CurrencyInfo(symbol="LST", name="LuckySevenToken"), scaling=Decimal("1e-18")
    ),
    "0x6ba083855c2a5b11fa557c853d73f4c215d6866c": TokenInfo(
        currency=CurrencyInfo(symbol="MTN", name="Motion One"), scaling=Decimal("1e-18")
    ),
    "0x6ba460ab75cd2c56343b3517ffeba60748654d26": TokenInfo(
        currency=CurrencyInfo(symbol="UP", name="UpToken"), scaling=Decimal("1e-8")
    ),
    "0x6baa91cd8aa07431760ef2eedfedcef662a6b8b3": TokenInfo(
        currency=CurrencyInfo(symbol="EXCHBEAR", name="3X Short Exchange Token Index Token"), scaling=Decimal("1e-18")
    ),
    "0x6baf7fcea90b0968dc5ed7b8dcb76c986637ff55": TokenInfo(
        currency=CurrencyInfo(symbol="HLI", name="Hoolicoin"), scaling=Decimal("1e-18")
    ),
    "0x6bb61215298f296c55b19ad842d3df69021da2ef": TokenInfo(
        currency=CurrencyInfo(symbol="DOP", name="Drops Ownership Pow"), scaling=Decimal("1e-18")
    ),
    "0x6bba316c48b49bd1eac44573c5c871ff02958469": TokenInfo(
        currency=CurrencyInfo(symbol="GAS", name="Gas DAO"), scaling=Decimal("1e-18")
    ),
    "0x6bc1f3a1ae56231dbb64d3e82e070857eae86045": TokenInfo(
        currency=CurrencyInfo(symbol="XSR", name="Xensor"), scaling=Decimal("1e-18")
    ),
    "0x6bc4375083d3ad563de91cad8438f629841448a5": TokenInfo(
        currency=CurrencyInfo(symbol="ID7", name="Cryptogeneid Token"), scaling=Decimal("1e-18")
    ),
    "0x6be61833fc4381990e82d7d4a9f4c9b3f67ea941": TokenInfo(
        currency=CurrencyInfo(symbol="HTB", name="Hotbit Token"), scaling=Decimal("1e-18")
    ),
    "0x6be7e93e45740c314c89a3be52473a0ddf2450fe": TokenInfo(
        currency=CurrencyInfo(symbol="XFYI", name="XCredit"), scaling=Decimal("1e-18")
    ),
    "0x6beb418fc6e1958204ac8baddcf109b8e9694966": TokenInfo(
        currency=CurrencyInfo(symbol="LNC", name="Linker Coin"), scaling=Decimal("1e-18")
    ),
    "0x6bec54e4fea5d541fb14de96993b8e11d81159b2": TokenInfo(
        currency=CurrencyInfo(symbol="FTEC", name="FTEC"), scaling=Decimal("1e-18")
    ),
    "0x6c103d85c15107dce19f5a75fc746227e610aabd": TokenInfo(
        currency=CurrencyInfo(symbol="UPEUR", name="Universal Euro"), scaling=Decimal("1e-2")
    ),
    "0x6c139349ee94ebaaff55ed52d382673c263b22d6": TokenInfo(
        currency=CurrencyInfo(symbol="EURU", name="Upper Euro"), scaling=Decimal("1e-18")
    ),
    "0x6c158864d3b06113bfd9f5f2c219725fd5bc3923": TokenInfo(
        currency=CurrencyInfo(symbol="METH", name="Mini Ethereum 2"), scaling=Decimal("1e-0")
    ),
    "0x6c22b815904165f3599f0a4a092d458966bd8024": TokenInfo(
        currency=CurrencyInfo(symbol="BPTN", name="Bit Public Talent Network"), scaling=Decimal("1e-18")
    ),
    "0x6c28aef8977c9b773996d0e8376d2ee379446f2f": TokenInfo(
        currency=CurrencyInfo(symbol="QUICK", name="Quickswap"), scaling=Decimal("1e-18")
    ),
    "0x6c2adc2073994fb2ccc5032cc2906fa221e9b391": TokenInfo(
        currency=CurrencyInfo(symbol="DPY", name="Delphy"), scaling=Decimal("1e-18")
    ),
    "0x6c37bf4f042712c978a73e3fd56d1f5738dd7c43": TokenInfo(
        currency=CurrencyInfo(symbol="ELET", name="Elementeum"), scaling=Decimal("1e-18")
    ),
    "0x6c3be406174349cfa4501654313d97e6a31072e1": TokenInfo(
        currency=CurrencyInfo(symbol="CNNS", name="CNNS"), scaling=Decimal("1e-18")
    ),
    "0x6c3f90f043a72fa612cbac8115ee7e52bde6e490": TokenInfo(
        currency=CurrencyInfo(symbol="3CRV", name="LP 3pool Curve"), scaling=Decimal("1e-18")
    ),
    "0x6c4522f0035bed2180b40f4c5d9dbaab64b41325": TokenInfo(
        currency=CurrencyInfo(symbol="PASS", name="Passport Finance"), scaling=Decimal("1e-18")
    ),
    "0x6c4b85cab20c13af72766025f0e17e0fe558a553": TokenInfo(
        currency=CurrencyInfo(symbol="YFFII", name="YFFII Finance"), scaling=Decimal("1e-18")
    ),
    "0x6c5024cd4f8a59110119c56f8933403a539555eb": TokenInfo(
        currency=CurrencyInfo(symbol="ASUSD", name="Aave SUSD"), scaling=Decimal("1e-18")
    ),
    "0x6c5ba91642f10282b576d91922ae6448c9d52f4e": TokenInfo(
        currency=CurrencyInfo(symbol="PHA", name="Phala Network"), scaling=Decimal("1e-18")
    ),
    "0x6c5fbc90e4d78f70cc5025db005b39b03914fc0c": TokenInfo(
        currency=CurrencyInfo(symbol="URUS", name="Aurox Token"), scaling=Decimal("1e-18")
    ),
    "0x6c6ab7fc6f906298d54fed3606a39b5e5ee5f782": TokenInfo(
        currency=CurrencyInfo(symbol="FWY", name="Fairway"), scaling=Decimal("1e-18")
    ),
    "0x6c6ee5e31d828de241282b9606c8e98ea48526e2": TokenInfo(
        currency=CurrencyInfo(symbol="HOT", name="Holo"), scaling=Decimal("1e-18")
    ),
    "0x6c86228d240c22d4f4744654026326895351b2ec": TokenInfo(
        currency=CurrencyInfo(symbol="ORC", name="Oracle G"), scaling=Decimal("1e-8")
    ),
    "0x6c8aad3100e3fa45aac799c0c302400900b60302": TokenInfo(
        currency=CurrencyInfo(symbol="YFIC", name="Yfi Credits"), scaling=Decimal("1e-18")
    ),
    "0x6c8c6b02e7b2be14d4fa6022dfd6d75921d90e4e": TokenInfo(
        currency=CurrencyInfo(symbol="CBAT", name="cBAT"), scaling=Decimal("1e-8")
    ),
    "0x6c929cde908481f3d1d775008791f42b1b89dbb0": TokenInfo(
        currency=CurrencyInfo(symbol="BOOL", name="Boolean"), scaling=Decimal("1e-18")
    ),
    "0x6c972b70c533e2e045f333ee28b9ffb8d717be69": TokenInfo(
        currency=CurrencyInfo(symbol="FRY", name="FoundryDAO Logistics"), scaling=Decimal("1e-18")
    ),
    "0x6ca88cc8d9288f5cad825053b6a1b179b05c76fc": TokenInfo(
        currency=CurrencyInfo(symbol="UPT", name="Universal Protocol Token"), scaling=Decimal("1e-18")
    ),
    "0x6cb1c2b61e24ad08bf5fff4d2b13ea987d211a88": TokenInfo(
        currency=CurrencyInfo(symbol="UBBEY", name="Universal Labs"), scaling=Decimal("1e-18")
    ),
    "0x6cb218854502a4e0f2ceb202616847ba470df1ca": TokenInfo(
        currency=CurrencyInfo(symbol="SPN.CX", name="Superi Ener Svcs"), scaling=Decimal("1e-8")
    ),
    "0x6cb262679c522c4f0834041a6248e8feb35f0337": TokenInfo(
        currency=CurrencyInfo(symbol="IOT", name="Itube Online Token"), scaling=Decimal("1e-18")
    ),
    "0x6cbedec4f1ac9d874987d2769596544e0d9161ab": TokenInfo(
        currency=CurrencyInfo(symbol="DEEP", name="DeepCloud AI"), scaling=Decimal("1e-18")
    ),
    "0x6ccb56947ea1d6efdc81acfbacd8263ddfa9b202": TokenInfo(
        currency=CurrencyInfo(symbol="RKC", name="Royal Kingdom Coin"), scaling=Decimal("1e-18")
    ),
    "0x6ccd05f73a54359a257fc5649c598a3de75905e7": TokenInfo(
        currency=CurrencyInfo(symbol="PDF", name="Port of DeFi Network"), scaling=Decimal("1e-18")
    ),
    "0x6ce654ac973d326f89f0685e7459542641410ed9": TokenInfo(
        currency=CurrencyInfo(symbol="HD", name="HubDao"), scaling=Decimal("1e-18")
    ),
    "0x6cfb6df56bbdb00226aeffcdb2cd1fe8da1abda7": TokenInfo(
        currency=CurrencyInfo(symbol="KOMET", name="Komet"), scaling=Decimal("1e-18")
    ),
    "0x6d0f5149c502faf215c89ab306ec3e50b15e2892": TokenInfo(
        currency=CurrencyInfo(symbol="PRT", name="Portion"), scaling=Decimal("1e-18")
    ),
    "0x6d2c508fc4a588a41713ff59212f85489291d244": TokenInfo(
        currency=CurrencyInfo(symbol="BLCT", name="Bloomzed Loyalty Club Ticket"), scaling=Decimal("1e-18")
    ),
    "0x6d45640f5d0b75280647f2f37ccd19c1167f833c": TokenInfo(
        currency=CurrencyInfo(symbol="FLEX", name="Flex Token"), scaling=Decimal("1e-4")
    ),
    "0x6d6506e6f438ede269877a0a720026559110b7d5": TokenInfo(
        currency=CurrencyInfo(symbol="BONK", name="BONK Token"), scaling=Decimal("1e-18")
    ),
    "0x6d68a12305051291d194162b8406aea080342645": TokenInfo(
        currency=CurrencyInfo(symbol="TDN", name="TODA Note"), scaling=Decimal("1e-18")
    ),
    "0x6d728ff862bfe74be2aba30537e992a24f259a22": TokenInfo(
        currency=CurrencyInfo(symbol="SIH", name="Salient Investment Holding"), scaling=Decimal("1e-18")
    ),
    "0x6d7917864003a9bb13cbbec8f1cdd4e36ddf6fc8": TokenInfo(
        currency=CurrencyInfo(symbol="SEMI", name="Semitoken"), scaling=Decimal("1e-18")
    ),
    "0x6dc02164d75651758ac74435806093e421b64605": TokenInfo(
        currency=CurrencyInfo(symbol="CHI", name="XAYA"), scaling=Decimal("1e-8")
    ),
    "0x6dccf9c0ab71dac26b7f7886e43a2b433806c590": TokenInfo(
        currency=CurrencyInfo(symbol="VBX", name="vibrant"), scaling=Decimal("1e-18")
    ),
    "0x6dd4e4aad29a40edd6a409b9c1625186c9855b4d": TokenInfo(
        currency=CurrencyInfo(symbol="GENE", name="Parkgene"), scaling=Decimal("1e-8")
    ),
    "0x6dddf4111ad997a8c7be9b2e502aa476bf1f4251": TokenInfo(
        currency=CurrencyInfo(symbol="UNT", name="Unimonitor"), scaling=Decimal("1e-18")
    ),
    "0x6de037ef9ad2725eb40118bb1702ebb27e4aeb24": TokenInfo(
        currency=CurrencyInfo(symbol="RNDR", name="Render Token"), scaling=Decimal("1e-18")
    ),
    "0x6de0d485a8218c0208db949456df05dd22450002": TokenInfo(
        currency=CurrencyInfo(symbol="ZGOLD", name="ZOLOGOLD"), scaling=Decimal("1e-8")
    ),
    "0x6dea81c8171d0ba574754ef6f8b412f2ed88c54d": TokenInfo(
        currency=CurrencyInfo(symbol="LQTY", name="Liquity"), scaling=Decimal("1e-18")
    ),
    "0x6e0dade58d2d89ebbe7afc384e3e4f15b70b14d8": TokenInfo(
        currency=CurrencyInfo(symbol="QRX", name="QuiverX"), scaling=Decimal("1e-18")
    ),
    "0x6e13a9e4ae3d0678e511fb6d2ad531fcf0e247bf": TokenInfo(
        currency=CurrencyInfo(symbol="BSVBULL", name="3X Long Bitcoin SV Token"), scaling=Decimal("1e-18")
    ),
    "0x6e1a19f235be7ed8e3369ef73b196c07257494de": TokenInfo(
        currency=CurrencyInfo(symbol="WFIL", name="Wrapped Filecoin"), scaling=Decimal("1e-18")
    ),
    "0x6e2050cbfb3ed8a4d39b64cc9f47e711a03a5a89": TokenInfo(
        currency=CurrencyInfo(symbol="SWRM", name="SWRM Coin"), scaling=Decimal("1e-18")
    ),
    "0x6e336c1934d99dab9ca3e4cc6357051aef4dfc0f": TokenInfo(
        currency=CurrencyInfo(symbol="PE", name="Preschool Education"), scaling=Decimal("1e-18")
    ),
    "0x6e34d8d84764d40f6d7b39cd569fd017bf53177d": TokenInfo(
        currency=CurrencyInfo(symbol="SKRP", name="Skraps"), scaling=Decimal("1e-18")
    ),
    "0x6e36556b3ee5aa28def2a8ec3dae30ec2b208739": TokenInfo(
        currency=CurrencyInfo(symbol="BUILD", name="BUILD Finance"), scaling=Decimal("1e-18")
    ),
    "0x6e55027cae60cfdb7baca78f3e6514aee716fcf9": TokenInfo(
        currency=CurrencyInfo(symbol="NECOS", name="Nano Ecosystem"), scaling=Decimal("1e-5")
    ),
    "0x6e5a43db10b04701385a34afb670e404bc7ea597": TokenInfo(
        currency=CurrencyInfo(symbol="RKN", name="RAKON"), scaling=Decimal("1e-12")
    ),
    "0x6e605c269e0c92e70beeb85486f1fc550f9380bd": TokenInfo(
        currency=CurrencyInfo(symbol="CATT", name="Catex Token"), scaling=Decimal("1e-18")
    ),
    "0x6e742e29395cf5736c358538f0f1372ab3dfe731": TokenInfo(
        currency=CurrencyInfo(symbol="TME", name="TAMA EGG NiftyGotchi"), scaling=Decimal("1e-18")
    ),
    "0x6e9730ecffbed43fd876a264c982e254ef05a0de": TokenInfo(
        currency=CurrencyInfo(symbol="NORD", name="Nord Finance"), scaling=Decimal("1e-18")
    ),
    "0x6ebccea09f6bb1a0dc550dcd66f15a7cb170ede1": TokenInfo(
        currency=CurrencyInfo(symbol="CRDR", name="CryptoDream Token"), scaling=Decimal("1e-18")
    ),
    "0x6ec47a178a9d50d4ec4683003d8324f19ca35382": TokenInfo(
        currency=CurrencyInfo(symbol="NDN", name="NDN Link"), scaling=Decimal("1e-18")
    ),
    "0x6ec8a24cabdc339a06a172f8223ea557055adaa5": TokenInfo(
        currency=CurrencyInfo(symbol="GNX", name="Genaro Network"), scaling=Decimal("1e-9")
    ),
    "0x6ee0f7bb50a54ab5253da0667b0dc2ee526c30a8": TokenInfo(
        currency=CurrencyInfo(symbol="ABUSD", name="Aave BUSD v1"), scaling=Decimal("1e-18")
    ),
    "0x6ef5febbd2a56fab23f18a69d3fb9f4e2a70440b": TokenInfo(
        currency=CurrencyInfo(symbol="ITR", name="Intercoin"), scaling=Decimal("1e-18")
    ),
    "0x6ef77d991eb5306e9f235abc0cc65925da398ad0": TokenInfo(
        currency=CurrencyInfo(symbol="MMT", name="Master MIX Token"), scaling=Decimal("1e-18")
    ),
    "0x6efc2e6c913ad5b7d91072bd1419b1f9d1080fc8": TokenInfo(
        currency=CurrencyInfo(symbol="GTF", name="GLOBALTRUSTFUND Token"), scaling=Decimal("1e-8")
    ),
    "0x6f02055e3541dd74a1abd8692116c22ffafadc5d": TokenInfo(
        currency=CurrencyInfo(symbol="TMT", name="The Mart Token"), scaling=Decimal("1e-18")
    ),
    "0x6f0b09bfa87410ab993291ec5f8cda81f1d2acd9": TokenInfo(
        currency=CurrencyInfo(symbol="PVG", name="Pilnette"), scaling=Decimal("1e-18")
    ),
    "0x6f0c544cfd52885cff69577f1b9fcc1c284e80ae": TokenInfo(
        currency=CurrencyInfo(symbol="F.CX", name="Ford Motor Co"), scaling=Decimal("1e-8")
    ),
    "0x6f0f17df020cb9f200c175883b24b4407d18c521": TokenInfo(
        currency=CurrencyInfo(symbol="ZTT", name="zTokens"), scaling=Decimal("1e-18")
    ),
    "0x6f259637dcd74c767781e37bc6133cd6a68aa161": TokenInfo(
        currency=CurrencyInfo(symbol="HT", name="Huobi Token"), scaling=Decimal("1e-18")
    ),
    "0x6f3009663470475f0749a6b76195375f95495fcb": TokenInfo(
        currency=CurrencyInfo(symbol="HATCH", name="Hatch DAO"), scaling=Decimal("1e-18")
    ),
    "0x6f39297bc0c386355c77da3a0275c867b21b2454": TokenInfo(
        currency=CurrencyInfo(symbol="FYY", name="GrandPa Fan"), scaling=Decimal("1e-8")
    ),
    "0x6f3bb1febc415183dec801d78b1f92eda200fe3e": TokenInfo(
        currency=CurrencyInfo(symbol="PUNT", name="Greenheart Punt"), scaling=Decimal("1e-18")
    ),
    "0x6f40d4a6237c257fff2db00fa0510deeecd303eb": TokenInfo(
        currency=CurrencyInfo(symbol="INST", name="INST"), scaling=Decimal("1e-18")
    ),
    "0x6f539a9456a5bcb6334a1a41207c3788f5825207": TokenInfo(
        currency=CurrencyInfo(symbol="OHNI", name="ohni_2"), scaling=Decimal("1e-18")
    ),
    "0x6f59e0461ae5e2799f1fb3847f05a63b16d0dbf8": TokenInfo(
        currency=CurrencyInfo(symbol="ORCA", name="ORCA Token"), scaling=Decimal("1e-18")
    ),
    "0x6f612996a752dc152cebef10c2e3e0649e49cdf4": TokenInfo(
        currency=CurrencyInfo(symbol="TWLO.CX", name="Twilio Cl A"), scaling=Decimal("1e-8")
    ),
    "0x6f6deb5db0c4994a8283a01d6cfeeb27fc3bbe9c": TokenInfo(
        currency=CurrencyInfo(symbol="PLAY", name="SmartBillions"), scaling=Decimal("1e-0")
    ),
    "0x6f80310ca7f2c654691d1383149fa1a57d8ab1f8": TokenInfo(
        currency=CurrencyInfo(symbol="SILO", name="Silo Finance"), scaling=Decimal("1e-18")
    ),
    "0x6f87d756daf0503d08eb8993686c7fc01dc44fb1": TokenInfo(
        currency=CurrencyInfo(symbol="TRADE", name="Unitrade"), scaling=Decimal("1e-18")
    ),
    "0x6f919d67967a97ea36195a2346d9244e60fe0ddb": TokenInfo(
        currency=CurrencyInfo(symbol="BLOC", name="Blockcloud"), scaling=Decimal("1e-18")
    ),
    "0x6f9cfda542db28ecdf3c18b5c40ed394d7adba47": TokenInfo(
        currency=CurrencyInfo(symbol="OKU", name="OKUBIT"), scaling=Decimal("1e-18")
    ),
    "0x6fa63f9b452a97d2df921378197570f9c04ea286": TokenInfo(
        currency=CurrencyInfo(symbol="HGS", name="Hawthorn Guardian System"), scaling=Decimal("1e-18")
    ),
    "0x6faa826af0568d1866fca570da79b318ef114dab": TokenInfo(
        currency=CurrencyInfo(symbol="B21", name="B21"), scaling=Decimal("1e-18")
    ),
    "0x6faff971d9248e7d398a98fdbe6a81f6d7489568": TokenInfo(
        currency=CurrencyInfo(symbol="TRYX", name="eToro Turkish Lira"), scaling=Decimal("1e-18")
    ),
    "0x6fb0855c404e09c47c3fbca25f08d4e41f9f062f": TokenInfo(
        currency=CurrencyInfo(symbol="AZRX", name="Aave ZRX v1"), scaling=Decimal("1e-18")
    ),
    "0x6fb3e0a217407efff7ca062d46c26e5d60a14d69": TokenInfo(
        currency=CurrencyInfo(symbol="IOTX", name="IoTeX Network"), scaling=Decimal("1e-18")
    ),
    "0x6fc13eace26590b80cccab1ba5d51890577d83b2": TokenInfo(
        currency=CurrencyInfo(symbol="UMB", name="Umbrella Network"), scaling=Decimal("1e-18")
    ),
    "0x6fcb6408499a7c0f242e32d77eb51ffa1dd28a7e": TokenInfo(
        currency=CurrencyInfo(symbol="XHDX", name="HydraDX"), scaling=Decimal("1e-12")
    ),
    "0x6fce4a401b6b80ace52baaefe4421bd188e76f6f": TokenInfo(
        currency=CurrencyInfo(symbol="AMANA", name="Aave MANA v1"), scaling=Decimal("1e-18")
    ),
    "0x6fd016ccc4611f7bab1dd3267334cb0216ef47f9": TokenInfo(
        currency=CurrencyInfo(
            symbol="REALTOKEN-8342-SCHAEFER-HWY-DETROIT-MI", name="RealToken 8342 Schaefer Hwy Detroit MI"
        ),
        scaling=Decimal("1e-18"),
    ),
    "0x6fe355c62c6faf6946ce888ffaba9fd12355ae27": TokenInfo(
        currency=CurrencyInfo(symbol="HBX", name="HashBX"), scaling=Decimal("1e-18")
    ),
    "0x6fe536a1d595c12cbb407c5b2c03999f658a5c72": TokenInfo(
        currency=CurrencyInfo(symbol="LG", name="LGame"), scaling=Decimal("1e-18")
    ),
    "0x6fe56c0bcdd471359019fcbc48863d6c3e9d4f41": TokenInfo(
        currency=CurrencyInfo(symbol="PROPS", name="Props Token"), scaling=Decimal("1e-18")
    ),
    "0x6febd6be8fa45be6a5eeb61a17c82d33b9addd41": TokenInfo(
        currency=CurrencyInfo(symbol="IDL", name="IDL Token"), scaling=Decimal("1e-18")
    ),
    "0x6febdfc0a9d9502c45343fce0df08828def44795": TokenInfo(
        currency=CurrencyInfo(symbol="BNBBEAR", name="3X Short BNB Token"), scaling=Decimal("1e-18")
    ),
    "0x6ff313fb38d53d7a458860b1bf7512f54a03e968": TokenInfo(
        currency=CurrencyInfo(symbol="MRO", name="Mero Currency"), scaling=Decimal("1e-18")
    ),
    "0x6ffbd6b41b802550c57d4661d81a1700a502f2ab": TokenInfo(
        currency=CurrencyInfo(symbol="PBLC", name="Politicoin"), scaling=Decimal("1e-9")
    ),
    "0x6fff3806bbac52a20e0d79bc538d527f6a22c96b": TokenInfo(
        currency=CurrencyInfo(symbol="CDX", name="CDX Network"), scaling=Decimal("1e-18")
    ),
    "0x701c244b988a513c945973defa05de933b23fe1d": TokenInfo(
        currency=CurrencyInfo(symbol="OAX", name="OAX"), scaling=Decimal("1e-18")
    ),
    "0x7025bab2ec90410de37f488d1298204cd4d6b29d": TokenInfo(
        currency=CurrencyInfo(symbol="XRA", name="Xriba"), scaling=Decimal("1e-18")
    ),
    "0x7031ab87dcc46818806ec07af46fa8c2ad2a2bfc": TokenInfo(
        currency=CurrencyInfo(symbol="TRBT", name="Tribute"), scaling=Decimal("1e-18")
    ),
    "0x70438034810b12798b1568b9d72792e073919a12": TokenInfo(
        currency=CurrencyInfo(symbol="ODC", name="Overseas Direct Certification"), scaling=Decimal("1e-18")
    ),
    "0x70460c3bb9abcc0aa51f922c00d37816d6ede4d7": TokenInfo(
        currency=CurrencyInfo(symbol="BBRA", name="BooBanker Research Association"), scaling=Decimal("1e-18")
    ),
    "0x705051bbfd9f287869a412cba8bc7d112de48e69": TokenInfo(
        currency=CurrencyInfo(symbol="SAKE", name="SAKECOIN"), scaling=Decimal("1e-8")
    ),
    "0x70508920986c120bc534f40450390bb1578b2637": TokenInfo(
        currency=CurrencyInfo(symbol="JADE", name="Jade Chain"), scaling=Decimal("1e-18")
    ),
    "0x7051620d11042c4335069aaa4f10cd3b4290c681": TokenInfo(
        currency=CurrencyInfo(symbol="TCASH", name="TCASH"), scaling=Decimal("1e-8")
    ),
    "0x705ee96c1c160842c92c1aecfcffccc9c412e3d9": TokenInfo(
        currency=CurrencyInfo(symbol="POLL", name="ClearPoll"), scaling=Decimal("1e-18")
    ),
    "0x706cb9e741cbfee00ad5b3f5acc8bd44d1644a74": TokenInfo(
        currency=CurrencyInfo(symbol="YFOX", name="YFOX Finance"), scaling=Decimal("1e-6")
    ),
    "0x70861e862e1ac0c96f853c8231826e469ead37b1": TokenInfo(
        currency=CurrencyInfo(symbol="DOS", name="DOS Network Token"), scaling=Decimal("1e-18")
    ),
    "0x70878b693a57a733a79560e33cf6a828e685d19a": TokenInfo(
        currency=CurrencyInfo(symbol="TRUMPLOSE", name="Trump Loses Token"), scaling=Decimal("1e-18")
    ),
    "0x708876f486e448ee89eb332bfbc8e593553058b9": TokenInfo(
        currency=CurrencyInfo(symbol="GAVEL", name="GavelCoin"), scaling=Decimal("1e-18")
    ),
    "0x708aa4e8aaeaad6074dd09cc4e5c52a70452eb39": TokenInfo(
        currency=CurrencyInfo(symbol="BFF", name="Bitcoffeen"), scaling=Decimal("1e-8")
    ),
    "0x7090a6e22c838469c9e67851d6489ba9c933a43f": TokenInfo(
        currency=CurrencyInfo(symbol="ZBUX", name="Zuck Bucks"), scaling=Decimal("1e-0")
    ),
    "0x70968feaf13299d0dbf78f66860bab9dbe3856bc": TokenInfo(
        currency=CurrencyInfo(symbol="TRN", name="Treelion"), scaling=Decimal("1e-18")
    ),
    "0x709e68ccea223a774f7144c1b04b71c8dad71138": TokenInfo(
        currency=CurrencyInfo(symbol="BA.CX", name="Boeing"), scaling=Decimal("1e-8")
    ),
    "0x70a63225bcadacc4430919f0c1a4f0f5fcffbaac": TokenInfo(
        currency=CurrencyInfo(symbol="VEY", name="VEY"), scaling=Decimal("1e-4")
    ),
    "0x70a6d0d1561ba98711e935a76b1c167c612978a2": TokenInfo(
        currency=CurrencyInfo(symbol="DFLY", name="Dragonfly Protocol"), scaling=Decimal("1e-9")
    ),
    "0x70a72833d6bf7f508c8224ce59ea1ef3d0ea3a38": TokenInfo(
        currency=CurrencyInfo(symbol="UTK", name="UTRUST Token"), scaling=Decimal("1e-18")
    ),
    "0x70b147e01e9285e7ce68b9ba437fe3a9190e756a": TokenInfo(
        currency=CurrencyInfo(symbol="FLX", name="BitFlux"), scaling=Decimal("1e-18")
    ),
    "0x70c621f949b6556c4545707a2d5d73a776b98359": TokenInfo(
        currency=CurrencyInfo(symbol="SKCH", name="Skychain"), scaling=Decimal("1e-6")
    ),
    "0x70d2b7c19352bb76e4409858ff5746e500f2b67c": TokenInfo(
        currency=CurrencyInfo(symbol="UPI", name="Pawtocol"), scaling=Decimal("1e-18")
    ),
    "0x70da48f4b7e83c386ef983d4cef4e58c2c09d8ac": TokenInfo(
        currency=CurrencyInfo(symbol="XQC", name="Quras Token"), scaling=Decimal("1e-8")
    ),
    "0x70debcdab2ef20be3d1dbff6a845e9ccb6e46930": TokenInfo(
        currency=CurrencyInfo(symbol="BIKI", name="BIKI"), scaling=Decimal("1e-8")
    ),
    "0x70e36f6bf80a52b3b46b3af8e106cc0ed743e8e4": TokenInfo(
        currency=CurrencyInfo(symbol="CCOMP", name="cCOMP"), scaling=Decimal("1e-8")
    ),
    "0x70e8de73ce538da2beed35d14187f6959a8eca96": TokenInfo(
        currency=CurrencyInfo(symbol="XSGD", name="XSGD"), scaling=Decimal("1e-6")
    ),
    "0x71010a9d003445ac60c4e6a7017c1e89a477b438": TokenInfo(
        currency=CurrencyInfo(symbol="AREP", name="Aave REP v1"), scaling=Decimal("1e-18")
    ),
    "0x7105ec15995a97496ec25de36cf7eec47b703375": TokenInfo(
        currency=CurrencyInfo(symbol="RBD", name="Red Box Dapp Token"), scaling=Decimal("1e-18")
    ),
    "0x71179af0e9d44a8299eb54c8c4eda226e8a93859": TokenInfo(
        currency=CurrencyInfo(symbol="TOCC", name="Texas Oil Crypto Currency"), scaling=Decimal("1e-8")
    ),
    "0x712db54daa836b53ef1ecbb9c6ba3b9efb073f40": TokenInfo(
        currency=CurrencyInfo(symbol="AENJ", name="Aave ENJ v1"), scaling=Decimal("1e-18")
    ),
    "0x71396a6410249725c5609646c4e449c6c4d41e27": TokenInfo(
        currency=CurrencyInfo(symbol="MVG", name="Max"), scaling=Decimal("1e-0")
    ),
    "0x714b1fded61090a6c49eb0b4d088b8e5ebd64e61": TokenInfo(
        currency=CurrencyInfo(symbol="TTM", name="To The Moon"), scaling=Decimal("1e-18")
    ),
    "0x716523231368d43bdfe1f06afe1c62930731ab13": TokenInfo(
        currency=CurrencyInfo(symbol="W0XETH", name="Wrapped 0xEthereum Token"), scaling=Decimal("1e-8")
    ),
    "0x71944c7953c93dbc0cd977e0ee1bbd9c2494b7b1": TokenInfo(
        currency=CurrencyInfo(symbol="KZE", name="Almeela"), scaling=Decimal("1e-8")
    ),
    "0x719ca90842a9f4d4fb52251db88703e4bc4a07ca": TokenInfo(
        currency=CurrencyInfo(symbol="DAIX", name="DAIX"), scaling=Decimal("1e-18")
    ),
    "0x71b4875fc519eea158855354916f2fdb73ef7081": TokenInfo(
        currency=CurrencyInfo(symbol="WATT.CX", name="Energous Corporation"), scaling=Decimal("1e-8")
    ),
    "0x71ba91dc68c6a206db0a6a92b4b1de3f9271432d": TokenInfo(
        currency=CurrencyInfo(symbol="wMBX", name="wMBX Token"), scaling=Decimal("1e-18")
    ),
    "0x71c25dd74a8bf4fb393cb06623aa43a5376d1431": TokenInfo(
        currency=CurrencyInfo(symbol="FTB", name="Feitebi"), scaling=Decimal("1e-18")
    ),
    "0x71d01db8d6a2fbea7f8d434599c237980c234e4c": TokenInfo(
        currency=CurrencyInfo(symbol="GLA", name="Gladius Token"), scaling=Decimal("1e-8")
    ),
    "0x71e5fb8793b5a2fb0c4918930180f8b36500cbb8": TokenInfo(
        currency=CurrencyInfo(symbol="ETR", name="Electric Token"), scaling=Decimal("1e-8")
    ),
    "0x71e8d74ff1c923e369d0e70dfb09866629c4dd35": TokenInfo(
        currency=CurrencyInfo(symbol="WRK", name="WorkCoin"), scaling=Decimal("1e-18")
    ),
    "0x71f7b56f9f8641f73ca71512a93857a7868d1443": TokenInfo(
        currency=CurrencyInfo(symbol="KMR", name="Kamera"), scaling=Decimal("1e-18")
    ),
    "0x71f85b2e46976bd21302b64329868fd15eb0d127": TokenInfo(
        currency=CurrencyInfo(symbol="AXN", name="Axion"), scaling=Decimal("1e-18")
    ),
    "0x71fc860f7d3a592a4a98740e39db31d25db65ae8": TokenInfo(
        currency=CurrencyInfo(symbol="AUSDT", name="Aave USDT v1"), scaling=Decimal("1e-6")
    ),
    "0x7206926ae9482dbdad19e112b1f2dd4f88dd7772": TokenInfo(
        currency=CurrencyInfo(symbol="JWN.CX", name="Nordstrom"), scaling=Decimal("1e-8")
    ),
    "0x72108a8cc3254813c6be2f1b77be53e185abfdd9": TokenInfo(
        currency=CurrencyInfo(symbol="ES", name="Era Swap Token"), scaling=Decimal("1e-18")
    ),
    "0x7220e92d418e2eb59d0c25d195fa004bfd3afc42": TokenInfo(
        currency=CurrencyInfo(symbol="ADF", name="Ad Flex Token"), scaling=Decimal("1e-18")
    ),
    "0x722f2f3eac7e9597c73a593f7cf3de33fbfc3308": TokenInfo(
        currency=CurrencyInfo(symbol="CNUS", name="CoinUs"), scaling=Decimal("1e-18")
    ),
    "0x72377f31e30a405282b522d588aebbea202b4f23": TokenInfo(
        currency=CurrencyInfo(symbol="VRN", name="Varen"), scaling=Decimal("1e-18")
    ),
    "0x723cbfc05e2cfcc71d3d89e770d32801a5eef5ab": TokenInfo(
        currency=CurrencyInfo(symbol="BTCP", name="Bitcoin Pro"), scaling=Decimal("1e-8")
    ),
    "0x7240ac91f01233baaf8b064248e80feaa5912ba3": TokenInfo(
        currency=CurrencyInfo(symbol="OCTO", name="OctoFi"), scaling=Decimal("1e-18")
    ),
    "0x72430a612adc007c50e3b6946dbb1bb0fd3101d1": TokenInfo(
        currency=CurrencyInfo(symbol="TIC", name="Thingschain"), scaling=Decimal("1e-8")
    ),
    "0x7252fdbb1097c7089d93b0fbdf3494aecf2c92a0": TokenInfo(
        currency=CurrencyInfo(symbol="VRX", name="VIRTEX TOKEN"), scaling=Decimal("1e-8")
    ),
    "0x725c263e32c72ddc3a19bea12c5a0479a81ee688": TokenInfo(
        currency=CurrencyInfo(symbol="BMI", name="Bridge Mutual"), scaling=Decimal("1e-18")
    ),
    "0x72630b1e3b42874bf335020ba0249e3e9e47bafc": TokenInfo(
        currency=CurrencyInfo(symbol="EPAN", name="Paypolitan Token"), scaling=Decimal("1e-18")
    ),
    "0x727f064a78dc734d33eec18d5370aef32ffd46e4": TokenInfo(
        currency=CurrencyInfo(symbol="ORION", name="Orion Money"), scaling=Decimal("1e-18")
    ),
    "0x728781e75735dc0962df3a51d7ef47e798a7107e": TokenInfo(
        currency=CurrencyInfo(symbol="WOLK", name="Wolk Protocol Token"), scaling=Decimal("1e-18")
    ),
    "0x728c2ba981f67677bd66e11ce389fb5fd0f33e95": TokenInfo(
        currency=CurrencyInfo(symbol="SIG.CX", name="Signet Jewelers"), scaling=Decimal("1e-8")
    ),
    "0x728f30fa2f100742c7949d1961804fa8e0b1387d": TokenInfo(
        currency=CurrencyInfo(symbol="GHX", name="GHX"), scaling=Decimal("1e-18")
    ),
    "0x72955ecff76e48f2c8abcce11d54e5734d6f3657": TokenInfo(
        currency=CurrencyInfo(symbol="TRV", name="TrustVerse"), scaling=Decimal("1e-18")
    ),
    "0x7297862b9670ff015192799cc849726c88bf1d77": TokenInfo(
        currency=CurrencyInfo(symbol="SKYM", name="SkyMap"), scaling=Decimal("1e-18")
    ),
    "0x72a6344185b383035d6665c3f44a9dfcc73873c8": TokenInfo(
        currency=CurrencyInfo(symbol="RNX", name="ROONEX"), scaling=Decimal("1e-18")
    ),
    "0x72adadb447784dd7ab1f472467750fc485e4cb2d": TokenInfo(
        currency=CurrencyInfo(symbol="WRC", name="Worldcore"), scaling=Decimal("1e-6")
    ),
    "0x72b886d09c117654ab7da13a14d603001de0b777": TokenInfo(
        currency=CurrencyInfo(symbol="XDEFI", name="XDEFI"), scaling=Decimal("1e-18")
    ),
    "0x72ba699f0f3c29d0f886c264ec7350533a32b3d5": TokenInfo(
        currency=CurrencyInfo(symbol="MCAN", name="Medican Coin"), scaling=Decimal("1e-8")
    ),
    "0x72ca0501427bb8f089c1c4f767cb17d017e803a9": TokenInfo(
        currency=CurrencyInfo(symbol="LIQ", name="Liquid DeFi"), scaling=Decimal("1e-18")
    ),
    "0x72d32ac1c5e66bfc5b08806271f8eef915545164": TokenInfo(
        currency=CurrencyInfo(symbol="KEE", name="CryptoKEE"), scaling=Decimal("1e-0")
    ),
    "0x72d530016e9e0fc23de6c1f7f487992c879518dc": TokenInfo(
        currency=CurrencyInfo(symbol="DEXT", name="Dex Delta Token"), scaling=Decimal("1e-1")
    ),
    "0x72dc3d52b7ef107a7cffb6953eaa8a2ad6a204cd": TokenInfo(
        currency=CurrencyInfo(symbol="SOUL", name="SOUL"), scaling=Decimal("1e-6")
    ),
    "0x72dd4b6bd852a3aa172be4d6c5a6dbec588cf131": TokenInfo(
        currency=CurrencyInfo(symbol="NGC", name="NAGA"), scaling=Decimal("1e-18")
    ),
    "0x72e203a17add19a3099137c9d7015fd3e2b7dba9": TokenInfo(
        currency=CurrencyInfo(symbol="BCP", name="BlockchainPoland"), scaling=Decimal("1e-18")
    ),
    "0x72e364f2abdc788b7e918bc238b21f109cd634d7": TokenInfo(
        currency=CurrencyInfo(symbol="MVI", name="Metaverse Index"), scaling=Decimal("1e-18")
    ),
    "0x72e5390edb7727e3d4e3436451dadaff675dbcc0": TokenInfo(
        currency=CurrencyInfo(symbol="HANU", name="Hanu Yokia"), scaling=Decimal("1e-12")
    ),
    "0x72ebd62060f78d91dc4bc33e8d88f39307365f87": TokenInfo(
        currency=CurrencyInfo(symbol="SEA", name="Second Exchange Alliance"), scaling=Decimal("1e-4")
    ),
    "0x72f020f8f3e8fd9382705723cd26380f8d0c66bb": TokenInfo(
        currency=CurrencyInfo(symbol="PLOT", name="PlotX"), scaling=Decimal("1e-18")
    ),
    "0x73104e9d3da91e410a6c211068f7bffabbbd3e26": TokenInfo(
        currency=CurrencyInfo(symbol="ETHMOONX", name="ETH Moonshot X Set"), scaling=Decimal("1e-18")
    ),
    "0x7350383f6367de8b2e042209ad1ae7e66c863a2c": TokenInfo(
        currency=CurrencyInfo(symbol="DOOMSHIT", name="10X Short Shitcoin Index Token"), scaling=Decimal("1e-18")
    ),
    "0x73621534d00d80f675b7e868860f97edb3c03935": TokenInfo(
        currency=CurrencyInfo(symbol="BBA", name="BBA Token"), scaling=Decimal("1e-18")
    ),
    "0x7367a68039d4704f30bfbf6d948020c3b07dfc59": TokenInfo(
        currency=CurrencyInfo(symbol="🍺", name="Beercoin"), scaling=Decimal("1e-18")
    ),
    "0x737f98ac8ca59f2c68ad658e3c3d8c8963e40a4c": TokenInfo(
        currency=CurrencyInfo(symbol="AMN", name="Amon"), scaling=Decimal("1e-18")
    ),
    "0x737fa0372c8d001904ae6acaf0552d4015f9c947": TokenInfo(
        currency=CurrencyInfo(symbol="MEDIBIT", name="MEDIBIT"), scaling=Decimal("1e-18")
    ),
    "0x73968b9a57c6e53d41345fd57a6e6ae27d6cdb2f": TokenInfo(
        currency=CurrencyInfo(symbol="SDT", name="Stake DAO"), scaling=Decimal("1e-18")
    ),
    "0x73a052500105205d34daf004eab301916da8190f": TokenInfo(
        currency=CurrencyInfo(symbol="YTUSD", name="yTUSD"), scaling=Decimal("1e-18")
    ),
    "0x73a9fb46e228628f8f9bb9004eca4f4f529d3998": TokenInfo(
        currency=CurrencyInfo(symbol="WLEO", name="Wrapped LEO"), scaling=Decimal("1e-3")
    ),
    "0x73b534fb6f07381a29a60b01eed5ae57d4ee24d7": TokenInfo(
        currency=CurrencyInfo(symbol="SDRN", name="Senderon"), scaling=Decimal("1e-18")
    ),
    "0x73c9275c3a2dd84b5741fd59aebf102c91eb033f": TokenInfo(
        currency=CurrencyInfo(symbol="BTRS", name="Bitball Treasure"), scaling=Decimal("1e-18")
    ),
    "0x73cee8348b9bdd48c64e13452b8a6fbc81630573": TokenInfo(
        currency=CurrencyInfo(symbol="EGR", name="EGORAS"), scaling=Decimal("1e-18")
    ),
    "0x73dd069c299a5d691e9836243bcaec9c8c1d8734": TokenInfo(
        currency=CurrencyInfo(symbol="BTE", name="Bitcoineum"), scaling=Decimal("1e-8")
    ),
    "0x73ee6d7e6b203125add89320e9f343d65ec7c39a": TokenInfo(
        currency=CurrencyInfo(symbol="AXI", name="Axioms"), scaling=Decimal("1e-18")
    ),
    "0x740623d2c797b7d8d1ecb98e9b4afcf99ec31e14": TokenInfo(
        currency=CurrencyInfo(symbol="DYT", name="DoYourTip"), scaling=Decimal("1e-18")
    ),
    "0x7420b4b9a0110cdc71fb720908340c03f9bc03ec": TokenInfo(
        currency=CurrencyInfo(symbol="JASMY", name="JasmyCoin"), scaling=Decimal("1e-18")
    ),
    "0x74232704659ef37c08995e386a2e26cc27a8d7b1": TokenInfo(
        currency=CurrencyInfo(symbol="STRK", name="Strike"), scaling=Decimal("1e-18")
    ),
    "0x743bba828949fce4557bad9a52db488ce6fdff8d": TokenInfo(
        currency=CurrencyInfo(symbol="ZHSH", name="ZHSH Chain"), scaling=Decimal("1e-4")
    ),
    "0x743c79f88dcadc6e7cfd7fa2bd8e2bfc68dae053": TokenInfo(
        currency=CurrencyInfo(symbol="JPYX", name="eToro Japanese Yen"), scaling=Decimal("1e-18")
    ),
    "0x744d70fdbe2ba4cf95131626614a1763df805b9e": TokenInfo(
        currency=CurrencyInfo(symbol="SNT", name="Status"), scaling=Decimal("1e-18")
    ),
    "0x7458fd786b2fe8cd801c0381f88b61c5071a006f": TokenInfo(
        currency=CurrencyInfo(symbol="LOA", name="LOA Protocol"), scaling=Decimal("1e-18")
    ),
    "0x74603e780545d02c4257e7d2be19c74de7be1952": TokenInfo(
        currency=CurrencyInfo(symbol="ETGF", name="ETG Finance"), scaling=Decimal("1e-18")
    ),
    "0x7461c43bb1e96863233d72a09191008ee9217ee8": TokenInfo(
        currency=CurrencyInfo(symbol="DGN", name="Degen Platform"), scaling=Decimal("1e-18")
    ),
    "0x746dda2ea243400d5a63e0700f190ab79f06489e": TokenInfo(
        currency=CurrencyInfo(symbol="BOA", name="BOSAGORA"), scaling=Decimal("1e-7")
    ),
    "0x74951b677de32d596ee851a233336926e6a2cd09": TokenInfo(
        currency=CurrencyInfo(symbol="WBA", name="We Bet Crypto"), scaling=Decimal("1e-7")
    ),
    "0x749826f1041caf0ea856a4b3578ba327b18335f8": TokenInfo(
        currency=CurrencyInfo(symbol="TIG", name="TIG Token"), scaling=Decimal("1e-18")
    ),
    "0x74c1e4b8cae59269ec1d85d3d4f324396048f4ac": TokenInfo(
        currency=CurrencyInfo(symbol="BeerCoin", name="BeerCoin"), scaling=Decimal("1e-0")
    ),
    "0x74ce17209d3a7cd057beb1ce1bab705e17b164f7": TokenInfo(
        currency=CurrencyInfo(symbol="NP5", name="New Pay Five"), scaling=Decimal("1e-18")
    ),
    "0x74ceda77281b339142a36817fa5f9e29412bab85": TokenInfo(
        currency=CurrencyInfo(symbol="ERO", name="Eroscoin"), scaling=Decimal("1e-8")
    ),
    "0x74d2cb65b1158300c3e6bea149d68509c7b2425d": TokenInfo(
        currency=CurrencyInfo(
            symbol="REALTOKEN-25097-ANDOVER-DR-DEARBORN-MI", name="RealToken 25097 Andover Dr Dearborn MI"
        ),
        scaling=Decimal("1e-18"),
    ),
    "0x74faab6986560fd1140508e4266d8a7b87274ffd": TokenInfo(
        currency=CurrencyInfo(symbol="HDAO", name="HyperDAO"), scaling=Decimal("1e-18")
    ),
    "0x74fd51a98a4a1ecbef8cc43be801cce630e260bd": TokenInfo(
        currency=CurrencyInfo(symbol="SCC", name="SiaCashCoin"), scaling=Decimal("1e-18")
    ),
    "0x7510d6fac98a6eca2db7c9357619715a7f5049d4": TokenInfo(
        currency=CurrencyInfo(symbol="TCAPBTCUSDC", name="Holistic BTC Set"), scaling=Decimal("1e-18")
    ),
    "0x75231f58b43240c9718dd58b4967c5114342a86c": TokenInfo(
        currency=CurrencyInfo(symbol="OKB", name="OKB"), scaling=Decimal("1e-18")
    ),
    "0x7528e3040376edd5db8263db2f5bd1bed91467fb": TokenInfo(
        currency=CurrencyInfo(symbol="SIM", name="Simmitri"), scaling=Decimal("1e-18")
    ),
    "0x752ff65b884b9c260d212c804e0b7aceea012473": TokenInfo(
        currency=CurrencyInfo(symbol="SNPC", name="SnapCoin"), scaling=Decimal("1e-18")
    ),
    "0x7533d63a2558965472398ef473908e1320520ae2": TokenInfo(
        currency=CurrencyInfo(symbol="INTX", name="INTEXCOIN"), scaling=Decimal("1e-9")
    ),
    "0x75387e1287dd85482ab66102da9f6577e027f609": TokenInfo(
        currency=CurrencyInfo(symbol="MAI", name="MindsyncAI"), scaling=Decimal("1e-18")
    ),
    "0x75572098dc462f976127f59f8c97dfa291f81d8b": TokenInfo(
        currency=CurrencyInfo(symbol="VETH", name="Vether"), scaling=Decimal("1e-18")
    ),
    "0x755eb14d2feff2939eb3026f5cad9d03775b9ff4": TokenInfo(
        currency=CurrencyInfo(symbol="BUNNY", name="BunnyToken"), scaling=Decimal("1e-18")
    ),
    "0x7574c09a26e781df694755cec8ac04af9d1e1cc0": TokenInfo(
        currency=CurrencyInfo(symbol="ALTMOON", name="10X Long Altcoin Index Token"), scaling=Decimal("1e-18")
    ),
    "0x757703bd5b2c4bbcfde0be2c0b0e7c2f31fcf4e9": TokenInfo(
        currency=CurrencyInfo(symbol="ZEST", name="Zest Token"), scaling=Decimal("1e-18")
    ),
    "0x757de3ac6b830a931ef178c6634c5c551773155c": TokenInfo(
        currency=CurrencyInfo(symbol="sNIKKEI", name="Synth sNIKKEI"), scaling=Decimal("1e-18")
    ),
    "0x7585f835ae2d522722d2684323a0ba83401f32f5": TokenInfo(
        currency=CurrencyInfo(symbol="GBT", name="HelloGold Gold Backed Token"), scaling=Decimal("1e-18")
    ),
    "0x758b4684be769e92eefea93f60dda0181ea303ec": TokenInfo(
        currency=CurrencyInfo(symbol="PHONON", name="Phonon DAO"), scaling=Decimal("1e-18")
    ),
    "0x75aa7b0d02532f3833b66c7f0ad35376d373ddf8": TokenInfo(
        currency=CurrencyInfo(symbol="ARD", name="Accord"), scaling=Decimal("1e-18")
    ),
    "0x75b5f145002ba88cdfdb7897e0550781e3909a08": TokenInfo(
        currency=CurrencyInfo(symbol="WES", name="World Electronic Sports coin"), scaling=Decimal("1e-18")
    ),
    "0x75c5ee419331b6150879530d06f9ba054755f1da": TokenInfo(
        currency=CurrencyInfo(symbol="SAL", name="SalPay"), scaling=Decimal("1e-18")
    ),
    "0x75f0038b8fbfccafe2ab9a51431658871ba5182c": TokenInfo(
        currency=CurrencyInfo(symbol="ATOMBULL", name="3X Long Cosmos Token"), scaling=Decimal("1e-18")
    ),
    "0x7611674336151835403c4db867fdd30782073c65": TokenInfo(
        currency=CurrencyInfo(symbol="UNIS", name="UniSlurm"), scaling=Decimal("1e-18")
    ),
    "0x761c9dde671191df36ec5fc374bcf21394879737": TokenInfo(
        currency=CurrencyInfo(symbol="FDX.CX", name="Fedex"), scaling=Decimal("1e-8")
    ),
    "0x761d38e5ddf6ccf6cf7c55759d5210750b5d60f3": TokenInfo(
        currency=CurrencyInfo(symbol="ELON", name="Dogelon Mars"), scaling=Decimal("1e-18")
    ),
    "0x7627de4b93263a6a7570b8dafa64bae812e5c394": TokenInfo(
        currency=CurrencyInfo(symbol="NXX", name="Nexxus"), scaling=Decimal("1e-8")
    ),
    "0x76306f029f8f99effe509534037ba7030999e3cf": TokenInfo(
        currency=CurrencyInfo(symbol="ACR", name="Acreage Coin"), scaling=Decimal("1e-18")
    ),
    "0x763186eb8d4856d536ed4478302971214febc6a9": TokenInfo(
        currency=CurrencyInfo(symbol="BETR", name="BetterBetting"), scaling=Decimal("1e-18")
    ),
    "0x763fa6806e1acf68130d2d0f0df754c93cc546b2": TokenInfo(
        currency=CurrencyInfo(symbol="LIT", name="Lition"), scaling=Decimal("1e-18")
    ),
    "0x7654915a1b82d6d2d0afc37c52af556ea8983c7e": TokenInfo(
        currency=CurrencyInfo(symbol="IFT", name="InvestFeed"), scaling=Decimal("1e-18")
    ),
    "0x7659ce147d0e714454073a5dd7003544234b6aa0": TokenInfo(
        currency=CurrencyInfo(symbol="XCAD", name="XCAD Network"), scaling=Decimal("1e-18")
    ),
    "0x765f0c16d1ddc279295c1a7c24b0883f62d33f75": TokenInfo(
        currency=CurrencyInfo(symbol="DTX", name="DaTa eXchange Token"), scaling=Decimal("1e-18")
    ),
    "0x7671904eed7f10808b664fc30bb8693fd7237abf": TokenInfo(
        currency=CurrencyInfo(symbol="BBR", name="Bitberry Token"), scaling=Decimal("1e-18")
    ),
    "0x767588059265d2a243445dd3f23db37b96018dd5": TokenInfo(
        currency=CurrencyInfo(symbol="PMC", name="Primebank Coin"), scaling=Decimal("1e-8")
    ),
    "0x767ba2915ec344015a7938e3eedfec2785195d05": TokenInfo(
        currency=CurrencyInfo(symbol="REA", name="Realisto Token"), scaling=Decimal("1e-18")
    ),
    "0x767fe9edc9e0df98e07454847909b5e959d7ca0e": TokenInfo(
        currency=CurrencyInfo(symbol="ILV", name="Illuvium"), scaling=Decimal("1e-18")
    ),
    "0x768386990688b293226b9f83465974003b5e40d7": TokenInfo(
        currency=CurrencyInfo(symbol="NRV", name="NRV Coin"), scaling=Decimal("1e-18")
    ),
    "0x76960dccd5a1fe799f7c29be9f19ceb4627aeb2f": TokenInfo(
        currency=CurrencyInfo(symbol="RED", name="Red"), scaling=Decimal("1e-18")
    ),
    "0x76974c7b79dc8a6a109fd71fd7ceb9e40eff5382": TokenInfo(
        currency=CurrencyInfo(symbol="DOW", name="Dowcoin"), scaling=Decimal("1e-18")
    ),
    "0x76a435b51baeae457324406da02ee7e3473288b5": TokenInfo(
        currency=CurrencyInfo(symbol="XTRLPAY", name="XTRLPAY"), scaling=Decimal("1e-8")
    ),
    "0x770192738485d4794f4222e49501f31e85814cec": TokenInfo(
        currency=CurrencyInfo(symbol="OEX", name="OEX"), scaling=Decimal("1e-18")
    ),
    "0x7703c35cffdc5cda8d27aa3df2f9ba6964544b6e": TokenInfo(
        currency=CurrencyInfo(symbol="PYLNT", name="Pylon Token"), scaling=Decimal("1e-18")
    ),
    "0x7705c572d9cc824fba4e4efb40f00916534396d9": TokenInfo(
        currency=CurrencyInfo(symbol="KSWAP", name="KimchiSwap"), scaling=Decimal("1e-18")
    ),
    "0x7705faa34b16eb6d77dfc7812be2367ba6b0248e": TokenInfo(
        currency=CurrencyInfo(symbol="ARX", name="Artex Token"), scaling=Decimal("1e-8")
    ),
    "0x7728dfef5abd468669eb7f9b48a7f70a501ed29d": TokenInfo(
        currency=CurrencyInfo(symbol="PRG", name="Paragon"), scaling=Decimal("1e-6")
    ),
    "0x773258b03c730f84af10dfcb1bfaa7487558b8ac": TokenInfo(
        currency=CurrencyInfo(symbol="SEFI", name="Secret Finance"), scaling=Decimal("1e-6")
    ),
    "0x773450335ed4ec3db45af74f34f2c85348645d39": TokenInfo(
        currency=CurrencyInfo(symbol="JET", name="JetCoins"), scaling=Decimal("1e-18")
    ),
    "0x77599d2c6db170224243e255e6669280f11f1473": TokenInfo(
        currency=CurrencyInfo(symbol="OPQ", name="Opacity"), scaling=Decimal("1e-18")
    ),
    "0x77607588222e01bf892a29abab45796a2047fc7b": TokenInfo(
        currency=CurrencyInfo(symbol="UETH", name="Unagii ETH"), scaling=Decimal("1e-18")
    ),
    "0x77761e63c05aee6648fdaeaa9b94248351af9bcd": TokenInfo(
        currency=CurrencyInfo(symbol="PASS", name="WisePass"), scaling=Decimal("1e-18")
    ),
    "0x7777770f8a6632ff043c8833310e245eba9209e6": TokenInfo(
        currency=CurrencyInfo(symbol="TOB", name="Tokens of Babel"), scaling=Decimal("1e-18")
    ),
    "0x77777777772cf0455fb38ee0e75f38034dfa50de": TokenInfo(
        currency=CurrencyInfo(symbol="XY", name="XY Finance"), scaling=Decimal("1e-18")
    ),
    "0x7777777777697cfeecf846a76326da79cc606517": TokenInfo(
        currency=CurrencyInfo(symbol="SIG", name="xSigma"), scaling=Decimal("1e-18")
    ),
    "0x77777feddddffc19ff86db637967013e6c6a116c": TokenInfo(
        currency=CurrencyInfo(symbol="TORN", name="Tornado Cash"), scaling=Decimal("1e-18")
    ),
    "0x7778360f035c589fce2f4ea5786cbd8b36e5396b": TokenInfo(
        currency=CurrencyInfo(symbol="OOE", name="OpenOcean"), scaling=Decimal("1e-18")
    ),
    "0x7788d759f21f53533051a9ae657fa05a1e068fc6": TokenInfo(
        currency=CurrencyInfo(symbol="FLETA", name="Fleta Token"), scaling=Decimal("1e-18")
    ),
    "0x779492d3644ddf4495aa2d80c468e1b7be6af1d2": TokenInfo(
        currency=CurrencyInfo(symbol="CAS", name="CAS Coin"), scaling=Decimal("1e-2")
    ),
    "0x779b7b713c86e3e6774f5040d9ccc2d43ad375f8": TokenInfo(
        currency=CurrencyInfo(symbol="POOL", name="StakePool"), scaling=Decimal("1e-8")
    ),
    "0x77b1465b0e01ba085e515324e30fee6555c623ea": TokenInfo(
        currency=CurrencyInfo(symbol="MQSS", name="Set of Sets Trailblazer Fund"), scaling=Decimal("1e-18")
    ),
    "0x77c07555af5ffdc946fb47ce15ea68620e4e7170": TokenInfo(
        currency=CurrencyInfo(symbol="BRZE", name="Breezecoin"), scaling=Decimal("1e-18")
    ),
    "0x77c6e4a580c0dce4e5c7a17d0bc077188a83a059": TokenInfo(
        currency=CurrencyInfo(symbol="SWUSD", name="Swerve.fi USD"), scaling=Decimal("1e-18")
    ),
    "0x77dba24943f348d9c3ce4d9df0675caa7bb550bf": TokenInfo(
        currency=CurrencyInfo(symbol="MAC", name="MagicNeWorld"), scaling=Decimal("1e-6")
    ),
    "0x77edd08fa155bce573a6a8c015db188152584572": TokenInfo(
        currency=CurrencyInfo(symbol="BSTC", name="BUSINESS TICKER COIN"), scaling=Decimal("1e-10")
    ),
    "0x77f06890793deed1338d995bfc36bd8ea2ce6b9a": TokenInfo(
        currency=CurrencyInfo(symbol="PBT", name="Prince Broadcast Token"), scaling=Decimal("1e-18")
    ),
    "0x77f973fcaf871459aa58cd81881ce453759281bc": TokenInfo(
        currency=CurrencyInfo(symbol="iETH", name="Fulcrum ETH iToken"), scaling=Decimal("1e-18")
    ),
    "0x77fba179c79de5b7653f68b5039af940ada60ce0": TokenInfo(
        currency=CurrencyInfo(symbol="FORTH", name="Ampleforth Governance Token"), scaling=Decimal("1e-18")
    ),
    "0x780116d91e5592e58a3b3c76a351571b39abcec6": TokenInfo(
        currency=CurrencyInfo(symbol="BOXX", name="Blockparty"), scaling=Decimal("1e-15")
    ),
    "0x7815bda662050d84718b988735218cffd32f75ea": TokenInfo(
        currency=CurrencyInfo(symbol="YEL", name="Yel Finance"), scaling=Decimal("1e-18")
    ),
    "0x78175901e9b04090bf3b3d3cb7f91ca986fb1af6": TokenInfo(
        currency=CurrencyInfo(symbol="ZOMB", name="Antique Zombie Shards"), scaling=Decimal("1e-18")
    ),
    "0x7825e833d495f3d1c28872415a4aee339d26ac88": TokenInfo(
        currency=CurrencyInfo(symbol="TLOS", name="Telos"), scaling=Decimal("1e-18")
    ),
    "0x783ba0062326861ee76e0e15429594922e9fe2f5": TokenInfo(
        currency=CurrencyInfo(symbol="AVVP", name="Andrey Voronkov Ventures Promo"), scaling=Decimal("1e-18")
    ),
    "0x7841b2a48d1f6e78acec359fed6d874eb8a0f63c": TokenInfo(
        currency=CurrencyInfo(symbol="KERMAN", name="KERMAN"), scaling=Decimal("1e-4")
    ),
    "0x78481fb80caabb252909218164266ac83f815000": TokenInfo(
        currency=CurrencyInfo(symbol="EHY", name="Ethereum High Yield Set"), scaling=Decimal("1e-18")
    ),
    "0x785585878feb8cf7cd1e3b9eca0635464c2dd0cb": TokenInfo(
        currency=CurrencyInfo(symbol="MCT", name="Miner Calculation Token"), scaling=Decimal("1e-18")
    ),
    "0x78571accaf24052795f98b11f093b488a2d9eaa4": TokenInfo(
        currency=CurrencyInfo(symbol="RCKT", name="Rocket Token"), scaling=Decimal("1e-18")
    ),
    "0x786001c9c5ca6e502deb8a8a72480d2147891f32": TokenInfo(
        currency=CurrencyInfo(symbol="BEPRO", name="BetProtocolToken"), scaling=Decimal("1e-18")
    ),
    "0x7865af71cf0b288b4e7f654f4f7851eb46a2b7f8": TokenInfo(
        currency=CurrencyInfo(symbol="SNTVT", name="Sentivate"), scaling=Decimal("1e-18")
    ),
    "0x7866e48c74cbfb8183cd1a929cd9b95a7a5cb4f4": TokenInfo(
        currency=CurrencyInfo(symbol="KIT", name="DexKit"), scaling=Decimal("1e-18")
    ),
    "0x7869c4a1a3f6f8684fbcc422a21ad7abe3167834": TokenInfo(
        currency=CurrencyInfo(symbol="PVT", name="Pivot Token"), scaling=Decimal("1e-18")
    ),
    "0x78751b12da02728f467a44eac40f5cbc16bd7934": TokenInfo(
        currency=CurrencyInfo(symbol="idleDAIYield", name="IdleDAI v3 [Max yield]"), scaling=Decimal("1e-18")
    ),
    "0x7875bafc5d63fa035dea0809c2a57a382d772903": TokenInfo(
        currency=CurrencyInfo(symbol="CRYPTO", name="BIZpaye"), scaling=Decimal("1e-18")
    ),
    "0x7878424e994d8a2b8e329d31096922b7ceabe660": TokenInfo(
        currency=CurrencyInfo(symbol="IMVR", name="ImmVRse"), scaling=Decimal("1e-18")
    ),
    "0x7884f51dc1410387371ce61747cb6264e1daee0b": TokenInfo(
        currency=CurrencyInfo(symbol="BDOT", name="Binance Wrapped DOT"), scaling=Decimal("1e-10")
    ),
    "0x78a2a1029e3168b49d3a276c787050ff5106dcf2": TokenInfo(
        currency=CurrencyInfo(symbol="EZW", name="EZOOW"), scaling=Decimal("1e-18")
    ),
    "0x78a52e12c7b63d05c12f9608307587cf654ec3d0": TokenInfo(
        currency=CurrencyInfo(symbol="CVA", name="Crypto Village Accelerator"), scaling=Decimal("1e-18")
    ),
    "0x78a5b382b9a83fe042a4f7eb2399d563fda931c3": TokenInfo(
        currency=CurrencyInfo(symbol="HZT", name="Black Diamond Rating"), scaling=Decimal("1e-2")
    ),
    "0x78a73b6cbc5d183ce56e786f6e905cadec63547b": TokenInfo(
        currency=CurrencyInfo(symbol="FT", name="Fabric Token"), scaling=Decimal("1e-18")
    ),
    "0x78b039921e84e726eb72e7b1212bb35504c645ca": TokenInfo(
        currency=CurrencyInfo(symbol="SETH", name="Sether"), scaling=Decimal("1e-18")
    ),
    "0x78b7fada55a64dd895d8c8c35779dd8b67fa8a05": TokenInfo(
        currency=CurrencyInfo(symbol="ATL", name="Atlant"), scaling=Decimal("1e-18")
    ),
    "0x78c292d1445e6b9558bf42e8bc369271ded062ea": TokenInfo(
        currency=CurrencyInfo(symbol="CYMT", name="CyberMusic"), scaling=Decimal("1e-8")
    ),
    "0x78e29d35573bea6265aedfcb9f45481b717ebfde": TokenInfo(
        currency=CurrencyInfo(symbol="LINKPT", name="LINK Profit Taker Set"), scaling=Decimal("1e-18")
    ),
    "0x78eb8dc641077f049f910659b6d580e80dc4d237": TokenInfo(
        currency=CurrencyInfo(symbol="SMT", name="Social Media Market"), scaling=Decimal("1e-8")
    ),
    "0x78f225869c08d478c34e5f645d07a87d3fe8eb78": TokenInfo(
        currency=CurrencyInfo(symbol="DEFI+L", name="PieDAO DEFI Large Cap"), scaling=Decimal("1e-18")
    ),
    "0x78f5bbc74fb9137a75d85f3c9c3c599be49f0a56": TokenInfo(
        currency=CurrencyInfo(symbol="SMARTUP", name="Smartup"), scaling=Decimal("1e-18")
    ),
    "0x78fe18e41f436e1981a3a60d1557c8a7a9370461": TokenInfo(
        currency=CurrencyInfo(symbol="SWC", name="Scandiweb Coin"), scaling=Decimal("1e-2")
    ),
    "0x79126d32a86e6663f3aaac4527732d0701c1ae6c": TokenInfo(
        currency=CurrencyInfo(symbol="DMT", name="Dark Matter"), scaling=Decimal("1e-18")
    ),
    "0x791425156956e39f2ab8ab06b79de189c18e95e5": TokenInfo(
        currency=CurrencyInfo(symbol="IBT", name="ICOBay Token"), scaling=Decimal("1e-18")
    ),
    "0x7928c8abf1f74ef9f96d4d0a44e3b4209d360785": TokenInfo(
        currency=CurrencyInfo(symbol="SLY", name="SELFLLERY token"), scaling=Decimal("1e-18")
    ),
    "0x792e0fc822ac6ff5531e46425f13540f1f68a7a8": TokenInfo(
        currency=CurrencyInfo(symbol="CHT", name="CoinHot"), scaling=Decimal("1e-8")
    ),
    "0x793786e2dd4cc492ed366a94b88a3ff9ba5e7546": TokenInfo(
        currency=CurrencyInfo(symbol="AXIAV3", name="Axia"), scaling=Decimal("1e-18")
    ),
    "0x7939882b54fcf0bcae6b53dec39ad6e806176442": TokenInfo(
        currency=CurrencyInfo(symbol="MKT", name="Mikado Token"), scaling=Decimal("1e-8")
    ),
    "0x793e2602a8396468f3ce6e34c1b6c6fd6d985bad": TokenInfo(
        currency=CurrencyInfo(symbol="ICK", name="$ICK Mask"), scaling=Decimal("1e-18")
    ),
    "0x794d1d86685d45f9297c2fe80f295aa7f8285bb4": TokenInfo(
        currency=CurrencyInfo(symbol="PALS", name="PALS"), scaling=Decimal("1e-18")
    ),
    "0x79650799e7899a802cb96c0bc33a6a8d4ce4936c": TokenInfo(
        currency=CurrencyInfo(symbol="AIT", name="AICHAIN"), scaling=Decimal("1e-18")
    ),
    "0x7968bc6a03017ea2de509aaa816f163db0f35148": TokenInfo(
        currency=CurrencyInfo(symbol="HGET", name="Hedget"), scaling=Decimal("1e-6")
    ),
    "0x796e47b85a0d759f300f1de96a3583004235d4d8": TokenInfo(
        currency=CurrencyInfo(symbol="ELD", name="Electrum Dark"), scaling=Decimal("1e-18")
    ),
    "0x797de1dc0b9faf5e25c1f7efe8df9599138fa09d": TokenInfo(
        currency=CurrencyInfo(symbol="GPOOL", name="Genesis Pool"), scaling=Decimal("1e-18")
    ),
    "0x798a9055a98913835bbfb45a0bbc209438dcfd97": TokenInfo(
        currency=CurrencyInfo(symbol="NYB", name="New Year Bull"), scaling=Decimal("1e-18")
    ),
    "0x798b5c3d3a56b6e55c1b44a8368746f9a11e4d7d": TokenInfo(
        currency=CurrencyInfo(symbol="TCLB", name="TCLB"), scaling=Decimal("1e-18")
    ),
    "0x798d1be841a82a273720ce31c822c61a67a601c3": TokenInfo(
        currency=CurrencyInfo(symbol="DIGG", name="DIGG"), scaling=Decimal("1e-9")
    ),
    "0x7995ab36bb307afa6a683c24a25d90dc1ea83566": TokenInfo(
        currency=CurrencyInfo(symbol="HIT", name="HitChain"), scaling=Decimal("1e-6")
    ),
    "0x799d214d7143b766cdd4979cd0280939288ba931": TokenInfo(
        currency=CurrencyInfo(symbol="CHT", name="Countinghouse Fund"), scaling=Decimal("1e-2")
    ),
    "0x79be75ffc64dd58e66787e4eae470c8a1fd08ba4": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMDAI", name="Aave AMM DAI"), scaling=Decimal("1e-18")
    ),
    "0x79bfd2670b6bb2219d30a6fd0dbf287f2b66633d": TokenInfo(
        currency=CurrencyInfo(symbol="ICN", name="IC-Node"), scaling=Decimal("1e-8")
    ),
    "0x79c5a1ae586322a07bfb60be36e1b31ce8c84a1e": TokenInfo(
        currency=CurrencyInfo(symbol="EDI", name="Freight Trust Network"), scaling=Decimal("1e-18")
    ),
    "0x79c71d3436f39ce382d0f58f1b011d88100b9d91": TokenInfo(
        currency=CurrencyInfo(symbol="XNS", name="Xeonbit Token"), scaling=Decimal("1e-18")
    ),
    "0x79c75e2e8720b39e258f41c37cc4f309e0b0ff80": TokenInfo(
        currency=CurrencyInfo(symbol="SOUL", name="Phantasma"), scaling=Decimal("1e-8")
    ),
    "0x79cdfa04e3c4eb58c4f49dae78b322e5b0d38788": TokenInfo(
        currency=CurrencyInfo(symbol="TFB", name="Truefeedback Token"), scaling=Decimal("1e-18")
    ),
    "0x79d617768c70936f097cf6e82d1fdca15dc4417c": TokenInfo(
        currency=CurrencyInfo(symbol="HUG", name="Hubbsgold"), scaling=Decimal("1e-8")
    ),
    "0x79da1431150c9b82d2e5dfc1c68b33216846851e": TokenInfo(
        currency=CurrencyInfo(symbol="ILTC", name="iLTC"), scaling=Decimal("1e-18")
    ),
    "0x79de7ab8aed2cf7187cafcc9bc5a8101364a3a9e": TokenInfo(
        currency=CurrencyInfo(symbol="AMUN.CX", name="Amundi"), scaling=Decimal("1e-8")
    ),
    "0x79ef5b79dc1e6b99fa9d896779e94ae659b494f2": TokenInfo(
        currency=CurrencyInfo(symbol="MYTH", name="Mythical Token"), scaling=Decimal("1e-9")
    ),
    "0x79f9ef8429b24e3cb0929eaaa5fabfcc3b15f86d": TokenInfo(
        currency=CurrencyInfo(symbol="GME.CX", name="Gamestop"), scaling=Decimal("1e-8")
    ),
    "0x7a07e1a0c2514d51132183ecfea2a880ec3b7648": TokenInfo(
        currency=CurrencyInfo(symbol="IXE", name="IXTUS"), scaling=Decimal("1e-18")
    ),
    "0x7a18919f0b05fa5e91f3ef43afe8a72105c9d4b8": TokenInfo(
        currency=CurrencyInfo(symbol="WMB", name="WatermelonBlock"), scaling=Decimal("1e-6")
    ),
    "0x7a2810d3d859ed03ede523eb801a3b43b5e8979c": TokenInfo(
        currency=CurrencyInfo(symbol="ZDC", name="Zodcoin"), scaling=Decimal("1e-18")
    ),
    "0x7a2bc711e19ba6aff6ce8246c546e8c4b4944dfd": TokenInfo(
        currency=CurrencyInfo(symbol="WAXE", name="WAXE"), scaling=Decimal("1e-8")
    ),
    "0x7a3d5d49d64e57dbd6fbb21df7202bd3ee7a2253": TokenInfo(
        currency=CurrencyInfo(symbol="TCORE", name="Tornado Core"), scaling=Decimal("1e-18")
    ),
    "0x7a41e0517a5eca4fdbc7fbeba4d4c47b9ff6dc63": TokenInfo(
        currency=CurrencyInfo(symbol="ZSC", name="Zeusshield"), scaling=Decimal("1e-18")
    ),
    "0x7a4d70528c0b8d376c206b0fb2c9db1d26315c2d": TokenInfo(
        currency=CurrencyInfo(symbol="IST", name="iShop Token"), scaling=Decimal("1e-18")
    ),
    "0x7a545ed3863221a974f327199ac22f7f12535f11": TokenInfo(
        currency=CurrencyInfo(symbol="BGTT", name="Baguette Token"), scaling=Decimal("1e-18")
    ),
    "0x7a54fae94b6960d9f7316612eec179078e911769": TokenInfo(
        currency=CurrencyInfo(symbol="MOVIE", name="MoviePass"), scaling=Decimal("1e-18")
    ),
    "0x7a5599b97e8c4abb5dd06eba0e9d1f75af818db9": TokenInfo(
        currency=CurrencyInfo(symbol="RTC", name="OSMOTIC TOKEN"), scaling=Decimal("1e-18")
    ),
    "0x7a58c0be72be218b41c608b7fe7c5bb630736c71": TokenInfo(
        currency=CurrencyInfo(symbol="PEOPLE", name="ConstitutionDAO"), scaling=Decimal("1e-18")
    ),
    "0x7a58da7c0568557ec65cd53c0dbe5b134a022a14": TokenInfo(
        currency=CurrencyInfo(symbol="WZBLT", name="Wrapped ZEBELLION"), scaling=Decimal("1e-18")
    ),
    "0x7a5ce2b56dc00cb7b369ad2e1b3309abdc145bef": TokenInfo(
        currency=CurrencyInfo(symbol="BNBMOON", name="10X Long BNB Token"), scaling=Decimal("1e-18")
    ),
    "0x7a5ce6abd131ea6b148a022cb76fc180ae3315a6": TokenInfo(
        currency=CurrencyInfo(symbol="BALPHA", name="bAlpha"), scaling=Decimal("1e-18")
    ),
    "0x7a5e6ca9d335e343d1ed12239f67248e056afe2f": TokenInfo(
        currency=CurrencyInfo(symbol="HETM", name="Ethash Miner"), scaling=Decimal("1e-6")
    ),
    "0x7a5ff295dc8239d5c2374e4d894202aaf029cab6": TokenInfo(
        currency=CurrencyInfo(symbol="SLT", name="Smartlands Token"), scaling=Decimal("1e-3")
    ),
    "0x7a6910b15d929f20f85ecbfcbd89862062147d78": TokenInfo(
        currency=CurrencyInfo(symbol="HDCC", name="Hyper Dimension Chain"), scaling=Decimal("1e-18")
    ),
    "0x7a74c427c833bad2a638e0fb203ba2c728f557c1": TokenInfo(
        currency=CurrencyInfo(symbol="RDC", name="Ordocoin"), scaling=Decimal("1e-18")
    ),
    "0x7a82c573b378ceea29772afb93891f0d0afa93b7": TokenInfo(
        currency=CurrencyInfo(symbol="WIZ", name="Wizard"), scaling=Decimal("1e-18")
    ),
    "0x7a8ca2f815a260660158a38c34ca321a3605ecfe": TokenInfo(
        currency=CurrencyInfo(symbol="BIZZ", name="BIZZCOIN"), scaling=Decimal("1e-8")
    ),
    "0x7a939bb714fd2a48ebeb1e495aa9aaa74ba9fa68": TokenInfo(
        currency=CurrencyInfo(symbol="EVZ", name="Electric Vehicle Zone"), scaling=Decimal("1e-18")
    ),
    "0x7aa6b33fb7f395ddbca7b7a33264a3c799fa626f": TokenInfo(
        currency=CurrencyInfo(symbol="DOGEBULL", name="3X Long Dogecoin Token"), scaling=Decimal("1e-18")
    ),
    "0x7aa82ec1cbd3769d2ea55cd3b7957b786d0eff49": TokenInfo(
        currency=CurrencyInfo(symbol="SMT", name="Summit Coin"), scaling=Decimal("1e-18")
    ),
    "0x7ab1fc79f319718690e9c883bac910f8e289ce8f": TokenInfo(
        currency=CurrencyInfo(symbol="MB", name="Microchain"), scaling=Decimal("1e-18")
    ),
    "0x7abc60b3290f68c85f495fd2e0c3bd278837a313": TokenInfo(
        currency=CurrencyInfo(symbol="CMCT", name="Cyber Movie Chain"), scaling=Decimal("1e-8")
    ),
    "0x7acb51e690301b114a2a65b2e557cc1b7e644ba8": TokenInfo(
        currency=CurrencyInfo(symbol="EXPO", name="Expo Token"), scaling=Decimal("1e-8")
    ),
    "0x7ae0d42f23c33338de15bfa89c7405c068d9dc0a": TokenInfo(
        currency=CurrencyInfo(symbol="VERSE", name="Shibaverse"), scaling=Decimal("1e-18")
    ),
    "0x7ae1d57b58fa6411f32948314badd83583ee0e8c": TokenInfo(
        currency=CurrencyInfo(symbol="PAPER", name="Dope Wars Paper"), scaling=Decimal("1e-18")
    ),
    "0x7af89c8a06719271a96e62e290ea9ed192e73fc1": TokenInfo(
        currency=CurrencyInfo(symbol="GMM", name="Gold Mining Members"), scaling=Decimal("1e-18")
    ),
    "0x7afac1d878c66a47263dce57976c371ae2e74882": TokenInfo(
        currency=CurrencyInfo(symbol="YFMB", name="YFMoonBeam"), scaling=Decimal("1e-18")
    ),
    "0x7b0c06043468469967dba22d1af33d77d44056c8": TokenInfo(
        currency=CurrencyInfo(symbol="MRPH", name="Morpheus Network"), scaling=Decimal("1e-4")
    ),
    "0x7b0f66fa5cf5cc28280c1e7051af881e06579362": TokenInfo(
        currency=CurrencyInfo(symbol="YFARMER", name="YFarmLand Token"), scaling=Decimal("1e-18")
    ),
    "0x7b123f53421b1bf8533339bfbdc7c98aa94163db": TokenInfo(
        currency=CurrencyInfo(symbol="BUIDL", name="dfohub"), scaling=Decimal("1e-18")
    ),
    "0x7b188a8b3a2113621895fb35fc67a779caffa92d": TokenInfo(
        currency=CurrencyInfo(symbol="QOS", name="QOS Chain"), scaling=Decimal("1e-4")
    ),
    "0x7b1fba5ddd5cfee1fcc27514d8f7dae4669c4d82": TokenInfo(
        currency=CurrencyInfo(symbol="TEAM.CX", name="Atlassian Corporation Plc"), scaling=Decimal("1e-8")
    ),
    "0x7b22938ca841aa392c93dbb7f4c42178e3d65e88": TokenInfo(
        currency=CurrencyInfo(symbol="ASTRO", name="Astro"), scaling=Decimal("1e-4")
    ),
    "0x7b2df125567815ac9b57da04b620f50bc93b320c": TokenInfo(
        currency=CurrencyInfo(symbol="ACTP", name="Archetypal Network"), scaling=Decimal("1e-8")
    ),
    "0x7b3296198f8a548edf89bdb16864da8f37b7d9cb": TokenInfo(
        currency=CurrencyInfo(symbol="GNTO", name="GoldeNugget"), scaling=Decimal("1e-18")
    ),
    "0x7b3d36eb606f873a75a6ab68f8c999848b04f935": TokenInfo(
        currency=CurrencyInfo(symbol="LOOT", name="NFTLootBox"), scaling=Decimal("1e-18")
    ),
    "0x7b6f71c8b123b38aa8099e0098bec7fbc35b8a13": TokenInfo(
        currency=CurrencyInfo(symbol="NVT", name="Nerve Network"), scaling=Decimal("1e-8")
    ),
    "0x7ba19b7f7d106a9a1e0985397b94f38eee0b555e": TokenInfo(
        currency=CurrencyInfo(symbol="WIX", name="Wixlar"), scaling=Decimal("1e-2")
    ),
    "0x7ba8a5d59b21390a70b2ba968a183712e12a049c": TokenInfo(
        currency=CurrencyInfo(symbol="VTY", name="Verity"), scaling=Decimal("1e-18")
    ),
    "0x7bd33c6daf9ba1bdbc7652fabdc7b308f41668c5": TokenInfo(
        currency=CurrencyInfo(symbol="TGBP", name="TrueGBP"), scaling=Decimal("1e-18")
    ),
    "0x7bd6a4e7db3a34c485a8dd02b30b6565e3bbc633": TokenInfo(
        currency=CurrencyInfo(symbol="KOK", name="KOK Coin"), scaling=Decimal("1e-18")
    ),
    "0x7be00ed6796b21656732e8f739fc1b8f1c53da0d": TokenInfo(
        currency=CurrencyInfo(symbol="ACXT", name="ACDX Exchange Token"), scaling=Decimal("1e-18")
    ),
    "0x7be5901f679bde8202a123c84c19bbce2cf3449b": TokenInfo(
        currency=CurrencyInfo(symbol="FLA", name="Fiola"), scaling=Decimal("1e-18")
    ),
    "0x7bebd226154e865954a87650faefa8f485d36081": TokenInfo(
        currency=CurrencyInfo(symbol="ZIG", name="Zignaly"), scaling=Decimal("1e-18")
    ),
    "0x7c0382583bc52d677d17e205665979ca75aa724a": TokenInfo(
        currency=CurrencyInfo(symbol="GLPG.CX", name="Galapagos NV"), scaling=Decimal("1e-8")
    ),
    "0x7c0afd49d40ec308d49e2926e5c99b037d54ee7e": TokenInfo(
        currency=CurrencyInfo(symbol="OUSD", name="Onyx USD"), scaling=Decimal("1e-18")
    ),
    "0x7c2af3a86b4bf47e6ee63ad9bde7b3b0ba7f95da": TokenInfo(
        currency=CurrencyInfo(symbol="ABA", name="EcoBall"), scaling=Decimal("1e-18")
    ),
    "0x7c2e5b7ec572199d3841f6a38f7d4868bd0798f1": TokenInfo(
        currency=CurrencyInfo(symbol="HAVY", name="Havy"), scaling=Decimal("1e-8")
    ),
    "0x7c32db0645a259fae61353c1f891151a2e7f8c1e": TokenInfo(
        currency=CurrencyInfo(symbol="PTM", name="Potentiam"), scaling=Decimal("1e-18")
    ),
    "0x7c3ff33c76c919b3f5fddaf7bdddbb20a826dc61": TokenInfo(
        currency=CurrencyInfo(symbol="FROGGIES", name="Froggies"), scaling=Decimal("1e-9")
    ),
    "0x7c5a0ce9267ed19b22f8cae653f198e3e8daf098": TokenInfo(
        currency=CurrencyInfo(symbol="SAN", name="Santiment Network Token"), scaling=Decimal("1e-18")
    ),
    "0x7c5d5100b339fe7d995a893af6cb496b9474373c": TokenInfo(
        currency=CurrencyInfo(symbol="LOON", name="Loon Network"), scaling=Decimal("1e-18")
    ),
    "0x7c6c3b4e91923f080d6cc847a68d7330400a95d7": TokenInfo(
        currency=CurrencyInfo(symbol="UNDT", name="Union Network Dollar Token"), scaling=Decimal("1e-18")
    ),
    "0x7c81542ed859a2061538fee22b6544a235b9557d": TokenInfo(
        currency=CurrencyInfo(symbol="COMB", name="Combo"), scaling=Decimal("1e-18")
    ),
    "0x7c82a76db0166b0e153a66b1a4c331970b2b0ee2": TokenInfo(
        currency=CurrencyInfo(symbol="DBY", name="Dobuy"), scaling=Decimal("1e-18")
    ),
    "0x7c9511e3e8b8875694d283b28cb21f12c0017b69": TokenInfo(
        currency=CurrencyInfo(symbol="TLRY.CX", name="Tilray Inc"), scaling=Decimal("1e-8")
    ),
    "0x7c974104df9dd7fb91205ab3d66d15aff1049de8": TokenInfo(
        currency=CurrencyInfo(symbol="WUSD", name="Wrapped USD"), scaling=Decimal("1e-18")
    ),
    "0x7ca121b093e2fbd4bb9a894bd5ff487d16f1f83b": TokenInfo(
        currency=CurrencyInfo(symbol="LESS", name="LORDLESS"), scaling=Decimal("1e-18")
    ),
    "0x7ca4408137eb639570f8e647d9bd7b7e8717514a": TokenInfo(
        currency=CurrencyInfo(symbol="ALPA", name="Alpaca City"), scaling=Decimal("1e-18")
    ),
    "0x7ca62545a380e7d71f8f5cfa14b9211002075930": TokenInfo(
        currency=CurrencyInfo(symbol="SVS", name="SVS"), scaling=Decimal("1e-18")
    ),
    "0x7cc61e3ae6360e923e9296c802382ec7c9dd3652": TokenInfo(
        currency=CurrencyInfo(symbol="SUN", name="SUN"), scaling=Decimal("1e-8")
    ),
    "0x7cca27e4ec9e448350db3f7671759d668737d906": TokenInfo(
        currency=CurrencyInfo(symbol="BLM", name="Bitalium Token"), scaling=Decimal("1e-0")
    ),
    "0x7cf271966f36343bf0150f25e5364f7961c58201": TokenInfo(
        currency=CurrencyInfo(symbol="DEPO", name="CRYPTODEPOZIT"), scaling=Decimal("1e-0")
    ),
    "0x7cf6dc769482abee2ff75795d000f381a8062dec": TokenInfo(
        currency=CurrencyInfo(symbol="FAR", name="Far Token"), scaling=Decimal("1e-18")
    ),
    "0x7d1234e0b45acb7dadc321325ba113a6f7caa7ee": TokenInfo(
        currency=CurrencyInfo(symbol="ETCDOOM", name="10X Short Ethereum Classic Token"), scaling=Decimal("1e-18")
    ),
    "0x7d14b842630cbc2530cb288109e5719e0c4d67d7": TokenInfo(
        currency=CurrencyInfo(symbol="IBP", name="Innovation Blockchain Payment"), scaling=Decimal("1e-18")
    ),
    "0x7d1afa7b718fb893db30a3abc0cfc608aacfebb0": TokenInfo(
        currency=CurrencyInfo(symbol="MATIC", name="Polygon"), scaling=Decimal("1e-18")
    ),
    "0x7d25d9f10cd224ecce0bc824a2ec800db81c01d7": TokenInfo(
        currency=CurrencyInfo(symbol="OPT", name="ETHOPT"), scaling=Decimal("1e-18")
    ),
    "0x7d29a64504629172a429e64183d6673b9dacbfce": TokenInfo(
        currency=CurrencyInfo(symbol="VXV", name="Vectorspace AI"), scaling=Decimal("1e-18")
    ),
    "0x7d2d3688df45ce7c552e19c27e007673da9204b8": TokenInfo(
        currency=CurrencyInfo(symbol="ALEND", name="Aave LEND v1"), scaling=Decimal("1e-18")
    ),
    "0x7d34c87c34a12f80912c452c528dbd24d8520e69": TokenInfo(
        currency=CurrencyInfo(symbol="RSX", name="Raisex Token"), scaling=Decimal("1e-18")
    ),
    "0x7d3e7d41da367b4fdce7cbe06502b13294deb758": TokenInfo(
        currency=CurrencyInfo(symbol="SSS", name="Sharechain"), scaling=Decimal("1e-8")
    ),
    "0x7d4b1d793239707445305d8d2456d2c735f6b25b": TokenInfo(
        currency=CurrencyInfo(symbol="CBSN", name="BlockSwap Network"), scaling=Decimal("1e-18")
    ),
    "0x7d4b8cce0591c9044a22ee543533b72e976e36c3": TokenInfo(
        currency=CurrencyInfo(symbol="CAG", name="Change"), scaling=Decimal("1e-18")
    ),
    "0x7d5121505149065b562c789a0145ed750e6e8cdd": TokenInfo(
        currency=CurrencyInfo(symbol="VR", name="Victoria VR"), scaling=Decimal("1e-18")
    ),
    "0x7d5edcd23daa3fb94317d32ae253ee1af08ba14d": TokenInfo(
        currency=CurrencyInfo(symbol="EBET", name="EthBet"), scaling=Decimal("1e-2")
    ),
    "0x7d85e23014f84e6e21d5663acd8751bef3562352": TokenInfo(
        currency=CurrencyInfo(symbol="AXN", name="Axion"), scaling=Decimal("1e-18")
    ),
    "0x7d91e637589ec3bb54d8213a9e92dc6e8d12da91": TokenInfo(
        currency=CurrencyInfo(symbol="FWB", name="Friends With Benefits [OLD]"), scaling=Decimal("1e-4")
    ),
    "0x7db02aa39a3d0271e4c61c04d03857a10fc922c5": TokenInfo(
        currency=CurrencyInfo(symbol="BTCA", name="Bitcoin Asia"), scaling=Decimal("1e-10")
    ),
    "0x7db5454f3500f28171d1f9c7a38527c9cf94e6b2": TokenInfo(
        currency=CurrencyInfo(symbol="AGS", name="Silver Standard"), scaling=Decimal("1e-4")
    ),
    "0x7db711fbe4bace5052f4ca19f700413a06e1f732": TokenInfo(
        currency=CurrencyInfo(symbol="EPS", name="Environmental Protection Share"), scaling=Decimal("1e-18")
    ),
    "0x7dbdd9dafdc4c1c03d67925a4f85daa398af32b0": TokenInfo(
        currency=CurrencyInfo(symbol="ANW", name="Anchor Neural World Token"), scaling=Decimal("1e-18")
    ),
    "0x7dc4f41294697a7903c4027f6ac528c5d14cd7eb": TokenInfo(
        currency=CurrencyInfo(symbol="RMC", name="RemiCoin"), scaling=Decimal("1e-8")
    ),
    "0x7dc59729b0adf4ae34721a1e06ef82a19e690b04": TokenInfo(
        currency=CurrencyInfo(symbol="BAC", name="BTC-Alpha Token"), scaling=Decimal("1e-8")
    ),
    "0x7dcb3b2356c822d3577d4d060d0d5d78c860488c": TokenInfo(
        currency=CurrencyInfo(symbol="FANX", name="FANX"), scaling=Decimal("1e-18")
    ),
    "0x7dd7f56d697cc0f2b52bd55c057f378f1fe6ab4b": TokenInfo(
        currency=CurrencyInfo(symbol="$TEAK", name="$TEAK"), scaling=Decimal("1e-18")
    ),
    "0x7dd9c5cba05e151c895fde1cf355c9a1d5da6429": TokenInfo(
        currency=CurrencyInfo(symbol="GLM", name="Golem"), scaling=Decimal("1e-18")
    ),
    "0x7de2d123042994737105802d2abd0a10a7bde276": TokenInfo(
        currency=CurrencyInfo(symbol="MEXC", name="MEXC Token"), scaling=Decimal("1e-18")
    ),
    "0x7de91b204c1c737bcee6f000aaa6569cf7061cb7": TokenInfo(
        currency=CurrencyInfo(symbol="XRT", name="Robonomics Network"), scaling=Decimal("1e-9")
    ),
    "0x7deb5e830be29f91e298ba5ff1356bb7f8146998": TokenInfo(
        currency=CurrencyInfo(symbol="AMKR", name="Aave MKR v1"), scaling=Decimal("1e-18")
    ),
    "0x7dee371a788f9bd6c546df83f0d74fbe37cbf006": TokenInfo(
        currency=CurrencyInfo(symbol="TECN", name="Teccoin"), scaling=Decimal("1e-18")
    ),
    "0x7e03521b9da891ca3f79a8728e2eaeb24886c5f9": TokenInfo(
        currency=CurrencyInfo(symbol="MATICBULL", name="3X Long Matic Token"), scaling=Decimal("1e-18")
    ),
    "0x7e1a6fb26702ecb0439a641c5c285f7eec430419": TokenInfo(
        currency=CurrencyInfo(symbol="KYSC", name="KYSC Token"), scaling=Decimal("1e-18")
    ),
    "0x7e291890b01e5181f7ecc98d79ffbe12ad23df9e": TokenInfo(
        currency=CurrencyInfo(symbol="NIF", name="Unifty"), scaling=Decimal("1e-18")
    ),
    "0x7e442206da059905050ba02be63cbb85c559eb04": TokenInfo(
        currency=CurrencyInfo(symbol="FICO", name="French ICO Coin"), scaling=Decimal("1e-18")
    ),
    "0x7e4d1cd8927ce41bcbfa4f32cada1a6998cb5a51": TokenInfo(
        currency=CurrencyInfo(symbol="ELL", name="ETH AI Limit Loss"), scaling=Decimal("1e-18")
    ),
    "0x7e5f9f248e84ef0b1f63586323e92a0d91b15568": TokenInfo(
        currency=CurrencyInfo(symbol="BTC3L", name="Amun Bitcoin 3x Daily Long"), scaling=Decimal("1e-18")
    ),
    "0x7e667525521cf61352e2e01b50faaae7df39749a": TokenInfo(
        currency=CurrencyInfo(symbol="CMC", name="CMC "), scaling=Decimal("1e-18")
    ),
    "0x7e8c149f70437eba6785f9059190a5b08abf03de": TokenInfo(
        currency=CurrencyInfo(symbol="MBTC", name="MiniBitcoin"), scaling=Decimal("1e-8")
    ),
    "0x7e9d62e1ff4e34096f91ee0153222ab81f7184f0": TokenInfo(
        currency=CurrencyInfo(symbol="ELTC2", name="eLTC"), scaling=Decimal("1e-8")
    ),
    "0x7e9d8f07a64e363e97a648904a89fb4cd5fb94cd": TokenInfo(
        currency=CurrencyInfo(symbol="FF", name="Forefront"), scaling=Decimal("1e-18")
    ),
    "0x7e9e431a0b8c4d532c745b1043c7fa29a48d4fba": TokenInfo(
        currency=CurrencyInfo(symbol="EOSDAC", name="eosDAC"), scaling=Decimal("1e-18")
    ),
    "0x7e9e99f059bb84298332b63be6f882a73120b9fb": TokenInfo(
        currency=CurrencyInfo(symbol="MCR", name="Macro"), scaling=Decimal("1e-8")
    ),
    "0x7eaf9c89037e4814dc0d9952ac7f888c784548db": TokenInfo(
        currency=CurrencyInfo(symbol="ROYA", name="Royale"), scaling=Decimal("1e-18")
    ),
    "0x7eaff6b30f225475061fa49aae97333666e258ff": TokenInfo(
        currency=CurrencyInfo(symbol="EDP", name="E-Dome Plus"), scaling=Decimal("1e-2")
    ),
    "0x7ed07b51975d9e8363b568b2d725be8f3e8516cf": TokenInfo(
        currency=CurrencyInfo(symbol="MUFC", name="Manchester United Fan Token"), scaling=Decimal("1e-18")
    ),
    "0x7edc9e8a1196259b7c6aba632037a9443d4e14f7": TokenInfo(
        currency=CurrencyInfo(symbol="AAPL.CX", name="Apple Inc"), scaling=Decimal("1e-8")
    ),
    "0x7ef55a013d0632c24955553367c8d5cc082ddbff": TokenInfo(
        currency=CurrencyInfo(symbol="SLVG", name="SILVERING"), scaling=Decimal("1e-18")
    ),
    "0x7f0c8b125040f707441cad9e5ed8a8408673b455": TokenInfo(
        currency=CurrencyInfo(symbol="NEBO", name="CSP DAO Network"), scaling=Decimal("1e-18")
    ),
    "0x7f1cdbab1e03882da7742e09611f3298add9f890": TokenInfo(
        currency=CurrencyInfo(symbol="ERA", name="EarthBi"), scaling=Decimal("1e-18")
    ),
    "0x7f1e2c7d6a69bf34824d72c53b4550e895c0d8c2": TokenInfo(
        currency=CurrencyInfo(symbol="BOP", name="blockoptions"), scaling=Decimal("1e-8")
    ),
    "0x7f20f6e68bd14dbdb95244dbee6c316999a2d4c1": TokenInfo(
        currency=CurrencyInfo(symbol="FUSD", name="Foton USD"), scaling=Decimal("1e-8")
    ),
    "0x7f23114a9810757f38bf5d5a342872aafbe98c13": TokenInfo(
        currency=CurrencyInfo(symbol="LEEE", name="LeeeMall"), scaling=Decimal("1e-18")
    ),
    "0x7f280dac515121dcda3eac69eb4c13a52392cace": TokenInfo(
        currency=CurrencyInfo(symbol="FNC", name="Fancy Games"), scaling=Decimal("1e-18")
    ),
    "0x7f288ff5a8055f5f6103a80dd806cf8415e035c7": TokenInfo(
        currency=CurrencyInfo(symbol="CFC", name="Chain Finance"), scaling=Decimal("1e-18")
    ),
    "0x7f373d989df0709273e18769300ef1177d333799": TokenInfo(
        currency=CurrencyInfo(symbol="BKB", name="Bitker Token"), scaling=Decimal("1e-18")
    ),
    "0x7f3edcdd180dbe4819bd98fee8929b5cedb3adeb": TokenInfo(
        currency=CurrencyInfo(symbol="XTK", name="xToken"), scaling=Decimal("1e-18")
    ),
    "0x7f4b2a690605a7cbb66f7aa6885ebd906a5e2e9e": TokenInfo(
        currency=CurrencyInfo(symbol="TICO", name="Topinvestmentcoin"), scaling=Decimal("1e-8")
    ),
    "0x7f585b9130c64e9e9f470b618a7badd03d79ca7e": TokenInfo(
        currency=CurrencyInfo(symbol="CR7", name="CR7Coin"), scaling=Decimal("1e-18")
    ),
    "0x7f65be7fad0c22813e51746e7e8f13a20baa9411": TokenInfo(
        currency=CurrencyInfo(symbol="RBTC", name="Rebitcoin"), scaling=Decimal("1e-8")
    ),
    "0x7f86c782ec802ac402e0369d2e6d500256f7abc5": TokenInfo(
        currency=CurrencyInfo(symbol="RINGX", name="RING X PLATFORM"), scaling=Decimal("1e-18")
    ),
    "0x7f927f984177323c4ac49e6b1d398e40cd1a78f6": TokenInfo(
        currency=CurrencyInfo(symbol="YLD", name="Yield Coin"), scaling=Decimal("1e-2")
    ),
    "0x7f969c4d388ca0ae39a4fddb1a6f89878ca2fbf8": TokenInfo(
        currency=CurrencyInfo(symbol="GGC", name="GGCOIN"), scaling=Decimal("1e-18")
    ),
    "0x7f9a00e03c2e53a3af6031c17a150dbedaaab3dc": TokenInfo(
        currency=CurrencyInfo(symbol="RTC", name="Read This Contract"), scaling=Decimal("1e-18")
    ),
    "0x7fc408011165760ee31be2bf20daf450356692af": TokenInfo(
        currency=CurrencyInfo(symbol="MTR", name="Mitrav"), scaling=Decimal("1e-8")
    ),
    "0x7fc66500c84a76ad7e9c93437bfc5ac33e2ddae9": TokenInfo(
        currency=CurrencyInfo(symbol="AAVE", name="Aave"), scaling=Decimal("1e-18")
    ),
    "0x7fc693b16184b6778f4534f5410f06633cb030e0": TokenInfo(
        currency=CurrencyInfo(symbol="RLX", name="RELAX Protocol"), scaling=Decimal("1e-6")
    ),
    "0x7fccadee21660425fdec86029b6362845ffc052c": TokenInfo(
        currency=CurrencyInfo(symbol="HIN", name="TimeBanking"), scaling=Decimal("1e-8")
    ),
    "0x7fce2856899a6806eeef70807985fc7554c66340": TokenInfo(
        currency=CurrencyInfo(symbol="CLPC", name="CLP token"), scaling=Decimal("1e-9")
    ),
    "0x7ff4169a6b5122b664c51c95727d87750ec07c84": TokenInfo(
        currency=CurrencyInfo(symbol="10SET", name="Tenset"), scaling=Decimal("1e-18")
    ),
    "0x8013d06a86f341afab95f82f6487e44c4dc0c655": TokenInfo(
        currency=CurrencyInfo(symbol="BSVG", name="BITCOINSVGOLD"), scaling=Decimal("1e-18")
    ),
    "0x8040d35ed6c82f75b1078cf5eb93a2cfd34b2bd8": TokenInfo(
        currency=CurrencyInfo(symbol="BTR", name="Bitreal"), scaling=Decimal("1e-18")
    ),
    "0x8064d9ae6cdf087b1bcd5bdf3531bd5d8c537a68": TokenInfo(
        currency=CurrencyInfo(symbol="OBTC", name="BoringDAO BTC"), scaling=Decimal("1e-18")
    ),
    "0x8069080a922834460c3a092fb2c1510224dc066b": TokenInfo(
        currency=CurrencyInfo(symbol="SPC", name="SpaceChain"), scaling=Decimal("1e-18")
    ),
    "0x808126cd87bde0144f1487dbfecc092613a3a832": TokenInfo(
        currency=CurrencyInfo(symbol="KO.CX", name="Coca-Cola"), scaling=Decimal("1e-8")
    ),
    "0x808507121b80c02388fad14726482e061b8da827": TokenInfo(
        currency=CurrencyInfo(symbol="PENDLE", name="Pendle"), scaling=Decimal("1e-18")
    ),
    "0x808662d05b8d6f613cab2fbfae3a32b20bf44f9a": TokenInfo(
        currency=CurrencyInfo(symbol="TGBP", name="TrueGBP"), scaling=Decimal("1e-18")
    ),
    "0x809826cceab68c387726af962713b64cb5cb3cca": TokenInfo(
        currency=CurrencyInfo(symbol="NCASH", name="Nucleus Vision"), scaling=Decimal("1e-18")
    ),
    "0x80a7e048f37a50500351c204cb407766fa3bae7f": TokenInfo(
        currency=CurrencyInfo(symbol="CRPT", name="CrypteriumToken"), scaling=Decimal("1e-18")
    ),
    "0x80ab141f324c3d6f2b18b030f1c4e95d4d658778": TokenInfo(
        currency=CurrencyInfo(symbol="DEA", name="DEA"), scaling=Decimal("1e-18")
    ),
    "0x80bc5512561c7f85a3a9508c7df7901b370fa1df": TokenInfo(
        currency=CurrencyInfo(symbol="TIO", name="TradeToken"), scaling=Decimal("1e-18")
    ),
    "0x80bd0cc689c206e3f642919244c4251c7ef19852": TokenInfo(
        currency=CurrencyInfo(symbol="SGC", name="Sudan Gold Coin"), scaling=Decimal("1e-18")
    ),
    "0x80c62fe4487e1351b47ba49809ebd60ed085bf52": TokenInfo(
        currency=CurrencyInfo(symbol="CLV", name="Clover Finance"), scaling=Decimal("1e-18")
    ),
    "0x80c8c3dcfb854f9542567c8dac3f44d709ebc1de": TokenInfo(
        currency=CurrencyInfo(symbol="MILK2", name="Spaceswap MILK2"), scaling=Decimal("1e-18")
    ),
    "0x80ce3027a70e0a928d9268994e9b85d03bd4cdcf": TokenInfo(
        currency=CurrencyInfo(symbol="LKR", name="Polkalokr"), scaling=Decimal("1e-18")
    ),
    "0x80d211718f9b9ba31959a14328acd8d8c9d5382f": TokenInfo(
        currency=CurrencyInfo(symbol="PLM", name="Palmes"), scaling=Decimal("1e-6")
    ),
    "0x80d55c03180349fff4a229102f62328220a96444": TokenInfo(
        currency=CurrencyInfo(symbol="OPUL", name="Opulous"), scaling=Decimal("1e-18")
    ),
    "0x80f222a749a2e18eb7f676d371f19ad7efeee3b7": TokenInfo(
        currency=CurrencyInfo(symbol="MGN", name="Magnolia Token"), scaling=Decimal("1e-18")
    ),
    "0x80fb784b7ed66730e8b1dbd9820afd29931aab03": TokenInfo(
        currency=CurrencyInfo(symbol="LEND", name="Aave [OLD]"), scaling=Decimal("1e-18")
    ),
    "0x810908b285f85af668f6348cd8b26d76b3ec12e1": TokenInfo(
        currency=CurrencyInfo(symbol="SPAZ", name="SwapCoinz"), scaling=Decimal("1e-8")
    ),
    "0x811817a87f9b9c00621d6a1a9a3cf8ccf10f4e7f": TokenInfo(
        currency=CurrencyInfo(symbol="BID", name="Bitcoin International Domestique"), scaling=Decimal("1e-18")
    ),
    "0x81313f7c5c9c824236c9e4cba3ac4b049986e756": TokenInfo(
        currency=CurrencyInfo(symbol="HIPPO", name="HippoFinance"), scaling=Decimal("1e-18")
    ),
    "0x81361ba977b6e214e905d4e03c65557b757240d9": TokenInfo(
        currency=CurrencyInfo(symbol="NSE", name="Neo Smart Energy"), scaling=Decimal("1e-8")
    ),
    "0x813b428af3920226e059b68a62e4c04933d4ea7a": TokenInfo(
        currency=CurrencyInfo(symbol="DATP", name="Decentralized Asset Trading Platform"), scaling=Decimal("1e-8")
    ),
    "0x814964b1bceaf24e26296d031eadf134a2ca4105": TokenInfo(
        currency=CurrencyInfo(symbol="NEWB", name="Newbium"), scaling=Decimal("1e-0")
    ),
    "0x814cafd4782d2e728170fda68257983f03321c58": TokenInfo(
        currency=CurrencyInfo(symbol="IDEA", name="IDEA Token"), scaling=Decimal("1e-0")
    ),
    "0x814e0908b12a99fecf5bc101bb5d0b8b5cdf7d26": TokenInfo(
        currency=CurrencyInfo(symbol="MDT", name="Measurable Data Token"), scaling=Decimal("1e-18")
    ),
    "0x814f67fa286f7572b041d041b1d99b432c9155ee": TokenInfo(
        currency=CurrencyInfo(symbol="DRG", name="Dragon Coin"), scaling=Decimal("1e-8")
    ),
    "0x81705082ef9f0d660f07be80093d46d826d48b25": TokenInfo(
        currency=CurrencyInfo(symbol="GVE", name="Globalvillage Ecosystem"), scaling=Decimal("1e-18")
    ),
    "0x8178851bb47227811f8d24bc2671ec2a63d4b70e": TokenInfo(
        currency=CurrencyInfo(symbol="AEM.CX", name="Agnico Eagle"), scaling=Decimal("1e-8")
    ),
    "0x817bbdbc3e8a1204f3691d14bb44992841e3db35": TokenInfo(
        currency=CurrencyInfo(symbol="CUDOS", name="Cudos"), scaling=Decimal("1e-18")
    ),
    "0x81824663353a9d29b01b2de9dd9a2bb271d298cd": TokenInfo(
        currency=CurrencyInfo(symbol="BVOL", name="Bitcoin Volatility Token"), scaling=Decimal("1e-18")
    ),
    "0x81859801b01764d4f0fa5e64729f5a6c3b91435b": TokenInfo(
        currency=CurrencyInfo(symbol="BFIE", name="BFIE"), scaling=Decimal("1e-18")
    ),
    "0x8188e51bc678f0070531f0e782718df0027452de": TokenInfo(
        currency=CurrencyInfo(symbol="ZERA", name="ZERACOIN"), scaling=Decimal("1e-8")
    ),
    "0x818fc6c2ec5986bc6e2cbf00939d90556ab12ce5": TokenInfo(
        currency=CurrencyInfo(symbol="KIN", name="Kin"), scaling=Decimal("1e-18")
    ),
    "0x81995ff7aee5c780192b47e0b42a7a86692d1415": TokenInfo(
        currency=CurrencyInfo(symbol="SCS", name="Speedcash"), scaling=Decimal("1e-18")
    ),
    "0x81ab848898b5ffd3354dbbefb333d5d183eedcb5": TokenInfo(
        currency=CurrencyInfo(symbol="YUSD-SEP20", name="yUSD Synthetic Token Expiring 1 September 2020"),
        scaling=Decimal("1e-18"),
    ),
    "0x81b1bfd6cb9ad42db395c2a27f73d4dcf5777e2d": TokenInfo(
        currency=CurrencyInfo(symbol="RARE", name="Rare"), scaling=Decimal("1e-4")
    ),
    "0x81b4d08645da11374a03749ab170836e4e539767": TokenInfo(
        currency=CurrencyInfo(symbol="PMNT", name="Paymon"), scaling=Decimal("1e-9")
    ),
    "0x81c55017f7ce6e72451ced49ff7bab1e3df64d0c": TokenInfo(
        currency=CurrencyInfo(symbol="BTCMINVOL", name="BTC Range Bound Min Volatility Set"), scaling=Decimal("1e-18")
    ),
    "0x81c9151de0c8bafcd325a57e3db5a5df1cebf79c": TokenInfo(
        currency=CurrencyInfo(symbol="DAT", name="Datum"), scaling=Decimal("1e-18")
    ),
    "0x81e74a3ea4bab2277aa3b941e9d9f37b08ac5374": TokenInfo(
        currency=CurrencyInfo(symbol="IFOOD", name="Ifoods Chain"), scaling=Decimal("1e-18")
    ),
    "0x81ea14e770101e2dfa61df3f38b663084bb0b7e8": TokenInfo(
        currency=CurrencyInfo(symbol="ATIC", name="Austin Chain"), scaling=Decimal("1e-18")
    ),
    "0x81f09ed4b98b1c8e99b1fa838b72acb842afe94c": TokenInfo(
        currency=CurrencyInfo(symbol="PAXGBULL", name="3X Long PAX Gold Token"), scaling=Decimal("1e-18")
    ),
    "0x81f8f0bb1cb2a06649e51913a151f0e7ef6fa321": TokenInfo(
        currency=CurrencyInfo(symbol="VITA", name="VitaDAO"), scaling=Decimal("1e-18")
    ),
    "0x820618367fb401310502760462fba400a32c1d69": TokenInfo(
        currency=CurrencyInfo(symbol="XCO", name="CorelFX Token"), scaling=Decimal("1e-2")
    ),
    "0x8207c1ffc5b6804f6024322ccf34f29c3541ae26": TokenInfo(
        currency=CurrencyInfo(symbol="OGN", name="Origin Protocol"), scaling=Decimal("1e-18")
    ),
    "0x820a8481451e893bc66dce50c84d45617cac3705": TokenInfo(
        currency=CurrencyInfo(symbol="BTCT", name="Bitcoin True"), scaling=Decimal("1e-18")
    ),
    "0x821144518dfe9e7b44fcf4d0824e15e8390d4637": TokenInfo(
        currency=CurrencyInfo(symbol="ATIS", name="Atlantis Token"), scaling=Decimal("1e-18")
    ),
    "0x82125afe01819dff1535d0d6276d57045291b6c0": TokenInfo(
        currency=CurrencyInfo(symbol="MRL", name="Marcelo"), scaling=Decimal("1e-18")
    ),
    "0x8232875761b97a5242a4cffb94828dff5c101950": TokenInfo(
        currency=CurrencyInfo(symbol="OVO", name="ICOVO"), scaling=Decimal("1e-9")
    ),
    "0x824a50df33ac1b41afc52f4194e2e8356c17c3ac": TokenInfo(
        currency=CurrencyInfo(symbol="KICK", name="Kick"), scaling=Decimal("1e-10")
    ),
    "0x825130aa1beef07bdf4f389705321816d05b0d0f": TokenInfo(
        currency=CurrencyInfo(symbol="UNII", name="UNII Finance"), scaling=Decimal("1e-18")
    ),
    "0x825a64810e3ee35bd64c940140ea91a609608abe": TokenInfo(
        currency=CurrencyInfo(symbol="CRTS", name="Cryptotipsfr"), scaling=Decimal("1e-18")
    ),
    "0x8260aa7b903fa1746820ebf674f2f837b22f016b": TokenInfo(
        currency=CurrencyInfo(symbol="LDN", name="LydianCoin"), scaling=Decimal("1e-8")
    ),
    "0x82622209cef6ebf4b8bdb353a8fc7e0b8655d0b0": TokenInfo(
        currency=CurrencyInfo(symbol="NB", name="NUCLEAR BOMB"), scaling=Decimal("1e-0")
    ),
    "0x8275ebf521dc217aa79c88132017a5bcef001dd9": TokenInfo(
        currency=CurrencyInfo(symbol="JWL", name="Jewel"), scaling=Decimal("1e-18")
    ),
    "0x8277bf16e448942c257d7ad51e4cac0004eb30a0": TokenInfo(
        currency=CurrencyInfo(symbol="GCC", name="GoldChainCoin"), scaling=Decimal("1e-18")
    ),
    "0x827d53c8170af52625f414bde00326fc8a085e86": TokenInfo(
        currency=CurrencyInfo(symbol="BXY", name="Beaxy"), scaling=Decimal("1e-18")
    ),
    "0x827e75a2c5f3cc0b2fef9273f6ae4518551ecafb": TokenInfo(
        currency=CurrencyInfo(symbol="ETCMOON", name="10X Long Ethereum Classic Token"), scaling=Decimal("1e-18")
    ),
    "0x827fe1736cee36f7737be6cf502434af294cf137": TokenInfo(
        currency=CurrencyInfo(symbol="ADC$", name="Africa Digital Coin"), scaling=Decimal("1e-18")
    ),
    "0x8287c7b963b405b7b8d467db9d79eec40625b13a": TokenInfo(
        currency=CurrencyInfo(symbol="SWINGBY", name="Swingby"), scaling=Decimal("1e-18")
    ),
    "0x8290333cef9e6d528dd5618fb97a76f268f3edd4": TokenInfo(
        currency=CurrencyInfo(symbol="ANKR", name="Ankr"), scaling=Decimal("1e-18")
    ),
    "0x829067d40a8d1233927891d9b3381d6aecee1e80": TokenInfo(
        currency=CurrencyInfo(symbol="IVY", name="Ivy Mining"), scaling=Decimal("1e-18")
    ),
    "0x8293bbd92c42608b20af588620a76128a33e4de9": TokenInfo(
        currency=CurrencyInfo(symbol="CATS", name="CATCOIN"), scaling=Decimal("1e-6")
    ),
    "0x829a4ca1303383f1082b6b1fb937116e4b3b5605": TokenInfo(
        currency=CurrencyInfo(symbol="WATT", name="WorkChain App Token"), scaling=Decimal("1e-18")
    ),
    "0x82a6a22d68ffba4057d5b49f93de5c05e4416bd1": TokenInfo(
        currency=CurrencyInfo(symbol="MWT", name="MingWen Token"), scaling=Decimal("1e-8")
    ),
    "0x82b0e50478eeafde392d45d1259ed1071b6fda81": TokenInfo(
        currency=CurrencyInfo(symbol="DNA", name="DNA Token"), scaling=Decimal("1e-18")
    ),
    "0x82bd526bdb718c6d4dd2291ed013a5186cae2dca": TokenInfo(
        currency=CurrencyInfo(symbol="VDOC", name="Duty of Care Token"), scaling=Decimal("1e-18")
    ),
    "0x82bddf734bea7f551d664dd23644f451b3c6e87f": TokenInfo(
        currency=CurrencyInfo(symbol="NCLH.CX", name="Norwegian Cruise Line Holdings Ltd"), scaling=Decimal("1e-8")
    ),
    "0x82bdfb4c6f488fc47700cef12c448a2f13f8ff4f": TokenInfo(
        currency=CurrencyInfo(symbol="SKT", name="SealBlock Token"), scaling=Decimal("1e-18")
    ),
    "0x82ef11f04bc3cb863373addf5558dbc01d8f9b9b": TokenInfo(
        currency=CurrencyInfo(symbol="HOROR", name="Halloween"), scaling=Decimal("1e-18")
    ),
    "0x82f39cd08a942f344ca7e7034461cc88c2009199": TokenInfo(
        currency=CurrencyInfo(symbol="AZBI", name="AZBI CORE"), scaling=Decimal("1e-18")
    ),
    "0x82f4ded9cec9b5750fbff5c2185aee35afc16587": TokenInfo(
        currency=CurrencyInfo(symbol="DREAM", name="DreamTeam"), scaling=Decimal("1e-6")
    ),
    "0x82fdedfb7635441aa5a92791d001fa7388da8025": TokenInfo(
        currency=CurrencyInfo(symbol="DTX", name="Digital Ticks"), scaling=Decimal("1e-18")
    ),
    "0x8301b6220eed034bc18e8406241e98fd306322f1": TokenInfo(
        currency=CurrencyInfo(symbol="CODO", name="Corona Dollar"), scaling=Decimal("1e-8")
    ),
    "0x830aae63669205ec1ab738fcc159f4977b06dcd6": TokenInfo(
        currency=CurrencyInfo(symbol="DEON", name="DeonCash"), scaling=Decimal("1e-8")
    ),
    "0x831091da075665168e01898c6dac004a867f1e1b": TokenInfo(
        currency=CurrencyInfo(symbol="GFARM2", name="Gains Farm"), scaling=Decimal("1e-18")
    ),
    "0x8315472bae77f9a2b856a67eb0796480aafcd51c": TokenInfo(
        currency=CurrencyInfo(symbol="MMAON", name="MMAON"), scaling=Decimal("1e-18")
    ),
    "0x832904863978b94802123106e6eb491bdf0df928": TokenInfo(
        currency=CurrencyInfo(symbol="OPTI", name="Optitoken"), scaling=Decimal("1e-18")
    ),
    "0x834625f5d8b006d70a6caaeef73c29442f156daf": TokenInfo(
        currency=CurrencyInfo(symbol="TILY", name="Instantily"), scaling=Decimal("1e-18")
    ),
    "0x834aa7a8dab83672609afa51b4fe6aa55114e424": TokenInfo(
        currency=CurrencyInfo(symbol="SLOPPS", name="SLOPPS"), scaling=Decimal("1e-8")
    ),
    "0x834ce7ad163ab3be0c5fd4e0a81e67ac8f51e00c": TokenInfo(
        currency=CurrencyInfo(symbol="PIS", name="Polkainsure Finance"), scaling=Decimal("1e-18")
    ),
    "0x837010619aeb2ae24141605afc8f66577f6fb2e7": TokenInfo(
        currency=CurrencyInfo(symbol="ZHEGIC", name="zHEGIC"), scaling=Decimal("1e-18")
    ),
    "0x838d8e11b160dec88fe62bf0f743fb7000941e13": TokenInfo(
        currency=CurrencyInfo(symbol="GIG", name="Krios/GIG"), scaling=Decimal("1e-18")
    ),
    "0x83984d6142934bb535793a82adb0a46ef0f66b6d": TokenInfo(
        currency=CurrencyInfo(symbol="REM", name="Remme"), scaling=Decimal("1e-4")
    ),
    "0x83ad87c988ac0c6277c0c6234cc8108b20bb5d9b": TokenInfo(
        currency=CurrencyInfo(symbol="LINKBULL", name="3X Long Chainlink Token"), scaling=Decimal("1e-18")
    ),
    "0x83cee9e086a77e492ee0bb93c2b0437ad6fdeccc": TokenInfo(
        currency=CurrencyInfo(symbol="MNTP", name="Goldmint"), scaling=Decimal("1e-18")
    ),
    "0x83d60e7aed59c6829fb251229061a55f35432c4d": TokenInfo(
        currency=CurrencyInfo(symbol="INFT", name="Infinito"), scaling=Decimal("1e-6")
    ),
    "0x83dc1a0f90bbc5c90d5ccc9c254bf164de4d9dde": TokenInfo(
        currency=CurrencyInfo(symbol="BDC", name="Boardcoin"), scaling=Decimal("1e-18")
    ),
    "0x83e2be8d114f9661221384b3a50d24b96a5653f5": TokenInfo(
        currency=CurrencyInfo(symbol="ZXC", name="0xcert"), scaling=Decimal("1e-18")
    ),
    "0x83e6f1e41cdd28eaceb20cb649155049fac3d5aa": TokenInfo(
        currency=CurrencyInfo(symbol="POLS", name="Polkastarter"), scaling=Decimal("1e-18")
    ),
    "0x83e9f223e1edb3486f876ee888d76bfba26c475a": TokenInfo(
        currency=CurrencyInfo(symbol="GUILD", name="BlockchainSpace"), scaling=Decimal("1e-18")
    ),
    "0x83eb94cb563146a42fe0a8b3d051f2387a7fb81f": TokenInfo(
        currency=CurrencyInfo(symbol="CIPHC", name="Cipher Core Token"), scaling=Decimal("1e-8")
    ),
    "0x83eea00d838f92dec4d1475697b9f4d3537b56e3": TokenInfo(
        currency=CurrencyInfo(symbol="VOISE", name="VOISE"), scaling=Decimal("1e-8")
    ),
    "0x83f798e925bcd4017eb265844fddabb448f1707d": TokenInfo(
        currency=CurrencyInfo(symbol="yUSDT", name="iearn USDT"), scaling=Decimal("1e-6")
    ),
    "0x83f873388cd14b83a9f47fabde3c9850b5c74548": TokenInfo(
        currency=CurrencyInfo(symbol="ZUT", name="Zero Utility Token"), scaling=Decimal("1e-18")
    ),
    "0x83ff572a1757b9e4508cb08f13a79ed162c756c4": TokenInfo(
        currency=CurrencyInfo(symbol="ZCOR", name="Zrocor"), scaling=Decimal("1e-0")
    ),
    "0x840086881facb1e8c222fa5deb2f93f238b0ba95": TokenInfo(
        currency=CurrencyInfo(symbol="RDC", name="Room Dao"), scaling=Decimal("1e-18")
    ),
    "0x8400d94a5cb0fa0d041a3788e395285d61c9ee5e": TokenInfo(
        currency=CurrencyInfo(symbol="UBT", name="Unibright"), scaling=Decimal("1e-8")
    ),
    "0x840fe75abfadc0f2d54037829571b2782e919ce4": TokenInfo(
        currency=CurrencyInfo(symbol="WEB", name="Webcoin"), scaling=Decimal("1e-18")
    ),
    "0x84119cb33e8f590d75c2d6ea4e6b0741a7494eda": TokenInfo(
        currency=CurrencyInfo(symbol="WTT", name="Giga Watt Token"), scaling=Decimal("1e-0")
    ),
    "0x8427760a577f7f2f91a7ba7a3c7826c92a950727": TokenInfo(
        currency=CurrencyInfo(symbol="IDX", name="Indonesian eXchange"), scaling=Decimal("1e-8")
    ),
    "0x84294fc9710e1252d407d3d80a84bc39001bd4a8": TokenInfo(
        currency=CurrencyInfo(symbol="NUTS", name="Squirrel Finance"), scaling=Decimal("1e-18")
    ),
    "0x8430acfd193271d004ac0f0825b95e6a382eeb22": TokenInfo(
        currency=CurrencyInfo(symbol="E01", name="Eleven01"), scaling=Decimal("1e-18")
    ),
    "0x843131b15f2ec5bea850ac5164d2e4a3749ad87f": TokenInfo(
        currency=CurrencyInfo(symbol="WOW", name="WowSecret"), scaling=Decimal("1e-18")
    ),
    "0x843c9af34f698618f90c898e3967278a260c8d9a": TokenInfo(
        currency=CurrencyInfo(symbol="AGS", name="Silver Standard"), scaling=Decimal("1e-4")
    ),
    "0x84543f868ec1b1fac510d49d13c069f64cd2d5f9": TokenInfo(
        currency=CurrencyInfo(symbol="Hdp.ф", name="HEdpAY"), scaling=Decimal("1e-18")
    ),
    "0x845838df265dcd2c412a1dc9e959c7d08537f8a2": TokenInfo(
        currency=CurrencyInfo(symbol="CCURVE", name="LP-cCurve"), scaling=Decimal("1e-18")
    ),
    "0x846c66cf71c43f80403b51fe3906b3599d63336f": TokenInfo(
        currency=CurrencyInfo(symbol="PMA", name="PumaPay"), scaling=Decimal("1e-18")
    ),
    "0x84841e552a021224de716b7be89747bb2d62d642": TokenInfo(
        currency=CurrencyInfo(symbol="uSD", name="uniswap State Dollar"), scaling=Decimal("1e-18")
    ),
    "0x84936cf7630aa3e27dd9aff968b140d5aee49f5a": TokenInfo(
        currency=CurrencyInfo(symbol="AMTC", name="AmberTime Coin"), scaling=Decimal("1e-8")
    ),
    "0x84bd083b1c8bf929f39c98bc17cf518f40154f58": TokenInfo(
        currency=CurrencyInfo(symbol="MARIO-CASH-JAN-2021", name="Mario Cash Synthetic Token Expiring 15 January 2021"),
        scaling=Decimal("1e-18"),
    ),
    "0x84c722e6f1363e8d5c6db3ea600bef9a006da824": TokenInfo(
        currency=CurrencyInfo(symbol="MSB", name="Misbloc"), scaling=Decimal("1e-18")
    ),
    "0x84ca8bc7997272c7cfb4d0cd3d55cd942b3c9419": TokenInfo(
        currency=CurrencyInfo(symbol="DIA", name="DIA"), scaling=Decimal("1e-18")
    ),
    "0x84e8a50ca43e8f26094799ba60705475cf2b9832": TokenInfo(
        currency=CurrencyInfo(symbol="EBLX", name="Bullion Exchange"), scaling=Decimal("1e-8")
    ),
    "0x84f43821c73da781a7c440c3ca1a50e1013f7219": TokenInfo(
        currency=CurrencyInfo(symbol="CGMT", name="ClickGem Token"), scaling=Decimal("1e-8")
    ),
    "0x84f710bae3316a74fb0fcb01904d2578a4cc6a26": TokenInfo(
        currency=CurrencyInfo(symbol="PPC", name="PHILLIPS PAY COIN"), scaling=Decimal("1e-1")
    ),
    "0x84f7c44b6fed1080f647e354d552595be2cc602f": TokenInfo(
        currency=CurrencyInfo(symbol="BBO", name="Bigbom"), scaling=Decimal("1e-18")
    ),
    "0x84fe25f3921f3426395c883707950d0c00367576": TokenInfo(
        currency=CurrencyInfo(symbol="INX", name="Insight Protocol"), scaling=Decimal("1e-18")
    ),
    "0x85089389c14bd9c77fc2b8f0c3d1dc3363bf06ef": TokenInfo(
        currency=CurrencyInfo(symbol="SPF", name="SportyCo"), scaling=Decimal("1e-18")
    ),
    "0x850aab69f0e0171a9a49db8be3e71351c8247df4": TokenInfo(
        currency=CurrencyInfo(symbol="KONO", name="Konomi Network"), scaling=Decimal("1e-18")
    ),
    "0x851017523ae205adc9195e7f97d029f4cfe7794c": TokenInfo(
        currency=CurrencyInfo(symbol="SLT", name="Social Lending Token"), scaling=Decimal("1e-9")
    ),
    "0x8511dc1dece6faf58f696aac265fef18da7d7a05": TokenInfo(
        currency=CurrencyInfo(symbol="TGBP", name="TrueGBP"), scaling=Decimal("1e-18")
    ),
    "0x8515cd0f00ad81996d24b9a9c35121a3b759d6cd": TokenInfo(
        currency=CurrencyInfo(symbol="BURN", name="BlockBurn"), scaling=Decimal("1e-18")
    ),
    "0x853d955acef822db058eb8505911ed77f175b99e": TokenInfo(
        currency=CurrencyInfo(symbol="FRAX", name="Frax"), scaling=Decimal("1e-18")
    ),
    "0x8542325b72c6d9fc0ad2ca965a78435413a915a0": TokenInfo(
        currency=CurrencyInfo(symbol="SHL", name="Oyster Shell"), scaling=Decimal("1e-18")
    ),
    "0x8564653879a18c560e7c0ea0e084c516c62f5653": TokenInfo(
        currency=CurrencyInfo(symbol="UBXT", name="UpBots"), scaling=Decimal("1e-18")
    ),
    "0x856c4388c56c2a613c60507a4701af627157fed6": TokenInfo(
        currency=CurrencyInfo(symbol="ETAS", name="ETH Trending Alpha ST Set II"), scaling=Decimal("1e-18")
    ),
    "0x856e19b3ce92dde6892290c48204aade2f9c3ea0": TokenInfo(
        currency=CurrencyInfo(symbol="BHG", name="Bit Global Payment Ecology"), scaling=Decimal("1e-8")
    ),
    "0x8578530205cecbe5db83f7f29ecfeec860c297c2": TokenInfo(
        currency=CurrencyInfo(symbol="AOG", name="smARTOFGIVING"), scaling=Decimal("1e-18")
    ),
    "0x85954c0adde80c73b019a92c08e0d22f16ac4067": TokenInfo(
        currency=CurrencyInfo(symbol="CERT", name="Certified Carbon Emission Transaction"), scaling=Decimal("1e-18")
    ),
    "0x859a9c0b44cb7066d956a958b0b82e54c9e44b4b": TokenInfo(
        currency=CurrencyInfo(symbol="iETH", name="iEthereum"), scaling=Decimal("1e-8")
    ),
    "0x85c4edc43724e954e5849caaab61a26a9cb65f1b": TokenInfo(
        currency=CurrencyInfo(symbol="BBCH", name="Binance Wrapped BCH"), scaling=Decimal("1e-8")
    ),
    "0x85ca6710d0f1d511d130f6935edda88acbd921bd": TokenInfo(
        currency=CurrencyInfo(symbol="PLG", name="Pledgecamp"), scaling=Decimal("1e-18")
    ),
    "0x85cf3e1e9854a6aace2dd595e82aa9eea4459a2a": TokenInfo(
        currency=CurrencyInfo(symbol="XPD.CX", name="Palladium Spot"), scaling=Decimal("1e-8")
    ),
    "0x85e076361cc813a908ff672f9bad1541474402b2": TokenInfo(
        currency=CurrencyInfo(symbol="TEL", name="Telcoin"), scaling=Decimal("1e-2")
    ),
    "0x85eee30c52b0b379b046fb0f85f4f3dc3009afec": TokenInfo(
        currency=CurrencyInfo(symbol="KEEP", name="Keep Network"), scaling=Decimal("1e-18")
    ),
    "0x85f6eb2bd5a062f5f8560be93fb7147e16c81472": TokenInfo(
        currency=CurrencyInfo(symbol="FLY", name="Franklin"), scaling=Decimal("1e-4")
    ),
    "0x8606a8f28e1e2fd50b9074d65c01548b1f040b32": TokenInfo(
        currency=CurrencyInfo(symbol="CTRT", name="Cryptrust"), scaling=Decimal("1e-8")
    ),
    "0x86225481747c774b24c7c3bac4c1b7382f787c7f": TokenInfo(
        currency=CurrencyInfo(symbol="WXC", name="WIIX Coin"), scaling=Decimal("1e-18")
    ),
    "0x8633e144f2d9b9b8bdd12ddb58e4bef1e163a0ce": TokenInfo(
        currency=CurrencyInfo(symbol="YEL", name="Yellow Token"), scaling=Decimal("1e-18")
    ),
    "0x86367c0e517622dacdab379f2de389c3c9524345": TokenInfo(
        currency=CurrencyInfo(symbol="UPUSD", name="Universal US Dollar"), scaling=Decimal("1e-2")
    ),
    "0x8642a849d0dcb7a15a974794668adcfbe4794b56": TokenInfo(
        currency=CurrencyInfo(symbol="PROS", name="Prosper"), scaling=Decimal("1e-18")
    ),
    "0x865377367054516e17014ccded1e7d814edc9ce4": TokenInfo(
        currency=CurrencyInfo(symbol="DOLA", name="Dola USD Stablecoin"), scaling=Decimal("1e-18")
    ),
    "0x865bfd8232778f00cae81315bf75ef1fe6e30cdd": TokenInfo(
        currency=CurrencyInfo(symbol="ABLX", name="ABLE X Token"), scaling=Decimal("1e-18")
    ),
    "0x865d176351f287fe1b0010805b110d08699c200a": TokenInfo(
        currency=CurrencyInfo(symbol="BCO", name="BananaCoin"), scaling=Decimal("1e-8")
    ),
    "0x865e3707a580f9db89304005cddd050ade8873eb": TokenInfo(
        currency=CurrencyInfo(symbol="HIRE", name="HireMatch"), scaling=Decimal("1e-18")
    ),
    "0x865ec58b06bf6305b886793aa20a2da31d034e68": TokenInfo(
        currency=CurrencyInfo(symbol="MOC", name="Mossland"), scaling=Decimal("1e-18")
    ),
    "0x86696431d6aca9bae5ce6536ecf5d437f2e6dba2": TokenInfo(
        currency=CurrencyInfo(symbol="SCC", name="SoftChain"), scaling=Decimal("1e-18")
    ),
    "0x867072d6245467edfdbd0fc8e9f2bf0701f40f94": TokenInfo(
        currency=CurrencyInfo(symbol="cyUSD", name="CreamY USD"), scaling=Decimal("1e-18")
    ),
    "0x86772b1409b61c639eaac9ba0acfbb6e238e5f83": TokenInfo(
        currency=CurrencyInfo(symbol="NDX", name="Indexed Finance"), scaling=Decimal("1e-18")
    ),
    "0x8678b5fb41d87f4bec43b3142bce852366100336": TokenInfo(
        currency=CurrencyInfo(symbol="GOT", name="GOeureka"), scaling=Decimal("1e-18")
    ),
    "0x86807da5b92d31f67e128771cacb85f3579646ea": TokenInfo(
        currency=CurrencyInfo(symbol="TRXBEAR", name="3X Short TRX Token"), scaling=Decimal("1e-18")
    ),
    "0x868277d475e0e475e38ec5cda2d9c83b5e1d9fc8": TokenInfo(
        currency=CurrencyInfo(symbol="DUSDT", name="dForce USDT"), scaling=Decimal("1e-6")
    ),
    "0x868ab6c9e560ff70584b9770d1bd1b961ad09d82": TokenInfo(
        currency=CurrencyInfo(symbol="SUPT", name="Super Trip Chain"), scaling=Decimal("1e-8")
    ),
    "0x86949dc8043a5fd7619a1289d65964ad5ec3d25c": TokenInfo(
        currency=CurrencyInfo(symbol="GCS", name="GameChain System"), scaling=Decimal("1e-8")
    ),
    "0x8694ee05b45c9fe1058ce532de8dbcf1d84a4154": TokenInfo(
        currency=CurrencyInfo(symbol="TFC", name="Treasure Financial Coin"), scaling=Decimal("1e-5")
    ),
    "0x86965a86539e2446f9e72634cefca7983cc21a81": TokenInfo(
        currency=CurrencyInfo(symbol="YFIS", name="YFISCURITY"), scaling=Decimal("1e-18")
    ),
    "0x86a0835f6b49f633fb1a3fa91b30dae1af4bbb6b": TokenInfo(
        currency=CurrencyInfo(symbol="SOG", name="SOULGAME"), scaling=Decimal("1e-18")
    ),
    "0x86a63063b3a60652fb070f23cbb4a9833fdbbff8": TokenInfo(
        currency=CurrencyInfo(symbol="HDLRE", name="Hodler Mining"), scaling=Decimal("1e-18")
    ),
    "0x86aa993fdb0a60c2d548256a862258ab5d352fab": TokenInfo(
        currency=CurrencyInfo(symbol="CHIP", name="ChipCoin"), scaling=Decimal("1e-18")
    ),
    "0x86b9018bd65629e047d4bee2a96cbea8931d6ea1": TokenInfo(
        currency=CurrencyInfo(symbol="PWZ", name="Powerlight"), scaling=Decimal("1e-18")
    ),
    "0x86b9d8b2491cd816b1b26ad2afc5c267126c0c34": TokenInfo(
        currency=CurrencyInfo(symbol="TCOIN", name="Corona Time Coins"), scaling=Decimal("1e-8")
    ),
    "0x86c2752f8fe2c6679a942c8ee6c785c28f42cd55": TokenInfo(
        currency=CurrencyInfo(symbol="BMT", name="BitMinutes"), scaling=Decimal("1e-18")
    ),
    "0x86c31e6da2190a1ffd39a36990a44174d0a8be15": TokenInfo(
        currency=CurrencyInfo(symbol="VIX", name="VianeX"), scaling=Decimal("1e-18")
    ),
    "0x86dd3002bf215082ea43b0bd2fd595ece4341880": TokenInfo(
        currency=CurrencyInfo(symbol="VIO", name="VIOToken"), scaling=Decimal("1e-18")
    ),
    "0x86e44543164d9b97b14ef7f6f3ab7ba670cab346": TokenInfo(
        currency=CurrencyInfo(symbol="QUIN", name="QUINADS"), scaling=Decimal("1e-18")
    ),
    "0x86e6a4f512b1290c043970b04e0b570d4fc98291": TokenInfo(
        currency=CurrencyInfo(symbol="INE", name="IntelliShare"), scaling=Decimal("1e-18")
    ),
    "0x86eb791495be777db763142a2c547d1112554fb8": TokenInfo(
        currency=CurrencyInfo(symbol="HTBEAR", name="3X Short Huobi Token Token"), scaling=Decimal("1e-18")
    ),
    "0x86ed939b500e121c0c5f493f399084db596dad20": TokenInfo(
        currency=CurrencyInfo(symbol="SPC", name="SpaceChain (ERC-20)"), scaling=Decimal("1e-18")
    ),
    "0x86f654cebb9bae068d0c4398d1e337b351e6523b": TokenInfo(
        currency=CurrencyInfo(symbol="Pigx", name="Pigx"), scaling=Decimal("1e-18")
    ),
    "0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0": TokenInfo(
        currency=CurrencyInfo(symbol="EOS", name="EOS"), scaling=Decimal("1e-18")
    ),
    "0x87026f792d09960232ca406e80c89bd35bafe566": TokenInfo(
        currency=CurrencyInfo(symbol="CDC", name="Commerce Data Connection"), scaling=Decimal("1e-18")
    ),
    "0x87047986e8e4961c11d2edcd94285e3a1331d97b": TokenInfo(
        currency=CurrencyInfo(symbol="YKZ", name="Yakuza DFO"), scaling=Decimal("1e-18")
    ),
    "0x8711cf7764d23d32092c0dcedfdac63ece1e6cf3": TokenInfo(
        currency=CurrencyInfo(symbol="TXL", name="Textile"), scaling=Decimal("1e-18")
    ),
    "0x8713d26637cf49e1b6b4a7ce57106aabc9325343": TokenInfo(
        currency=CurrencyInfo(symbol="CNN", name="Content Neutrality Network"), scaling=Decimal("1e-18")
    ),
    "0x8716fc5da009d3a208f0178b637a50f4ef42400f": TokenInfo(
        currency=CurrencyInfo(symbol="UGAS", name="Ultrain"), scaling=Decimal("1e-18")
    ),
    "0x871baed4088b863fd6407159f3672d70cd34837d": TokenInfo(
        currency=CurrencyInfo(symbol="ETHBULL", name="3X Long Ethereum Token"), scaling=Decimal("1e-18")
    ),
    "0x87210f1d3422ba75b6c40c63c78d79324dabcd55": TokenInfo(
        currency=CurrencyInfo(symbol="EOST", name="EOS TRUST"), scaling=Decimal("1e-18")
    ),
    "0x8727c112c712c4a03371ac87a74dd6ab104af768": TokenInfo(
        currency=CurrencyInfo(symbol="JET", name="Jetcoin"), scaling=Decimal("1e-18")
    ),
    "0x874d4c9b980f1a13dd44cbcdb912e24ef0671ed0": TokenInfo(
        currency=CurrencyInfo(symbol="GDR", name="Guider"), scaling=Decimal("1e-18")
    ),
    "0x875089a734213ca39f0d93c2bbb8209827ec5e9f": TokenInfo(
        currency=CurrencyInfo(symbol="EPH", name="Euphoria"), scaling=Decimal("1e-8")
    ),
    "0x875773784af8135ea0ef43b5a374aad105c5d39e": TokenInfo(
        currency=CurrencyInfo(symbol="IDLE", name="IDLE"), scaling=Decimal("1e-18")
    ),
    "0x875ef445e0873b6c2d5e58f68113e0937ba8a441": TokenInfo(
        currency=CurrencyInfo(symbol="BSVMOON", name="10X Long Bitcoin SV Token"), scaling=Decimal("1e-18")
    ),
    "0x8762db106b2c2a0bccb3a80d1ed41273552616e8": TokenInfo(
        currency=CurrencyInfo(symbol="RSR", name="Reserve Rights Token"), scaling=Decimal("1e-18")
    ),
    "0x877c7deb5eb1fc5faad30c71e3a6e39dc8b1519f": TokenInfo(
        currency=CurrencyInfo(symbol="HB", name="HeartBout"), scaling=Decimal("1e-18")
    ),
    "0x877f2558cdfe1953606ac8c13ba262007ffd8f1e": TokenInfo(
        currency=CurrencyInfo(symbol="OAS", name="OAS Chain"), scaling=Decimal("1e-18")
    ),
    "0x8798249c2e607446efb7ad49ec89dd1865ff4272": TokenInfo(
        currency=CurrencyInfo(symbol="XSUSHI", name="xSUSHI"), scaling=Decimal("1e-18")
    ),
    "0x87b008e57f640d94ee44fd893f0323af933f9195": TokenInfo(
        currency=CurrencyInfo(symbol="COIN", name="Coin Artist"), scaling=Decimal("1e-18")
    ),
    "0x87b87a7583d8d8f15b58bdd290318386ac8ee174": TokenInfo(
        currency=CurrencyInfo(symbol="DGW", name="Digiwill"), scaling=Decimal("1e-18")
    ),
    "0x87c00817abe35ed4c093e59043fae488238d2f74": TokenInfo(
        currency=CurrencyInfo(symbol="YNK", name="Yoink"), scaling=Decimal("1e-18")
    ),
    "0x87c4bd3038176301e81e6682ce51a6fdaefabd0c": TokenInfo(
        currency=CurrencyInfo(symbol="PFID", name="Pofid Dao"), scaling=Decimal("1e-18")
    ),
    "0x87cdc02f0812f08cd50f946793706fad9c265e2d": TokenInfo(
        currency=CurrencyInfo(symbol="SANA", name="Storage Area Networ"), scaling=Decimal("1e-16")
    ),
    "0x87d73e916d7057945c9bcd8cdd94e42a6f47f776": TokenInfo(
        currency=CurrencyInfo(symbol="NFTX", name="NFTX"), scaling=Decimal("1e-18")
    ),
    "0x87de305311d5788e8da38d19bb427645b09cb4e5": TokenInfo(
        currency=CurrencyInfo(symbol="VRX", name="Verox"), scaling=Decimal("1e-18")
    ),
    "0x87def9265b40ba7f867f73d4af519cd9f074bed6": TokenInfo(
        currency=CurrencyInfo(symbol="OBSR", name="OBSR"), scaling=Decimal("1e-8")
    ),
    "0x87edffde3e14c7a66c9b9724747a1c5696b742e6": TokenInfo(
        currency=CurrencyInfo(symbol="SWAG", name="SWAG Finance"), scaling=Decimal("1e-18")
    ),
    "0x87f14e9460cecb789f1b125b2e3e353ff8ed6fcd": TokenInfo(
        currency=CurrencyInfo(symbol="BYTS", name="Bytus"), scaling=Decimal("1e-3")
    ),
    "0x87f56ee356b434187105b40f96b230f5283c0ab4": TokenInfo(
        currency=CurrencyInfo(symbol="PITCH", name="Pitch"), scaling=Decimal("1e-9")
    ),
    "0x87f5e8c3425218837f3cb67db941af0c01323e56": TokenInfo(
        currency=CurrencyInfo(symbol="BTCONE", name="BitCoin One"), scaling=Decimal("1e-18")
    ),
    "0x8806926ab68eb5a7b909dcaf6fdbe5d93271d6e2": TokenInfo(
        currency=CurrencyInfo(symbol="UQC", name="Uquid Coin"), scaling=Decimal("1e-18")
    ),
    "0x88093840aad42d2621e1a452bf5d7076ff804d61": TokenInfo(
        currency=CurrencyInfo(symbol="SYFI", name="Soft Yearn Finance"), scaling=Decimal("1e-9")
    ),
    "0x8810c63470d38639954c6b41aac545848c46484a": TokenInfo(
        currency=CurrencyInfo(symbol="ADI", name="Aditus"), scaling=Decimal("1e-18")
    ),
    "0x8811e4dd5ec5eb8764b97cc814b1339089717ada": TokenInfo(
        currency=CurrencyInfo(symbol="BITH", name="Bithachi"), scaling=Decimal("1e-8")
    ),
    "0x881a7e25d44591c467a37da96adf3c3705e7251b": TokenInfo(
        currency=CurrencyInfo(symbol="ELYX", name="Elynet Token"), scaling=Decimal("1e-18")
    ),
    "0x881e1344eee25ce7de2f4857ba86b04df8f77bea": TokenInfo(
        currency=CurrencyInfo(symbol="VTCH", name="VertcoinCash"), scaling=Decimal("1e-18")
    ),
    "0x881ef48211982d01e2cb7092c915e647cd40d85c": TokenInfo(
        currency=CurrencyInfo(symbol="OTN", name="Open Trading Network"), scaling=Decimal("1e-18")
    ),
    "0x882448f83d90b2bf477af2ea79327fdea1335d93": TokenInfo(
        currency=CurrencyInfo(symbol="VIBEX", name="VIBEX Exchange Token"), scaling=Decimal("1e-18")
    ),
    "0x8832e23b1135f78ad08a044c2550489eea1e1098": TokenInfo(
        currency=CurrencyInfo(symbol="2248", name="2+2=4+4=8"), scaling=Decimal("1e-8")
    ),
    "0x8837ad911818d61def3c65c199c06b5706f95364": TokenInfo(
        currency=CurrencyInfo(symbol="0241.CX", name="Alibaba Health Information Technology Limited"),
        scaling=Decimal("1e-8"),
    ),
    "0x883a158c9b28f8d626acfcfbe1028f49e70c9d75": TokenInfo(
        currency=CurrencyInfo(symbol="CNG", name="CNG Casino"), scaling=Decimal("1e-18")
    ),
    "0x884181554dfa9e578d36379919c05c25dc4a15bb": TokenInfo(
        currency=CurrencyInfo(symbol="GENE", name="Gene Source Code Token"), scaling=Decimal("1e-18")
    ),
    "0x884e3902c4d5cfa86de4ace7a96aa91ebc25c0ff": TokenInfo(
        currency=CurrencyInfo(symbol="JBX", name="JBOX"), scaling=Decimal("1e-18")
    ),
    "0x885e127aba09bf8fae058a2895c221b37697c9be": TokenInfo(
        currency=CurrencyInfo(symbol="AceD", name="AceD"), scaling=Decimal("1e-18")
    ),
    "0x8869b1f9bc8b246a4d7220f834e56ddfdd8255e7": TokenInfo(
        currency=CurrencyInfo(symbol="ECP", name="ECrypto Coin"), scaling=Decimal("1e-18")
    ),
    "0x887168120cb89fb06f3e74dc4af20d67df0977f6": TokenInfo(
        currency=CurrencyInfo(symbol="SKRT", name="Sekuritance"), scaling=Decimal("1e-18")
    ),
    "0x887834d3b8d450b6bab109c252df3da286d73ce4": TokenInfo(
        currency=CurrencyInfo(symbol="ATT", name="Atmatrix Token"), scaling=Decimal("1e-18")
    ),
    "0x888666ca69e0f178ded6d75b5726cee99a87d698": TokenInfo(
        currency=CurrencyInfo(symbol="ICN", name="Iconomi"), scaling=Decimal("1e-18")
    ),
    "0x8888801af4d980682e47f1a9036e589479e835c5": TokenInfo(
        currency=CurrencyInfo(symbol="MPH", name="88mph"), scaling=Decimal("1e-18")
    ),
    "0x888888435fde8e7d4c54cab67f206e4199454c60": TokenInfo(
        currency=CurrencyInfo(symbol="DFX", name="DFX Finance"), scaling=Decimal("1e-18")
    ),
    "0x888888848b652b3e3a0f34c96e00eec0f3a23f72": TokenInfo(
        currency=CurrencyInfo(symbol="TLM", name="Alien Worlds"), scaling=Decimal("1e-4")
    ),
    "0x888888888889c00c67689029d7856aac1065ec11": TokenInfo(
        currency=CurrencyInfo(symbol="OPIUM", name="Opium"), scaling=Decimal("1e-18")
    ),
    "0x8888889213dd4da823ebdd1e235b09590633c150": TokenInfo(
        currency=CurrencyInfo(symbol="MBC", name="Marblecoin"), scaling=Decimal("1e-18")
    ),
    "0x889bc62e94bb6902d022bb82b38f7fcd637df28c": TokenInfo(
        currency=CurrencyInfo(symbol="OKBHEDGE", name="1X Short OKB Token"), scaling=Decimal("1e-18")
    ),
    "0x889efb523cc39590b8483eb9491890ac71407f64": TokenInfo(
        currency=CurrencyInfo(symbol="JUICE", name="Moon Juice"), scaling=Decimal("1e-18")
    ),
    "0x88a3e4f35d64aad41a6d4030ac9afe4356cb84fa": TokenInfo(
        currency=CurrencyInfo(symbol="PRE", name="Presearch"), scaling=Decimal("1e-18")
    ),
    "0x88a9a52f944315d5b4e917b9689e65445c401e83": TokenInfo(
        currency=CurrencyInfo(symbol="FEAR", name="Fear"), scaling=Decimal("1e-18")
    ),
    "0x88ac94d5d175130347fc95e109d77ac09dbf5ab7": TokenInfo(
        currency=CurrencyInfo(symbol="HKY", name="HKY Token"), scaling=Decimal("1e-18")
    ),
    "0x88acdd2a6425c3faae4bc9650fd7e27e0bebb7ab": TokenInfo(
        currency=CurrencyInfo(symbol="MIST", name="Alchemist"), scaling=Decimal("1e-18")
    ),
    "0x88ae96845e157558ef59e9ff90e766e22e480390": TokenInfo(
        currency=CurrencyInfo(symbol="IKB", name="Digital Zone of Immaterial Pictorial Sensibility"),
        scaling=Decimal("1e-0"),
    ),
    "0x88c8cf3a212c0369698d13fe98fcb76620389841": TokenInfo(
        currency=CurrencyInfo(symbol="SEOS", name="sEOS"), scaling=Decimal("1e-18")
    ),
    "0x88cb253d4c8cab8cdf7948a9251db85a13669e23": TokenInfo(
        currency=CurrencyInfo(symbol="YLDY", name="Yieldly"), scaling=Decimal("1e-18")
    ),
    "0x88d50b466be55222019d71f9e8fae17f5f45fca1": TokenInfo(
        currency=CurrencyInfo(symbol="CPT", name="Cryptaur"), scaling=Decimal("1e-8")
    ),
    "0x88d59ba796fdf639ded3b5e720988d59fdb71eb8": TokenInfo(
        currency=CurrencyInfo(symbol="PSHP", name="Payship"), scaling=Decimal("1e-18")
    ),
    "0x88df592f8eb5d7bd38bfef7deb0fbc02cf3778a0": TokenInfo(
        currency=CurrencyInfo(symbol="TRB", name="Tellor"), scaling=Decimal("1e-18")
    ),
    "0x88ef27e69108b2633f8e1c184cc37940a075cc02": TokenInfo(
        currency=CurrencyInfo(symbol="DEGO", name="Dego Finance"), scaling=Decimal("1e-18")
    ),
    "0x88f400f6a26465c9ac6ae5c1c8c14cf12b515c96": TokenInfo(
        currency=CurrencyInfo(symbol="VIRUS", name="Virus Token"), scaling=Decimal("1e-9")
    ),
    "0x88fcfbc22c6d3dbaa25af478c578978339bde77a": TokenInfo(
        currency=CurrencyInfo(symbol="KAT", name="Katalyse"), scaling=Decimal("1e-18")
    ),
    "0x8901bed88a57db0eae2bb87d72ced14c6c91164b": TokenInfo(
        currency=CurrencyInfo(symbol="YFIP", name="YFI Product Token"), scaling=Decimal("1e-18")
    ),
    "0x89020f0d5c5af4f3407eb5fe185416c457b0e93e": TokenInfo(
        currency=CurrencyInfo(symbol="EDN", name="Edenchain"), scaling=Decimal("1e-18")
    ),
    "0x8903e8f101d86ea097efe104a3d53f4c42cb44bc": TokenInfo(
        currency=CurrencyInfo(symbol="ICY", name="ICURY"), scaling=Decimal("1e-18")
    ),
    "0x89205a3a3b2a69de6dbf7f01ed13b2108b2c43e7": TokenInfo(
        currency=CurrencyInfo(symbol="🦄", name="Unicorns"), scaling=Decimal("1e-0")
    ),
    "0x892a6f9df0147e5f079b0993f486f9aca3c87881": TokenInfo(
        currency=CurrencyInfo(symbol="XFUND", name="xFund"), scaling=Decimal("1e-9")
    ),
    "0x892b14321a4fcba80669ae30bd0cd99a7ecf6ac0": TokenInfo(
        currency=CurrencyInfo(symbol="crCREAM", name="Cream Cream"), scaling=Decimal("1e-8")
    ),
    "0x89303500a7abfb178b274fd89f2469c264951e1f": TokenInfo(
        currency=CurrencyInfo(symbol="REF", name="RefToken"), scaling=Decimal("1e-8")
    ),
    "0x8933ea1ce67b946bdf2436ce860ffbb53ce814d2": TokenInfo(
        currency=CurrencyInfo(symbol="LINKETHRSI", name="LINK/ETH RSI Ratio Trading Set"), scaling=Decimal("1e-18")
    ),
    "0x895311ca2eb28bd839dcfe63c542304aad1bb3c3": TokenInfo(
        currency=CurrencyInfo(symbol="RH.CX", name="Rh"), scaling=Decimal("1e-8")
    ),
    "0x89700d6cd7b77d1f52c29ca776a1eae313320fc5": TokenInfo(
        currency=CurrencyInfo(symbol="PMD", name="Pyramid"), scaling=Decimal("1e-18")
    ),
    "0x8971f9fd7196e5cee2c1032b50f656855af7dd26": TokenInfo(
        currency=CurrencyInfo(symbol="LAMB", name="Lambda"), scaling=Decimal("1e-18")
    ),
    "0x899338b84d25ac505a332adce7402d697d947494": TokenInfo(
        currency=CurrencyInfo(symbol="WIN", name="WCOIN"), scaling=Decimal("1e-8")
    ),
    "0x89ab32156e46f46d02ade3fecbe5fc4243b9aaed": TokenInfo(
        currency=CurrencyInfo(symbol="PNT", name="pNetwork"), scaling=Decimal("1e-18")
    ),
    "0x89c6c856a6db3e46107163d0cda7a7ff211bd655": TokenInfo(
        currency=CurrencyInfo(symbol="DEC2", name="Darico Ecosystem Coin"), scaling=Decimal("1e-18")
    ),
    "0x89cbeac5e8a13f0ebb4c74fadfc69be81a501106": TokenInfo(
        currency=CurrencyInfo(symbol="DEPO", name="Depository Network Token"), scaling=Decimal("1e-18")
    ),
    "0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359": TokenInfo(
        currency=CurrencyInfo(symbol="SAI", name="Sai"), scaling=Decimal("1e-18")
    ),
    "0x89d3c0249307ae570a316030764d12f53bb191fd": TokenInfo(
        currency=CurrencyInfo(symbol="XGC", name="Xiglute Coin"), scaling=Decimal("1e-14")
    ),
    "0x89ee58af4871b474c30001982c3d7439c933c838": TokenInfo(
        currency=CurrencyInfo(symbol="YFBETA", name="yfBeta"), scaling=Decimal("1e-18")
    ),
    "0x8a187d5285d316bcbc9adafc08b51d70a0d8e000": TokenInfo(
        currency=CurrencyInfo(symbol="SIFT", name="Smart Investment Fund Token"), scaling=Decimal("1e-0")
    ),
    "0x8a1a9477a710d470575b1da335e524b27e8091ab": TokenInfo(
        currency=CurrencyInfo(symbol="COI", name="Coinnec"), scaling=Decimal("1e-18")
    ),
    "0x8a2279d4a90b6fe1c4b30fa660cc9f926797baa2": TokenInfo(
        currency=CurrencyInfo(symbol="CHR", name="Chromia"), scaling=Decimal("1e-6")
    ),
    "0x8a2a3f3ffb78880838f9d7603601f837f72c2ec9": TokenInfo(
        currency=CurrencyInfo(symbol="GBX", name="G-BOX Coin"), scaling=Decimal("1e-18")
    ),
    "0x8a3d77e9d6968b780564936d15b09805827c21fa": TokenInfo(
        currency=CurrencyInfo(symbol="UCO", name="Uniris"), scaling=Decimal("1e-18")
    ),
    "0x8a3e08353e3c64d9fa5683bb5e2fbbf8aef7e7e9": TokenInfo(
        currency=CurrencyInfo(symbol="CNMC", name="Agricultural ecological chain"), scaling=Decimal("1e-18")
    ),
    "0x8a40c222996f9f3431f63bf80244c36822060f12": TokenInfo(
        currency=CurrencyInfo(symbol="FXF", name="Finxflo"), scaling=Decimal("1e-18")
    ),
    "0x8a4491936a8e5a1662c8a755932b83dbe9634b0d": TokenInfo(
        currency=CurrencyInfo(symbol="OG", name="One Genesis"), scaling=Decimal("1e-18")
    ),
    "0x8a5ad873a1a615001acc1757214f67e1ba145cc9": TokenInfo(
        currency=CurrencyInfo(symbol="HBIT", name="HeartBeat"), scaling=Decimal("1e-18")
    ),
    "0x8a63be90f095f6777be3ed25d9fc7cd2a63ddb30": TokenInfo(
        currency=CurrencyInfo(symbol="LELOAP", name="LINK/ETH Long-Only Alpha Portfolio"), scaling=Decimal("1e-18")
    ),
    "0x8a65ab17324c155fac3e46ad33e9553d9165a252": TokenInfo(
        currency=CurrencyInfo(symbol="SCN", name="Silver Coin"), scaling=Decimal("1e-8")
    ),
    "0x8a6aca71a218301c7081d4e96d64292d3b275ce0": TokenInfo(
        currency=CurrencyInfo(symbol="SFG", name="S.Finance"), scaling=Decimal("1e-18")
    ),
    "0x8a6f3bf52a26a21531514e23016eeae8ba7e7018": TokenInfo(
        currency=CurrencyInfo(symbol="MXX", name="Multiplier"), scaling=Decimal("1e-8")
    ),
    "0x8a732bc91c33c167f868e0af7e6f31e0776d0f71": TokenInfo(
        currency=CurrencyInfo(symbol="LTK", name="Litecoin Token"), scaling=Decimal("1e-18")
    ),
    "0x8a77e40936bbc27e80e9a3f526368c967869c86d": TokenInfo(
        currency=CurrencyInfo(symbol="MVP", name="Merculet"), scaling=Decimal("1e-18")
    ),
    "0x8a7b7b9b2f7d0c63f66171721339705a6188a7d5": TokenInfo(
        currency=CurrencyInfo(symbol="EDOGE", name="EtherDoge"), scaling=Decimal("1e-18")
    ),
    "0x8a8079c7149b8a1611e5c5d978dca3be16545f83": TokenInfo(
        currency=CurrencyInfo(symbol="IADA", name="iADA"), scaling=Decimal("1e-18")
    ),
    "0x8a845fc339ceb022a695281554890429a34df120": TokenInfo(
        currency=CurrencyInfo(symbol="MGP", name="MangoChain"), scaling=Decimal("1e-18")
    ),
    "0x8a854288a5976036a725879164ca3e91d30c6a1b": TokenInfo(
        currency=CurrencyInfo(symbol="GET", name="GET Protocol"), scaling=Decimal("1e-18")
    ),
    "0x8a88f04e0c905054d2f33b26bb3a46d7091a039a": TokenInfo(
        currency=CurrencyInfo(symbol="IG", name="IGToken"), scaling=Decimal("1e-18")
    ),
    "0x8a91eecd3f6b6b7833fd6961e7f654c3d016a068": TokenInfo(
        currency=CurrencyInfo(symbol="WWX", name="Wowoo Exchange Token"), scaling=Decimal("1e-18")
    ),
    "0x8a95ca448a52c0adf0054bb3402dc5e09cd6b232": TokenInfo(
        currency=CurrencyInfo(symbol="CDL", name="Confideal"), scaling=Decimal("1e-18")
    ),
    "0x8a99ed8a1b204903ee46e733f2c1286f6d20b177": TokenInfo(
        currency=CurrencyInfo(symbol="NTO", name="Fujinto"), scaling=Decimal("1e-18")
    ),
    "0x8a9c67fee641579deba04928c4bc45f66e26343a": TokenInfo(
        currency=CurrencyInfo(symbol="JRT", name="Jarvis Reward Token"), scaling=Decimal("1e-18")
    ),
    "0x8a9e5032803ff0867f5c58e08d268c089f57cbb5": TokenInfo(
        currency=CurrencyInfo(symbol="MSFT.CX", name="Microsoft"), scaling=Decimal("1e-8")
    ),
    "0x8aa33a7899fcc8ea5fbe6a608a109c3893a1b8b2": TokenInfo(
        currency=CurrencyInfo(symbol="BET", name="DAOBet"), scaling=Decimal("1e-18")
    ),
    "0x8aa688ab789d1848d131c65d98ceaa8875d97ef1": TokenInfo(
        currency=CurrencyInfo(symbol="MTV", name="MultiVAC"), scaling=Decimal("1e-18")
    ),
    "0x8ab0565dfe65bf9be754d7b0dadbb42c4ecaec01": TokenInfo(
        currency=CurrencyInfo(symbol="TLB", name="The Luxury Coin"), scaling=Decimal("1e-18")
    ),
    "0x8ab7404063ec4dbcfd4598215992dc3f8ec853d7": TokenInfo(
        currency=CurrencyInfo(symbol="AKRO", name="Akropolis"), scaling=Decimal("1e-18")
    ),
    "0x8ae4bf2c33a8e667de34b54938b0ccd03eb8cc06": TokenInfo(
        currency=CurrencyInfo(symbol="PTOY", name="Patientory"), scaling=Decimal("1e-8")
    ),
    "0x8ae56a6850a7cbeac3c3ab2cb311e7620167eac8": TokenInfo(
        currency=CurrencyInfo(symbol="PEG", name="PEG Network Token"), scaling=Decimal("1e-18")
    ),
    "0x8aedb297fed4b6884b808ee61faf0837713670d0": TokenInfo(
        currency=CurrencyInfo(symbol="WMC", name="Wrapped MarbleCards"), scaling=Decimal("1e-18")
    ),
    "0x8aefc499a2b69d1a4ff77a3e7903792f4c3e80d8": TokenInfo(
        currency=CurrencyInfo(symbol="BSX.CX", name="Boston Scientific"), scaling=Decimal("1e-8")
    ),
    "0x8af17a6396c8f315f6b6dbc6aa686c85f9b3e554": TokenInfo(
        currency=CurrencyInfo(symbol="XTZBULL", name="3X Long Tezos Token"), scaling=Decimal("1e-18")
    ),
    "0x8af22fbdefe01b4dc7960ec04ec73e8502f4a6b0": TokenInfo(
        currency=CurrencyInfo(symbol="BKKG", name="Biokkoin"), scaling=Decimal("1e-8")
    ),
    "0x8af785687ee8d75114b028997c9ca36b5cc67bc4": TokenInfo(
        currency=CurrencyInfo(symbol="OKBBULL", name="3X Long OKB Token"), scaling=Decimal("1e-18")
    ),
    "0x8b0e42f366ba502d787bb134478adfae966c8798": TokenInfo(
        currency=CurrencyInfo(symbol="LABS", name="LABS Group"), scaling=Decimal("1e-18")
    ),
    "0x8b1f49491477e0fb46a29fef53f1ea320d13c349": TokenInfo(
        currency=CurrencyInfo(symbol="AMM", name="MicroMoney"), scaling=Decimal("1e-6")
    ),
    "0x8b342d2de85cd4f6e206e7b8d777029c13ec213f": TokenInfo(
        currency=CurrencyInfo(symbol="GANA", name="GANA"), scaling=Decimal("1e-18")
    ),
    "0x8b353021189375591723e7384262f45709a3c3dc": TokenInfo(
        currency=CurrencyInfo(symbol="TOMO", name="Tomocoin"), scaling=Decimal("1e-18")
    ),
    "0x8b3870df408ff4d7c3a26df852d41034eda11d81": TokenInfo(
        currency=CurrencyInfo(symbol="IOI", name="IOI Token"), scaling=Decimal("1e-6")
    ),
    "0x8b39b70e39aa811b69365398e0aace9bee238aeb": TokenInfo(
        currency=CurrencyInfo(symbol="PKF", name="PolkaFoundry"), scaling=Decimal("1e-18")
    ),
    "0x8b40761142b9aa6dc8964e61d0585995425c3d94": TokenInfo(
        currency=CurrencyInfo(symbol="TRIO", name="Tripio"), scaling=Decimal("1e-18")
    ),
    "0x8b47b1698625d0734022de17afc2457d35205e87": TokenInfo(
        currency=CurrencyInfo(symbol="DLTR.CX", name="Dollar Tree Inc"), scaling=Decimal("1e-8")
    ),
    "0x8b4f0e7df51a49f18e77132b010a75ab191b9c97": TokenInfo(
        currency=CurrencyInfo(symbol="AURA", name="AURA Token"), scaling=Decimal("1e-2")
    ),
    "0x8b6c0dbc499eaf97f54b54fe0019a4c676db534a": TokenInfo(
        currency=CurrencyInfo(symbol="BYT", name="Bytex Token"), scaling=Decimal("1e-8")
    ),
    "0x8b6c3b7c01d9db4393f9aa734750f36df1543e9a": TokenInfo(
        currency=CurrencyInfo(symbol="VI", name="Vid"), scaling=Decimal("1e-18")
    ),
    "0x8b6cda5cc518c904e8844f445e1a7c7d2db0ff16": TokenInfo(
        currency=CurrencyInfo(symbol="SFCP", name="SF Capital"), scaling=Decimal("1e-18")
    ),
    "0x8b73f7ac6b831dbc7ded283554d1d39ebbaad28c": TokenInfo(
        currency=CurrencyInfo(symbol="HROI", name="High Roi"), scaling=Decimal("1e-18")
    ),
    "0x8b79656fc38a04044e495e22fad747126ca305c4": TokenInfo(
        currency=CurrencyInfo(symbol="AGVC", name="AgaveCoin"), scaling=Decimal("1e-18")
    ),
    "0x8b83116e05f722554e1089b9850e731ee20dd692": TokenInfo(
        currency=CurrencyInfo(symbol="ZCNOX", name="ZCNOX Coin"), scaling=Decimal("1e-18")
    ),
    "0x8b98df4dff429e64e9a56fc6eebe2380c6c3409c": TokenInfo(
        currency=CurrencyInfo(symbol="SI14", name="Si14Bet"), scaling=Decimal("1e-8")
    ),
    "0x8b9a25dfae16173403a21894eb9046084f717ec0": TokenInfo(
        currency=CurrencyInfo(symbol="CACHE", name="Cache"), scaling=Decimal("1e-18")
    ),
    "0x8ba009cad493c7646e31d69428ab9a54f47b3779": TokenInfo(
        currency=CurrencyInfo(symbol="VXT", name="VirgoX Token"), scaling=Decimal("1e-18")
    ),
    "0x8ba6dcc667d3ff64c1a2123ce72ff5f0199e5315": TokenInfo(
        currency=CurrencyInfo(symbol="ALEX", name="Alex"), scaling=Decimal("1e-4")
    ),
    "0x8bb95734f5011088fd228c8060b3e02ca53e3c0d": TokenInfo(
        currency=CurrencyInfo(symbol="CANDYBOX", name="Candy Box"), scaling=Decimal("1e-18")
    ),
    "0x8bbf4dd0f11b3a535660fd7fcb7158daebd3a17e": TokenInfo(
        currency=CurrencyInfo(symbol="EGAS", name="ETHGAS"), scaling=Decimal("1e-8")
    ),
    "0x8bd18c6fbe72ada40f54d5921dfd5454a6d548a9": TokenInfo(
        currency=CurrencyInfo(symbol="BMRN.CX", name="BioMarin Pharmaceutical Inc"), scaling=Decimal("1e-8")
    ),
    "0x8be6a6158f6b8a19fe60569c757d16e546c2296d": TokenInfo(
        currency=CurrencyInfo(symbol="YFF", name="YFF.Finance"), scaling=Decimal("1e-18")
    ),
    "0x8bf7326c3fff3a3ba9fcc618641bb8f3cd2eb7f9": TokenInfo(
        currency=CurrencyInfo(symbol="XSCC", name="Ghost Talk"), scaling=Decimal("1e-18")
    ),
    "0x8c15ef5b4b21951d50e53e4fbda8298ffad25057": TokenInfo(
        currency=CurrencyInfo(symbol="FX", name="Function X"), scaling=Decimal("1e-18")
    ),
    "0x8c168ef06b8baf8ad2236eef2286f7870ad50f9b": TokenInfo(
        currency=CurrencyInfo(symbol="SANTA", name="Santa Token"), scaling=Decimal("1e-18")
    ),
    "0x8c18d6a985ef69744b9d57248a45c0861874f244": TokenInfo(
        currency=CurrencyInfo(symbol="CTI", name="ClinTex CTi"), scaling=Decimal("1e-18")
    ),
    "0x8c32e8c6487c35deff3d65bcda73f86db8a1fa67": TokenInfo(
        currency=CurrencyInfo(symbol="PLA", name="Pelecanus"), scaling=Decimal("1e-18")
    ),
    "0x8c3ee4f778e282b59d42d693a97b80b1ed80f4ee": TokenInfo(
        currency=CurrencyInfo(symbol="STOP", name="SatoPay"), scaling=Decimal("1e-18")
    ),
    "0x8c4e7f814d40f8929f9112c5d09016f923d34472": TokenInfo(
        currency=CurrencyInfo(symbol="XLAB", name="XCELTOKEN PLUS"), scaling=Decimal("1e-18")
    ),
    "0x8c543aed163909142695f2d2acd0d55791a9edb9": TokenInfo(
        currency=CurrencyInfo(symbol="VLX", name="Velas"), scaling=Decimal("1e-18")
    ),
    "0x8c576b67e1caa070fc2cc00b615c1f530796da3e": TokenInfo(
        currency=CurrencyInfo(symbol="ETM", name="EtherMan Token"), scaling=Decimal("1e-18")
    ),
    "0x8c5cc09dfc32af3fbe764c5ec9ffada63aada32a": TokenInfo(
        currency=CurrencyInfo(symbol="MCS", name="Magic Stone Fund"), scaling=Decimal("1e-18")
    ),
    "0x8c65e992297d5f092a756def24f4781a280198ff": TokenInfo(
        currency=CurrencyInfo(symbol="GZE", name="GazeCoin"), scaling=Decimal("1e-18")
    ),
    "0x8c6fa66c21ae3fc435790e451946a9ea82e6e523": TokenInfo(
        currency=CurrencyInfo(symbol="FABRIC", name="MetaFabric"), scaling=Decimal("1e-18")
    ),
    "0x8c8687fc965593dfb2f0b4eaefd55e9d8df348df": TokenInfo(
        currency=CurrencyInfo(symbol="PAID", name="PAID Network"), scaling=Decimal("1e-18")
    ),
    "0x8c9e4cf756b9d01d791b95bc2d0913ef2bf03784": TokenInfo(
        currency=CurrencyInfo(symbol="AET", name="AEROTOKEN"), scaling=Decimal("1e-18")
    ),
    "0x8cbc6d8e11a9cb59922278321e0e61dfabc0d9f4": TokenInfo(
        currency=CurrencyInfo(symbol="KOPI", name="Kopi"), scaling=Decimal("1e-2")
    ),
    "0x8cce19943a01e78b7c277794fb081816f6151bab": TokenInfo(
        currency=CurrencyInfo(symbol="USDTBULL", name="3X Long Tether Token"), scaling=Decimal("1e-18")
    ),
    "0x8cd024cc8f73f5cd132005d1584403877b318c9d": TokenInfo(
        currency=CurrencyInfo(symbol="HPOT", name="Hash Pot"), scaling=Decimal("1e-18")
    ),
    "0x8cd58d4a29aa5461d07f7fe1edb5f6d3d22d5ada": TokenInfo(
        currency=CurrencyInfo(symbol="LORI", name="LORI"), scaling=Decimal("1e-18")
    ),
    "0x8ce5256f14a432579f7ee608a61761e1c4af7d93": TokenInfo(
        currency=CurrencyInfo(symbol="KNZV", name="Knyazev SA Token"), scaling=Decimal("1e-8")
    ),
    "0x8ce9137d39326ad0cd6491fb5cc0cba0e089b6a9": TokenInfo(
        currency=CurrencyInfo(symbol="SXP", name="Swipe"), scaling=Decimal("1e-18")
    ),
    "0x8cea63f6383c1c13633f179f1af70ef75701a979": TokenInfo(
        currency=CurrencyInfo(symbol="TORM", name="Thorium"), scaling=Decimal("1e-18")
    ),
    "0x8d1ce361eb68e9e05573443c407d4a3bed23b033": TokenInfo(
        currency=CurrencyInfo(symbol="DEFI++", name="PieDAO DEFI++"), scaling=Decimal("1e-18")
    ),
    "0x8d2bffcbb19ff14a698c424fbcdcfd17aab9b905": TokenInfo(
        currency=CurrencyInfo(symbol="UPUNK", name="Unicly CryptoPunks "), scaling=Decimal("1e-18")
    ),
    "0x8d4a15c9355b70a2558c99299c6990917758b76e": TokenInfo(
        currency=CurrencyInfo(symbol="CC.CX", name="Chemours"), scaling=Decimal("1e-8")
    ),
    "0x8d5682941ce456900b12d47ac06a88b47c764ce1": TokenInfo(
        currency=CurrencyInfo(symbol="RMESH", name="RightMesh"), scaling=Decimal("1e-18")
    ),
    "0x8d5a69dc82a47594881256f2eef81770274fa30f": TokenInfo(
        currency=CurrencyInfo(symbol="NTC", name="Natcoin"), scaling=Decimal("1e-18")
    ),
    "0x8d5db0c1f0681071cb38a382ae6704588d9da587": TokenInfo(
        currency=CurrencyInfo(symbol="PROPHET", name="Prophet"), scaling=Decimal("1e-9")
    ),
    "0x8d5e98738c6a83b5e7aea2b4937c2a9d92f779ba": TokenInfo(
        currency=CurrencyInfo(symbol="YY.CX", name="YY Inc."), scaling=Decimal("1e-8")
    ),
    "0x8d75959f1e61ec2571aa72798237101f084de63a": TokenInfo(
        currency=CurrencyInfo(symbol="SUB", name="Substratum"), scaling=Decimal("1e-18")
    ),
    "0x8d7db6a562764b437f3248031f886359b4183cc4": TokenInfo(
        currency=CurrencyInfo(symbol="SSS", name="SSS Finance"), scaling=Decimal("1e-18")
    ),
    "0x8d80de8a78198396329dfa769ad54d24bf90e7aa": TokenInfo(
        currency=CurrencyInfo(symbol="NAC", name="Nami.Trade"), scaling=Decimal("1e-18")
    ),
    "0x8d8129963291740dddd917ab01af18c7aed4ba58": TokenInfo(
        currency=CurrencyInfo(symbol="MB", name="MineBee"), scaling=Decimal("1e-18")
    ),
    "0x8d97c127236d3aef539171394212f2e43ad701c4": TokenInfo(
        currency=CurrencyInfo(symbol="HENA", name="HENA"), scaling=Decimal("1e-18")
    ),
    "0x8da25b8ed753a5910013167945a676921e864436": TokenInfo(
        currency=CurrencyInfo(symbol="BLV", name="Bellevue Network"), scaling=Decimal("1e-18")
    ),
    "0x8dae6cb04688c62d939ed9b68d32bc62e49970b1": TokenInfo(
        currency=CurrencyInfo(symbol="ACRV", name="Aave CRV"), scaling=Decimal("1e-18")
    ),
    "0x8daebade922df735c38c80c7ebd708af50815faa": TokenInfo(
        currency=CurrencyInfo(symbol="TBTC", name="tBTC"), scaling=Decimal("1e-18")
    ),
    "0x8db1d28ee0d822367af8d220c0dc7cb6fe9dc442": TokenInfo(
        currency=CurrencyInfo(symbol="ETHPAD", name="ETHPad"), scaling=Decimal("1e-18")
    ),
    "0x8db253a1943dddf1af9bcf8706ac9a0ce939d922": TokenInfo(
        currency=CurrencyInfo(symbol="UNB", name="Unbound Finance"), scaling=Decimal("1e-18")
    ),
    "0x8db54ca569d3019a2ba126d03c37c44b5ef81ef6": TokenInfo(
        currency=CurrencyInfo(symbol="DXT", name="Datawallet"), scaling=Decimal("1e-8")
    ),
    "0x8db90e3e7d04c875a51997092f9178fcac9defdb": TokenInfo(
        currency=CurrencyInfo(symbol="PORTAL", name="Portal"), scaling=Decimal("1e-18")
    ),
    "0x8dd57c98580e5070853272e765ea2c243f2d13e0": TokenInfo(
        currency=CurrencyInfo(symbol="PCCM", name="Poseidon Chain"), scaling=Decimal("1e-18")
    ),
    "0x8dd5fbce2f6a956c3022ba3663759011dd51e73e": TokenInfo(
        currency=CurrencyInfo(symbol="TUSD", name="TrueUSD"), scaling=Decimal("1e-18")
    ),
    "0x8ddc86dba7ad728012efc460b8a168aba60b403b": TokenInfo(
        currency=CurrencyInfo(symbol="ETHHIVOL", name="ETH Range Bound High Volatility Set"), scaling=Decimal("1e-18")
    ),
    "0x8ddf05c42c698329053c4f39b5bb05a350fd8132": TokenInfo(
        currency=CurrencyInfo(symbol="ETHSB", name="ETH Smart Beta Set"), scaling=Decimal("1e-18")
    ),
    "0x8deef89058090ac5655a99eeb451a4f9183d1678": TokenInfo(
        currency=CurrencyInfo(symbol="iXTZ", name="Synth iXTZ"), scaling=Decimal("1e-18")
    ),
    "0x8e16bf47065fe843a82f4399baf5abac4e0822b7": TokenInfo(
        currency=CurrencyInfo(symbol="BFIL", name="Binance Wrapped FIL"), scaling=Decimal("1e-18")
    ),
    "0x8e1b448ec7adfc7fa35fc2e885678bd323176e34": TokenInfo(
        currency=CurrencyInfo(symbol="EGT", name="Egretia"), scaling=Decimal("1e-18")
    ),
    "0x8e2b4badac15a4ec8c56020f4ce60faa7558c052": TokenInfo(
        currency=CurrencyInfo(symbol="CNFT", name="Communifty"), scaling=Decimal("1e-18")
    ),
    "0x8e30ea2329d95802fd804f4291220b0e2f579812": TokenInfo(
        currency=CurrencyInfo(symbol="DVP", name="Decentralized Vulnerability Platform"), scaling=Decimal("1e-18")
    ),
    "0x8e4dbf540bf814c044785218b58c930b20a56be1": TokenInfo(
        currency=CurrencyInfo(symbol="TCAPETHDAI", name="Holistic ETH Set"), scaling=Decimal("1e-18")
    ),
    "0x8e5610ab5e39d26828167640ea29823fe1dd5843": TokenInfo(
        currency=CurrencyInfo(symbol="KNDC", name="KanadeCoin"), scaling=Decimal("1e-8")
    ),
    "0x8e5afc69f6227a3ad75ed346c8723bc62ce97123": TokenInfo(
        currency=CurrencyInfo(symbol="UMKA", name="UMKA"), scaling=Decimal("1e-4")
    ),
    "0x8e6cd950ad6ba651f6dd608dc70e5886b1aa6b24": TokenInfo(
        currency=CurrencyInfo(symbol="STARL", name="StarLink"), scaling=Decimal("1e-18")
    ),
    "0x8e766f57f7d16ca50b4a0b90b88f6468a09b0439": TokenInfo(
        currency=CurrencyInfo(symbol="MXM", name="Maximine"), scaling=Decimal("1e-18")
    ),
    "0x8e854926d29855d16661f4572f8ca1785bb240c2": TokenInfo(
        currency=CurrencyInfo(symbol="LB.CX", name="L Brands"), scaling=Decimal("1e-8")
    ),
    "0x8e870d67f660d95d5be530380d0ec0bd388289e1": TokenInfo(
        currency=CurrencyInfo(symbol="USDP", name="Pax Dollar"), scaling=Decimal("1e-18")
    ),
    "0x8e87f1811de0025d2335174dbc7338a43df6d7cc": TokenInfo(
        currency=CurrencyInfo(symbol="VGO", name="Virtual Goods Token"), scaling=Decimal("1e-18")
    ),
    "0x8e907bba61ae322a067644d6c8211fa05f2a12f4": TokenInfo(
        currency=CurrencyInfo(symbol="LNX", name="LNX Protocol"), scaling=Decimal("1e-18")
    ),
    "0x8e91a9cbadb74ef60c456f1e4ba3e391b143aad9": TokenInfo(
        currency=CurrencyInfo(symbol="OPTC", name="Optical Network"), scaling=Decimal("1e-18")
    ),
    "0x8e9a29e7ed21db7c5b2e1cd75e676da0236dfb45": TokenInfo(
        currency=CurrencyInfo(symbol="HUB", name="Minter Hub"), scaling=Decimal("1e-18")
    ),
    "0x8e9c3d1f30904e91764b7b8bbfda3a429b886874": TokenInfo(
        currency=CurrencyInfo(symbol="0XESV", name="0xETH SV"), scaling=Decimal("1e-8")
    ),
    "0x8eab2c9fcb31ad9cd7eccb48634b849dc9c81af2": TokenInfo(
        currency=CurrencyInfo(symbol="BABA", name="Base Ecosystem"), scaling=Decimal("1e-8")
    ),
    "0x8eb24319393716668d768dcec29356ae9cffe285": TokenInfo(
        currency=CurrencyInfo(symbol="AGI", name="SingularityNET Token"), scaling=Decimal("1e-8")
    ),
    "0x8eb38715604b938812dec25a0a1bc05b4becb9ca": TokenInfo(
        currency=CurrencyInfo(symbol="GC", name="Gric Coin"), scaling=Decimal("1e-18")
    ),
    "0x8eb965ee9ccfbce76c0a06264492c0afefc2826d": TokenInfo(
        currency=CurrencyInfo(symbol="TOOR", name="ToorCoin"), scaling=Decimal("1e-18")
    ),
    "0x8ecb1ca966b6804b129d3c0f9771e079cbf48efe": TokenInfo(
        currency=CurrencyInfo(symbol="EPT", name="e-Pocket Token"), scaling=Decimal("1e-18")
    ),
    "0x8ed5afcb8877624802a0cbfb942c95c2b7c87146": TokenInfo(
        currency=CurrencyInfo(symbol="ZXT", name="Zhixin Chain"), scaling=Decimal("1e-18")
    ),
    "0x8ed876e408959643479534a21970ec023d0fb51e": TokenInfo(
        currency=CurrencyInfo(symbol="CADX", name="eToro Canadian Dollar"), scaling=Decimal("1e-18")
    ),
    "0x8ed9f862363ffdfd3a07546e618214b6d59f03d4": TokenInfo(
        currency=CurrencyInfo(symbol="OCUSDC", name="Opyn cUSDC Insurance"), scaling=Decimal("1e-8")
    ),
    "0x8eef5a82e6aa222a60f009ac18c24ee12dbf4b41": TokenInfo(
        currency=CurrencyInfo(symbol="TXL", name="Tixl"), scaling=Decimal("1e-18")
    ),
    "0x8ef47555856f6ce2e0cd7c36aef4fab317d2e2e2": TokenInfo(
        currency=CurrencyInfo(symbol="PAYT", name="PayAccept"), scaling=Decimal("1e-18")
    ),
    "0x8effd494eb698cc399af6231fccd39e08fd20b15": TokenInfo(
        currency=CurrencyInfo(symbol="PIX", name="Lampix"), scaling=Decimal("1e-0")
    ),
    "0x8f0921f30555624143d427b340b1156914882c10": TokenInfo(
        currency=CurrencyInfo(symbol="FYP", name="FlypMe"), scaling=Decimal("1e-18")
    ),
    "0x8f179114235842978d8917e08721541072c46584": TokenInfo(
        currency=CurrencyInfo(symbol="PXP", name="PXP Token"), scaling=Decimal("1e-3")
    ),
    "0x8f2c72056b3fef90d07aa7db86dccfc0af3270a8": TokenInfo(
        currency=CurrencyInfo(symbol="EMT", name="EMT Chain"), scaling=Decimal("1e-18")
    ),
    "0x8f32cbcc9cab6a748829f8de41a46d02d995dabc": TokenInfo(
        currency=CurrencyInfo(symbol="DFL", name="DFlow Token"), scaling=Decimal("1e-8")
    ),
    "0x8f3470a7388c05ee4e7af3d01d8c722b0ff52374": TokenInfo(
        currency=CurrencyInfo(symbol="VERI", name="Veritaseum"), scaling=Decimal("1e-18")
    ),
    "0x8f606c58aeff00169b06f88ca2f28862971668dd": TokenInfo(
        currency=CurrencyInfo(symbol="XPO.CX", name="XPO Logistics"), scaling=Decimal("1e-8")
    ),
    "0x8f66a173696502a0ad280781c3e55928a06c1312": TokenInfo(
        currency=CurrencyInfo(symbol="PWV", name="Peoplewave"), scaling=Decimal("1e-18")
    ),
    "0x8f7a9b503aa7f9255368bd34d01aea2b502164c2": TokenInfo(
        currency=CurrencyInfo(symbol="BRC", name="Bryllite"), scaling=Decimal("1e-18")
    ),
    "0x8f7b0b40e27e357540f90f187d90ce06366ac5a5": TokenInfo(
        currency=CurrencyInfo(symbol="VLC", name="ValueChain"), scaling=Decimal("1e-18")
    ),
    "0x8f8221afbb33998d8584a2b05749ba73c37a938a": TokenInfo(
        currency=CurrencyInfo(symbol="REQ", name="Request"), scaling=Decimal("1e-18")
    ),
    "0x8f8e787989bc652eea01a6c88a19f0f379bdf4fd": TokenInfo(
        currency=CurrencyInfo(symbol="HLX", name="Helex"), scaling=Decimal("1e-5")
    ),
    "0x8f9933218213c9bef8048cc4618ebb1df96bde8e": TokenInfo(
        currency=CurrencyInfo(symbol="XKN", name="KOIN"), scaling=Decimal("1e-18")
    ),
    "0x8f9bfe5b6a5c3fea8c64ad41a5cf6f60ec4aa47c": TokenInfo(
        currency=CurrencyInfo(symbol="SPAZ", name="SWAPCOINZ"), scaling=Decimal("1e-8")
    ),
    "0x8fac8031e079f409135766c7d5de29cf22ef897c": TokenInfo(
        currency=CurrencyInfo(symbol="HEART", name="Humans ai"), scaling=Decimal("1e-18")
    ),
    "0x8faf0be1465b9be70ee73d9123b2a1fdd9f2aae4": TokenInfo(
        currency=CurrencyInfo(symbol="XLC", name="Ethereum Lite Cash"), scaling=Decimal("1e-8")
    ),
    "0x8fc01e6cbdffaf09b54f423f9bb1f856b22e47b2": TokenInfo(
        currency=CurrencyInfo(symbol="OBTC", name="Obitan Chain"), scaling=Decimal("1e-8")
    ),
    "0x8fc9b6354e839ab1c8b31f4afa53607092b8c2e5": TokenInfo(
        currency=CurrencyInfo(symbol="ECU", name="ECOSC"), scaling=Decimal("1e-18")
    ),
    "0x8feef860e9fa9326ff9d7e0058f637be8579cc29": TokenInfo(
        currency=CurrencyInfo(symbol="IPM", name="Timers"), scaling=Decimal("1e-18")
    ),
    "0x9002d4485b7594e3e850f0a206713b305113f69e": TokenInfo(
        currency=CurrencyInfo(symbol="HAT", name="HAT Token"), scaling=Decimal("1e-12")
    ),
    "0x9003ce9e92e1105f235ca59e2bf65abd36dfdc01": TokenInfo(
        currency=CurrencyInfo(symbol="BCHMOON", name="10X Long Bitcoin Cash Token"), scaling=Decimal("1e-18")
    ),
    "0x900b4449236a7bb26b286601dd14d2bde7a6ac6c": TokenInfo(
        currency=CurrencyInfo(symbol="EARTH", name="EarthToken"), scaling=Decimal("1e-8")
    ),
    "0x90162f41886c0946d09999736f1c15c8a105a421": TokenInfo(
        currency=CurrencyInfo(symbol="FAN", name="Fan Token"), scaling=Decimal("1e-18")
    ),
    "0x901f8679a6ef435d533732f5ea49bb82d568be99": TokenInfo(
        currency=CurrencyInfo(symbol="TRB", name="Trebit Network"), scaling=Decimal("1e-18")
    ),
    "0x901fe080ee18383bf5494049538f1bca155f4d0b": TokenInfo(
        currency=CurrencyInfo(symbol="TMH", name="TrusMarketHub Token"), scaling=Decimal("1e-18")
    ),
    "0x9025f9a59694dd939739e05beb2502a567e8326f": TokenInfo(
        currency=CurrencyInfo(symbol="NAMTT", name="NamTanToken"), scaling=Decimal("1e-18")
    ),
    "0x903b76f361298169535b2b0ef065c4adb0623aaa": TokenInfo(
        currency=CurrencyInfo(symbol="BPAY", name="Butterfly Protocol Token"), scaling=Decimal("1e-18")
    ),
    "0x903bef1736cddf2a537176cf3c64579c3867a881": TokenInfo(
        currency=CurrencyInfo(symbol="ICHI", name="ICHI"), scaling=Decimal("1e-9")
    ),
    "0x9040e237c3bf18347bb00957dc22167d0f2b999d": TokenInfo(
        currency=CurrencyInfo(symbol="STND", name="Standard Protocol"), scaling=Decimal("1e-18")
    ),
    "0x9041fe5b3fdea0f5e4afdc17e75180738d877a01": TokenInfo(
        currency=CurrencyInfo(symbol="PRA", name="ProChain"), scaling=Decimal("1e-18")
    ),
    "0x9043d4d51c9d2e31e3f169de4551e416970c27ef": TokenInfo(
        currency=CurrencyInfo(symbol="PDAI", name="Prime DAI"), scaling=Decimal("1e-18")
    ),
    "0x90528aeb3a2b736b780fd1b6c478bb7e1d643170": TokenInfo(
        currency=CurrencyInfo(symbol="XPA", name="XPA"), scaling=Decimal("1e-18")
    ),
    "0x905e337c6c8645263d3521205aa37bf4d034e745": TokenInfo(
        currency=CurrencyInfo(symbol="MTC", name="Doc.com"), scaling=Decimal("1e-18")
    ),
    "0x9064c91e51d7021a85ad96817e1432abf6624470": TokenInfo(
        currency=CurrencyInfo(symbol="SHE", name="ShineChain"), scaling=Decimal("1e-18")
    ),
    "0x906b3f8b7845840188eab53c3f5ad348a787752f": TokenInfo(
        currency=CurrencyInfo(symbol="DOR", name="Dorado"), scaling=Decimal("1e-15")
    ),
    "0x9080e92296a176883aab1d7d1b7e50bc055b0caa": TokenInfo(
        currency=CurrencyInfo(symbol="YFICG", name="YFI Credits Group"), scaling=Decimal("1e-18")
    ),
    "0x90a1ef62b5f71be34c68ef0a5f593cf21034158c": TokenInfo(
        currency=CurrencyInfo(symbol="CVS.CX", name="CVS Health"), scaling=Decimal("1e-8")
    ),
    "0x90ad3de8e3a93177e4b999e21f1d70a6496d44a9": TokenInfo(
        currency=CurrencyInfo(symbol="STLD.CX", name="Steel Dynamics Inc"), scaling=Decimal("1e-8")
    ),
    "0x90b417ab462440cf59767bcf72d0d91ca42f21ed": TokenInfo(
        currency=CurrencyInfo(symbol="ALTBEAR", name="3X Short Altcoin Index Token"), scaling=Decimal("1e-18")
    ),
    "0x90b426067be0b0ff5de257bc4dd6a4815ea03b5f": TokenInfo(
        currency=CurrencyInfo(symbol="STRN", name="Strain"), scaling=Decimal("1e-18")
    ),
    "0x90b831fa3bebf58e9744a14d638e25b4ee06f9bc": TokenInfo(
        currency=CurrencyInfo(symbol="MIMO", name="MIMO Parallel Gover"), scaling=Decimal("1e-18")
    ),
    "0x90d46a9636b973f18186541d1b04ed3621a49cb0": TokenInfo(
        currency=CurrencyInfo(symbol="NAT", name="Natmin"), scaling=Decimal("1e-18")
    ),
    "0x90d702f071d2af33032943137ad0ab4280705817": TokenInfo(
        currency=CurrencyInfo(symbol="YFFS", name="YFFS Finance"), scaling=Decimal("1e-18")
    ),
    "0x90f08cc8ddc43f5c01224f67fdf4640995139e8f": TokenInfo(
        currency=CurrencyInfo(symbol="HETH", name="Ethash"), scaling=Decimal("1e-8")
    ),
    "0x90f49083ff588ec5a5459f4d2a64b8d409c03122": TokenInfo(
        currency=CurrencyInfo(symbol="BTCMOONX", name="BTC Moonshot X Set"), scaling=Decimal("1e-18")
    ),
    "0x90f802c7e8fb5d40b0de583e34c065a3bd2020d8": TokenInfo(
        currency=CurrencyInfo(symbol="YD-ETH-MAR21", name="YD-ETH-MAR21"), scaling=Decimal("1e-18")
    ),
    "0x910524678c0b1b23ffb9285a81f99c29c11cbaed": TokenInfo(
        currency=CurrencyInfo(symbol="AZUKI", name="Azuki"), scaling=Decimal("1e-18")
    ),
    "0x9108e027384506c528bd3d3603a46986c065b8fa": TokenInfo(
        currency=CurrencyInfo(symbol="EHC", name="Ecosystem Health Chain"), scaling=Decimal("1e-18")
    ),
    "0x910dfc18d6ea3d6a7124a6f8b5458f281060fa4c": TokenInfo(
        currency=CurrencyInfo(symbol="X8X", name="X8X Token"), scaling=Decimal("1e-18")
    ),
    "0x91264366d679ff09bbc07a2b58e3e2d9c002eeff": TokenInfo(
        currency=CurrencyInfo(symbol="CRS", name="CRS Token"), scaling=Decimal("1e-18")
    ),
    "0x912b38134f395d1bfab4c6f9db632c31667acf98": TokenInfo(
        currency=CurrencyInfo(symbol="BIDS", name="DeFi Bids"), scaling=Decimal("1e-18")
    ),
    "0x9135d92e3a34e2a94e4474b74b9dc2d51118eed5": TokenInfo(
        currency=CurrencyInfo(symbol="UHP", name="Ulgen Hash Power"), scaling=Decimal("1e-18")
    ),
    "0x91371b9bc6e90f6db3c4f4d630cf5f7700ab917c": TokenInfo(
        currency=CurrencyInfo(symbol="BSVDOOM", name="10X Short Bitcoin SV Token"), scaling=Decimal("1e-18")
    ),
    "0x913d8adf7ce6986a8cbfee5a54725d9eea4f0729": TokenInfo(
        currency=CurrencyInfo(symbol="EASY", name="EASY"), scaling=Decimal("1e-18")
    ),
    "0x915044526758533dfb918eceb6e44bc21632060d": TokenInfo(
        currency=CurrencyInfo(symbol="CHR", name="Chroma"), scaling=Decimal("1e-6")
    ),
    "0x917fd2f7378ff479419dcb56c5cbb445fbbf902a": TokenInfo(
        currency=CurrencyInfo(symbol="CAN", name="Coinwaycoin"), scaling=Decimal("1e-10")
    ),
    "0x9196e18bc349b1f64bc08784eae259525329a1ad": TokenInfo(
        currency=CurrencyInfo(symbol="PUSSY", name="Pussy Financial"), scaling=Decimal("1e-18")
    ),
    "0x919d3a363776b1ceec9352610c82dfaf80edc32d": TokenInfo(
        currency=CurrencyInfo(symbol="GFUN", name="GoldFund"), scaling=Decimal("1e-18")
    ),
    "0x91af0fbb28aba7e31403cb457106ce79397fd4e6": TokenInfo(
        currency=CurrencyInfo(symbol="AERGO", name="Aergo"), scaling=Decimal("1e-18")
    ),
    "0x91b7ed3b352aa3502f94e58eac930ae1f5b5ebcd": TokenInfo(
        currency=CurrencyInfo(symbol="CNYT", name="CNY Tether"), scaling=Decimal("1e-0")
    ),
    "0x91bb6965bace45bae7e78ae638152af467f9b004": TokenInfo(
        currency=CurrencyInfo(symbol="PXG", name="Piexgo Token"), scaling=Decimal("1e-18")
    ),
    "0x91bd140bf6656228583ce1bb7c04f32609625644": TokenInfo(
        currency=CurrencyInfo(symbol="BIGB", name="BIGBANG Coin"), scaling=Decimal("1e-18")
    ),
    "0x91cdb5bb5969bfed2373e97378354052bbc606f2": TokenInfo(
        currency=CurrencyInfo(symbol="DRCT", name="DRC Token"), scaling=Decimal("1e-18")
    ),
    "0x91dfbee3965baaee32784c2d546b7a0c62f268c9": TokenInfo(
        currency=CurrencyInfo(symbol="BONDLY", name="Bondly"), scaling=Decimal("1e-18")
    ),
    "0x91e64f39c1fe14492e8fdf5a8b0f305bd218c8a1": TokenInfo(
        currency=CurrencyInfo(symbol="VDX", name="Vodi X"), scaling=Decimal("1e-18")
    ),
    "0x91e84ec6101547c1fa39dd565dd8b020e3c20cf2": TokenInfo(
        currency=CurrencyInfo(symbol="CND", name="Cannadrix"), scaling=Decimal("1e-18")
    ),
    "0x920db6c38cf5a2a12554e812d4b3ac2daa8eba4d": TokenInfo(
        currency=CurrencyInfo(symbol="EVI", name="Evimeria"), scaling=Decimal("1e-18")
    ),
    "0x9214ec02cb71cba0ada6896b8da260736a67ab10": TokenInfo(
        currency=CurrencyInfo(symbol="REAL", name="Real Estate Asset Ledger"), scaling=Decimal("1e-18")
    ),
    "0x922105fad8153f516bcfb829f56dc097a0e1d705": TokenInfo(
        currency=CurrencyInfo(symbol="YEE", name="Yee"), scaling=Decimal("1e-18")
    ),
    "0x92298fa0647b5dcff6eeabab97c9bd81b5c30d06": TokenInfo(
        currency=CurrencyInfo(symbol="LIKE", name="LikeApp"), scaling=Decimal("1e-0")
    ),
    "0x922ac473a3cc241fd3a0049ed14536452d58d73c": TokenInfo(
        currency=CurrencyInfo(symbol="VLD", name="Vetri"), scaling=Decimal("1e-18")
    ),
    "0x923108a439c4e8c2315c4f6521e5ce95b44e9b4c": TokenInfo(
        currency=CurrencyInfo(symbol="EVE", name="Devery"), scaling=Decimal("1e-18")
    ),
    "0x9238bfb781a55eacc3cf05f7df94038c198cd9b9": TokenInfo(
        currency=CurrencyInfo(symbol="CRMT", name="Cremit"), scaling=Decimal("1e-8")
    ),
    "0x923c90b98ee834d118c85ddf44906ee1769df648": TokenInfo(
        currency=CurrencyInfo(symbol="QTC", name="Qitcoin"), scaling=Decimal("1e-6")
    ),
    "0x9248c485b0b80f76da451f167a8db30f33c70907": TokenInfo(
        currency=CurrencyInfo(symbol="DEBASE", name="Debase"), scaling=Decimal("1e-18")
    ),
    "0x924e26fee8e10c20726006cc2bd307a538b0ebe5": TokenInfo(
        currency=CurrencyInfo(symbol="BTCRSIAPY", name="BTC RSI Crossover Yield Set"), scaling=Decimal("1e-18")
    ),
    "0x9250e33f8ae7b9fe02fb9af97a0c55b42a5ad9d8": TokenInfo(
        currency=CurrencyInfo(symbol="CINO", name="Cino Games"), scaling=Decimal("1e-18")
    ),
    "0x92685e93956537c25bb75d5d47fca4266dd628b8": TokenInfo(
        currency=CurrencyInfo(symbol="BTL", name="Bitlle Token"), scaling=Decimal("1e-4")
    ),
    "0x926be13b4d93f29ea254e4e518f33099e45d7f06": TokenInfo(
        currency=CurrencyInfo(symbol="POCC", name="POC Chain"), scaling=Decimal("1e-18")
    ),
    "0x927159670c50042109d7c0f4aed0cee89452433e": TokenInfo(
        currency=CurrencyInfo(symbol="DGP", name="DGPayment"), scaling=Decimal("1e-18")
    ),
    "0x9281c548c6d107aea807b87a776da045f71fa193": TokenInfo(
        currency=CurrencyInfo(symbol="ALGODOOM", name="10X Short Algorand Token"), scaling=Decimal("1e-18")
    ),
    "0x9288d6b823927f528aea244c5fa71a356b807112": TokenInfo(
        currency=CurrencyInfo(symbol="JCT", name="Japan Content Token"), scaling=Decimal("1e-8")
    ),
    "0x92a42db88ed0f02c71d439e55962ca7cab0168b5": TokenInfo(
        currency=CurrencyInfo(symbol="TRDG", name="TRDG"), scaling=Decimal("1e-9")
    ),
    "0x92a5b04d0ed5d94d7a193d1d334d3d16996f4e13": TokenInfo(
        currency=CurrencyInfo(symbol="ERT", name="Eristica token"), scaling=Decimal("1e-18")
    ),
    "0x92aadc367feb0cad3cc52bb19721be3aad95953c": TokenInfo(
        currency=CurrencyInfo(symbol="PITI", name="Piti"), scaling=Decimal("1e-18")
    ),
    "0x92b7e4409dcf8c439f313ed1f05fdc0550d18ddd": TokenInfo(
        currency=CurrencyInfo(symbol="MDS", name="MYDAS"), scaling=Decimal("1e-18")
    ),
    "0x92d6c1e31e14520e676a687f0a93788b716beff5": TokenInfo(
        currency=CurrencyInfo(symbol="DYDX", name="dYdX"), scaling=Decimal("1e-18")
    ),
    "0x92d7a89405ea3cc605a467e834236e09df60bf16": TokenInfo(
        currency=CurrencyInfo(symbol="SPIRIT", name="SPIRIT"), scaling=Decimal("1e-18")
    ),
    "0x92e187a03b6cd19cb6af293ba17f2745fd2357d5": TokenInfo(
        currency=CurrencyInfo(symbol="DUCK", name="Unit Protocol New"), scaling=Decimal("1e-18")
    ),
    "0x92e52a1a235d9a103d970901066ce910aacefd37": TokenInfo(
        currency=CurrencyInfo(symbol="UCASH", name="U.CASH"), scaling=Decimal("1e-8")
    ),
    "0x92e78dae1315067a8819efd6dca432de9dcde2e9": TokenInfo(
        currency=CurrencyInfo(symbol="VRS", name="Veros"), scaling=Decimal("1e-6")
    ),
    "0x92ec47df1aa167806dfa4916d9cfb99da6953b8f": TokenInfo(
        currency=CurrencyInfo(symbol="IDV", name="Idavoll Network"), scaling=Decimal("1e-18")
    ),
    "0x92ece48522e1acbcda4aaa8c2fbf2aa9fb15d624": TokenInfo(
        currency=CurrencyInfo(symbol="ROCKS", name="Rocki"), scaling=Decimal("1e-18")
    ),
    "0x92ef4ffbfe0df030837b65d7fccfe1abd6549579": TokenInfo(
        currency=CurrencyInfo(symbol="SWGB", name="Swirge"), scaling=Decimal("1e-18")
    ),
    "0x9303eabc860a743aabcc3a1629014cabcc3f8d36": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNIDAIWETH", name="Aave AMM UniDAIWETH"), scaling=Decimal("1e-18")
    ),
    "0x930ed81ad809603baf727117385d01f04354612e": TokenInfo(
        currency=CurrencyInfo(symbol="SOLARITE", name="Solarite"), scaling=Decimal("1e-18")
    ),
    "0x931684139f756c24ec0731e9f74fe50e5548ddef": TokenInfo(
        currency=CurrencyInfo(symbol="URB", name="Urbit Token"), scaling=Decimal("1e-18")
    ),
    "0x9317ae2dc3313ae2177910cebc3feaccbba2e824": TokenInfo(
        currency=CurrencyInfo(symbol="RXE", name="realxoin"), scaling=Decimal("1e-6")
    ),
    "0x9318105460626e7fa58308fa4bce40e4616f3565": TokenInfo(
        currency=CurrencyInfo(symbol="PIXIE", name="Pixie Dust"), scaling=Decimal("1e-18")
    ),
    "0x931a9350333c79d9da373ee857ca97273c5a595f": TokenInfo(
        currency=CurrencyInfo(symbol="XLNX.CX", name="Xilinx, Inc."), scaling=Decimal("1e-8")
    ),
    "0x931ad0628aa11791c26ff4d41ce23e40c31c5e4e": TokenInfo(
        currency=CurrencyInfo(symbol="PGS", name="Pegasus"), scaling=Decimal("1e-8")
    ),
    "0x932d447274dcffb4aea4f0944d3c804e88056416": TokenInfo(
        currency=CurrencyInfo(symbol="LBET", name="Lemon Bet"), scaling=Decimal("1e-18")
    ),
    "0x933dfc5622792b41245ab8313416caf0ba885ae7": TokenInfo(
        currency=CurrencyInfo(symbol="COBR", name="CoinBroker"), scaling=Decimal("1e-18")
    ),
    "0x9344b383b1d59b5ce3468b234dab43c7190ba735": TokenInfo(
        currency=CurrencyInfo(symbol="NCC", name="NeedsCoin"), scaling=Decimal("1e-18")
    ),
    "0x9355372396e3f6daf13359b7b607a3374cc638e0": TokenInfo(
        currency=CurrencyInfo(symbol="WHALE", name="WHALE"), scaling=Decimal("1e-4")
    ),
    "0x9388f54fa978aa9e24395a8b69033304eccea4df": TokenInfo(
        currency=CurrencyInfo(symbol="BTCX", name="BITSCOIN"), scaling=Decimal("1e-4")
    ),
    "0x9389434852b94bbad4c8afed5b7bdbc5ff0c2275": TokenInfo(
        currency=CurrencyInfo(symbol="TTC", name="TTC"), scaling=Decimal("1e-18")
    ),
    "0x938f66735c6b4f99ee51e657d51e86c2847788cb": TokenInfo(
        currency=CurrencyInfo(symbol="VREX", name="Veron Coin"), scaling=Decimal("1e-18")
    ),
    "0x93a7174dafd31d13400cd9fa01f4e5b5baa00d39": TokenInfo(
        currency=CurrencyInfo(symbol="HAK", name="Shaka"), scaling=Decimal("1e-18")
    ),
    "0x93b1e78a3e652cd2e71c4a767595b77282344932": TokenInfo(
        currency=CurrencyInfo(symbol="BITO", name="BITO Coin"), scaling=Decimal("1e-18")
    ),
    "0x93c564d4cc593867daae181eb3b494a2362b1ec5": TokenInfo(
        currency=CurrencyInfo(symbol="CSAC", name="Credit Safe Application Chain"), scaling=Decimal("1e-8")
    ),
    "0x93d3296cac208422bf587c3597d116e809870f2b": TokenInfo(
        currency=CurrencyInfo(symbol="pUSD", name="US Dollar"), scaling=Decimal("1e-8")
    ),
    "0x93dfaf57d986b9ca77df9376c50878e013d9c7c8": TokenInfo(
        currency=CurrencyInfo(symbol="RARE", name="Unique One"), scaling=Decimal("1e-18")
    ),
    "0x93e3ea31a74209daf3fcbd8a4013236b8e21559f": TokenInfo(
        currency=CurrencyInfo(symbol="OEN", name="OEN"), scaling=Decimal("1e-18")
    ),
    "0x93e682107d1e9defb0b5ee701c71707a4b2e46bc": TokenInfo(
        currency=CurrencyInfo(symbol="MCAP", name="MCAP"), scaling=Decimal("1e-8")
    ),
    "0x93ec2b9d85a7f4b0abc66abf4ca8d5e50c355516": TokenInfo(
        currency=CurrencyInfo(symbol="NXC", name="Nixma Coin"), scaling=Decimal("1e-18")
    ),
    "0x93ecd2ecdfb91ab2fee28a8779a6adfe2851cda6": TokenInfo(
        currency=CurrencyInfo(symbol="LBURST", name="LoanBurst"), scaling=Decimal("1e-18")
    ),
    "0x93ed3fbe21207ec2e8f2d3c3de6e058cb73bc04d": TokenInfo(
        currency=CurrencyInfo(symbol="PNK", name="Kleros"), scaling=Decimal("1e-18")
    ),
    "0x940a2db1b7008b6c776d4faaca729d6d4a4aa551": TokenInfo(
        currency=CurrencyInfo(symbol="DUSK", name="DUSK Network"), scaling=Decimal("1e-18")
    ),
    "0x94236591125e935f5ac128bb3d5062944c24958c": TokenInfo(
        currency=CurrencyInfo(symbol="VGW", name="VegaWallet Token"), scaling=Decimal("1e-5")
    ),
    "0x943ed852dadb5c3938ecdc6883718df8142de4c8": TokenInfo(
        currency=CurrencyInfo(symbol="FTI", name="FansTime"), scaling=Decimal("1e-18")
    ),
    "0x945facb997494cc2570096c74b5f66a3507330a1": TokenInfo(
        currency=CurrencyInfo(symbol="mBTC", name="mStable mBTC"), scaling=Decimal("1e-18")
    ),
    "0x946112efab61c3636cbd52de2e1392d7a75a6f01": TokenInfo(
        currency=CurrencyInfo(symbol="HYDRO", name="Hydro"), scaling=Decimal("1e-18")
    ),
    "0x946551dd05c5abd7cc808927480225ce36d8c475": TokenInfo(
        currency=CurrencyInfo(symbol="ONE", name="One"), scaling=Decimal("1e-18")
    ),
    "0x9469d013805bffb7d3debe5e7839237e535ec483": TokenInfo(
        currency=CurrencyInfo(symbol="RING", name="Darwinia Network Native Token"), scaling=Decimal("1e-18")
    ),
    "0x946ea588417ffa565976efda354d82c01719a2ea": TokenInfo(
        currency=CurrencyInfo(symbol="SWZL", name="Swapzilla"), scaling=Decimal("1e-0")
    ),
    "0x947aeb02304391f8fbe5b25d7d98d649b57b1788": TokenInfo(
        currency=CurrencyInfo(symbol="MDX", name="Mandala Exchange Token"), scaling=Decimal("1e-18")
    ),
    "0x94837e5a3d1a3957b8782e8a303f226b29e38a34": TokenInfo(
        currency=CurrencyInfo(symbol="APA.CX", name="Apache"), scaling=Decimal("1e-8")
    ),
    "0x94939d55000b31b7808904a80aa7bab05ef59ed6": TokenInfo(
        currency=CurrencyInfo(symbol="JIAOZI", name="Jiaozi"), scaling=Decimal("1e-18")
    ),
    "0x949bed886c739f1a3273629b3320db0c5024c719": TokenInfo(
        currency=CurrencyInfo(symbol="AMIS", name="AMIS"), scaling=Decimal("1e-9")
    ),
    "0x949d48eca67b17269629c7194f4b727d4ef9e5d6": TokenInfo(
        currency=CurrencyInfo(symbol="MC", name="Merit Circle"), scaling=Decimal("1e-18")
    ),
    "0x94bed3c94123af8cebdb6c025240043fceb8dbf5": TokenInfo(
        currency=CurrencyInfo(symbol="ROKU.CX", name="Roku Inc"), scaling=Decimal("1e-8")
    ),
    "0x94cb815f4b601b00b363b3177b4d8ed8e0eb7cf2": TokenInfo(
        currency=CurrencyInfo(symbol="CCC", name="Coindom"), scaling=Decimal("1e-18")
    ),
    "0x94d863173ee77439e4292284ff13fad54b3ba182": TokenInfo(
        currency=CurrencyInfo(symbol="ADEL", name="Delphi"), scaling=Decimal("1e-18")
    ),
    "0x94d8db14831c2c08943798542c450df2844913e5": TokenInfo(
        currency=CurrencyInfo(symbol="ZLP", name="Zuplo"), scaling=Decimal("1e-18")
    ),
    "0x94e0bab2f6ab1f19f4750e42d7349f2740513ad5": TokenInfo(
        currency=CurrencyInfo(symbol="UNIC", name="Unicly"), scaling=Decimal("1e-18")
    ),
    "0x94eea9a484f0bae03d19623cfe389e2cba56b72f": TokenInfo(
        currency=CurrencyInfo(symbol="NZO", name="Enzo"), scaling=Decimal("1e-18")
    ),
    "0x94fc5934cf5970e944a67de806eeb5a4b493c6e6": TokenInfo(
        currency=CurrencyInfo(symbol="XRPBEAR", name="3X Short XRP Token"), scaling=Decimal("1e-18")
    ),
    "0x9501bfc48897dceeadf73113ef635d2ff7ee4b97": TokenInfo(
        currency=CurrencyInfo(symbol="EMT", name="easyMine"), scaling=Decimal("1e-18")
    ),
    "0x9506d37f70eb4c3d79c398d326c871abbf10521d": TokenInfo(
        currency=CurrencyInfo(symbol="MLT", name="Media Licensing Tok"), scaling=Decimal("1e-18")
    ),
    "0x95172ccbe8344fecd73d0a30f54123652981bd6f": TokenInfo(
        currency=CurrencyInfo(symbol="LOCK", name="Meridian Network"), scaling=Decimal("1e-18")
    ),
    "0x951a1070ac39851dcc07b302230a68f81929a5f1": TokenInfo(
        currency=CurrencyInfo(symbol="GTS", name="GT STAR Token"), scaling=Decimal("1e-8")
    ),
    "0x9534ad65fb398e27ac8f4251dae1780b989d136e": TokenInfo(
        currency=CurrencyInfo(symbol="PYR", name="Vulcan Forged"), scaling=Decimal("1e-18")
    ),
    "0x953e22945b416730bad05009af05b420e598e412": TokenInfo(
        currency=CurrencyInfo(symbol="GXC", name="GameXCoin"), scaling=Decimal("1e-18")
    ),
    "0x9541fd8b9b5fa97381783783cebf2f5fa793c262": TokenInfo(
        currency=CurrencyInfo(symbol="KZN", name="Kaizen"), scaling=Decimal("1e-8")
    ),
    "0x954b5de09a55e59755acbda29e1eb74a45d30175": TokenInfo(
        currency=CurrencyInfo(symbol="FLUZ", name="FluzFluz"), scaling=Decimal("1e-18")
    ),
    "0x954b890704693af242613edef1b603825afcd708": TokenInfo(
        currency=CurrencyInfo(symbol="CARD", name="Cardstack"), scaling=Decimal("1e-18")
    ),
    "0x956cdac781389d259de92e427ecd86e1cc273f7f": TokenInfo(
        currency=CurrencyInfo(symbol="BTGN", name="Bitre Mining"), scaling=Decimal("1e-8")
    ),
    "0x956eaaaacb521558cd4485115df412aa01f1057e": TokenInfo(
        currency=CurrencyInfo(symbol="HOX", name="Hug Oxytocin"), scaling=Decimal("1e-18")
    ),
    "0x956f47f50a910163d8bf957cf5846d573e7f87ca": TokenInfo(
        currency=CurrencyInfo(symbol="FEI", name="FEI"), scaling=Decimal("1e-18")
    ),
    "0x9570893324f2bbe9e774230ee3524e8928e0ce51": TokenInfo(
        currency=CurrencyInfo(symbol="TPX.CX", name="Tempur Sealy International"), scaling=Decimal("1e-8")
    ),
    "0x9570ec7ab05d61877ff7eb180f837c7c079c4844": TokenInfo(
        currency=CurrencyInfo(symbol="GAP", name="Gaps Chain"), scaling=Decimal("1e-18")
    ),
    "0x957c30ab0426e0c93cd8241e2c60392d08c6ac8e": TokenInfo(
        currency=CurrencyInfo(symbol="MOD", name="Modum"), scaling=Decimal("1e-0")
    ),
    "0x95a4492f028aa1fd432ea71146b433e7b4446611": TokenInfo(
        currency=CurrencyInfo(symbol="APY", name="APY.Finance"), scaling=Decimal("1e-18")
    ),
    "0x95aa5d2dbd3c16ee3fdea82d5c6ec3e38ce3314f": TokenInfo(
        currency=CurrencyInfo(symbol="PXP", name="PointPay"), scaling=Decimal("1e-18")
    ),
    "0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce": TokenInfo(
        currency=CurrencyInfo(symbol="SHIB", name="Shiba Inu"), scaling=Decimal("1e-18")
    ),
    "0x95ba34760ac3d7fbe98ee8b2ab33b4f1a6d18878": TokenInfo(
        currency=CurrencyInfo(symbol="DESH", name="DeCash"), scaling=Decimal("1e-18")
    ),
    "0x95c4be8534d69c248c0623c4c9a7a2a001c17337": TokenInfo(
        currency=CurrencyInfo(symbol="HDL", name="HODLER.TECH"), scaling=Decimal("1e-18")
    ),
    "0x95daaab98046846bf4b2853e23cba236fa394a31": TokenInfo(
        currency=CurrencyInfo(symbol="EMONT", name="EthermonToken"), scaling=Decimal("1e-8")
    ),
    "0x95db29acce0db3d3c9b0a1772ec13bd13138cf3f": TokenInfo(
        currency=CurrencyInfo(symbol="PROVE", name="Prove Token"), scaling=Decimal("1e-18")
    ),
    "0x95e40e065afb3059dcabe4aaf404c1f92756603a": TokenInfo(
        currency=CurrencyInfo(symbol="KDAG", name="King DAG"), scaling=Decimal("1e-18")
    ),
    "0x95e6737ef3d4a65535cdfab02f4de54d904bea0b": TokenInfo(
        currency=CurrencyInfo(symbol="ASPENCOIN", name="ER - St Regis Aspen – fragmented ownership"),
        scaling=Decimal("1e-0"),
    ),
    "0x95efd1fe6099f65a7ed524def487483221094947": TokenInfo(
        currency=CurrencyInfo(symbol="CBM", name="Crypto Bonus Miles Token"), scaling=Decimal("1e-18")
    ),
    "0x95fa5c2d804838164bdca5c188e9ffd1d8a624dc": TokenInfo(
        currency=CurrencyInfo(symbol="PONG", name="Pong Chain"), scaling=Decimal("1e-8")
    ),
    "0x96006f60b452526481a26eab55265ecdf82e7361": TokenInfo(
        currency=CurrencyInfo(symbol="HEX", name="HollaEx"), scaling=Decimal("1e-18")
    ),
    "0x960b236a07cf122663c4303350609a66a7b288c0": TokenInfo(
        currency=CurrencyInfo(symbol="ANT", name="Aragon Network Token"), scaling=Decimal("1e-18")
    ),
    "0x96184d9c811ea0624fc30c80233b1d749b9e485b": TokenInfo(
        currency=CurrencyInfo(symbol="DAPPT", name="Dapp.com"), scaling=Decimal("1e-18")
    ),
    "0x961c8c0b1aad0c0b10a51fef6a867e3091bcef17": TokenInfo(
        currency=CurrencyInfo(symbol="DYP", name="DeFi Yield Protocol"), scaling=Decimal("1e-18")
    ),
    "0x9631483f28b7f5cbf7d435ab249be8f709215bc3": TokenInfo(
        currency=CurrencyInfo(symbol="SPA", name="Sperax"), scaling=Decimal("1e-18")
    ),
    "0x9653cfd0865ad8313bea2f0c2ec0584bfd05115b": TokenInfo(
        currency=CurrencyInfo(symbol="FXE", name="FuturXe"), scaling=Decimal("1e-8")
    ),
    "0x965697b4ef02f0de01384d0d4f9f782b1670c163": TokenInfo(
        currency=CurrencyInfo(symbol="OXY", name="Oxygen"), scaling=Decimal("1e-6")
    ),
    "0x965f109d31ccb77005858defae0ebaf7b4381652": TokenInfo(
        currency=CurrencyInfo(symbol="STASH", name="BitStash"), scaling=Decimal("1e-18")
    ),
    "0x96610186f3ab8d73ebee1cf950c750f3b1fb79c2": TokenInfo(
        currency=CurrencyInfo(symbol="EJS", name="Enjinstarter"), scaling=Decimal("1e-18")
    ),
    "0x9669890e48f330acd88b78d63e1a6b3482652cd9": TokenInfo(
        currency=CurrencyInfo(symbol="BCNT", name="Bincentive"), scaling=Decimal("1e-18")
    ),
    "0x967da4048cd07ab37855c090aaf366e4ce1b9f48": TokenInfo(
        currency=CurrencyInfo(symbol="OCEAN", name="Ocean Protocol"), scaling=Decimal("1e-18")
    ),
    "0x9686b875439dd142b0f2008b6596d6313a68a937": TokenInfo(
        currency=CurrencyInfo(symbol="PS", name="Paul Sports Coin"), scaling=Decimal("1e-18")
    ),
    "0x968f6f898a6df937fc1859b323ac2f14643e3fed": TokenInfo(
        currency=CurrencyInfo(symbol="NWC", name="Newscrypto Coin"), scaling=Decimal("1e-18")
    ),
    "0x9693dded163393f18810c7a799c662998bf8bf3e": TokenInfo(
        currency=CurrencyInfo(symbol="TRON", name="Bitcoin Tron"), scaling=Decimal("1e-18")
    ),
    "0x9695e0114e12c0d3a3636fab5a18e6b737529023": TokenInfo(
        currency=CurrencyInfo(symbol="DFYN", name="Dfyn Network"), scaling=Decimal("1e-18")
    ),
    "0x96a65609a7b84e8842732deb08f56c3e21ac6f8a": TokenInfo(
        currency=CurrencyInfo(symbol="Centra", name="Centra token"), scaling=Decimal("1e-18")
    ),
    "0x96b0bf939d9460095c15251f71fda11e41dcbddb": TokenInfo(
        currency=CurrencyInfo(symbol="S", name="Sharpay"), scaling=Decimal("1e-18")
    ),
    "0x96b52b5bf8d902252d0714a1bd2651a785fd2660": TokenInfo(
        currency=CurrencyInfo(symbol="ETHBN", name="EtherBone"), scaling=Decimal("1e-18")
    ),
    "0x96c30d5499ef6ea96a9c221bc18bc39d29c97f27": TokenInfo(
        currency=CurrencyInfo(symbol="Thar", name="Thar token"), scaling=Decimal("1e-18")
    ),
    "0x96c645d3d3706f793ef52c19bbace441900ed47d": TokenInfo(
        currency=CurrencyInfo(symbol="MPS", name="Mt Pelerin Shares"), scaling=Decimal("1e-0")
    ),
    "0x96d62cdcd1cc49cb6ee99c867cb8812bea86b9fa": TokenInfo(
        currency=CurrencyInfo(symbol="YFP", name="Yearn Finance Protocol"), scaling=Decimal("1e-18")
    ),
    "0x96e322f2a4f151cd898f86ea5626cc6e10090c76": TokenInfo(
        currency=CurrencyInfo(symbol="IAG", name="Iagon"), scaling=Decimal("1e-18")
    ),
    "0x96e61422b6a9ba0e068b6c5add4ffabc6a4aae27": TokenInfo(
        currency=CurrencyInfo(symbol="IBEUR", name="Iron Bank EURO"), scaling=Decimal("1e-18")
    ),
    "0x96ee9b27f822d71ae9cbf06773a878b41308c396": TokenInfo(
        currency=CurrencyInfo(symbol="CSNP", name="CrowdSale Network"), scaling=Decimal("1e-18")
    ),
    "0x96ef7f9cf1b6ecc66e482a6598fc9f009e9277da": TokenInfo(
        currency=CurrencyInfo(symbol="POMI", name="Pomi"), scaling=Decimal("1e-8")
    ),
    "0x9709bb5ce25fcd6f9786d3e4ccf422717367473c": TokenInfo(
        currency=CurrencyInfo(symbol="MFBT", name="MoFlux - Boomtown Set II"), scaling=Decimal("1e-18")
    ),
    "0x970b9bb2c0444f5e81e9d0efb84c8ccdcdcaf84d": TokenInfo(
        currency=CurrencyInfo(symbol="FUSE", name="Fuse"), scaling=Decimal("1e-18")
    ),
    "0x970e035e2a013cf4becd67e300d65bc32a56d826": TokenInfo(
        currency=CurrencyInfo(symbol="BOE", name="Bodhi [ETH]"), scaling=Decimal("1e-8")
    ),
    "0x971d048e737619884f2df75e31c7eb6412392328": TokenInfo(
        currency=CurrencyInfo(symbol="SPRK", name="Sparkster"), scaling=Decimal("1e-18")
    ),
    "0x9720b467a710382a232a32f540bdced7d662a10b": TokenInfo(
        currency=CurrencyInfo(symbol="VZT", name="Vezt"), scaling=Decimal("1e-18")
    ),
    "0x9730eeee01d9068e8c37fc2e92045295a617b329": TokenInfo(
        currency=CurrencyInfo(symbol="NEM.CX", name="Newmont Mining"), scaling=Decimal("1e-8")
    ),
    "0x973b569b1d025c41cd9c19cbf8f931175e874dd0": TokenInfo(
        currency=CurrencyInfo(symbol="BOOM", name="BOOM"), scaling=Decimal("1e-8")
    ),
    "0x973e52691176d36453868d9d86572788d27041a9": TokenInfo(
        currency=CurrencyInfo(symbol="DX", name="DxChain Token"), scaling=Decimal("1e-18")
    ),
    "0x9741eaa28c446e87ec859ad871f85ac9b62a983c": TokenInfo(
        currency=CurrencyInfo(symbol="ACOIN", name="Aladdin Coins"), scaling=Decimal("1e-18")
    ),
    "0x9746953f5b1324a78132895cfd263f417b0faae3": TokenInfo(
        currency=CurrencyInfo(symbol="VCT", name="ValueCyberToken"), scaling=Decimal("1e-18")
    ),
    "0x974c98bc2e82fa18de92b7e697a1d9bd25682e80": TokenInfo(
        currency=CurrencyInfo(symbol="ETCBULL", name="3X Long Ethereum Classic Token"), scaling=Decimal("1e-18")
    ),
    "0x975ce667d59318e13da8acd3d2f534be5a64087b": TokenInfo(
        currency=CurrencyInfo(symbol="TWOB", name="The Whale of Blockchain"), scaling=Decimal("1e-18")
    ),
    "0x976010db5538f0c1daf9f3855b8504721a23e5d4": TokenInfo(
        currency=CurrencyInfo(symbol="DBB", name="Document Bill Bit"), scaling=Decimal("1e-18")
    ),
    "0x97872eafd79940c7b24f7bcc1eadb1457347adc9": TokenInfo(
        currency=CurrencyInfo(symbol="STRP", name="Strips Finance"), scaling=Decimal("1e-18")
    ),
    "0x97941ff1962026955852e9609e202d1058bc0f48": TokenInfo(
        currency=CurrencyInfo(symbol="VNS", name="Va Na Su"), scaling=Decimal("1e-8")
    ),
    "0x979aca85ba37c675e78322ed5d97fa980b9bdf00": TokenInfo(
        currency=CurrencyInfo(symbol="FSN", name="FUSION"), scaling=Decimal("1e-18")
    ),
    "0x97aeb5066e1a590e868b511457beb6fe99d329f5": TokenInfo(
        currency=CurrencyInfo(symbol="ATMI", name="Atonomi"), scaling=Decimal("1e-18")
    ),
    "0x97af10d3fc7c70f67711bf715d8397c6da79c1ab": TokenInfo(
        currency=CurrencyInfo(symbol="DIP", name="Dipper Network"), scaling=Decimal("1e-12")
    ),
    "0x97bdd9fdfa0b1677a2a353848514d93c108bec85": TokenInfo(
        currency=CurrencyInfo(symbol="LPS", name="Lapis Chain"), scaling=Decimal("1e-10")
    ),
    "0x97c4025aae58b8530ec86368101fdece17433b33": TokenInfo(
        currency=CurrencyInfo(symbol="GW", name="Global Players World"), scaling=Decimal("1e-8")
    ),
    "0x97cb5cc1b2e10cc56dc16ab9179f06dfedbe41a2": TokenInfo(
        currency=CurrencyInfo(symbol="MOLK", name="MobilinkToken"), scaling=Decimal("1e-18")
    ),
    "0x97fb6fc2ad532033af97043b563131c5204f8a35": TokenInfo(
        currency=CurrencyInfo(symbol="NPLC", name="Plus Coin"), scaling=Decimal("1e-18")
    ),
    "0x97fe22e7341a0cd8db6f6c021a24dc8f4dad855f": TokenInfo(
        currency=CurrencyInfo(symbol="SGBP", name="sGBP"), scaling=Decimal("1e-18")
    ),
    "0x980e45ab37c6bcaf93fe911b3e207e08a3a60b5e": TokenInfo(
        currency=CurrencyInfo(symbol="SIBU", name="SIBU"), scaling=Decimal("1e-2")
    ),
    "0x9813037ee2218799597d83d4a5b6f3b6778218d9": TokenInfo(
        currency=CurrencyInfo(symbol="BONE", name="Bone ShibaSwap"), scaling=Decimal("1e-18")
    ),
    "0x9827f6e8df0ccc584ff7b37144de8bac7c446385": TokenInfo(
        currency=CurrencyInfo(symbol="KTC", name="Kitcoin"), scaling=Decimal("1e-18")
    ),
    "0x983f6d60db79ea8ca4eb9968c6aff8cfa04b3c63": TokenInfo(
        currency=CurrencyInfo(symbol="SNM", name="SONM"), scaling=Decimal("1e-18")
    ),
    "0x9847345de8b614c956146bbea549336d9c8d26b6": TokenInfo(
        currency=CurrencyInfo(symbol="GULD", name="GULD ERC20"), scaling=Decimal("1e-8")
    ),
    "0x984c134a8809571993fd1573fb99f06dc61e216f": TokenInfo(
        currency=CurrencyInfo(symbol="ACG", name="Art Chain Global"), scaling=Decimal("1e-8")
    ),
    "0x985dd3d42de1e256d09e1c10f112bccb8015ad41": TokenInfo(
        currency=CurrencyInfo(symbol="OCEAN", name="OceanToken"), scaling=Decimal("1e-18")
    ),
    "0x98626e2c9231f03504273d55f397409defd4a093": TokenInfo(
        currency=CurrencyInfo(symbol="DEV", name="Dev"), scaling=Decimal("1e-18")
    ),
    "0x986ee2b944c42d017f52af21c4c69b84dbea35d8": TokenInfo(
        currency=CurrencyInfo(symbol="BMX", name="BitMart Token"), scaling=Decimal("1e-18")
    ),
    "0x9885ca101dfd8f23d364874f799554c52bfee820": TokenInfo(
        currency=CurrencyInfo(symbol="BTMXBULL", name="3X Long BitMax Token Token"), scaling=Decimal("1e-18")
    ),
    "0x989ac4c1fc5ab2b8c86924c6253aaf1ee68e9ce9": TokenInfo(
        currency=CurrencyInfo(symbol="PFI", name="Prime Finance"), scaling=Decimal("1e-18")
    ),
    "0x989ebc2b7e1e16f1ececd9a4fad931618c12ce36": TokenInfo(
        currency=CurrencyInfo(symbol="UNI-V2", name="Uniswap V2"), scaling=Decimal("1e-18")
    ),
    "0x98a1208a9287e378d329225836b823481d890409": TokenInfo(
        currency=CurrencyInfo(symbol="ZBLT", name="ZEBELLION"), scaling=Decimal("1e-18")
    ),
    "0x98a90499b62ae48e151a66b0f647570b5a473b1c": TokenInfo(
        currency=CurrencyInfo(symbol="ZAC", name="ZAC Finance"), scaling=Decimal("1e-18")
    ),
    "0x98ad9b32dd10f8d8486927d846d4df8baf39abe2": TokenInfo(
        currency=CurrencyInfo(symbol="VLO", name="VELO Token"), scaling=Decimal("1e-18")
    ),
    "0x98b2de885e916b598f65ded2fdbb63187eaef184": TokenInfo(
        currency=CurrencyInfo(symbol="DEFI", name="Defi"), scaling=Decimal("1e-18")
    ),
    "0x98b89a9947a668c1baa48382de7f4a952ef37b53": TokenInfo(
        currency=CurrencyInfo(symbol="PKO", name="PUKAO GLOBAL"), scaling=Decimal("1e-18")
    ),
    "0x98cc3bd6af1880fcfda17ac477b2f612980e5e33": TokenInfo(
        currency=CurrencyInfo(symbol="OCDAI", name="Opyn cDai Insurance"), scaling=Decimal("1e-8")
    ),
    "0x98d0cde5c3d79531613e18f0912127bf172bd7aa": TokenInfo(
        currency=CurrencyInfo(symbol="ATG", name="Biotech Token"), scaling=Decimal("1e-18")
    ),
    "0x98d8d146e644171cd47ff8588987b7bdeef72a87": TokenInfo(
        currency=CurrencyInfo(symbol="BXA", name="Blockchain Exchange Alliance"), scaling=Decimal("1e-18")
    ),
    "0x98e0438d3ee1404fea48e38e92853bb08cfa68bd": TokenInfo(
        currency=CurrencyInfo(symbol="TVT", name="TVT"), scaling=Decimal("1e-8")
    ),
    "0x98f5e9b7f0e33956c0443e81bf7deb8b5b1ed545": TokenInfo(
        currency=CurrencyInfo(symbol="SEXY", name="Sexy Token"), scaling=Decimal("1e-18")
    ),
    "0x9903a4cd589da8e434f264deafc406836418578e": TokenInfo(
        currency=CurrencyInfo(symbol="FIRST", name="Harrison First"), scaling=Decimal("1e-4")
    ),
    "0x990f341946a3fdb507ae7e52d17851b87168017c": TokenInfo(
        currency=CurrencyInfo(symbol="STRONG", name="Strong"), scaling=Decimal("1e-18")
    ),
    "0x9910f4aed4a7550a4120ad7da8df8b56e91197fa": TokenInfo(
        currency=CurrencyInfo(symbol="TCST", name="TradeCloud Security Token"), scaling=Decimal("1e-0")
    ),
    "0x99295f1141d58a99e939f7be6bbe734916a875b8": TokenInfo(
        currency=CurrencyInfo(symbol="LPL", name="LinkPool"), scaling=Decimal("1e-18")
    ),
    "0x993864e43caa7f7f12953ad6feb1d1ca635b875f": TokenInfo(
        currency=CurrencyInfo(symbol="SDAO", name="SingularityDAO"), scaling=Decimal("1e-18")
    ),
    "0x9945e8d665365a3b27654f27a7cfe6d70b2cb9b5": TokenInfo(
        currency=CurrencyInfo(symbol="TTWO.CX", name="Take-Two Interactive Software, Inc."), scaling=Decimal("1e-8")
    ),
    "0x9947a675cb4d4a19e020e1dd035955c0150b1e5e": TokenInfo(
        currency=CurrencyInfo(symbol="COVC", name="COVIDCoin"), scaling=Decimal("1e-18")
    ),
    "0x994f0dffdbae0bbf09b652d6f11a493fd33f42b9": TokenInfo(
        currency=CurrencyInfo(symbol="EAGLE", name="EagleCoin"), scaling=Decimal("1e-18")
    ),
    "0x9954ff0295443c01f562dccb1f893be464e01986": TokenInfo(
        currency=CurrencyInfo(symbol="pahoo", name="pahoo"), scaling=Decimal("1e-18")
    ),
    "0x995de3d961b40ec6cdee0009059d48768ccbdd48": TokenInfo(
        currency=CurrencyInfo(symbol="UFC", name="Union Fair Coin"), scaling=Decimal("1e-8")
    ),
    "0x996229d0c6a485c7f4b52e092eaa907cb2def5c6": TokenInfo(
        currency=CurrencyInfo(symbol="BHIG", name="BuckHath Coin"), scaling=Decimal("1e-18")
    ),
    "0x996dc5dfc819408dd98cd92c9a76f64b0738dc3d": TokenInfo(
        currency=CurrencyInfo(symbol="SKI", name="Skillchain"), scaling=Decimal("1e-18")
    ),
    "0x997080b8ee7d75fba23f3ec794df99da646c87ec": TokenInfo(
        currency=CurrencyInfo(symbol="ESTN", name="ESTONN"), scaling=Decimal("1e-18")
    ),
    "0x9972a0f24194447e73a7e8b6cd26a52e02ddfad5": TokenInfo(
        currency=CurrencyInfo(symbol="TCH", name="Thorecash (ERC-20)"), scaling=Decimal("1e-0")
    ),
    "0x998b3b82bc9dba173990be7afb772788b5acb8bd": TokenInfo(
        currency=CurrencyInfo(symbol="BANCA", name="Banca"), scaling=Decimal("1e-18")
    ),
    "0x998ffe1e43facffb941dc337dd0468d52ba5b48a": TokenInfo(
        currency=CurrencyInfo(symbol="IDRT", name="Rupiah Token"), scaling=Decimal("1e-2")
    ),
    "0x9992ec3cf6a55b00978cddf2b27bc6882d88d1ec": TokenInfo(
        currency=CurrencyInfo(symbol="POLY", name="Polymath Network"), scaling=Decimal("1e-18")
    ),
    "0x99963ee76c886fc43d5063428ff8f926e8a50985": TokenInfo(
        currency=CurrencyInfo(symbol="NVZN", name="INVIZION"), scaling=Decimal("1e-18")
    ),
    "0x999967e2ec8a74b7c8e9db19e039d920b31d39d0": TokenInfo(
        currency=CurrencyInfo(symbol="TIE", name="Ties.DB"), scaling=Decimal("1e-18")
    ),
    "0x99bc08db67f52010f2d6017b7ad968808113db10": TokenInfo(
        currency=CurrencyInfo(symbol="APOD", name="AirPod"), scaling=Decimal("1e-18")
    ),
    "0x99c6e435ec259a7e8d65e1955c9423db624ba54c": TokenInfo(
        currency=CurrencyInfo(symbol="FMT", name="FMT"), scaling=Decimal("1e-18")
    ),
    "0x99d1f0f82c028bf4e017dd397a05bd860fc6edfb": TokenInfo(
        currency=CurrencyInfo(symbol="WDAY.CX", name="Workday Inc"), scaling=Decimal("1e-8")
    ),
    "0x99d8a9c45b2eca8864373a26d1459e3dff1e17f3": TokenInfo(
        currency=CurrencyInfo(symbol="MIM", name="Magic Internet Mone"), scaling=Decimal("1e-18")
    ),
    "0x99ea4db9ee77acd40b119bd1dc4e33e1c070b80d": TokenInfo(
        currency=CurrencyInfo(symbol="QSP", name="Quantstamp"), scaling=Decimal("1e-18")
    ),
    "0x99f653292d2343c92e72212dc5ccddfb04c6368b": TokenInfo(
        currency=CurrencyInfo(symbol="SYY.CX", name="Sysco"), scaling=Decimal("1e-8")
    ),
    "0x99fe3b1391503a1bc1788051347a1324bff41452": TokenInfo(
        currency=CurrencyInfo(symbol="SX", name="SportX"), scaling=Decimal("1e-18")
    ),
    "0x9a005c9a89bd72a4bd27721e7a09a3c11d2b03c4": TokenInfo(
        currency=CurrencyInfo(symbol="STC", name="CoinStarter"), scaling=Decimal("1e-18")
    ),
    "0x9a0242b7a33dacbe40edb927834f96eb39f8fbcb": TokenInfo(
        currency=CurrencyInfo(symbol="BAX", name="BABB"), scaling=Decimal("1e-18")
    ),
    "0x9a0587eae7ef64b2b38a10442a44cfa43edd7d2a": TokenInfo(
        currency=CurrencyInfo(symbol="WTL", name="Welltrado"), scaling=Decimal("1e-18")
    ),
    "0x9a0aba393aac4dfbff4333b06c407458002c6183": TokenInfo(
        currency=CurrencyInfo(symbol="AC", name="ACoconut"), scaling=Decimal("1e-18")
    ),
    "0x9a1997c130f4b2997166975d9aff92797d5134c2": TokenInfo(
        currency=CurrencyInfo(symbol="USDAP", name="Bond Appetite USD"), scaling=Decimal("1e-18")
    ),
    "0x9a1bf361798ef6538ccb8137ea900c4d4b48ca3d": TokenInfo(
        currency=CurrencyInfo(symbol="CNTM", name="Connectome Token"), scaling=Decimal("1e-18")
    ),
    "0x9a24b8e8a6d4563c575a707b1275381119298e60": TokenInfo(
        currency=CurrencyInfo(symbol="EVNY", name="EVNY Token"), scaling=Decimal("1e-18")
    ),
    "0x9a3619499825fbae63329aa8bcb3f10cd5958e1c": TokenInfo(
        currency=CurrencyInfo(symbol="JBD", name="Jubilee Dollar"), scaling=Decimal("1e-10")
    ),
    "0x9a387c22cefc08ce815e0e8e5841c98537e4d039": TokenInfo(
        currency=CurrencyInfo(symbol="SPN3.CX", name="Spain 35"), scaling=Decimal("1e-8")
    ),
    "0x9a3f91237408ecb94e21e4c293010347f80a136f": TokenInfo(
        currency=CurrencyInfo(symbol="MKC", name="Medical Link Chain"), scaling=Decimal("1e-18")
    ),
    "0x9a48bd0ec040ea4f1d3147c025cd4076a2e71e3e": TokenInfo(
        currency=CurrencyInfo(symbol="USD++", name="PieDAO USD++"), scaling=Decimal("1e-18")
    ),
    "0x9a49f02e128a8e989b443a8f94843c0918bf45e7": TokenInfo(
        currency=CurrencyInfo(symbol="TOK", name="Tokok"), scaling=Decimal("1e-8")
    ),
    "0x9a5ff62fd25b5fec3409cca1d5762b976293dd89": TokenInfo(
        currency=CurrencyInfo(symbol="CBK.CX", name="Commerzbank AG"), scaling=Decimal("1e-8")
    ),
    "0x9a642d6b3368ddc662ca244badf32cda716005bc": TokenInfo(
        currency=CurrencyInfo(symbol="QTUM", name="Qtum"), scaling=Decimal("1e-18")
    ),
    "0x9a794dc1939f1d78fa48613b89b8f9d0a20da00e": TokenInfo(
        currency=CurrencyInfo(symbol="ABX", name="Arbidex"), scaling=Decimal("1e-18")
    ),
    "0x9a882ddd550b9e1a211c849496d1ccb7bbcc32ae": TokenInfo(
        currency=CurrencyInfo(symbol="PNC.CX", name="PNC Financial Services Group"), scaling=Decimal("1e-8")
    ),
    "0x9a96e767bfcce8e80370be00821ed5ba283d4a17": TokenInfo(
        currency=CurrencyInfo(symbol="GOGO", name="GOGO Finance"), scaling=Decimal("1e-18")
    ),
    "0x9a9bb9b4b11bf8eccff84b58a6ccccd4058a7f0d": TokenInfo(
        currency=CurrencyInfo(symbol="VD", name="Bitcoin Card"), scaling=Decimal("1e-8")
    ),
    "0x9aa7d119bdf77f65a7284581a211d8c44ffb04b4": TokenInfo(
        currency=CurrencyInfo(symbol="GIRL", name="Girl Coin"), scaling=Decimal("1e-18")
    ),
    "0x9aab071b4129b083b01cb5a0cb513ce7eca26fa5": TokenInfo(
        currency=CurrencyInfo(symbol="HUNT", name="HUNT"), scaling=Decimal("1e-18")
    ),
    "0x9ab165d795019b6d8b3e971dda91071421305e5a": TokenInfo(
        currency=CurrencyInfo(symbol="AOA", name="Aurora"), scaling=Decimal("1e-18")
    ),
    "0x9ab7bb7fdc60f4357ecfef43986818a2a3569c62": TokenInfo(
        currency=CurrencyInfo(symbol="GOG", name="Guild of Guardians"), scaling=Decimal("1e-18")
    ),
    "0x9ad685a3eaa6b0a1ea601f48b7797a12011fdeb0": TokenInfo(
        currency=CurrencyInfo(symbol="TRDS", name="Traders Token"), scaling=Decimal("1e-3")
    ),
    "0x9aeb50f542050172359a0e1a25a9933bc8c01259": TokenInfo(
        currency=CurrencyInfo(symbol="OIN", name="OIN Finance"), scaling=Decimal("1e-8")
    ),
    "0x9aefbe0b3c3ba9eab262cb9856e8157ab7648e09": TokenInfo(
        currency=CurrencyInfo(symbol="FLR", name="Flair Coin"), scaling=Decimal("1e-18")
    ),
    "0x9af15d7b8776fa296019979e70a5be53c714a7ec": TokenInfo(
        currency=CurrencyInfo(symbol="EVN", name="Evolution Finance"), scaling=Decimal("1e-18")
    ),
    "0x9af4f26941677c706cfecf6d3379ff01bb85d5ab": TokenInfo(
        currency=CurrencyInfo(symbol="DRT", name="DomRaider"), scaling=Decimal("1e-8")
    ),
    "0x9af5a20aac8d83230ba68542ba29d132d50cbe08": TokenInfo(
        currency=CurrencyInfo(symbol="MRS", name="Marsan Exchange Token"), scaling=Decimal("1e-18")
    ),
    "0x9af839687f6c94542ac5ece2e317daae355493a1": TokenInfo(
        currency=CurrencyInfo(symbol="HOT", name="Hydro Protocol"), scaling=Decimal("1e-18")
    ),
    "0x9b02dd390a603add5c07f9fd9175b7dabe8d63b7": TokenInfo(
        currency=CurrencyInfo(symbol="SPI", name="Shopping.io"), scaling=Decimal("1e-18")
    ),
    "0x9b06d48e0529ecf05905ff52dd426ebec0ea3011": TokenInfo(
        currency=CurrencyInfo(symbol="XSP", name="XSwap"), scaling=Decimal("1e-18")
    ),
    "0x9b11efcaaa1890f6ee52c6bb7cf8153ac5d74139": TokenInfo(
        currency=CurrencyInfo(symbol="ATM", name="ATMChain"), scaling=Decimal("1e-8")
    ),
    "0x9b17baadf0f21f03e35249e0e59723f34994f806": TokenInfo(
        currency=CurrencyInfo(symbol="GEM", name="NFTmall"), scaling=Decimal("1e-18")
    ),
    "0x9b1b1e109ff130b298cf1d47389c47569f5c2932": TokenInfo(
        currency=CurrencyInfo(symbol="BION", name="Biido"), scaling=Decimal("1e-18")
    ),
    "0x9b20dabcec77f6289113e61893f7beefaeb1990a": TokenInfo(
        currency=CurrencyInfo(symbol="FAIR", name="FairGame"), scaling=Decimal("1e-18")
    ),
    "0x9b31bb425d8263fa1b8b9d090b83cf0c31665355": TokenInfo(
        currency=CurrencyInfo(symbol="CPD", name="CoinsPaid"), scaling=Decimal("1e-18")
    ),
    "0x9b39a0b97319a9bd5fed217c1db7b030453bac91": TokenInfo(
        currency=CurrencyInfo(symbol="TCH", name="TigerCash"), scaling=Decimal("1e-18")
    ),
    "0x9b4a295282ab64f284787b43e706722c1ad78c45": TokenInfo(
        currency=CurrencyInfo(symbol="UST", name="Universal Shield Token"), scaling=Decimal("1e-6")
    ),
    "0x9b4e2b4b13d125238aa0480dd42b4f6fc71b37cc": TokenInfo(
        currency=CurrencyInfo(symbol="MT", name="MyToken"), scaling=Decimal("1e-18")
    ),
    "0x9b53e429b0badd98ef7f01f03702986c516a5715": TokenInfo(
        currency=CurrencyInfo(symbol="HY", name="Hybrix"), scaling=Decimal("1e-18")
    ),
    "0x9b5c2be869a19e84bdbcb1386dad83a2ec8dae82": TokenInfo(
        currency=CurrencyInfo(symbol="STPL", name="Stream Protocol"), scaling=Decimal("1e-18")
    ),
    "0x9b62513c8a27290cf6a7a9e29386e600245ea819": TokenInfo(
        currency=CurrencyInfo(symbol="CPT", name="Contents Protocol"), scaling=Decimal("1e-18")
    ),
    "0x9b639486f4a40c1a7a6728114f2413973f5fa4c6": TokenInfo(
        currency=CurrencyInfo(symbol="EMP", name="Electronic Move Pay"), scaling=Decimal("1e-18")
    ),
    "0x9b6443b0fb9c241a7fdac375595cea13e6b7807a": TokenInfo(
        currency=CurrencyInfo(symbol="RCC", name="Reality Clash"), scaling=Decimal("1e-18")
    ),
    "0x9b68bfae21df5a510931a262cecf63f41338f264": TokenInfo(
        currency=CurrencyInfo(symbol="DBET", name="DecentBet"), scaling=Decimal("1e-18")
    ),
    "0x9b70740e708a083c6ff38df52297020f5dfaa5ee": TokenInfo(
        currency=CurrencyInfo(symbol="DAN", name="Daneel"), scaling=Decimal("1e-10")
    ),
    "0x9b8c184439245b7bb24a5b2ec51ec81c39589e8a": TokenInfo(
        currency=CurrencyInfo(symbol="KMX", name="KIMEX"), scaling=Decimal("1e-18")
    ),
    "0x9b8d5f3402f74c7a61d9f09c32d3ca07b45c1466": TokenInfo(
        currency=CurrencyInfo(symbol="GMR", name="Gimmer"), scaling=Decimal("1e-18")
    ),
    "0x9b9087756eca997c5d595c840263001c9a26646d": TokenInfo(
        currency=CurrencyInfo(symbol="DOGEFI", name="DogeFi"), scaling=Decimal("1e-18")
    ),
    "0x9b99cca871be05119b2012fd4474731dd653febe": TokenInfo(
        currency=CurrencyInfo(symbol="MATTER", name="AntiMatter"), scaling=Decimal("1e-18")
    ),
    "0x9ba00d6856a4edf4665bca2c2309936572473b7e": TokenInfo(
        currency=CurrencyInfo(symbol="AUSDC", name="Aave USDC v1"), scaling=Decimal("1e-6")
    ),
    "0x9ba60ba98413a60db4c651d4afe5c937bbd8044b": TokenInfo(
        currency=CurrencyInfo(symbol="YLA", name="Yearn Lazy Ape"), scaling=Decimal("1e-18")
    ),
    "0x9bb1db1445b83213a56d90d331894b3f26218e4e": TokenInfo(
        currency=CurrencyInfo(symbol="HIBT", name="HiBTCToken"), scaling=Decimal("1e-18")
    ),
    "0x9bc0b36cdedadb9ae906f53bdea6debe20b81b8e": TokenInfo(
        currency=CurrencyInfo(symbol="PXL", name="PixelPropertyToken"), scaling=Decimal("1e-0")
    ),
    "0x9bd4f0b2c73b5e2bef9f1ab0841e5c460cf8cedc": TokenInfo(
        currency=CurrencyInfo(symbol="GCM", name="Global Coin Market"), scaling=Decimal("1e-0")
    ),
    "0x9be89d2a4cd102d8fecc6bf9da793be995c22541": TokenInfo(
        currency=CurrencyInfo(symbol="BBTC", name="Binance Wrapped BTC"), scaling=Decimal("1e-8")
    ),
    "0x9bfb088c9f311415e3f9b507da73081c52a49d8c": TokenInfo(
        currency=CurrencyInfo(symbol="TAPE", name="BOY Cassette Tape by RAC"), scaling=Decimal("1e-18")
    ),
    "0x9bfedc30a3930b709c0fcb01c5c59733b64ac827": TokenInfo(
        currency=CurrencyInfo(symbol="FIT", name="Facite"), scaling=Decimal("1e-18")
    ),
    "0x9c10b6d9a92e8cda1179f20a637f748e965f64e7": TokenInfo(
        currency=CurrencyInfo(symbol="KON", name="Konios"), scaling=Decimal("1e-18")
    ),
    "0x9c13833483885455bd8767b20f8bd39fa76fbb9c": TokenInfo(
        currency=CurrencyInfo(symbol="BBY.CX", name="Best Buy"), scaling=Decimal("1e-8")
    ),
    "0x9c197c4b58527faaab67cb35e3145166b23d242e": TokenInfo(
        currency=CurrencyInfo(symbol="HNB", name="HashNet BitEco"), scaling=Decimal("1e-18")
    ),
    "0x9c23d67aea7b95d80942e3836bcdf7e708a747c2": TokenInfo(
        currency=CurrencyInfo(symbol="LOCI", name="LOCIcoin"), scaling=Decimal("1e-18")
    ),
    "0x9c2d9be4bb7352d2eca65675067f9e6194e597b5": TokenInfo(
        currency=CurrencyInfo(symbol="BARIN", name="BARIN"), scaling=Decimal("1e-18")
    ),
    "0x9c2dc0c3cc2badde84b0025cf4df1c5af288d835": TokenInfo(
        currency=CurrencyInfo(symbol="COR", name="Coreto"), scaling=Decimal("1e-18")
    ),
    "0x9c405acf8688afb61b3197421cdeec1a266c6839": TokenInfo(
        currency=CurrencyInfo(symbol="DOGY", name="DogeYield"), scaling=Decimal("1e-18")
    ),
    "0x9c4a4204b79dd291d6b6571c5be8bbcd0622f050": TokenInfo(
        currency=CurrencyInfo(symbol="TCR", name="Tracer DAO"), scaling=Decimal("1e-18")
    ),
    "0x9c664f20c0a00a4949dffca76748c02754c875aa": TokenInfo(
        currency=CurrencyInfo(symbol="YSKF", name="Yearn Shark Finance"), scaling=Decimal("1e-18")
    ),
    "0x9c78ee466d6cb57a4d01fd887d2b5dfb2d46288f": TokenInfo(
        currency=CurrencyInfo(symbol="MUST", name="Must"), scaling=Decimal("1e-18")
    ),
    "0x9c794f933b4dd8b49031a79b0f924d68bef43992": TokenInfo(
        currency=CurrencyInfo(symbol="XTRD", name="XTRD"), scaling=Decimal("1e-18")
    ),
    "0x9c9fe3bd60b22a9735908b9589011e78f2025c11": TokenInfo(
        currency=CurrencyInfo(symbol="HNST", name="Honest"), scaling=Decimal("1e-18")
    ),
    "0x9cb085053fae27adda04c09e2ba1af61489bf741": TokenInfo(
        currency=CurrencyInfo(symbol="SATOS", name="Satowallet Shares"), scaling=Decimal("1e-8")
    ),
    "0x9cb1aeafcc8a9406632c5b084246ea72f62d37b6": TokenInfo(
        currency=CurrencyInfo(symbol="LBK", name="LBK"), scaling=Decimal("1e-8")
    ),
    "0x9cb2f26a23b8d89973f08c957c4d7cdf75cd341c": TokenInfo(
        currency=CurrencyInfo(symbol="DZAR", name="Digital Rand"), scaling=Decimal("1e-6")
    ),
    "0x9cd39da8f25ec50cf2ee260e464ac23ea23f6bb0": TokenInfo(
        currency=CurrencyInfo(symbol="YFT", name="Toshify.finance"), scaling=Decimal("1e-18")
    ),
    "0x9cda8a60dd5afa156c95bd974428d91a0812e054": TokenInfo(
        currency=CurrencyInfo(symbol="TTU", name="TaTaTu"), scaling=Decimal("1e-18")
    ),
    "0x9ceb84f92a0561fa3cc4132ab9c0b76a59787544": TokenInfo(
        currency=CurrencyInfo(symbol="DOKI", name="Doki Doki"), scaling=Decimal("1e-18")
    ),
    "0x9cec335cf6922eeb5a563c871d1f09f2cf264230": TokenInfo(
        currency=CurrencyInfo(symbol="NIOX", name="Autonio"), scaling=Decimal("1e-4")
    ),
    "0x9cec686ba6f07d6135b2091140c795166ef5b761": TokenInfo(
        currency=CurrencyInfo(symbol="SVCS", name="GivingToServices"), scaling=Decimal("1e-18")
    ),
    "0x9d03393d297e42c135625d450c814892505f1a84": TokenInfo(
        currency=CurrencyInfo(symbol="MDX", name="Mandala Token"), scaling=Decimal("1e-18")
    ),
    "0x9d0b65a76274645b29e4cc41b8f23081fa09f4a3": TokenInfo(
        currency=CurrencyInfo(symbol="LIME", name="iMe Lab"), scaling=Decimal("1e-18")
    ),
    "0x9d1233cc46795e94029fda81aaadc1455d510f15": TokenInfo(
        currency=CurrencyInfo(symbol="ZAI", name="Zero Collateral Dai"), scaling=Decimal("1e-18")
    ),
    "0x9d1555d8cb3c846bb4f7d5b1b1080872c3166676": TokenInfo(
        currency=CurrencyInfo(symbol="MSLV", name="Mirrored iShares Silver Trust"), scaling=Decimal("1e-18")
    ),
    "0x9d1a62c2ad99019768b9126fda004a9952853f6e": TokenInfo(
        currency=CurrencyInfo(symbol="BNBBULL", name="3X Long BNB Token"), scaling=Decimal("1e-18")
    ),
    "0x9d22c3bf2b51213a3572e865ecf78fab0294e75b": TokenInfo(
        currency=CurrencyInfo(symbol="KCY", name="KickCity"), scaling=Decimal("1e-18")
    ),
    "0x9d24364b97270961b2948734afe8d58832efd43a": TokenInfo(
        currency=CurrencyInfo(symbol="FAM", name="Yefam.Finance"), scaling=Decimal("1e-18")
    ),
    "0x9d29bd441e9da3eff48568aea1348383544547e7": TokenInfo(
        currency=CurrencyInfo(symbol="TBUX", name="TrumpBux"), scaling=Decimal("1e-18")
    ),
    "0x9d3571f685e0fec61925b248977a09f8da047f48": TokenInfo(
        currency=CurrencyInfo(symbol="ZAM", name="ZAMRUD"), scaling=Decimal("1e-18")
    ),
    "0x9d3e0892d11f19f5181d4a4c5d04187a9e0d7032": TokenInfo(
        currency=CurrencyInfo(symbol="DRGB", name="Dragonbit"), scaling=Decimal("1e-18")
    ),
    "0x9d409a0a012cfba9b15f6d4b36ac57a46966ab9a": TokenInfo(
        currency=CurrencyInfo(symbol="YVBOOST", name="Yearn Compounding v"), scaling=Decimal("1e-18")
    ),
    "0x9d47894f8becb68b9cf3428d256311affe8b068b": TokenInfo(
        currency=CurrencyInfo(symbol="$ROPE", name="Rope"), scaling=Decimal("1e-18")
    ),
    "0x9d4a6860830bb62459fe8528fd249d972ddff6c4": TokenInfo(
        currency=CurrencyInfo(symbol="TGT.CX", name="Target Corp"), scaling=Decimal("1e-8")
    ),
    "0x9d5e6b92ba3f75589943372df82dbd3a8a802e80": TokenInfo(
        currency=CurrencyInfo(symbol="FPT", name="FINPLE"), scaling=Decimal("1e-18")
    ),
    "0x9d707701a56655202379f6b4ca5109bcc1c3d7ec": TokenInfo(
        currency=CurrencyInfo(symbol="SKD", name="STAKD Token"), scaling=Decimal("1e-18")
    ),
    "0x9d7630adf7ab0b0cb00af747db76864df0ec82e4": TokenInfo(
        currency=CurrencyInfo(symbol="GATE", name="GATE Token"), scaling=Decimal("1e-18")
    ),
    "0x9d79d5b61de59d882ce90125b18f74af650acb93": TokenInfo(
        currency=CurrencyInfo(symbol="NSBT", name="Neutrino System Bas"), scaling=Decimal("1e-6")
    ),
    "0x9d8268e4ad1a617f4386ee384d90bb4c3a86d0c9": TokenInfo(
        currency=CurrencyInfo(symbol="EXAS.CX", name="Exact Sciences Corporation"), scaling=Decimal("1e-8")
    ),
    "0x9d86b1b2554ec410eccffbf111a6994910111340": TokenInfo(
        currency=CurrencyInfo(symbol="OPEN", name="Open Platform"), scaling=Decimal("1e-8")
    ),
    "0x9d8a4a7eb39ece343f99ef25b1df38a08311d371": TokenInfo(
        currency=CurrencyInfo(symbol="DIS.CX", name="Walt Disney"), scaling=Decimal("1e-8")
    ),
    "0x9d91be44c06d373a8a226e1f3b146956083803eb": TokenInfo(
        currency=CurrencyInfo(symbol="AKNC", name="Aave KNC v1"), scaling=Decimal("1e-18")
    ),
    "0x9d9223436ddd466fc247e9dbbd20207e640fef58": TokenInfo(
        currency=CurrencyInfo(symbol="OLE", name="Olive"), scaling=Decimal("1e-18")
    ),
    "0x9dae8b7f6d37ea8e5d32c6c3e856a6d8a1d3b363": TokenInfo(
        currency=CurrencyInfo(symbol="GZB", name="GigziBlack"), scaling=Decimal("1e-18")
    ),
    "0x9dde7cdd09dbed542fc422d18d89a589fa9fd4c0": TokenInfo(
        currency=CurrencyInfo(symbol="iETH", name="iEther"), scaling=Decimal("1e-18")
    ),
    "0x9dfc4b433d359024eb3e810d77d60fbe8b0d9b82": TokenInfo(
        currency=CurrencyInfo(symbol="DANDY", name="Dandy Dego"), scaling=Decimal("1e-18")
    ),
    "0x9e12c837159dedc233719edf5a4ec2405644e8a7": TokenInfo(
        currency=CurrencyInfo(symbol="NUK", name="NUKlear"), scaling=Decimal("1e-3")
    ),
    "0x9e176ad338d72dda4b3434a2a9daa598b08fa5c5": TokenInfo(
        currency=CurrencyInfo(symbol="NC", name="NewChat"), scaling=Decimal("1e-18")
    ),
    "0x9e32b13ce7f2e80a01932b42553652e053d6ed8e": TokenInfo(
        currency=CurrencyInfo(symbol="METIS", name="Metis Token"), scaling=Decimal("1e-18")
    ),
    "0x9e3319636e2126e3c0bc9e3134aec5e1508a46c7": TokenInfo(
        currency=CurrencyInfo(symbol="UTNP", name="Universa"), scaling=Decimal("1e-18")
    ),
    "0x9e46a38f5daabe8683e10793b06749eef7d733d1": TokenInfo(
        currency=CurrencyInfo(symbol="NCT", name="PolySwarm"), scaling=Decimal("1e-18")
    ),
    "0x9e4c143bfe35f855624b3f84465ab7401a17a120": TokenInfo(
        currency=CurrencyInfo(symbol="EXC", name="EXCOIN CASH"), scaling=Decimal("1e-18")
    ),
    "0x9e4db6014a598fa1365e7c3f0f013477c961134a": TokenInfo(
        currency=CurrencyInfo(symbol="AEP", name="Agricultural Ecology Protocol"), scaling=Decimal("1e-18")
    ),
    "0x9e547061a345015869d26c7b6ee4ab5b63424441": TokenInfo(
        currency=CurrencyInfo(symbol="CC", name="Cryptocart"), scaling=Decimal("1e-18")
    ),
    "0x9e5a64943f9f48463f07cc0578bbf9e2e67f0f61": TokenInfo(
        currency=CurrencyInfo(symbol="AMC", name="Anonymous Coin"), scaling=Decimal("1e-18")
    ),
    "0x9e5bd9d9fad182ff0a93ba8085b664bcab00fa68": TokenInfo(
        currency=CurrencyInfo(symbol="DINGER", name="Dinger Token"), scaling=Decimal("1e-9")
    ),
    "0x9e6b2b11542f2bc52f3029077ace37e8fd838d7f": TokenInfo(
        currency=CurrencyInfo(symbol="HKN", name="Hacken"), scaling=Decimal("1e-8")
    ),
    "0x9e77d5a1251b6f7d456722a6eac6d2d5980bd891": TokenInfo(
        currency=CurrencyInfo(symbol="BRAT", name="BROTHER"), scaling=Decimal("1e-8")
    ),
    "0x9e78b8274e1d6a76a0dbbf90418894df27cbceb5": TokenInfo(
        currency=CurrencyInfo(symbol="UNIFI", name="Covenants"), scaling=Decimal("1e-18")
    ),
    "0x9e7cb236e43c4bd042fe463df6a175d4479ee186": TokenInfo(
        currency=CurrencyInfo(symbol="HALV", name="Halving"), scaling=Decimal("1e-18")
    ),
    "0x9e7ce36dbd1a9a6c6e80d08e38077745855edd3a": TokenInfo(
        currency=CurrencyInfo(symbol="BIM", name="Bimcoin"), scaling=Decimal("1e-18")
    ),
    "0x9e7cf1898ea701eab2bfa04ff47bdb09dc6a7d78": TokenInfo(
        currency=CurrencyInfo(symbol="CTGBP", name="CTINGBP"), scaling=Decimal("1e-6")
    ),
    "0x9e7d29bd499b6c7da2a5b2eafcf4a39d3bd845d1": TokenInfo(
        currency=CurrencyInfo(symbol="CTGC", name="Convenient To Go"), scaling=Decimal("1e-18")
    ),
    "0x9e88613418cf03dca54d6a2cf6ad934a78c7a17a": TokenInfo(
        currency=CurrencyInfo(symbol="SWM", name="Swarm Fund Token"), scaling=Decimal("1e-18")
    ),
    "0x9e923c70d090c5fa57dc4cf377bdd826c5ced550": TokenInfo(
        currency=CurrencyInfo(symbol="ETC8", name="Ethereum Legend Eight"), scaling=Decimal("1e-4")
    ),
    "0x9e96604445ec19ffed9a5e8dd7b50a29c899a10c": TokenInfo(
        currency=CurrencyInfo(symbol="COSS", name="COSS"), scaling=Decimal("1e-18")
    ),
    "0x9e976f211daea0d652912ab99b0dc21a7fd728e4": TokenInfo(
        currency=CurrencyInfo(symbol="MAP", name="MAP Protocol"), scaling=Decimal("1e-18")
    ),
    "0x9e9801bace260f58407c15e6e515c45918756e0f": TokenInfo(
        currency=CurrencyInfo(symbol="WUC", name="World Union Certificate"), scaling=Decimal("1e-8")
    ),
    "0x9ea20fbfaa44efbc60c6728fcdba17f01b7e04fe": TokenInfo(
        currency=CurrencyInfo(symbol="TOR", name="Torex"), scaling=Decimal("1e-8")
    ),
    "0x9ea463ec4ce9e9e5bc9cfd0187c4ac3a70dd951d": TokenInfo(
        currency=CurrencyInfo(symbol="ETH20SMACO", name="ETH 20 Day MA Crossover Set"), scaling=Decimal("1e-18")
    ),
    "0x9eb4f2dd25958ef1c72fe115d62da67abd6c000c": TokenInfo(
        currency=CurrencyInfo(symbol="LTCONE", name="Litecoin One"), scaling=Decimal("1e-18")
    ),
    "0x9eb5f8478ab6ce37ce30eb073f8731ab75df8dcc": TokenInfo(
        currency=CurrencyInfo(symbol="WFC", name="Work Force Coin"), scaling=Decimal("1e-2")
    ),
    "0x9eb6be354d88fd88795a04de899a57a77c545590": TokenInfo(
        currency=CurrencyInfo(symbol="GME", name="GameStop Finance"), scaling=Decimal("1e-18")
    ),
    "0x9ec251401eafb7e98f37a1d911c0aea02cb63a80": TokenInfo(
        currency=CurrencyInfo(symbol="BCT", name="Bitcratic"), scaling=Decimal("1e-18")
    ),
    "0x9ed8e7c9604790f7ec589f99b94361d8aab64e5e": TokenInfo(
        currency=CurrencyInfo(symbol="UNISTAKE", name="Unistake"), scaling=Decimal("1e-18")
    ),
    "0x9eeab220e44410c16ac80c12830bc11af7dd5c6e": TokenInfo(
        currency=CurrencyInfo(symbol="TST", name="ThunderStone"), scaling=Decimal("1e-18")
    ),
    "0x9eec65e5b998db6845321baa915ec3338b1a469b": TokenInfo(
        currency=CurrencyInfo(symbol="ONLY", name="OnlyChain"), scaling=Decimal("1e-18")
    ),
    "0x9eecec130fb665d03a37289ee34c818ee7f79926": TokenInfo(
        currency=CurrencyInfo(symbol="BTY", name="BETTY"), scaling=Decimal("1e-18")
    ),
    "0x9efa0e2387e4cba02a6e4e6594b8f4dd209a0b93": TokenInfo(
        currency=CurrencyInfo(symbol="LDX", name="LondonCoin"), scaling=Decimal("1e-0")
    ),
    "0x9efc8df9ccc40017e800381cd9fd457dbebed995": TokenInfo(
        currency=CurrencyInfo(symbol="K.CX", name="Kellogg"), scaling=Decimal("1e-8")
    ),
    "0x9f0f1be08591ab7d990faf910b38ed5d60e4d5bf": TokenInfo(
        currency=CurrencyInfo(symbol="MNC", name="MainCoin"), scaling=Decimal("1e-18")
    ),
    "0x9f195617fa8fbad9540c5d113a99a0a0172aaedc": TokenInfo(
        currency=CurrencyInfo(symbol="NBC", name="Niobium Coin"), scaling=Decimal("1e-18")
    ),
    "0x9f235d23354857efe6c541db92a9ef1877689bcb": TokenInfo(
        currency=CurrencyInfo(symbol="BOLT", name="Bolt Token"), scaling=Decimal("1e-18")
    ),
    "0x9f31fab2405dfba05a487ebce88f3abd26f1cba6": TokenInfo(
        currency=CurrencyInfo(symbol="AAT", name="Agricultural Trade Chain"), scaling=Decimal("1e-18")
    ),
    "0x9f452e458b024e82d6e3ff50a07b8de74c988523": TokenInfo(
        currency=CurrencyInfo(symbol="GOAT", name="Goat Cash"), scaling=Decimal("1e-18")
    ),
    "0x9f49ed43c90a540d1cf12f6170ace8d0b88a14e6": TokenInfo(
        currency=CurrencyInfo(symbol="ETHRSIAPY", name="ETH RSI 60/40 Yield Set II"), scaling=Decimal("1e-18")
    ),
    "0x9f4de9ba900fd9fdf56f96439a0c2f447a1eaeb9": TokenInfo(
        currency=CurrencyInfo(symbol="SOVC", name="Sovereign Cash"), scaling=Decimal("1e-10")
    ),
    "0x9f52c8ecbee10e00d9faaac5ee9ba0ff6550f511": TokenInfo(
        currency=CurrencyInfo(symbol="SIPHER", name="Sipher"), scaling=Decimal("1e-18")
    ),
    "0x9f549ebfd4974cd4ed4a1550d40394b44a7382aa": TokenInfo(
        currency=CurrencyInfo(symbol="LKN", name="LinkCoin Token"), scaling=Decimal("1e-18")
    ),
    "0x9f58702ef19ebeb76363884362439a8691e3f033": TokenInfo(
        currency=CurrencyInfo(symbol="THPT", name="HELIO POWER TOKEN"), scaling=Decimal("1e-4")
    ),
    "0x9f5f3cfd7a32700c93f971637407ff17b91c7342": TokenInfo(
        currency=CurrencyInfo(symbol="DDD", name="Scry.info"), scaling=Decimal("1e-18")
    ),
    "0x9f6513ed2b0de89218e97db4a5115ba04be449f1": TokenInfo(
        currency=CurrencyInfo(symbol="WAK", name="Wak Coin"), scaling=Decimal("1e-18")
    ),
    "0x9f801c1f02af03cc240546dadef8e56cd46ea2e9": TokenInfo(
        currency=CurrencyInfo(symbol="VAI", name="Vaiot"), scaling=Decimal("1e-18")
    ),
    "0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2": TokenInfo(
        currency=CurrencyInfo(symbol="MKR", name="Maker"), scaling=Decimal("1e-18")
    ),
    "0x9f978aa425148cdd9223eb175446a877b86727ff": TokenInfo(
        currency=CurrencyInfo(symbol="YOT", name="PayYoda"), scaling=Decimal("1e-6")
    ),
    "0x9f9c8ec3534c3ce16f928381372bfbfbfb9f4d24": TokenInfo(
        currency=CurrencyInfo(symbol="GLQ", name="GraphLinq Protocol"), scaling=Decimal("1e-18")
    ),
    "0x9fa69536d1cda4a04cfb50688294de75b505a9ae": TokenInfo(
        currency=CurrencyInfo(symbol="DERC", name="DeRace"), scaling=Decimal("1e-18")
    ),
    "0x9fadea1aff842d407893e21dbd0e2017b4c287b6": TokenInfo(
        currency=CurrencyInfo(symbol="PGF7T", name="PGF500"), scaling=Decimal("1e-18")
    ),
    "0x9fb83c0635de2e815fd1c21b3a292277540c2e8d": TokenInfo(
        currency=CurrencyInfo(symbol="FEVR", name="RealFevr"), scaling=Decimal("1e-18")
    ),
    "0x9fba684d77d2d6a1408c24b60a1f5534e71f5b75": TokenInfo(
        currency=CurrencyInfo(symbol="PATR", name="PATRIOT"), scaling=Decimal("1e-18")
    ),
    "0x9fbfed658919a896b5dc7b00456ce22d780f9b65": TokenInfo(
        currency=CurrencyInfo(symbol="PLT", name="PlutusDeFi"), scaling=Decimal("1e-18")
    ),
    "0x9fc0583220eb44faee9e2dc1e63f39204ddd9090": TokenInfo(
        currency=CurrencyInfo(symbol="2DC", name="DualChain"), scaling=Decimal("1e-18")
    ),
    "0x9fe173573b3f3cf4aebce5fd5bef957b9a6686e8": TokenInfo(
        currency=CurrencyInfo(symbol="BVT", name="VTChain"), scaling=Decimal("1e-6")
    ),
    "0x9ff58f4ffb29fa2266ab25e75e2a8b3503311656": TokenInfo(
        currency=CurrencyInfo(symbol="AWBTC", name="Aave WBTC"), scaling=Decimal("1e-8")
    ),
    "0xa00055e6ee4d1f4169096ecb682f70caa8c29987": TokenInfo(
        currency=CurrencyInfo(symbol="WIVA", name="WIVA"), scaling=Decimal("1e-18")
    ),
    "0xa017ac5fac5941f95010b12570b812c974469c2c": TokenInfo(
        currency=CurrencyInfo(symbol="XES", name="Proxeus"), scaling=Decimal("1e-18")
    ),
    "0xa01b656e49efbb8210d882a1f1a4d10f5cada8cc": TokenInfo(
        currency=CurrencyInfo(symbol="ECGO", name="Eco Gold"), scaling=Decimal("1e-18")
    ),
    "0xa02120696c7b8fe16c09c749e4598819b2b0e915": TokenInfo(
        currency=CurrencyInfo(symbol="WXT", name="Wirex"), scaling=Decimal("1e-18")
    ),
    "0xa0246c9032bc3a600820415ae600c6388619a14d": TokenInfo(
        currency=CurrencyInfo(symbol="FARM", name="Harvest Finance"), scaling=Decimal("1e-18")
    ),
    "0xa024e8057eec474a9b2356833707dd0579e26ef3": TokenInfo(
        currency=CurrencyInfo(symbol="FXY", name="FIXY NETWORK"), scaling=Decimal("1e-18")
    ),
    "0xa02d0b6bfce1dbd02b9cbb70e6b480333e8a86ec": TokenInfo(
        currency=CurrencyInfo(symbol="IPWT", name="IPWeb"), scaling=Decimal("1e-18")
    ),
    "0xa0471cdd5c0dc2614535fd7505b17a651a8f0dab": TokenInfo(
        currency=CurrencyInfo(symbol="ESWA", name="EasySwap"), scaling=Decimal("1e-8")
    ),
    "0xa05a577732b6f52cec3d35eb5cc8f91cba8d0be4": TokenInfo(
        currency=CurrencyInfo(symbol="VNG", name="Gateway Cash"), scaling=Decimal("1e-6")
    ),
    "0xa063341d10054188e3cb715bfb663b37c0c1515e": TokenInfo(
        currency=CurrencyInfo(symbol="DGN", name="Diagon Coin"), scaling=Decimal("1e-6")
    ),
    "0xa06bc25b5805d5f8d82847d191cb4af5a3e873e0": TokenInfo(
        currency=CurrencyInfo(symbol="ALINK", name="Aave LINK"), scaling=Decimal("1e-18")
    ),
    "0xa0a6b8f5f8d41b88a4306c6a9e85028cbefad8e1": TokenInfo(
        currency=CurrencyInfo(symbol="HMK", name="HMK Global Economic Circular"), scaling=Decimal("1e-18")
    ),
    "0xa0afaa285ce85974c3c881256cb7f225e3a1178a": TokenInfo(
        currency=CurrencyInfo(symbol="WCRES", name="Wrapped CrescoFin"), scaling=Decimal("1e-18")
    ),
    "0xa0b207103f764a920b4af9e691f5bd956de14ded": TokenInfo(
        currency=CurrencyInfo(symbol="ABST", name="Abitshadow Token"), scaling=Decimal("1e-8")
    ),
    "0xa0b73e1ff0b80914ab6fe0444e65848c4c34450b": TokenInfo(
        currency=CurrencyInfo(symbol="CRO", name="Crypto.com Coin"), scaling=Decimal("1e-8")
    ),
    "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48": TokenInfo(
        currency=CurrencyInfo(symbol="USDC", name="USD Coin"), scaling=Decimal("1e-6")
    ),
    "0xa0cf46eb152656c7090e769916eb44a138aaa406": TokenInfo(
        currency=CurrencyInfo(symbol="SPH", name="Spheroid Universe"), scaling=Decimal("1e-18")
    ),
    "0xa0d440c6da37892dc06ee7930b2eede0634fd681": TokenInfo(
        currency=CurrencyInfo(symbol="MASH", name="Masternet"), scaling=Decimal("1e-8")
    ),
    "0xa0e5a7da90765bef7550cbd0e208e50e20c97d41": TokenInfo(
        currency=CurrencyInfo(symbol="LGC", name="Language Coin"), scaling=Decimal("1e-8")
    ),
    "0xa0ed4c4acbf07c03365d6bbe28150a819aff700f": TokenInfo(
        currency=CurrencyInfo(symbol="BITX", name="BITIFEX"), scaling=Decimal("1e-18")
    ),
    "0xa101e27f06a97985b925e244111b61560ecd97db": TokenInfo(
        currency=CurrencyInfo(symbol="BITTO", name="BITTO"), scaling=Decimal("1e-18")
    ),
    "0xa105c740bc012a43a342ab4a0ef40143452c8e89": TokenInfo(
        currency=CurrencyInfo(symbol="LTB", name="Litbinex Coin"), scaling=Decimal("1e-18")
    ),
    "0xa10740ff9ff6852eac84cdcff9184e1d6d27c057": TokenInfo(
        currency=CurrencyInfo(symbol="WG0", name="Wrapped Gen-0 CryptoKitties"), scaling=Decimal("1e-18")
    ),
    "0xa10ae543db5d967a73e9abcc69c81a18a7fc0a78": TokenInfo(
        currency=CurrencyInfo(symbol="CLOUT", name="BLOCKCLOUT"), scaling=Decimal("1e-18")
    ),
    "0xa110eeebc0751407bdcaea4cd230f04a2b82a33a": TokenInfo(
        currency=CurrencyInfo(symbol="GMAT", name="GoWithMi"), scaling=Decimal("1e-18")
    ),
    "0xa117000000f279d81a1d3cc75430faa017fa5a2e": TokenInfo(
        currency=CurrencyInfo(symbol="ANT", name="Aragon"), scaling=Decimal("1e-18")
    ),
    "0xa117ea1c0c85cef648df2b6f40e50bb5475c228d": TokenInfo(
        currency=CurrencyInfo(symbol="DUCATO", name="Ducato Protocol Token"), scaling=Decimal("1e-18")
    ),
    "0xa119f0f5fd06ebadff8883c0f3c40b2d22e7a44f": TokenInfo(
        currency=CurrencyInfo(symbol="CRTM", name="Corethum"), scaling=Decimal("1e-8")
    ),
    "0xa11bd36801d8fa4448f0ac4ea7a62e3634ce8c7c": TokenInfo(
        currency=CurrencyInfo(symbol="ABR", name="Allbridge"), scaling=Decimal("1e-18")
    ),
    "0xa1248c718d52752b2cc257eeb0eba900408daeb8": TokenInfo(
        currency=CurrencyInfo(symbol="SWYFTT", name="SWYFT"), scaling=Decimal("1e-18")
    ),
    "0xa130e3a33a4d84b04c3918c4e5762223ae252f80": TokenInfo(
        currency=CurrencyInfo(symbol="SWASH", name="Swash"), scaling=Decimal("1e-18")
    ),
    "0xa13f0743951b4f6e3e3aa039f682e17279f52bc3": TokenInfo(
        currency=CurrencyInfo(symbol="SENC", name="Sentinel Chain"), scaling=Decimal("1e-18")
    ),
    "0xa14516ff788338f34db1a591497a616e3a759e23": TokenInfo(
        currency=CurrencyInfo(symbol="EVS", name="EverySave"), scaling=Decimal("1e-8")
    ),
    "0xa150db9b1fa65b44799d4dd949d922c0a33ee606": TokenInfo(
        currency=CurrencyInfo(symbol="DRC", name="Digital Reserve Currency"), scaling=Decimal("1e-0")
    ),
    "0xa15c7ebe1f07caf6bff097d8a589fb8ac49ae5b3": TokenInfo(
        currency=CurrencyInfo(symbol="NPXS", name="Pundi X [OLD]"), scaling=Decimal("1e-18")
    ),
    "0xa160d857fced9436a57c6a405b2f379aceb83186": TokenInfo(
        currency=CurrencyInfo(symbol="OKBMOON", name="10X Long OKB Token"), scaling=Decimal("1e-18")
    ),
    "0xa1653cb37852249e4f18dfbc473a5ce3f88fa6ad": TokenInfo(
        currency=CurrencyInfo(symbol="TOMOBEAR", name="3X Short TomoChain Token"), scaling=Decimal("1e-18")
    ),
    "0xa17d1bf14802e0eec8f84b3b8b638a9402d60e9e": TokenInfo(
        currency=CurrencyInfo(symbol="RST", name="REGA"), scaling=Decimal("1e-10")
    ),
    "0xa17de0ab0a97bc5e56fa8b39ebfc81cc3f1f349e": TokenInfo(
        currency=CurrencyInfo(symbol="DFK", name="DefiKing"), scaling=Decimal("1e-18")
    ),
    "0xa19a40fbd7375431fab013a4b08f00871b9a2791": TokenInfo(
        currency=CurrencyInfo(symbol="SWAGG", name="Swagg Network"), scaling=Decimal("1e-4")
    ),
    "0xa19bbef64eff0d060a653e4df10a57b6d8006d3e": TokenInfo(
        currency=CurrencyInfo(symbol="EGX", name="Enegra"), scaling=Decimal("1e-18")
    ),
    "0xa1afffe3f4d611d252010e3eaf6f4d77088b0cd7": TokenInfo(
        currency=CurrencyInfo(symbol="RFI", name="reflect.finance"), scaling=Decimal("1e-9")
    ),
    "0xa1b0edf4460cc4d8bfaa18ed871bff15e5b57eb4": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNIBATWETH", name="Aave AMM UniBATWETH"), scaling=Decimal("1e-18")
    ),
    "0xa1ba7186eec1be5114b0cf49b95b23adc4131b51": TokenInfo(
        currency=CurrencyInfo(symbol="TECH", name="FTI NEWS Token"), scaling=Decimal("1e-10")
    ),
    "0xa1ccc166faf0e998b3e33225a1a0301b1c86119d": TokenInfo(
        currency=CurrencyInfo(symbol="SGEL", name="SGELDER"), scaling=Decimal("1e-18")
    ),
    "0xa1d0e215a23d7030842fc67ce582a6afa3ccab83": TokenInfo(
        currency=CurrencyInfo(symbol="YFII", name="DFI.money"), scaling=Decimal("1e-18")
    ),
    "0xa1d65e8fb6e87b60feccbc582f7f97804b725521": TokenInfo(
        currency=CurrencyInfo(symbol="DXD", name="DXdao"), scaling=Decimal("1e-18")
    ),
    "0xa1d6df714f91debf4e0802a542e13067f31b8262": TokenInfo(
        currency=CurrencyInfo(symbol="RFOX", name="RedFOX Labs"), scaling=Decimal("1e-18")
    ),
    "0xa1dda546100ec31f8ac5c37eece894ca863e9596": TokenInfo(
        currency=CurrencyInfo(symbol="CSCC", name="Constant Source Chain"), scaling=Decimal("1e-8")
    ),
    "0xa1faa113cbe53436df28ff0aee54275c13b40975": TokenInfo(
        currency=CurrencyInfo(symbol="ALPHA", name="Alpha Finance"), scaling=Decimal("1e-18")
    ),
    "0xa2060391990368cd595496ff0145f425333c1291": TokenInfo(
        currency=CurrencyInfo(symbol="DHR.CX", name="Danaher"), scaling=Decimal("1e-8")
    ),
    "0xa2085073878152ac3090ea13d1e41bd69e60dc99": TokenInfo(
        currency=CurrencyInfo(symbol="ELG", name="Escoin Token"), scaling=Decimal("1e-18")
    ),
    "0xa209ba34c01a2713a4453a656630cc9de8a362bc": TokenInfo(
        currency=CurrencyInfo(symbol="LINKBEAR", name="3X Short Chainlink Token"), scaling=Decimal("1e-18")
    ),
    "0xa211f450ce88deb31d3f12ae3c1ebf6b0e55a5d9": TokenInfo(
        currency=CurrencyInfo(symbol="PRQBOOST", name="Parsiq Boost"), scaling=Decimal("1e-18")
    ),
    "0xa2120b9e674d3fc3875f415a7df52e382f141225": TokenInfo(
        currency=CurrencyInfo(symbol="ATA", name="ATA"), scaling=Decimal("1e-18")
    ),
    "0xa22525aad7a794d5b923ecb036ced9eb66d7d5ed": TokenInfo(
        currency=CurrencyInfo(symbol="ALLBI", name="ALL BEST ICO Verified"), scaling=Decimal("1e-18")
    ),
    "0xa23c150bd61fef5e4ed2dc480461c0ea2e6dd977": TokenInfo(
        currency=CurrencyInfo(symbol="IT40.CX", name="FTSE Borsa Italiana Index 40"), scaling=Decimal("1e-8")
    ),
    "0xa249f0e9a464b9685f66992f41e1012388e39e81": TokenInfo(
        currency=CurrencyInfo(symbol="XRM", name="AERUM"), scaling=Decimal("1e-18")
    ),
    "0xa253be28580ae23548a4182d95bf8201c28369a8": TokenInfo(
        currency=CurrencyInfo(symbol="DIW", name="DIW Token"), scaling=Decimal("1e-18")
    ),
    "0xa261e1facd9e90233dc08f785c2b1fb1691024ba": TokenInfo(
        currency=CurrencyInfo(symbol="IGF", name="IGF Token"), scaling=Decimal("1e-8")
    ),
    "0xa26c4caaaea8b88ef49bf8c380488f66c2d807ae": TokenInfo(
        currency=CurrencyInfo(symbol="EVF", name="Eviff"), scaling=Decimal("1e-18")
    ),
    "0xa2a54f1ec1f09316ef12c1770d32ed8f21b1fb6a": TokenInfo(
        currency=CurrencyInfo(symbol="DFT", name="DigiFinexToken"), scaling=Decimal("1e-8")
    ),
    "0xa2a7963b19a82665e0f471c0bee29b111d4ae0a2": TokenInfo(
        currency=CurrencyInfo(symbol="TED", name="Token Economy Doin"), scaling=Decimal("1e-18")
    ),
    "0xa2a8dec9d963e2fe7a5ab8469586b07ef53bb505": TokenInfo(
        currency=CurrencyInfo(symbol="PEAK", name="Peak"), scaling=Decimal("1e-18")
    ),
    "0xa2b0fde6d710e201d0d608e924a484d1a5fed57c": TokenInfo(
        currency=CurrencyInfo(symbol="SXRP", name="sXRP"), scaling=Decimal("1e-18")
    ),
    "0xa2b2953b35971d7f85cbe38b7dc9c42e8b1adef4": TokenInfo(
        currency=CurrencyInfo(symbol="MSA", name="MSA"), scaling=Decimal("1e-18")
    ),
    "0xa2b47bc1f3e58c30d7744ef1194e2dbb4363e287": TokenInfo(
        currency=CurrencyInfo(symbol="QQBC", name="QQBC"), scaling=Decimal("1e-18")
    ),
    "0xa2b4c0af19cc16a6cfacce81f192b024d625817d": TokenInfo(
        currency=CurrencyInfo(symbol="KISHU", name="Kishu Inu"), scaling=Decimal("1e-9")
    ),
    "0xa2b72ff1edbd1cb26fcf941983376f89a4e230eb": TokenInfo(
        currency=CurrencyInfo(symbol="SAFT", name="Safety Token"), scaling=Decimal("1e-18")
    ),
    "0xa2c1e04aca801da92fa95af161040d37f103d69d": TokenInfo(
        currency=CurrencyInfo(symbol="COY", name="CoinAnalyst"), scaling=Decimal("1e-18")
    ),
    "0xa2d77f8353cb2afd709aba4a967257511ecff716": TokenInfo(
        currency=CurrencyInfo(symbol="INEX", name="Internet Exchange Token"), scaling=Decimal("1e-8")
    ),
    "0xa2dca1505b07e39f96ce41e875b447f46d50c6fc": TokenInfo(
        currency=CurrencyInfo(symbol="ETHS", name="Ethercash"), scaling=Decimal("1e-18")
    ),
    "0xa30c7cdac7d8505f32bb0930ed82b9ba5777b5f3": TokenInfo(
        currency=CurrencyInfo(symbol="NLM", name="NUCLUM"), scaling=Decimal("1e-18")
    ),
    "0xa31108e5bab5494560db34c95492658af239357c": TokenInfo(
        currency=CurrencyInfo(symbol="DACS", name="Dacsee"), scaling=Decimal("1e-18")
    ),
    "0xa311856b777df090d2d3d8c306caaf6e4dfd9ae9": TokenInfo(
        currency=CurrencyInfo(symbol="GMC", name="Gamma Coin"), scaling=Decimal("1e-18")
    ),
    "0xa3149e0fa0061a9007faf307074cdcd290f0e2fd": TokenInfo(
        currency=CurrencyInfo(symbol="PRON", name="PronCoin"), scaling=Decimal("1e-8")
    ),
    "0xa31b1767e09f842ecfd4bc471fe44f830e3891aa": TokenInfo(
        currency=CurrencyInfo(symbol="ROOBEE", name="Roobee"), scaling=Decimal("1e-18")
    ),
    "0xa33e729bf4fdeb868b534e1f20523463d9c46bee": TokenInfo(
        currency=CurrencyInfo(symbol="¢", name="ICO"), scaling=Decimal("1e-10")
    ),
    "0xa340f0937a8c00db11c83cc16cec12310160f0b6": TokenInfo(
        currency=CurrencyInfo(symbol="ETCBEAR", name="3X Short Ethereum Classic Token"), scaling=Decimal("1e-18")
    ),
    "0xa353d00fa6d940cb625045d74fef8406854dd0da": TokenInfo(
        currency=CurrencyInfo(symbol="DAKU", name="Dakuce"), scaling=Decimal("1e-18")
    ),
    "0xa35fc5019c4dc509394bd4d74591a0bf8852c195": TokenInfo(
        currency=CurrencyInfo(symbol="BTCETH7525", name="BTC ETH 75%/25% Weight Set"), scaling=Decimal("1e-18")
    ),
    "0xa360f2af3f957906468c0fd7526391aed08ae3db": TokenInfo(
        currency=CurrencyInfo(symbol="ETH50SMACO", name="ETH 50 Day MA Crossover Set"), scaling=Decimal("1e-18")
    ),
    "0xa361718326c15715591c299427c62086f69923d9": TokenInfo(
        currency=CurrencyInfo(symbol="ABUSD", name="Aave BUSD"), scaling=Decimal("1e-18")
    ),
    "0xa36fdbbae3c9d55a1d67ee5821d53b50b63a1ab9": TokenInfo(
        currency=CurrencyInfo(symbol="TEMP", name="Tempus"), scaling=Decimal("1e-18")
    ),
    "0xa3865e64121537b5b59b5e239db4acbe6f36aa74": TokenInfo(
        currency=CurrencyInfo(symbol="WXTZ", name="Wrapped Tezos"), scaling=Decimal("1e-18")
    ),
    "0xa386e04f0fb641869accd582c1b76eaa7d7087fe": TokenInfo(
        currency=CurrencyInfo(symbol="ALGOMOON", name="10X Long Algorand Token"), scaling=Decimal("1e-18")
    ),
    "0xa38920c00d1a5303db538a3ea08da7a779e1f751": TokenInfo(
        currency=CurrencyInfo(symbol="TOMOBULL", name="3X Long TomoChain Token"), scaling=Decimal("1e-18")
    ),
    "0xa38b7ee9df79955b90cc4e2de90421f6baa83a3d": TokenInfo(
        currency=CurrencyInfo(symbol="MC", name="Monkey Coin"), scaling=Decimal("1e-18")
    ),
    "0xa393473d64d2f9f026b60b6df7859a689715d092": TokenInfo(
        currency=CurrencyInfo(symbol="LTX", name="Lattice Token"), scaling=Decimal("1e-8")
    ),
    "0xa3a3f076413a362bb0d69eea1dc5b0e79c831edc": TokenInfo(
        currency=CurrencyInfo(symbol="COKE", name="Cocaine Cowboy Shards"), scaling=Decimal("1e-18")
    ),
    "0xa3afe717038d4e12133d84088754811220af9329": TokenInfo(
        currency=CurrencyInfo(symbol="VMC", name="V-Members Coin"), scaling=Decimal("1e-18")
    ),
    "0xa3bed4e1c75d00fa6f4e5e6922db7261b5e9acd2": TokenInfo(
        currency=CurrencyInfo(symbol="MTA", name="mStable Governance Token: Meta"), scaling=Decimal("1e-18")
    ),
    "0xa3c22370de5f9544f0c4de126b1e46ceadf0a51b": TokenInfo(
        currency=CurrencyInfo(symbol="STRAX", name="Stratis"), scaling=Decimal("1e-18")
    ),
    "0xa3ceac0aac5c5d868973e546ce4731ba90e873c2": TokenInfo(
        currency=CurrencyInfo(symbol="STOR", name="Self Storage Coin"), scaling=Decimal("1e-8")
    ),
    "0xa3d58c4e56fedcae3a7c43a725aee9a71f0ece4e": TokenInfo(
        currency=CurrencyInfo(symbol="MET", name="Metronome"), scaling=Decimal("1e-18")
    ),
    "0xa3ee21c306a700e682abcdfe9baa6a08f3820419": TokenInfo(
        currency=CurrencyInfo(symbol="CTC", name="Creditcoin"), scaling=Decimal("1e-18")
    ),
    "0xa3efef1a1e3d1ad72b9d0f4253e7c9c084c2c08b": TokenInfo(
        currency=CurrencyInfo(symbol="OIO", name="Online"), scaling=Decimal("1e-18")
    ),
    "0xa3fae71843524eb359bcac859e8c8c10fd18e0e4": TokenInfo(
        currency=CurrencyInfo(symbol="KDH", name="Key Decade Holding Token"), scaling=Decimal("1e-8")
    ),
    "0xa40106134c5bf4c41411554e6db99b95a15ed9d8": TokenInfo(
        currency=CurrencyInfo(symbol="ROCK", name="Rocket Token"), scaling=Decimal("1e-18")
    ),
    "0xa41f142b6eb2b164f8164cae0716892ce02f311f": TokenInfo(
        currency=CurrencyInfo(symbol="AVG", name="Avocado DAO"), scaling=Decimal("1e-18")
    ),
    "0xa44e5137293e855b1b7bc7e2c6f8cd796ffcb037": TokenInfo(
        currency=CurrencyInfo(symbol="DVPN", name="Sentinel [OLD]"), scaling=Decimal("1e-8")
    ),
    "0xa44fb3aa5c8465512b806145a8f9b60e74f3f851": TokenInfo(
        currency=CurrencyInfo(symbol="PIT", name="PITSTOP"), scaling=Decimal("1e-18")
    ),
    "0xa456b515303b2ce344e9d2601f91270f8c2fea5e": TokenInfo(
        currency=CurrencyInfo(symbol="CORN", name="Cornichon"), scaling=Decimal("1e-18")
    ),
    "0xa462d0e6bb788c7807b1b1c96992ce1f7069e195": TokenInfo(
        currency=CurrencyInfo(symbol="EQMT", name="Equus Mining Token"), scaling=Decimal("1e-18")
    ),
    "0xa47c8bf37f92abed4a126bda807a7b7498661acd": TokenInfo(
        currency=CurrencyInfo(symbol="UST", name="TerraUSD"), scaling=Decimal("1e-18")
    ),
    "0xa487bf43cf3b10dffc97a9a744cbb7036965d3b9": TokenInfo(
        currency=CurrencyInfo(symbol="DERI", name="Deri Protocol"), scaling=Decimal("1e-18")
    ),
    "0xa497a35c26d019b61ff05ad090323bc8690a1ecd": TokenInfo(
        currency=CurrencyInfo(symbol="OBE", name="OneBitEarn"), scaling=Decimal("1e-18")
    ),
    "0xa499648fd0e80fd911972bbeb069e4c20e68bf22": TokenInfo(
        currency=CurrencyInfo(symbol="UJENNY", name="Jenny Metaverse DAO"), scaling=Decimal("1e-18")
    ),
    "0xa49d7499271ae71cd8ab9ac515e6694c755d400c": TokenInfo(
        currency=CurrencyInfo(symbol="MUTE", name="Mute"), scaling=Decimal("1e-18")
    ),
    "0xa49ded8b4607f958003e0d87d7f2d2f69bcadd41": TokenInfo(
        currency=CurrencyInfo(symbol="ZTH", name="Zenith"), scaling=Decimal("1e-18")
    ),
    "0xa4bad5d040d4464ec5ce130987731f2f428c9307": TokenInfo(
        currency=CurrencyInfo(symbol="SPORE", name="Enoki Finance"), scaling=Decimal("1e-18")
    ),
    "0xa4bbe66f151b22b167127c770016b15ff97dd35c": TokenInfo(
        currency=CurrencyInfo(symbol="UMBR", name="Umbria Network"), scaling=Decimal("1e-18")
    ),
    "0xa4bdb11dc0a2bec88d24a3aa1e6bb17201112ebe": TokenInfo(
        currency=CurrencyInfo(symbol="USDS", name="Stably USD"), scaling=Decimal("1e-6")
    ),
    "0xa4c9d058a462936a1faadac012df99d9bdd71f41": TokenInfo(
        currency=CurrencyInfo(symbol="DET", name="Diamond Exchange Token"), scaling=Decimal("1e-8")
    ),
    "0xa4d17ab1ee0efdd23edc2869e7ba96b89eecf9ab": TokenInfo(
        currency=CurrencyInfo(symbol="TRUE", name="TRUE Token"), scaling=Decimal("1e-18")
    ),
    "0xa4e7414fcba1af15203030c6daac630df8f16aea": TokenInfo(
        currency=CurrencyInfo(symbol="MCH", name="Meme Cash"), scaling=Decimal("1e-18")
    ),
    "0xa4e8c3ec456107ea67d3075bf9e3df3a75823db0": TokenInfo(
        currency=CurrencyInfo(symbol="LOOMOLD", name="Loom Network (OLD)"), scaling=Decimal("1e-18")
    ),
    "0xa4e9584daa093cb1205e17ba737c3fd015748087": TokenInfo(
        currency=CurrencyInfo(symbol="FOREX", name="FOREXCOIN"), scaling=Decimal("1e-18")
    ),
    "0xa4ea687a2a7f29cf2dc66b39c68e4411c0d00c49": TokenInfo(
        currency=CurrencyInfo(symbol="IVY", name="Ivy"), scaling=Decimal("1e-18")
    ),
    "0xa4ec83c8907888d006a37debf755ee39766f38ae": TokenInfo(
        currency=CurrencyInfo(symbol="GCU", name="Global Currency Unit"), scaling=Decimal("1e-18")
    ),
    "0xa4eed63db85311e22df4473f87ccfc3dadcfa3e3": TokenInfo(
        currency=CurrencyInfo(symbol="RBC", name="Rubic"), scaling=Decimal("1e-18")
    ),
    "0xa4f267b2bf5c47873ec85cb55749368bc15ec2ec": TokenInfo(
        currency=CurrencyInfo(symbol="TWS", name="Energy27 Token"), scaling=Decimal("1e-8")
    ),
    "0xa4f779074850d320b5553c9db5fc6a8ab15bd34a": TokenInfo(
        currency=CurrencyInfo(symbol="YFIX", name="YFIX.finance"), scaling=Decimal("1e-18")
    ),
    "0xa4fb385820a9eef842a419e08f8540fd7d1bf6e8": TokenInfo(
        currency=CurrencyInfo(symbol="BHT", name="BeeStore"), scaling=Decimal("1e-5")
    ),
    "0xa50e0620233e87bfac560aad39505c79e1f9092b": TokenInfo(
        currency=CurrencyInfo(symbol="FLXC", name="Flexo Coin"), scaling=Decimal("1e-18")
    ),
    "0xa517a46baad6b054a76bd19c46844f717fe69fea": TokenInfo(
        currency=CurrencyInfo(symbol="CARB", name="CarbCoin"), scaling=Decimal("1e-8")
    ),
    "0xa51fc71422a30fa7ffa605b360c3b283501b5bf6": TokenInfo(
        currency=CurrencyInfo(symbol="AWX", name="AurusDeFi"), scaling=Decimal("1e-18")
    ),
    "0xa52383b665b91dce42dd4b6d1e0fb37d3effe489": TokenInfo(
        currency=CurrencyInfo(symbol="MUSD", name="MASTER USD"), scaling=Decimal("1e-18")
    ),
    "0xa54c67bd320da4f9725a6f585b7635a0c09b122e": TokenInfo(
        currency=CurrencyInfo(symbol="TIME", name="TimeMiner"), scaling=Decimal("1e-6")
    ),
    "0xa54ddc7b3cce7fc8b1e3fa0256d0db80d2c10970": TokenInfo(
        currency=CurrencyInfo(symbol="NDC", name="NEVERDIE"), scaling=Decimal("1e-18")
    ),
    "0xa55ffaea5c8cf32b550f663bf17d4f7b739534ff": TokenInfo(
        currency=CurrencyInfo(symbol="ATF", name="Agro Tech Farm"), scaling=Decimal("1e-18")
    ),
    "0xa573661b5fb2063d7ab12336ee24589f7a79fdab": TokenInfo(
        currency=CurrencyInfo(symbol="ICHX", name="IceChain"), scaling=Decimal("1e-18")
    ),
    "0xa578acc0cb7875781b7880903f4594d13cfa8b98": TokenInfo(
        currency=CurrencyInfo(symbol="ECN", name=" EtherCarbon"), scaling=Decimal("1e-2")
    ),
    "0xa57a2ad52ad6b1995f215b12fc037bffd990bc5e": TokenInfo(
        currency=CurrencyInfo(symbol="TXT", name="Tunetrade"), scaling=Decimal("1e-18")
    ),
    "0xa58a4f5c4bb043d2cc1e170613b74e767c94189b": TokenInfo(
        currency=CurrencyInfo(symbol="UTU", name="UTU Coin"), scaling=Decimal("1e-18")
    ),
    "0xa58b5c6c60d2f05792e9261727143db1ee544c54": TokenInfo(
        currency=CurrencyInfo(symbol="SWN.CX", name="Southwestern Energy"), scaling=Decimal("1e-8")
    ),
    "0xa5a283557653f36cf9aa0d5cc74b1e30422349f2": TokenInfo(
        currency=CurrencyInfo(symbol="UETL", name="Useless Eth Token Lite"), scaling=Decimal("1e-8")
    ),
    "0xa5b399a76bbabef93d70255525c1d2bcc3701d0b": TokenInfo(
        currency=CurrencyInfo(symbol="GL", name="GLOSMATIN"), scaling=Decimal("1e-18")
    ),
    "0xa5b46ff9a887180c8fb2d97146398ddfc5fef1cd": TokenInfo(
        currency=CurrencyInfo(symbol="SSN", name="SuperSkyNet"), scaling=Decimal("1e-18")
    ),
    "0xa5ddfca8b837ccd0cf80fe6c24e2a9018fb50dba": TokenInfo(
        currency=CurrencyInfo(symbol="TRYBBEAR", name="3X Short BiLira Token"), scaling=Decimal("1e-18")
    ),
    "0xa5def515cfd373d17830e7c1de1639cb3530a112": TokenInfo(
        currency=CurrencyInfo(symbol="DEPO", name="Depo"), scaling=Decimal("1e-18")
    ),
    "0xa5e412ba6fca1e07b15defcaa4236ff7b5a7f086": TokenInfo(
        currency=CurrencyInfo(symbol="CBANK", name="Crypto Bank"), scaling=Decimal("1e-18")
    ),
    "0xa5e99ad202bdd71d3518306cf4dd163261981af1": TokenInfo(
        currency=CurrencyInfo(symbol="COMC", name="Community Chain"), scaling=Decimal("1e-18")
    ),
    "0xa5ef74068d04ba0809b7379dd76af5ce34ab7c57": TokenInfo(
        currency=CurrencyInfo(symbol="LUCHOW", name="LunaChow"), scaling=Decimal("1e-18")
    ),
    "0xa5f2211b9b8170f694421f2046281775e8468044": TokenInfo(
        currency=CurrencyInfo(symbol="THOR", name="THORSwap"), scaling=Decimal("1e-18")
    ),
    "0xa5f8fc0921880cb7342368bd128eb8050442b1a1": TokenInfo(
        currency=CurrencyInfo(symbol="ARY", name="Block Array"), scaling=Decimal("1e-18")
    ),
    "0xa5fd1a791c4dfcaacc963d4f73c6ae5824149ea7": TokenInfo(
        currency=CurrencyInfo(symbol="JNT", name="Jibrel Network"), scaling=Decimal("1e-18")
    ),
    "0xa617e4728f216009b86354797d8d2305d3380179": TokenInfo(
        currency=CurrencyInfo(symbol="PRT", name="PalaceResidence"), scaling=Decimal("1e-18")
    ),
    "0xa6272359bc37f61af398071b65c8934aca744d53": TokenInfo(
        currency=CurrencyInfo(symbol="GMC", name="GokuMarket Credit"), scaling=Decimal("1e-18")
    ),
    "0xa6281838f4a9c5736b2aa1cba9260d3f879623ca": TokenInfo(
        currency=CurrencyInfo(symbol="DCA", name="Decentralize Currency Assets"), scaling=Decimal("1e-18")
    ),
    "0xa62ce5f4175ba550440171ef809197ee21002d64": TokenInfo(
        currency=CurrencyInfo(symbol="SCAVO", name="SCAVO Technologies"), scaling=Decimal("1e-18")
    ),
    "0xa62f436faaa942a518a9543f5ef3174ad4112a9e": TokenInfo(
        currency=CurrencyInfo(symbol="EDRA", name="EDRA"), scaling=Decimal("1e-18")
    ),
    "0xa6446d655a0c34bc4f05042ee88170d056cbaf45": TokenInfo(
        currency=CurrencyInfo(symbol="CSP", name="Caspian"), scaling=Decimal("1e-18")
    ),
    "0xa645264c5603e96c3b0b078cdab68733794b0a71": TokenInfo(
        currency=CurrencyInfo(symbol="MYST", name="Mysterium"), scaling=Decimal("1e-8")
    ),
    "0xa64bd6c70cb9051f6a9ba1f163fdc07e0dfb5f84": TokenInfo(
        currency=CurrencyInfo(symbol="ALINK", name="Aave LINK v1"), scaling=Decimal("1e-18")
    ),
    "0xa66daa57432024023db65477ba87d4e7f5f95213": TokenInfo(
        currency=CurrencyInfo(symbol="HPT", name="Huobi Pool Token"), scaling=Decimal("1e-18")
    ),
    "0xa6714a2e5f0b1bdb97b895b0913b4fcd3a775e4d": TokenInfo(
        currency=CurrencyInfo(symbol="PC", name="PromotionChain"), scaling=Decimal("1e-5")
    ),
    "0xa685a61171bb30d4072b338c80cb7b2c865c873e": TokenInfo(
        currency=CurrencyInfo(symbol="AMANA", name="Aave MANA"), scaling=Decimal("1e-18")
    ),
    "0xa686514faf7d54289266f483d1e4852c99e13ec7": TokenInfo(
        currency=CurrencyInfo(symbol="WORK", name="Aworker"), scaling=Decimal("1e-8")
    ),
    "0xa68b177677452c6858440ca1b5bfce1faaeaa98f": TokenInfo(
        currency=CurrencyInfo(symbol="PZT", name="Panzu Token"), scaling=Decimal("1e-18")
    ),
    "0xa6a840e50bcaa50da017b91a0d86b8b2d41156ee": TokenInfo(
        currency=CurrencyInfo(symbol="EKO", name="EchoLink"), scaling=Decimal("1e-18")
    ),
    "0xa6c040045d962e4b8efa00954c7d23ccd0a2b8ad": TokenInfo(
        currency=CurrencyInfo(symbol="ETHBTC7525", name="ETH BTC 75%/25% Weight Set"), scaling=Decimal("1e-18")
    ),
    "0xa6d6720258cbb7e4a79bb2f379e3d8f25d78b716": TokenInfo(
        currency=CurrencyInfo(symbol="TKL", name="Tokelite"), scaling=Decimal("1e-18")
    ),
    "0xa6e7dc135bdf4b3fee7183eab2e87c0bb9684783": TokenInfo(
        currency=CurrencyInfo(symbol="BIGO", name="BIGOCOIN"), scaling=Decimal("1e-8")
    ),
    "0xa6eb54102f20095679882db4c84e72e65ab782a4": TokenInfo(
        currency=CurrencyInfo(symbol="MGC", name="Magnachain"), scaling=Decimal("1e-8")
    ),
    "0xa6fb1df483b24eeab569e19447e0e107003b9e15": TokenInfo(
        currency=CurrencyInfo(symbol="ENB", name="Earnbase"), scaling=Decimal("1e-18")
    ),
    "0xa701122c1b67220a8b6883d03c8ad67896b12466": TokenInfo(
        currency=CurrencyInfo(symbol="PEW", name="Brofist Coin"), scaling=Decimal("1e-8")
    ),
    "0xa704fce7b309ec09df16e2f5ab8caf6fe8a4baa9": TokenInfo(
        currency=CurrencyInfo(symbol="AGRI", name="AgriChain Utility Token"), scaling=Decimal("1e-18")
    ),
    "0xa70b2f0738749248153446e8feaece123714a104": TokenInfo(
        currency=CurrencyInfo(symbol="KTN", name="Kasoutuuka News"), scaling=Decimal("1e-8")
    ),
    "0xa7211022b34a84905dbc54bcf11d9d395ca4155f": TokenInfo(
        currency=CurrencyInfo(symbol="HTH", name="Heath"), scaling=Decimal("1e-8")
    ),
    "0xa73862c5a66cf3be4bf86f60acf085bd927f83f8": TokenInfo(
        currency=CurrencyInfo(symbol="DF", name="Daily Funds"), scaling=Decimal("1e-8")
    ),
    "0xa740684c9022dc07540031b10dd57984640babef": TokenInfo(
        currency=CurrencyInfo(symbol="DECH", name="Decash"), scaling=Decimal("1e-18")
    ),
    "0xa74476443119a942de498590fe1f2454d7d4ac0d": TokenInfo(
        currency=CurrencyInfo(symbol="GNT", name="Golem Network Token"), scaling=Decimal("1e-18")
    ),
    "0xa771b49064da011df051052848477f18dba1d2ac": TokenInfo(
        currency=CurrencyInfo(symbol="HNS", name="Handshake"), scaling=Decimal("1e-6")
    ),
    "0xa79e0012bb3379f8509a5ab49cab7e6abb49701d": TokenInfo(
        currency=CurrencyInfo(symbol="NAMTC", name="NAMTANCOIN"), scaling=Decimal("1e-18")
    ),
    "0xa7a5c1058194af8f00c187adb7fcc0c95f1c6c2d": TokenInfo(
        currency=CurrencyInfo(symbol="SPIZ", name="SPACE-iZ"), scaling=Decimal("1e-18")
    ),
    "0xa7c8d7a1c894e51dbb7c680b5b1dbdc845bfbdab": TokenInfo(
        currency=CurrencyInfo(symbol="SKT", name="SpeedKingToken"), scaling=Decimal("1e-5")
    ),
    "0xa7d10ff962eda41f3b037e3af1d8b4037eba4b86": TokenInfo(
        currency=CurrencyInfo(symbol="BICAS", name="BitherCash"), scaling=Decimal("1e-18")
    ),
    "0xa7db8a24d77c0a20f9ef84ff219749d9f3e51886": TokenInfo(
        currency=CurrencyInfo(symbol="WORK.CX", name="Slack Technologies Inc"), scaling=Decimal("1e-8")
    ),
    "0xa7de087329bfcda5639247f96140f9dabe3deed1": TokenInfo(
        currency=CurrencyInfo(symbol="STA", name="Statera"), scaling=Decimal("1e-18")
    ),
    "0xa7ed29b253d8b4e3109ce07c80fc570f81b63696": TokenInfo(
        currency=CurrencyInfo(symbol="BAS", name="BAS"), scaling=Decimal("1e-18")
    ),
    "0xa7f976c360ebbed4465c2855684d1aae5271efa9": TokenInfo(
        currency=CurrencyInfo(symbol="TFL", name="TrueFlip"), scaling=Decimal("1e-8")
    ),
    "0xa7fc5d2453e3f68af0cc1b78bcfee94a1b293650": TokenInfo(
        currency=CurrencyInfo(symbol="SPIKE", name="Spiking"), scaling=Decimal("1e-10")
    ),
    "0xa8006c4ca56f24d6836727d106349320db7fef82": TokenInfo(
        currency=CurrencyInfo(symbol="INXT", name="Internxt"), scaling=Decimal("1e-8")
    ),
    "0xa8006e3ac1bd94e54e3136b8e5dd75db0163e6f4": TokenInfo(
        currency=CurrencyInfo(symbol="EOC", name="EveryonesCrypto"), scaling=Decimal("1e-18")
    ),
    "0xa806b3fed6891136940cf81c4085661500aa2709": TokenInfo(
        currency=CurrencyInfo(symbol="SNL", name="Sport and Leisure"), scaling=Decimal("1e-6")
    ),
    "0xa809d363a66c576a2a814cdbfefc107c600a55f0": TokenInfo(
        currency=CurrencyInfo(symbol="HLT", name="Hyperloot"), scaling=Decimal("1e-18")
    ),
    "0xa823e6722006afe99e91c30ff5295052fe6b8e32": TokenInfo(
        currency=CurrencyInfo(symbol="NEU", name="Neumark"), scaling=Decimal("1e-18")
    ),
    "0xa8258abc8f2811dd48eccd209db68f25e3e34667": TokenInfo(
        currency=CurrencyInfo(symbol="DAG", name="Constellation"), scaling=Decimal("1e-8")
    ),
    "0xa8262eb913fccea4c3f77fc95b8b4043b384cfbb": TokenInfo(
        currency=CurrencyInfo(symbol="KGC", name="Krypton Galaxy Coin"), scaling=Decimal("1e-18")
    ),
    "0xa829f97373069ee5d23175e4105df8fd49238be7": TokenInfo(
        currency=CurrencyInfo(symbol="OPNN", name="Opennity"), scaling=Decimal("1e-18")
    ),
    "0xa838be6e4b760e6061d4732d6b9f11bf578f9a76": TokenInfo(
        currency=CurrencyInfo(symbol="TTV", name="TV-TWO"), scaling=Decimal("1e-18")
    ),
    "0xa842844d1a0e2a7bf17c55a3ead3a144a1d51ed7": TokenInfo(
        currency=CurrencyInfo(symbol="ACC", name="AlphaCity"), scaling=Decimal("1e-18")
    ),
    "0xa849eaae994fb86afa73382e9bd88c2b6b18dc71": TokenInfo(
        currency=CurrencyInfo(symbol="MVL", name="MVL"), scaling=Decimal("1e-18")
    ),
    "0xa858bc1b71a895ee83b92f149616f9b3f6afa0fb": TokenInfo(
        currency=CurrencyInfo(symbol="KAT", name="Kambria Token"), scaling=Decimal("1e-18")
    ),
    "0xa866f0198208eb07c83081d5136be7f775c2399e": TokenInfo(
        currency=CurrencyInfo(symbol="KORE", name="Kore"), scaling=Decimal("1e-18")
    ),
    "0xa86a0da9d05d0771955df05b44ca120661af16de": TokenInfo(
        currency=CurrencyInfo(symbol="OTB", name="OTCBTC Token"), scaling=Decimal("1e-18")
    ),
    "0xa86ecab27c0f92f4393a6bcb03b01407b87b0892": TokenInfo(
        currency=CurrencyInfo(symbol="IPN.CX", name="Ipsen"), scaling=Decimal("1e-8")
    ),
    "0xa87135285ae208e22068acdbff64b11ec73eaa5a": TokenInfo(
        currency=CurrencyInfo(symbol="LUNR", name="Lunr Token"), scaling=Decimal("1e-4")
    ),
    "0xa883e72c12473ded50a5fbffa60e4000fa5fe3c8": TokenInfo(
        currency=CurrencyInfo(symbol="LOAD", name="LOAD Network"), scaling=Decimal("1e-8")
    ),
    "0xa8892bfc33fa44053a9e402b1839966f4fec74a4": TokenInfo(
        currency=CurrencyInfo(symbol="CUB", name="Crypto User Base"), scaling=Decimal("1e-18")
    ),
    "0xa897303e3f1ec585aa0816d1527f9025a37a5905": TokenInfo(
        currency=CurrencyInfo(symbol="BBRT", name="Block bank"), scaling=Decimal("1e-2")
    ),
    "0xa89ac6e529acf391cfbbd377f3ac9d93eae9664e": TokenInfo(
        currency=CurrencyInfo(symbol="KP4R", name="Keep4r"), scaling=Decimal("1e-18")
    ),
    "0xa89b5934863447f6e4fc53b315a93e873bda69a3": TokenInfo(
        currency=CurrencyInfo(symbol="LUM", name="LuminoCoin"), scaling=Decimal("1e-18")
    ),
    "0xa89fd5459c67afc8727c07333ed830643cf898b6": TokenInfo(
        currency=CurrencyInfo(symbol="DICO", name="Dico Coin"), scaling=Decimal("1e-8")
    ),
    "0xa8a695e805e0e1b7f5d97d0f8a0b5a298896e508": TokenInfo(
        currency=CurrencyInfo(symbol="BTGS", name="BitDog Token"), scaling=Decimal("1e-18")
    ),
    "0xa8b0f154a688c22142e361707df64277e0a0be66": TokenInfo(
        currency=CurrencyInfo(symbol="RAK", name="Rake Finance"), scaling=Decimal("1e-18")
    ),
    "0xa8b12cc90abf65191532a12bb5394a714a46d358": TokenInfo(
        currency=CurrencyInfo(symbol="PBTC35A", name="pBTC35A"), scaling=Decimal("1e-18")
    ),
    "0xa8b919680258d369114910511cc87595aec0be6d": TokenInfo(
        currency=CurrencyInfo(symbol="LYXE", name="LUKSO Token"), scaling=Decimal("1e-18")
    ),
    "0xa8b9cd2577d20224af856c19af20040290705932": TokenInfo(
        currency=CurrencyInfo(symbol="EVC", name="Eleent Value Chain"), scaling=Decimal("1e-8")
    ),
    "0xa8c8cfb141a3bb59fea1e2ea6b79b5ecbcd7b6ca": TokenInfo(
        currency=CurrencyInfo(symbol="NOIA", name="Syntropy"), scaling=Decimal("1e-18")
    ),
    "0xa8daa52ded91f7c82b4bb02b4b87c6a841db1fd5": TokenInfo(
        currency=CurrencyInfo(symbol="BGF", name="Biograffi"), scaling=Decimal("1e-8")
    ),
    "0xa8dba64afc4a8704c98b0d1c9bfb7d307b30963a": TokenInfo(
        currency=CurrencyInfo(symbol="XSHOP", name="Shopereum"), scaling=Decimal("1e-18")
    ),
    "0xa8e7ad77c60ee6f30bac54e2e7c0617bd7b5a03e": TokenInfo(
        currency=CurrencyInfo(symbol="ZLOT", name="zLOT"), scaling=Decimal("1e-18")
    ),
    "0xa8f93faee440644f89059a2c88bdc9bf3be5e2ea": TokenInfo(
        currency=CurrencyInfo(symbol="CASH", name="Cash Poker Pro"), scaling=Decimal("1e-18")
    ),
    "0xa9080bf7c8e55f2af5c6603243d5865f4f328715": TokenInfo(
        currency=CurrencyInfo(symbol="MAR", name="MARKYT"), scaling=Decimal("1e-18")
    ),
    "0xa90c43e0d6c92b8e6171a829beb38be28a0ad073": TokenInfo(
        currency=CurrencyInfo(symbol="EUSD", name="Egoras Dollar"), scaling=Decimal("1e-18")
    ),
    "0xa91464abd4625a23ab719e3f0fce84dadd54e546": TokenInfo(
        currency=CurrencyInfo(symbol="IVI", name="Inoovi"), scaling=Decimal("1e-18")
    ),
    "0xa91ac63d040deb1b7a5e4d4134ad23eb0ba07e14": TokenInfo(
        currency=CurrencyInfo(symbol="BEL", name="Bella Protocol"), scaling=Decimal("1e-18")
    ),
    "0xa9240fbcac1f0b9a6adfb04a53c8e3b0cc1d1444": TokenInfo(
        currency=CurrencyInfo(symbol="HIG", name="ethereumhigh"), scaling=Decimal("1e-18")
    ),
    "0xa92e7c82b11d10716ab534051b271d2f6aef7df5": TokenInfo(
        currency=CurrencyInfo(symbol="ARA", name="Ara"), scaling=Decimal("1e-18")
    ),
    "0xa93f2a6b50d92bd64848f5ea15164f558b75ce9c": TokenInfo(
        currency=CurrencyInfo(symbol="thrm", name="thirm"), scaling=Decimal("1e-18")
    ),
    "0xa95592dcffa3c080b4b40e459c5f5692f67db7f8": TokenInfo(
        currency=CurrencyInfo(symbol="ELY", name="Elysian"), scaling=Decimal("1e-18")
    ),
    "0xa960d2ba7000d58773e7fa5754dec3bb40a069d5": TokenInfo(
        currency=CurrencyInfo(symbol="ODEX", name="One DEX"), scaling=Decimal("1e-18")
    ),
    "0xa96f31f1c187c28980176c3a27ba7069f48abde4": TokenInfo(
        currency=CurrencyInfo(symbol="ETGP", name="Ethereum Gold Project"), scaling=Decimal("1e-8")
    ),
    "0xa974c709cfb4566686553a20790685a47aceaa33": TokenInfo(
        currency=CurrencyInfo(symbol="XIN", name="Mixin"), scaling=Decimal("1e-18")
    ),
    "0xa982b2e19e90b2d9f7948e9c1b65d119f1ce88d6": TokenInfo(
        currency=CurrencyInfo(symbol="WOM", name="WOM Token"), scaling=Decimal("1e-18")
    ),
    "0xa9859874e1743a32409f75bb11549892138bba1e": TokenInfo(
        currency=CurrencyInfo(symbol="IETH", name="iETH"), scaling=Decimal("1e-18")
    ),
    "0xa9877b1e05d035899131dbd1e403825166d09f92": TokenInfo(
        currency=CurrencyInfo(symbol="MNT", name="Media Network Token"), scaling=Decimal("1e-18")
    ),
    "0xa98ed1fd277ead2c00d143cbe1465f59e65a0066": TokenInfo(
        currency=CurrencyInfo(symbol="THX", name="Thx!"), scaling=Decimal("1e-18")
    ),
    "0xa9aa40627c6b989f97a6656a4ad658275479361c": TokenInfo(
        currency=CurrencyInfo(symbol="MFR", name="MAFER"), scaling=Decimal("1e-8")
    ),
    "0xa9aad2dc3a8315caeee5f458b1d8edc31d8467bd": TokenInfo(
        currency=CurrencyInfo(symbol="BTCM", name="BTCMoon"), scaling=Decimal("1e-18")
    ),
    "0xa9b1eb5908cfc3cdf91f9b8b3a74108598009096": TokenInfo(
        currency=CurrencyInfo(symbol="AUCTION", name="Bounce"), scaling=Decimal("1e-18")
    ),
    "0xa9c44135b3a87e0688c41cf8c27939a22dd437c9": TokenInfo(
        currency=CurrencyInfo(symbol="BOOB", name="BooBank"), scaling=Decimal("1e-18")
    ),
    "0xa9d2927d3a04309e008b6af6e2e282ae2952e7fd": TokenInfo(
        currency=CurrencyInfo(symbol="ZIP", name="Zipper Network"), scaling=Decimal("1e-18")
    ),
    "0xa9e201a4e269d6cd5e9f0fcbcb78520cf815878b": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNIRENWETH", name="Aave AMM UniRENWETH"), scaling=Decimal("1e-18")
    ),
    "0xa9fbb83a2689f4ff86339a4b96874d718673b627": TokenInfo(
        currency=CurrencyInfo(symbol="ANTS", name="FireAnts"), scaling=Decimal("1e-18")
    ),
    "0xa9fc65da36064ce545e87690e06f5de10c52c690": TokenInfo(
        currency=CurrencyInfo(symbol="BCHBEAR", name="3X Short Bitcoin Cash Token"), scaling=Decimal("1e-18")
    ),
    "0xa9ff725189fe00da9c5f27a580dc67fea61e3fb2": TokenInfo(
        currency=CurrencyInfo(symbol="ARM", name="Armours"), scaling=Decimal("1e-18")
    ),
    "0xaa031595d2d9b82847a5df3390c6395839b273d0": TokenInfo(
        currency=CurrencyInfo(symbol="LXT", name="LEXIT Token"), scaling=Decimal("1e-18")
    ),
    "0xaa0bb10cec1fa372eb3abc17c933fc6ba863dd9e": TokenInfo(
        currency=CurrencyInfo(symbol="HMC", name="Hi Mutual Society"), scaling=Decimal("1e-18")
    ),
    "0xaa1878e5243b86c4ba9073f8419ccb37bfeb5631": TokenInfo(
        currency=CurrencyInfo(symbol="MGM.CX", name="MGM Resorts International"), scaling=Decimal("1e-8")
    ),
    "0xaa19673aa1b483a5c4f73b446b4f851629a7e7d6": TokenInfo(
        currency=CurrencyInfo(symbol="XETH", name="Xplosive Ethereum"), scaling=Decimal("1e-18")
    ),
    "0xaa19961b6b858d9f18a115f25aa1d98abc1fdba8": TokenInfo(
        currency=CurrencyInfo(symbol="LCS", name="LocalCoinSwap"), scaling=Decimal("1e-18")
    ),
    "0xaa2ce7ae64066175e0b90497ce7d9c190c315db4": TokenInfo(
        currency=CurrencyInfo(symbol="SUTER", name="Suterusu"), scaling=Decimal("1e-18")
    ),
    "0xaa3a522d9e25070d30961baeae0112498f90e295": TokenInfo(
        currency=CurrencyInfo(symbol="JBT", name="Jukebucks"), scaling=Decimal("1e-18")
    ),
    "0xaa3f8e382cb01cae98a7f37a170f3d218c38e3ec": TokenInfo(
        currency=CurrencyInfo(symbol="FIN", name="FENNIECOIN"), scaling=Decimal("1e-18")
    ),
    "0xaa4ab1c817e4df7d25ce4d42352649d592a3bba0": TokenInfo(
        currency=CurrencyInfo(symbol="ANK", name="Ankorus Token"), scaling=Decimal("1e-18")
    ),
    "0xaa4e3edb11afa93c41db59842b29de64b72e355b": TokenInfo(
        currency=CurrencyInfo(symbol="MFI", name="Marginswap"), scaling=Decimal("1e-18")
    ),
    "0xaa5c28be0f1173612ea3fcc9e461ccb7b9390213": TokenInfo(
        currency=CurrencyInfo(symbol="EVCO", name="EVCOIN"), scaling=Decimal("1e-18")
    ),
    "0xaa602de53347579f86b996d2add74bb6f79462b2": TokenInfo(
        currency=CurrencyInfo(symbol="ZMT", name="Zipmex Token"), scaling=Decimal("1e-18")
    ),
    "0xaa6e8127831c9de45ae56bb1b0d4d4da6e5665bd": TokenInfo(
        currency=CurrencyInfo(symbol="ETH2X-FLI", name="ETH 2x Flexible Leverage Index"), scaling=Decimal("1e-18")
    ),
    "0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f": TokenInfo(
        currency=CurrencyInfo(symbol="TRAC", name="OriginTrail"), scaling=Decimal("1e-18")
    ),
    "0xaa8330fb2b4d5d07abfe7a72262752a8505c6b37": TokenInfo(
        currency=CurrencyInfo(symbol="POLC", name="Polkacity"), scaling=Decimal("1e-18")
    ),
    "0xaa843f65872a25d6e9552ea0b360fb1d5e333124": TokenInfo(
        currency=CurrencyInfo(symbol="EVC", name="Eco Value Coin"), scaling=Decimal("1e-18")
    ),
    "0xaaa7a10a8ee237ea61e8ac46c50a8db8bcc1baaa": TokenInfo(
        currency=CurrencyInfo(symbol="QANX", name="QANplatform"), scaling=Decimal("1e-18")
    ),
    "0xaaaaaa20d9e0e2461697782ef11675f668207961": TokenInfo(
        currency=CurrencyInfo(symbol="AURORA", name="Aurora"), scaling=Decimal("1e-18")
    ),
    "0xaaaaaaaba2ea3daab0a6c05f1b962c78c9836d99": TokenInfo(
        currency=CurrencyInfo(symbol="AZ", name="Azbit"), scaling=Decimal("1e-18")
    ),
    "0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d": TokenInfo(
        currency=CurrencyInfo(symbol="CEL", name="Celsius Network"), scaling=Decimal("1e-4")
    ),
    "0xaaaf91d9b90df800df4f55c205fd6989c977e73a": TokenInfo(
        currency=CurrencyInfo(symbol="TKN", name="Monolith"), scaling=Decimal("1e-8")
    ),
    "0xaab29ecc3783acb436a6679919f22d30932e93f2": TokenInfo(
        currency=CurrencyInfo(symbol="IFTC", name="Internet Fintech Coin"), scaling=Decimal("1e-18")
    ),
    "0xaab606817809841e8b1168be8779eeaf6744ef64": TokenInfo(
        currency=CurrencyInfo(symbol="TTA", name="Tend Token"), scaling=Decimal("1e-18")
    ),
    "0xaac41ec512808d64625576eddd580e7ea40ef8b2": TokenInfo(
        currency=CurrencyInfo(symbol="GSWAP", name="Gameswap"), scaling=Decimal("1e-18")
    ),
    "0xaaca86b876ca011844b5798eca7a67591a9743c8": TokenInfo(
        currency=CurrencyInfo(symbol="BIOS", name="0x nodes"), scaling=Decimal("1e-18")
    ),
    "0xaace6480798b4a7b596ec4ce3a26b8de9b9ae2e2": TokenInfo(
        currency=CurrencyInfo(symbol="PLNX", name="eToro Polish Zloty"), scaling=Decimal("1e-18")
    ),
    "0xaad483f97f13c6a20b9d05d07c397ce85c42c393": TokenInfo(
        currency=CurrencyInfo(symbol="WOOP", name="Woonkly Power"), scaling=Decimal("1e-18")
    ),
    "0xaae81c0194d6459f320b70ca0cedf88e11a242ce": TokenInfo(
        currency=CurrencyInfo(symbol="WT", name="World Wi-Fi WeToken"), scaling=Decimal("1e-18")
    ),
    "0xaaef88cea01475125522e117bfe45cf32044e238": TokenInfo(
        currency=CurrencyInfo(symbol="GF", name="GuildFi"), scaling=Decimal("1e-18")
    ),
    "0xaaf37055188feee4869de63464937e683d61b2a1": TokenInfo(
        currency=CurrencyInfo(symbol="UCN", name="UChain"), scaling=Decimal("1e-18")
    ),
    "0xab37e1358b639fd877f015027bb62d3ddaa7557e": TokenInfo(
        currency=CurrencyInfo(symbol="LIEN", name="Lien"), scaling=Decimal("1e-8")
    ),
    "0xab51e836bdcbc7cc06d926c50d88328f1bb17148": TokenInfo(
        currency=CurrencyInfo(symbol="WCDC", name="World Credit Diamond Coin"), scaling=Decimal("1e-18")
    ),
    "0xab55bdef7057b76482914e79f037999f4ebb6bf1": TokenInfo(
        currency=CurrencyInfo(symbol="HP", name="Healing Plus"), scaling=Decimal("1e-8")
    ),
    "0xab5c04bbe42667610a2da07ac98ea9fa6e4a9514": TokenInfo(
        currency=CurrencyInfo(symbol="IZER", name="IZEROIUM"), scaling=Decimal("1e-8")
    ),
    "0xab622b253e441928affa6e2efb2f0f9a8bf6890d": TokenInfo(
        currency=CurrencyInfo(symbol="NUT", name="NutCoin"), scaling=Decimal("1e-4")
    ),
    "0xab6cf87a50f17d7f5e1feaf81b6fe9ffbe8ebf84": TokenInfo(
        currency=CurrencyInfo(symbol="MRV", name="Macroverse Token"), scaling=Decimal("1e-18")
    ),
    "0xab7aaf9e485a3bc885985184abe9fc6aba727bd6": TokenInfo(
        currency=CurrencyInfo(symbol="MANY", name="MANY"), scaling=Decimal("1e-18")
    ),
    "0xab93df617f51e1e415b5b4f8111f122d6b48e55c": TokenInfo(
        currency=CurrencyInfo(symbol="DETO", name="Delta Exchange Toke"), scaling=Decimal("1e-18")
    ),
    "0xab95e915c123fded5bdfb6325e35ef5515f1ea69": TokenInfo(
        currency=CurrencyInfo(symbol="XNN", name="Xenon Network"), scaling=Decimal("1e-18")
    ),
    "0xaba8cac6866b83ae4eec97dd07ed254282f6ad8a": TokenInfo(
        currency=CurrencyInfo(symbol="YAMV2", name="YAM v2"), scaling=Decimal("1e-24")
    ),
    "0xabb77f5c1e1c61adc3666b62dc614e64c584be6b": TokenInfo(
        currency=CurrencyInfo(symbol="TCOIN", name="TRUECOIN"), scaling=Decimal("1e-8")
    ),
    "0xabbbb6447b68ffd6141da77c18c7b5876ed6c5ab": TokenInfo(
        currency=CurrencyInfo(symbol="DATX", name="DATx"), scaling=Decimal("1e-18")
    ),
    "0xabc1280a0187a2020cc675437aed400185f86db6": TokenInfo(
        currency=CurrencyInfo(symbol="SAC", name="Smart Application Coin"), scaling=Decimal("1e-18")
    ),
    "0xabc430136a4de71c9998242de8c1b4b97d2b9045": TokenInfo(
        currency=CurrencyInfo(symbol="VRS", name="Veros"), scaling=Decimal("1e-6")
    ),
    "0xabc754ac2161b557d28062f41dcc0fc18440ac7e": TokenInfo(
        currency=CurrencyInfo(symbol="ETH10K", name="ETH Maximalist Set"), scaling=Decimal("1e-18")
    ),
    "0xabccaadd77078a67622dfd5f74066ce4581c0a99": TokenInfo(
        currency=CurrencyInfo(symbol="MAME", name="mameCoin"), scaling=Decimal("1e-8")
    ),
    "0xabd1f4cf6d1119895faed8dea5748726f254b3b2": TokenInfo(
        currency=CurrencyInfo(symbol="MBIT", name="MessengerBank"), scaling=Decimal("1e-8")
    ),
    "0xabdf147870235fcfc34153828c769a70b3fae01f": TokenInfo(
        currency=CurrencyInfo(symbol="EURT", name="Tether EUR"), scaling=Decimal("1e-6")
    ),
    "0xabe580e7ee158da464b51ee1a83ac0289622e6be": TokenInfo(
        currency=CurrencyInfo(symbol="XFT", name="Offshift"), scaling=Decimal("1e-18")
    ),
    "0xac0104cca91d167873b8601d2e71eb3d4d8c33e0": TokenInfo(
        currency=CurrencyInfo(symbol="CWS", name="Crowns"), scaling=Decimal("1e-18")
    ),
    "0xac0c8da4a4748d8d821a0973d00b157aa78c473d": TokenInfo(
        currency=CurrencyInfo(symbol="YFO", name="YFIONE"), scaling=Decimal("1e-18")
    ),
    "0xac1565e473f69fada09661a6b4103fbbf801ceee": TokenInfo(
        currency=CurrencyInfo(symbol="IETH50SMACO", name="Inverse ETH 50 Day MA Crossover Set"),
        scaling=Decimal("1e-18"),
    ),
    "0xac2385e183d9301dd5e2bb08da932cbf9800dc9c": TokenInfo(
        currency=CurrencyInfo(symbol="LIQUID", name="Netkoin Liquid"), scaling=Decimal("1e-18")
    ),
    "0xac2e58a06e6265f1cf5084ee58da68e5d75b49ca": TokenInfo(
        currency=CurrencyInfo(symbol="ORS", name="ORS Group"), scaling=Decimal("1e-18")
    ),
    "0xac3211a5025414af2866ff09c23fc18bc97e79b1": TokenInfo(
        currency=CurrencyInfo(symbol="DOV", name="Dovu"), scaling=Decimal("1e-18")
    ),
    "0xac3da587eac229c9896d919abc235ca4fd7f72c1": TokenInfo(
        currency=CurrencyInfo(symbol="TGT", name="Target Coin"), scaling=Decimal("1e-1")
    ),
    "0xac4d22e40bf0b8ef4750a99ed4e935b99a42685e": TokenInfo(
        currency=CurrencyInfo(symbol="AER", name="Aeryus"), scaling=Decimal("1e-18")
    ),
    "0xac4f2f204b38390b92d0540908447d5ed352799a": TokenInfo(
        currency=CurrencyInfo(symbol="OLDNII", name="Nahmii v1 (DEPRECATED)"), scaling=Decimal("1e-15")
    ),
    "0xac51066d7bec65dc4589368da368b212745d63e8": TokenInfo(
        currency=CurrencyInfo(symbol="ALICE", name="My Neighbor Alice"), scaling=Decimal("1e-6")
    ),
    "0xac5470280c680956b1851f4ef9330f32e6fd243f": TokenInfo(
        currency=CurrencyInfo(symbol="KNG", name="KingCoin"), scaling=Decimal("1e-18")
    ),
    "0xac57de9c1a09fec648e93eb98875b212db0d460b": TokenInfo(
        currency=CurrencyInfo(symbol="BABYDOGE", name="Baby Doge Coin"), scaling=Decimal("1e-9")
    ),
    "0xac6560df686f3ac7039b0dd6867c874c99d9da06": TokenInfo(
        currency=CurrencyInfo(symbol="EVOL", name="ETH Volatility Adjusted Set"), scaling=Decimal("1e-18")
    ),
    "0xac6df26a590f08dcc95d5a4705ae8abbc88509ef": TokenInfo(
        currency=CurrencyInfo(symbol="AENJ", name="Aave ENJ"), scaling=Decimal("1e-18")
    ),
    "0xac709fcb44a43c35f0da4e3163b117a17f3770f5": TokenInfo(
        currency=CurrencyInfo(symbol="ARC", name="Arcade Token"), scaling=Decimal("1e-18")
    ),
    "0xac8e13ecc30da7ff04b842f21a62a1fb0f10ebd5": TokenInfo(
        currency=CurrencyInfo(symbol="BABYDOGE", name="BabyDoge ETH"), scaling=Decimal("1e-9")
    ),
    "0xac8ea871e2d5f4be618905f36f73c760f8cfdc8e": TokenInfo(
        currency=CurrencyInfo(symbol="BYTE", name="BTC Network Demand Set II"), scaling=Decimal("1e-18")
    ),
    "0xac9749c854b31bba3b3e71b30fdd7aea4fcc0db9": TokenInfo(
        currency=CurrencyInfo(symbol="FBC", name="FightBackCoin"), scaling=Decimal("1e-18")
    ),
    "0xac9bb427953ac7fddc562adca86cf42d988047fd": TokenInfo(
        currency=CurrencyInfo(symbol="STT", name="Scatter.cx"), scaling=Decimal("1e-18")
    ),
    "0xac9ce326e95f51b5005e9fe1dd8085a01f18450c": TokenInfo(
        currency=CurrencyInfo(symbol="VSF", name="VeriSafe"), scaling=Decimal("1e-18")
    ),
    "0xacaca5b8805636608e14c64b0bfffc2deb2c6cec": TokenInfo(
        currency=CurrencyInfo(symbol="ROM", name="ROM Token"), scaling=Decimal("1e-18")
    ),
    "0xacb53386b1c8015ae9352c8482d10c0d4a03c38a": TokenInfo(
        currency=CurrencyInfo(symbol="CMID", name="CREATIVE MEDIA INITIATIVE"), scaling=Decimal("1e-18")
    ),
    "0xacce88f5a63a5e65db9aa7303720be16b556e751": TokenInfo(
        currency=CurrencyInfo(symbol="NEAL", name="Coineal Token"), scaling=Decimal("1e-18")
    ),
    "0xacf3d402e5e2c3edd5b8129e966017d293f12a4c": TokenInfo(
        currency=CurrencyInfo(symbol="BAXS", name="BoxAxis"), scaling=Decimal("1e-18")
    ),
    "0xacfa209fb73bf3dd5bbfb1101b9bc999c49062a5": TokenInfo(
        currency=CurrencyInfo(symbol="BCDT", name="EvidenZ"), scaling=Decimal("1e-18")
    ),
    "0xad22f63404f7305e4713ccbd4f296f34770513f4": TokenInfo(
        currency=CurrencyInfo(symbol="AWC", name="Atomic Wallet Coin"), scaling=Decimal("1e-8")
    ),
    "0xad32a8e6220741182940c5abf610bde99e737b2d": TokenInfo(
        currency=CurrencyInfo(symbol="DOUGH", name="PieDAO DOUGH v2"), scaling=Decimal("1e-18")
    ),
    "0xad3e3fc59dff318beceaab7d00eb4f68b1ecf195": TokenInfo(
        currency=CurrencyInfo(symbol="WCUSD", name="Wrapped Celo Dollar"), scaling=Decimal("1e-18")
    ),
    "0xad4f86a25bbc20ffb751f2fac312a0b4d8f88c64": TokenInfo(
        currency=CurrencyInfo(symbol="ROOM", name="OptionRoom"), scaling=Decimal("1e-18")
    ),
    "0xad584f8b2d721adbd28f587274aa4ebe488b3ba8": TokenInfo(
        currency=CurrencyInfo(symbol="GHC", name="GHC"), scaling=Decimal("1e-18")
    ),
    "0xad5fe5b0b8ec8ff4565204990e4405b2da117d8e": TokenInfo(
        currency=CurrencyInfo(symbol="TRXC", name="TronClassic"), scaling=Decimal("1e-0")
    ),
    "0xad640689e6950b7453729a4686edb3fdfd754616": TokenInfo(
        currency=CurrencyInfo(symbol="CIC", name="CIChain"), scaling=Decimal("1e-18")
    ),
    "0xad6683b7f3618c44f5ca6040902812dd890dde4d": TokenInfo(
        currency=CurrencyInfo(symbol="TNO", name="TNOS COIN"), scaling=Decimal("1e-18")
    ),
    "0xad6714bd97cbbd29788f8838bc865ee71b843eb8": TokenInfo(
        currency=CurrencyInfo(symbol="HDLB", name="HODL Bucks"), scaling=Decimal("1e-8")
    ),
    "0xad6a626ae2b43dcb1b39430ce496d2fa0365ba9c": TokenInfo(
        currency=CurrencyInfo(symbol="DEFI+S", name="PieDAO DEFI Small Cap"), scaling=Decimal("1e-18")
    ),
    "0xad7195e2f5e4f104cc2ed31cb719efd95b9eb490": TokenInfo(
        currency=CurrencyInfo(symbol="IOTE", name="IOTEdge Network"), scaling=Decimal("1e-18")
    ),
    "0xad808ba4eb817a968889ec0e93130c4fde8e71b8": TokenInfo(
        currency=CurrencyInfo(symbol="PBC", name="Parinita Bansode Coin"), scaling=Decimal("1e-8")
    ),
    "0xad8dd4c725de1d31b9e8f8d146089e9dc6882093": TokenInfo(
        currency=CurrencyInfo(symbol="MIT", name="Mychatcoin"), scaling=Decimal("1e-6")
    ),
    "0xad9355f782c6ec75f134b93304b8f9a691a4432a": TokenInfo(
        currency=CurrencyInfo(symbol="TRU", name="TERASU"), scaling=Decimal("1e-18")
    ),
    "0xada62f7ccd6af6cacff04accbc4f56f3d4ffd4ef": TokenInfo(
        currency=CurrencyInfo(symbol="PLF", name="PlayFuel"), scaling=Decimal("1e-18")
    ),
    "0xada86b1b313d1d5267e3fc0bb303f0a2b66d0ea7": TokenInfo(
        currency=CurrencyInfo(symbol="COV", name="Covesting"), scaling=Decimal("1e-18")
    ),
    "0xadb2437e6f65682b85f814fbc12fec0508a7b1d0": TokenInfo(
        currency=CurrencyInfo(symbol="UNCX", name="UniCrypt"), scaling=Decimal("1e-18")
    ),
    "0xadd5e881984783dd432f80381fb52f45b53f3e70": TokenInfo(
        currency=CurrencyInfo(symbol="VITE", name="Vite"), scaling=Decimal("1e-18")
    ),
    "0xade00c28244d5ce17d72e40330b1c318cd12b7c3": TokenInfo(
        currency=CurrencyInfo(symbol="ADX", name="AdEx"), scaling=Decimal("1e-18")
    ),
    "0xadf8b8050639b6236915f7516d69de714672f0bf": TokenInfo(
        currency=CurrencyInfo(symbol="SWC", name="Scanetchain"), scaling=Decimal("1e-18")
    ),
    "0xae12c5930881c53715b369cec7606b70d8eb229f": TokenInfo(
        currency=CurrencyInfo(symbol="C98", name="Coin98"), scaling=Decimal("1e-18")
    ),
    "0xae17f4f5ca32f77ea8e3786db7c0b2fe877ac176": TokenInfo(
        currency=CurrencyInfo(symbol="BCC", name="Basis Coin Cash"), scaling=Decimal("1e-18")
    ),
    "0xae1eaae3f627aaca434127644371b67b18444051": TokenInfo(
        currency=CurrencyInfo(symbol="YOP", name="Yield Optimization Platform & Protocol"), scaling=Decimal("1e-8")
    ),
    "0xae31b85bfe62747d0836b82608b4830361a3d37a": TokenInfo(
        currency=CurrencyInfo(symbol="AERGO", name="Aergo"), scaling=Decimal("1e-18")
    ),
    "0xae353daeed8dcc7a9a12027f7e070c0a50b7b6a4": TokenInfo(
        currency=CurrencyInfo(symbol="MINX", name="InnovaMinex"), scaling=Decimal("1e-6")
    ),
    "0xae36c4a6e5076d76579dd2b00df90890da2fbae8": TokenInfo(
        currency=CurrencyInfo(symbol="KOP", name="BitKop Token"), scaling=Decimal("1e-18")
    ),
    "0xae4f56f072c34c0a65b3ae3e4db797d831439d93": TokenInfo(
        currency=CurrencyInfo(symbol="GIM", name="Gimli"), scaling=Decimal("1e-8")
    ),
    "0xae679636776e1f9e3d02daf2c4023ae0cedd93a4": TokenInfo(
        currency=CurrencyInfo(symbol="AGBC", name="AgriBlock"), scaling=Decimal("1e-18")
    ),
    "0xae697f994fc5ebc000f8e22ebffee04612f98a0d": TokenInfo(
        currency=CurrencyInfo(symbol="LGCY", name="LGCY Network"), scaling=Decimal("1e-18")
    ),
    "0xae6eb6f6c0a1694968b9f78a4316319c27b0964b": TokenInfo(
        currency=CurrencyInfo(symbol="OIL", name="PETROLEUM"), scaling=Decimal("1e-18")
    ),
    "0xae73b38d1c9a8b274127ec30160a4927c4d71824": TokenInfo(
        currency=CurrencyInfo(symbol="STK", name="STK"), scaling=Decimal("1e-18")
    ),
    "0xae73e05847461dce0d113cd2f09c7069b85b6e3e": TokenInfo(
        currency=CurrencyInfo(symbol="EVS", name="ETH Vol Switching Set"), scaling=Decimal("1e-18")
    ),
    "0xae7ab96520de3a18e5e111b5eaab095312d7fe84": TokenInfo(
        currency=CurrencyInfo(symbol="STETH", name="Lido Staked Ether"), scaling=Decimal("1e-18")
    ),
    "0xae8488e75493b89a0e1488bf91542208c416f486": TokenInfo(
        currency=CurrencyInfo(symbol="BUZ", name="Buzcoin"), scaling=Decimal("1e-18")
    ),
    "0xaea46a60368a7bd060eec7df8cba43b7ef41ad85": TokenInfo(
        currency=CurrencyInfo(symbol="FET", name="Fetch.ai"), scaling=Decimal("1e-18")
    ),
    "0xaea5e11e22e447fa9837738a0cd2848857748adf": TokenInfo(
        currency=CurrencyInfo(symbol="SOFI", name="Social Finance"), scaling=Decimal("1e-18")
    ),
    "0xaec2e87e0a235266d9c5adc9deb4b2e29b54d009": TokenInfo(
        currency=CurrencyInfo(symbol="SNGLS", name="SingularDTV"), scaling=Decimal("1e-0")
    ),
    "0xaec39406348becc28aa008b70fef6063a36ce10f": TokenInfo(
        currency=CurrencyInfo(symbol="THP", name="TurboHigh Performance"), scaling=Decimal("1e-18")
    ),
    "0xaec7e1f531bb09115103c53ba76829910ec48966": TokenInfo(
        currency=CurrencyInfo(symbol="BLANK", name="Blank"), scaling=Decimal("1e-18")
    ),
    "0xaec98a708810414878c3bcdf46aad31ded4a4557": TokenInfo(
        currency=CurrencyInfo(symbol="300", name="300 Token"), scaling=Decimal("1e-18")
    ),
    "0xaecc217a749c2405b5ebc9857a16d58bdc1c367f": TokenInfo(
        currency=CurrencyInfo(symbol="PAWTH", name="Pawthereum"), scaling=Decimal("1e-9")
    ),
    "0xaee7474c3713ece228aa5ec43c89c708f2ec7ed2": TokenInfo(
        currency=CurrencyInfo(symbol="SLOT", name="Alphaslot"), scaling=Decimal("1e-18")
    ),
    "0xaeea2ebc48178af826986314280da3d6743e6766": TokenInfo(
        currency=CurrencyInfo(symbol="DLT", name="Dalong Token"), scaling=Decimal("1e-6")
    ),
    "0xaef38fbfbf932d1aef3b808bc8fbd8cd8e1f8bc5": TokenInfo(
        currency=CurrencyInfo(symbol="CRB", name="Creditbit"), scaling=Decimal("1e-8")
    ),
    "0xaef4f02e31cdbf007f8d98da4ae365188a0e9ecc": TokenInfo(
        currency=CurrencyInfo(symbol="TFT", name="The Famous Token"), scaling=Decimal("1e-8")
    ),
    "0xaf0336137c2f68e881cea7d95059e6b2ddcf7e57": TokenInfo(
        currency=CurrencyInfo(symbol="PDC", name="PLATINUM DIGITAL CORPORATED"), scaling=Decimal("1e-18")
    ),
    "0xaf1250fa68d7decd34fd75de8742bc03b29bd58e": TokenInfo(
        currency=CurrencyInfo(symbol="IHF", name="Invictus Hyperion Fund"), scaling=Decimal("1e-18")
    ),
    "0xaf146fbd319ca7ae178caa2c9d80a2db6b944350": TokenInfo(
        currency=CurrencyInfo(symbol="PXT", name="Propx"), scaling=Decimal("1e-18")
    ),
    "0xaf30d2a7e90d7dc361c8c4585e9bb7d2f6f15bc7": TokenInfo(
        currency=CurrencyInfo(symbol="1ST", name="First Blood"), scaling=Decimal("1e-18")
    ),
    "0xaf4dce16da2877f8c9e00544c93b62ac40631f16": TokenInfo(
        currency=CurrencyInfo(symbol="MTH", name="Monetha"), scaling=Decimal("1e-5")
    ),
    "0xaf5e6afa14a5de9a48395869f4f887a63f7f755f": TokenInfo(
        currency=CurrencyInfo(symbol="BBY", name="BlocBuy"), scaling=Decimal("1e-18")
    ),
    "0xaf691508ba57d416f895e32a1616da1024e882d2": TokenInfo(
        currency=CurrencyInfo(symbol="PNODE", name="Pinknode"), scaling=Decimal("1e-18")
    ),
    "0xaf80951201a0eff85a0fd3adf4c7043db856d3e6": TokenInfo(
        currency=CurrencyInfo(symbol="MBN", name="Mobilian Coin"), scaling=Decimal("1e-18")
    ),
    "0xaf80e6612d9c2e883122e7f2292ee6c34176ad4f": TokenInfo(
        currency=CurrencyInfo(symbol="JAN", name="CoinJanitor"), scaling=Decimal("1e-18")
    ),
    "0xaf8a215e81faea7c180ce22b72483525121813bd": TokenInfo(
        currency=CurrencyInfo(symbol="EGCC", name="Engine"), scaling=Decimal("1e-18")
    ),
    "0xaf9f549774ecedbd0966c52f250acc548d3f36e5": TokenInfo(
        currency=CurrencyInfo(symbol="RFUEL", name="RioDeFi"), scaling=Decimal("1e-18")
    ),
    "0xafbec4d65bc7b116d85107fd05d912491029bf46": TokenInfo(
        currency=CurrencyInfo(symbol="ARB", name="ARBITRAGE"), scaling=Decimal("1e-18")
    ),
    "0xafc21be9e4d9303d51a61cc5a236619e65e873d9": TokenInfo(
        currency=CurrencyInfo(symbol="BIDU.CX", name="Baidu Inc"), scaling=Decimal("1e-8")
    ),
    "0xafc39788c51f0c1ff7b55317f3e70299e521fff6": TokenInfo(
        currency=CurrencyInfo(symbol="EBCH", name="eBitcoin Cash"), scaling=Decimal("1e-8")
    ),
    "0xafd870f32ce54efdbf677466b612bf8ad164454b": TokenInfo(
        currency=CurrencyInfo(symbol="IBNB", name="iBNB"), scaling=Decimal("1e-18")
    ),
    "0xafe60511341a37488de25bef351952562e31fcc1": TokenInfo(
        currency=CurrencyInfo(symbol="TBT", name="TBOT"), scaling=Decimal("1e-8")
    ),
    "0xaff4abdc75f07387401ba9bc0f75ebe4c734b4c9": TokenInfo(
        currency=CurrencyInfo(symbol="TTC", name="TheTimesChainCoin"), scaling=Decimal("1e-18")
    ),
    "0xaff84e86d72edb971341a6a66eb2da209446fa14": TokenInfo(
        currency=CurrencyInfo(symbol="TCAT", name="The Currency Analytics"), scaling=Decimal("1e-18")
    ),
    "0xaffcdd96531bcd66faed95fc61e443d08f79efef": TokenInfo(
        currency=CurrencyInfo(symbol="PMGT", name="Perth Mint Gold Token"), scaling=Decimal("1e-5")
    ),
    "0xb020ed54651831878e5c967e0953a900786178f9": TokenInfo(
        currency=CurrencyInfo(symbol="BAZT", name="Baz Token"), scaling=Decimal("1e-18")
    ),
    "0xb0280743b44bf7db4b6be482b2ba7b75e5da096c": TokenInfo(
        currency=CurrencyInfo(symbol="TNS", name="Transcodium"), scaling=Decimal("1e-18")
    ),
    "0xb0514a5b4aa58ac6e954f537598dd42a71916581": TokenInfo(
        currency=CurrencyInfo(symbol="HUM", name="HUMToken"), scaling=Decimal("1e-18")
    ),
    "0xb052f8a33d8bb068414eade06af6955199f9f010": TokenInfo(
        currency=CurrencyInfo(symbol="ECOREAL", name="Ecoreal Estate"), scaling=Decimal("1e-18")
    ),
    "0xb056c38f6b7dc4064367403e26424cd2c60655e1": TokenInfo(
        currency=CurrencyInfo(symbol="CEEK", name="CEEK Smart VR Token"), scaling=Decimal("1e-18")
    ),
    "0xb05af453011d7ad68a92b0065ffd9d1277ed2741": TokenInfo(
        currency=CurrencyInfo(symbol="TEAM", name="Team Finance"), scaling=Decimal("1e-18")
    ),
    "0xb07ec2c28834b889b1ce527ca0f19364cd38935c": TokenInfo(
        currency=CurrencyInfo(symbol="CARD (OLD)", name="Cardstack Token"), scaling=Decimal("1e-18")
    ),
    "0xb0866289e870d2efc282406cf4123df6e5bcb652": TokenInfo(
        currency=CurrencyInfo(symbol="NFC", name="NoFakeCoin"), scaling=Decimal("1e-18")
    ),
    "0xb09ad98524780228d2df4f34aa665d9dbb9999e4": TokenInfo(
        currency=CurrencyInfo(symbol="TRAD", name="Tradcoin"), scaling=Decimal("1e-18")
    ),
    "0xb09fb1961d5a222e934f97e1f6d0f003ac7f883a": TokenInfo(
        currency=CurrencyInfo(symbol="ALLBIH", name="ALLBI Cash"), scaling=Decimal("1e-18")
    ),
    "0xb0a181a1154d622ddec62524ab6469e62f84031a": TokenInfo(
        currency=CurrencyInfo(symbol="DTC", name="Data Transaction"), scaling=Decimal("1e-8")
    ),
    "0xb0a66227b50810df87ce4b152920d22a716b9b1d": TokenInfo(
        currency=CurrencyInfo(symbol="IEI", name="inheritance"), scaling=Decimal("1e-18")
    ),
    "0xb0b1685f55843d03739c7d9b0a230f1b7dcf03d5": TokenInfo(
        currency=CurrencyInfo(symbol="LYN", name="Lynchpin Token"), scaling=Decimal("1e-18")
    ),
    "0xb0bfb1e2f72511cf8b4d004852e2054d7b9a76e1": TokenInfo(
        currency=CurrencyInfo(symbol="MIXS", name="Streamix"), scaling=Decimal("1e-18")
    ),
    "0xb0c7a3ba49c7a6eaba6cd4a96c55a1391070ac9a": TokenInfo(
        currency=CurrencyInfo(symbol="MAGIC", name="Magic"), scaling=Decimal("1e-18")
    ),
    "0xb0ca787f8cf38f077e8201b05378da230a8b462f": TokenInfo(
        currency=CurrencyInfo(symbol="BHTX", name="BHTX Token"), scaling=Decimal("1e-18")
    ),
    "0xb0cc5610e590eb7215bf4d69eca2ca26b6a9bc87": TokenInfo(
        currency=CurrencyInfo(symbol="SCUDO", name="ScudoCash"), scaling=Decimal("1e-18")
    ),
    "0xb0d761755efc1a7c45391815e0057b9598ddae18": TokenInfo(
        currency=CurrencyInfo(symbol="DOGETHER", name="Dogethereum Token"), scaling=Decimal("1e-18")
    ),
    "0xb0d926c1bc3d78064f3e1075d5bd9a24f35ae6c5": TokenInfo(
        currency=CurrencyInfo(symbol="ARX", name="Assistive Reality ARX"), scaling=Decimal("1e-18")
    ),
    "0xb0e99627bc29adef1178f16117bf495351e81997": TokenInfo(
        currency=CurrencyInfo(symbol="DXC", name="Dex-Trade Coin"), scaling=Decimal("1e-18")
    ),
    "0xb0f14f66cae71164d89e8a0cf0875ef2c32fb660": TokenInfo(
        currency=CurrencyInfo(symbol="CTAG", name="CTAGtoken"), scaling=Decimal("1e-8")
    ),
    "0xb110ec7b1dcb8fab8dedbf28f53bc63ea5bedd84": TokenInfo(
        currency=CurrencyInfo(symbol="XID", name="Sphere Identity"), scaling=Decimal("1e-8")
    ),
    "0xb1191f691a355b43542bea9b8847bc73e7abb137": TokenInfo(
        currency=CurrencyInfo(symbol="KIRO", name="Kirobo"), scaling=Decimal("1e-18")
    ),
    "0xb119ce94d098c18fe380904c24e358bd887f00be": TokenInfo(
        currency=CurrencyInfo(symbol="MACH", name="MACH Project"), scaling=Decimal("1e-18")
    ),
    "0xb13de094cc5cee6c4cc0a3737bf0290166d9ca5d": TokenInfo(
        currency=CurrencyInfo(symbol="GMAT", name="GoWithMi"), scaling=Decimal("1e-18")
    ),
    "0xb15a0becfb3b7da042f969a8e401c2ce8b8679d0": TokenInfo(
        currency=CurrencyInfo(symbol="CITA", name="CitaBit Token"), scaling=Decimal("1e-8")
    ),
    "0xb15ae165000c8d7b69d2a82e425e110668c73ad5": TokenInfo(
        currency=CurrencyInfo(symbol="LBD", name="LinkBased"), scaling=Decimal("1e-9")
    ),
    "0xb16d3ed603d62b125c6bd45519eda40829549489": TokenInfo(
        currency=CurrencyInfo(symbol="ISR", name="Insureum"), scaling=Decimal("1e-18")
    ),
    "0xb17548c7b510427baac4e267bea62e800b247173": TokenInfo(
        currency=CurrencyInfo(symbol="SMT", name="Swarm Markets"), scaling=Decimal("1e-18")
    ),
    "0xb17bfa6da55cdafcd1dbc2023cdd0bc821b0677d": TokenInfo(
        currency=CurrencyInfo(symbol="GWPH.CX", name="GW Pharmaceuticals PLC"), scaling=Decimal("1e-8")
    ),
    "0xb17c88bda07d28b3838e0c1de6a30eafbcf52d85": TokenInfo(
        currency=CurrencyInfo(symbol="SHFT", name="Shyft Network"), scaling=Decimal("1e-18")
    ),
    "0xb17df9a3b09583a9bdcf757d6367171476d4d8a3": TokenInfo(
        currency=CurrencyInfo(symbol="MVC", name="Maverick Chain"), scaling=Decimal("1e-18")
    ),
    "0xb1a219e35ac1aab0ea8f7dae92b06142c1bff542": TokenInfo(
        currency=CurrencyInfo(symbol="BPK", name="Bitpacket"), scaling=Decimal("1e-18")
    ),
    "0xb1c1cb8c7c1992dba24e628bf7d38e71dad46aeb": TokenInfo(
        currency=CurrencyInfo(symbol="CLB", name="Cloudbric"), scaling=Decimal("1e-18")
    ),
    "0xb1ca7e6714263a64659a3a89e1c313af30fd660a": TokenInfo(
        currency=CurrencyInfo(symbol="ETHMOONX", name="ETH Moonshot X Yield Set"), scaling=Decimal("1e-18")
    ),
    "0xb1cfb2421f6f12ebda4f9b8d0336518c82e63b2c": TokenInfo(
        currency=CurrencyInfo(symbol="VOC", name="Vocal Chain"), scaling=Decimal("1e-8")
    ),
    "0xb1d22dffb6c9bf70544116b3ce784454cf383577": TokenInfo(
        currency=CurrencyInfo(symbol="LDEX", name="LogicDEX"), scaling=Decimal("1e-18")
    ),
    "0xb1dc9124c395c1e97773ab855d66e879f053a289": TokenInfo(
        currency=CurrencyInfo(symbol="YAX", name="yAxis"), scaling=Decimal("1e-18")
    ),
    "0xb1e9157c2fdcc5a856c8da8b2d89b6c32b3c1229": TokenInfo(
        currency=CurrencyInfo(symbol="ZEFU", name="Zenfuse"), scaling=Decimal("1e-18")
    ),
    "0xb1ec548f296270bc96b8a1b3b3c8f3f04b494215": TokenInfo(
        currency=CurrencyInfo(symbol="FORS", name="Foresight"), scaling=Decimal("1e-18")
    ),
    "0xb1eef147028e9f480dbc5ccaa3277d417d1b85f0": TokenInfo(
        currency=CurrencyInfo(symbol="Seele", name="SeeleToken"), scaling=Decimal("1e-18")
    ),
    "0xb1f2b122139dacd2ad29840e92cbc38716568994": TokenInfo(
        currency=CurrencyInfo(symbol="LBRTY", name="LIBERTY Token"), scaling=Decimal("1e-18")
    ),
    "0xb1f66997a5760428d3a87d68b90bfe0ae64121cc": TokenInfo(
        currency=CurrencyInfo(symbol="LUA", name="LuaSwap"), scaling=Decimal("1e-18")
    ),
    "0xb1f871ae9462f1b2c6826e88a7827e76f86751d4": TokenInfo(
        currency=CurrencyInfo(symbol="GNY", name="GNY"), scaling=Decimal("1e-18")
    ),
    "0xb20043f149817bff5322f1b928e89abfc65a9925": TokenInfo(
        currency=CurrencyInfo(symbol="EXRT", name="EXRT Network"), scaling=Decimal("1e-8")
    ),
    "0xb2135ab9695a7678dd590b1a996cb0f37bcb0718": TokenInfo(
        currency=CurrencyInfo(symbol="SGN", name="Signals"), scaling=Decimal("1e-9")
    ),
    "0xb22083ba68ebe04a5306625d01f25ef17475cb1b": TokenInfo(
        currency=CurrencyInfo(symbol="TER.CX", name="Teradyne"), scaling=Decimal("1e-8")
    ),
    "0xb2279b6769cfba691416f00609b16244c0cf4b20": TokenInfo(
        currency=CurrencyInfo(symbol="WAIF", name="Waifu Token"), scaling=Decimal("1e-18")
    ),
    "0xb22be3c9fef880ee58155cd402b67ce6d7b45504": TokenInfo(
        currency=CurrencyInfo(symbol="DXG", name="DexAge"), scaling=Decimal("1e-18")
    ),
    "0xb22c2786a549b008517b67625f5296e8faf9589e": TokenInfo(
        currency=CurrencyInfo(symbol="BRP", name="Rental Processor Token"), scaling=Decimal("1e-18")
    ),
    "0xb23be73573bc7e03db6e5dfc62405368716d28a8": TokenInfo(
        currency=CurrencyInfo(symbol="ONEK", name="oneK"), scaling=Decimal("1e-18")
    ),
    "0xb24754be79281553dc1adc160ddf5cd9b74361a4": TokenInfo(
        currency=CurrencyInfo(symbol="XRL", name="Rialto"), scaling=Decimal("1e-9")
    ),
    "0xb2617246d0c6c0087f18703d576831899ca94f01": TokenInfo(
        currency=CurrencyInfo(symbol="ZIG", name="Zignaly"), scaling=Decimal("1e-18")
    ),
    "0xb26631c6dda06ad89b93c71400d25692de89c068": TokenInfo(
        currency=CurrencyInfo(symbol="MINDS", name="Minds"), scaling=Decimal("1e-18")
    ),
    "0xb26c4b3ca601136daf98593feaeff9e0ca702a8d": TokenInfo(
        currency=CurrencyInfo(symbol="ALD", name="Aladdin DAO"), scaling=Decimal("1e-18")
    ),
    "0xb29663aa4e2e81e425294193616c1b102b70a158": TokenInfo(
        currency=CurrencyInfo(symbol="LDN", name="Ludena Protocol"), scaling=Decimal("1e-18")
    ),
    "0xb2a01ad9738450f082e5238e43b17fe80781faae": TokenInfo(
        currency=CurrencyInfo(symbol="FDT", name="Food Token"), scaling=Decimal("1e-18")
    ),
    "0xb2b9335791346e94245dcd316a9c9ed486e6dd7f": TokenInfo(
        currency=CurrencyInfo(symbol="PIPT", name="Baby Power Index Pool Token"), scaling=Decimal("1e-18")
    ),
    "0xb2bfeb70b903f1baac7f2ba2c62934c7e5b974c4": TokenInfo(
        currency=CurrencyInfo(symbol="BKB", name="BetKing Bankroll Token"), scaling=Decimal("1e-8")
    ),
    "0xb2c19ba4d5246d4c587a62f0dfe9f78083568455": TokenInfo(
        currency=CurrencyInfo(symbol="CMDX", name="CMDX"), scaling=Decimal("1e-18")
    ),
    "0xb2cf3a438acf46275839a38db7594065f64151d3": TokenInfo(
        currency=CurrencyInfo(symbol="WRLD", name="TheWorldsAMine"), scaling=Decimal("1e-18")
    ),
    "0xb2e260f12406c401874ecc960893c0f74cd6afcd": TokenInfo(
        currency=CurrencyInfo(symbol="BUT", name="BitUP Token"), scaling=Decimal("1e-18")
    ),
    "0xb2f7eb1f2c37645be61d73953035360e768d81e6": TokenInfo(
        currency=CurrencyInfo(symbol="COB", name="Cobinhood"), scaling=Decimal("1e-18")
    ),
    "0xb2fdd60ad80ca7ba89b9bab3b5336c2601c020b4": TokenInfo(
        currency=CurrencyInfo(symbol="YUSD-OCT20", name="yUSD Synthetic Token Expiring 1 October 2020"),
        scaling=Decimal("1e-18"),
    ),
    "0xb3104b4b9da82025e8b9f8fb28b3553ce2f67069": TokenInfo(
        currency=CurrencyInfo(symbol="BIX", name="BIX Token"), scaling=Decimal("1e-18")
    ),
    "0xb31c219959e06f9afbeb36b388a4bad13e802725": TokenInfo(
        currency=CurrencyInfo(symbol="ONOT", name="ONO"), scaling=Decimal("1e-18")
    ),
    "0xb3203db25a01fa7950a860b42b899ad7da52ddd6": TokenInfo(
        currency=CurrencyInfo(symbol="PLX", name="PlexCoin"), scaling=Decimal("1e-8")
    ),
    "0xb3299d4bab93bf04d5b11bc49cd6dfad1f77d23f": TokenInfo(
        currency=CurrencyInfo(symbol="ADABEAR", name="3X Short Cardano Token"), scaling=Decimal("1e-18")
    ),
    "0xb32c960c46f28059c2b5f1c3ecc2b9dd77ab0aa0": TokenInfo(
        currency=CurrencyInfo(symbol="INTBTC", name="Intelligent BTC Set II"), scaling=Decimal("1e-18")
    ),
    "0xb3319f5d18bc0d84dd1b4825dcde5d5f7266d407": TokenInfo(
        currency=CurrencyInfo(symbol="CZRX", name="c0x"), scaling=Decimal("1e-8")
    ),
    "0xb33ad2acedea7d698b987e0d8195c4df3f6629e8": TokenInfo(
        currency=CurrencyInfo(symbol="FCC", name="FiveColorsCoin"), scaling=Decimal("1e-18")
    ),
    "0xb348cb0638b2399ae598b5575d5c12e0f15d3690": TokenInfo(
        currency=CurrencyInfo(symbol="ABDX", name="allbandex"), scaling=Decimal("1e-18")
    ),
    "0xb3616550abc8af79c7a5902def9efa3bc9a95200": TokenInfo(
        currency=CurrencyInfo(symbol="TLX", name="Telex"), scaling=Decimal("1e-8")
    ),
    "0xb363a3c584b1f379c79fbf09df015da5529d4dac": TokenInfo(
        currency=CurrencyInfo(symbol="TELE", name="Miracle Tele"), scaling=Decimal("1e-18")
    ),
    "0xb37a769b37224449d92aac57de379e1267cd3b00": TokenInfo(
        currency=CurrencyInfo(symbol="COVA", name="Cova Unity"), scaling=Decimal("1e-18")
    ),
    "0xb38018c51987dc57a815ab21f5dd94004c259686": TokenInfo(
        currency=CurrencyInfo(symbol="SILS", name="Silisius"), scaling=Decimal("1e-18")
    ),
    "0xb38f206615325306dddeb0794a6482486b6b78b8": TokenInfo(
        currency=CurrencyInfo(symbol="EOSHEDGE", name="1X Short EOS Token"), scaling=Decimal("1e-18")
    ),
    "0xb3a1770c1cd53947c3ff8809bd1150ea4c45ac1d": TokenInfo(
        currency=CurrencyInfo(symbol="CNCC", name="Coin Node Chain"), scaling=Decimal("1e-18")
    ),
    "0xb3aae68d195138cb1faed4d8c905b8113ea33049": TokenInfo(
        currency=CurrencyInfo(symbol="PPN", name="PiedPiperNetwork"), scaling=Decimal("1e-0")
    ),
    "0xb3bace433288645114fe8e8aa91f87659cbf665b": TokenInfo(
        currency=CurrencyInfo(symbol="WPX", name="Wallet Plus X"), scaling=Decimal("1e-18")
    ),
    "0xb3bd49e28f8f832b8d1e246106991e546c323502": TokenInfo(
        currency=CurrencyInfo(symbol="GMT", name="Mercury Protocol"), scaling=Decimal("1e-18")
    ),
    "0xb3dd5dce850dca7519e74a943568b69f958df52c": TokenInfo(
        currency=CurrencyInfo(symbol="UENC", name="UniversalEnergyChain"), scaling=Decimal("1e-18")
    ),
    "0xb3e210b3982ae8f48defa3d440f6c92afa104209": TokenInfo(
        currency=CurrencyInfo(symbol="CADG", name="Canadian Dollar General Dynamics"), scaling=Decimal("1e-18")
    ),
    "0xb3e2cb7cccfe139f8ff84013823bf22da6b6390a": TokenInfo(
        currency=CurrencyInfo(symbol="ICNQ", name="Iconic Token"), scaling=Decimal("1e-18")
    ),
    "0xb3f83a3be59e71876659c5cecc6a3c4d690d258e": TokenInfo(
        currency=CurrencyInfo(symbol="ZELDA SUMMER NUTS CASH", name="Zelda Summer Nuts Cash"), scaling=Decimal("1e-18")
    ),
    "0xb4058411967d5046f3510943103805be61f0600e": TokenInfo(
        currency=CurrencyInfo(symbol="STONK", name="Stonk"), scaling=Decimal("1e-18")
    ),
    "0xb414f8ec2d14c64f37b1559cbe43746284514596": TokenInfo(
        currency=CurrencyInfo(symbol="FTH", name="FITCASH"), scaling=Decimal("1e-18")
    ),
    "0xb41f09a973a85c7f497c10b00a939de667b55a78": TokenInfo(
        currency=CurrencyInfo(symbol="KNOW", name="KNOW"), scaling=Decimal("1e-10")
    ),
    "0xb422e605fbd765b80d2c4b5d8196c2f94144438b": TokenInfo(
        currency=CurrencyInfo(symbol="LTCBEAR", name="3X Short Litecoin Token"), scaling=Decimal("1e-18")
    ),
    "0xb4272071ecadd69d933adcd19ca99fe80664fc08": TokenInfo(
        currency=CurrencyInfo(symbol="XCHF", name="CryptoFranc"), scaling=Decimal("1e-18")
    ),
    "0xb4371da53140417cbb3362055374b10d97e420bb": TokenInfo(
        currency=CurrencyInfo(symbol="SWTH", name="Switcheo"), scaling=Decimal("1e-8")
    ),
    "0xb444208cb0516c150178fcf9a52604bc04a1acea": TokenInfo(
        currency=CurrencyInfo(symbol="GRMD", name="GreenMed"), scaling=Decimal("1e-18")
    ),
    "0xb45a50545beeab73f38f31e5973768c421805e5e": TokenInfo(
        currency=CurrencyInfo(symbol="TKR", name="CryptoInsight"), scaling=Decimal("1e-18")
    ),
    "0xb45d7bc4cebcab98ad09babdf8c818b2292b672c": TokenInfo(
        currency=CurrencyInfo(symbol="HODL", name="HODLCoin"), scaling=Decimal("1e-18")
    ),
    "0xb472c71365ef9ed14226bb0aa4c9a3fa45ece510": TokenInfo(
        currency=CurrencyInfo(symbol="STISH", name="Stish"), scaling=Decimal("1e-4")
    ),
    "0xb48e0f69e6a3064f5498d495f77ad83e0874ab28": TokenInfo(
        currency=CurrencyInfo(symbol="CXN", name="CXN Network"), scaling=Decimal("1e-18")
    ),
    "0xb49c61b2da035bf198815a0d43f108530a834cce": TokenInfo(
        currency=CurrencyInfo(symbol="IOTU", name="IOTU"), scaling=Decimal("1e-18")
    ),
    "0xb49fa25978abf9a248b8212ab4b87277682301c0": TokenInfo(
        currency=CurrencyInfo(symbol="SOFI", name="RAI Finance"), scaling=Decimal("1e-18")
    ),
    "0xb4a3b0faf0ab53df58001804dda5bfc6a3d59008": TokenInfo(
        currency=CurrencyInfo(symbol="SPA", name="Sperax"), scaling=Decimal("1e-18")
    ),
    "0xb4a677b0e363c3815d46326954a4e4d2b1ace357": TokenInfo(
        currency=CurrencyInfo(symbol="THE", name="THENODE"), scaling=Decimal("1e-18")
    ),
    "0xb4ae194a0dcf1b4080b164c1d775ee06e0817305": TokenInfo(
        currency=CurrencyInfo(symbol="SSJ", name="Super Saiya-jin"), scaling=Decimal("1e-18")
    ),
    "0xb4b1d2c217ec0776584ce08d3dd98f90ededa44b": TokenInfo(
        currency=CurrencyInfo(symbol="CO2", name="Climatecoin"), scaling=Decimal("1e-18")
    ),
    "0xb4bebd34f6daafd808f73de0d10235a92fbb6c3d": TokenInfo(
        currency=CurrencyInfo(symbol="YETI", name="Yearn Ecosystem Token Index"), scaling=Decimal("1e-18")
    ),
    "0xb4c9abc8a74bd2e0e0b7ac5ece30792e65d86c59": TokenInfo(
        currency=CurrencyInfo(symbol="LTG", name="LiteGold"), scaling=Decimal("1e-8")
    ),
    "0xb4d0fdfc8497aef97d3c2892ae682ee06064a2bc": TokenInfo(
        currency=CurrencyInfo(symbol="FMF", name="Formosa Financial"), scaling=Decimal("1e-18")
    ),
    "0xb4d930279552397bba2ee473229f89ec245bc365": TokenInfo(
        currency=CurrencyInfo(symbol="MAHA", name="MahaDAO"), scaling=Decimal("1e-18")
    ),
    "0xb4ea189499c7722b39cba00443cd9d0e600a8670": TokenInfo(
        currency=CurrencyInfo(symbol="LNOT", name="Livenodes Token"), scaling=Decimal("1e-18")
    ),
    "0xb4efd85c19999d84251304bda99e90b92300bd93": TokenInfo(
        currency=CurrencyInfo(symbol="RPL", name="Rocket Pool"), scaling=Decimal("1e-18")
    ),
    "0xb4fbed161bebcb37afb1cb4a6f7ca18b977ccb25": TokenInfo(
        currency=CurrencyInfo(symbol="DOGES", name="Dogeswap"), scaling=Decimal("1e-18")
    ),
    "0xb526fd41360c98929006f3bdcbd16d55de4b0069": TokenInfo(
        currency=CurrencyInfo(symbol="THIRM", name="Thirm Protocol Old"), scaling=Decimal("1e-18")
    ),
    "0xb52fc0f17df38ad76f290467aab57cabaeeada14": TokenInfo(
        currency=CurrencyInfo(symbol="VGTN", name="VideoGamesToken"), scaling=Decimal("1e-18")
    ),
    "0xb53a96bcbdd9cf78dff20bab6c2be7baec8f00f8": TokenInfo(
        currency=CurrencyInfo(symbol="eGAS", name="ETHGAS"), scaling=Decimal("1e-8")
    ),
    "0xb53e08b97724126bda6d237b94f766c0b81c90fe": TokenInfo(
        currency=CurrencyInfo(symbol="PIXBY", name="PIXBY"), scaling=Decimal("1e-18")
    ),
    "0xb551d08d2189ef67b4788be2c35c0743693625ca": TokenInfo(
        currency=CurrencyInfo(symbol="ATO", name="EAutocoin"), scaling=Decimal("1e-18")
    ),
    "0xb563300a3bac79fc09b93b6f84ce0d4465a2ac27": TokenInfo(
        currency=CurrencyInfo(symbol="REDC", name="RedCab"), scaling=Decimal("1e-18")
    ),
    "0xb56739d48429d272881597090e5680409271bc24": TokenInfo(
        currency=CurrencyInfo(symbol="LGD", name="Lab Grown Diamond"), scaling=Decimal("1e-18")
    ),
    "0xb59490ab09a0f526cc7305822ac65f2ab12f9723": TokenInfo(
        currency=CurrencyInfo(symbol="LIT", name="Litentry"), scaling=Decimal("1e-18")
    ),
    "0xb5a4ac5b04e777230ba3381195eff6a60c3934f2": TokenInfo(
        currency=CurrencyInfo(symbol="SURE", name="inSure"), scaling=Decimal("1e-18")
    ),
    "0xb5a52519426ec6d88784cc80e621062498306734": TokenInfo(
        currency=CurrencyInfo(symbol="CPS", name="Cash Per Scan"), scaling=Decimal("1e-18")
    ),
    "0xb5a5f22694352c15b00323844ad545abb2b11028": TokenInfo(
        currency=CurrencyInfo(symbol="ICX", name="ICX"), scaling=Decimal("1e-18")
    ),
    "0xb5a73f5fc8bbdbce59bfd01ca8d35062e0dad801": TokenInfo(
        currency=CurrencyInfo(symbol="PERL", name="Perlin"), scaling=Decimal("1e-9")
    ),
    "0xb5b8f5616fe42d5ceca3e87f3fddbdd8f496d760": TokenInfo(
        currency=CurrencyInfo(symbol="ZPR", name="ZPER"), scaling=Decimal("1e-18")
    ),
    "0xb5bb48567bfd0bfe9e4b08ef8b7f91556cc2a112": TokenInfo(
        currency=CurrencyInfo(symbol="BCASH", name="BankCoin BCash"), scaling=Decimal("1e-18")
    ),
    "0xb5c33f965c8899d255c34cdd2a3efa8abcbb3dea": TokenInfo(
        currency=CurrencyInfo(symbol="KPR", name="KPR Coin"), scaling=Decimal("1e-18")
    ),
    "0xb5ca46cf1da09248126682a7bd72401fd7a6b151": TokenInfo(
        currency=CurrencyInfo(symbol="VOCO", name="Provoco"), scaling=Decimal("1e-18")
    ),
    "0xb5ceab8559742713c9e3306e72b69a429ebf166b": TokenInfo(
        currency=CurrencyInfo(symbol="BTE", name="Bit Eternity"), scaling=Decimal("1e-18")
    ),
    "0xb5dbc6d3cf380079df3b27135664b6bcf45d1869": TokenInfo(
        currency=CurrencyInfo(symbol="OMX", name="Project SHIVOM"), scaling=Decimal("1e-8")
    ),
    "0xb5fe099475d3030dde498c3bb6f3854f762a48ad": TokenInfo(
        currency=CurrencyInfo(symbol="FNK", name="FNK"), scaling=Decimal("1e-18")
    ),
    "0xb6098082cc5b21e3cf89e802dd2343455b545c3b": TokenInfo(
        currency=CurrencyInfo(symbol="PWMC", name="Phoenix Wealth Management Coin"), scaling=Decimal("1e-8")
    ),
    "0xb60fde5d798236fbf1e2697b2a0645380921fccf": TokenInfo(
        currency=CurrencyInfo(symbol="STONK", name="STONK"), scaling=Decimal("1e-18")
    ),
    "0xb62132e35a6c13ee1ee0f84dc5d40bad8d815206": TokenInfo(
        currency=CurrencyInfo(symbol="NEXO", name="NEXO"), scaling=Decimal("1e-18")
    ),
    "0xb621bb8064a1b2b2d6c2fd4330293f3e7acbc15f": TokenInfo(
        currency=CurrencyInfo(symbol="HTMOON", name="10X Long Huobi Token Token"), scaling=Decimal("1e-18")
    ),
    "0xb627d12f7024c78b1139cbb31348393b3d37774d": TokenInfo(
        currency=CurrencyInfo(symbol="GCC", name="Game Currency Coin"), scaling=Decimal("1e-8")
    ),
    "0xb628919a5456fd746a6b7a9f1003040ca63e6d45": TokenInfo(
        currency=CurrencyInfo(symbol="PP", name="ProducePay Chain"), scaling=Decimal("1e-18")
    ),
    "0xb628bc994e39ce264eca6f6ee1620909816a9f12": TokenInfo(
        currency=CurrencyInfo(symbol="PRPS", name="Purpose"), scaling=Decimal("1e-18")
    ),
    "0xb62d18dea74045e822352ce4b3ee77319dc5ff2f": TokenInfo(
        currency=CurrencyInfo(symbol="EVC", name="EventChain"), scaling=Decimal("1e-18")
    ),
    "0xb63b606ac810a52cca15e44bb630fd42d8d1d83d": TokenInfo(
        currency=CurrencyInfo(symbol="MCO", name="MCO"), scaling=Decimal("1e-8")
    ),
    "0xb63ffe88c2903080ccf9ab14efa56a11e3e01273": TokenInfo(
        currency=CurrencyInfo(symbol="MBC", name="Mobiicoin"), scaling=Decimal("1e-18")
    ),
    "0xb647a1d7633c6c4d434e22ee9756b36f2b219525": TokenInfo(
        currency=CurrencyInfo(symbol="ETH20MACOAPY", name="ETH 20 MA Crossover Yield Set II"), scaling=Decimal("1e-18")
    ),
    "0xb64ef51c888972c908cfacf59b47c1afbc0ab8ac": TokenInfo(
        currency=CurrencyInfo(symbol="STORJ", name="Storj"), scaling=Decimal("1e-8")
    ),
    "0xb67718b98d52318240c52e71a898335da4a28c42": TokenInfo(
        currency=CurrencyInfo(symbol="INNBC", name="Innovative Bioresearch Coin"), scaling=Decimal("1e-6")
    ),
    "0xb67734521eabbe9c773729db73e16cc2dfb20a58": TokenInfo(
        currency=CurrencyInfo(symbol="e₹", name="eRupee"), scaling=Decimal("1e-2")
    ),
    "0xb67b88a25708a35ae7c2d736d398d268ce4f7f83": TokenInfo(
        currency=CurrencyInfo(symbol="EMON", name="Etheremon"), scaling=Decimal("1e-8")
    ),
    "0xb683d83a532e2cb7dfa5275eed3698436371cc9f": TokenInfo(
        currency=CurrencyInfo(symbol="BTU", name="BTU Protocol"), scaling=Decimal("1e-18")
    ),
    "0xb688a7b1472e2427c338b975d77e12389ecf2558": TokenInfo(
        currency=CurrencyInfo(symbol="INBOX", name="INBOX TOKEN"), scaling=Decimal("1e-8")
    ),
    "0xb68db6b3e0dd4213f17cb2bf1039f08f69437b99": TokenInfo(
        currency=CurrencyInfo(symbol="CNX.CX", name="Consol Energy"), scaling=Decimal("1e-8")
    ),
    "0xb693364be3576ec59a1867d23f32362382f762ac": TokenInfo(
        currency=CurrencyInfo(symbol="BDB", name="Decentralized Big Data Business"), scaling=Decimal("1e-5")
    ),
    "0xb6957bf56805faed7f1bae30eaebe918b8baff71": TokenInfo(
        currency=CurrencyInfo(symbol="JLT", name="JILT"), scaling=Decimal("1e-18")
    ),
    "0xb6c3dc857845a713d3531cea5ac546f6767992f4": TokenInfo(
        currency=CurrencyInfo(symbol="ADCO", name="Advertise Coin"), scaling=Decimal("1e-6")
    ),
    "0xb6c4267c4877bb0d6b1685cfd85b0fbe82f105ec": TokenInfo(
        currency=CurrencyInfo(symbol="REL", name="Relevant"), scaling=Decimal("1e-18")
    ),
    "0xb6c65067b2a6fb0bce553fa893602de43a7a7f84": TokenInfo(
        currency=CurrencyInfo(symbol="PCCS", name="PCCS Chain"), scaling=Decimal("1e-8")
    ),
    "0xb6c6920327b33f8eec26786c7462c5f4098d47e3": TokenInfo(
        currency=CurrencyInfo(symbol="MINTY", name="Minty Art"), scaling=Decimal("1e-18")
    ),
    "0xb6ca7399b4f9ca56fc27cbff44f4d2e4eef1fc81": TokenInfo(
        currency=CurrencyInfo(symbol="MUSE", name="Muse"), scaling=Decimal("1e-18")
    ),
    "0xb6ed7644c69416d67b522e20bc294a9a9b405b31": TokenInfo(
        currency=CurrencyInfo(symbol="0XBTC", name="0xBitcoin"), scaling=Decimal("1e-8")
    ),
    "0xb6ee603933e024d8d53dde3faa0bf98fe2a3d6f1": TokenInfo(
        currency=CurrencyInfo(symbol="DFT", name="DeFiat"), scaling=Decimal("1e-18")
    ),
    "0xb6ee9668771a79be7967ee29a63d4184f8097143": TokenInfo(
        currency=CurrencyInfo(symbol="CXO", name="CargoX"), scaling=Decimal("1e-18")
    ),
    "0xb6f43025b29196af2dddd69b0a58afba079cd600": TokenInfo(
        currency=CurrencyInfo(symbol="IIC", name="Intelligent Investment Chain"), scaling=Decimal("1e-18")
    ),
    "0xb6ff96b8a8d214544ca0dbc9b33f7ad6503efd32": TokenInfo(
        currency=CurrencyInfo(symbol="SYNC", name="Sync Network"), scaling=Decimal("1e-18")
    ),
    "0xb705268213d593b8fd88d3fdeff93aff5cbdcfae": TokenInfo(
        currency=CurrencyInfo(symbol="IDEX", name="IDEX"), scaling=Decimal("1e-18")
    ),
    "0xb70835d7822ebb9426b56543e391846c107bd32c": TokenInfo(
        currency=CurrencyInfo(symbol="GTC", name="Game"), scaling=Decimal("1e-18")
    ),
    "0xb72c794effb775197287d767ca80c22ae9094cb5": TokenInfo(
        currency=CurrencyInfo(symbol="SCDS", name="Shrine Cloud Storage Network"), scaling=Decimal("1e-18")
    ),
    "0xb73e314501ec4dc2c7c7351514458b1c139df98a": TokenInfo(
        currency=CurrencyInfo(symbol="SPY", name="Super Pay"), scaling=Decimal("1e-18")
    ),
    "0xb753428af26e81097e7fd17f40c88aaa3e04902c": TokenInfo(
        currency=CurrencyInfo(symbol="SFI", name="saffron.finance"), scaling=Decimal("1e-18")
    ),
    "0xb763628c6bde4266cd4232a0cd91c1523aaa077c": TokenInfo(
        currency=CurrencyInfo(symbol="VIR", name="VirtualToken"), scaling=Decimal("1e-18")
    ),
    "0xb787d4eac8899730bb8c57fc3c998c49c5244ec0": TokenInfo(
        currency=CurrencyInfo(symbol="CPEX", name="CoinPulseToken"), scaling=Decimal("1e-8")
    ),
    "0xb78b3320493a4efaa1028130c5ba26f0b6085ef8": TokenInfo(
        currency=CurrencyInfo(symbol="DRC", name="Dracula Token"), scaling=Decimal("1e-18")
    ),
    "0xb7ba8461664de526a3ae44189727dfc768625902": TokenInfo(
        currency=CurrencyInfo(symbol="YMPL", name="YMPL"), scaling=Decimal("1e-9")
    ),
    "0xb7cb1c96db6b22b0d3d9536e0108d062bd488f74": TokenInfo(
        currency=CurrencyInfo(symbol="WTC", name="Waltonchain"), scaling=Decimal("1e-18")
    ),
    "0xb7e77aebbe0687d2eff24cc90c41a3b6ea74bdab": TokenInfo(
        currency=CurrencyInfo(symbol="WIKEN", name="ProjectWITH"), scaling=Decimal("1e-18")
    ),
    "0xb80112e516dabcac6ab4665f1bd650996403156c": TokenInfo(
        currency=CurrencyInfo(symbol="NCOV", name="CoronaCoin"), scaling=Decimal("1e-18")
    ),
    "0xb802b24e0637c2b87d2e8b7784c055bbe921011a": TokenInfo(
        currency=CurrencyInfo(symbol="EMV", name="Ethereum Movie Venture"), scaling=Decimal("1e-2")
    ),
    "0xb8155b9f5676d26a8e90e830e4fea103a3d340fc": TokenInfo(
        currency=CurrencyInfo(symbol="FTXR.CX", name="First Trust Nasdaq Transportation ETF"), scaling=Decimal("1e-8")
    ),
    "0xb81d70802a816b5dacba06d708b5acf19dcd436d": TokenInfo(
        currency=CurrencyInfo(symbol="DEXG", name="Dextoken Governance"), scaling=Decimal("1e-18")
    ),
    "0xb83cd8d39462b761bb0092437d38b37812dd80a2": TokenInfo(
        currency=CurrencyInfo(symbol="GRT", name="Golden Ratio Token"), scaling=Decimal("1e-18")
    ),
    "0xb8796542765747ed7f921ff12faff057b5d624d7": TokenInfo(
        currency=CurrencyInfo(symbol="VOID", name="Void Token"), scaling=Decimal("1e-18")
    ),
    "0xb879da8b24c9b8685de8526cf492e954f165d74b": TokenInfo(
        currency=CurrencyInfo(symbol="MBL", name="MovieBloc"), scaling=Decimal("1e-18")
    ),
    "0xb8a5dba52fe8a0dd737bf15ea5043cea30c7e30b": TokenInfo(
        currency=CurrencyInfo(symbol="AFCASH", name="AFRICUNIA BANK"), scaling=Decimal("1e-18")
    ),
    "0xb8baa0e4287890a5f79863ab62b7f175cecbd433": TokenInfo(
        currency=CurrencyInfo(symbol="SWRV", name="Swerve"), scaling=Decimal("1e-18")
    ),
    "0xb8c77482e45f1f44de1745f52c74426c631bdd52": TokenInfo(
        currency=CurrencyInfo(symbol="BNB", name="BNB"), scaling=Decimal("1e-18")
    ),
    "0xb8db81b84d30e2387de0ff330420a4aaa6688134": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNILINKWETH", name="Aave AMM UniLINKWET"), scaling=Decimal("1e-18")
    ),
    "0xb8ddc930c2bab6c71610a2be639036e829f9c10b": TokenInfo(
        currency=CurrencyInfo(symbol="KWH", name="KwhCoin"), scaling=Decimal("1e-18")
    ),
    "0xb8e103b60a33597136ea9511f46b6dbeb643a3a5": TokenInfo(
        currency=CurrencyInfo(symbol="SBTC", name="SiamBitcoin"), scaling=Decimal("1e-18")
    ),
    "0xb8e3bb633f7276cc17735d86154e0ad5ec9928c0": TokenInfo(
        currency=CurrencyInfo(symbol="VLXPAD", name="VelasPad"), scaling=Decimal("1e-18")
    ),
    "0xb901351bb846fed866554945b22cbdd38a3df1d1": TokenInfo(
        currency=CurrencyInfo(symbol="NIUMC", name="Nium"), scaling=Decimal("1e-18")
    ),
    "0xb90e7eb29f5db631c13838411cc58bb2d1475810": TokenInfo(
        currency=CurrencyInfo(symbol="RNO.CX", name="Renault Par"), scaling=Decimal("1e-8")
    ),
    "0xb91318f35bdb262e9423bc7c7c2a3a93dd93c92c": TokenInfo(
        currency=CurrencyInfo(symbol="NULS", name="Nuls"), scaling=Decimal("1e-18")
    ),
    "0xb91c2a2b953d72f3ef890490669a0a41b0add5f7": TokenInfo(
        currency=CurrencyInfo(symbol="BEFX", name="Belifex"), scaling=Decimal("1e-8")
    ),
    "0xb92f51ce4045212eef8008c2f665da713035267b": TokenInfo(
        currency=CurrencyInfo(symbol="RTL", name="Rentledger"), scaling=Decimal("1e-18")
    ),
    "0xb9440022a095343b440d590fcd2d7a3794bd76c8": TokenInfo(
        currency=CurrencyInfo(symbol="SATURN", name="Saturn DAO Token"), scaling=Decimal("1e-4")
    ),
    "0xb9464ef80880c5aea54c7324c0b8dd6ca6d05a90": TokenInfo(
        currency=CurrencyInfo(symbol="LOCK", name="LOCK Token"), scaling=Decimal("1e-18")
    ),
    "0xb94edb666710430803c7de70ce7cad553153e6e2": TokenInfo(
        currency=CurrencyInfo(symbol="MJ.CX", name="ETFMG Alternative Harvest ETF"), scaling=Decimal("1e-8")
    ),
    "0xb95d3bdf3f2b6b5dd380693acbdeccaa291506d8": TokenInfo(
        currency=CurrencyInfo(symbol="GTR", name="GTR"), scaling=Decimal("1e-18")
    ),
    "0xb97048628db6b661d4c2aa833e95dbe1a905b280": TokenInfo(
        currency=CurrencyInfo(symbol="PAY", name="TenX"), scaling=Decimal("1e-18")
    ),
    "0xb9782532fa7062a6f73df1ce71d75c0e16046ebc": TokenInfo(
        currency=CurrencyInfo(symbol="YFIP", name="YFI Paprika"), scaling=Decimal("1e-8")
    ),
    "0xb97d5cf2864fb0d08b34a484ff48d5492b2324a0": TokenInfo(
        currency=CurrencyInfo(symbol="KLON", name="Klondike Finance v1"), scaling=Decimal("1e-18")
    ),
    "0xb97faf860045483e0c7f08c56acb31333084a988": TokenInfo(
        currency=CurrencyInfo(symbol="VNLA", name="Vanilla Network"), scaling=Decimal("1e-18")
    ),
    "0xb9843e5de0f37d1e22c8075e5814e13565fe7c22": TokenInfo(
        currency=CurrencyInfo(symbol="LBN", name="Lucky Block Network"), scaling=Decimal("1e-18")
    ),
    "0xb9871cb10738eada636432e86fc0cb920dc3de24": TokenInfo(
        currency=CurrencyInfo(symbol="PRIA", name="PRIA"), scaling=Decimal("1e-18")
    ),
    "0xb98d4c97425d9908e66e53a6fdf673acca0be986": TokenInfo(
        currency=CurrencyInfo(symbol="ABT", name="Arcblock"), scaling=Decimal("1e-18")
    ),
    "0xb9961ee048ff6e5f14c56cf4057078403759fbb4": TokenInfo(
        currency=CurrencyInfo(symbol="BTCG", name="Bitcoin GEN"), scaling=Decimal("1e-8")
    ),
    "0xb9bb08ab7e9fa0a1356bd4a39ec0ca267e03b0b3": TokenInfo(
        currency=CurrencyInfo(symbol="PAI", name="PCHAIN"), scaling=Decimal("1e-18")
    ),
    "0xb9c6782f875f92670342dd5e1ff1a57b41588ce2": TokenInfo(
        currency=CurrencyInfo(symbol="GDCT", name="GDCT"), scaling=Decimal("1e-8")
    ),
    "0xb9cb7905981198add8059114b3b7dc7042b52f7b": TokenInfo(
        currency=CurrencyInfo(symbol="TMT", name="Tamy Token"), scaling=Decimal("1e-18")
    ),
    "0xb9d7cb55f463405cdfbe4e90a6d2df01c2b92bf1": TokenInfo(
        currency=CurrencyInfo(symbol="AUNI", name="Aave UNI"), scaling=Decimal("1e-18")
    ),
    "0xb9d99c33ea2d86ec5ec6b8a4dd816ebba64404af": TokenInfo(
        currency=CurrencyInfo(symbol="K21", name="K21"), scaling=Decimal("1e-18")
    ),
    "0xb9e7f8568e08d5659f5d29c4997173d84cdf2607": TokenInfo(
        currency=CurrencyInfo(symbol="SWT", name="Swarm City"), scaling=Decimal("1e-18")
    ),
    "0xb9eefc4b0d472a44be93970254df4f4016569d27": TokenInfo(
        currency=CurrencyInfo(symbol="XDB", name="DigitalBits"), scaling=Decimal("1e-7")
    ),
    "0xb9ef770b6a5e12e45983c5d80545258aa38f3b78": TokenInfo(
        currency=CurrencyInfo(symbol="ZCN", name="0chain"), scaling=Decimal("1e-10")
    ),
    "0xb9ffe0b8ee2d1af94202ffed366520300748a4d8": TokenInfo(
        currency=CurrencyInfo(symbol="ETHBTCEMACO", name="ETH/BTC EMA Ratio Trading Set"), scaling=Decimal("1e-18")
    ),
    "0xba069ee53b8b531f3ab117c92ca09a204c9e6285": TokenInfo(
        currency=CurrencyInfo(symbol="PLG", name="Plug"), scaling=Decimal("1e-18")
    ),
    "0xba100000625a3754423978a60c9317c58a424e3d": TokenInfo(
        currency=CurrencyInfo(symbol="BAL", name="Balancer"), scaling=Decimal("1e-18")
    ),
    "0xba11d00c5f74255f56a5e366f4f77f5a186d7f55": TokenInfo(
        currency=CurrencyInfo(symbol="BAND", name="Band Protocol"), scaling=Decimal("1e-18")
    ),
    "0xba14b245d449965bdbeb630ebe135b569474f5b1": TokenInfo(
        currency=CurrencyInfo(symbol="EVC", name="EvaCash"), scaling=Decimal("1e-6")
    ),
    "0xba2184520a1cc49a6159c57e61e1844e085615b6": TokenInfo(
        currency=CurrencyInfo(symbol="HGT", name="HelloGold"), scaling=Decimal("1e-8")
    ),
    "0xba21ef4c9f433ede00badefcc2754b8e74bd538a": TokenInfo(
        currency=CurrencyInfo(symbol="SWFL", name="Swapfolio"), scaling=Decimal("1e-18")
    ),
    "0xba358b6f5b4c0215650444b8c30d870b55050d2d": TokenInfo(
        currency=CurrencyInfo(symbol="HUB", name="HubToken"), scaling=Decimal("1e-18")
    ),
    "0xba3a79d758f19efe588247388754b8e4d6edda81": TokenInfo(
        currency=CurrencyInfo(symbol="VSF", name="VeriSafe"), scaling=Decimal("1e-18")
    ),
    "0xba4cfe5741b357fa371b506e5db0774abfecf8fc": TokenInfo(
        currency=CurrencyInfo(symbol="VVSP", name="vVSP"), scaling=Decimal("1e-18")
    ),
    "0xba50933c268f567bdc86e1ac131be072c6b0b71a": TokenInfo(
        currency=CurrencyInfo(symbol="ARPA", name="ARPA Chain"), scaling=Decimal("1e-18")
    ),
    "0xba5bde662c17e2adff1075610382b9b691296350": TokenInfo(
        currency=CurrencyInfo(symbol="RARE", name="SuperRare"), scaling=Decimal("1e-18")
    ),
    "0xba5f11b16b155792cf3b2e6880e8706859a8aeb6": TokenInfo(
        currency=CurrencyInfo(symbol="ARN", name="Aeron"), scaling=Decimal("1e-8")
    ),
    "0xba68d28dda9708bc6100ec403cbacbffa1f9b283": TokenInfo(
        currency=CurrencyInfo(symbol="ARNC.CX", name="Arconic"), scaling=Decimal("1e-8")
    ),
    "0xba6db13aeae3607d400ddffd675aa4e88ecc9a69": TokenInfo(
        currency=CurrencyInfo(symbol="SENSO", name="Sensorium"), scaling=Decimal("1e-0")
    ),
    "0xba7234570fcdac6954156c13fb1d167890549cd2": TokenInfo(
        currency=CurrencyInfo(symbol="RNG", name="Royal Never Give Up"), scaling=Decimal("1e-4")
    ),
    "0xba7435a4b4c747e0101780073eeda872a69bdcd4": TokenInfo(
        currency=CurrencyInfo(symbol="AIRDROP", name="Airdrop Token"), scaling=Decimal("1e-18")
    ),
    "0xba745513acebcbb977497c569d4f7d340f2a936b": TokenInfo(
        currency=CurrencyInfo(symbol="MFTU", name="Mainstream For The Underground"), scaling=Decimal("1e-18")
    ),
    "0xba7b2c094c1a4757f9534a37d296a3bed7f544dc": TokenInfo(
        currency=CurrencyInfo(symbol="HLAND", name="HLand Token"), scaling=Decimal("1e-18")
    ),
    "0xba7cdd0953e8f950317dda347a716f162713b226": TokenInfo(
        currency=CurrencyInfo(symbol="MOON", name="10X Long Bitcoin Token"), scaling=Decimal("1e-18")
    ),
    "0xba7dcba2ade319bc772db4df75a76ba00dfb31b0": TokenInfo(
        currency=CurrencyInfo(symbol="A18", name="Apollo18"), scaling=Decimal("1e-18")
    ),
    "0xba8a621b4a54e61c442f5ec623687e2a942225ef": TokenInfo(
        currency=CurrencyInfo(symbol="QUARTZ", name="Sandclock"), scaling=Decimal("1e-18")
    ),
    "0xba8ea15b647f54d9ff849670fcaacf35df21a457": TokenInfo(
        currency=CurrencyInfo(symbol="INTRATIO", name="Intelligent Ratio Set"), scaling=Decimal("1e-18")
    ),
    "0xba90351ac53860eca66fb57ae43640fbb066418c": TokenInfo(
        currency=CurrencyInfo(symbol="XSP", name="SpaikCoin"), scaling=Decimal("1e-18")
    ),
    "0xba9d4199fab4f26efe3551d490e3821486f135ba": TokenInfo(
        currency=CurrencyInfo(symbol="CHSB", name="SwissBorg"), scaling=Decimal("1e-8")
    ),
    "0xbaa103e4aa491602f5afb01267c02fd84d75d55e": TokenInfo(
        currency=CurrencyInfo(symbol="SLCA.CX", name="Us Silica Holdings"), scaling=Decimal("1e-8")
    ),
    "0xbaac2b4491727d78d2b78815144570b9f2fe8899": TokenInfo(
        currency=CurrencyInfo(symbol="DOG", name="The Doge NFT"), scaling=Decimal("1e-18")
    ),
    "0xbab165df9455aa0f2aed1f2565520b91ddadb4c8": TokenInfo(
        currency=CurrencyInfo(symbol="EKT", name="EDUCare"), scaling=Decimal("1e-8")
    ),
    "0xbac6874fff7ac02c06907d0e340af9f1832e7908": TokenInfo(
        currency=CurrencyInfo(symbol="A1", name="A1 Coin"), scaling=Decimal("1e-18")
    ),
    "0xbae235823d7255d9d48635ced4735227244cd583": TokenInfo(
        currency=CurrencyInfo(symbol="STR", name="Staker"), scaling=Decimal("1e-18")
    ),
    "0xbb0e17ef65f82ab018d8edd776e8dd940327b28b": TokenInfo(
        currency=CurrencyInfo(symbol="AXS", name="AXS"), scaling=Decimal("1e-18")
    ),
    "0xbb0ef9e617faddf54b8d16e29046f72b4d3ec77f": TokenInfo(
        currency=CurrencyInfo(symbol="PEP", name="PEP Token"), scaling=Decimal("1e-18")
    ),
    "0xbb1f24c0c1554b9990222f036b0aad6ee4caec29": TokenInfo(
        currency=CurrencyInfo(symbol="SOUL", name="CryptoSoul"), scaling=Decimal("1e-18")
    ),
    "0xbb1fa4fdeb3459733bf67ebc6f893003fa976a82": TokenInfo(
        currency=CurrencyInfo(symbol="XPAT", name="Pangea Arbitration Token (Bitnation)"), scaling=Decimal("1e-18")
    ),
    "0xbb340a2eaf55c5e67a5a05fe5ceed9b9702d76f4": TokenInfo(
        currency=CurrencyInfo(symbol="BOLTT", name="BolttCoin"), scaling=Decimal("1e-8")
    ),
    "0xbb49a51ee5a66ca3a8cbe529379ba44ba67e6771": TokenInfo(
        currency=CurrencyInfo(symbol="CST", name="Cryptosolartech"), scaling=Decimal("1e-18")
    ),
    "0xbb97e381f1d1e94ffa2a5844f6875e6146981009": TokenInfo(
        currency=CurrencyInfo(symbol="WBX", name="WiBX"), scaling=Decimal("1e-18")
    ),
    "0xbb9bc244d798123fde783fcc1c72d3bb8c189413": TokenInfo(
        currency=CurrencyInfo(symbol="TheDAO", name="TheDAO"), scaling=Decimal("1e-16")
    ),
    "0xbbbbbbb5aa847a2003fbc6b5c16df0bd1e725f61": TokenInfo(
        currency=CurrencyInfo(symbol="BPRO", name="B Protocol"), scaling=Decimal("1e-18")
    ),
    "0xbbbbca6a901c926f240b89eacb641d8aec7aeafd": TokenInfo(
        currency=CurrencyInfo(symbol="LRC", name="Loopring"), scaling=Decimal("1e-18")
    ),
    "0xbbc2045d335cb224228f1850b29173d9d7d7b989": TokenInfo(
        currency=CurrencyInfo(symbol="HELP", name="GoHelpFund"), scaling=Decimal("1e-18")
    ),
    "0xbbc2ae13b23d715c30720f079fcd9b4a74093505": TokenInfo(
        currency=CurrencyInfo(symbol="ERN", name="Ethernity Chain"), scaling=Decimal("1e-18")
    ),
    "0xbbc455cb4f1b9e4bfc4b73970d360c8f032efee6": TokenInfo(
        currency=CurrencyInfo(symbol="SLINK", name="sLINK"), scaling=Decimal("1e-18")
    ),
    "0xbbd227e805b90b8fe8f4c01a3f4e48bdae0599af": TokenInfo(
        currency=CurrencyInfo(symbol="PHT", name="Phoneum Token"), scaling=Decimal("1e-2")
    ),
    "0xbbff34e47e559ef680067a6b1c980639eeb64d24": TokenInfo(
        currency=CurrencyInfo(symbol="L2", name="Leverj Gluon"), scaling=Decimal("1e-18")
    ),
    "0xbbff862d906e348e9946bfb2132ecb157da3d4b4": TokenInfo(
        currency=CurrencyInfo(symbol="SS", name="Sharder protocol"), scaling=Decimal("1e-18")
    ),
    "0xbc1234552ebea32b5121190356bba6d3bb225bb5": TokenInfo(
        currency=CurrencyInfo(symbol="BCL", name="BitClave"), scaling=Decimal("1e-18")
    ),
    "0xbc138bd20c98186cc0342c8e380953af0cb48ba8": TokenInfo(
        currency=CurrencyInfo(symbol="CNDL", name="Candle"), scaling=Decimal("1e-18")
    ),
    "0xbc16da9df0a22f01a16bc0620a27e7d6d6488550": TokenInfo(
        currency=CurrencyInfo(symbol="PCT", name="Percent"), scaling=Decimal("1e-18")
    ),
    "0xbc19712feb3a26080ebf6f2f7849b417fdd792ca": TokenInfo(
        currency=CurrencyInfo(symbol="BORING", name="BoringDAO"), scaling=Decimal("1e-18")
    ),
    "0xbc19f228a2637b7b03205ab5753df50f545d667d": TokenInfo(
        currency=CurrencyInfo(symbol="WNS", name="Winners Token"), scaling=Decimal("1e-8")
    ),
    "0xbc34985b4d345aea933d5cac19f3a86bd1fb398f": TokenInfo(
        currency=CurrencyInfo(symbol="ZJLT", name="ZJLT Distributed Factoring Network"), scaling=Decimal("1e-18")
    ),
    "0xbc396689893d065f41bc2c6ecbee5e0085233447": TokenInfo(
        currency=CurrencyInfo(symbol="PERP", name="Perpetual Protocol"), scaling=Decimal("1e-18")
    ),
    "0xbc3a40ecda4fa380f0d5f3201ad85e9126fd2817": TokenInfo(
        currency=CurrencyInfo(symbol="XTI-CX", name="US Crude Oil Spot"), scaling=Decimal("1e-8")
    ),
    "0xbc3ec4e491b835dce394a53e9a9a10ac19564839": TokenInfo(
        currency=CurrencyInfo(symbol="BUGS", name="Starbugs Shards"), scaling=Decimal("1e-18")
    ),
    "0xbc4171f45ef0ef66e76f979df021a34b46dcc81d": TokenInfo(
        currency=CurrencyInfo(symbol="DORA", name="Dora Factory"), scaling=Decimal("1e-18")
    ),
    "0xbc41d05287498dec58129560de6bd1b8d4e3ac1d": TokenInfo(
        currency=CurrencyInfo(symbol="XTZBEAR", name="3X Short Tezos Token"), scaling=Decimal("1e-18")
    ),
    "0xbc46d9961a3932f7d6b64abfdec80c1816c4b835": TokenInfo(
        currency=CurrencyInfo(symbol="LXT", name="LITEX"), scaling=Decimal("1e-18")
    ),
    "0xbc5991ccd8caceba01edc44c2bb9832712c29cab": TokenInfo(
        currency=CurrencyInfo(symbol="UUSDC", name="Unagii USD Coin"), scaling=Decimal("1e-6")
    ),
    "0xbc647aad10114b89564c0a7aabe542bd0cf2c5af": TokenInfo(
        currency=CurrencyInfo(symbol="IONC", name="IONChain"), scaling=Decimal("1e-18")
    ),
    "0xbc6da0fe9ad5f3b0d58160288917aa56653660e9": TokenInfo(
        currency=CurrencyInfo(symbol="ALUSD", name="Alchemix USD"), scaling=Decimal("1e-18")
    ),
    "0xbc7250c8c3eca1dfc1728620af835fca489bfdf3": TokenInfo(
        currency=CurrencyInfo(symbol="GM", name="GM"), scaling=Decimal("1e-9")
    ),
    "0xbc7942054f77b82e8a71ace170e4b00ebae67eb6": TokenInfo(
        currency=CurrencyInfo(symbol="SRNT", name="Serenity"), scaling=Decimal("1e-18")
    ),
    "0xbc7ed0c8cf986ae62337fc8df3b02c6ec87310ed": TokenInfo(
        currency=CurrencyInfo(symbol="XPAY", name="Xpayment"), scaling=Decimal("1e-18")
    ),
    "0xbc86727e770de68b1060c91f6bb6945c73e10388": TokenInfo(
        currency=CurrencyInfo(symbol="XNK", name="Ink Protocol"), scaling=Decimal("1e-18")
    ),
    "0xbc8deee89f1cf4b661514185aa1ab780336c4c4a": TokenInfo(
        currency=CurrencyInfo(symbol="POK", name="Poker.io"), scaling=Decimal("1e-18")
    ),
    "0xbca3c97837a39099ec3082df97e28ce91be14472": TokenInfo(
        currency=CurrencyInfo(symbol="DUST", name="DUST Token"), scaling=Decimal("1e-8")
    ),
    "0xbcc66ed2ab491e9ae7bf8386541fb17421fa9d35": TokenInfo(
        currency=CurrencyInfo(symbol="SKULL", name="Skull"), scaling=Decimal("1e-4")
    ),
    "0xbcca60bb61934080951369a648fb03df4f96263c": TokenInfo(
        currency=CurrencyInfo(symbol="AUSDC", name="Aave USDC"), scaling=Decimal("1e-6")
    ),
    "0xbcd4b7de6fde81025f74426d43165a5b0d790fdd": TokenInfo(
        currency=CurrencyInfo(symbol="SPDR", name="SpiderDAO"), scaling=Decimal("1e-18")
    ),
    "0xbcd8756ea481608ea3dd5a555493305cf0a79640": TokenInfo(
        currency=CurrencyInfo(symbol="PAZZI", name="Paparazzi"), scaling=Decimal("1e-18")
    ),
    "0xbcdfe338d55c061c084d81fd793ded00a27f226d": TokenInfo(
        currency=CurrencyInfo(symbol="DML", name="Decentralized Machine Learning Protocol"), scaling=Decimal("1e-18")
    ),
    "0xbd03bd923c7d51019fd84571d84e4ebcf7213509": TokenInfo(
        currency=CurrencyInfo(symbol="RCKT", name="Rocket"), scaling=Decimal("1e-18")
    ),
    "0xbd0793332e9fb844a52a205a233ef27a5b34b927": TokenInfo(
        currency=CurrencyInfo(symbol="ZB", name="ZB Token"), scaling=Decimal("1e-18")
    ),
    "0xbd10eaccc4004f379b30562835668f3a74433714": TokenInfo(
        currency=CurrencyInfo(symbol="MSG", name="BitMessage"), scaling=Decimal("1e-18")
    ),
    "0xbd168cbf9d3a375b38dc51a202b5e8a4e52069ed": TokenInfo(
        currency=CurrencyInfo(symbol="BWX", name="BlueWhwaleToken"), scaling=Decimal("1e-18")
    ),
    "0xbd2949f67dcdc549c6ebe98696449fa79d988a9f": TokenInfo(
        currency=CurrencyInfo(symbol="EMTRG", name="Meter Governance mapped by Meter.io"), scaling=Decimal("1e-18")
    ),
    "0xbd2f0cd039e0bfcf88901c98c0bfac5ab27566e3": TokenInfo(
        currency=CurrencyInfo(symbol="DSD", name="Dynamic Set Dollar"), scaling=Decimal("1e-18")
    ),
    "0xbd301be09eb78df47019aa833d29edc5d815d838": TokenInfo(
        currency=CurrencyInfo(symbol="YFUEL", name="YFUEL"), scaling=Decimal("1e-18")
    ),
    "0xbd356a39bff2cada8e9248532dd879147221cf76": TokenInfo(
        currency=CurrencyInfo(symbol="WOM", name="WOM Protocol"), scaling=Decimal("1e-18")
    ),
    "0xbd3de9a069648c84d27d74d701c9fa3253098b15": TokenInfo(
        currency=CurrencyInfo(symbol="EQX", name="EQIFi"), scaling=Decimal("1e-18")
    ),
    "0xbd4b60a138b3fce3584ea01f50c0908c18f9677a": TokenInfo(
        currency=CurrencyInfo(symbol="FNTB", name="FinTab"), scaling=Decimal("1e-8")
    ),
    "0xbd4e39acf23c96d68e2ab28337ae6b25441b32c2": TokenInfo(
        currency=CurrencyInfo(symbol="MFR2", name="MaferToken.co"), scaling=Decimal("1e-8")
    ),
    "0xbd5b192fa5af70f1f871e4a155a3be1a43a1d583": TokenInfo(
        currency=CurrencyInfo(symbol="GPS.CX", name="The Gap Inc"), scaling=Decimal("1e-8")
    ),
    "0xbd6467a31899590474ce1e84f70594c53d628e46": TokenInfo(
        currency=CurrencyInfo(symbol="KAI", name="KardiaChain Token"), scaling=Decimal("1e-18")
    ),
    "0xbdab72602e9ad40fc6a6852caf43258113b8f7a5": TokenInfo(
        currency=CurrencyInfo(symbol="SOV", name="Sovryn"), scaling=Decimal("1e-18")
    ),
    "0xbdbb0ee6144544ec814d417b0ad41f16fc8b858e": TokenInfo(
        currency=CurrencyInfo(symbol="KAM", name="BitKAM"), scaling=Decimal("1e-8")
    ),
    "0xbdbc2a5b32f3a5141acd18c39883066e4dab9774": TokenInfo(
        currency=CurrencyInfo(symbol="EMRX", name="Emirex Token"), scaling=Decimal("1e-8")
    ),
    "0xbdc5bac39dbe132b1e030e898ae3830017d7d969": TokenInfo(
        currency=CurrencyInfo(symbol="SNOV", name="Snovian.Space"), scaling=Decimal("1e-18")
    ),
    "0xbdcfbf5c4d91abc0bc9709c7286d00063c0e6f22": TokenInfo(
        currency=CurrencyInfo(symbol="GUESS", name="PeerGuess"), scaling=Decimal("1e-2")
    ),
    "0xbdda280ee7bccc68f3be60a369b6b1eaee02493c": TokenInfo(
        currency=CurrencyInfo(symbol="BITOX", name="Bitox Token"), scaling=Decimal("1e-18")
    ),
    "0xbdeb4b83251fb146687fa19d1c660f99411eefe3": TokenInfo(
        currency=CurrencyInfo(symbol="SVD", name="Savedroid"), scaling=Decimal("1e-18")
    ),
    "0xbded3f7537e75d6c38c036a3a788a549afde12b1": TokenInfo(
        currency=CurrencyInfo(symbol="DCS", name="DCS TOKEN"), scaling=Decimal("1e-8")
    ),
    "0xbdfa65533074b0b23ebc18c7190be79fa74b30c2": TokenInfo(
        currency=CurrencyInfo(symbol="ZDR", name="Zloadr"), scaling=Decimal("1e-18")
    ),
    "0xbe11eeb186e624b8f26a5045575a1340e4054552": TokenInfo(
        currency=CurrencyInfo(symbol="CCC", name="Crush Crypto Core"), scaling=Decimal("1e-18")
    ),
    "0xbe1a001fe942f96eea22ba08783140b9dcc09d28": TokenInfo(
        currency=CurrencyInfo(symbol="BETA", name="Beta Finance"), scaling=Decimal("1e-18")
    ),
    "0xbe30f684d62c9f7883a75a29c162c332c0d98f23": TokenInfo(
        currency=CurrencyInfo(symbol="GHT", name="Global Human Trust"), scaling=Decimal("1e-18")
    ),
    "0xbe3c393fb670f0a29c3f3e660ffb113200e36676": TokenInfo(
        currency=CurrencyInfo(symbol="DANT", name="Digital Antares Dollar"), scaling=Decimal("1e-18")
    ),
    "0xbe428c3867f05dea2a89fc76a102b544eac7f772": TokenInfo(
        currency=CurrencyInfo(symbol="CVT", name="CyberVeinToken"), scaling=Decimal("1e-18")
    ),
    "0xbe5b336ef62d1626940363cf34be079e0ab89f20": TokenInfo(
        currency=CurrencyInfo(symbol="BNC", name="Bnoincoin"), scaling=Decimal("1e-18")
    ),
    "0xbe685c5e06866cfb94a4242e3df8f2fa3e7c2b73": TokenInfo(
        currency=CurrencyInfo(symbol="YFRM", name="Yearn Finance Red Moon"), scaling=Decimal("1e-18")
    ),
    "0xbe68b4645ab798ed4db88192a444898ff4fda5ae": TokenInfo(
        currency=CurrencyInfo(symbol="WON", name="WONCOIN"), scaling=Decimal("1e-8")
    ),
    "0xbe6ac6b50f577205c9d107f37b6e205aa6acc5d4": TokenInfo(
        currency=CurrencyInfo(symbol="UND", name="United Network Distribution"), scaling=Decimal("1e-18")
    ),
    "0xbe893b4c214dbffc17ef1e338fbdb7061ff09237": TokenInfo(
        currency=CurrencyInfo(symbol="MATICBEAR", name="3X Short Matic Token"), scaling=Decimal("1e-18")
    ),
    "0xbe9375c6a420d2eeb258962efb95551a5b722803": TokenInfo(
        currency=CurrencyInfo(symbol="STMX", name="StormX"), scaling=Decimal("1e-18")
    ),
    "0xbe99b09709fc753b09bcf557a992f6605d5997b0": TokenInfo(
        currency=CurrencyInfo(symbol="RLTY", name="SMARTRealty"), scaling=Decimal("1e-8")
    ),
    "0xbea98c05eeae2f3bc8c3565db7551eb738c8ccab": TokenInfo(
        currency=CurrencyInfo(symbol="GYSR", name="Geyser"), scaling=Decimal("1e-18")
    ),
    "0xbea9ba2527f584b9543d1fdf402493bf23ef156f": TokenInfo(
        currency=CurrencyInfo(symbol="LT", name="Lemon Game"), scaling=Decimal("1e-18")
    ),
    "0xbebdab6da046bc49ffbb61fbd7b33157eb270d05": TokenInfo(
        currency=CurrencyInfo(symbol="SHARD", name="Shard"), scaling=Decimal("1e-18")
    ),
    "0xbecaea7aa3629d4b7ddccf3a973bef09ff34d4b6": TokenInfo(
        currency=CurrencyInfo(
            symbol="REALTOKEN-15634-LIBERAL-ST-DETROIT-MI", name="RealToken 15634 Liberal St Detroit MI"
        ),
        scaling=Decimal("1e-18"),
    ),
    "0xbed04d5ba351fb2a93470bee04babb32d7f6817c": TokenInfo(
        currency=CurrencyInfo(symbol="MIDHEDGE", name="1X Short Midcap Index Token"), scaling=Decimal("1e-18")
    ),
    "0xbee6edf5fa7e862ed2ea9b9f42cb0849184aae85": TokenInfo(
        currency=CurrencyInfo(symbol="BKN", name="BlockState Security Token"), scaling=Decimal("1e-0")
    ),
    "0xbeea2890775889c7723e5c0b80527976803b5a99": TokenInfo(
        currency=CurrencyInfo(symbol="AUC", name="Afri Union Coin"), scaling=Decimal("1e-18")
    ),
    "0xbf18f246b9301f231e9561b35a3879769bb46375": TokenInfo(
        currency=CurrencyInfo(symbol="CARE", name="Token Care"), scaling=Decimal("1e-18")
    ),
    "0xbf2179859fc6d5bee9bf9158632dc51678a4100e": TokenInfo(
        currency=CurrencyInfo(symbol="ELF", name="aelf"), scaling=Decimal("1e-18")
    ),
    "0xbf4a29269bf3a5c351c2af3a9c9ed81b07129ce4": TokenInfo(
        currency=CurrencyInfo(symbol="KEN", name="Kencoin"), scaling=Decimal("1e-18")
    ),
    "0xbf4a2ddaa16148a9d0fa2093ffac450adb7cd4aa": TokenInfo(
        currency=CurrencyInfo(symbol="ETHMNY", name="Ethereum Money"), scaling=Decimal("1e-2")
    ),
    "0xbf4cfd7d1edeeea5f6600827411b41a21eb08abd": TokenInfo(
        currency=CurrencyInfo(symbol="CTL", name="Citadel"), scaling=Decimal("1e-2")
    ),
    "0xbf52f2ab39e26e0951d2a02b49b7702abe30406a": TokenInfo(
        currency=CurrencyInfo(symbol="ODE", name="ODEM"), scaling=Decimal("1e-18")
    ),
    "0xbf5496122cf1bb778e0cbe5eab936f2be5fc0940": TokenInfo(
        currency=CurrencyInfo(symbol="FUNDZ", name="FundFantasy"), scaling=Decimal("1e-18")
    ),
    "0xbf70a33a13fbe8d0106df321da0cf654d2e9ab50": TokenInfo(
        currency=CurrencyInfo(symbol="ETHBTCRSI", name="ETH/BTC RSI Ratio Trading Set"), scaling=Decimal("1e-18")
    ),
    "0xbf85479abcf60328cd7224f43ecd71e2f9a282f8": TokenInfo(
        currency=CurrencyInfo(symbol="RESH", name="RESH"), scaling=Decimal("1e-18")
    ),
    "0xbf8be431aa8d8b2f58b6f0727c25a67b41beaaf8": TokenInfo(
        currency=CurrencyInfo(symbol="ELC", name="Elama Coin"), scaling=Decimal("1e-4")
    ),
    "0xbf8d8f1242b95dfbae532af6b0f4463905415cc1": TokenInfo(
        currency=CurrencyInfo(symbol="EDX", name="Edex"), scaling=Decimal("1e-18")
    ),
    "0xbf8fb919a8bbf28e590852aef2d284494ebc0657": TokenInfo(
        currency=CurrencyInfo(symbol="AT", name="ABCC Token"), scaling=Decimal("1e-18")
    ),
    "0xbfbe5332f172d77811bc6c272844f3e54a7b23bb": TokenInfo(
        currency=CurrencyInfo(symbol="WMK", name="Wemark"), scaling=Decimal("1e-18")
    ),
    "0xbfc1502ebc37475b940ced8f036b91018a73c8f6": TokenInfo(
        currency=CurrencyInfo(symbol="BDK", name="Bidesk"), scaling=Decimal("1e-18")
    ),
    "0xbfd16e47a1b6ad4adbe7ab2a1cb624c6c8b1bc3d": TokenInfo(
        currency=CurrencyInfo(symbol="ACO", name="AMPLE! Coin"), scaling=Decimal("1e-18")
    ),
    "0xbfd78aebccf26cb964a7836263143b5ee8072d84": TokenInfo(
        currency=CurrencyInfo(symbol="PERA", name="PAYERA"), scaling=Decimal("1e-8")
    ),
    "0xbfe03707adb75b478add9a01978057803f480e44": TokenInfo(
        currency=CurrencyInfo(symbol="IMT", name="IMSMART Token"), scaling=Decimal("1e-8")
    ),
    "0xbff0e42eec4223fbd12260f47f3348d29876db42": TokenInfo(
        currency=CurrencyInfo(symbol="XTK", name="Xtake"), scaling=Decimal("1e-6")
    ),
    "0xbffe4fdcd397e7942fd7c9f99255e0aa34e4b3fb": TokenInfo(
        currency=CurrencyInfo(symbol="TRM", name="Tranium"), scaling=Decimal("1e-8")
    ),
    "0xc00e94cb662c3520282e6f5717214004a7f26888": TokenInfo(
        currency=CurrencyInfo(symbol="COMP", name="Compound"), scaling=Decimal("1e-18")
    ),
    "0xc011a72400e58ecd99ee497cf89e3775d4bd732f": TokenInfo(
        currency=CurrencyInfo(symbol="SNX", name="Synthetix Network Token"), scaling=Decimal("1e-18")
    ),
    "0xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f": TokenInfo(
        currency=CurrencyInfo(symbol="SNX", name="Synthetix Network Token"), scaling=Decimal("1e-18")
    ),
    "0xc0134b5b924c2fca106efb33c45446c466fbe03e": TokenInfo(
        currency=CurrencyInfo(symbol="ALEPH", name="aleph.im"), scaling=Decimal("1e-18")
    ),
    "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2": TokenInfo(
        currency=CurrencyInfo(symbol="WETH", name="WETH"), scaling=Decimal("1e-18")
    ),
    "0xc05d14442a510de4d3d71a3d316585aa0ce32b50": TokenInfo(
        currency=CurrencyInfo(symbol="LINA", name="LINA"), scaling=Decimal("1e-18")
    ),
    "0xc06aec5191be16b94ffc97b6fc01393527367365": TokenInfo(
        currency=CurrencyInfo(symbol="BTCETH5050", name="BTC ETH Equal Weight Set"), scaling=Decimal("1e-18")
    ),
    "0xc08512927d12348f6620a698105e1baac6ecd911": TokenInfo(
        currency=CurrencyInfo(symbol="GYEN", name="GYEN"), scaling=Decimal("1e-6")
    ),
    "0xc0a25a24cce412e2fb407c08e3785437fee9ad1d": TokenInfo(
        currency=CurrencyInfo(symbol="OFT", name="Orient"), scaling=Decimal("1e-18")
    ),
    "0xc0ba369c8db6eb3924965e5c4fd0b4c1b91e305f": TokenInfo(
        currency=CurrencyInfo(symbol="DUCK", name="DLP Duck Token"), scaling=Decimal("1e-18")
    ),
    "0xc0d4ceb216b3ba9c3701b291766fdcba977cec3a": TokenInfo(
        currency=CurrencyInfo(symbol="BTRFLY", name="Redacted Cartel"), scaling=Decimal("1e-9")
    ),
    "0xc0d9da090194d62b2027e4009d9123de399ea7bf": TokenInfo(
        currency=CurrencyInfo(symbol="VIP", name="VIPChain"), scaling=Decimal("1e-18")
    ),
    "0xc0ea83113038987d974fe667831a36e442e661e7": TokenInfo(
        currency=CurrencyInfo(symbol="LIBFX", name="Libfx"), scaling=Decimal("1e-18")
    ),
    "0xc0eb85285d83217cd7c891702bcbc0fc401e2d9d": TokenInfo(
        currency=CurrencyInfo(symbol="HVN", name="Hiveterminal token"), scaling=Decimal("1e-8")
    ),
    "0xc0ec8caec55f37d47fbfa595727418868a21fd48": TokenInfo(
        currency=CurrencyInfo(symbol="EGC", name="EcoG9coin"), scaling=Decimal("1e-8")
    ),
    "0xc0f1728d9513efc316d0e93a0758c992f88b0809": TokenInfo(
        currency=CurrencyInfo(symbol="SWAT", name="SWTCoin"), scaling=Decimal("1e-8")
    ),
    "0xc0f9bd5fa5698b6505f643900ffa515ea5df54a9": TokenInfo(
        currency=CurrencyInfo(symbol="DONUT", name="Donut"), scaling=Decimal("1e-18")
    ),
    "0xc11551bb497875050b69a2fdccc20a53a9a70263": TokenInfo(
        currency=CurrencyInfo(symbol="TXC", name="TenXCoin"), scaling=Decimal("1e-18")
    ),
    "0xc118ab211227a35386718804a1fd14946d42643f": TokenInfo(
        currency=CurrencyInfo(symbol="MWT", name="Matrix World Network"), scaling=Decimal("1e-18")
    ),
    "0xc11b1268c1a384e55c48c2391d8d480264a3a7f4": TokenInfo(
        currency=CurrencyInfo(symbol="CWBTC", name="cWBTC (Legacy)"), scaling=Decimal("1e-8")
    ),
    "0xc12d099be31567add4e4e4d0d45691c3f58f5663": TokenInfo(
        currency=CurrencyInfo(symbol="AUC", name="Auctus"), scaling=Decimal("1e-18")
    ),
    "0xc12d1c73ee7dc3615ba4e37e4abfdbddfa38907e": TokenInfo(
        currency=CurrencyInfo(symbol="KICK", name="KickToken"), scaling=Decimal("1e-8")
    ),
    "0xc1322d8ae3b0e2e437e0ae36388d0cfd2c02f1c9": TokenInfo(
        currency=CurrencyInfo(symbol="PMT", name="DAO PlayMarket 2.0"), scaling=Decimal("1e-4")
    ),
    "0xc14103c2141e842e228fbac594579e798616ce7a": TokenInfo(
        currency=CurrencyInfo(symbol="SLTC", name="sLTC"), scaling=Decimal("1e-18")
    ),
    "0xc14830e53aa344e8c14603a91229a0b925b0b262": TokenInfo(
        currency=CurrencyInfo(symbol="PXT", name="Populous XBRL Token"), scaling=Decimal("1e-8")
    ),
    "0xc151ca64d66ea44ee4be9d47c3ce7e031b2fccb7": TokenInfo(
        currency=CurrencyInfo(symbol="YFET", name="YFET"), scaling=Decimal("1e-18")
    ),
    "0xc15a399c4ea7815fe36857c9e290ee452a5d6b21": TokenInfo(
        currency=CurrencyInfo(symbol="NAVY", name="BoatPilot"), scaling=Decimal("1e-18")
    ),
    "0xc166038705ffbab3794185b3a9d925632a1df37d": TokenInfo(
        currency=CurrencyInfo(symbol="CC3", name="Coal Coin"), scaling=Decimal("1e-18")
    ),
    "0xc166f976ce9926a3205b145af104eb0e4b38b5c0": TokenInfo(
        currency=CurrencyInfo(symbol="LEGA", name="LINK/ETH Growth Alpha Set"), scaling=Decimal("1e-18")
    ),
    "0xc16b542ff490e01fcc0dc58a60e1efdc3e357ca6": TokenInfo(
        currency=CurrencyInfo(symbol="ROCK2", name="Ice Rock Mining"), scaling=Decimal("1e-0")
    ),
    "0xc17195bde49d70cefcf8a9f2ee1759ffc27bf0b1": TokenInfo(
        currency=CurrencyInfo(symbol="GROO", name="Groocoin"), scaling=Decimal("1e-18")
    ),
    "0xc173af61aa4bab0a5296deff512973b8540d9d1b": TokenInfo(
        currency=CurrencyInfo(symbol="CPT", name="CPT"), scaling=Decimal("1e-18")
    ),
    "0xc175e77b04f2341517334ea3ed0b198a01a97383": TokenInfo(
        currency=CurrencyInfo(symbol="TRXBULL", name="3X Long TRX Token"), scaling=Decimal("1e-18")
    ),
    "0xc18360217d8f7ab5e7c516566761ea12ce7f9d72": TokenInfo(
        currency=CurrencyInfo(symbol="ENS", name="Ethereum Name Service"), scaling=Decimal("1e-18")
    ),
    "0xc1915a97fd75818d3e10570b7613eda8636720bb": TokenInfo(
        currency=CurrencyInfo(symbol="ALTDOOM", name="10X Short Altcoin Index Token"), scaling=Decimal("1e-18")
    ),
    "0xc19216eea17b2f4dd677f1024cda59c7d142f189": TokenInfo(
        currency=CurrencyInfo(symbol="ELOAP", name="ETH Long-Only Alpha Portfolio"), scaling=Decimal("1e-18")
    ),
    "0xc1965d7d18f37062b18ab3d5d1fe7f69873b30dd": TokenInfo(
        currency=CurrencyInfo(symbol="CNZ", name="Coinzo Token"), scaling=Decimal("1e-18")
    ),
    "0xc1ad269f10bf36d6972ee30827051b59d0d2456b": TokenInfo(
        currency=CurrencyInfo(symbol="AGOV", name="Answer Governance"), scaling=Decimal("1e-18")
    ),
    "0xc1ad68c43508dd5addb8d0ac0927dbe752d149d6": TokenInfo(
        currency=CurrencyInfo(symbol="STL", name="Stablecoinswap"), scaling=Decimal("1e-18")
    ),
    "0xc1bfccd4c29813ede019d00d2179eea838a67703": TokenInfo(
        currency=CurrencyInfo(symbol="LUFFY", name="Luffy"), scaling=Decimal("1e-9")
    ),
    "0xc1c7883ea017b083b6167040dbb9c156a8e6b9e9": TokenInfo(
        currency=CurrencyInfo(symbol="ABB", name="ARMENIAN BLOCKCHAIN BANK"), scaling=Decimal("1e-18")
    ),
    "0xc1d204d77861def49b6e769347a883b15ec397ff": TokenInfo(
        currency=CurrencyInfo(symbol="PAX", name="PayperEx"), scaling=Decimal("1e-18")
    ),
    "0xc1d9b5a0776d7c8b98b8a838e5a0dd1bc5fdd53c": TokenInfo(
        currency=CurrencyInfo(symbol="ZONE", name="GridZone io"), scaling=Decimal("1e-18")
    ),
    "0xc1e83478bfa1f590a75d3477dbcb995aa2a142dd": TokenInfo(
        currency=CurrencyInfo(symbol="OGZD.CX", name="Gazprom PJSC ADR"), scaling=Decimal("1e-8")
    ),
    "0xc1eecf1f4af8eb9a2a19f6c26b434aa96ce859e1": TokenInfo(
        currency=CurrencyInfo(symbol="SAVE", name="SaveToken"), scaling=Decimal("1e-8")
    ),
    "0xc1fb6c015fc535abd331d3029de76a62e412fb23": TokenInfo(
        currency=CurrencyInfo(symbol="FORCER", name="Forcer"), scaling=Decimal("1e-4")
    ),
    "0xc20464e0c373486d2b3335576e83a218b1618a5e": TokenInfo(
        currency=CurrencyInfo(symbol="DTRC", name="Datarius Credit"), scaling=Decimal("1e-18")
    ),
    "0xc21dbee65d62770953035f0434c532d578a666c9": TokenInfo(
        currency=CurrencyInfo(symbol="CNRG", name="CryptoEnergy"), scaling=Decimal("1e-18")
    ),
    "0xc221b7e65ffc80de234bbb6667abdd46593d34f0": TokenInfo(
        currency=CurrencyInfo(symbol="WCFG", name="Wrapped Centrifuge"), scaling=Decimal("1e-18")
    ),
    "0xc222e5b89309fab5faf55a3b3bd9082be834916c": TokenInfo(
        currency=CurrencyInfo(symbol="BCA", name="Bitcoiva"), scaling=Decimal("1e-6")
    ),
    "0xc22b30e4cce6b78aaaadae91e44e73593929a3e9": TokenInfo(
        currency=CurrencyInfo(symbol="RAC", name="RAC"), scaling=Decimal("1e-18")
    ),
    "0xc230ce24b527ed4caf97310753330a2965f3a4bd": TokenInfo(
        currency=CurrencyInfo(symbol="C4C", name="Coin4Cast"), scaling=Decimal("1e-10")
    ),
    "0xc237868a9c5729bdf3173dddacaa336a0a5bb6e0": TokenInfo(
        currency=CurrencyInfo(symbol="WGR", name="Wagerr"), scaling=Decimal("1e-8")
    ),
    "0xc242eb8e4e27eae6a2a728a41201152f19595c83": TokenInfo(
        currency=CurrencyInfo(symbol="ECO", name="EcoFi"), scaling=Decimal("1e-18")
    ),
    "0xc2494604e9dcefa2a70dcebf81e6d7be064a334e": TokenInfo(
        currency=CurrencyInfo(symbol="OWT", name="OpenWeb Token"), scaling=Decimal("1e-18")
    ),
    "0xc25a3a3b969415c80451098fa907ec722572917f": TokenInfo(
        currency=CurrencyInfo(symbol="SCURVE", name="LP-sCurve"), scaling=Decimal("1e-18")
    ),
    "0xc25cb249d4f6b8f2e69f58703f03e76523b081b0": TokenInfo(
        currency=CurrencyInfo(symbol="RGLS", name="Regulus Token"), scaling=Decimal("1e-18")
    ),
    "0xc2685307ef2b8842fbf3def432408c46bd0420fd": TokenInfo(
        currency=CurrencyInfo(symbol="LEOBULL", name="3X Long LEO Token"), scaling=Decimal("1e-18")
    ),
    "0xc2708a3a4ba7f64bddc1a49f92f941bc77cad23a": TokenInfo(
        currency=CurrencyInfo(symbol="EGG", name="Waves Ducks"), scaling=Decimal("1e-18")
    ),
    "0xc27a2f05fa577a83ba0fdb4c38443c0718356501": TokenInfo(
        currency=CurrencyInfo(symbol="TAU", name="Lamden Tau"), scaling=Decimal("1e-18")
    ),
    "0xc27c95350ecd634c80df89db0f10cd5c24b7b11f": TokenInfo(
        currency=CurrencyInfo(symbol="PXC", name="Pixie Coin"), scaling=Decimal("1e-2")
    ),
    "0xc2856a8310af421a2a65de16428c2dec6ceacb36": TokenInfo(
        currency=CurrencyInfo(symbol="YAH", name="JamaiCoin"), scaling=Decimal("1e-18")
    ),
    "0xc28d4341ad8224e1a424558074ef0b4515f424d5": TokenInfo(
        currency=CurrencyInfo(symbol="DBT", name="Datbit"), scaling=Decimal("1e-0")
    ),
    "0xc28e27870558cf22add83540d2126da2e4b464c2": TokenInfo(
        currency=CurrencyInfo(symbol="SASHIMI", name="Sashimi"), scaling=Decimal("1e-18")
    ),
    "0xc28e931814725bbeb9e670676fabbcb694fe7df2": TokenInfo(
        currency=CurrencyInfo(symbol="EQUAD", name="Quadrant Protocol"), scaling=Decimal("1e-18")
    ),
    "0xc29004ab38334dc7a9eca1b89d6d4bf9f564d5cf": TokenInfo(
        currency=CurrencyInfo(symbol="OMNES", name="OmnesCoin"), scaling=Decimal("1e-18")
    ),
    "0xc292b91277066b644f53352be19a734f20fa0f0d": TokenInfo(
        currency=CurrencyInfo(symbol="BZUN.CX", name="Baozun Inc"), scaling=Decimal("1e-8")
    ),
    "0xc299004a310303d1c0005cb14c70ccc02863924d": TokenInfo(
        currency=CurrencyInfo(symbol="TRI", name="Trinity Protocol"), scaling=Decimal("1e-9")
    ),
    "0xc2992b2c22238f296c2f429ee2f7afb462ed1750": TokenInfo(
        currency=CurrencyInfo(symbol="IXTZ", name="iXTZ"), scaling=Decimal("1e-18")
    ),
    "0xc2b58812c24020ea924c3d7c241c441605f12e75": TokenInfo(
        currency=CurrencyInfo(symbol="ETF", name="Entherfound"), scaling=Decimal("1e-8")
    ),
    "0xc2be193f581f129ace32d2fe949d100dc09c2a05": TokenInfo(
        currency=CurrencyInfo(symbol="UTD", name="United Token Dollars"), scaling=Decimal("1e-18")
    ),
    "0xc2c4d4094f521a6905d46cb8aa3d1765abea89cf": TokenInfo(
        currency=CurrencyInfo(symbol="9988.CX", name="Alibaba Group Holding Limited"), scaling=Decimal("1e-8")
    ),
    "0xc2c63f23ec5e97efbd7565df9ec764fdc7d4e91d": TokenInfo(
        currency=CurrencyInfo(symbol="BOU", name="Boule Token"), scaling=Decimal("1e-18")
    ),
    "0xc2cb1040220768554cf699b0d863a3cd4324ce32": TokenInfo(
        currency=CurrencyInfo(symbol="yDAI", name="iearn DAI"), scaling=Decimal("1e-18")
    ),
    "0xc2d3d1cbab16f0e77acd96b08edd3c4dd4129763": TokenInfo(
        currency=CurrencyInfo(symbol="USDTDOOM", name="10X Short Tether Token"), scaling=Decimal("1e-18")
    ),
    "0xc2e343118f937f88ee1fc3150cdc0d6f3d11bba7": TokenInfo(
        currency=CurrencyInfo(symbol="STRO", name="Supertron"), scaling=Decimal("1e-18")
    ),
    "0xc2e3ed7f61d338755bf7b6fb4baa0fffada4ac28": TokenInfo(
        currency=CurrencyInfo(symbol="DRC", name="Dmaarc"), scaling=Decimal("1e-18")
    ),
    "0xc305787acdc859b36f64d72cb0e00519d20731ad": TokenInfo(
        currency=CurrencyInfo(symbol="GILD.CX", name="Gilead Sciences"), scaling=Decimal("1e-8")
    ),
    "0xc314b0e758d5ff74f63e307a86ebfe183c95767b": TokenInfo(
        currency=CurrencyInfo(symbol="ADP", name="ADP"), scaling=Decimal("1e-18")
    ),
    "0xc324a2f6b05880503444451b8b27e6f9e63287cb": TokenInfo(
        currency=CurrencyInfo(symbol="XUC", name="Exchange Union"), scaling=Decimal("1e-18")
    ),
    "0xc32cc5b70bee4bd54aa62b9aefb91346d18821c4": TokenInfo(
        currency=CurrencyInfo(symbol="ITS", name="Iteration Syndicate"), scaling=Decimal("1e-18")
    ),
    "0xc3332ce4991fc311aae888c8d265b900f6e59b0b": TokenInfo(
        currency=CurrencyInfo(symbol="SFT", name="SportsFix"), scaling=Decimal("1e-18")
    ),
    "0xc34b21f6f8e51cc965c2393b3ccfa3b82beb2403": TokenInfo(
        currency=CurrencyInfo(symbol="IoT", name="IoTコイン"), scaling=Decimal("1e-6")
    ),
    "0xc350e846e2c57f9eece90febc253d14c8080871b": TokenInfo(
        currency=CurrencyInfo(symbol="SRH", name="SRH"), scaling=Decimal("1e-18")
    ),
    "0xc3589f56b6869824804a5ea29f2c9886af1b0fce": TokenInfo(
        currency=CurrencyInfo(symbol="HNY", name="Honey"), scaling=Decimal("1e-18")
    ),
    "0xc35aaea6dd561a9976e1745a22f8cc5a762354bb": TokenInfo(
        currency=CurrencyInfo(symbol="AIV", name="AIVIA"), scaling=Decimal("1e-18")
    ),
    "0xc35e16a4fb05f12e3cb0253c807ee76c2833be65": TokenInfo(
        currency=CurrencyInfo(symbol="SEOS", name="Smart Eye Operating System"), scaling=Decimal("1e-18")
    ),
    "0xc36e2c02e64585c15794b8e25e826d50b15fd878": TokenInfo(
        currency=CurrencyInfo(symbol="ANIME", name="Animeyen"), scaling=Decimal("1e-8")
    ),
    "0xc3761eb917cd790b30dad99f6cc5b4ff93c4f9ea": TokenInfo(
        currency=CurrencyInfo(symbol="ERC20", name="ERC20"), scaling=Decimal("1e-18")
    ),
    "0xc3771d47e2ab5a519e2917e61e23078d0c05ed7f": TokenInfo(
        currency=CurrencyInfo(symbol="GTH", name="Gather"), scaling=Decimal("1e-18")
    ),
    "0xc37e8a31ba2d110c12f09f0239954a68b00bc599": TokenInfo(
        currency=CurrencyInfo(symbol="EUBC", name="EUB Chain"), scaling=Decimal("1e-8")
    ),
    "0xc3884e677e0a3953072a7fc63e158e98313bf97b": TokenInfo(
        currency=CurrencyInfo(symbol="HEY", name="HEY-Chain"), scaling=Decimal("1e-18")
    ),
    "0xc38f1fb49acdf2f1213caf3319f6eb3ea2cb7527": TokenInfo(
        currency=CurrencyInfo(symbol="BITS", name="Bitcoinus"), scaling=Decimal("1e-18")
    ),
    "0xc39835d32428728cbde6903f84c76750976c0323": TokenInfo(
        currency=CurrencyInfo(symbol="BOCBP", name="BTC On-Chain Beta Portfolio Set"), scaling=Decimal("1e-18")
    ),
    "0xc39e626a04c5971d770e319760d7926502975e47": TokenInfo(
        currency=CurrencyInfo(symbol="AXPR", name="aXpire"), scaling=Decimal("1e-18")
    ),
    "0xc3bc9eb71f75ec439a6b6c8e8b746fcf5b62f703": TokenInfo(
        currency=CurrencyInfo(symbol="VOC", name="VORMACOIN"), scaling=Decimal("1e-18")
    ),
    "0xc3d6dda603fc15fd4bf9303150fe11c7cd6059dc": TokenInfo(
        currency=CurrencyInfo(symbol="COW", name="Coweye"), scaling=Decimal("1e-18")
    ),
    "0xc3dd23a0a854b4f9ae80670f528094e9eb607ccb": TokenInfo(
        currency=CurrencyInfo(symbol="TRND", name="Trendering"), scaling=Decimal("1e-18")
    ),
    "0xc3e2de0b661cf58f66bde8e896905399ded58af5": TokenInfo(
        currency=CurrencyInfo(symbol="MAC", name="Matrexcoin"), scaling=Decimal("1e-0")
    ),
    "0xc3eb2622190c57429aac3901808994443b64b466": TokenInfo(
        currency=CurrencyInfo(symbol="ORO", name="ORO"), scaling=Decimal("1e-18")
    ),
    "0xc3f206e06b33c3f5df9b95b8294a5e71f09480ab": TokenInfo(
        currency=CurrencyInfo(symbol="EXCHDOOM", name="10X Short Exchange Token Index Token"), scaling=Decimal("1e-18")
    ),
    "0xc4131c1893576e078a0b637b653f3e6a18e137ac": TokenInfo(
        currency=CurrencyInfo(symbol="YB", name="YB"), scaling=Decimal("1e-4")
    ),
    "0xc4199fb6ffdb30a829614beca030f9042f1c3992": TokenInfo(
        currency=CurrencyInfo(symbol="SGT", name="snglsDAO Governance Token"), scaling=Decimal("1e-18")
    ),
    "0xc42209accc14029c1012fb5680d95fbd6036e2a0": TokenInfo(
        currency=CurrencyInfo(symbol="PPP", name="PayPie"), scaling=Decimal("1e-18")
    ),
    "0xc438b4c0dfbb1593be6dee03bbd1a84bb3aa6213": TokenInfo(
        currency=CurrencyInfo(symbol="EQC", name="Qchain"), scaling=Decimal("1e-8")
    ),
    "0xc4621cb2e5e6ff8252e25dbc8e4e6ee34afa0c9c": TokenInfo(
        currency=CurrencyInfo(symbol="OCFT.CX", name="OneConnect"), scaling=Decimal("1e-8")
    ),
    "0xc477d038d5420c6a9e0b031712f61c5120090de9": TokenInfo(
        currency=CurrencyInfo(symbol="BOSON", name="Boson Protocol"), scaling=Decimal("1e-18")
    ),
    "0xc48b1ac1417db27c4e2c2ed3dae5a3d2fbb07dc5": TokenInfo(
        currency=CurrencyInfo(symbol="STB", name="StarBlock"), scaling=Decimal("1e-8")
    ),
    "0xc4a59854a63588a049f4e326af927400c6140746": TokenInfo(
        currency=CurrencyInfo(symbol="PCTO", name="Simply Crypto"), scaling=Decimal("1e-3")
    ),
    "0xc4a86561cb0b7ea1214904f26e6d50fd357c7986": TokenInfo(
        currency=CurrencyInfo(symbol="CHG", name="Charg Coin"), scaling=Decimal("1e-18")
    ),
    "0xc4bb7277a74678f053259cb1f96140347efbfd46": TokenInfo(
        currency=CurrencyInfo(symbol="COC", name="Coin of the champio"), scaling=Decimal("1e-18")
    ),
    "0xc4bcd64cb216d49fd3c643a32762f34626b45a1a": TokenInfo(
        currency=CurrencyInfo(symbol="COSM", name="CosmoCoin"), scaling=Decimal("1e-18")
    ),
    "0xc4c1f484b6dc3edb27f3a208735dc96ac9c03bdd": TokenInfo(
        currency=CurrencyInfo(symbol="TRN", name="Transfereuim"), scaling=Decimal("1e-18")
    ),
    "0xc4c2614e694cf534d407ee49f8e44d125e4681c4": TokenInfo(
        currency=CurrencyInfo(symbol="CHAIN", name="Chain Games"), scaling=Decimal("1e-18")
    ),
    "0xc4c7ea4fab34bd9fb9a5e1b1a98df76e26e6407c": TokenInfo(
        currency=CurrencyInfo(symbol="COCOS", name="COCOS BCX"), scaling=Decimal("1e-18")
    ),
    "0xc4cb5793bd58bad06bf51fb37717b86b02cbe8a4": TokenInfo(
        currency=CurrencyInfo(symbol="CREDIT", name="PROXI DeFi"), scaling=Decimal("1e-18")
    ),
    "0xc4ce6cb000d1c435c6d0c28814a2d61120f32b84": TokenInfo(
        currency=CurrencyInfo(symbol="1211.CX", name="BYD Company Limited"), scaling=Decimal("1e-8")
    ),
    "0xc4d5545392f5fc57eba3af8981815669bb7e2a48": TokenInfo(
        currency=CurrencyInfo(symbol="HDP.Ф", name="HEdpAY"), scaling=Decimal("1e-4")
    ),
    "0xc4de189abf94c57f396bd4c52ab13b954febefd8": TokenInfo(
        currency=CurrencyInfo(symbol="B20", name="B20"), scaling=Decimal("1e-18")
    ),
    "0xc4e15973e6ff2a35cc804c2cf9d2a1b817a8b40f": TokenInfo(
        currency=CurrencyInfo(symbol="IBBTC", name="Interest Bearing Bi"), scaling=Decimal("1e-18")
    ),
    "0xc4f6e93aeddc11dc22268488465babcaf09399ac": TokenInfo(
        currency=CurrencyInfo(symbol="HI", name="hi Dollar"), scaling=Decimal("1e-18")
    ),
    "0xc50948bac01116f246259070ea6084c04649efdf": TokenInfo(
        currency=CurrencyInfo(symbol="PDI", name="Pindex"), scaling=Decimal("1e-6")
    ),
    "0xc50ef449171a51fbeafd7c562b064b6471c36caa": TokenInfo(
        currency=CurrencyInfo(symbol="ZINU", name="Zombie Inu"), scaling=Decimal("1e-9")
    ),
    "0xc520f3ac303a107d8f4b08b326b6ea66a4f961cd": TokenInfo(
        currency=CurrencyInfo(symbol="LG", name="LG"), scaling=Decimal("1e-18")
    ),
    "0xc528c28fec0a90c083328bc45f587ee215760a0f": TokenInfo(
        currency=CurrencyInfo(symbol="EDR", name="Endor Protocol Token"), scaling=Decimal("1e-18")
    ),
    "0xc52c326331e9ce41f04484d3b5e5648158028804": TokenInfo(
        currency=CurrencyInfo(symbol="ZCX", name="Unizen"), scaling=Decimal("1e-18")
    ),
    "0xc538143202f3b11382d8606aae90a96b042a19db": TokenInfo(
        currency=CurrencyInfo(symbol="CNB", name="Coinsbit Token"), scaling=Decimal("1e-18")
    ),
    "0xc54083e77f913a4f99e1232ae80c318ff03c9d17": TokenInfo(
        currency=CurrencyInfo(symbol="CIT", name="CariNet"), scaling=Decimal("1e-18")
    ),
    "0xc541b907478d5cd334c0cbfcb9603b6dac6e9ee3": TokenInfo(
        currency=CurrencyInfo(symbol="CNYQ", name="CNYQ Stablecoin by Q DAO v1.0"), scaling=Decimal("1e-18")
    ),
    "0xc5516ab4614f33328131da27ecba516a396178b4": TokenInfo(
        currency=CurrencyInfo(symbol="GTSE", name="Global Tourism Sharing Ecology"), scaling=Decimal("1e-18")
    ),
    "0xc55c2175e90a46602fd42e931f62b3acc1a013ca": TokenInfo(
        currency=CurrencyInfo(symbol="STARS", name="Mogul Productions"), scaling=Decimal("1e-18")
    ),
    "0xc56b13ebbcffa67cfb7979b900b736b3fb480d78": TokenInfo(
        currency=CurrencyInfo(symbol="SAT", name="Social Activity Token"), scaling=Decimal("1e-8")
    ),
    "0xc57d533c50bc22247d49a368880fb49a1caa39f7": TokenInfo(
        currency=CurrencyInfo(symbol="PTF", name="PowerTrade Fuel"), scaling=Decimal("1e-18")
    ),
    "0xc5807183a9661a533cb08cbc297594a0b864dc12": TokenInfo(
        currency=CurrencyInfo(symbol="iTRX", name="Synth iTRX"), scaling=Decimal("1e-18")
    ),
    "0xc581b735a1688071a1746c968e0798d642ede491": TokenInfo(
        currency=CurrencyInfo(symbol="EURT", name="Euro Tether"), scaling=Decimal("1e-6")
    ),
    "0xc58432a1969a2cb15f14dae6dcca736cfa60285a": TokenInfo(
        currency=CurrencyInfo(symbol="TRXDOOM", name="10X Short TRX Token"), scaling=Decimal("1e-18")
    ),
    "0xc58c0fca06908e66540102356f2e91edcaeb8d81": TokenInfo(
        currency=CurrencyInfo(symbol="NUKE", name="Half Life"), scaling=Decimal("1e-18")
    ),
    "0xc58f53a8adff2fb4eb16ed56635772075e2ee123": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNIWBTCWETH", name="Aave AMM UniWBTCWET"), scaling=Decimal("1e-18")
    ),
    "0xc596bd09d652827b0106292d3e378d5938df4b12": TokenInfo(
        currency=CurrencyInfo(symbol="TPT", name="Teleport Token"), scaling=Decimal("1e-18")
    ),
    "0xc59cb23295e2deeb66bd090acb6b02be8d30a11f": TokenInfo(
        currency=CurrencyInfo(symbol="KUB", name="Kublaicoin"), scaling=Decimal("1e-10")
    ),
    "0xc5b3d3231001a776123194cf1290068e8b0c783b": TokenInfo(
        currency=CurrencyInfo(symbol="LIT", name="LIT"), scaling=Decimal("1e-18")
    ),
    "0xc5bbae50781be1669306b9e001eff57a2957b09d": TokenInfo(
        currency=CurrencyInfo(symbol="GTO", name="Gifto"), scaling=Decimal("1e-5")
    ),
    "0xc5bddf9843308380375a611c18b50fb9341f502a": TokenInfo(
        currency=CurrencyInfo(symbol="YVE-CRVDAO", name="veCRV-DAO yVault"), scaling=Decimal("1e-18")
    ),
    "0xc5cea8292e514405967d958c2325106f2f48da77": TokenInfo(
        currency=CurrencyInfo(symbol="PRFT", name="Proof Token"), scaling=Decimal("1e-18")
    ),
    "0xc5d105e63711398af9bbff092d4b6769c82f793d": TokenInfo(
        currency=CurrencyInfo(symbol="BEC", name="Beauty Chain"), scaling=Decimal("1e-18")
    ),
    "0xc5d350b854a6cff0fc5a38a115a90c774dcae1b9": TokenInfo(
        currency=CurrencyInfo(symbol="CFT", name="CryptoForecast"), scaling=Decimal("1e-18")
    ),
    "0xc5e017450346e4f9a2e477519d65affcfc90586a": TokenInfo(
        currency=CurrencyInfo(symbol="ZUBE", name="zuzubecoin"), scaling=Decimal("1e-18")
    ),
    "0xc5e19fd321b9bc49b41d9a3a5ad71bcc21cc3c54": TokenInfo(
        currency=CurrencyInfo(symbol="TDEX", name="TradePower Dex"), scaling=Decimal("1e-18")
    ),
    "0xc5ef726e7f244522876fee3292db6557b6b854c9": TokenInfo(
        currency=CurrencyInfo(symbol="DLPH.CX", name="Delphi Automotive"), scaling=Decimal("1e-8")
    ),
    "0xc6003a33f7464d6e6c1dc17344a75a9952187541": TokenInfo(
        currency=CurrencyInfo(symbol="TST", name="Trust Shore Token"), scaling=Decimal("1e-18")
    ),
    "0xc626e0619ac79afea9281c8eb9b1a9f9d3fab532": TokenInfo(
        currency=CurrencyInfo(symbol="FR", name="Freedom Reserve"), scaling=Decimal("1e-18")
    ),
    "0xc6363c1a05f840be2d185d7084b28af84c543d40": TokenInfo(
        currency=CurrencyInfo(symbol="BMT", name="BMToken"), scaling=Decimal("1e-18")
    ),
    "0xc64500dd7b0f1794807e67802f8abbf5f8ffb054": TokenInfo(
        currency=CurrencyInfo(symbol="LOCUS", name="Locus Chain"), scaling=Decimal("1e-18")
    ),
    "0xc650f5514ae1a3a27930922145ce49e8a91b91ab": TokenInfo(
        currency=CurrencyInfo(symbol="VNTY", name="VENOTY"), scaling=Decimal("1e-18")
    ),
    "0xc666081073e8dff8d3d1c2292a29ae1a2153ec09": TokenInfo(
        currency=CurrencyInfo(symbol="DGTX", name="Digitex Token"), scaling=Decimal("1e-18")
    ),
    "0xc669928185dbce49d2230cc9b0979be6dc797957": TokenInfo(
        currency=CurrencyInfo(symbol="BTT", name="BitTorrent"), scaling=Decimal("1e-18")
    ),
    "0xc66ea802717bfb9833400264dd12c2bceaa34a6d": TokenInfo(
        currency=CurrencyInfo(symbol="MKR", name="MKR"), scaling=Decimal("1e-18")
    ),
    "0xc690f7c7fcffa6a82b79fab7508c466fefdfc8c5": TokenInfo(
        currency=CurrencyInfo(symbol="LYM", name="Lympo"), scaling=Decimal("1e-18")
    ),
    "0xc6afbdef9467517410a49cbe513270de3c96ebd7": TokenInfo(
        currency=CurrencyInfo(symbol="XPT.CX", name="Platinum Spot"), scaling=Decimal("1e-8")
    ),
    "0xc6bf2a2a43ca360bb0ec6770f57f77cdde64bb3f": TokenInfo(
        currency=CurrencyInfo(symbol="UTY", name="UnityDAO"), scaling=Decimal("1e-8")
    ),
    "0xc6c2a8f2c957806ac0580b46d84d2717291b9df1": TokenInfo(
        currency=CurrencyInfo(symbol="CMA", name="CoinMarketAlert"), scaling=Decimal("1e-18")
    ),
    "0xc6c6224cf32f5b0850ddf740b47cd1ed31abead4": TokenInfo(
        currency=CurrencyInfo(symbol="KUPP", name="KUPP"), scaling=Decimal("1e-8")
    ),
    "0xc6d603a9df53d1542552058c382bf115aace70c7": TokenInfo(
        currency=CurrencyInfo(symbol="TRET", name="Tourist Review Token"), scaling=Decimal("1e-8")
    ),
    "0xc6dddb5bc6e61e0841c54f3e723ae1f3a807260b": TokenInfo(
        currency=CurrencyInfo(symbol="URUS", name="Aurox Token"), scaling=Decimal("1e-18")
    ),
    "0xc6e64729931f60d2c8bc70a27d66d9e0c28d1bf9": TokenInfo(
        currency=CurrencyInfo(symbol="FLOW", name="Flow Protocol"), scaling=Decimal("1e-9")
    ),
    "0xc7038ccf60e48c5b7119e55566a6ad9f2d66c7c2": TokenInfo(
        currency=CurrencyInfo(symbol="TRYBBULL", name="3X Long BiLira Token"), scaling=Decimal("1e-18")
    ),
    "0xc7088fac73c55bfae5c2a963c3029b072c7dff25": TokenInfo(
        currency=CurrencyInfo(symbol="BLL", name="BTC AI Limit Loss"), scaling=Decimal("1e-18")
    ),
    "0xc713e5e149d5d0715dcd1c156a020976e7e56b88": TokenInfo(
        currency=CurrencyInfo(symbol="AMKR", name="Aave MKR"), scaling=Decimal("1e-18")
    ),
    "0xc719d010b63e5bbf2c0551872cd5316ed26acd83": TokenInfo(
        currency=CurrencyInfo(symbol="DIP", name="Etherisc DIP Token"), scaling=Decimal("1e-18")
    ),
    "0xc71e20e54adfc415f79bf0a8f11122917920050e": TokenInfo(
        currency=CurrencyInfo(symbol="TORI", name="Storichain Token"), scaling=Decimal("1e-18")
    ),
    "0xc7283b66eb1eb5fb86327f08e1b5816b0720212b": TokenInfo(
        currency=CurrencyInfo(symbol="TRIBE", name="TRIBE"), scaling=Decimal("1e-18")
    ),
    "0xc72fe8e3dd5bef0f9f31f259399f301272ef2a2d": TokenInfo(
        currency=CurrencyInfo(symbol="INSTAR", name="Insights Network"), scaling=Decimal("1e-18")
    ),
    "0xc73f2474001ad1d6aed615af53631148cf98de6b": TokenInfo(
        currency=CurrencyInfo(symbol="BAR", name="Billionaire Ambition"), scaling=Decimal("1e-18")
    ),
    "0xc741f06082aa47f93729070ad0dd95e223bda091": TokenInfo(
        currency=CurrencyInfo(symbol="LEDU", name="Education"), scaling=Decimal("1e-8")
    ),
    "0xc7596f3fc97ae603e1d7ffa61e6efb7b6a59bed2": TokenInfo(
        currency=CurrencyInfo(symbol="YOO", name="Yoo Ecology"), scaling=Decimal("1e-18")
    ),
    "0xc75f15ada581219c95485c578e124df3985e4ce0": TokenInfo(
        currency=CurrencyInfo(symbol="ZZZ", name="zzz.finance"), scaling=Decimal("1e-18")
    ),
    "0xc761c8dc05ae52a8a785665e528ddbb00c098ad1": TokenInfo(
        currency=CurrencyInfo(symbol="SMT", name="SunMoney"), scaling=Decimal("1e-18")
    ),
    "0xc761d1ccb38a94703675d2cdb15f7f1b3dcff7b7": TokenInfo(
        currency=CurrencyInfo(symbol="HIZ", name="Hiz Finance"), scaling=Decimal("1e-18")
    ),
    "0xc769506c9411821f62aebc13a98d002561fb3a1f": TokenInfo(
        currency=CurrencyInfo(symbol="TDC", name="Derby Coin"), scaling=Decimal("1e-10")
    ),
    "0xc76fb75950536d98fa62ea968e1d6b45ffea2a55": TokenInfo(
        currency=CurrencyInfo(symbol="COL", name="Unit Protocol"), scaling=Decimal("1e-18")
    ),
    "0xc770eefad204b5180df6a14ee197d99d808ee52d": TokenInfo(
        currency=CurrencyInfo(symbol="FOX", name="FOX"), scaling=Decimal("1e-18")
    ),
    "0xc7743bf0b300ec041e704cc34d4f43050942099e": TokenInfo(
        currency=CurrencyInfo(symbol="CATX", name="CAT.trade Protocol"), scaling=Decimal("1e-18")
    ),
    "0xc77b230f31b517f1ef362e59c173c2be6540b5e8": TokenInfo(
        currency=CurrencyInfo(symbol="VIDY", name="VIDY"), scaling=Decimal("1e-18")
    ),
    "0xc77d7e0dd7b2a01b990e866feb21d031f1418c2e": TokenInfo(
        currency=CurrencyInfo(symbol="LSC", name="Littlesesame"), scaling=Decimal("1e-18")
    ),
    "0xc787a019ea4e0700e997c8e7d26ba2efa2e6862a": TokenInfo(
        currency=CurrencyInfo(symbol="SHARE", name="Mining.Taxi"), scaling=Decimal("1e-0")
    ),
    "0xc798cd1c49db0e297312e4c682752668ce1db2ad": TokenInfo(
        currency=CurrencyInfo(symbol="LFR", name="LifeRun Coin"), scaling=Decimal("1e-5")
    ),
    "0xc79d440551a03f84f863b1f259f135794c8a7190": TokenInfo(
        currency=CurrencyInfo(symbol="MGX", name="MegaX"), scaling=Decimal("1e-18")
    ),
    "0xc7bba5b765581efb2cdd2679db5bea9ee79b201f": TokenInfo(
        currency=CurrencyInfo(symbol="GEM", name="Gems"), scaling=Decimal("1e-18")
    ),
    "0xc7c03b8a3fc5719066e185ea616e87b88eba44a3": TokenInfo(
        currency=CurrencyInfo(symbol="ELI", name="EligmaToken"), scaling=Decimal("1e-18")
    ),
    "0xc7e43a1c8e118aa2965f5eabe0e718d83db7a63c": TokenInfo(
        currency=CurrencyInfo(symbol="ZCRT", name="ZCore Token"), scaling=Decimal("1e-18")
    ),
    "0xc7f77384b416b68d6ae1ddc3ed55ba2797e3b7f2": TokenInfo(
        currency=CurrencyInfo(symbol="OAS.CX", name="Oasis Petroleum"), scaling=Decimal("1e-8")
    ),
    "0xc80c5e40220172b36adee2c951f26f2a577810c5": TokenInfo(
        currency=CurrencyInfo(symbol="BNK", name="Bankera"), scaling=Decimal("1e-8")
    ),
    "0xc813ea5e3b48bebeedb796ab42a30c5599b01740": TokenInfo(
        currency=CurrencyInfo(symbol="NIOX", name="Autonio"), scaling=Decimal("1e-4")
    ),
    "0xc8209c0dd9577ab10c2bdbd96b02eab114af80e0": TokenInfo(
        currency=CurrencyInfo(symbol="ISRG.CX", name="Intuitive Surgical Inc"), scaling=Decimal("1e-8")
    ),
    "0xc82abb524257c8ee4790bfdefb452b2d6a395e21": TokenInfo(
        currency=CurrencyInfo(symbol="MIDBEAR", name="3X Short Midcap Index Token"), scaling=Decimal("1e-18")
    ),
    "0xc834fa996fa3bec7aad3693af486ae53d8aa8b50": TokenInfo(
        currency=CurrencyInfo(symbol="CONV", name="Convergence"), scaling=Decimal("1e-18")
    ),
    "0xc86817249634ac209bc73fca1712bbd75e37407d": TokenInfo(
        currency=CurrencyInfo(symbol="1-UP", name="1 UP"), scaling=Decimal("1e-18")
    ),
    "0xc86d054809623432210c107af2e3f619dcfbf652": TokenInfo(
        currency=CurrencyInfo(symbol="UPP", name="Sentinel Protocol"), scaling=Decimal("1e-18")
    ),
    "0xc8717fe8465d51d83581c3941171c0b74cb64f9b": TokenInfo(
        currency=CurrencyInfo(symbol="TYD", name="Tianya Diamond"), scaling=Decimal("1e-8")
    ),
    "0xc87412535bec14fe79497914dc5886fb0a163123": TokenInfo(
        currency=CurrencyInfo(symbol="BDX", name="Bright Dream X Token"), scaling=Decimal("1e-18")
    ),
    "0xc87c5dd86a3d567ff28701886fb0745aaa898da4": TokenInfo(
        currency=CurrencyInfo(symbol="CTG", name="CT Global"), scaling=Decimal("1e-18")
    ),
    "0xc87f95aa269dd300d9f1ce49d8e1fd8119a10456": TokenInfo(
        currency=CurrencyInfo(symbol="BDCC", name="BDCC COIN"), scaling=Decimal("1e-18")
    ),
    "0xc8807f0f5ba3fa45ffbdc66928d71c5289249014": TokenInfo(
        currency=CurrencyInfo(symbol="ISP", name="Ispolink"), scaling=Decimal("1e-18")
    ),
    "0xc88be04c809856b75e3dfe19eb4dcf0a3b15317a": TokenInfo(
        currency=CurrencyInfo(symbol="BKC", name="Bankcoin Cash"), scaling=Decimal("1e-8")
    ),
    "0xc89b4a8a121dd3e726fe7515e703936cf83e3350": TokenInfo(
        currency=CurrencyInfo(symbol="KPER", name="Kper Network"), scaling=Decimal("1e-18")
    ),
    "0xc8c424b91d8ce0137bab4b832b7f7d154156ba6c": TokenInfo(
        currency=CurrencyInfo(symbol="APM", name="apM Coin"), scaling=Decimal("1e-18")
    ),
    "0xc8c6a31a4a806d3710a7b38b7b296d2fabccdba8": TokenInfo(
        currency=CurrencyInfo(symbol="ELIX", name="Elixir"), scaling=Decimal("1e-18")
    ),
    "0xc8c6fc3c4f6342c5291e747268625f979a888ebf": TokenInfo(
        currency=CurrencyInfo(symbol="GRM", name="Green Money"), scaling=Decimal("1e-18")
    ),
    "0xc8cac7672f4669685817cf332a33eb249f085475": TokenInfo(
        currency=CurrencyInfo(symbol="LVN", name="LivenCoin"), scaling=Decimal("1e-18")
    ),
    "0xc8d2ab2a6fdebc25432e54941cb85b55b9f152db": TokenInfo(
        currency=CurrencyInfo(symbol="GRAP", name="Grap Finance"), scaling=Decimal("1e-18")
    ),
    "0xc8d674114bac90148d11d3c1d33c61835a0f9dcd": TokenInfo(
        currency=CurrencyInfo(symbol="MNFLX", name="Mirrored Netflix"), scaling=Decimal("1e-18")
    ),
    "0xc8dfb3bba61c150e6a0f8b6c85a5207ec92adea7": TokenInfo(
        currency=CurrencyInfo(symbol="DDOG.CX", name="Datadog Inc"), scaling=Decimal("1e-8")
    ),
    "0xc8e69913c0ea5d45bf67e52412eb8bcab5b9875e": TokenInfo(
        currency=CurrencyInfo(symbol="BNBDOOM", name="10X Short BNB Token"), scaling=Decimal("1e-18")
    ),
    "0xc8f5e4c77422ad6423458cbe189f41bf669787c8": TokenInfo(
        currency=CurrencyInfo(symbol="SELF", name="SELF Token"), scaling=Decimal("1e-6")
    ),
    "0xc918b74218528f4afa91ff3e8dd4b6eed955c1a4": TokenInfo(
        currency=CurrencyInfo(symbol="MTCH.CX", name="Match Group Inc"), scaling=Decimal("1e-8")
    ),
    "0xc9287623832668432099cef2ffdef3ced14f4315": TokenInfo(
        currency=CurrencyInfo(symbol="XAUTBULL", name="3X Long Tether Gold Token"), scaling=Decimal("1e-18")
    ),
    "0xc944e90c64b2c07662a292be6244bdf05cda44a7": TokenInfo(
        currency=CurrencyInfo(symbol="GRT", name="The Graph"), scaling=Decimal("1e-18")
    ),
    "0xc94537de4b1def7c6664c3d9aa7cb5549953dc4f": TokenInfo(
        currency=CurrencyInfo(symbol="DE.CX", name="Deere"), scaling=Decimal("1e-8")
    ),
    "0xc958e9fb59724f8b0927426a8836f1158f0d03cf": TokenInfo(
        currency=CurrencyInfo(symbol="SWAP", name="SWAPS.NETWORK"), scaling=Decimal("1e-18")
    ),
    "0xc962ad021a69d457564e985738c719ae3f79b707": TokenInfo(
        currency=CurrencyInfo(symbol="IFX24", name="IFX24"), scaling=Decimal("1e-18")
    ),
    "0xc9634da9b1eefd1cb3d88b598a91ec69e5afe4e4": TokenInfo(
        currency=CurrencyInfo(symbol="MUM", name="Maxum"), scaling=Decimal("1e-0")
    ),
    "0xc96df921009b790dffca412375251ed1a2b75c60": TokenInfo(
        currency=CurrencyInfo(symbol="ORME", name="Ormeus Coin"), scaling=Decimal("1e-8")
    ),
    "0xc97a5cdf41bafd51c8dbe82270097e704d748b92": TokenInfo(
        currency=CurrencyInfo(symbol="KLOWN", name="Ether Clown"), scaling=Decimal("1e-7")
    ),
    "0xc980be019f2ac10a1c96f964b971a5f44551d318": TokenInfo(
        currency=CurrencyInfo(symbol="BFI", name="BitFarmings"), scaling=Decimal("1e-18")
    ),
    "0xc98e0639c6d2ec037a615341c369666b110e80e5": TokenInfo(
        currency=CurrencyInfo(symbol="EXMR", name="EXMR"), scaling=Decimal("1e-8")
    ),
    "0xc9a2c4868f0f96faaa739b59934dc9cb304112ec": TokenInfo(
        currency=CurrencyInfo(symbol="BGBP", name="Binance GBP Stable Coin"), scaling=Decimal("1e-8")
    ),
    "0xc9afdea326c109d441519d355756f4e88465f94d": TokenInfo(
        currency=CurrencyInfo(symbol="DOB", name="Doblone"), scaling=Decimal("1e-8")
    ),
    "0xc9bc48c72154ef3e5425641a3c747242112a46af": TokenInfo(
        currency=CurrencyInfo(symbol="ARAI", name="Aave RAI"), scaling=Decimal("1e-18")
    ),
    "0xc9c4d9ec2b44b241361707679d3db0876ac10ca6": TokenInfo(
        currency=CurrencyInfo(symbol="POC", name="Power Candy"), scaling=Decimal("1e-18")
    ),
    "0xc9c69a216568de4d5b991b05cc9c382494ffa62e": TokenInfo(
        currency=CurrencyInfo(symbol="YAMA", name="Okayama"), scaling=Decimal("1e-18")
    ),
    "0xc9ce70a381910d0a90b30d408cc9c7705ee882de": TokenInfo(
        currency=CurrencyInfo(symbol="NYAN", name="Nyan Finance [old]"), scaling=Decimal("1e-18")
    ),
    "0xc9de4b7f0c3d991e967158e4d4bfa4b51ec0b114": TokenInfo(
        currency=CurrencyInfo(symbol="ROK", name="Rocketchain"), scaling=Decimal("1e-18")
    ),
    "0xc9ffa1fa580ac40525dbf1ddf06b9b6e5c3c9657": TokenInfo(
        currency=CurrencyInfo(symbol="BNTX.CX", name="Biontech SE"), scaling=Decimal("1e-8")
    ),
    "0xca00bc15f67ebea4b20dfaaa847cace113cc5501": TokenInfo(
        currency=CurrencyInfo(symbol="XCD", name="Capdax"), scaling=Decimal("1e-18")
    ),
    "0xca0e7269600d353f70b14ad118a49575455c0f2f": TokenInfo(
        currency=CurrencyInfo(symbol="AMLT", name="AMLT Network"), scaling=Decimal("1e-18")
    ),
    "0xca1207647ff814039530d7d35df0e1dd2e91fa84": TokenInfo(
        currency=CurrencyInfo(symbol="DHT", name="dHEDGE DAO"), scaling=Decimal("1e-18")
    ),
    "0xca176a8ac234446b2561293db7543e0cdadc6627": TokenInfo(
        currency=CurrencyInfo(symbol="HDW", name="Hardware Chain"), scaling=Decimal("1e-4")
    ),
    "0xca208bfd69ae6d2667f1fcbe681bae12767c0078": TokenInfo(
        currency=CurrencyInfo(symbol="HOMI", name="HOMIHELP"), scaling=Decimal("1e-0")
    ),
    "0xca224dfa3c3b2e44f31b5f4bb2b69be70a0e474e": TokenInfo(
        currency=CurrencyInfo(symbol="GDP", name="Asset GDP Token"), scaling=Decimal("1e-18")
    ),
    "0xca24db399ffc8f33aaefa4926c9de3f58d1da63d": TokenInfo(
        currency=CurrencyInfo(symbol="KTT", name="Kringle Trade Token"), scaling=Decimal("1e-18")
    ),
    "0xca2796f9f61dc7b238aab043971e49c6164df375": TokenInfo(
        currency=CurrencyInfo(symbol="YEED", name="Yggdrash"), scaling=Decimal("1e-18")
    ),
    "0xca29db4221c111888a7e80b12eac8a266da3ee0d": TokenInfo(
        currency=CurrencyInfo(symbol="BLN", name="Bolenum"), scaling=Decimal("1e-18")
    ),
    "0xca3c18a65b802ec267f8f4802545e7f53d24c75e": TokenInfo(
        currency=CurrencyInfo(symbol="BUC", name="BeeunityChain"), scaling=Decimal("1e-18")
    ),
    "0xca3fe04c7ee111f0bbb02c328c699226acf9fd33": TokenInfo(
        currency=CurrencyInfo(symbol="SEEN", name="SEEN"), scaling=Decimal("1e-18")
    ),
    "0xca40fd7471a441a196b9e5d031baf0a8f391313b": TokenInfo(
        currency=CurrencyInfo(symbol="JBL.CX", name="Jabil"), scaling=Decimal("1e-8")
    ),
    "0xca52a83d53f3a0beed391657c0e83b915489fd1c": TokenInfo(
        currency=CurrencyInfo(symbol="ADBE.CX", name="Adobe Systems Inc"), scaling=Decimal("1e-8")
    ),
    "0xca673072ceedc01486e51a5434c3849216445658": TokenInfo(
        currency=CurrencyInfo(symbol="WS30.CX", name="Dow Jones 30"), scaling=Decimal("1e-8")
    ),
    "0xca694eb79ef355ea0999485d211e68f39ae98493": TokenInfo(
        currency=CurrencyInfo(symbol="TAC", name="Traceability Chain"), scaling=Decimal("1e-8")
    ),
    "0xca76baa777d749de63ca044853d22d56bc70bb47": TokenInfo(
        currency=CurrencyInfo(symbol="FFYI", name="Fiscus FYI"), scaling=Decimal("1e-18")
    ),
    "0xcaa05e82bdcba9e25cd1a3bf1afb790c1758943d": TokenInfo(
        currency=CurrencyInfo(symbol="PRC", name="Partner"), scaling=Decimal("1e-8")
    ),
    "0xcaaa93712bdac37f736c323c93d4d5fdefcc31cc": TokenInfo(
        currency=CurrencyInfo(symbol="CRD", name="CRD Network"), scaling=Decimal("1e-18")
    ),
    "0xcaabcaa4ca42e1d86de1a201c818639def0ba7a7": TokenInfo(
        currency=CurrencyInfo(symbol="TALK", name="Talken"), scaling=Decimal("1e-18")
    ),
    "0xcabec58a571979f9fe825885fcb8f7a93892eab0": TokenInfo(
        currency=CurrencyInfo(symbol="UNB", name="United Bull Traders"), scaling=Decimal("1e-18")
    ),
    "0xcac67589df40394c6f658f06a6545166c7ca6768": TokenInfo(
        currency=CurrencyInfo(symbol="MDXT", name="MutualDEXToken"), scaling=Decimal("1e-18")
    ),
    "0xcad2d4c4469ff09ab24d02a63bcedfcd44be0645": TokenInfo(
        currency=CurrencyInfo(symbol="ACPT", name="Crypto Accept"), scaling=Decimal("1e-18")
    ),
    "0xcae72a7a0fd9046cf6b165ca54c9e3a3872109e0": TokenInfo(
        currency=CurrencyInfo(symbol="$ANRX", name="AnRKey X"), scaling=Decimal("1e-18")
    ),
    "0xcafe001067cdef266afb7eb5a286dcfd277f3de5": TokenInfo(
        currency=CurrencyInfo(symbol="PSP", name="ParaSwap"), scaling=Decimal("1e-18")
    ),
    "0xcafe27178308351a12fffffdeb161d9d730da082": TokenInfo(
        currency=CurrencyInfo(symbol="HDS", name="HotDollars Token"), scaling=Decimal("1e-18")
    ),
    "0xcb03bec536843d338ac138205a6689d4cdc11046": TokenInfo(
        currency=CurrencyInfo(symbol="ABPT", name="ABPT Crypto"), scaling=Decimal("1e-18")
    ),
    "0xcb17cd357c7acd594717d899ecb9df540f633f27": TokenInfo(
        currency=CurrencyInfo(symbol="CDL", name="CoinDeal Token"), scaling=Decimal("1e-18")
    ),
    "0xcb1fc914cf9b7ce568ab289ea126707c15e36047": TokenInfo(
        currency=CurrencyInfo(symbol="BIX1901", name="Bibox bond"), scaling=Decimal("1e-18")
    ),
    "0xcb21b60dc7d0ec8341b55adfe2df25db8503a21b": TokenInfo(
        currency=CurrencyInfo(symbol="VOW3.CX", name="Volkswagen AG"), scaling=Decimal("1e-8")
    ),
    "0xcb2fa15f4ea7c55bf6ef9456a662412b137043e9": TokenInfo(
        currency=CurrencyInfo(symbol="PAYOU", name="Payou Finance"), scaling=Decimal("1e-18")
    ),
    "0xcb324e4c8c1561d547c38bd1d4a3b12a405b8019": TokenInfo(
        currency=CurrencyInfo(symbol="PVB", name="Points Value Bank"), scaling=Decimal("1e-18")
    ),
    "0xcb3df3108635932d912632ef7132d03ecfc39080": TokenInfo(
        currency=CurrencyInfo(symbol="WING", name="Wing Shop"), scaling=Decimal("1e-18")
    ),
    "0xcb3f902bf97626391bf8ba87264bbc3dc13469be": TokenInfo(
        currency=CurrencyInfo(symbol="TRC", name="The Real Coin"), scaling=Decimal("1e-18")
    ),
    "0xcb4787bf505a751ec37678e33d2b4fdf491af9d2": TokenInfo(
        currency=CurrencyInfo(symbol="GQC", name="GOLDQR COIN"), scaling=Decimal("1e-18")
    ),
    "0xcb4e8cafeda995da5cedfda5205bd5664a12b848": TokenInfo(
        currency=CurrencyInfo(symbol="KOBE", name="Shabu Shabu"), scaling=Decimal("1e-18")
    ),
    "0xcb529ae44941500ded968baf9617ddecacc6fb87": TokenInfo(
        currency=CurrencyInfo(symbol="MYFIE", name="Monetize Your Selfie"), scaling=Decimal("1e-8")
    ),
    "0xcb554bfb068b54a474a184acd1f743ccd27afe5b": TokenInfo(
        currency=CurrencyInfo(symbol="FXBK", name="FX Buy Back"), scaling=Decimal("1e-2")
    ),
    "0xcb5a05bef3257613e984c17dbcf039952b6d883f": TokenInfo(
        currency=CurrencyInfo(symbol="SGR", name="Sugar Exchange"), scaling=Decimal("1e-8")
    ),
    "0xcb5f72d37685c3d5ad0bb5f982443bc8fcdf570e": TokenInfo(
        currency=CurrencyInfo(symbol="ROOT", name="Rootkit"), scaling=Decimal("1e-18")
    ),
    "0xcb86c6a22cb56b6cf40cafedb06ba0df188a416e": TokenInfo(
        currency=CurrencyInfo(symbol="SURE", name="SURE"), scaling=Decimal("1e-18")
    ),
    "0xcb8d1260f9c92a3a545d409466280ffdd7af7042": TokenInfo(
        currency=CurrencyInfo(symbol="NFT", name="NFT Protocol"), scaling=Decimal("1e-18")
    ),
    "0xcb94be6f13a1182e4a4b6140cb7bf2025d28e41b": TokenInfo(
        currency=CurrencyInfo(symbol="TRST", name="WeTrust"), scaling=Decimal("1e-6")
    ),
    "0xcb97e65f07da24d46bcdd078ebebd7c6e6e3d750": TokenInfo(
        currency=CurrencyInfo(symbol="BTM", name="Bytom"), scaling=Decimal("1e-8")
    ),
    "0xcb98f42221b2c251a4e74a1609722ee09f0cc08e": TokenInfo(
        currency=CurrencyInfo(symbol="IDASH", name="iDASH"), scaling=Decimal("1e-18")
    ),
    "0xcb9a14d68cd0690b3696f42dcfdf609a67824736": TokenInfo(
        currency=CurrencyInfo(symbol="XTT", name="Dr.Xin Health Industry Chain"), scaling=Decimal("1e-18")
    ),
    "0xcba3eae7f55d0f423af43cc85e67ab0fbf87b61c": TokenInfo(
        currency=CurrencyInfo(symbol="SHFT", name="Shyft Network"), scaling=Decimal("1e-18")
    ),
    "0xcba8162778e6a3eba60e1cf7c012b327340bd05d": TokenInfo(
        currency=CurrencyInfo(symbol="SINOC", name="SINOC"), scaling=Decimal("1e-18")
    ),
    "0xcbc1065255cbc3ab41a6868c22d1f1c573ab89fd": TokenInfo(
        currency=CurrencyInfo(symbol="CRETH2", name="Cream ETH 2"), scaling=Decimal("1e-18")
    ),
    "0xcbcc0f036ed4788f63fc0fee32873d6a7487b908": TokenInfo(
        currency=CurrencyInfo(symbol="HMQ", name="Humaniq"), scaling=Decimal("1e-8")
    ),
    "0xcbd55d4ffc43467142761a764763652b48b969ff": TokenInfo(
        currency=CurrencyInfo(symbol="ASTRO", name="AstroTools"), scaling=Decimal("1e-18")
    ),
    "0xcbe3f73c65d13402cbbc2f9db8b6999d5c52982a": TokenInfo(
        currency=CurrencyInfo(symbol="ICSS", name="Infinite Cloud Storage System"), scaling=Decimal("1e-4")
    ),
    "0xcbe79ceca09092648995b2ccdf91ca5ecd1edec9": TokenInfo(
        currency=CurrencyInfo(symbol="BTCSHORT", name="BTCShort"), scaling=Decimal("1e-18")
    ),
    "0xcbeaec699431857fdb4d37addbbdc20e132d4903": TokenInfo(
        currency=CurrencyInfo(symbol="YOYOW", name="YOYOW"), scaling=Decimal("1e-18")
    ),
    "0xcbee6459728019cb1f2bb971dde2ee3271bc7617": TokenInfo(
        currency=CurrencyInfo(symbol="MRG", name="WemergeToken"), scaling=Decimal("1e-18")
    ),
    "0xcbf15fb8246f679f9df0135881cb29a3746f734b": TokenInfo(
        currency=CurrencyInfo(symbol="BTR", name="Bither Platform Token"), scaling=Decimal("1e-18")
    ),
    "0xcbfef8fdd706cde6f208460f2bf39aa9c785f05d": TokenInfo(
        currency=CurrencyInfo(symbol="KINE", name="Kine Protocol"), scaling=Decimal("1e-18")
    ),
    "0xcc12abe4ff81c9378d670de1b57f8e0dd228d77a": TokenInfo(
        currency=CurrencyInfo(symbol="AREN", name="Aave REN"), scaling=Decimal("1e-18")
    ),
    "0xcc13fc627effd6e35d2d2706ea3c4d7396c610ea": TokenInfo(
        currency=CurrencyInfo(symbol="IDXM", name="IDEX Membership"), scaling=Decimal("1e-8")
    ),
    "0xcc26550cb4edfb2b54a514e102e803e58f39cfc7": TokenInfo(
        currency=CurrencyInfo(symbol="SELF", name="SELF TOKEN"), scaling=Decimal("1e-18")
    ),
    "0xcc2a74b28e786fac86be3ca354b1941c25ab3eab": TokenInfo(
        currency=CurrencyInfo(symbol="GBO", name="GABO"), scaling=Decimal("1e-18")
    ),
    "0xcc2ad789f459bc73e5fb33364964b658a62c1ee7": TokenInfo(
        currency=CurrencyInfo(symbol="NIO", name="NioShares"), scaling=Decimal("1e-8")
    ),
    "0xcc33da342f28c4e52c349d6d3ab2d6ecb4969ba2": TokenInfo(
        currency=CurrencyInfo(symbol="KING", name="KINGS Token"), scaling=Decimal("1e-18")
    ),
    "0xcc34366e3842ca1bd36c1f324d15257960fcc801": TokenInfo(
        currency=CurrencyInfo(symbol="BON", name="Bonpay"), scaling=Decimal("1e-18")
    ),
    "0xcc3693c52d4e4ffc1910d90cdd8c52f66bc83262": TokenInfo(
        currency=CurrencyInfo(symbol="GMC", name="Game Chain"), scaling=Decimal("1e-4")
    ),
    "0xcc394f10545aeef24483d2347b32a34a44f20e6f": TokenInfo(
        currency=CurrencyInfo(symbol="VGT", name="Vault Guardian Token"), scaling=Decimal("1e-18")
    ),
    "0xcc4304a31d09258b0029ea7fe63d032f52e44efe": TokenInfo(
        currency=CurrencyInfo(symbol="SWAP", name="Trustswap"), scaling=Decimal("1e-18")
    ),
    "0xcc4ef9eeaf656ac1a2ab886743e98e97e090ed38": TokenInfo(
        currency=CurrencyInfo(symbol="DDF", name="DigitalDevelopersFund"), scaling=Decimal("1e-18")
    ),
    "0xcc6f15be8573cb8243c42d300565566d328213dd": TokenInfo(
        currency=CurrencyInfo(symbol="OWN", name="OWN Token"), scaling=Decimal("1e-18")
    ),
    "0xcc771a11d368a76e6fa34b3aab8227297f48fe41": TokenInfo(
        currency=CurrencyInfo(symbol="DHT", name="Deep Health Chain"), scaling=Decimal("1e-18")
    ),
    "0xcc7ab8d78dba187dc95bf3bb86e65e0c26d0041f": TokenInfo(
        currency=CurrencyInfo(symbol="SPACE", name="SPACELENS"), scaling=Decimal("1e-18")
    ),
    "0xcc7d26d8ea6281bb363c8448515f2c61f7bc19f0": TokenInfo(
        currency=CurrencyInfo(symbol="ABCH", name="ABBC Cash(ABCH)"), scaling=Decimal("1e-18")
    ),
    "0xcc80c051057b774cd75067dc48f8987c4eb97a5e": TokenInfo(
        currency=CurrencyInfo(symbol="NEC", name="Nectar"), scaling=Decimal("1e-18")
    ),
    "0xcc8fa225d80b9c7d42f96e9570156c65d6caaa25": TokenInfo(
        currency=CurrencyInfo(symbol="SLP", name="Smooth Love Potion"), scaling=Decimal("1e-0")
    ),
    "0xcca0c9c383076649604ee31b20248bc04fdf61ca": TokenInfo(
        currency=CurrencyInfo(symbol="ASD", name="AscendEx Token"), scaling=Decimal("1e-18")
    ),
    "0xccade040b89d7865977c0f9cf09bdb897b8f8d40": TokenInfo(
        currency=CurrencyInfo(symbol="IPGO", name="IpgoCoin"), scaling=Decimal("1e-4")
    ),
    "0xccc85aa8999505d6f886a32da4a107bbe0d1de9e": TokenInfo(
        currency=CurrencyInfo(symbol="RPE", name="REPE"), scaling=Decimal("1e-18")
    ),
    "0xccc8cb5229b0ac8069c51fd58367fd1e622afd97": TokenInfo(
        currency=CurrencyInfo(symbol="GODS", name="Gods Unchained"), scaling=Decimal("1e-18")
    ),
    "0xcced5b8288086be8c38e23567e684c3740be4d48": TokenInfo(
        currency=CurrencyInfo(symbol="RLT", name="RouletteToken"), scaling=Decimal("1e-10")
    ),
    "0xccf4429db6322d5c611ee964527d42e5d685dd6a": TokenInfo(
        currency=CurrencyInfo(symbol="CWBTC", name="cWBTC"), scaling=Decimal("1e-8")
    ),
    "0xccf4fe6ac4b53193457e6ead1a2b92e78f4dd8a0": TokenInfo(
        currency=CurrencyInfo(symbol="NIX", name="Nifexcoin"), scaling=Decimal("1e-18")
    ),
    "0xcd1cb16a67937ff8af5d726e2681010ce1e9891a": TokenInfo(
        currency=CurrencyInfo(symbol="MIS", name="Themis"), scaling=Decimal("1e-8")
    ),
    "0xcd1faff6e578fa5cac469d2418c95671ba1a62fe": TokenInfo(
        currency=CurrencyInfo(symbol="XTM", name="Torum"), scaling=Decimal("1e-18")
    ),
    "0xcd23ef2cba177a1b5f5d3818d055868e4b599d18": TokenInfo(
        currency=CurrencyInfo(symbol="MM", name="Moon Money Chain"), scaling=Decimal("1e-18")
    ),
    "0xcd254568ebf88f088e40f456db9e17731243cb25": TokenInfo(
        currency=CurrencyInfo(symbol="YFOS", name="YFOS.finance"), scaling=Decimal("1e-18")
    ),
    "0xcd2828fc4d8e8a0ede91bb38cf64b1a81de65bf6": TokenInfo(
        currency=CurrencyInfo(symbol="ODDZ", name="Oddz"), scaling=Decimal("1e-18")
    ),
    "0xcd3673af09e76c74d889aabab68ca0645566a3a1": TokenInfo(
        currency=CurrencyInfo(symbol="CANDY", name="UnicornGo Candy"), scaling=Decimal("1e-18")
    ),
    "0xcd453276f4db9c38855056a036c4a99a8cac7b8d": TokenInfo(
        currency=CurrencyInfo(symbol="YKZ", name="Yakuza DAO"), scaling=Decimal("1e-18")
    ),
    "0xcd475371e39c0d94e82fccc9dd0ea710d0dc0c0b": TokenInfo(
        currency=CurrencyInfo(symbol="TCH", name="THECASH"), scaling=Decimal("1e-18")
    ),
    "0xcd4b4b0f3284a33ac49c67961ec6e111708318cf": TokenInfo(
        currency=CurrencyInfo(symbol="AX1", name="AX1 Mining token"), scaling=Decimal("1e-5")
    ),
    "0xcd56fc21564fba45c17d0bf663cced37f5e22d7e": TokenInfo(
        currency=CurrencyInfo(symbol="JPX", name="Japan Excitement Coin"), scaling=Decimal("1e-4")
    ),
    "0xcd62b1c403fa761baadfc74c525ce2b51780b184": TokenInfo(
        currency=CurrencyInfo(symbol="ANJ", name="Aragon Court"), scaling=Decimal("1e-18")
    ),
    "0xcd64aa18ddbce84411adbfe6da49354ba5187a45": TokenInfo(
        currency=CurrencyInfo(symbol="KBOT", name="Korbot"), scaling=Decimal("1e-8")
    ),
    "0xcd7492db29e2ab436e819b249452ee1bbdf52214": TokenInfo(
        currency=CurrencyInfo(symbol="SMI", name="SafeMoon Inu"), scaling=Decimal("1e-8")
    ),
    "0xcd8d927f2cb03d2efb7f96ceb66ec4976843e012": TokenInfo(
        currency=CurrencyInfo(symbol="ITRX", name="iTRX"), scaling=Decimal("1e-18")
    ),
    "0xcda4377806cb09f226aa4840a9df8b5c2b7744ec": TokenInfo(
        currency=CurrencyInfo(symbol="UST", name="Uservice"), scaling=Decimal("1e-18")
    ),
    "0xcdb7ecfd3403eef3882c65b761ef9b5054890a47": TokenInfo(
        currency=CurrencyInfo(symbol="HUR", name="Hurify"), scaling=Decimal("1e-18")
    ),
    "0xcdcfc0f66c522fd086a1b725ea3c0eeb9f9e8814": TokenInfo(
        currency=CurrencyInfo(symbol="AURA", name="Aurora DAO"), scaling=Decimal("1e-18")
    ),
    "0xcdd0a6b15b49a9eb3ce011cce22fac2ccf09ece6": TokenInfo(
        currency=CurrencyInfo(symbol="TARM", name="ARMTOKEN"), scaling=Decimal("1e-18")
    ),
    "0xcddb1bceb7a1979c6caa0229820707429dd3ec6c": TokenInfo(
        currency=CurrencyInfo(symbol="idleUSDCSafe", name="IdleUSDC v3 [Risk adjusted]"), scaling=Decimal("1e-18")
    ),
    "0xcde3ef6cacf84ad36d8a6eccc964f25351296d36": TokenInfo(
        currency=CurrencyInfo(symbol="BTCG", name="Bitcoin Galaxy"), scaling=Decimal("1e-8")
    ),
    "0xcdeee767bed58c5325f68500115d4b722b3724ee": TokenInfo(
        currency=CurrencyInfo(symbol="CRBN", name="Carbon"), scaling=Decimal("1e-18")
    ),
    "0xce13abce0db5a8224616ef24d3979d466f19cf90": TokenInfo(
        currency=CurrencyInfo(symbol="KEYT", name="Rebit"), scaling=Decimal("1e-18")
    ),
    "0xce25b4271cc4d937a7d9bf75b2068a7892b9961d": TokenInfo(
        currency=CurrencyInfo(symbol="UPP", name="Unipump"), scaling=Decimal("1e-18")
    ),
    "0xce27a2388d2ba7a9995fa0960fb168568e2a7923": TokenInfo(
        currency=CurrencyInfo(symbol="CNR", name="Cinder"), scaling=Decimal("1e-18")
    ),
    "0xce49c3c92b33a1653f34811a9d7e34502bf12b89": TokenInfo(
        currency=CurrencyInfo(symbol="BSVBEAR", name="3X Short Bitcoin SV Token"), scaling=Decimal("1e-18")
    ),
    "0xce5114d7fa8361f0c088ee26fa3a5446c4a1f50b": TokenInfo(
        currency=CurrencyInfo(symbol="BWX", name="Blue Whale"), scaling=Decimal("1e-18")
    ),
    "0xce593a29905951e8fc579bc092eca72577da575c": TokenInfo(
        currency=CurrencyInfo(symbol="GR", name="GROM"), scaling=Decimal("1e-6")
    ),
    "0xce59d29b09aae565feeef8e52f47c3cd5368c663": TokenInfo(
        currency=CurrencyInfo(symbol="BLX", name="BLX"), scaling=Decimal("1e-18")
    ),
    "0xce5c603c78d047ef43032e96b5b785324f753a4f": TokenInfo(
        currency=CurrencyInfo(symbol="E4ROW", name="E4ROW"), scaling=Decimal("1e-2")
    ),
    "0xce833222051740aa5427d089a46ff3918763107f": TokenInfo(
        currency=CurrencyInfo(symbol="PAMP", name="Pamp Network"), scaling=Decimal("1e-18")
    ),
    "0xcec2387e04f9815bf12670dbf6cf03bba26df25f": TokenInfo(
        currency=CurrencyInfo(symbol="YFILD", name="YFILEND.FINANCE"), scaling=Decimal("1e-18")
    ),
    "0xcec38306558a31cdbb2a9d6285947c5b44a24f3e": TokenInfo(
        currency=CurrencyInfo(symbol="DFS", name="Fantasy Sports"), scaling=Decimal("1e-18")
    ),
    "0xced4e93198734ddaff8492d525bd258d49eb388e": TokenInfo(
        currency=CurrencyInfo(symbol="EDO", name="Eidoo"), scaling=Decimal("1e-18")
    ),
    "0xcee1d3c3a02267e37e6b373060f79d5d7b9e1669": TokenInfo(
        currency=CurrencyInfo(symbol="YFFI", name="yffi finance"), scaling=Decimal("1e-18")
    ),
    "0xcee4019fd41ecdc8bae9efdd20510f4b6faa6197": TokenInfo(
        currency=CurrencyInfo(symbol="NLYA", name="Nollya Coin"), scaling=Decimal("1e-18")
    ),
    "0xcef46305d096fa876dd23048bf80f9345282e3fc": TokenInfo(
        currency=CurrencyInfo(symbol="CBU", name="Banque Universal"), scaling=Decimal("1e-0")
    ),
    "0xcf0c122c6b73ff809c693db761e7baebe62b6a2e": TokenInfo(
        currency=CurrencyInfo(symbol="FLOKI", name="Floki Inu"), scaling=Decimal("1e-9")
    ),
    "0xcf282ba0bc91d2aa6e775bcfd90da6b7912f1b1a": TokenInfo(
        currency=CurrencyInfo(symbol="YEFI", name="Yearn Ethereum Finance"), scaling=Decimal("1e-18")
    ),
    "0xcf28bf20b662f746a4b487fa81de5a40ac0af49c": TokenInfo(
        currency=CurrencyInfo(symbol="XGR", name="GoldReserve"), scaling=Decimal("1e-8")
    ),
    "0xcf2f184b317573103b19e9d0c0204c841d70fe04": TokenInfo(
        currency=CurrencyInfo(symbol="PRO", name="Pro School Token"), scaling=Decimal("1e-18")
    ),
    "0xcf3c8be2e2c42331da80ef210e9b1b307c03d36a": TokenInfo(
        currency=CurrencyInfo(symbol="BEPRO", name="BEPRO Network"), scaling=Decimal("1e-18")
    ),
    "0xcf42de80d80edc4a8d56e4e840b5ff0dc84aaa17": TokenInfo(
        currency=CurrencyInfo(symbol="RSP", name="Real-estate Sales Platform"), scaling=Decimal("1e-18")
    ),
    "0xcf55a7f92d5e0c6683debbc1fc20c0a6e056df13": TokenInfo(
        currency=CurrencyInfo(symbol="ZELDA ELASTIC CASH", name="Zelda Elastic Cash"), scaling=Decimal("1e-18")
    ),
    "0xcf58e894042c41a72fbb3b57811b11f987e19741": TokenInfo(
        currency=CurrencyInfo(symbol="R.CX", name="Ryder System"), scaling=Decimal("1e-8")
    ),
    "0xcf5a08af322e52bee93861341f7bd90eb3d65aa3": TokenInfo(
        currency=CurrencyInfo(symbol="HLTC", name="HeavyLitecoin"), scaling=Decimal("1e-18")
    ),
    "0xcf8048b2d336c569a3985bd93cbb91b758ded178": TokenInfo(
        currency=CurrencyInfo(symbol="IZE", name="IZE Fintech Blockchain"), scaling=Decimal("1e-18")
    ),
    "0xcf8f9555d55ce45a3a33a81d6ef99a2a2e71dee2": TokenInfo(
        currency=CurrencyInfo(symbol="CBIX7", name="CBI Index 7"), scaling=Decimal("1e-18")
    ),
    "0xcf9c692f7e62af3c571d4173fd4abf9a3e5330d0": TokenInfo(
        currency=CurrencyInfo(symbol="ONIGIRI", name="Onigiri"), scaling=Decimal("1e-18")
    ),
    "0xcfa0885131f602d11d4da248d2c65a62063567a9": TokenInfo(
        currency=CurrencyInfo(symbol="TORG", name="TORG"), scaling=Decimal("1e-18")
    ),
    "0xcfad57a67689809cda997f655802a119838c9cec": TokenInfo(
        currency=CurrencyInfo(symbol="BSC", name="Benscoin"), scaling=Decimal("1e-7")
    ),
    "0xcfb98637bcae43c13323eaa1731ced2b716962fd": TokenInfo(
        currency=CurrencyInfo(symbol="NET", name="Nimiq Exchange Token"), scaling=Decimal("1e-18")
    ),
    "0xcfbf70e33d5163e25b0dad73955c1bd9e8cd8ba2": TokenInfo(
        currency=CurrencyInfo(symbol="WNL", name="WinStars Live"), scaling=Decimal("1e-18")
    ),
    "0xcfc2437916a6df165235272dbfb116687bb1a00b": TokenInfo(
        currency=CurrencyInfo(symbol="PLCN", name="PlusCoin"), scaling=Decimal("1e-18")
    ),
    "0xcfcd67348e28d202bd01b94214a1b366a35ce27b": TokenInfo(
        currency=CurrencyInfo(symbol="EDF.CX", name="Edf"), scaling=Decimal("1e-8")
    ),
    "0xcfcecfe2bd2fed07a9145222e8a7ad9cf1ccd22a": TokenInfo(
        currency=CurrencyInfo(symbol="ADS", name="Adshares"), scaling=Decimal("1e-11")
    ),
    "0xcfd6ae8bf13f42de14867351eaff7a8a3b9fbbe7": TokenInfo(
        currency=CurrencyInfo(symbol="SNG", name="Sinergia"), scaling=Decimal("1e-8")
    ),
    "0xcfe4f03c3afbb9857b29fc706180bf0044900d59": TokenInfo(
        currency=CurrencyInfo(symbol="GOLDR", name="Golden Ratio Coin"), scaling=Decimal("1e-8")
    ),
    "0xcfeb09c3c5f0f78ad72166d55f9e6e9a60e96eec": TokenInfo(
        currency=CurrencyInfo(symbol="VEMP", name="vEmpire DDAO"), scaling=Decimal("1e-18")
    ),
    "0xcfeb236743bd4b3789d28bbea9dc4ef0792c87f9": TokenInfo(
        currency=CurrencyInfo(symbol="LEOMOON", name="10X Long LEO Token"), scaling=Decimal("1e-18")
    ),
    "0xcfee207a9a4e2ed5027c5830b2611f1944899130": TokenInfo(
        currency=CurrencyInfo(symbol="EMN.CX", name="Eastman Chemical"), scaling=Decimal("1e-8")
    ),
    "0xcff20ce22e71ecf2ea89c86ecbd4a3cf513768c7": TokenInfo(
        currency=CurrencyInfo(symbol="MKS", name="Makes"), scaling=Decimal("1e-6")
    ),
    "0xd01409314acb3b245cea9500ece3f6fd4d70ea30": TokenInfo(
        currency=CurrencyInfo(symbol="LTO", name="LTO Network"), scaling=Decimal("1e-8")
    ),
    "0xd01db73e047855efb414e6202098c4be4cd2423b": TokenInfo(
        currency=CurrencyInfo(symbol="UQC", name="Uquid Coin"), scaling=Decimal("1e-18")
    ),
    "0xd0345d30fd918d7682398acbcdf139c808998709": TokenInfo(
        currency=CurrencyInfo(symbol="LIX", name="Lixir Finance"), scaling=Decimal("1e-18")
    ),
    "0xd0352a019e9ab9d757776f532377aaebd36fd541": TokenInfo(
        currency=CurrencyInfo(symbol="FSN", name="Fusion Token"), scaling=Decimal("1e-18")
    ),
    "0xd03b6ae96cae26b743a6207dcee7cbe60a425c70": TokenInfo(
        currency=CurrencyInfo(symbol="UNDB", name="UniDexBot"), scaling=Decimal("1e-18")
    ),
    "0xd04785c4d8195e4a54d9dec3a9043872875ae9e2": TokenInfo(
        currency=CurrencyInfo(symbol="ROT", name="Rotten"), scaling=Decimal("1e-18")
    ),
    "0xd059c8a4c7f53c4352d933b059349ba492294ac9": TokenInfo(
        currency=CurrencyInfo(symbol="AAPL", name="Apple Protocol Token"), scaling=Decimal("1e-18")
    ),
    "0xd0658324074d6249a51876438916f7c423075451": TokenInfo(
        currency=CurrencyInfo(symbol="YLAND", name="Yearn Land"), scaling=Decimal("1e-18")
    ),
    "0xd0660cd418a64a1d44e9214ad8e459324d8157f1": TokenInfo(
        currency=CurrencyInfo(symbol="WOOFY", name="Woofy"), scaling=Decimal("1e-12")
    ),
    "0xd06b25f67a17f12b41f615b34d87ecd716ff55a0": TokenInfo(
        currency=CurrencyInfo(symbol="BULLSHIT", name="3X Long Shitcoin Index Token"), scaling=Decimal("1e-18")
    ),
    "0xd07d9fe2d2cc067015e2b4917d24933804f42cfa": TokenInfo(
        currency=CurrencyInfo(symbol="TOL", name="Tolar"), scaling=Decimal("1e-18")
    ),
    "0xd084944d3c05cd115c09d072b9f44ba3e0e45921": TokenInfo(
        currency=CurrencyInfo(symbol="FOLD", name="Manifold Finance"), scaling=Decimal("1e-18")
    ),
    "0xd084b83c305dafd76ae3e1b4e1f1fe2ecccb3988": TokenInfo(
        currency=CurrencyInfo(symbol="TVK", name="Terra Virtua Kolect"), scaling=Decimal("1e-18")
    ),
    "0xd0929d411954c47438dc1d871dd6081f5c5e149c": TokenInfo(
        currency=CurrencyInfo(symbol="RFR", name="Refereum"), scaling=Decimal("1e-4")
    ),
    "0xd0943ff6a36b421189d2af4a03bd53d31f55a624": TokenInfo(
        currency=CurrencyInfo(symbol="GT.CX", name="The Goodyear Tire & Rubber Company"), scaling=Decimal("1e-8")
    ),
    "0xd0a4b8946cb52f0661273bfbc6fd0e0c75fc6433": TokenInfo(
        currency=CurrencyInfo(symbol="STORM", name="Storm Token"), scaling=Decimal("1e-18")
    ),
    "0xd0c59798f986d333554688cd667033d469c2398e": TokenInfo(
        currency=CurrencyInfo(symbol="YMEN", name="Ymen.Finance"), scaling=Decimal("1e-18")
    ),
    "0xd0c64d6c0e9aa53fffd8b80313e035f7b83083f3": TokenInfo(
        currency=CurrencyInfo(symbol="LTCHEDGE", name="1X Short Litecoin Token"), scaling=Decimal("1e-18")
    ),
    "0xd0cb75298d5c1e3b277e3cd95c56b3caa81a99d3": TokenInfo(
        currency=CurrencyInfo(symbol="HDT", name="HDT"), scaling=Decimal("1e-8")
    ),
    "0xd0d6d6c5fe4a677d343cc433536bb717bae167dd": TokenInfo(
        currency=CurrencyInfo(symbol="ADT", name="adToken"), scaling=Decimal("1e-9")
    ),
    "0xd0df51cec800d1f8045722377f6faceba8d15a4d": TokenInfo(
        currency=CurrencyInfo(symbol="THS", name="TheHashSpeed"), scaling=Decimal("1e-18")
    ),
    "0xd0f05d3d4e4d1243ac826d8c6171180c58eaa9bc": TokenInfo(
        currency=CurrencyInfo(symbol="VNTW", name="Value Network Token"), scaling=Decimal("1e-18")
    ),
    "0xd13c7342e1ef687c5ad21b27c2b65d772cab5c8c": TokenInfo(
        currency=CurrencyInfo(symbol="UOS", name="Ultra"), scaling=Decimal("1e-4")
    ),
    "0xd15ecdcf5ea68e3995b2d0527a0ae0a3258302f8": TokenInfo(
        currency=CurrencyInfo(symbol="MCX", name="Machi X"), scaling=Decimal("1e-18")
    ),
    "0xd1632efa392925089785b43410c529f8959a8d9a": TokenInfo(
        currency=CurrencyInfo(symbol="RLD", name="Real Land"), scaling=Decimal("1e-8")
    ),
    "0xd16c79c8a39d44b2f3eb45d2019cd6a42b03e2a9": TokenInfo(
        currency=CurrencyInfo(symbol="UUSDWETH-DEC", name="uUSDwETH Synthetic Token Expiring 31 December 2020"),
        scaling=Decimal("1e-18"),
    ),
    "0xd1766a85b0d6f81185782dc07f15326d63c3cbaa": TokenInfo(
        currency=CurrencyInfo(symbol="TUBER", name="TokenTuber"), scaling=Decimal("1e-18")
    ),
    "0xd17f8c64635e189f3ca1ca3a16b33e841bf53427": TokenInfo(
        currency=CurrencyInfo(symbol="UPA", name="Unitopia"), scaling=Decimal("1e-2")
    ),
    "0xd1d3b662d91faaa4a5d809d804fa70550b2b3e9c": TokenInfo(
        currency=CurrencyInfo(symbol="PETC", name="Petcoin"), scaling=Decimal("1e-18")
    ),
    "0xd1e10c37a27d95d95720291b1dc6f12f74c71443": TokenInfo(
        currency=CurrencyInfo(symbol="COSM", name="Cosmo Coin"), scaling=Decimal("1e-18")
    ),
    "0xd1e4deb6d4cee49e4c721aaba13c7d6b4a12ce73": TokenInfo(
        currency=CurrencyInfo(symbol="NKTR.CX", name="Nektar Therapeutics"), scaling=Decimal("1e-8")
    ),
    "0xd1ef44d439a885a867732db280d233213ef54c2b": TokenInfo(
        currency=CurrencyInfo(symbol="SLUSD", name="Silisius USD"), scaling=Decimal("1e-6")
    ),
    "0xd1ef9a7310d0806855c672288ef5a1bab62cef33": TokenInfo(
        currency=CurrencyInfo(symbol="BLVR", name="BELIEVER"), scaling=Decimal("1e-18")
    ),
    "0xd1f579cc0a5405d7610346b371371bed1528d18b": TokenInfo(
        currency=CurrencyInfo(symbol="IMG", name="SAHARA"), scaling=Decimal("1e-18")
    ),
    "0xd20bcbd56d9d551cac10a6bc2a83635bfb72f3f4": TokenInfo(
        currency=CurrencyInfo(symbol="FUND", name="FUNDChains"), scaling=Decimal("1e-6")
    ),
    "0xd218d75ba0fc45858a4e9ef57a257ed9977db5f4": TokenInfo(
        currency=CurrencyInfo(symbol="BTCUSDCTA", name="BTC TA Set II"), scaling=Decimal("1e-18")
    ),
    "0xd2299b3098cf5e13144caebfdad61ebe505233dc": TokenInfo(
        currency=CurrencyInfo(symbol="AO", name="AurumOx"), scaling=Decimal("1e-18")
    ),
    "0xd233d1f6fd11640081abb8db125f722b5dc729dc": TokenInfo(
        currency=CurrencyInfo(symbol="USD", name="Dollars"), scaling=Decimal("1e-9")
    ),
    "0xd234bf2410a0009df9c3c63b610c09738f18ccd7": TokenInfo(
        currency=CurrencyInfo(symbol="DTR", name="Dynamic Trading Rights"), scaling=Decimal("1e-8")
    ),
    "0xd23ac27148af6a2f339bd82d0e3cff380b5093de": TokenInfo(
        currency=CurrencyInfo(symbol="SI", name="Siren"), scaling=Decimal("1e-18")
    ),
    "0xd241d7b5cb0ef9fc79d9e4eb9e21f5e209f52f7d": TokenInfo(
        currency=CurrencyInfo(symbol="HOO", name="Hoo Token"), scaling=Decimal("1e-8")
    ),
    "0xd248b0d48e44aaf9c49aea0312be7e13a6dc1468": TokenInfo(
        currency=CurrencyInfo(symbol="SGT", name="Status Genesis Token"), scaling=Decimal("1e-1")
    ),
    "0xd24946147829deaa935be2ad85a3291dbf109c80": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUSDC", name="Aave AMM USDC"), scaling=Decimal("1e-6")
    ),
    "0xd24e56f02ee723a443575836b9668587ffd6204f": TokenInfo(
        currency=CurrencyInfo(symbol="BCG", name="BCG Chain"), scaling=Decimal("1e-18")
    ),
    "0xd26114cd6ee289accf82350c8d8487fedb8a0c07": TokenInfo(
        currency=CurrencyInfo(symbol="OMG", name="OMG Network"), scaling=Decimal("1e-18")
    ),
    "0xd265f1ab53be1eebdf55a0a6e6f2ca3af86b1778": TokenInfo(
        currency=CurrencyInfo(symbol="GZB", name="Gzclub Token"), scaling=Decimal("1e-6")
    ),
    "0xd26a9c3437f7d121098c8c05c7413f5cc70bb070": TokenInfo(
        currency=CurrencyInfo(symbol="AZUM", name="Azuma Coin"), scaling=Decimal("1e-18")
    ),
    "0xd26fb114401ec86887cd09f62eccd95fcf20b571": TokenInfo(
        currency=CurrencyInfo(symbol="BCP", name="Bitcoin Platinums"), scaling=Decimal("1e-8")
    ),
    "0xd27d76a1ba55ce5c0291ccd04febbe793d22ebf4": TokenInfo(
        currency=CurrencyInfo(symbol="BNP", name="BenePit"), scaling=Decimal("1e-18")
    ),
    "0xd28807d7ef028af6728d12ccd621b2242da2a64f": TokenInfo(
        currency=CurrencyInfo(symbol="GMX", name="Global Monetary Transfer"), scaling=Decimal("1e-18")
    ),
    "0xd28cfec79db8d0a225767d06140aee280718ab7e": TokenInfo(
        currency=CurrencyInfo(symbol="BZKY", name="Bizkey"), scaling=Decimal("1e-16")
    ),
    "0xd291e7a03283640fdc51b121ac401383a46cc623": TokenInfo(
        currency=CurrencyInfo(symbol="RGT", name="Rari Governance Token"), scaling=Decimal("1e-18")
    ),
    "0xd2946be786f35c3cc402c29b323647abda799071": TokenInfo(
        currency=CurrencyInfo(symbol="VIKKY", name="VikkyToken"), scaling=Decimal("1e-8")
    ),
    "0xd29f0b5b3f50b07fe9a9511f7d86f4f4bac3f8c4": TokenInfo(
        currency=CurrencyInfo(symbol="LQD", name="Liquidity Network"), scaling=Decimal("1e-18")
    ),
    "0xd29fa4b8cc936a68bb560b19eed969ebfdbaa565": TokenInfo(
        currency=CurrencyInfo(symbol="ACW", name="Ace Wins"), scaling=Decimal("1e-10")
    ),
    "0xd2ae2619ed65bfe3a421f1f250f21e899f0dc086": TokenInfo(
        currency=CurrencyInfo(symbol="NL25.CX", name="Amsterdam Exchange Index 25"), scaling=Decimal("1e-8")
    ),
    "0xd2bb16cf38ca086cab5128d5c25de9477ebd596b": TokenInfo(
        currency=CurrencyInfo(symbol="XCT", name="xCrypt Token"), scaling=Decimal("1e-18")
    ),
    "0xd2d01dd6aa7a2f5228c7c17298905a7c7e1dfe81": TokenInfo(
        currency=CurrencyInfo(symbol="OUSD", name="Onyx USD"), scaling=Decimal("1e-18")
    ),
    "0xd2d6158683aee4cc838067727209a0aaf4359de3": TokenInfo(
        currency=CurrencyInfo(symbol="BNTY", name="Bounty0x"), scaling=Decimal("1e-18")
    ),
    "0xd2dda223b2617cb616c1580db421e4cfae6a8a85": TokenInfo(
        currency=CurrencyInfo(symbol="BONDLY", name="Bondly"), scaling=Decimal("1e-18")
    ),
    "0xd2fa8f92ea72abb35dbd6deca57173d22db2ba49": TokenInfo(
        currency=CurrencyInfo(symbol="ORI", name="Origami Network"), scaling=Decimal("1e-18")
    ),
    "0xd3003b3778bf4887e73eb320b71a04728961505c": TokenInfo(
        currency=CurrencyInfo(symbol="TEEN", name="MyTeenCoin"), scaling=Decimal("1e-18")
    ),
    "0xd30a2e9347ad48ea208ee563a9cdfd80e962a727": TokenInfo(
        currency=CurrencyInfo(symbol="RYLT", name="RoyaltyCOIN"), scaling=Decimal("1e-18")
    ),
    "0xd31695a1d35e489252ce57b129fd4b1b05e6acac": TokenInfo(
        currency=CurrencyInfo(symbol="TKP", name="TOKPIE"), scaling=Decimal("1e-18")
    ),
    "0xd31a9d28d66a1f7e62b5565416ea14607690f788": TokenInfo(
        currency=CurrencyInfo(symbol="HCUT", name="HealthChainUS"), scaling=Decimal("1e-18")
    ),
    "0xd321ca7cd7a233483b8cd5a11a89e9337e70df84": TokenInfo(
        currency=CurrencyInfo(symbol="VI", name="VI"), scaling=Decimal("1e-18")
    ),
    "0xd32641191578ea9b208125ddd4ec5e7b84fcab4c": TokenInfo(
        currency=CurrencyInfo(symbol="TMED", name="MDsquare"), scaling=Decimal("1e-18")
    ),
    "0xd33526068d116ce69f19a9ee46f0bd304f21a51f": TokenInfo(
        currency=CurrencyInfo(symbol="RPL", name="Rocket Pool"), scaling=Decimal("1e-18")
    ),
    "0xd341d1680eeee3255b8c4c75bcce7eb57f144dae": TokenInfo(
        currency=CurrencyInfo(symbol="ONG", name="SoMee.Social [OLD]"), scaling=Decimal("1e-18")
    ),
    "0xd348e07a2806505b856123045d27aeed90924b50": TokenInfo(
        currency=CurrencyInfo(symbol="CCLC", name="Christ Coin"), scaling=Decimal("1e-8")
    ),
    "0xd35833f9255fb28cc6b91acb8a66ba6429d6ef5a": TokenInfo(
        currency=CurrencyInfo(symbol="HYPX", name="HYPNOXYS"), scaling=Decimal("1e-18")
    ),
    "0xd36932143f6ebdedd872d5fb0651f4b72fd15a84": TokenInfo(
        currency=CurrencyInfo(symbol="MAAPL", name="Mirrored Apple"), scaling=Decimal("1e-18")
    ),
    "0xd36a0e7b741542208ae0fbb35453c893d0136625": TokenInfo(
        currency=CurrencyInfo(symbol="IUT", name="ITO Utility Token"), scaling=Decimal("1e-0")
    ),
    "0xd375eed3549cbc8243358ef3bd6026e2c2dc8e53": TokenInfo(
        currency=CurrencyInfo(symbol="CSCJ", name="CSC JACKPOT"), scaling=Decimal("1e-9")
    ),
    "0xd379700999f4805ce80aa32db46a94df64561108": TokenInfo(
        currency=CurrencyInfo(symbol="DETS", name="Dextrust"), scaling=Decimal("1e-18")
    ),
    "0xd37ee7e4f452c6638c96536e68090de8cbcdb583": TokenInfo(
        currency=CurrencyInfo(symbol="AGUSD", name="Aave GUSD"), scaling=Decimal("1e-2")
    ),
    "0xd387f0e62e3f123a54ae486056a5d859affed0c8": TokenInfo(
        currency=CurrencyInfo(symbol="YETH", name="Fyeth.finance"), scaling=Decimal("1e-18")
    ),
    "0xd38bb40815d2b0c2d2c866e0c72c5728ffc76dd9": TokenInfo(
        currency=CurrencyInfo(symbol="SIS", name="Symbiosis Finance"), scaling=Decimal("1e-18")
    ),
    "0xd3c00772b24d997a812249ca637a921e81357701": TokenInfo(
        currency=CurrencyInfo(symbol="WILD", name="Wild Crypto"), scaling=Decimal("1e-18")
    ),
    "0xd3c51de3e6dd9b53d7f37699afb3ee3bf9b9b3f4": TokenInfo(
        currency=CurrencyInfo(symbol="MCONTENT", name="MContent"), scaling=Decimal("1e-6")
    ),
    "0xd3cdc4e75750dc1e59f8342200742b6b29490e70": TokenInfo(
        currency=CurrencyInfo(symbol="ECU", name="Decurian"), scaling=Decimal("1e-3")
    ),
    "0xd3e41fd8bbcd3d512119608cf4a687a1fda9807d": TokenInfo(
        currency=CurrencyInfo(symbol="KPW", name="Kapow"), scaling=Decimal("1e-8")
    ),
    "0xd3e4ba569045546d09cf021ecc5dfe42b1d7f6e4": TokenInfo(
        currency=CurrencyInfo(symbol="MNW", name="Morpheus Network"), scaling=Decimal("1e-18")
    ),
    "0xd3e7e71d20403a6d0bead558c0bf19452a3fd002": TokenInfo(
        currency=CurrencyInfo(symbol="EOTO", name="Everyonetoken"), scaling=Decimal("1e-18")
    ),
    "0xd3e8695d2bef061eab38b5ef526c0f714108119c": TokenInfo(
        currency=CurrencyInfo(symbol="YFIVE", name="YFIVE FINANCE"), scaling=Decimal("1e-18")
    ),
    "0xd3ec111e4e33c0a1c32e3ad0be976214d30dc37e": TokenInfo(
        currency=CurrencyInfo(symbol="UMC", name="Universal Marketing Coin"), scaling=Decimal("1e-18")
    ),
    "0xd3f04e421771e92a5026affdda5aba80952917a0": TokenInfo(
        currency=CurrencyInfo(symbol="RF", name="Raido Token"), scaling=Decimal("1e-8")
    ),
    "0xd3f89750010eae391d2e40e3b3f9d638c7635279": TokenInfo(
        currency=CurrencyInfo(symbol="SKE", name="Skeyer Chain"), scaling=Decimal("1e-18")
    ),
    "0xd3fb5cabd07c85395667f83d20b080642bde66c7": TokenInfo(
        currency=CurrencyInfo(symbol="AMR", name="Ammbr"), scaling=Decimal("1e-16")
    ),
    "0xd4078bdb652610ad5383a747d130cbe905911102": TokenInfo(
        currency=CurrencyInfo(symbol="VAI", name="Viola.AI"), scaling=Decimal("1e-18")
    ),
    "0xd40adff097e3cde2b96d81a4727f3e47093f3405": TokenInfo(
        currency=CurrencyInfo(symbol="YFIAG", name="YearnAgnostic"), scaling=Decimal("1e-18")
    ),
    "0xd417144312dbf50465b1c641d016962017ef6240": TokenInfo(
        currency=CurrencyInfo(symbol="CQT", name="Covalent"), scaling=Decimal("1e-18")
    ),
    "0xd42debe4edc92bd5a3fbb4243e1eccf6d63a4a5d": TokenInfo(
        currency=CurrencyInfo(symbol="C8", name="Carboneum"), scaling=Decimal("1e-18")
    ),
    "0xd433138d12beb9929ff6fd583dc83663eea6aaa5": TokenInfo(
        currency=CurrencyInfo(symbol="BTR", name="Bitrue Coin"), scaling=Decimal("1e-18")
    ),
    "0xd44bb6663936cab1310584a277f7daa6943d4904": TokenInfo(
        currency=CurrencyInfo(symbol="WCO", name="Winco"), scaling=Decimal("1e-8")
    ),
    "0xd45247c07379d94904e0a87b4481f0a1ddfa0c64": TokenInfo(
        currency=CurrencyInfo(symbol="BCZERO", name="Buggyra Coin Zero"), scaling=Decimal("1e-18")
    ),
    "0xd46ba6d942050d489dbd938a2c909a5d5039a161": TokenInfo(
        currency=CurrencyInfo(symbol="AMPL", name="Ampleforth"), scaling=Decimal("1e-9")
    ),
    "0xd46df541148932690b81092f600f35208afd4325": TokenInfo(
        currency=CurrencyInfo(symbol="PRISM", name="Prism Network"), scaling=Decimal("1e-18")
    ),
    "0xd478161c952357f05f0292b56012cd8457f1cfbf": TokenInfo(
        currency=CurrencyInfo(symbol="POLK", name="Polkamarkets"), scaling=Decimal("1e-18")
    ),
    "0xd49ff13661451313ca1553fd6954bd1d9b6e02b9": TokenInfo(
        currency=CurrencyInfo(symbol="ELEC", name="Electrify.Asia"), scaling=Decimal("1e-18")
    ),
    "0xd4a8c8cafd223e372c8a217fd201f9e11e440b85": TokenInfo(
        currency=CurrencyInfo(symbol="SPXM.CX", name="S&P 500"), scaling=Decimal("1e-8")
    ),
    "0xd4c435f5b09f855c3317c8524cb1f586e42795fa": TokenInfo(
        currency=CurrencyInfo(symbol="CND", name="Cindicator"), scaling=Decimal("1e-18")
    ),
    "0xd4ca5c2aff1eefb0bea9e9eab16f88db2990c183": TokenInfo(
        currency=CurrencyInfo(symbol="XRPC", name="XRP Classic"), scaling=Decimal("1e-8")
    ),
    "0xd4cdd5e54ccedda7e9408b31759c9f9ceecbb3ec": TokenInfo(
        currency=CurrencyInfo(symbol="HD", name="HARDCORE"), scaling=Decimal("1e-2")
    ),
    "0xd4dd48fa7eca5cde1b31f780774c9563186f91c0": TokenInfo(
        currency=CurrencyInfo(symbol="SELF", name="Self Token"), scaling=Decimal("1e-18")
    ),
    "0xd4f6f9ae14399fd5eb8dfc7725f0094a1a7f5d80": TokenInfo(
        currency=CurrencyInfo(symbol="BST", name="Bitsten Token"), scaling=Decimal("1e-18")
    ),
    "0xd4fa1460f537bb9085d22c7bccb5dd450ef28e3a": TokenInfo(
        currency=CurrencyInfo(symbol="PPT", name="Populous"), scaling=Decimal("1e-8")
    ),
    "0xd4fb1706ae549febec06bb7175b08010dd1b0c2e": TokenInfo(
        currency=CurrencyInfo(symbol="iETH", name="Synth iETH"), scaling=Decimal("1e-18")
    ),
    "0xd501900646641eaf5755758e11eeaa43df691924": TokenInfo(
        currency=CurrencyInfo(symbol="VKNF", name="VKENAF"), scaling=Decimal("1e-12")
    ),
    "0xd50c1746d835d2770dda3703b69187bffeb14126": TokenInfo(
        currency=CurrencyInfo(symbol="IETC", name="iETC"), scaling=Decimal("1e-18")
    ),
    "0xd51e852630debc24e9e1041a03d80a0107f8ef0c": TokenInfo(
        currency=CurrencyInfo(symbol="ORM", name="ORIUM"), scaling=Decimal("1e-0")
    ),
    "0xd528cf2e081f72908e086f8800977df826b5a483": TokenInfo(
        currency=CurrencyInfo(symbol="PBX", name="Paribus"), scaling=Decimal("1e-18")
    ),
    "0xd52a7503051deaad31a7a8b49b4685e3058eed91": TokenInfo(
        currency=CurrencyInfo(symbol="BHI", name="BHI Token"), scaling=Decimal("1e-18")
    ),
    "0xd533a949740bb3306d119cc777fa900ba034cd52": TokenInfo(
        currency=CurrencyInfo(symbol="CRV", name="Curve DAO Token"), scaling=Decimal("1e-18")
    ),
    "0xd536bbd5414a8c2beed82a63737b9327d2fa35a6": TokenInfo(
        currency=CurrencyInfo(symbol="ACU", name="Aitheon"), scaling=Decimal("1e-18")
    ),
    "0xd5525d397898e5502075ea5e830d8914f6f0affe": TokenInfo(
        currency=CurrencyInfo(symbol="MEME", name="Meme"), scaling=Decimal("1e-8")
    ),
    "0xd5527579226e4ebc8864906e49d05d4458ccf47f": TokenInfo(
        currency=CurrencyInfo(symbol="KBR", name="Kubera Coin"), scaling=Decimal("1e-0")
    ),
    "0xd559f20296ff4895da39b5bd9add54b442596a61": TokenInfo(
        currency=CurrencyInfo(symbol="FTX", name="FintruX"), scaling=Decimal("1e-18")
    ),
    "0xd55bd2c12b30075b325bc35aef0b46363b3818f8": TokenInfo(
        currency=CurrencyInfo(symbol="ZOMBIE", name="Zombie.Finance"), scaling=Decimal("1e-18")
    ),
    "0xd55e5ea9e6c055708ec01c881cb12907d33b21d4": TokenInfo(
        currency=CurrencyInfo(symbol="ZETH", name="Zethereum"), scaling=Decimal("1e-18")
    ),
    "0xd567b5f02b9073ad3a982a099a23bf019ff11d1c": TokenInfo(
        currency=CurrencyInfo(symbol="GAME", name="Gamestarter"), scaling=Decimal("1e-5")
    ),
    "0xd56dac73a4d6766464b38ec6d91eb45ce7457c44": TokenInfo(
        currency=CurrencyInfo(symbol="PAN", name="Panvala Pan"), scaling=Decimal("1e-18")
    ),
    "0xd5930c307d7395ff807f2921f12c5eb82131a789": TokenInfo(
        currency=CurrencyInfo(symbol="BOLT", name="Bolt"), scaling=Decimal("1e-18")
    ),
    "0xd5ccddc71353ca810ae577ccafbc6fd53161944b": TokenInfo(
        currency=CurrencyInfo(symbol="AF.CX", name="Air France-Klm"), scaling=Decimal("1e-8")
    ),
    "0xd5dc8921a5c58fb0eba6db6b40eab40283dc3c01": TokenInfo(
        currency=CurrencyInfo(symbol="DDAM", name="Decentralized Data Assets Management"), scaling=Decimal("1e-9")
    ),
    "0xd5e2a54fef5f9e4a6b21ec646bbed7a160a00f18": TokenInfo(
        currency=CurrencyInfo(symbol="BCMC1", name="BeforeCoinMarketCap"), scaling=Decimal("1e-18")
    ),
    "0xd6014ea05bde904448b743833ddf07c3c7837481": TokenInfo(
        currency=CurrencyInfo(symbol="IBTC", name="iBTC"), scaling=Decimal("1e-18")
    ),
    "0xd64809f5f7d772d9112a6bd379de00a77188199e": TokenInfo(
        currency=CurrencyInfo(symbol="LSILVER", name="Lyfe Silver"), scaling=Decimal("1e-18")
    ),
    "0xd65960facb8e4a2dfcb2c2212cb2e44a02e2a57e": TokenInfo(
        currency=CurrencyInfo(symbol="SOAR", name="Soarcoin"), scaling=Decimal("1e-6")
    ),
    "0xd668e107aab776e35061d208bb083918aaede9b5": TokenInfo(
        currency=CurrencyInfo(symbol="KAKI", name="KAKI"), scaling=Decimal("1e-18")
    ),
    "0xd67b1db49801b6f4c96a01a4f7964233150dc58b": TokenInfo(
        currency=CurrencyInfo(symbol="KBC", name="Karatgold Coin"), scaling=Decimal("1e-7")
    ),
    "0xd688bac17e2d58db5b5a61a6fa658c24bc7d45c0": TokenInfo(
        currency=CurrencyInfo(symbol="FTBC", name="Film & Television Blockchain"), scaling=Decimal("1e-18")
    ),
    "0xd68a2cb2bacd96d81e7342f041851b68458116ed": TokenInfo(
        currency=CurrencyInfo(symbol="TSLA.CX", name="Tesla"), scaling=Decimal("1e-8")
    ),
    "0xd6940a1ffd9f3b025d1f1055abcfd9f7cda81ef9": TokenInfo(
        currency=CurrencyInfo(symbol="YFR", name="YouForia"), scaling=Decimal("1e-18")
    ),
    "0xd69f306549e9d96f183b1aeca30b8f4353c2ecc3": TokenInfo(
        currency=CurrencyInfo(symbol="MCHC", name="MCH Coin"), scaling=Decimal("1e-18")
    ),
    "0xd6a073d973f95b7ce2ecf2b19224fa12103cf460": TokenInfo(
        currency=CurrencyInfo(symbol="AMZN.CX", name="Amazon.com Inc"), scaling=Decimal("1e-8")
    ),
    "0xd6a55c63865affd67e2fb9f284f87b7a9e5ff3bd": TokenInfo(
        currency=CurrencyInfo(symbol="ESH", name="Switch"), scaling=Decimal("1e-18")
    ),
    "0xd6a5ab46ead26f49b03bbb1f9eb1ad5c1767974a": TokenInfo(
        currency=CurrencyInfo(symbol="EMON", name="Ethermon"), scaling=Decimal("1e-18")
    ),
    "0xd6ad7a6750a7593e092a9b218d66c0a814a3436e": TokenInfo(
        currency=CurrencyInfo(symbol="yUSDC", name="iearn USDC"), scaling=Decimal("1e-6")
    ),
    "0xd6b107d3e45b959b6d13faf1bb2a2cf8fc7025e6": TokenInfo(
        currency=CurrencyInfo(symbol="BTNG", name="Bitnex Global"), scaling=Decimal("1e-18")
    ),
    "0xd6bd97a26232ba02172ff86b055d5d7be789335b": TokenInfo(
        currency=CurrencyInfo(symbol="OMC", name="Ormeus Cash"), scaling=Decimal("1e-18")
    ),
    "0xd6bfc2d9c5bf6eec918a7ebc4e80843876efd6ae": TokenInfo(
        currency=CurrencyInfo(symbol="XAUM.CX", name="Gold Spot"), scaling=Decimal("1e-8")
    ),
    "0xd6c67b93a7b248df608a653d82a100556144c5da": TokenInfo(
        currency=CurrencyInfo(symbol="EXNT", name="ExNetwork Token"), scaling=Decimal("1e-16")
    ),
    "0xd6cb175719365a2ea630f266c53ddfbe4e468e25": TokenInfo(
        currency=CurrencyInfo(symbol="HNI", name="Hunimal Token"), scaling=Decimal("1e-18")
    ),
    "0xd6e1401a079922469e9b965cb090ea6ff64c6839": TokenInfo(
        currency=CurrencyInfo(symbol="HOLD", name="Hold"), scaling=Decimal("1e-18")
    ),
    "0xd6e6a28eb0a72af2336f80e143e7311bc3108b97": TokenInfo(
        currency=CurrencyInfo(symbol="TAT", name="Leblock"), scaling=Decimal("1e-18")
    ),
    "0xd6f0bb2a45110f819e908a915237d652ac7c5aa8": TokenInfo(
        currency=CurrencyInfo(symbol="BUIDL", name="DFOHub"), scaling=Decimal("1e-18")
    ),
    "0xd6f279b7ccbcd70f8be439d25b9df93aeb60ec55": TokenInfo(
        currency=CurrencyInfo(symbol="idleWBTCYield", name="IdleWBTC v3 [Max yield]"), scaling=Decimal("1e-18")
    ),
    "0xd717b75404022fb1c8582adf1c66b9a553811754": TokenInfo(
        currency=CurrencyInfo(symbol="MILC", name="Micro Licensing Coin"), scaling=Decimal("1e-18")
    ),
    "0xd71ecff9342a5ced620049e616c5035f1db98620": TokenInfo(
        currency=CurrencyInfo(symbol="SEUR", name="sEUR"), scaling=Decimal("1e-18")
    ),
    "0xd7394087e1dbbe477fe4f1cf373b9ac9459565ff": TokenInfo(
        currency=CurrencyInfo(symbol="RET", name="RealTract"), scaling=Decimal("1e-8")
    ),
    "0xd73a66b8fb26be8b0acd7c52bd325054ac7d468b": TokenInfo(
        currency=CurrencyInfo(symbol="WNK", name="Woonk"), scaling=Decimal("1e-18")
    ),
    "0xd73be539d6b2076bab83ca6ba62dfe189abc6bbe": TokenInfo(
        currency=CurrencyInfo(symbol="BC", name="BlockchainCuties"), scaling=Decimal("1e-0")
    ),
    "0xd750430fb81dc53a23ad225cdc82d7e4c22b0cfb": TokenInfo(
        currency=CurrencyInfo(symbol="UBIT", name="Ubit Cash"), scaling=Decimal("1e-6")
    ),
    "0xd760addfb24d9c01fe4bfea7475c5e3636684058": TokenInfo(
        currency=CurrencyInfo(symbol="USDM", name="Mether"), scaling=Decimal("1e-2")
    ),
    "0xd7631787b4dcc87b1254cfd1e5ce48e96823dee8": TokenInfo(
        currency=CurrencyInfo(symbol="SCL", name="Sociall"), scaling=Decimal("1e-8")
    ),
    "0xd776291ec1ae42d57642b9c512832d880edc668b": TokenInfo(
        currency=CurrencyInfo(symbol="CXO", name="Comet-X"), scaling=Decimal("1e-18")
    ),
    "0xd778e4f5450ede47289fef874a37b79db77c4cf1": TokenInfo(
        currency=CurrencyInfo(symbol="YFIA", name="YFIA"), scaling=Decimal("1e-18")
    ),
    "0xd780ae2bf04cd96e577d3d014762f831d97129d0": TokenInfo(
        currency=CurrencyInfo(symbol="EVN", name="Envion"), scaling=Decimal("1e-18")
    ),
    "0xd794dd1cada4cf79c9eebaab8327a1b0507ef7d4": TokenInfo(
        currency=CurrencyInfo(symbol="HYVE", name="Hyve"), scaling=Decimal("1e-18")
    ),
    "0xd7b7d3c0bda57723fb54ab95fd8f9ea033af37f2": TokenInfo(
        currency=CurrencyInfo(symbol="PYLON", name="Pylon Finance"), scaling=Decimal("1e-18")
    ),
    "0xd7c49cee7e9188cca6ad8ff264c1da2e69d4cf3b": TokenInfo(
        currency=CurrencyInfo(symbol="NXM", name="Nexus Mutual"), scaling=Decimal("1e-18")
    ),
    "0xd7cddd45629934c2f6ed3b63217bd8085d7c14a8": TokenInfo(
        currency=CurrencyInfo(symbol="AVH", name="Animation Vision Cash"), scaling=Decimal("1e-18")
    ),
    "0xd7e1e4530d95717506633e58437f056a49c1fabb": TokenInfo(
        currency=CurrencyInfo(symbol="AMA", name="AMA Token"), scaling=Decimal("1e-18")
    ),
    "0xd7eed0fcde8d805b6798cda396968c25335cd379": TokenInfo(
        currency=CurrencyInfo(symbol="BTP", name="BitPlay"), scaling=Decimal("1e-18")
    ),
    "0xd7efb00d12c2c13131fd319336fdf952525da2af": TokenInfo(
        currency=CurrencyInfo(symbol="XPR", name="Proton"), scaling=Decimal("1e-4")
    ),
    "0xd7f5cabdf696d7d1bf384d7688926a4bdb092c67": TokenInfo(
        currency=CurrencyInfo(symbol="DRC", name="DRC Mobility"), scaling=Decimal("1e-18")
    ),
    "0xd811250b7fe83150cbb3d70a892fce6189fb3e08": TokenInfo(
        currency=CurrencyInfo(symbol="VMC", name="Virtual Mind Chain"), scaling=Decimal("1e-18")
    ),
    "0xd811e485cb4ab1fad56233de4464fb5d1c9f3e99": TokenInfo(
        currency=CurrencyInfo(symbol="YG", name="Yearn Global"), scaling=Decimal("1e-18")
    ),
    "0xd829664cdbf3195b2ce76047a65de29e7ed0a9a8": TokenInfo(
        currency=CurrencyInfo(symbol="ALTBULL", name="3X Long Altcoin Index Token"), scaling=Decimal("1e-18")
    ),
    "0xd82bb924a1707950903e2c0a619824024e254cd1": TokenInfo(
        currency=CurrencyInfo(symbol="DAOFI", name="DAOfi"), scaling=Decimal("1e-18")
    ),
    "0xd82df0abd3f51425eb15ef7580fda55727875f14": TokenInfo(
        currency=CurrencyInfo(symbol="DAV", name="DAV Network"), scaling=Decimal("1e-18")
    ),
    "0xd83c5c357969628272def87dcdb5b66352dfd794": TokenInfo(
        currency=CurrencyInfo(symbol="LEOHEDGE", name="1X Short LEO Token"), scaling=Decimal("1e-18")
    ),
    "0xd8446236fa95b9b5f9fd0f8e7df1a944823c683d": TokenInfo(
        currency=CurrencyInfo(symbol="NEEO", name="NEEO Token"), scaling=Decimal("1e-18")
    ),
    "0xd84958efa6fe4e6f29457917a9ab1bbc1b542995": TokenInfo(
        currency=CurrencyInfo(symbol="OCG", name="Orocrypt Gold Token"), scaling=Decimal("1e-9")
    ),
    "0xd850942ef8811f2a866692a623011bde52a462c1": TokenInfo(
        currency=CurrencyInfo(symbol="VEN", name="VeChain (Old, ERC-20)"), scaling=Decimal("1e-18")
    ),
    "0xd85a6ae55a7f33b0ee113c234d2ee308edeaf7fd": TokenInfo(
        currency=CurrencyInfo(symbol="CBK", name="Cobak Token"), scaling=Decimal("1e-18")
    ),
    "0xd8698a985b89650d0a70f99ad2909bd0c0b4b51c": TokenInfo(
        currency=CurrencyInfo(symbol="CSM", name="Consentium"), scaling=Decimal("1e-18")
    ),
    "0xd88a43facba9990b536113ea3b2bbba93f75fa9a": TokenInfo(
        currency=CurrencyInfo(symbol="SKC", name="Skeincoin"), scaling=Decimal("1e-18")
    ),
    "0xd88dc46b9b5d1eaf9acb5d446e96576ceb7264b8": TokenInfo(
        currency=CurrencyInfo(symbol="MRVL.CX", name="Marvell Technology Group Ltd"), scaling=Decimal("1e-8")
    ),
    "0xd89040ac9823b72f64d71f66fa2deae7c8520671": TokenInfo(
        currency=CurrencyInfo(symbol="NST", name="NewSolution"), scaling=Decimal("1e-18")
    ),
    "0xd8912c10681d8b21fd3742244f44658dba12264e": TokenInfo(
        currency=CurrencyInfo(symbol="PLU", name="Pluton"), scaling=Decimal("1e-18")
    ),
    "0xd8950fdeaa10304b7a7fd03a2fc66bc39f3c711a": TokenInfo(
        currency=CurrencyInfo(symbol="WYS", name="Wysker Token"), scaling=Decimal("1e-18")
    ),
    "0xd8a8843b0a5aba6b030e92b3f4d669fad8a5be50": TokenInfo(
        currency=CurrencyInfo(symbol="AFDLT", name="AfroDex Labs Token"), scaling=Decimal("1e-4")
    ),
    "0xd8b8e1eca89da014e67fdbc2014eaa8e171079bf": TokenInfo(
        currency=CurrencyInfo(symbol="FRECNX", name="FreldoCoinX"), scaling=Decimal("1e-18")
    ),
    "0xd8bd3958725f216eb236e9dc65b169de48101c6a": TokenInfo(
        currency=CurrencyInfo(symbol="GBT", name="Globatalent"), scaling=Decimal("1e-8")
    ),
    "0xd8c82fbc4d8ed0644a7ec04cf973e84c6153c1d7": TokenInfo(
        currency=CurrencyInfo(symbol="RZN", name="Rizen Coin (Old)"), scaling=Decimal("1e-18")
    ),
    "0xd8dc1070b5510583728ee2afd6934877ea2de474": TokenInfo(
        currency=CurrencyInfo(symbol="XGP", name="AIGO Payment"), scaling=Decimal("1e-18")
    ),
    "0xd8e3fb3b08eba982f2754988d70d57edc0055ae6": TokenInfo(
        currency=CurrencyInfo(symbol="ZORA", name="Zoracles"), scaling=Decimal("1e-9")
    ),
    "0xd8ef149b4e1e8f050d52925f9c68d3a296e77227": TokenInfo(
        currency=CurrencyInfo(symbol="BEP", name="Blucon"), scaling=Decimal("1e-18")
    ),
    "0xd9016a907dc0ecfa3ca425ab20b6b785b42f2373": TokenInfo(
        currency=CurrencyInfo(symbol="GMEE", name="GAMEE"), scaling=Decimal("1e-18")
    ),
    "0xd905e2eaebe188fc92179b6350807d8bd91db0d8": TokenInfo(
        currency=CurrencyInfo(symbol="PAXCURVE", name="LP-paxCurve"), scaling=Decimal("1e-18")
    ),
    "0xd907daeed4dae963b0e2442e330d1760d752a68e": TokenInfo(
        currency=CurrencyInfo(symbol="SEOL", name="SEED OF LOVE"), scaling=Decimal("1e-18")
    ),
    "0xd90e69f67203ebe02c917b5128629e77b4cd92dc": TokenInfo(
        currency=CurrencyInfo(symbol="ONC", name="One Cash"), scaling=Decimal("1e-18")
    ),
    "0xd91a6162f146ef85922d9a15ee6eb14a00344586": TokenInfo(
        currency=CurrencyInfo(symbol="KICKS", name="SESSIA"), scaling=Decimal("1e-18")
    ),
    "0xd938137e6d96c72e4a6085412ada2dad78ff89c4": TokenInfo(
        currency=CurrencyInfo(symbol="AAA", name="Abulaba"), scaling=Decimal("1e-8")
    ),
    "0xd945d2031b4c63c0e363304fb771f709b502dc0a": TokenInfo(
        currency=CurrencyInfo(symbol="BMC", name="BountyMarketCap"), scaling=Decimal("1e-18")
    ),
    "0xd947b0ceab2a8885866b9a04a06ae99de852a3d4": TokenInfo(
        currency=CurrencyInfo(symbol="TIOX", name="Trade Token X"), scaling=Decimal("1e-18")
    ),
    "0xd9485499499d66b175cf5ed54c0a19f1a6bcb61a": TokenInfo(
        currency=CurrencyInfo(symbol="USE", name="Usechain"), scaling=Decimal("1e-18")
    ),
    "0xd957e08ac5421e2c28510586b57d095e5094836a": TokenInfo(
        currency=CurrencyInfo(symbol="VTX", name="VorteX Network"), scaling=Decimal("1e-18")
    ),
    "0xd967d9f941cd316ab238d3ee761f80b7caec7819": TokenInfo(
        currency=CurrencyInfo(symbol="RDV", name="Rendezvous"), scaling=Decimal("1e-18")
    ),
    "0xd96b9fd7586d9ea24c950d24399be4fb65372fdd": TokenInfo(
        currency=CurrencyInfo(symbol="BTCS", name="Bitcoin Silver"), scaling=Decimal("1e-18")
    ),
    "0xd97e471695f73d8186deabc1ab5b8765e667cd96": TokenInfo(
        currency=CurrencyInfo(symbol="EMCO", name="EmcoToken"), scaling=Decimal("1e-18")
    ),
    "0xd98f75b1a3261dab9eed4956c93f33749027a964": TokenInfo(
        currency=CurrencyInfo(symbol="SHR", name="ShareToken"), scaling=Decimal("1e-2")
    ),
    "0xd99298985902c9a69bf4c8a0895fa10721204ecc": TokenInfo(
        currency=CurrencyInfo(symbol="EUCX", name="EUCX Token"), scaling=Decimal("1e-18")
    ),
    "0xd9964e1306dda055f5284c52048712c35ddb61fd": TokenInfo(
        currency=CurrencyInfo(symbol="BTNT", name="BitNautic"), scaling=Decimal("1e-18")
    ),
    "0xd99b8a7fa48e25cce83b81812220a3e03bf64e5f": TokenInfo(
        currency=CurrencyInfo(symbol="SKM", name="Skrumble Token"), scaling=Decimal("1e-18")
    ),
    "0xd9a12cde03a86e800496469858de8581d3a5353d": TokenInfo(
        currency=CurrencyInfo(symbol="YUP", name="Crowdholding"), scaling=Decimal("1e-18")
    ),
    "0xd9a8cfe21c232d485065cb62a96866799d4645f7": TokenInfo(
        currency=CurrencyInfo(symbol="FGP", name="FingerPrint"), scaling=Decimal("1e-18")
    ),
    "0xd9a947789974bad9be77e45c2b327174a9c59d71": TokenInfo(
        currency=CurrencyInfo(symbol="YSR", name="Ystar"), scaling=Decimal("1e-18")
    ),
    "0xd9af2d11d788da0097076f4eb21bd1c5533743d9": TokenInfo(
        currency=CurrencyInfo(symbol="LBK", name="Legal Block"), scaling=Decimal("1e-18")
    ),
    "0xd9b312d77bc7bed9b9cecb56636300bed4fe5ce9": TokenInfo(
        currency=CurrencyInfo(symbol="GAINS", name="Gains"), scaling=Decimal("1e-18")
    ),
    "0xd9b6f884771857a2afb9171ea53303ff041c2af9": TokenInfo(
        currency=CurrencyInfo(symbol="XPV", name="Percival"), scaling=Decimal("1e-18")
    ),
    "0xd9bae39c725a1864b1133ad0ef1640d02f79b78c": TokenInfo(
        currency=CurrencyInfo(symbol="TST", name="Touch Social"), scaling=Decimal("1e-18")
    ),
    "0xd9c2d319cd7e6177336b0a9c93c21cb48d84fb54": TokenInfo(
        currency=CurrencyInfo(symbol="HAPI", name="HAPI"), scaling=Decimal("1e-18")
    ),
    "0xd9d2c606ec5f7a01df496768cfc9e5003b23d193": TokenInfo(
        currency=CurrencyInfo(symbol="YCN", name="YouthCoin"), scaling=Decimal("1e-8")
    ),
    "0xd9dac7b72472376b60b6aee9cfa2498cccdcb2a7": TokenInfo(
        currency=CurrencyInfo(symbol="HOR", name="Hours Chain"), scaling=Decimal("1e-18")
    ),
    "0xd9dbe80995dbe64e371464b94d78baf10a694ed0": TokenInfo(
        currency=CurrencyInfo(symbol="SAM", name="Six Farm"), scaling=Decimal("1e-0")
    ),
    "0xd9dc38f1c0f551f949a81cf7269a017e48b1d5a4": TokenInfo(
        currency=CurrencyInfo(symbol="XGP", name="Gold Power Coin"), scaling=Decimal("1e-18")
    ),
    "0xd9ec3ff1f8be459bb9369b4e79e9ebcf7141c093": TokenInfo(
        currency=CurrencyInfo(symbol="KAI", name="KardiaChain"), scaling=Decimal("1e-18")
    ),
    "0xd9f7deaeb3450cd698fd6d45a7b05a18d84bb1e1": TokenInfo(
        currency=CurrencyInfo(symbol="NEXE", name="Nexeum Protocol"), scaling=Decimal("1e-18")
    ),
    "0xda0c94c73d127ee191955fb46bacd7ff999b2bcd": TokenInfo(
        currency=CurrencyInfo(symbol="STANDARD", name="Stakeborg DAO"), scaling=Decimal("1e-18")
    ),
    "0xda2c424fc98c741c2d4ef2f42897cefed897ca75": TokenInfo(
        currency=CurrencyInfo(symbol="BNFT", name="Blockchain Benefits"), scaling=Decimal("1e-9")
    ),
    "0xda4c5aea122260e70616e979592735f12fe20499": TokenInfo(
        currency=CurrencyInfo(symbol="AXN", name="Axion (OLD)"), scaling=Decimal("1e-18")
    ),
    "0xda5180086461ff6eeb09580181ac160522dcdcd4": TokenInfo(
        currency=CurrencyInfo(symbol="BRZX", name="Braziliex Token"), scaling=Decimal("1e-8")
    ),
    "0xda6cb58a0d0c01610a29c5a65c303e13e885887c": TokenInfo(
        currency=CurrencyInfo(symbol="cV", name="cVToken"), scaling=Decimal("1e-18")
    ),
    "0xda80b20038bdf968c7307bb5907a469482cf6251": TokenInfo(
        currency=CurrencyInfo(symbol="BNN", name="Broker Neko Network"), scaling=Decimal("1e-8")
    ),
    "0xdaab5e695bb0e8ce8384ee56ba38fa8290618e52": TokenInfo(
        currency=CurrencyInfo(symbol="CRDT", name="CRDT"), scaling=Decimal("1e-18")
    ),
    "0xdab0c31bf34c897fb0fe90d12ec9401caf5c36ec": TokenInfo(
        currency=CurrencyInfo(symbol="DAB", name="DABcoin"), scaling=Decimal("1e-0")
    ),
    "0xdab396ccf3d84cf2d07c4454e10c8a6f5b008d2b": TokenInfo(
        currency=CurrencyInfo(symbol="GFI", name="Goldfinch"), scaling=Decimal("1e-18")
    ),
    "0xdaba2cdc53fbfc7ef00ce427de493c679a6db151": TokenInfo(
        currency=CurrencyInfo(symbol="DBX.CX", name="DropBox"), scaling=Decimal("1e-8")
    ),
    "0xdac17f958d2ee523a2206206994597c13d831ec7": TokenInfo(
        currency=CurrencyInfo(symbol="USDT", name="Tether"), scaling=Decimal("1e-6")
    ),
    "0xdac2bd8fbaae386eb50f084b82a04815dd8b0a60": TokenInfo(
        currency=CurrencyInfo(symbol="INEX", name="InternetExchangeToken"), scaling=Decimal("1e-8")
    ),
    "0xdac4ae188ace3c8985765edc6c9b4739d4845ddc": TokenInfo(
        currency=CurrencyInfo(symbol="INVE", name="InterValue"), scaling=Decimal("1e-18")
    ),
    "0xdac657ffd44a3b9d8aba8749830bf14beb66ff2d": TokenInfo(
        currency=CurrencyInfo(symbol="HDAO", name="humanDAO"), scaling=Decimal("1e-18")
    ),
    "0xdacd69347de42babfaecd09dc88958378780fb62": TokenInfo(
        currency=CurrencyInfo(symbol="ATRI", name="Atari"), scaling=Decimal("1e-0")
    ),
    "0xdad59fd8b366a5536c014da9eb81d19ec9953920": TokenInfo(
        currency=CurrencyInfo(symbol="FLINT", name="MintFlint"), scaling=Decimal("1e-18")
    ),
    "0xdae1baf249964bc4b6ac98c3122f0e3e785fd279": TokenInfo(
        currency=CurrencyInfo(symbol="TKA", name="Tokia"), scaling=Decimal("1e-18")
    ),
    "0xdaf1fe038a05e66304a696e2d0dfd07510c8db2b": TokenInfo(
        currency=CurrencyInfo(symbol="MNK.CX", name="Mallinckrodt"), scaling=Decimal("1e-8")
    ),
    "0xdaf76716996052aff7edb66ef0edb301bf001b6f": TokenInfo(
        currency=CurrencyInfo(symbol="ABA", name="ABACOIN"), scaling=Decimal("1e-18")
    ),
    "0xdaf88906ac1de12ba2b1d2f7bfc94e9638ac40c4": TokenInfo(
        currency=CurrencyInfo(symbol="EPK", name="EpiK Protocol"), scaling=Decimal("1e-18")
    ),
    "0xdaff85b6f5787b2d9ee11ccdf5e852816063326a": TokenInfo(
        currency=CurrencyInfo(symbol="PXUSD-OCT2020", name="pxUSD Synthetic USD Expiring 1 November 2020"),
        scaling=Decimal("1e-18"),
    ),
    "0xdb0170e2d0c1cc1b2e7a90313d9b9afa4f250289": TokenInfo(
        currency=CurrencyInfo(symbol="ADAPAD", name="ADAPad"), scaling=Decimal("1e-18")
    ),
    "0xdb03cf87e195eba7f1a259d3a70030918d7efa2e": TokenInfo(
        currency=CurrencyInfo(symbol="TOOS", name="Toos"), scaling=Decimal("1e-8")
    ),
    "0xdb05ea0877a2622883941b939f0bb11d1ac7c400": TokenInfo(
        currency=CurrencyInfo(symbol="OPCT", name="Opacity"), scaling=Decimal("1e-18")
    ),
    "0xdb0acc14396d108b3c5574483acb817855c9dc8d": TokenInfo(
        currency=CurrencyInfo(symbol="EMB", name="Overline Emblem"), scaling=Decimal("1e-8")
    ),
    "0xdb0f69306ff8f949f258e83f6b87ee5d052d0b23": TokenInfo(
        currency=CurrencyInfo(symbol="GCP", name="GlobCoin Crypto Platform"), scaling=Decimal("1e-18")
    ),
    "0xdb13025b219db5e4529f48b65ff009a26b6ae733": TokenInfo(
        currency=CurrencyInfo(symbol="UBN", name="Ubricoin"), scaling=Decimal("1e-18")
    ),
    "0xdb144cd0f15ee40aac5602364b470d703d7e16b6": TokenInfo(
        currency=CurrencyInfo(symbol="VSL", name="vSlice"), scaling=Decimal("1e-8")
    ),
    "0xdb25f211ab05b1c97d595516f45794528a807ad8": TokenInfo(
        currency=CurrencyInfo(symbol="EURS", name="STASIS EURO"), scaling=Decimal("1e-2")
    ),
    "0xdb298285fe4c5410b05390ca80e8fbe9de1f259b": TokenInfo(
        currency=CurrencyInfo(symbol="FOREX", name="handle fi"), scaling=Decimal("1e-18")
    ),
    "0xdb2f2bcce3efa95eda95a233af45f3e0d4f00e2a": TokenInfo(
        currency=CurrencyInfo(symbol="AGS", name="Aegis"), scaling=Decimal("1e-8")
    ),
    "0xdb33d49b5a41a97d296b7242a96ebd8ac77b3bb8": TokenInfo(
        currency=CurrencyInfo(symbol="CYF", name="CY Finance"), scaling=Decimal("1e-18")
    ),
    "0xdb455c71c1bc2de4e80ca451184041ef32054001": TokenInfo(
        currency=CurrencyInfo(symbol="JOT", name="Jury.Online Token"), scaling=Decimal("1e-18")
    ),
    "0xdb52a87cda28eda00f8add1c79c9db4a50a70457": TokenInfo(
        currency=CurrencyInfo(symbol="TRC", name="Trader Cash"), scaling=Decimal("1e-18")
    ),
    "0xdb56448fe2635f7912287cd619e7ed3d93180f25": TokenInfo(
        currency=CurrencyInfo(symbol="CVS", name="CoinVisa"), scaling=Decimal("1e-18")
    ),
    "0xdb5c3c46e28b53a39c255aa39a411dd64e5fed9c": TokenInfo(
        currency=CurrencyInfo(symbol="NCR", name="Neos Credits"), scaling=Decimal("1e-18")
    ),
    "0xdb61354e9cf2217a29770e9811832b360a8daad3": TokenInfo(
        currency=CurrencyInfo(symbol="LTCBULL", name="3X Long Litecoin Token"), scaling=Decimal("1e-18")
    ),
    "0xdb7eab9ba6be88b869f738f6deeba96d49fe13fd": TokenInfo(
        currency=CurrencyInfo(symbol="BOOM", name="Boom Token"), scaling=Decimal("1e-18")
    ),
    "0xdb80734b094a3f964dedfd10e8946753ae0ac04c": TokenInfo(
        currency=CurrencyInfo(symbol="KCH", name="Keep Calm and Hodl"), scaling=Decimal("1e-18")
    ),
    "0xdb85f6685950e285b1e611037bebe5b34e2b7d78": TokenInfo(
        currency=CurrencyInfo(symbol="ZANO", name="Zano"), scaling=Decimal("1e-18")
    ),
    "0xdb8646f5b487b5dd979fac618350e85018f557d4": TokenInfo(
        currency=CurrencyInfo(symbol="BTK", name="BitcoinToken"), scaling=Decimal("1e-18")
    ),
    "0xdbb2f12cb89af05516768c2c69a771d92a25d17c": TokenInfo(
        currency=CurrencyInfo(symbol="BEAST", name="Beast DAO"), scaling=Decimal("1e-18")
    ),
    "0xdbdb4d16eda451d0503b854cf79d55697f90c8df": TokenInfo(
        currency=CurrencyInfo(symbol="ALCX", name="Alchemix"), scaling=Decimal("1e-18")
    ),
    "0xdbdd6f355a37b94e6c7d32fef548e98a280b8df5": TokenInfo(
        currency=CurrencyInfo(symbol="UWL", name="UniWhales"), scaling=Decimal("1e-18")
    ),
    "0xdbddf072d7aae7b9288e31a4eebe6c54e3a143b1": TokenInfo(
        currency=CurrencyInfo(symbol="CRWNY", name="Crowny Token"), scaling=Decimal("1e-18")
    ),
    "0xdbf637f78624f896b92f801e81f6031b7865ed20": TokenInfo(
        currency=CurrencyInfo(symbol="BTMXBEAR", name="3X Short BitMax Token Token"), scaling=Decimal("1e-18")
    ),
    "0xdbfb423e9bbf16294388e07696a5120e4ceba0c5": TokenInfo(
        currency=CurrencyInfo(symbol="ETHD", name="Ethereum Dark"), scaling=Decimal("1e-18")
    ),
    "0xdc10e348ab2e3849573bd17ba1db9e0eda705b5e": TokenInfo(
        currency=CurrencyInfo(symbol="KGSL", name="KYRGYZSOMcrncyLATOKEN"), scaling=Decimal("1e-18")
    ),
    "0xdc3228e10259494a834743260ca8340c7ea90391": TokenInfo(
        currency=CurrencyInfo(symbol="MRC", name="Marco Token"), scaling=Decimal("1e-18")
    ),
    "0xdc349913d53b446485e98b76800b6254f43df695": TokenInfo(
        currency=CurrencyInfo(symbol="BEZOGE", name="Bezoge Earth"), scaling=Decimal("1e-9")
    ),
    "0xdc5864ede28bd4405aa04d93e05a0531797d9d59": TokenInfo(
        currency=CurrencyInfo(symbol="FNT", name="Falcon Project"), scaling=Decimal("1e-6")
    ),
    "0xdc59ac4fefa32293a95889dc396682858d52e5db": TokenInfo(
        currency=CurrencyInfo(symbol="BEAN", name="Bean"), scaling=Decimal("1e-6")
    ),
    "0xdc8af07a7861bedd104b8093ae3e9376fc8596d2": TokenInfo(
        currency=CurrencyInfo(symbol="RVF", name="RocketX"), scaling=Decimal("1e-18")
    ),
    "0xdc98c5543f3004debfaad8966ec403093d0aa4a8": TokenInfo(
        currency=CurrencyInfo(symbol="PEBBLE", name="Etherrock  72"), scaling=Decimal("1e-18")
    ),
    "0xdc9ac3c20d1ed0b540df9b1fedc10039df13f99c": TokenInfo(
        currency=CurrencyInfo(symbol="UTK", name="UTRUST"), scaling=Decimal("1e-18")
    ),
    "0xdcb01cc464238396e213a6fdd933e36796eaff9f": TokenInfo(
        currency=CurrencyInfo(symbol="YLD", name="Yield"), scaling=Decimal("1e-18")
    ),
    "0xdcd85914b8ae28c1e62f1c488e1d968d5aaffe2b": TokenInfo(
        currency=CurrencyInfo(symbol="TOP", name="TOP Network"), scaling=Decimal("1e-18")
    ),
    "0xdcde110057f01d1516b2fa308587c6a30bdc85ba": TokenInfo(
        currency=CurrencyInfo(symbol="CHS", name="CryptoHours"), scaling=Decimal("1e-18")
    ),
    "0xdcfe18bc46f5a0cd0d3af0c2155d2bcb5ade2fc5": TokenInfo(
        currency=CurrencyInfo(symbol="HUE", name="Hue"), scaling=Decimal("1e-4")
    ),
    "0xdd0020b1d5ba47a54e2eb16800d73beb6546f91a": TokenInfo(
        currency=CurrencyInfo(symbol="AXPR", name="aXpire"), scaling=Decimal("1e-18")
    ),
    "0xdd007278b667f6bef52fd0a4c23604aa1f96039a": TokenInfo(
        currency=CurrencyInfo(symbol="RIPT", name="Riptide Coin"), scaling=Decimal("1e-8")
    ),
    "0xdd16ec0f66e54d453e6756713e533355989040e4": TokenInfo(
        currency=CurrencyInfo(symbol="TEN", name="Tokenomy"), scaling=Decimal("1e-18")
    ),
    "0xdd436a0dce9244b36599ae7b22f0373b4e33992d": TokenInfo(
        currency=CurrencyInfo(symbol="TRUSD", name="TrustUSD"), scaling=Decimal("1e-18")
    ),
    "0xdd6bf56ca2ada24c683fac50e37783e55b57af9f": TokenInfo(
        currency=CurrencyInfo(symbol="BNC", name="Brave New Coin"), scaling=Decimal("1e-12")
    ),
    "0xdd6c68bb32462e01705011a4e2ad1a60740f217f": TokenInfo(
        currency=CurrencyInfo(symbol="HBT", name="Hubii Network"), scaling=Decimal("1e-15")
    ),
    "0xdd6eef0507f10d21f716e36d8b1aae76a4fa3f62": TokenInfo(
        currency=CurrencyInfo(symbol="CXGC", name="Cashex Global Coin"), scaling=Decimal("1e-18")
    ),
    "0xdd74a7a3769fa72561b3a69e65968f49748c690c": TokenInfo(
        currency=CurrencyInfo(symbol="ETCH", name="ETCH Supply Token"), scaling=Decimal("1e-18")
    ),
    "0xdd94842c15abfe4c9bafe4222ade02896beb064c": TokenInfo(
        currency=CurrencyInfo(symbol="WGP", name="W Green Pay"), scaling=Decimal("1e-18")
    ),
    "0xdd94de9cfe063577051a5eb7465d08317d8808b6": TokenInfo(
        currency=CurrencyInfo(symbol="Devcon2", name="Devcon2"), scaling=Decimal("1e-0")
    ),
    "0xdd974d5c2e2928dea5f71b9825b8b646686bd200": TokenInfo(
        currency=CurrencyInfo(symbol="KNCL", name="Kyber Network Crystal Legacy"), scaling=Decimal("1e-18")
    ),
    "0xddaaf4a0702a03a4505f2352a1aba001ffc344be": TokenInfo(
        currency=CurrencyInfo(symbol="ATCC", name="ATC Coin"), scaling=Decimal("1e-18")
    ),
    "0xddb3422497e61e13543bea06989c0789117555c5": TokenInfo(
        currency=CurrencyInfo(symbol="COTI", name="COTI Token"), scaling=Decimal("1e-18")
    ),
    "0xddd460bbd9f79847ea08681563e8a9696867210c": TokenInfo(
        currency=CurrencyInfo(symbol="SPND", name="Spendcoin"), scaling=Decimal("1e-18")
    ),
    "0xddd6a0ecc3c6f6c102e5ea3d8af7b801d1a77ac8": TokenInfo(
        currency=CurrencyInfo(symbol="UNIX", name="UniX"), scaling=Decimal("1e-18")
    ),
    "0xdddddd4301a082e62e84e43f474f044423921918": TokenInfo(
        currency=CurrencyInfo(symbol="DVF", name="DVF"), scaling=Decimal("1e-18")
    ),
    "0xdde12a12a6f67156e0da672be05c374e1b0a3e57": TokenInfo(
        currency=CurrencyInfo(symbol="JOY", name="JOYSO"), scaling=Decimal("1e-6")
    ),
    "0xdde45247da97491efd04e96518ae71288f11e0e6": TokenInfo(
        currency=CurrencyInfo(symbol="FURT", name="furtcoin"), scaling=Decimal("1e-18")
    ),
    "0xddf993bebbd397f2a42de7c39f09f9c8e34ef322": TokenInfo(
        currency=CurrencyInfo(symbol="CRO", name="Cronos Coin"), scaling=Decimal("1e-18")
    ),
    "0xde12c7959e1a72bbe8a5f7a1dc8f8eef9ab011b3": TokenInfo(
        currency=CurrencyInfo(symbol="DEI", name="DEI Token"), scaling=Decimal("1e-18")
    ),
    "0xde1e0ae6101b46520cf66fdc0b1059c5cc3d106c": TokenInfo(
        currency=CurrencyInfo(symbol="DELTA", name="DeltaChain"), scaling=Decimal("1e-8")
    ),
    "0xde201daec04ba73166d9917fdf08e1728e270f06": TokenInfo(
        currency=CurrencyInfo(symbol="MEXP", name="MOJI Experience Points"), scaling=Decimal("1e-18")
    ),
    "0xde24f0bbf288ea5902c95dd0b63ba38d569a1a8e": TokenInfo(
        currency=CurrencyInfo(symbol="UBS", name="UBIT SHARE"), scaling=Decimal("1e-18")
    ),
    "0xde2f7766c8bf14ca67193128535e5c7454f8387c": TokenInfo(
        currency=CurrencyInfo(symbol="META", name="Metadium"), scaling=Decimal("1e-18")
    ),
    "0xde30da39c46104798bb5aa3fe8b9e0e1f348163f": TokenInfo(
        currency=CurrencyInfo(symbol="GTC", name="Gitcoin"), scaling=Decimal("1e-18")
    ),
    "0xde4c5a791913838027a2185709e98c5c6027ea63": TokenInfo(
        currency=CurrencyInfo(symbol="XAC", name="General Attention Currency"), scaling=Decimal("1e-8")
    ),
    "0xde4ee8057785a7e8e800db58f9784845a5c2cbd6": TokenInfo(
        currency=CurrencyInfo(symbol="DEXE", name="DeXe"), scaling=Decimal("1e-18")
    ),
    "0xde522a2778e4554707e6a8df36a4871ce9967bb5": TokenInfo(
        currency=CurrencyInfo(symbol="FML", name="FormulA"), scaling=Decimal("1e-18")
    ),
    "0xde5ed76e7c05ec5e4572cfc88d1acea165109e44": TokenInfo(
        currency=CurrencyInfo(symbol="DEUS", name="DEUS Finance"), scaling=Decimal("1e-18")
    ),
    "0xde7d85157d9714eadf595045cc12ca4a5f3e2adb": TokenInfo(
        currency=CurrencyInfo(symbol="STPT", name="STP Network"), scaling=Decimal("1e-18")
    ),
    "0xdea67845a51e24461d5fed8084e69b426af3d5db": TokenInfo(
        currency=CurrencyInfo(symbol="HTRE", name="HodlTree"), scaling=Decimal("1e-18")
    ),
    "0xdecade1c6bf2cd9fb89afad73e4a519c867adcf5": TokenInfo(
        currency=CurrencyInfo(symbol="WIS", name="Experty Wisdom Token"), scaling=Decimal("1e-18")
    ),
    "0xdecf7be29f8832e9c2ddf0388c9778b8ba76af43": TokenInfo(
        currency=CurrencyInfo(symbol="BXC", name="BonusCloud"), scaling=Decimal("1e-18")
    ),
    "0xdee02d94be4929d26f67b64ada7acf1914007f10": TokenInfo(
        currency=CurrencyInfo(symbol="RUNE", name="Rune"), scaling=Decimal("1e-18")
    ),
    "0xdef1fac7bf08f173d286bbbdcbeeade695129840": TokenInfo(
        currency=CurrencyInfo(symbol="CERBY", name="Cerby Token"), scaling=Decimal("1e-18")
    ),
    "0xdefa4e8a7bcba345f687a2f1456f5edd9ce97202": TokenInfo(
        currency=CurrencyInfo(symbol="KNC", name="KNC"), scaling=Decimal("1e-18")
    ),
    "0xdf0041891bda1f911c4243f328f7cf61b37f965b": TokenInfo(
        currency=CurrencyInfo(symbol="BST", name="BOOSTO"), scaling=Decimal("1e-18")
    ),
    "0xdf0960778c6e6597f197ed9a25f12f5d971da86c": TokenInfo(
        currency=CurrencyInfo(symbol="GOO", name="Vials of Goo"), scaling=Decimal("1e-12")
    ),
    "0xdf1338fbafe7af1789151627b886781ba556ef9a": TokenInfo(
        currency=CurrencyInfo(symbol="KUE", name="Kuende"), scaling=Decimal("1e-18")
    ),
    "0xdf18a53c2eeb81635c306c555d7a844e42bf7134": TokenInfo(
        currency=CurrencyInfo(symbol="TDC", name="Trustdex Token"), scaling=Decimal("1e-0")
    ),
    "0xdf195c2101959f6f39f583ffa5a2aeae71c0f503": TokenInfo(
        currency=CurrencyInfo(symbol="SCO", name="Scoin"), scaling=Decimal("1e-18")
    ),
    "0xdf1d6405df92d981a2fb3ce68f6a03bac6c0e41f": TokenInfo(
        currency=CurrencyInfo(symbol="VRA", name="Verasity (Old)"), scaling=Decimal("1e-18")
    ),
    "0xdf1e9e1a218cff9888faef311d6fbb472e4175ce": TokenInfo(
        currency=CurrencyInfo(symbol="AUDX", name="eToro Australian Dollar"), scaling=Decimal("1e-18")
    ),
    "0xdf2237d32ab6945657a6e56f6e4568d19dace492": TokenInfo(
        currency=CurrencyInfo(symbol="IDLV", name="IDLV Token"), scaling=Decimal("1e-18")
    ),
    "0xdf22da9a8c1d80095175ae601d182a734923f01a": TokenInfo(
        currency=CurrencyInfo(symbol="BPAKC", name="BitpakcoinToken"), scaling=Decimal("1e-8")
    ),
    "0xdf2c7238198ad8b389666574f2d8bc411a4b7428": TokenInfo(
        currency=CurrencyInfo(symbol="MFT", name="Hifi Finance"), scaling=Decimal("1e-18")
    ),
    "0xdf347911910b6c9a4286ba8e2ee5ea4a39eb2134": TokenInfo(
        currency=CurrencyInfo(symbol="BOB", name="Bob's Repair"), scaling=Decimal("1e-18")
    ),
    "0xdf413690fb785e56895551cc21086a15b6e90386": TokenInfo(
        currency=CurrencyInfo(symbol="VNC", name="Vincoin Cash"), scaling=Decimal("1e-8")
    ),
    "0xdf44a0043dfae212a49ccfa2c480e52e3e4367bc": TokenInfo(
        currency=CurrencyInfo(symbol="LLU", name="Light Lemon Unicorn"), scaling=Decimal("1e-18")
    ),
    "0xdf44a80c17813789f60090638827aeb23698b122": TokenInfo(
        currency=CurrencyInfo(symbol="STDEX", name="stableDEX"), scaling=Decimal("1e-18")
    ),
    "0xdf4df8ee1bd1c9f01e60ee15e4c2f7643b690699": TokenInfo(
        currency=CurrencyInfo(symbol="POMAC", name="POMA"), scaling=Decimal("1e-18")
    ),
    "0xdf574c24545e5ffecb9a659c229253d4111d87e1": TokenInfo(
        currency=CurrencyInfo(symbol="HUSD", name="HUSD"), scaling=Decimal("1e-8")
    ),
    "0xdf5e0e81dff6faf3a7e52ba697820c5e32d806a8": TokenInfo(
        currency=CurrencyInfo(symbol="YCURVE", name="LP-yCurve"), scaling=Decimal("1e-18")
    ),
    "0xdf6ef343350780bf8c3410bf062e0c015b1dd671": TokenInfo(
        currency=CurrencyInfo(symbol="BMC", name="Blackmoon Crypto"), scaling=Decimal("1e-8")
    ),
    "0xdf7ff54aacacbff42dfe29dd6144a69b629f8c9e": TokenInfo(
        currency=CurrencyInfo(symbol="AZRX", name="Aave ZRX"), scaling=Decimal("1e-18")
    ),
    "0xdf801468a808a32656d2ed2d2d80b72a129739f4": TokenInfo(
        currency=CurrencyInfo(symbol="CUBE", name="Somnium Space CUBEs"), scaling=Decimal("1e-8")
    ),
    "0xdf859c9878ef5e742d7bbe3c22a496c088c89fa9": TokenInfo(
        currency=CurrencyInfo(symbol="FIND", name="FIND Token"), scaling=Decimal("1e-18")
    ),
    "0xdf9307dff0a1b57660f60f9457d32027a55ca0b2": TokenInfo(
        currency=CurrencyInfo(symbol="mETH", name="DMM: ETH"), scaling=Decimal("1e-18")
    ),
    "0xdf9d4674a430bdcc096a3a403128357ab36844ba": TokenInfo(
        currency=CurrencyInfo(symbol="WTK", name="WadzPay Token"), scaling=Decimal("1e-2")
    ),
    "0xdfb410994b66778bd6cc2c82e8ffe4f7b2870006": TokenInfo(
        currency=CurrencyInfo(symbol="KRS", name="Kinguin Krowns"), scaling=Decimal("1e-18")
    ),
    "0xdfb903f323cccd364b3491d9e45b92854bea29d5": TokenInfo(
        currency=CurrencyInfo(symbol="BOST", name="BOSTTE"), scaling=Decimal("1e-18")
    ),
    "0xdfbc9050f5b01df53512dcc39b4f2b2bbacd517a": TokenInfo(
        currency=CurrencyInfo(symbol="JOB", name="Jobchain"), scaling=Decimal("1e-8")
    ),
    "0xdfc3e857c8ccea7657e0ed98ab92e048e38dee0f": TokenInfo(
        currency=CurrencyInfo(symbol="FIH", name="FidelityHouse"), scaling=Decimal("1e-18")
    ),
    "0xdfdb7f72c1f195c5951a234e8db9806eb0635346": TokenInfo(
        currency=CurrencyInfo(symbol="NFD", name="Feisty Doge NFT"), scaling=Decimal("1e-18")
    ),
    "0xdfdc0d82d96f8fd40ca0cfb4a288955becec2088": TokenInfo(
        currency=CurrencyInfo(symbol="MTC", name="MTC Mesh Network"), scaling=Decimal("1e-18")
    ),
    "0xdfe0ec369ea08ea65c486ac5c20bb7a2eebcabea": TokenInfo(
        currency=CurrencyInfo(symbol="GRVC", name="Gravel Coin"), scaling=Decimal("1e-0")
    ),
    "0xdfe35224b17b2e12b92e3987340abf5247fce201": TokenInfo(
        currency=CurrencyInfo(symbol="TWTR.CX", name="Twitter"), scaling=Decimal("1e-8")
    ),
    "0xdfe66b14d37c77f4e9b180ceb433d1b164f0281d": TokenInfo(
        currency=CurrencyInfo(symbol="STETH", name="StakeHound Staked Ether"), scaling=Decimal("1e-18")
    ),
    "0xdfe691f37b6264a90ff507eb359c45d55037951c": TokenInfo(
        currency=CurrencyInfo(symbol="KARMA", name="Karma DAO"), scaling=Decimal("1e-4")
    ),
    "0xdfe7351c291bc0e49079c62212587244e1c666ba": TokenInfo(
        currency=CurrencyInfo(symbol="SME", name="SME Banking Platform"), scaling=Decimal("1e-18")
    ),
    "0xe02784175c3be0dea7cc0f284041b64503639e66": TokenInfo(
        currency=CurrencyInfo(symbol="TOC", name="TouchCon"), scaling=Decimal("1e-18")
    ),
    "0xe03b4386b75e121e04d580d6b8376ceee0615ca8": TokenInfo(
        currency=CurrencyInfo(symbol="DIGI", name="Digiverse"), scaling=Decimal("1e-18")
    ),
    "0xe04491d64eaa464ec8fdf53c7a4c92bf5b2278cd": TokenInfo(
        currency=CurrencyInfo(symbol="WPT", name="WORLDPET"), scaling=Decimal("1e-18")
    ),
    "0xe06af951086ec3c488b50e31be29c07f8a260ca3": TokenInfo(
        currency=CurrencyInfo(symbol="EXU", name="EXU Protocol"), scaling=Decimal("1e-16")
    ),
    "0xe06d2bf8fb832020091fdc0063b5cb6c5b889ea4": TokenInfo(
        currency=CurrencyInfo(symbol="LX.CX", name="LexinFintech Holdings Ltd"), scaling=Decimal("1e-8")
    ),
    "0xe06eda7435ba749b047380ced49121dde93334ae": TokenInfo(
        currency=CurrencyInfo(symbol="SET", name="Transferable Sydney Ethereum Token"), scaling=Decimal("1e-0")
    ),
    "0xe08854b668958657064fa20f309f6ba7a19d5af2": TokenInfo(
        currency=CurrencyInfo(symbol="BLTV", name="BLTV Token"), scaling=Decimal("1e-18")
    ),
    "0xe09394f8ba642430ed448ca20f342ec7aa1ba2e1": TokenInfo(
        currency=CurrencyInfo(symbol="FESS", name="Fesschain"), scaling=Decimal("1e-18")
    ),
    "0xe0955f26515d22e347b17669993fcefcc73c3a0a": TokenInfo(
        currency=CurrencyInfo(symbol="STACK", name="Stacker Ventures"), scaling=Decimal("1e-18")
    ),
    "0xe09f5a388d4ec73db7bcac6594a9a699c54ca80b": TokenInfo(
        currency=CurrencyInfo(symbol="NYOMI", name="Queen Nyomi Token"), scaling=Decimal("1e-18")
    ),
    "0xe0a84699a583d467001fcfe1d52930cf6f3b0bfa": TokenInfo(
        currency=CurrencyInfo(symbol="BTCUSDCRSI", name="WBTC cUSDC RSI Set"), scaling=Decimal("1e-18")
    ),
    "0xe0ad1806fd3e7edf6ff52fdb822432e847411033": TokenInfo(
        currency=CurrencyInfo(symbol="ONX", name="OnX Finance"), scaling=Decimal("1e-18")
    ),
    "0xe0b7927c4af23765cb51314a0e0521a9645f0e2a": TokenInfo(
        currency=CurrencyInfo(symbol="DGD", name="DigixDAO"), scaling=Decimal("1e-9")
    ),
    "0xe0b7e882c194881c690924cb46154b8241f9145e": TokenInfo(
        currency=CurrencyInfo(symbol="CNX", name="Cofinex"), scaling=Decimal("1e-18")
    ),
    "0xe0b9bcd54bf8a730ea5d3f1ffce0885e911a502c": TokenInfo(
        currency=CurrencyInfo(symbol="ZUM", name="ZUM TOKEN"), scaling=Decimal("1e-8")
    ),
    "0xe0bdaafd0aab238c55d68ad54e616305d4a21772": TokenInfo(
        currency=CurrencyInfo(symbol="RFR", name="Refract"), scaling=Decimal("1e-9")
    ),
    "0xe0c6ce3e73029f201e5c0bedb97f67572a93711c": TokenInfo(
        currency=CurrencyInfo(symbol="ETHPLO", name="ETHplode"), scaling=Decimal("1e-6")
    ),
    "0xe0c8087ce1a17bdd5d6c12eb52f8d7eff7791987": TokenInfo(
        currency=CurrencyInfo(symbol="LFC", name="Linfinity"), scaling=Decimal("1e-18")
    ),
    "0xe0c8b298db4cffe05d1bea0bb1ba414522b33c1b": TokenInfo(
        currency=CurrencyInfo(symbol="NCDT", name="Nuco.Cloud"), scaling=Decimal("1e-18")
    ),
    "0xe0d95530820aafc51b1d98023aa1ff000b78d8b2": TokenInfo(
        currency=CurrencyInfo(symbol="PRS", name="PressOne"), scaling=Decimal("1e-18")
    ),
    "0xe120c1ecbfdfea7f0a8f0ee30063491e8c26fedf": TokenInfo(
        currency=CurrencyInfo(symbol="SUR", name="Suretly"), scaling=Decimal("1e-8")
    ),
    "0xe1229dc9824f9911ba4b0f427f1ac95fbdd10308": TokenInfo(
        currency=CurrencyInfo(symbol="TNPC", name="THE NEW PUBLIC COIN"), scaling=Decimal("1e-8")
    ),
    "0xe1237aa7f535b0cc33fd973d66cbf830354d16c7": TokenInfo(
        currency=CurrencyInfo(symbol="yWETH", name="yearn Wrapped Ether"), scaling=Decimal("1e-18")
    ),
    "0xe130d59c0d7f84260b776aa5f93de5031c5a0bf6": TokenInfo(
        currency=CurrencyInfo(symbol="ABAO", name="Aladdin Galaxy"), scaling=Decimal("1e-18")
    ),
    "0xe1329ebf8b719881549909d689987f746a8931d1": TokenInfo(
        currency=CurrencyInfo(symbol="XRM", name="Refine Medium"), scaling=Decimal("1e-18")
    ),
    "0xe13559cf6edf84bd04bf679e251f285000b9305e": TokenInfo(
        currency=CurrencyInfo(symbol="TMC", name="TMC NiftyGotchi"), scaling=Decimal("1e-18")
    ),
    "0xe138fda441fc31b36171122397a8a11d6cd2c479": TokenInfo(
        currency=CurrencyInfo(symbol="GTC", name="Global Trust Coin"), scaling=Decimal("1e-0")
    ),
    "0xe13ef257cf4d5df928ca11d230427c037666d466": TokenInfo(
        currency=CurrencyInfo(symbol="WIT", name="WITChain"), scaling=Decimal("1e-6")
    ),
    "0xe1403e2972145d86f66299380ade23169580beca": TokenInfo(
        currency=CurrencyInfo(symbol="DOOM", name="10X Short Bitcoin Token"), scaling=Decimal("1e-18")
    ),
    "0xe142bef1c919c243b5c9d59b5e7bad3635c7ae78": TokenInfo(
        currency=CurrencyInfo(symbol="1810.CX", name="Xiaomi Corp"), scaling=Decimal("1e-8")
    ),
    "0xe14a603f7c77d4101a87859b8736a04cfd85c688": TokenInfo(
        currency=CurrencyInfo(symbol="TENA", name="TENA"), scaling=Decimal("1e-18")
    ),
    "0xe15254a13d34f9700320330abcb7c7f857af2fb7": TokenInfo(
        currency=CurrencyInfo(symbol="KAPA", name="KAPA COIN"), scaling=Decimal("1e-2")
    ),
    "0xe154d54890c35634ca525d543ed58c741af7cf7a": TokenInfo(
        currency=CurrencyInfo(symbol="MKEY", name="MEDIKEY"), scaling=Decimal("1e-18")
    ),
    "0xe15684ff27237be7f681eb6bdf301d0b2fbf191c": TokenInfo(
        currency=CurrencyInfo(symbol="PLT", name="PLT"), scaling=Decimal("1e-18")
    ),
    "0xe172f366678ec7b559f6c2913a437baadfd4e6c8": TokenInfo(
        currency=CurrencyInfo(symbol="KAU", name="Kauri"), scaling=Decimal("1e-8")
    ),
    "0xe17e41acd4caa3cec048837bfd1918b3c4141767": TokenInfo(
        currency=CurrencyInfo(symbol="ACE", name="Ace Entertainment"), scaling=Decimal("1e-6")
    ),
    "0xe17f017475a709de58e976081eb916081ff4c9d5": TokenInfo(
        currency=CurrencyInfo(symbol="RMPL", name="RMPL"), scaling=Decimal("1e-9")
    ),
    "0xe1a178b681bd05964d3e3ed33ae731577d9d96dd": TokenInfo(
        currency=CurrencyInfo(symbol="BOX", name="BOX Token"), scaling=Decimal("1e-18")
    ),
    "0xe1ac9eb7cddabfd9e5ca49c23bd521afcdf8be49": TokenInfo(
        currency=CurrencyInfo(symbol="MYC", name="Mycion"), scaling=Decimal("1e-18")
    ),
    "0xe1aee98495365fc179699c1bb3e761fa716bee62": TokenInfo(
        currency=CurrencyInfo(symbol="BZNT", name="Bezant"), scaling=Decimal("1e-18")
    ),
    "0xe1afe1fd76fd88f78cbf599ea1846231b8ba3b6b": TokenInfo(
        currency=CurrencyInfo(symbol="SDEFI", name="sDEFI"), scaling=Decimal("1e-18")
    ),
    "0xe1ba0fb44ccb0d11b80f92f4f8ed94ca3ff51d00": TokenInfo(
        currency=CurrencyInfo(symbol="ABAT", name="Aave BAT v1"), scaling=Decimal("1e-18")
    ),
    "0xe1bad922f84b198a08292fb600319300ae32471b": TokenInfo(
        currency=CurrencyInfo(symbol="FCT", name="Firmachain"), scaling=Decimal("1e-18")
    ),
    "0xe1c7e30c42c24582888c758984f6e382096786bd": TokenInfo(
        currency=CurrencyInfo(symbol="XCUR", name="Curate"), scaling=Decimal("1e-8")
    ),
    "0xe1d7c7a4596b038ced2a84bf65b8647271c53208": TokenInfo(
        currency=CurrencyInfo(symbol="NFTY", name="NFTY Token"), scaling=Decimal("1e-18")
    ),
    "0xe1f28d7d34faecddf912b717434e3c3373f0d1d6": TokenInfo(
        currency=CurrencyInfo(symbol="CH50.CX", name="FTSE China A50"), scaling=Decimal("1e-8")
    ),
    "0xe202873079913858f9ba8795ba957a4ad561ca24": TokenInfo(
        currency=CurrencyInfo(symbol="WIFI", name="Wifi Coin"), scaling=Decimal("1e-18")
    ),
    "0xe2311ae37502105b442bbef831e9b53c5d2e9b3b": TokenInfo(
        currency=CurrencyInfo(symbol="BANANA", name="Banana"), scaling=Decimal("1e-18")
    ),
    "0xe23665542fdd22de602eab11bb4d1ddbfb07e53b": TokenInfo(
        currency=CurrencyInfo(symbol="BRN", name="Brainmab"), scaling=Decimal("1e-18")
    ),
    "0xe23cd160761f63fc3a1cf78aa034b6cdf97d3e0c": TokenInfo(
        currency=CurrencyInfo(symbol="MIT", name="Mainstreet Token"), scaling=Decimal("1e-18")
    ),
    "0xe2492f8d2a2618d8709ca99b1d8d75713bd84089": TokenInfo(
        currency=CurrencyInfo(symbol="HB", name="HeartBout"), scaling=Decimal("1e-18")
    ),
    "0xe25b0bba01dc5630312b6a21927e578061a13f55": TokenInfo(
        currency=CurrencyInfo(symbol="SHIP", name="ShipChain"), scaling=Decimal("1e-18")
    ),
    "0xe25bcec5d3801ce3a794079bf94adf1b8ccd802d": TokenInfo(
        currency=CurrencyInfo(symbol="MAN", name="Matrix AI Network"), scaling=Decimal("1e-18")
    ),
    "0xe25faab5821ce70ba4179a70c1d481ba45b9d0c9": TokenInfo(
        currency=CurrencyInfo(symbol="ZMAN", name="ZMAN Coin"), scaling=Decimal("1e-8")
    ),
    "0xe26517a9967299453d3f1b48aa005e6127e67210": TokenInfo(
        currency=CurrencyInfo(symbol="NIMFA", name="NIMFA Token"), scaling=Decimal("1e-18")
    ),
    "0xe26668cc7ce5239304b5af8f54b4bd57d11084d2": TokenInfo(
        currency=CurrencyInfo(symbol="DAY", name="DAY"), scaling=Decimal("1e-18")
    ),
    "0xe26d6d83d8607ab016e3f8a5b00d91b0c9731840": TokenInfo(
        currency=CurrencyInfo(symbol="PT", name="Pet Token"), scaling=Decimal("1e-8")
    ),
    "0xe277ac35f9d327a670c1a3f3eec80a83022431e4": TokenInfo(
        currency=CurrencyInfo(symbol="PUX", name="PolypuX"), scaling=Decimal("1e-8")
    ),
    "0xe27fc04d0f239ddff43c4a2531d2a16c26ec014b": TokenInfo(
        currency=CurrencyInfo(symbol="PBF.CX", name="Pbf Energy Cl A"), scaling=Decimal("1e-8")
    ),
    "0xe28b3b32b6c345a34ff64674606124dd5aceca30": TokenInfo(
        currency=CurrencyInfo(symbol="INJ", name="Injective Protocol"), scaling=Decimal("1e-18")
    ),
    "0xe2ad8c40a00926023d0cb4d5c6a6306470524001": TokenInfo(
        currency=CurrencyInfo(symbol="SZC", name="SZC Wallet"), scaling=Decimal("1e-18")
    ),
    "0xe2b407160aad5540eac0e80338b9a5085c60f25b": TokenInfo(
        currency=CurrencyInfo(symbol="GPN", name="GPN COIN"), scaling=Decimal("1e-18")
    ),
    "0xe2b8c4938a3103c1ab5c19a6b93d07ab6f9da2ba": TokenInfo(
        currency=CurrencyInfo(symbol="CACXT", name="Convertible ACXT"), scaling=Decimal("1e-18")
    ),
    "0xe2bdd39a86a711a167967d04f39ac75e3ca14a08": TokenInfo(
        currency=CurrencyInfo(symbol="HTT", name="HOST TOKEN"), scaling=Decimal("1e-18")
    ),
    "0xe2d82dc7da0e6f882e96846451f4fabcc8f90528": TokenInfo(
        currency=CurrencyInfo(symbol="JC", name="Jesus Coin"), scaling=Decimal("1e-18")
    ),
    "0xe2db94e8d4e4144c336e45668a792d17d48a482c": TokenInfo(
        currency=CurrencyInfo(symbol="NUVO", name="Nuvo Cash"), scaling=Decimal("1e-18")
    ),
    "0xe2dc070524a6e305ddb64d8513dc444b6a1ec845": TokenInfo(
        currency=CurrencyInfo(symbol="NEX", name="Nash"), scaling=Decimal("1e-8")
    ),
    "0xe2e6d4be086c6938b53b22144855eef674281639": TokenInfo(
        currency=CurrencyInfo(symbol="LNK", name="Link Platform"), scaling=Decimal("1e-18")
    ),
    "0xe2ee1ac57b2e5564522b2de064a47b3f98b0e9c9": TokenInfo(
        currency=CurrencyInfo(symbol="WBT", name="Whalesburg"), scaling=Decimal("1e-18")
    ),
    "0xe2f2a5c287993345a840db3b0845fbc70f5935a5": TokenInfo(
        currency=CurrencyInfo(symbol="MUSD", name="mStable USD"), scaling=Decimal("1e-18")
    ),
    "0xe2f385f672d9a4fe44b172b9bdee023ac4732d77": TokenInfo(
        currency=CurrencyInfo(symbol="WILL", name="Octowill"), scaling=Decimal("1e-18")
    ),
    "0xe2fb6529ef566a080e6d23de0bd351311087d567": TokenInfo(
        currency=CurrencyInfo(symbol="COV", name="Covesting"), scaling=Decimal("1e-18")
    ),
    "0xe2fe5e7e206e7b46cad6a5146320e5b4b9a18e97": TokenInfo(
        currency=CurrencyInfo(symbol="BM", name="Bitcomo"), scaling=Decimal("1e-2")
    ),
    "0xe30e02f049957e2a5907589e06ba646fb2c321ba": TokenInfo(
        currency=CurrencyInfo(symbol="DRPU", name="DRP Utility"), scaling=Decimal("1e-8")
    ),
    "0xe3278df3eb2085ba9b6899812a99a10f9ca5e0df": TokenInfo(
        currency=CurrencyInfo(symbol="TOTO", name="Tourist Token"), scaling=Decimal("1e-8")
    ),
    "0xe340b25fe32b1011616bb8ec495a4d503e322177": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNIDAIUSDC", name="Aave AMM UniDAIUSDC"), scaling=Decimal("1e-18")
    ),
    "0xe34e1944e776f39b9252790a0527ebda647ae668": TokenInfo(
        currency=CurrencyInfo(symbol="HBZ", name="HBZ"), scaling=Decimal("1e-18")
    ),
    "0xe36e2d3c7c34281fa3bc737950a68571736880a1": TokenInfo(
        currency=CurrencyInfo(symbol="SADA", name="sADA"), scaling=Decimal("1e-18")
    ),
    "0xe3818504c1b32bf1557b16c238b2e01fd3149c17": TokenInfo(
        currency=CurrencyInfo(symbol="PLR", name="Pillar"), scaling=Decimal("1e-18")
    ),
    "0xe3831c5a982b279a198456d577cfb90424cb6340": TokenInfo(
        currency=CurrencyInfo(symbol="IMC", name="Immune Coin"), scaling=Decimal("1e-6")
    ),
    "0xe386b139ed3715ca4b18fd52671bdcea1cdfe4b1": TokenInfo(
        currency=CurrencyInfo(symbol="ZST", name="Zeus Token"), scaling=Decimal("1e-8")
    ),
    "0xe3a64a3c4216b83255b53ec7ea078b13f21a7dad": TokenInfo(
        currency=CurrencyInfo(symbol="DFGL", name="DeFi Gold"), scaling=Decimal("1e-18")
    ),
    "0xe3b05c42667de42ca4a4ea1e9682eb590b6a65d1": TokenInfo(
        currency=CurrencyInfo(symbol="OROM", name="Orom Token"), scaling=Decimal("1e-18")
    ),
    "0xe3bebaafa32767a7ee6102664079f11801586e1c": TokenInfo(
        currency=CurrencyInfo(symbol="NFT", name="National Fitness Token"), scaling=Decimal("1e-18")
    ),
    "0xe3c51fc064053ebc5a802e6f1d2897bf457c244f": TokenInfo(
        currency=CurrencyInfo(symbol="JAAG", name="Jaag Coin"), scaling=Decimal("1e-18")
    ),
    "0xe3c864307b5592404431649de541c259497e2bd1": TokenInfo(
        currency=CurrencyInfo(symbol="LOV", name="LoveChain"), scaling=Decimal("1e-8")
    ),
    "0xe3d0a162fcc5c02c9448274d7c58e18e1811385f": TokenInfo(
        currency=CurrencyInfo(symbol="MHLK", name="Maharlika Coin"), scaling=Decimal("1e-2")
    ),
    "0xe3f4b4a5d91e5cb9435b947f090a319737036312": TokenInfo(
        currency=CurrencyInfo(symbol="PCH", name="Popchain"), scaling=Decimal("1e-18")
    ),
    "0xe3fa177acecfb86721cf6f9f4206bd3bd672d7d5": TokenInfo(
        currency=CurrencyInfo(symbol="CTC", name="ChainTrade Coin"), scaling=Decimal("1e-18")
    ),
    "0xe3fb646fc31ca12657b17070bc31a52e323b8543": TokenInfo(
        currency=CurrencyInfo(symbol="eGLD", name="Elrond Gold"), scaling=Decimal("1e-18")
    ),
    "0xe3fedaecd47aa8eab6b23227b0ee56f092c967a9": TokenInfo(
        currency=CurrencyInfo(symbol="PST", name="Primas"), scaling=Decimal("1e-18")
    ),
    "0xe40c374d8805b1dd58cdceff998a2f6920cb52fd": TokenInfo(
        currency=CurrencyInfo(symbol="PRPS", name="Purpose"), scaling=Decimal("1e-18")
    ),
    "0xe41d2489571d322189246dafa5ebde1f4699f498": TokenInfo(
        currency=CurrencyInfo(symbol="ZRX", name="0x"), scaling=Decimal("1e-18")
    ),
    "0xe431a4c5db8b73c773e06cf2587da1eb53c41373": TokenInfo(
        currency=CurrencyInfo(symbol="TRY", name="Trias [Old Token]"), scaling=Decimal("1e-18")
    ),
    "0xe43e2041dc3786e166961ed9484a5539033d10fb": TokenInfo(
        currency=CurrencyInfo(symbol="DNX", name="DenCity"), scaling=Decimal("1e-18")
    ),
    "0xe452e6ea2ddeb012e20db73bf5d3863a3ac8d77a": TokenInfo(
        currency=CurrencyInfo(symbol="WCELO", name="Wrapped CELO"), scaling=Decimal("1e-18")
    ),
    "0xe45fc4290fd3159588f532058592ea327d2e97d4": TokenInfo(
        currency=CurrencyInfo(symbol="ACD", name="Alliance Cargo Direct"), scaling=Decimal("1e-18")
    ),
    "0xe463d1ee18bcbce681215d15738018eadaa82260": TokenInfo(
        currency=CurrencyInfo(symbol="FIIC", name="Film Industry Investment Chain"), scaling=Decimal("1e-0")
    ),
    "0xe469c4473af82217b30cf17b10bcdb6c8c796e75": TokenInfo(
        currency=CurrencyInfo(symbol="EXRN", name="EXRNchain"), scaling=Decimal("1e-0")
    ),
    "0xe46f290cd59195a83e757891430d8d517d16b334": TokenInfo(
        currency=CurrencyInfo(symbol="AFN", name="AltaFin"), scaling=Decimal("1e-18")
    ),
    "0xe470a51d750cff9e74252441b89b625121475049": TokenInfo(
        currency=CurrencyInfo(symbol="AUDF", name="AUDF"), scaling=Decimal("1e-6")
    ),
    "0xe477292f1b3268687a29376116b0ed27a9c76170": TokenInfo(
        currency=CurrencyInfo(symbol="PLAY", name="HEROcoin"), scaling=Decimal("1e-18")
    ),
    "0xe4815ae53b124e7263f08dcdbbb757d41ed658c6": TokenInfo(
        currency=CurrencyInfo(symbol="ZKS", name="ZKSwap"), scaling=Decimal("1e-18")
    ),
    "0xe4883bcb919386bb5f48ef59b7c31c1d93a51a57": TokenInfo(
        currency=CurrencyInfo(symbol="SPY", name="Satopay Yield Token"), scaling=Decimal("1e-18")
    ),
    "0xe48972fcd82a274411c01834e2f031d4377fa2c0": TokenInfo(
        currency=CurrencyInfo(symbol="2KEY", name="2key.network"), scaling=Decimal("1e-18")
    ),
    "0xe49214e4c92dc9bcb3b56c1309afe0d626dd730e": TokenInfo(
        currency=CurrencyInfo(symbol="SYC", name="SynchroLife"), scaling=Decimal("1e-18")
    ),
    "0xe4ae84448db5cfe1daf1e6fb172b469c161cb85f": TokenInfo(
        currency=CurrencyInfo(symbol="UOP", name="Utopia Genesis Foundation"), scaling=Decimal("1e-18")
    ),
    "0xe4c94d45f7aef7018a5d66f44af780ec6023378e": TokenInfo(
        currency=CurrencyInfo(symbol="CCRB", name="CCRB"), scaling=Decimal("1e-6")
    ),
    "0xe4cfe9eaa8cdb0942a80b7bc68fd8ab0f6d44903": TokenInfo(
        currency=CurrencyInfo(symbol="XEND", name="Xend Finance"), scaling=Decimal("1e-18")
    ),
    "0xe4e2daf5f7f0c1c35df922c5d9340913edecc8e8": TokenInfo(
        currency=CurrencyInfo(symbol="MNR", name="Mnoer"), scaling=Decimal("1e-18")
    ),
    "0xe4f726adc8e89c6a6017f01eada77865db22da14": TokenInfo(
        currency=CurrencyInfo(symbol="BCP", name="PieDAO Balanced Crypto Pie"), scaling=Decimal("1e-18")
    ),
    "0xe4f83110b59c0a751733263a870bb63b407ad0c0": TokenInfo(
        currency=CurrencyInfo(symbol="SPS", name="Share Public System"), scaling=Decimal("1e-3")
    ),
    "0xe50365f5d679cb98a1dd62d6f6e58e59321bcddf": TokenInfo(
        currency=CurrencyInfo(symbol="LA", name="LATOKEN"), scaling=Decimal("1e-18")
    ),
    "0xe52e75e8a97546f40991b489e92c68ebb386dc97": TokenInfo(
        currency=CurrencyInfo(symbol="ETHPAY", name="ETHPAY"), scaling=Decimal("1e-18")
    ),
    "0xe530441f4f73bdb6dc2fa5af7c3fc5fd551ec838": TokenInfo(
        currency=CurrencyInfo(symbol="GSE", name="GSENetwork"), scaling=Decimal("1e-4")
    ),
    "0xe531642e9bb5d027e9c20e03284287b97919a9a5": TokenInfo(
        currency=CurrencyInfo(symbol="FAITH", name="FaithCoin"), scaling=Decimal("1e-8")
    ),
    "0xe532a2a37b0707b4306b21b412d2e8c22f9824ec": TokenInfo(
        currency=CurrencyInfo(symbol="EUP", name="EUP Chain"), scaling=Decimal("1e-18")
    ),
    "0xe53ec727dbdeb9e2d5456c3be40cff031ab40a55": TokenInfo(
        currency=CurrencyInfo(symbol="SUPER", name="SuperFarm"), scaling=Decimal("1e-18")
    ),
    "0xe541b34f73a4789a033a962ad43655221b4e516e": TokenInfo(
        currency=CurrencyInfo(symbol="CMB", name="Creatanium"), scaling=Decimal("1e-18")
    ),
    "0xe54b3458c47e44c37a267e7c633afef88287c294": TokenInfo(
        currency=CurrencyInfo(symbol="AT", name="Artfinity Token"), scaling=Decimal("1e-5")
    ),
    "0xe54f9e6ab80ebc28515af8b8233c1aee6506a15e": TokenInfo(
        currency=CurrencyInfo(symbol="PASTA", name="Spaghetti"), scaling=Decimal("1e-18")
    ),
    "0xe55cc44c0cf9cede2d68f9432cbeeafa6357ed92": TokenInfo(
        currency=CurrencyInfo(symbol="ROZ", name="Rozeus"), scaling=Decimal("1e-8")
    ),
    "0xe57425f1598f9b0d6219706b77f4b3da573a3695": TokenInfo(
        currency=CurrencyInfo(symbol="BTCBR", name="Bitcoin BR"), scaling=Decimal("1e-18")
    ),
    "0xe5867608b51a2c9c78b9587355cc093140a49b0a": TokenInfo(
        currency=CurrencyInfo(symbol="SMS", name="Speed Mining Service"), scaling=Decimal("1e-3")
    ),
    "0xe5869a1ade66f0174c0fae6cd6cc303c54d7c738": TokenInfo(
        currency=CurrencyInfo(symbol="FNL", name="Finlocale"), scaling=Decimal("1e-18")
    ),
    "0xe58c8df0088cf27b26c7d546a9835deacc29496c": TokenInfo(
        currency=CurrencyInfo(symbol="TRXHEDGE", name="1X Short TRX Token"), scaling=Decimal("1e-18")
    ),
    "0xe58e8d254d17520ff1e7bf0cde3ae32bd795203b": TokenInfo(
        currency=CurrencyInfo(symbol="LKC", name="Liker World"), scaling=Decimal("1e-18")
    ),
    "0xe59064a8185ed1fca1d17999621efedfab4425c9": TokenInfo(
        currency=CurrencyInfo(symbol="PRIME", name="PrimeDAO"), scaling=Decimal("1e-18")
    ),
    "0xe59d2ff6995a926a574390824a657eed36801e55": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMUNIAAVEWETH", name="Aave AMM UniAAVEWET"), scaling=Decimal("1e-18")
    ),
    "0xe5a09784b16e1065c37df14c6e2f06fdce317a1b": TokenInfo(
        currency=CurrencyInfo(symbol="KaiInu", name="KaiInu"), scaling=Decimal("1e-9")
    ),
    "0xe5a3229ccb22b6484594973a03a3851dcd948756": TokenInfo(
        currency=CurrencyInfo(symbol="RAE", name="Receive Access Ecosystem"), scaling=Decimal("1e-18")
    ),
    "0xe5a7c12972f3bbfe70ed29521c8949b8af6a0970": TokenInfo(
        currency=CurrencyInfo(symbol="BLX", name="Blockchain Index"), scaling=Decimal("1e-18")
    ),
    "0xe5a9f7d738a839e93e611b9bfa19251542c72427": TokenInfo(
        currency=CurrencyInfo(symbol="GOCO", name="Gocoworker"), scaling=Decimal("1e-18")
    ),
    "0xe5aee163513119f4f750376c718766b40fa37a5f": TokenInfo(
        currency=CurrencyInfo(symbol="FZ", name="Frozencoin Network"), scaling=Decimal("1e-18")
    ),
    "0xe5b826ca2ca02f09c1725e9bd98d9a8874c30532": TokenInfo(
        currency=CurrencyInfo(symbol="ZEON", name="ZEON Network"), scaling=Decimal("1e-18")
    ),
    "0xe5bafc0e45973259bce6923ec884680867332447": TokenInfo(
        currency=CurrencyInfo(symbol="RBC", name="Reibex Coin"), scaling=Decimal("1e-18")
    ),
    "0xe5bf6790d138b154f1df3db8d245be46a5d05ee4": TokenInfo(
        currency=CurrencyInfo(symbol="LLAND", name="Lyfe Land"), scaling=Decimal("1e-18")
    ),
    "0xe5caef4af8780e59df925470b050fb23c43ca68c": TokenInfo(
        currency=CurrencyInfo(symbol="FRM", name="Ferrum Network"), scaling=Decimal("1e-6")
    ),
    "0xe5dada80aa6477e85d09747f2842f7993d0df71c": TokenInfo(
        currency=CurrencyInfo(symbol="DOCK", name="Dock"), scaling=Decimal("1e-18")
    ),
    "0xe5e36647efde7951e95fd612ea23803aff2a1b83": TokenInfo(
        currency=CurrencyInfo(symbol="STM.CX", name="Stmicroelectronics Adr"), scaling=Decimal("1e-8")
    ),
    "0xe5f166c0d8872b68790061317bb6cca04582c912": TokenInfo(
        currency=CurrencyInfo(symbol="TFD", name="TE-FOOD"), scaling=Decimal("1e-18")
    ),
    "0xe5f7ef61443fc36ae040650aa585b0395aef77c8": TokenInfo(
        currency=CurrencyInfo(
            symbol="REALTOKEN-9943-MARLOWE-ST-DETROIT-MI", name="RealToken 9943 Marlowe Street Detroit MI"
        ),
        scaling=Decimal("1e-18"),
    ),
    "0xe5f867de1ea81346df5181b8b48dd6b0bb3357b0": TokenInfo(
        currency=CurrencyInfo(symbol="BTZ", name="BTZ by Bunz"), scaling=Decimal("1e-18")
    ),
    "0xe60573eee9daff7a1ab1540b81b08cf2a3d51611": TokenInfo(
        currency=CurrencyInfo(symbol="BILL.CX", name="Bill.com Inc"), scaling=Decimal("1e-8")
    ),
    "0xe60b3fcbd8f400a38476adeb01fcac861ccd2e42": TokenInfo(
        currency=CurrencyInfo(symbol="XCMG", name="Connect Mining Token"), scaling=Decimal("1e-18")
    ),
    "0xe6179bb571d2d69837be731da88c76e377ec4738": TokenInfo(
        currency=CurrencyInfo(symbol="WHOLE", name="Wormhole.Finance"), scaling=Decimal("1e-18")
    ),
    "0xe61eecfdba2ad1669cee138f1919d08ced070b83": TokenInfo(
        currency=CurrencyInfo(symbol="VGTG", name="VGTGToken"), scaling=Decimal("1e-18")
    ),
    "0xe61fdaf474fac07063f2234fb9e60c1163cfa850": TokenInfo(
        currency=CurrencyInfo(symbol="COIN", name="Coin"), scaling=Decimal("1e-18")
    ),
    "0xe632ea2ef2cfd8fc4a2731c76f99078aef6a4b31": TokenInfo(
        currency=CurrencyInfo(symbol="THX", name="THX Network"), scaling=Decimal("1e-18")
    ),
    "0xe6354ed5bc4b393a5aad09f21c46e101e692d447": TokenInfo(
        currency=CurrencyInfo(symbol="yUSDT", name="iearn USDT"), scaling=Decimal("1e-6")
    ),
    "0xe638dc39b6adbee8526b5c22380b4b45daf46d8e": TokenInfo(
        currency=CurrencyInfo(symbol="GZR", name="Gizer"), scaling=Decimal("1e-6")
    ),
    "0xe63d6b308bce0f6193aec6b7e6eba005f41e36ab": TokenInfo(
        currency=CurrencyInfo(symbol="STN", name="Stone Token"), scaling=Decimal("1e-18")
    ),
    "0xe6404a4472e5222b440f8fafb795553046000841": TokenInfo(
        currency=CurrencyInfo(symbol="BLOAP", name="BTC Long-Only Alpha Portfolio"), scaling=Decimal("1e-18")
    ),
    "0xe6410569602124506658ff992f258616ea2d4a3d": TokenInfo(
        currency=CurrencyInfo(symbol="KATANA", name="Katana Finance"), scaling=Decimal("1e-18")
    ),
    "0xe64509f0bf07ce2d29a7ef19a8a9bc065477c1b4": TokenInfo(
        currency=CurrencyInfo(symbol="PIPL", name="PiplCoin"), scaling=Decimal("1e-8")
    ),
    "0xe649cd5f867ce87bd361d36a8ed4f7a87462042d": TokenInfo(
        currency=CurrencyInfo(symbol="SDC.CX", name="SmileDirectClub Inc"), scaling=Decimal("1e-8")
    ),
    "0xe64b47931f28f89cc7a0c6965ecf89eadb4975f5": TokenInfo(
        currency=CurrencyInfo(symbol="LUD", name="Ludos Protocol"), scaling=Decimal("1e-18")
    ),
    "0xe650cac294202d1b6221a84d5a26a8671071a076": TokenInfo(
        currency=CurrencyInfo(symbol="W.CX", name="Wayfair Cl A"), scaling=Decimal("1e-8")
    ),
    "0xe65ee7c03bbb3c950cfd4895c24989afa233ef01": TokenInfo(
        currency=CurrencyInfo(symbol="ZYN", name="Zynecoin"), scaling=Decimal("1e-18")
    ),
    "0xe666bcf60bdcfdc66fea10f27eab84e3f255ef72": TokenInfo(
        currency=CurrencyInfo(symbol="DFINE", name="DalecoinFinance"), scaling=Decimal("1e-18")
    ),
    "0xe66747a101bff2dba3697199dcce5b743b454759": TokenInfo(
        currency=CurrencyInfo(symbol="GT", name="GateToken"), scaling=Decimal("1e-18")
    ),
    "0xe66f7261f72861e3399eb15424f2f2a2e976cab3": TokenInfo(
        currency=CurrencyInfo(symbol="SSC", name="SilverStone"), scaling=Decimal("1e-18")
    ),
    "0xe6710e0cda178f3d921f456902707b0d4c4a332b": TokenInfo(
        currency=CurrencyInfo(symbol="JULIEN", name="JULIEN"), scaling=Decimal("1e-4")
    ),
    "0xe6877ea9c28fbdec631ffbc087956d0023a76bf2": TokenInfo(
        currency=CurrencyInfo(symbol="UNI", name="UNI COIN"), scaling=Decimal("1e-18")
    ),
    "0xe6923e9b56db1eed1c9f430ea761da7565e260fe": TokenInfo(
        currency=CurrencyInfo(symbol="FC", name="Facecoin"), scaling=Decimal("1e-2")
    ),
    "0xe692c8d72bd4ac7764090d54842a305546dd1de5": TokenInfo(
        currency=CurrencyInfo(symbol="ABLOCK", name="ANY Blocknet"), scaling=Decimal("1e-8")
    ),
    "0xe69a353b3152dd7b706ff7dd40fe1d18b7802d31": TokenInfo(
        currency=CurrencyInfo(symbol="ADH", name="AdHive"), scaling=Decimal("1e-18")
    ),
    "0xe6a9e1bec166f50eda336d02df2662d4eb8ab23c": TokenInfo(
        currency=CurrencyInfo(symbol="LIQ", name="Liquid Bank"), scaling=Decimal("1e-18")
    ),
    "0xe6b75a1960f91bfa7010dec8543685ead67f8cff": TokenInfo(
        currency=CurrencyInfo(symbol="SCC", name="Sea Cucumber Chain"), scaling=Decimal("1e-18")
    ),
    "0xe6bc60a00b81c7f3cbc8f4ef3b0a6805b6851753": TokenInfo(
        currency=CurrencyInfo(symbol="ICST", name="Individual Content and Skill Token"), scaling=Decimal("1e-18")
    ),
    "0xe6ca8989544337da2283232feb36f442b1aa3cab": TokenInfo(
        currency=CurrencyInfo(symbol="1COV.CX", name="Covestro AG"), scaling=Decimal("1e-8")
    ),
    "0xe6d2a9fcd946e07826c6cdd919da04763ea4d812": TokenInfo(
        currency=CurrencyInfo(symbol="BRUH", name="Bruh"), scaling=Decimal("1e-18")
    ),
    "0xe6d2c3cb986db66818c14c7032db05d1d2a6ee74": TokenInfo(
        currency=CurrencyInfo(symbol="FNB", name="FinexboxToken"), scaling=Decimal("1e-8")
    ),
    "0xe6dfbf1faca95036b8e76e1fb28933d025b76cc0": TokenInfo(
        currency=CurrencyInfo(symbol="LIBER", name="Libereum"), scaling=Decimal("1e-18")
    ),
    "0xe6f74dcfa0e20883008d8c16b6d9a329189d0c30": TokenInfo(
        currency=CurrencyInfo(symbol="FTC", name="FinTech Coin"), scaling=Decimal("1e-2")
    ),
    "0xe6fd75ff38adca4b97fbcd938c86b98772431867": TokenInfo(
        currency=CurrencyInfo(symbol="ELA", name="Elastos"), scaling=Decimal("1e-18")
    ),
    "0xe70be6622d2316003d07a659dbbdb47241a68ff7": TokenInfo(
        currency=CurrencyInfo(symbol="EMOJI", name="Emojitoken"), scaling=Decimal("1e-18")
    ),
    "0xe71458296ce66f7e8c8df694569b519013f3bd3c": TokenInfo(
        currency=CurrencyInfo(symbol="UNI-V2", name="UNI-V2"), scaling=Decimal("1e-18")
    ),
    "0xe748269494e76c1cec3f627bb1e561e607da9161": TokenInfo(
        currency=CurrencyInfo(symbol="XELS", name="XELS"), scaling=Decimal("1e-8")
    ),
    "0xe74dc43867e0cbeb208f1a012fc60dcbbf0e3044": TokenInfo(
        currency=CurrencyInfo(symbol="CWAP", name="DeFIRE"), scaling=Decimal("1e-18")
    ),
    "0xe75ad3aab14e4b0df8c5da4286608dabb21bd864": TokenInfo(
        currency=CurrencyInfo(symbol="AAC", name="Acute Angle Cloud"), scaling=Decimal("1e-5")
    ),
    "0xe76c6c83af64e4c60245d8c7de953df673a7a33d": TokenInfo(
        currency=CurrencyInfo(symbol="RAIL", name="Railgun"), scaling=Decimal("1e-18")
    ),
    "0xe7750c38c9a10d877650c0d99d1717bb28a5c42e": TokenInfo(
        currency=CurrencyInfo(symbol="ZIK", name="Ziktalk Token"), scaling=Decimal("1e-18")
    ),
    "0xe7775a6e9bcf904eb39da2b68c5efb4f9360e08c": TokenInfo(
        currency=CurrencyInfo(symbol="TAAS", name="TaaS"), scaling=Decimal("1e-6")
    ),
    "0xe77dbb83deb90749486a1d94fc47e1f42b55562b": TokenInfo(
        currency=CurrencyInfo(symbol="SAGE.CX", name="Sage Therapeutics Inc"), scaling=Decimal("1e-8")
    ),
    "0xe796d6ca1ceb1b022ece5296226bf784110031cd": TokenInfo(
        currency=CurrencyInfo(symbol="BLES", name="Blind Boxes"), scaling=Decimal("1e-18")
    ),
    "0xe7976c4efc60d9f4c200cc1bcef1a1e3b02c73e7": TokenInfo(
        currency=CurrencyInfo(symbol="MAX", name="MAX Token"), scaling=Decimal("1e-18")
    ),
    "0xe79a9bc076523660c7393d5576700d922f7dcea5": TokenInfo(
        currency=CurrencyInfo(symbol="BEL", name="Bitexlive Coin"), scaling=Decimal("1e-8")
    ),
    "0xe79e177d2a5c7085027d7c64c8f271c81430fc9b": TokenInfo(
        currency=CurrencyInfo(symbol="idleSUSDYield", name="IdleSUSD v3 [Max yield]"), scaling=Decimal("1e-18")
    ),
    "0xe7c6708bf942a80c9a5811033a2a68205b034486": TokenInfo(
        currency=CurrencyInfo(symbol="TWBT", name="TheWatcherBotToken"), scaling=Decimal("1e-18")
    ),
    "0xe7c7036c5c532180ee9d240b87b713bce797d0ae": TokenInfo(
        currency=CurrencyInfo(symbol="VOO.CX", name="Vanguard S&P 500 ETF"), scaling=Decimal("1e-8")
    ),
    "0xe7c9c188138f7d70945d420d75f8ca7d8ab9c700": TokenInfo(
        currency=CurrencyInfo(symbol="BSDS", name="Basis Dollar Share"), scaling=Decimal("1e-18")
    ),
    "0xe7d324b2677440608fb871981b220eca062c3fbf": TokenInfo(
        currency=CurrencyInfo(symbol="BVL", name="Bullswap Protocol"), scaling=Decimal("1e-18")
    ),
    "0xe7d3e4413e29ae35b0893140f4500965c74365e5": TokenInfo(
        currency=CurrencyInfo(symbol="BBC", name="TraDove B2BCoin"), scaling=Decimal("1e-18")
    ),
    "0xe7d7b37e72510309db27c460378f957b1b04bd5d": TokenInfo(
        currency=CurrencyInfo(symbol="EMPR", name="empowr Coin"), scaling=Decimal("1e-18")
    ),
    "0xe7e4279b80d319ede2889855135a22021baf0907": TokenInfo(
        currency=CurrencyInfo(symbol="ZEUS", name="ZeusNetwork"), scaling=Decimal("1e-18")
    ),
    "0xe7e6c560c7e07b9fdbe8f88ed8c0988b1fec055d": TokenInfo(
        currency=CurrencyInfo(symbol="YOLO.CX", name="AdvisorShares Pure Cannabis ETF"), scaling=Decimal("1e-8")
    ),
    "0xe7f72bc0252ca7b16dbb72eeee1afcdb2429f2dd": TokenInfo(
        currency=CurrencyInfo(symbol="NFTL", name="NFTLaunch"), scaling=Decimal("1e-18")
    ),
    "0xe814aee960a85208c3db542c53e7d4a6c8d5f60f": TokenInfo(
        currency=CurrencyInfo(symbol="DAY", name="Chronologic"), scaling=Decimal("1e-18")
    ),
    "0xe81d72d14b1516e68ac3190a46c93302cc8ed60f": TokenInfo(
        currency=CurrencyInfo(symbol="CL", name="Coinlancer"), scaling=Decimal("1e-18")
    ),
    "0xe83e098eedb43b33d340d4757529e5a2c4ee3230": TokenInfo(
        currency=CurrencyInfo(symbol="BOON", name="Boon Tech"), scaling=Decimal("1e-18")
    ),
    "0xe860b123b38306b0f3409bdbb6a8fe85ed61c6d4": TokenInfo(
        currency=CurrencyInfo(symbol="SHOP", name="SHOPCOIN"), scaling=Decimal("1e-0")
    ),
    "0xe8663a64a96169ff4d95b4299e7ae9a76b905b31": TokenInfo(
        currency=CurrencyInfo(symbol="RATING", name="DPRating"), scaling=Decimal("1e-8")
    ),
    "0xe86811516f9e46f6f2a8a19754c893ded414d682": TokenInfo(
        currency=CurrencyInfo(symbol="ICHIEMA", name="12H Ichimoku HA EMA Breakout Set"), scaling=Decimal("1e-18")
    ),
    "0xe8780b48bdb05f928697a5e8155f672ed91462f7": TokenInfo(
        currency=CurrencyInfo(symbol="CAS", name="Cashaa"), scaling=Decimal("1e-18")
    ),
    "0xe884cc2795b9c45beeac0607da9539fd571ccf85": TokenInfo(
        currency=CurrencyInfo(symbol="ULT", name="Ultiledger"), scaling=Decimal("1e-18")
    ),
    "0xe88f8313e61a97cec1871ee37fbbe2a8bf3ed1e4": TokenInfo(
        currency=CurrencyInfo(symbol="VAL", name="Sora Validator Token"), scaling=Decimal("1e-18")
    ),
    "0xe88fff42196f5a47ffc1ba2854c14e8eee4bfd05": TokenInfo(
        currency=CurrencyInfo(symbol="VTM", name="Victorieum"), scaling=Decimal("1e-18")
    ),
    "0xe8a1df958be379045e2b46a31a98b93a2ecdfded": TokenInfo(
        currency=CurrencyInfo(symbol="ESZ", name="EtherSportz"), scaling=Decimal("1e-18")
    ),
    "0xe8b251822d003a2b2466ee0e38391c2db2048739": TokenInfo(
        currency=CurrencyInfo(symbol="RBASE", name="rbase.finance"), scaling=Decimal("1e-9")
    ),
    "0xe8c09672cfb9cfce6e2edbb01057d9fa569f97c1": TokenInfo(
        currency=CurrencyInfo(symbol="INDI", name="Indicoin"), scaling=Decimal("1e-18")
    ),
    "0xe8d17542dfe79ff4fbd4b850f2d39dc69c4489a2": TokenInfo(
        currency=CurrencyInfo(symbol="KMPL", name="KiloAmple"), scaling=Decimal("1e-9")
    ),
    "0xe8d1efd0c95011298e9a30143a0182c06b45ff5d": TokenInfo(
        currency=CurrencyInfo(symbol="SION", name="SION"), scaling=Decimal("1e-9")
    ),
    "0xe8e29fa0e8b21f6791ad9f65347d806d4f47d063": TokenInfo(
        currency=CurrencyInfo(symbol="BMW.CX", name="BMW AG"), scaling=Decimal("1e-8")
    ),
    "0xe8ed08a581777f112654e28de507e11613da0379": TokenInfo(
        currency=CurrencyInfo(symbol="YFC", name="Yearn Finance Center"), scaling=Decimal("1e-18")
    ),
    "0xe8f8378f02dd54153aa21d93673f291322222714": TokenInfo(
        currency=CurrencyInfo(symbol="PYD", name="PayPDM Coin"), scaling=Decimal("1e-18")
    ),
    "0xe8f9fa977ea585591d9f394681318c16552577fb": TokenInfo(
        currency=CurrencyInfo(symbol="ZTX", name="Zulu Republic Token"), scaling=Decimal("1e-18")
    ),
    "0xe8ff5c9c75deb346acac493c463c8950be03dfba": TokenInfo(
        currency=CurrencyInfo(symbol="VIBE", name="VIBE"), scaling=Decimal("1e-18")
    ),
    "0xe912b8ba2513d7e29b7b2e5b14398dbf77503fb4": TokenInfo(
        currency=CurrencyInfo(symbol="VNT", name="InventoryClub"), scaling=Decimal("1e-18")
    ),
    "0xe933c0cd9784414d5f278c114904f5a84b396919": TokenInfo(
        currency=CurrencyInfo(symbol="WHO", name="WhoHas"), scaling=Decimal("1e-18")
    ),
    "0xe947b388fbe682784170b62f2bd4665f9719a285": TokenInfo(
        currency=CurrencyInfo(symbol="RALLY", name="Rally [Old]"), scaling=Decimal("1e-18")
    ),
    "0xe9541c7ea236332f4d07be73101670f39b27da02": TokenInfo(
        currency=CurrencyInfo(symbol="PLD", name="Pureland Project"), scaling=Decimal("1e-18")
    ),
    "0xe95990825aab1a7f0af4cc648f76a3bcc99f25b2": TokenInfo(
        currency=CurrencyInfo(symbol="ZNT", name="Zenswap Network Token"), scaling=Decimal("1e-18")
    ),
    "0xe95a203b1a91a908f9b9ce46459d101078c2c3cb": TokenInfo(
        currency=CurrencyInfo(symbol="AETH", name="ankrETH"), scaling=Decimal("1e-18")
    ),
    "0xe96bfebe8b8c85540519c57c06ab96f7435dc184": TokenInfo(
        currency=CurrencyInfo(symbol="KHC.CX", name="The Kraft Heinz Company"), scaling=Decimal("1e-8")
    ),
    "0xe99a76d5fb19bc419d72f355050045fad88e060f": TokenInfo(
        currency=CurrencyInfo(symbol="RAZ", name="RAZ Token"), scaling=Decimal("1e-18")
    ),
    "0xe99a894a69d7c2e3c92e61b64c505a6a57d2bc07": TokenInfo(
        currency=CurrencyInfo(symbol="HYN", name="Hyperion"), scaling=Decimal("1e-18")
    ),
    "0xe9c9e7e1dabea830c958c39d6b25964a6f52143a": TokenInfo(
        currency=CurrencyInfo(symbol="HEY", name="HeyToken"), scaling=Decimal("1e-18")
    ),
    "0xe9f3cb0229eb8d0aaf03ec84883950134ed20ddc": TokenInfo(
        currency=CurrencyInfo(symbol="SLT", name="SLT"), scaling=Decimal("1e-8")
    ),
    "0xe9f84de264e91529af07fa2c746e934397810334": TokenInfo(
        currency=CurrencyInfo(symbol="SAK3", name="SAK3"), scaling=Decimal("1e-18")
    ),
    "0xe9fa21e671bcfb04e6868784b89c19d5aa2424ea": TokenInfo(
        currency=CurrencyInfo(symbol="ECTE", name="EurocoinToken"), scaling=Decimal("1e-18")
    ),
    "0xe9fba30ff18d305fea49836939eaca55f26c019c": TokenInfo(
        currency=CurrencyInfo(symbol="ISLAINU", name="Island Inu"), scaling=Decimal("1e-9")
    ),
    "0xe9ff07809ccff05dae74990e25831d0bc5cbe575": TokenInfo(
        currency=CurrencyInfo(symbol="Hdp.ф", name="HEDPAY"), scaling=Decimal("1e-18")
    ),
    "0xea004e8fa3701b8e58e41b78d50996e0f7176cbd": TokenInfo(
        currency=CurrencyInfo(symbol="YFFC", name="yffc.finance"), scaling=Decimal("1e-18")
    ),
    "0xea097a2b1db00627b2fa17460ad260c016016977": TokenInfo(
        currency=CurrencyInfo(symbol="UFR", name="Upfiring"), scaling=Decimal("1e-18")
    ),
    "0xea11755ae41d889ceec39a63e6ff75a02bc1c00d": TokenInfo(
        currency=CurrencyInfo(symbol="CTXC", name="Cortex"), scaling=Decimal("1e-18")
    ),
    "0xea1ea0972fa092dd463f2968f9bb51cc4c981d71": TokenInfo(
        currency=CurrencyInfo(symbol="MOD", name="Modefi"), scaling=Decimal("1e-18")
    ),
    "0xea1f346faf023f974eb5adaf088bbcdf02d761f4": TokenInfo(
        currency=CurrencyInfo(symbol="TIX", name="Blocktix"), scaling=Decimal("1e-18")
    ),
    "0xea2524bb0773de6a5f641aa97294401f116572e7": TokenInfo(
        currency=CurrencyInfo(symbol="XMD", name="XMD Token"), scaling=Decimal("1e-8")
    ),
    "0xea26c4ac16d4a5a106820bc8aee85fd0b7b2b664": TokenInfo(
        currency=CurrencyInfo(symbol="QKC", name="QuarkChain"), scaling=Decimal("1e-18")
    ),
    "0xea319e87cf06203dae107dd8e5672175e3ee976c": TokenInfo(
        currency=CurrencyInfo(symbol="SURF", name="Surf.Finance"), scaling=Decimal("1e-18")
    ),
    "0xea38eaa3c86c8f9b751533ba2e562deb9acded40": TokenInfo(
        currency=CurrencyInfo(symbol="FUEL", name="Etherparty"), scaling=Decimal("1e-18")
    ),
    "0xea3983fc6d0fbbc41fb6f6091f68f3e08894dc06": TokenInfo(
        currency=CurrencyInfo(symbol="UDO", name="Unido"), scaling=Decimal("1e-18")
    ),
    "0xea4931bfcf3260da6dbf0550e27f5c214e3c268b": TokenInfo(
        currency=CurrencyInfo(symbol="MOZOX", name="MozoX"), scaling=Decimal("1e-2")
    ),
    "0xea54c81fe0f72de8e86b6dc78a9271aa3925e3b5": TokenInfo(
        currency=CurrencyInfo(symbol="BGG", name="Bgogo Token"), scaling=Decimal("1e-18")
    ),
    "0xea5f88e54d982cbb0c441cde4e79bc305e5b43bc": TokenInfo(
        currency=CurrencyInfo(symbol="PARETO", name="PARETO Rewards"), scaling=Decimal("1e-18")
    ),
    "0xea610b1153477720748dc13ed378003941d84fab": TokenInfo(
        currency=CurrencyInfo(symbol="ALIS", name="ALIS"), scaling=Decimal("1e-18")
    ),
    "0xea6412fb370e8d1605e6aeeaa21ad07c3c7e9f24": TokenInfo(
        currency=CurrencyInfo(symbol="MUSH", name="Mushroom"), scaling=Decimal("1e-18")
    ),
    "0xea7aa1edd21735a5ab05ee3e90869016191e274e": TokenInfo(
        currency=CurrencyInfo(symbol="JCC", name="JCC"), scaling=Decimal("1e-18")
    ),
    "0xea8df5308e7463c555047fcd612decfae7d71058": TokenInfo(
        currency=CurrencyInfo(symbol="FVRR.CX", name="Fiverr International Ltd"), scaling=Decimal("1e-8")
    ),
    "0xeaa088ccc8254795cb372000bda9b11e075e1dd0": TokenInfo(
        currency=CurrencyInfo(symbol="GRMN.CX", name="Garmin Ltd"), scaling=Decimal("1e-8")
    ),
    "0xeab43193cf0623073ca89db9b712796356fa7414": TokenInfo(
        currency=CurrencyInfo(symbol="GOLDX", name="GOLDX"), scaling=Decimal("1e-18")
    ),
    "0xeabacd844a196d7faf3ce596edebf9900341b420": TokenInfo(
        currency=CurrencyInfo(symbol="SCEX", name="sCEX"), scaling=Decimal("1e-18")
    ),
    "0xeabb8996ea1662cad2f7fb715127852cd3262ae9": TokenInfo(
        currency=CurrencyInfo(symbol="CNFI", name="Connect Financial"), scaling=Decimal("1e-18")
    ),
    "0xeaccb6e0f24d66cf4aa6cbda33971b9231d332a1": TokenInfo(
        currency=CurrencyInfo(symbol="PGT", name="Polyient Games Governance Token"), scaling=Decimal("1e-18")
    ),
    "0xead7f3ae4e0bb0d8785852cc37cc9d0b5e75c06a": TokenInfo(
        currency=CurrencyInfo(symbol="EOSBULL", name="3X Long EOS Token"), scaling=Decimal("1e-18")
    ),
    "0xeadd9b69f96140283f9ff75da5fd33bcf54e6296": TokenInfo(
        currency=CurrencyInfo(symbol="CYCE", name="Crypto Carbon Energ"), scaling=Decimal("1e-6")
    ),
    "0xeaf61fc150cd5c3bea75744e830d916e60ea5a9f": TokenInfo(
        currency=CurrencyInfo(symbol="TYPE", name="Typerium"), scaling=Decimal("1e-4")
    ),
    "0xeaf7d8395cce52daef138d39a1cefa51b97c15ae": TokenInfo(
        currency=CurrencyInfo(symbol="TBC", name="TBC"), scaling=Decimal("1e-18")
    ),
    "0xeb269732ab75a6fd61ea60b06fe994cd32a83549": TokenInfo(
        currency=CurrencyInfo(symbol="USDX", name="USDx Stablecoin"), scaling=Decimal("1e-18")
    ),
    "0xeb2c0e11af20fb1c41c6e7abe5ad214e48738514": TokenInfo(
        currency=CurrencyInfo(symbol="SINE", name="Sinelock"), scaling=Decimal("1e-18")
    ),
    "0xeb4c2781e4eba804ce9a9803c67d0893436bb27d": TokenInfo(
        currency=CurrencyInfo(symbol="RENBTC", name="renBTC"), scaling=Decimal("1e-8")
    ),
    "0xeb547ed1d8a3ff1461abaa7f0022fed4836e00a4": TokenInfo(
        currency=CurrencyInfo(symbol="COIN", name="Coinvest COIN V3 Token"), scaling=Decimal("1e-18")
    ),
    "0xeb6985acd6d0cbff60b88032b0b29ac1d9d66a1b": TokenInfo(
        currency=CurrencyInfo(symbol="BXK", name="Bitbook Gambling"), scaling=Decimal("1e-18")
    ),
    "0xeb7c20027172e5d143fb030d50f91cece2d1485d": TokenInfo(
        currency=CurrencyInfo(symbol="EBTC", name="eBitcoin"), scaling=Decimal("1e-8")
    ),
    "0xeb85a7b3fed933ec3b4599f1b4f8f3f838d0bedf": TokenInfo(
        currency=CurrencyInfo(symbol="ALMX", name="Almace Shards"), scaling=Decimal("1e-18")
    ),
    "0xeb953eda0dc65e3246f43dc8fa13f35623bdd5ed": TokenInfo(
        currency=CurrencyInfo(symbol="RAINI", name="Rainicorn"), scaling=Decimal("1e-18")
    ),
    "0xeb9951021698b42e4399f9cbb6267aa35f82d59d": TokenInfo(
        currency=CurrencyInfo(symbol="LIF", name="Lif"), scaling=Decimal("1e-18")
    ),
    "0xeb9a4b185816c354db92db09cc3b50be60b901b6": TokenInfo(
        currency=CurrencyInfo(symbol="ORS", name="Origin Sport"), scaling=Decimal("1e-18")
    ),
    "0xebbbe2ae55c9b2e21b09239362f3eee69455934d": TokenInfo(
        currency=CurrencyInfo(symbol="RES", name="Resistance"), scaling=Decimal("1e-8")
    ),
    "0xebbdf302c940c6bfd49c6b165f457fdb324649bc": TokenInfo(
        currency=CurrencyInfo(symbol="HYDRO", name="Hydro"), scaling=Decimal("1e-18")
    ),
    "0xebd01df7e1e56e89a52c5de185377d3a2eef9a2b": TokenInfo(
        currency=CurrencyInfo(symbol="FHT", name="Flamehyre Token"), scaling=Decimal("1e-8")
    ),
    "0xebd9d99a3982d547c5bb4db7e3b1f9f14b67eb83": TokenInfo(
        currency=CurrencyInfo(symbol="ID", name="Everest"), scaling=Decimal("1e-18")
    ),
    "0xebe4a49df7885d015329c919bf43e6460a858f1e": TokenInfo(
        currency=CurrencyInfo(symbol="SHK", name="iShook"), scaling=Decimal("1e-18")
    ),
    "0xebed4ff9fe34413db8fc8294556bbd1528a4daca": TokenInfo(
        currency=CurrencyInfo(symbol="VENUS", name="VENUS"), scaling=Decimal("1e-3")
    ),
    "0xebf2f9e8de960f64ec0fdcda6cb282423133347b": TokenInfo(
        currency=CurrencyInfo(symbol="CNB", name="Canabio"), scaling=Decimal("1e-8")
    ),
    "0xebf4ca5319f406602eeff68da16261f1216011b5": TokenInfo(
        currency=CurrencyInfo(symbol="YO", name="Yobit Token"), scaling=Decimal("1e-18")
    ),
    "0xebfc4fa869a6db3cbd6a849b5b656bae4aba68f0": TokenInfo(
        currency=CurrencyInfo(symbol="MVC", name="MaiVangCity"), scaling=Decimal("1e-0")
    ),
    "0xec02cec4edd54196d2767b61f43b29a49b056fe6": TokenInfo(
        currency=CurrencyInfo(symbol="UNIF", name="Unifier"), scaling=Decimal("1e-7")
    ),
    "0xec0a0915a7c3443862b678b0d4721c7ab133fdcf": TokenInfo(
        currency=CurrencyInfo(symbol="WOA", name="Wrapped Origin Axie"), scaling=Decimal("1e-18")
    ),
    "0xec18f898b4076a3e18f1089d33376cc380bde61d": TokenInfo(
        currency=CurrencyInfo(symbol="PETRO", name="Petro"), scaling=Decimal("1e-18")
    ),
    "0xec193241dc1ca3bbe3165de6d37a793585b4504e": TokenInfo(
        currency=CurrencyInfo(symbol="EVE", name="EMP"), scaling=Decimal("1e-18")
    ),
    "0xec1a718d1a6f8f8d94ecec6fe91465697bb2b88c": TokenInfo(
        currency=CurrencyInfo(symbol="ENTONE", name="Entone"), scaling=Decimal("1e-8")
    ),
    "0xec1b7eb3d3cfac7027fa60b5376e5eadef4f1300": TokenInfo(
        currency=CurrencyInfo(symbol="HZM", name="HZMCoin"), scaling=Decimal("1e-8")
    ),
    "0xec1cad815b5e8f0f86bb8fb2add2774886e79cf0": TokenInfo(
        currency=CurrencyInfo(symbol="FCL", name="Free Crypto Lotto"), scaling=Decimal("1e-18")
    ),
    "0xec213f83defb583af3a000b1c0ada660b1902a0f": TokenInfo(
        currency=CurrencyInfo(symbol="PRE", name="Presearch"), scaling=Decimal("1e-18")
    ),
    "0xec2da10f32aa3844a981108887d7e50efb7e2425": TokenInfo(
        currency=CurrencyInfo(symbol="AAP.CX", name="Advance Auto Parts"), scaling=Decimal("1e-8")
    ),
    "0xec32a9725c59855d841ba7d8d9c99c84ff754688": TokenInfo(
        currency=CurrencyInfo(symbol="TEL", name="Meditel"), scaling=Decimal("1e-18")
    ),
    "0xec46f8207d766012454c408de210bcbc2243e71c": TokenInfo(
        currency=CurrencyInfo(symbol="NOX", name="NITRO"), scaling=Decimal("1e-18")
    ),
    "0xec491c1088eae992b7a214efb0a266ad0927a72a": TokenInfo(
        currency=CurrencyInfo(symbol="RTB", name="AB Chain RTB"), scaling=Decimal("1e-18")
    ),
    "0xec5483804e637d45cde22fa0869656b64b5ab1ab": TokenInfo(
        currency=CurrencyInfo(symbol="ACE", name="Acent"), scaling=Decimal("1e-18")
    ),
    "0xec67005c4e498ec7f55e092bd1d35cbc47c91892": TokenInfo(
        currency=CurrencyInfo(symbol="MLN", name="Enzyme"), scaling=Decimal("1e-18")
    ),
    "0xec681f28f4561c2a9534799aa38e0d36a83cf478": TokenInfo(
        currency=CurrencyInfo(symbol="YVS", name="YVS Finance"), scaling=Decimal("1e-18")
    ),
    "0xec6a5d88bf56fd3f96957ae65916c69f29db35c5": TokenInfo(
        currency=CurrencyInfo(symbol="APEUSD-AAVE-DEC21", name="apeUSD-AAVE Synthetic USD (Dec 2021)"),
        scaling=Decimal("1e-18"),
    ),
    "0xec79e0efa4ae3d8b3c9fbcee21683c7f2e507b66": TokenInfo(
        currency=CurrencyInfo(symbol="DBT", name="Dengba Planet"), scaling=Decimal("1e-18")
    ),
    "0xec7d3e835da3f6118079fa9a236b267d044fd7ca": TokenInfo(
        currency=CurrencyInfo(symbol="CRS", name="CryptoRewards"), scaling=Decimal("1e-18")
    ),
    "0xec9ee41b316b7f335274c37ef17f8e34b1171df8": TokenInfo(
        currency=CurrencyInfo(symbol="MSDZAR", name="Multi Stable DZAR"), scaling=Decimal("1e-18")
    ),
    "0xeca82185adce47f39c684352b0439f030f860318": TokenInfo(
        currency=CurrencyInfo(symbol="PERL", name="PERL.eco"), scaling=Decimal("1e-18")
    ),
    "0xecb79a9b7559168174c41b153997bc462b6dfe4e": TokenInfo(
        currency=CurrencyInfo(symbol="NAT", name="Nature"), scaling=Decimal("1e-18")
    ),
    "0xecb8f588eaf5a8ce9d964b0acece5d954e130e2f": TokenInfo(
        currency=CurrencyInfo(symbol="SBA", name="SimplyBrand"), scaling=Decimal("1e-18")
    ),
    "0xecbf566944250dde88322581024e611419715f7a": TokenInfo(
        currency=CurrencyInfo(symbol="XBTC", name="xBTC"), scaling=Decimal("1e-9")
    ),
    "0xecc0f1f860a82ab3b442382d93853c02d6384389": TokenInfo(
        currency=CurrencyInfo(symbol="AXIS", name="Axis DeFi"), scaling=Decimal("1e-18")
    ),
    "0xeccf15a4b5976a1365baed5297058b4ca42777c0": TokenInfo(
        currency=CurrencyInfo(symbol="NTRS", name="Nosturis"), scaling=Decimal("1e-18")
    ),
    "0xecd570bbf74761b960fa04cc10fe2c4e86ffda36": TokenInfo(
        currency=CurrencyInfo(symbol="STP", name="STASHPAY"), scaling=Decimal("1e-8")
    ),
    "0xece83617db208ad255ad4f45daf81e25137535bb": TokenInfo(
        currency=CurrencyInfo(symbol="INV", name="Invacio"), scaling=Decimal("1e-8")
    ),
    "0xece935de3ccb9e78add846bea5638e0eb52e71fb": TokenInfo(
        currency=CurrencyInfo(symbol="WGTG", name="World Game Token"), scaling=Decimal("1e-18")
    ),
    "0xecf52b1cd443e51bf9bcea862b584b748725da9f": TokenInfo(
        currency=CurrencyInfo(symbol="TCO", name="Tourcom"), scaling=Decimal("1e-18")
    ),
    "0xed0439eacf4c4965ae4613d77a5c2efe10e5f183": TokenInfo(
        currency=CurrencyInfo(symbol="SHROOM", name="Niftyx Protocol"), scaling=Decimal("1e-18")
    ),
    "0xed04915c23f00a313a544955524eb7dbd823143d": TokenInfo(
        currency=CurrencyInfo(symbol="ACH", name="Alchemy Pay"), scaling=Decimal("1e-8")
    ),
    "0xed0849bf46cfb9845a2d900a0a4e593f2dd3673c": TokenInfo(
        currency=CurrencyInfo(symbol="SGA", name="SGA Token"), scaling=Decimal("1e-18")
    ),
    "0xed0d5747a9ab03a75fbfec3228cd55848245b75d": TokenInfo(
        currency=CurrencyInfo(symbol="NGM", name="e Money"), scaling=Decimal("1e-6")
    ),
    "0xed0e2041bfb5a426e5ed426a73765624e08bbb75": TokenInfo(
        currency=CurrencyInfo(symbol="FX1", name="FANZY"), scaling=Decimal("1e-18")
    ),
    "0xed1199093b1abd07a368dd1c0cdc77d8517ba2a0": TokenInfo(
        currency=CurrencyInfo(symbol="HEX2T", name="HEX2T"), scaling=Decimal("1e-18")
    ),
    "0xed141928b4a5184603105bd9a5aea5eb63182f7b": TokenInfo(
        currency=CurrencyInfo(symbol="ANU", name="Alphanu"), scaling=Decimal("1e-18")
    ),
    "0xed247980396b10169bb1d36f6e278ed16700a60f": TokenInfo(
        currency=CurrencyInfo(symbol="AVA", name="Avalon"), scaling=Decimal("1e-4")
    ),
    "0xed30dd7e50edf3581ad970efc5d9379ce2614adb": TokenInfo(
        currency=CurrencyInfo(symbol="ARCX", name="ARC Governance  Old"), scaling=Decimal("1e-18")
    ),
    "0xed35af169af46a02ee13b9d79eb57d6d68c1749e": TokenInfo(
        currency=CurrencyInfo(symbol="OMI", name="ECOMI"), scaling=Decimal("1e-18")
    ),
    "0xed40834a13129509a89be39a9be9c0e96a0ddd71": TokenInfo(
        currency=CurrencyInfo(symbol="WARP", name="Warp Finance"), scaling=Decimal("1e-18")
    ),
    "0xed42cedcadbfbcaa3e6f411b09567c2c0b5ad28f": TokenInfo(
        currency=CurrencyInfo(
            symbol="REALTOKEN-9336-PATTON-ST-DETROIT-MI", name="RealToken 9336 Patton Street Detroit MI"
        ),
        scaling=Decimal("1e-18"),
    ),
    "0xed494c9e2f8e34e53bdd0ea9b4d80305cb15c5c2": TokenInfo(
        currency=CurrencyInfo(symbol="CWV", name="CryptoWorld.VIP"), scaling=Decimal("1e-18")
    ),
    "0xed5a55797caecca39811ac3cc0ee085cafc05953": TokenInfo(
        currency=CurrencyInfo(symbol="BSN", name="Bastonet"), scaling=Decimal("1e-18")
    ),
    "0xed64142f7d0a4d94ce0e7fe45d12f712fe360bd0": TokenInfo(
        currency=CurrencyInfo(symbol="COT", name="Cosplay Token"), scaling=Decimal("1e-18")
    ),
    "0xed6aad9650815d1647480caa1133043800d31533": TokenInfo(
        currency=CurrencyInfo(symbol="TOP", name="TokenSwap"), scaling=Decimal("1e-18")
    ),
    "0xed79e6dd91324f6af138f01967bd24233d642a24": TokenInfo(
        currency=CurrencyInfo(symbol="KMC", name="King Maker Coin"), scaling=Decimal("1e-8")
    ),
    "0xed7fa212e100dfb3b13b834233e4b680332a3420": TokenInfo(
        currency=CurrencyInfo(symbol="CRED", name="Street Cred"), scaling=Decimal("1e-18")
    ),
    "0xed7fea78c393cf7b17b152a8c2d0cd97ac31790b": TokenInfo(
        currency=CurrencyInfo(symbol="DUBI", name="Decentralized Universal Basic Income"), scaling=Decimal("1e-18")
    ),
    "0xed82730312babb41367e060911f798002ffa445f": TokenInfo(
        currency=CurrencyInfo(symbol="TCT", name="The Crypto Tech"), scaling=Decimal("1e-18")
    ),
    "0xed91879919b71bb6905f23af0a68d231ecf87b14": TokenInfo(
        currency=CurrencyInfo(symbol="DMG", name="DMM: Governance"), scaling=Decimal("1e-18")
    ),
    "0xeda6efe5556e134ef52f2f858aa1e81c84cda84b": TokenInfo(
        currency=CurrencyInfo(symbol="CAP", name="Capital.finance"), scaling=Decimal("1e-18")
    ),
    "0xeda8b016efa8b1161208cf041cd86972eee0f31e": TokenInfo(
        currency=CurrencyInfo(symbol="IHT", name="IHT Real Estate Protocol"), scaling=Decimal("1e-18")
    ),
    "0xedb0414627e6f1e3f082de65cd4f9c693d78cca9": TokenInfo(
        currency=CurrencyInfo(symbol="MTWTR", name="Mirrored Twitter"), scaling=Decimal("1e-18")
    ),
    "0xedbaf3c5100302dcdda53269322f3730b1f0416d": TokenInfo(
        currency=CurrencyInfo(symbol="Veros", name="Veros"), scaling=Decimal("1e-5")
    ),
    "0xedbcc06b603ea1f512720a4073a62cc4fdefcb86": TokenInfo(
        currency=CurrencyInfo(symbol="HTX", name="Hashtrust"), scaling=Decimal("1e-0")
    ),
    "0xedc1a631d4c3d0f554da14a4bce630f6cbc30a68": TokenInfo(
        currency=CurrencyInfo(symbol="NTRT", name="Nitro Platform Token"), scaling=Decimal("1e-8")
    ),
    "0xedc502b12ced7e16ce21749e7161f9ed22bfca53": TokenInfo(
        currency=CurrencyInfo(symbol="ICC", name="Intelligent Commerce Chain"), scaling=Decimal("1e-4")
    ),
    "0xedc87cab8bd12ca39088deaf9fdfb63503f19f85": TokenInfo(
        currency=CurrencyInfo(symbol="UNIS", name="Universe Coin"), scaling=Decimal("1e-18")
    ),
    "0xedd7c94fd7b4971b916d15067bc454b9e1bad980": TokenInfo(
        currency=CurrencyInfo(symbol="ZIPT", name="Zippie"), scaling=Decimal("1e-18")
    ),
    "0xedd8da5c20eb014e550008df3304213dde5e29f0": TokenInfo(
        currency=CurrencyInfo(symbol="MARS", name="Mars Network"), scaling=Decimal("1e-8")
    ),
    "0xede35fea9186f117d90c450a390bb6d6fdd70afb": TokenInfo(
        currency=CurrencyInfo(symbol="UBL", name="Unbelievable Token"), scaling=Decimal("1e-18")
    ),
    "0xede7518b8f90cbca48b551e5658b20513937d622": TokenInfo(
        currency=CurrencyInfo(symbol="INT", name="I Net Token"), scaling=Decimal("1e-8")
    ),
    "0xedf12cd1cef3c09f599962d1f15a79de19df8ebd": TokenInfo(
        currency=CurrencyInfo(symbol="CMT", name="Central Market"), scaling=Decimal("1e-8")
    ),
    "0xedf44412b47a76e452fd133794e45d9485e4cd4b": TokenInfo(
        currency=CurrencyInfo(symbol="CUAN", name="Kingcuan"), scaling=Decimal("1e-18")
    ),
    "0xedf6568618a00c6f0908bf7758a16f76b6e04af9": TokenInfo(
        currency=CurrencyInfo(symbol="ARIA20", name="Arianee"), scaling=Decimal("1e-18")
    ),
    "0xedfbd6c48c3ddff5612ade14b45bb19f916809ba": TokenInfo(
        currency=CurrencyInfo(symbol="RUGZ", name="pulltherug.finance"), scaling=Decimal("1e-18")
    ),
    "0xee059f0ca1507e4e20c689b20cff71b5e924f7bd": TokenInfo(
        currency=CurrencyInfo(symbol="LSV", name="Litecoin SV"), scaling=Decimal("1e-18")
    ),
    "0xee06a81a695750e71a662b51066f2c74cf4478a0": TokenInfo(
        currency=CurrencyInfo(symbol="DG", name="Decentral Games"), scaling=Decimal("1e-18")
    ),
    "0xee0f286776639cd363da810daf3e0623f82576b0": TokenInfo(
        currency=CurrencyInfo(symbol="L2P", name="Lung Protocol"), scaling=Decimal("1e-18")
    ),
    "0xee388f0527907339254f31254faeaffc4072a7ed": TokenInfo(
        currency=CurrencyInfo(symbol="BTCDai", name="BTCDaiRebalancingSetToken"), scaling=Decimal("1e-18")
    ),
    "0xee395235ac363725c6b895d8994706cb7050482f": TokenInfo(
        currency=CurrencyInfo(symbol="DSCOIN", name="Sky Net Security"), scaling=Decimal("1e-8")
    ),
    "0xee3b9b531f4c564c70e14b7b3bb7d516f33513ff": TokenInfo(
        currency=CurrencyInfo(symbol="DFIO", name="DeFi Omega"), scaling=Decimal("1e-18")
    ),
    "0xee4458e052b533b1aabd493b5f8c4d85d7b263dc": TokenInfo(
        currency=CurrencyInfo(symbol="PASS", name="Blockpass"), scaling=Decimal("1e-6")
    ),
    "0xee573a945b01b788b9287ce062a0cfc15be9fd86": TokenInfo(
        currency=CurrencyInfo(symbol="XED", name="Exeedme"), scaling=Decimal("1e-18")
    ),
    "0xee59784fc8fba300ae37fa41e229163dfaeb68c3": TokenInfo(
        currency=CurrencyInfo(symbol="TOOLS", name="Tools Chain"), scaling=Decimal("1e-18")
    ),
    "0xee5fe244406f35d9b4ddb488a64d51456630befc": TokenInfo(
        currency=CurrencyInfo(symbol="SHR", name="ShareToken"), scaling=Decimal("1e-2")
    ),
    "0xee609fe292128cad03b786dbb9bc2634ccdbe7fc": TokenInfo(
        currency=CurrencyInfo(symbol="POS", name="PoSToken"), scaling=Decimal("1e-18")
    ),
    "0xee74110fb5a1007b06282e0de5d73a61bf41d9cd": TokenInfo(
        currency=CurrencyInfo(symbol="BHPC", name="BHPCash"), scaling=Decimal("1e-18")
    ),
    "0xee87b220d9b0e762f0643c501fadefd6d9cc5b7e": TokenInfo(
        currency=CurrencyInfo(symbol="DGNN", name="Dragon Network"), scaling=Decimal("1e-18")
    ),
    "0xee9801669c6138e84bd50deb500827b776777d28": TokenInfo(
        currency=CurrencyInfo(symbol="O3", name="O3"), scaling=Decimal("1e-18")
    ),
    "0xee98a5c3fd8c9063c5d8777758d3901a88df957b": TokenInfo(
        currency=CurrencyInfo(symbol="ZEB", name="Zeb Token"), scaling=Decimal("1e-18")
    ),
    "0xee9e5eff401ee921b138490d00ca8d1f13f67a72": TokenInfo(
        currency=CurrencyInfo(symbol="AFIN", name="Asian Fintech"), scaling=Decimal("1e-8")
    ),
    "0xeea9ae787f3a620072d13b2cdc8cabffb9c0ab96": TokenInfo(
        currency=CurrencyInfo(symbol="YSEC", name="Yearn Secure"), scaling=Decimal("1e-18")
    ),
    "0xeeaa40b28a2d1b0b08f6f97bb1dd4b75316c6107": TokenInfo(
        currency=CurrencyInfo(symbol="GOVI", name="Govi"), scaling=Decimal("1e-18")
    ),
    "0xeeac3f8da16bb0485a4a11c5128b0518dac81448": TokenInfo(
        currency=CurrencyInfo(symbol="TEU", name="300cubits"), scaling=Decimal("1e-18")
    ),
    "0xeeb7a9744e82d00998ebfe232f4b00f3d03b7a77": TokenInfo(
        currency=CurrencyInfo(symbol="TKC", name="TAN-KE"), scaling=Decimal("1e-18")
    ),
    "0xeec2be5c91ae7f8a338e1e5f3b5de49d07afdc81": TokenInfo(
        currency=CurrencyInfo(symbol="DPX", name="Dopex"), scaling=Decimal("1e-18")
    ),
    "0xeed3ae7b0f8b5b9bb8c035a9941382b1822671cd": TokenInfo(
        currency=CurrencyInfo(symbol="EVY", name="EveryCoin"), scaling=Decimal("1e-12")
    ),
    "0xeed736b2b809550d89a941c2005de93588c628e2": TokenInfo(
        currency=CurrencyInfo(symbol="ETHP", name="ETHPlus"), scaling=Decimal("1e-18")
    ),
    "0xeee2d00eb7deb8dd6924187f5aa3496b7d06e62a": TokenInfo(
        currency=CurrencyInfo(symbol="TIG", name="Tigereum"), scaling=Decimal("1e-18")
    ),
    "0xeeee2a622330e6d2036691e983dee87330588603": TokenInfo(
        currency=CurrencyInfo(symbol="ASKO", name="Asko"), scaling=Decimal("1e-18")
    ),
    "0xeeeeeeeee2af8d0e1940679860398308e0ef24d6": TokenInfo(
        currency=CurrencyInfo(symbol="ETHV", name="Ethverse"), scaling=Decimal("1e-18")
    ),
    "0xeef85c9d7486748aae4a26aa55eeb82a62e631c3": TokenInfo(
        currency=CurrencyInfo(symbol="HTDOOM", name="10X Short Huobi Token Token"), scaling=Decimal("1e-18")
    ),
    "0xeef9f339514298c6a857efcfc1a762af84438dee": TokenInfo(
        currency=CurrencyInfo(symbol="HEZ", name="Hermez Network"), scaling=Decimal("1e-18")
    ),
    "0xef0fda1d4bd73ddc2f93a4e46e2e5adbc2d668f4": TokenInfo(
        currency=CurrencyInfo(symbol="ETHMACOAPY", name="ETH 20 Day MA Crossover Yield Set"), scaling=Decimal("1e-18")
    ),
    "0xef1223208d93d7c4934c2d426d939a9a0b917b6e": TokenInfo(
        currency=CurrencyInfo(symbol="PTON.CX", name="Peloton Interactive Inc"), scaling=Decimal("1e-8")
    ),
    "0xef1344bdf80bef3ff4428d8becec3eea4a2cf574": TokenInfo(
        currency=CurrencyInfo(symbol="ES", name="Era Swap"), scaling=Decimal("1e-18")
    ),
    "0xef1483ef1bc192f1c8201df89f9356fe80652089": TokenInfo(
        currency=CurrencyInfo(symbol="GPS", name="Coinscious Network"), scaling=Decimal("1e-8")
    ),
    "0xef19f4e48830093ce5bc8b3ff7f903a0ae3e9fa1": TokenInfo(
        currency=CurrencyInfo(symbol="BOTX", name="BOTXCOIN"), scaling=Decimal("1e-18")
    ),
    "0xef2463099360a085f1f10b076ed72ef625497a06": TokenInfo(
        currency=CurrencyInfo(symbol="SHP", name="Sharpe Platform Token"), scaling=Decimal("1e-18")
    ),
    "0xef2e9966eb61bb494e5375d5df8d67b7db8a780d": TokenInfo(
        currency=CurrencyInfo(symbol="SHIT", name="Shitcoin"), scaling=Decimal("1e-0")
    ),
    "0xef327568556310d344c49fb7ce6cbfe7b2bb83e6": TokenInfo(
        currency=CurrencyInfo(symbol="YFA", name="YFA Finance"), scaling=Decimal("1e-18")
    ),
    "0xef3a930e1ffffacd2fc13434ac81bd278b0ecc8d": TokenInfo(
        currency=CurrencyInfo(symbol="FIS", name="Stafi"), scaling=Decimal("1e-18")
    ),
    "0xef40b859d21e4d566a3d713e756197c021bffaaa": TokenInfo(
        currency=CurrencyInfo(symbol="NFT", name="APENFT"), scaling=Decimal("1e-6")
    ),
    "0xef50d71a8019508217ec4cc662d63158c1f8e617": TokenInfo(
        currency=CurrencyInfo(symbol="GDAX.CX", name="Germany 30"), scaling=Decimal("1e-8")
    ),
    "0xef51c9377feb29856e61625caf9390bd0b67ea18": TokenInfo(
        currency=CurrencyInfo(symbol="BNC", name="Bionic"), scaling=Decimal("1e-8")
    ),
    "0xef6344de1fcfc5f48c30234c16c1389e8cdc572c": TokenInfo(
        currency=CurrencyInfo(symbol="DNA", name="EncrypGen"), scaling=Decimal("1e-18")
    ),
    "0xef65887a05415bf6316204b5ffb350d4d1a19bba": TokenInfo(
        currency=CurrencyInfo(symbol="XT", name="ExtStock Token"), scaling=Decimal("1e-18")
    ),
    "0xef68e7c694f40c8202821edf525de3782458639f": TokenInfo(
        currency=CurrencyInfo(symbol="LRC", name="Loopring"), scaling=Decimal("1e-18")
    ),
    "0xef6b4ce8c9bc83744fbcde2657b32ec18790458a": TokenInfo(
        currency=CurrencyInfo(symbol="PUC", name="PUC"), scaling=Decimal("1e-0")
    ),
    "0xef7379179a9a85e1244bfc25fae3292ee09af8b8": TokenInfo(
        currency=CurrencyInfo(symbol="0522.CX", name="ASM Pacific Technology Limited"), scaling=Decimal("1e-8")
    ),
    "0xef7a985e4ff9b5dccd6eddf58577486887288711": TokenInfo(
        currency=CurrencyInfo(symbol="HOMT", name="HOM Token"), scaling=Decimal("1e-15")
    ),
    "0xef7f1aae6f60de9f353dc170a35b8f7c7814e32b": TokenInfo(
        currency=CurrencyInfo(symbol="AZT", name="AZ Fundchain"), scaling=Decimal("1e-18")
    ),
    "0xef8ba8cba86f81b3108f60186fce9c81b5096d5c": TokenInfo(
        currency=CurrencyInfo(symbol="YFIIG", name="YFII Gold"), scaling=Decimal("1e-18")
    ),
    "0xef9c8a1b3ce9055266e1ce20b98a4c882f0e5c78": TokenInfo(
        currency=CurrencyInfo(symbol="ETH3S", name="Amun Ether 3x Daily Short"), scaling=Decimal("1e-18")
    ),
    "0xef9cd7882c067686691b6ff49e650b43afbbcc6b": TokenInfo(
        currency=CurrencyInfo(symbol="FNX", name="FinNexus"), scaling=Decimal("1e-18")
    ),
    "0xefab7248d36585e2340e5d25f8a8d243e6e3193f": TokenInfo(
        currency=CurrencyInfo(symbol="DACXI", name="Dacxi"), scaling=Decimal("1e-18")
    ),
    "0xefbb3f1058fd8e0c9d7204f532e17d7572affc3e": TokenInfo(
        currency=CurrencyInfo(symbol="MBCASH", name="MBCash"), scaling=Decimal("1e-18")
    ),
    "0xefbd6d7def37ffae990503ecdb1291b2f7e38788": TokenInfo(
        currency=CurrencyInfo(symbol="EVO", name="EVO"), scaling=Decimal("1e-18")
    ),
    "0xefc1c73a3d8728dc4cf2a18ac5705fe93e5914ac": TokenInfo(
        currency=CurrencyInfo(symbol="METRIC", name="MetricExchange"), scaling=Decimal("1e-18")
    ),
    "0xefcafd4a1e76d392d683d4a79cd0e4a751d0be75": TokenInfo(
        currency=CurrencyInfo(symbol="BCST", name="BlockChain Store"), scaling=Decimal("1e-8")
    ),
    "0xefcec6d87e3ce625c90865a49f2b7482963d73fe": TokenInfo(
        currency=CurrencyInfo(symbol="FETISH", name="Fetish Coin"), scaling=Decimal("1e-6")
    ),
    "0xefe98765da3824ef4a5358ba798cec87c13d8c62": TokenInfo(
        currency=CurrencyInfo(symbol="BOL", name="Freight Trust Protocol"), scaling=Decimal("1e-18")
    ),
    "0xeffea57067e02999fdcd0bb45c0f1071a29472d9": TokenInfo(
        currency=CurrencyInfo(symbol="ZPAY", name="Zantepay"), scaling=Decimal("1e-18")
    ),
    "0xf013e0ea26cb386b3021783a3201bf2652778f93": TokenInfo(
        currency=CurrencyInfo(symbol="ARTS", name="ARTISTA"), scaling=Decimal("1e-18")
    ),
    "0xf028adee51533b1b47beaa890feb54a457f51e89": TokenInfo(
        currency=CurrencyInfo(symbol="BMT", name="BMCHAIN token"), scaling=Decimal("1e-18")
    ),
    "0xf02dab52205aff6bb3d47cc7b21624a5064f9fba": TokenInfo(
        currency=CurrencyInfo(symbol="PGOLD", name="Pyrrhos Gold Token"), scaling=Decimal("1e-4")
    ),
    "0xf03045a4c8077e38f3b8e2ed33b8aee69edf869f": TokenInfo(
        currency=CurrencyInfo(symbol="BMH", name="BlockMesh"), scaling=Decimal("1e-18")
    ),
    "0xf03f8d65bafa598611c3495124093c56e8f638f0": TokenInfo(
        currency=CurrencyInfo(symbol="VIEW", name="View"), scaling=Decimal("1e-18")
    ),
    "0xf04a8ac553fcedb5ba99a64799155826c136b0be": TokenInfo(
        currency=CurrencyInfo(symbol="FLIXX", name="Flixxo"), scaling=Decimal("1e-18")
    ),
    "0xf05a9382a4c3f29e2784502754293d88b835109c": TokenInfo(
        currency=CurrencyInfo(symbol="REX", name="Imbrex"), scaling=Decimal("1e-18")
    ),
    "0xf063fe1ab7a291c5d06a86e14730b00bf24cb589": TokenInfo(
        currency=CurrencyInfo(symbol="SALE", name="DxSale Network"), scaling=Decimal("1e-18")
    ),
    "0xf0667d12278a5f0519aaa01d91e94d94f7ab0f4d": TokenInfo(
        currency=CurrencyInfo(symbol="BCT", name="BiCoin"), scaling=Decimal("1e-18")
    ),
    "0xf06ddacf71e2992e2122a1a0168c6967afdf63ce": TokenInfo(
        currency=CurrencyInfo(symbol="UUSDRBTC-DEC", name="uUSDrBTC Synthetic Token Expiring 31 December 2020"),
        scaling=Decimal("1e-18"),
    ),
    "0xf091cf09c51811819db705710e9634b8bf18f164": TokenInfo(
        currency=CurrencyInfo(symbol="COU", name="Couchain"), scaling=Decimal("1e-18")
    ),
    "0xf0939011a9bb95c3b791f0cb546377ed2693a574": TokenInfo(
        currency=CurrencyInfo(symbol="ZERO", name="0.exchange"), scaling=Decimal("1e-18")
    ),
    "0xf0998faebc12188172310403814e0399f7af3f73": TokenInfo(
        currency=CurrencyInfo(symbol="HET", name="HavEtherToken"), scaling=Decimal("1e-18")
    ),
    "0xf0a0f3a6fa6bed75345171a5ea18abcadf6453ba": TokenInfo(
        currency=CurrencyInfo(symbol="YFBT", name="Yearn Finance Bit"), scaling=Decimal("1e-18")
    ),
    "0xf0b0a13d908253d954ba031a425dfd54f94a2e3d": TokenInfo(
        currency=CurrencyInfo(symbol="FSXA", name="FlashX Advance"), scaling=Decimal("1e-8")
    ),
    "0xf0bc1ae4ef7ffb126a8347d06ac6f8add770e1ce": TokenInfo(
        currency=CurrencyInfo(symbol="1MT", name="1Million Token"), scaling=Decimal("1e-7")
    ),
    "0xf0be50ed0620e0ba60ca7fc968ed14762e0a5dd3": TokenInfo(
        currency=CurrencyInfo(symbol="COW", name="Cowboy.Finance"), scaling=Decimal("1e-9")
    ),
    "0xf0c6521b1f8ad9c33a99aaf056f6c6247a3862ba": TokenInfo(
        currency=CurrencyInfo(symbol="ELD", name="ETH.limiteD"), scaling=Decimal("1e-18")
    ),
    "0xf0da1186a4977226b9135d0613ee72e229ec3f4d": TokenInfo(
        currency=CurrencyInfo(symbol="CRT", name="CreamtoeCoin"), scaling=Decimal("1e-18")
    ),
    "0xf0e3543744afced8042131582f2a19b6aeb82794": TokenInfo(
        currency=CurrencyInfo(symbol="VTD", name="Variable Time Dollar"), scaling=Decimal("1e-18")
    ),
    "0xf0ebb4a0784e710bfe06e69935018a94926ccd57": TokenInfo(
        currency=CurrencyInfo(symbol="TAX", name="TAXEM"), scaling=Decimal("1e-18")
    ),
    "0xf0ee6b27b759c9893ce4f094b49ad28fd15a23e4": TokenInfo(
        currency=CurrencyInfo(symbol="ENG", name="Enigma"), scaling=Decimal("1e-8")
    ),
    "0xf0f8b0b8dbb1124261fc8d778e2287e3fd2cf4f5": TokenInfo(
        currency=CurrencyInfo(symbol="BQ", name="bitqy"), scaling=Decimal("1e-3")
    ),
    "0xf0fac7104aac544e4a7ce1a55adf2b5a25c65bd1": TokenInfo(
        currency=CurrencyInfo(symbol="PAMP", name="Pamp Network"), scaling=Decimal("1e-18")
    ),
    "0xf1290473e210b2108a85237fbcd7b6eb42cc654f": TokenInfo(
        currency=CurrencyInfo(symbol="HEDG", name="HedgeTrade"), scaling=Decimal("1e-18")
    ),
    "0xf133f87980cfa1edc6594bb37409d9abccbba786": TokenInfo(
        currency=CurrencyInfo(symbol="LC+", name="LifeCare Plus"), scaling=Decimal("1e-18")
    ),
    "0xf14922001a2fb8541a433905437ae954419c2439": TokenInfo(
        currency=CurrencyInfo(symbol="DIT", name="Direct Insurance Token"), scaling=Decimal("1e-8")
    ),
    "0xf150b9054013552a6288320dc4afe1beebb79d8e": TokenInfo(
        currency=CurrencyInfo(symbol="ANGEL", name="AngelToken"), scaling=Decimal("1e-18")
    ),
    "0xf151980e7a781481709e8195744bf2399fb3cba4": TokenInfo(
        currency=CurrencyInfo(symbol="FWT", name="Freeway Token"), scaling=Decimal("1e-18")
    ),
    "0xf16e81dce15b08f326220742020379b855b87df9": TokenInfo(
        currency=CurrencyInfo(symbol="ICE", name="ICE"), scaling=Decimal("1e-18")
    ),
    "0xf17e65822b568b3903685a7c9f496cf7656cc6c2": TokenInfo(
        currency=CurrencyInfo(symbol="BICO", name="Biconomy"), scaling=Decimal("1e-18")
    ),
    "0xf18432ef894ef4b2a5726f933718f5a8cf9ff831": TokenInfo(
        currency=CurrencyInfo(symbol="BIO", name="BioCrypt"), scaling=Decimal("1e-8")
    ),
    "0xf18af466f8885f9ea93d2b85c47a427cb01bad52": TokenInfo(
        currency=CurrencyInfo(symbol="RPC", name="Racing Pigeon Chain"), scaling=Decimal("1e-18")
    ),
    "0xf1a355cc5953a5c04130f221b6ccad13c3f82990": TokenInfo(
        currency=CurrencyInfo(symbol="GNG", name="Gold And Gold"), scaling=Decimal("1e-18")
    ),
    "0xf1a91c7d44768070f711c68f33a7ca25c8d30268": TokenInfo(
        currency=CurrencyInfo(symbol="C3", name="Charli3"), scaling=Decimal("1e-18")
    ),
    "0xf1ac7a375429719de0dde33528e2639b9a206eba": TokenInfo(
        currency=CurrencyInfo(symbol="AMGO", name="Arena Match Gold"), scaling=Decimal("1e-18")
    ),
    "0xf1ca9cb74685755965c7458528a36934df52a3ef": TokenInfo(
        currency=CurrencyInfo(symbol="AVINOC", name="AVINOC"), scaling=Decimal("1e-18")
    ),
    "0xf1dd5964eabcc6e86230fa6f222677cfdaaf9f0e": TokenInfo(
        currency=CurrencyInfo(symbol="THM", name="Themis Chain"), scaling=Decimal("1e-18")
    ),
    "0xf1ded9284c73f9c3a664503e9a5e15188a991935": TokenInfo(
        currency=CurrencyInfo(symbol="ZALX", name="Zalxthereum"), scaling=Decimal("1e-6")
    ),
    "0xf1e5f03086e1c0ce55e54cd8146bc9c28435346f": TokenInfo(
        currency=CurrencyInfo(symbol="ETHMINVOL", name="ETH Range Bound Min Volatility Set"), scaling=Decimal("1e-18")
    ),
    "0xf1f508c7c9f0d1b15a76fba564eef2d956220cf7": TokenInfo(
        currency=CurrencyInfo(symbol="PPDEX", name="Pepedex"), scaling=Decimal("1e-18")
    ),
    "0xf1f5de69c9c8d9be8a7b01773cc1166d4ec6ede2": TokenInfo(
        currency=CurrencyInfo(symbol="DFX", name="Definitex"), scaling=Decimal("1e-18")
    ),
    "0xf1f955016ecbcd7321c7266bccfb96c68ea5e49b": TokenInfo(
        currency=CurrencyInfo(symbol="RLY", name="Rally"), scaling=Decimal("1e-18")
    ),
    "0xf2051511b9b121394fa75b8f7d4e7424337af687": TokenInfo(
        currency=CurrencyInfo(symbol="HAUS", name="DAOhaus"), scaling=Decimal("1e-18")
    ),
    "0xf205d2d65205711b6f6aae3fcb7ebdbc8573f192": TokenInfo(
        currency=CurrencyInfo(symbol="BMT", name="Bmining Token"), scaling=Decimal("1e-18")
    ),
    "0xf21661d0d1d76d3ecb8e1b9f1c923dbfffae4097": TokenInfo(
        currency=CurrencyInfo(symbol="RIO", name="Realio Network"), scaling=Decimal("1e-18")
    ),
    "0xf23444084c75b15d76414633abb003d855df4605": TokenInfo(
        currency=CurrencyInfo(symbol="LDS", name="L-Dimension"), scaling=Decimal("1e-18")
    ),
    "0xf2354f740f31704820f6fcfba70b9da065459b62": TokenInfo(
        currency=CurrencyInfo(symbol="ISDT", name="Istardust"), scaling=Decimal("1e-18")
    ),
    "0xf237f9cb687857b41fa88a141793115f1af9ac80": TokenInfo(
        currency=CurrencyInfo(symbol="QRVO.CX", name="Qorvo Inc"), scaling=Decimal("1e-8")
    ),
    "0xf256cc7847e919fac9b808cc216cac87ccf2f47a": TokenInfo(
        currency=CurrencyInfo(symbol="AXSUSHI", name="Aave XSUSHI"), scaling=Decimal("1e-18")
    ),
    "0xf25c91c87e0b1fd9b4064af0f427157aab0193a7": TokenInfo(
        currency=CurrencyInfo(symbol="BASIC", name="BASIC"), scaling=Decimal("1e-18")
    ),
    "0xf263292e14d9d8ecd55b58dad1f1df825a874b7c": TokenInfo(
        currency=CurrencyInfo(symbol="EDU", name="Educoin"), scaling=Decimal("1e-18")
    ),
    "0xf26893f89b23084c4c6216038d6ebdbe9e96c5cb": TokenInfo(
        currency=CurrencyInfo(symbol="MLR", name="MLR Token - Mega Lottery Services Global"), scaling=Decimal("1e-18")
    ),
    "0xf26ef5e0545384b7dcc0f297f2674189586830df": TokenInfo(
        currency=CurrencyInfo(symbol="BSDC", name="BitsIdea"), scaling=Decimal("1e-18")
    ),
    "0xf278c1ca969095ffddded020290cf8b5c424ace2": TokenInfo(
        currency=CurrencyInfo(symbol="RUFF", name="Ruff"), scaling=Decimal("1e-18")
    ),
    "0xf293d23bf2cdc05411ca0eddd588eb1977e8dcd4": TokenInfo(
        currency=CurrencyInfo(symbol="SYLO", name="Sylo"), scaling=Decimal("1e-18")
    ),
    "0xf29992d7b589a0a6bd2de7be29a97a6eb73eaf85": TokenInfo(
        currency=CurrencyInfo(symbol="DMST", name="DMScript"), scaling=Decimal("1e-18")
    ),
    "0xf29e46887ffae92f1ff87dfe39713875da541373": TokenInfo(
        currency=CurrencyInfo(symbol="UNC", name="UniCrypt (Old)"), scaling=Decimal("1e-18")
    ),
    "0xf2cee90309418353a57717eca26c4f8754f0d84e": TokenInfo(
        currency=CurrencyInfo(symbol="BTCB", name="BitcoinBrand"), scaling=Decimal("1e-18")
    ),
    "0xf2d4dcfe87430ae9d1e0235edaa7cd3d445e2378": TokenInfo(
        currency=CurrencyInfo(symbol="OPC", name="Oil Pact Chain"), scaling=Decimal("1e-18")
    ),
    "0xf2da15ae6ef94988534bad4b9e646f5911cbd487": TokenInfo(
        currency=CurrencyInfo(symbol="FAME", name="Fame"), scaling=Decimal("1e-8")
    ),
    "0xf2e08356588ec5cd9e437552da87c0076b4970b0": TokenInfo(
        currency=CurrencyInfo(symbol="sTRX", name="Synth sTRX"), scaling=Decimal("1e-18")
    ),
    "0xf2eab3a2034d3f6b63734d2e08262040e3ff7b48": TokenInfo(
        currency=CurrencyInfo(symbol="CANDY", name="Candy"), scaling=Decimal("1e-18")
    ),
    "0xf2eb99dec2feef17f7158b67dcb959fa08a41852": TokenInfo(
        currency=CurrencyInfo(symbol="PFE.CX", name="Pfizer Inc"), scaling=Decimal("1e-8")
    ),
    "0xf2f9a7e93f845b3ce154efbeb64fb9346fcce509": TokenInfo(
        currency=CurrencyInfo(symbol="POWER", name="UniPower"), scaling=Decimal("1e-18")
    ),
    "0xf3281c539716a08c754ec4c8f2b4cee0fab64bb9": TokenInfo(
        currency=CurrencyInfo(symbol="MKCY", name="Markaccy"), scaling=Decimal("1e-18")
    ),
    "0xf333b2ace992ac2bbd8798bf57bc65a06184afba": TokenInfo(
        currency=CurrencyInfo(symbol="SND", name="Sandcoin"), scaling=Decimal("1e-0")
    ),
    "0xf346298c09ea6726308d9ce82eddcb93cfccab6e": TokenInfo(
        currency=CurrencyInfo(symbol="FSLR.CX", name="First Solar Inc"), scaling=Decimal("1e-8")
    ),
    "0xf34960d9d60be18cc1d5afc1a6f012a723a28811": TokenInfo(
        currency=CurrencyInfo(symbol="KCS", name="KuCoin Token"), scaling=Decimal("1e-6")
    ),
    "0xf37a3fb5543f7283c051e8fed12b9e98dc54e5dc": TokenInfo(
        currency=CurrencyInfo(symbol="PAYC.CX", name="Paycom Software Inc"), scaling=Decimal("1e-8")
    ),
    "0xf38011f9153acffaca3fbfc42ddfa766c980d967": TokenInfo(
        currency=CurrencyInfo(symbol="PLUT", name="Pluto"), scaling=Decimal("1e-18")
    ),
    "0xf3949f351758fbb7608c934f133c3ed1f2e94d17": TokenInfo(
        currency=CurrencyInfo(symbol="XEC.CX", name="Cimarex Energy"), scaling=Decimal("1e-8")
    ),
    "0xf39f19565b8d937ec30f1db5bd42f558d1e312a6": TokenInfo(
        currency=CurrencyInfo(symbol="KAPP", name="Kappi Network"), scaling=Decimal("1e-18")
    ),
    "0xf3a2ace8e48751c965ea0a1d064303aca53842b9": TokenInfo(
        currency=CurrencyInfo(symbol="HXY", name="HXY Money"), scaling=Decimal("1e-8")
    ),
    "0xf3b3cad094b89392fce5fafd40bc03b80f2bc624": TokenInfo(
        currency=CurrencyInfo(symbol="PAT", name="Patron"), scaling=Decimal("1e-18")
    ),
    "0xf3b8d4b2607a39114dacb902bacd4ddde7182560": TokenInfo(
        currency=CurrencyInfo(symbol="USDTHEDGE", name="1X Short Tether Token"), scaling=Decimal("1e-18")
    ),
    "0xf3c092ca8cd6d3d4ca004dc1d0f1fe8ccab53599": TokenInfo(
        currency=CurrencyInfo(symbol="ZIX", name="Zeex Token"), scaling=Decimal("1e-18")
    ),
    "0xf3d29fb98d2dc5e78c87198deef99377345fd6f1": TokenInfo(
        currency=CurrencyInfo(symbol="BPC", name="Bitparkcoin"), scaling=Decimal("1e-8")
    ),
    "0xf3d6af45c6dfec43216cc3347ea91fefba0849d1": TokenInfo(
        currency=CurrencyInfo(symbol="DUBI", name="Decentralized Universal Basic Income"), scaling=Decimal("1e-18")
    ),
    "0xf3db5fa2c66b7af3eb0c0b782510816cbe4813b8": TokenInfo(
        currency=CurrencyInfo(symbol="EVX", name="Everex"), scaling=Decimal("1e-4")
    ),
    "0xf3db7560e820834658b590c96234c333cd3d5e5e": TokenInfo(
        currency=CurrencyInfo(symbol="CHP", name="CoinPoker"), scaling=Decimal("1e-18")
    ),
    "0xf3dcbc6d72a4e1892f7917b7c43b74131df8480e": TokenInfo(
        currency=CurrencyInfo(symbol="BDP", name="Big Data Protocol"), scaling=Decimal("1e-18")
    ),
    "0xf3dd98c8716fe4c8a559eeef84c5fe1fe697cdce": TokenInfo(
        currency=CurrencyInfo(symbol="DED", name="The Other Deadness"), scaling=Decimal("1e-18")
    ),
    "0xf3e014fe81267870624132ef3a646b8e83853a96": TokenInfo(
        currency=CurrencyInfo(symbol="VIN", name="VIN"), scaling=Decimal("1e-18")
    ),
    "0xf3e0b9368993640287eeed970945fdf57da53ed1": TokenInfo(
        currency=CurrencyInfo(symbol="KGT", name="KIZUNA GLOBAL TOKEN"), scaling=Decimal("1e-18")
    ),
    "0xf406f7a9046793267bc276908778b29563323996": TokenInfo(
        currency=CurrencyInfo(symbol="VISION", name="APY.vision"), scaling=Decimal("1e-18")
    ),
    "0xf411903cbc70a74d22900a5de66a2dda66507255": TokenInfo(
        currency=CurrencyInfo(symbol="VRA", name="Verasity"), scaling=Decimal("1e-18")
    ),
    "0xf4134146af2d511dd5ea8cdb1c4ac88c57d60404": TokenInfo(
        currency=CurrencyInfo(symbol="SNC", name="SunContract"), scaling=Decimal("1e-18")
    ),
    "0xf418588522d5dd018b425e472991e52ebbeeeeee": TokenInfo(
        currency=CurrencyInfo(symbol="PUSH", name="Ethereum Push Notif"), scaling=Decimal("1e-18")
    ),
    "0xf41e5fbc2f6aac200dd8619e121ce1f05d150077": TokenInfo(
        currency=CurrencyInfo(symbol="CRC", name="CRYCASH"), scaling=Decimal("1e-18")
    ),
    "0xf433089366899d83a9f26a773d59ec7ecf30355e": TokenInfo(
        currency=CurrencyInfo(symbol="MTL", name="Metal"), scaling=Decimal("1e-8")
    ),
    "0xf44745fbd41f6a1ba151df190db0564c5fcc4410": TokenInfo(
        currency=CurrencyInfo(symbol="CPY", name="COPYTRACK"), scaling=Decimal("1e-18")
    ),
    "0xf4490981a99019d9ff07e000b9b00238f399b04b": TokenInfo(
        currency=CurrencyInfo(symbol="NVDA.CX", name="NVIDIA"), scaling=Decimal("1e-8")
    ),
    "0xf45091f25d374bbe956c0bb64bb85e02d07aa741": TokenInfo(
        currency=CurrencyInfo(symbol="MNMC", name="MNMCoin"), scaling=Decimal("1e-8")
    ),
    "0xf453b5b9d4e0b5c62ffb256bb2378cc2bc8e8a89": TokenInfo(
        currency=CurrencyInfo(symbol="MRK", name="MARK.SPACE"), scaling=Decimal("1e-8")
    ),
    "0xf45b14ddabf0f0e275e215b94dd24ae013a27f12": TokenInfo(
        currency=CurrencyInfo(symbol="SXTZ", name="sXTZ"), scaling=Decimal("1e-18")
    ),
    "0xf45b778e53d858c79bf4dfbdd5c1bfdb426bb891": TokenInfo(
        currency=CurrencyInfo(symbol="MFCC", name="MFCC Token"), scaling=Decimal("1e-18")
    ),
    "0xf45f0e16b5e096286e1fb463d34be9f3df5e3602": TokenInfo(
        currency=CurrencyInfo(symbol="BTMX", name="BitMax token"), scaling=Decimal("1e-18")
    ),
    "0xf46490aaf79dad46682468cc3e6eca0372eed8dc": TokenInfo(
        currency=CurrencyInfo(symbol="BIG.CX", name="Big Lots"), scaling=Decimal("1e-8")
    ),
    "0xf46f98a8f6032914921ae9cfb5aaab5083bd9376": TokenInfo(
        currency=CurrencyInfo(symbol="OSCH", name="Open Source Chain"), scaling=Decimal("1e-18")
    ),
    "0xf485c5e679238f9304d986bb2fc28fe3379200e5": TokenInfo(
        currency=CurrencyInfo(symbol="UGC", name="ugChain"), scaling=Decimal("1e-18")
    ),
    "0xf48e200eaf9906362bb1442fca31e0835773b8b4": TokenInfo(
        currency=CurrencyInfo(symbol="SAUD", name="sAUD"), scaling=Decimal("1e-18")
    ),
    "0xf49cdd50ad408d387d611f88a647179c3de3492b": TokenInfo(
        currency=CurrencyInfo(symbol="CRGO", name="CargoCoin"), scaling=Decimal("1e-18")
    ),
    "0xf4b5470523ccd314c6b9da041076e7d79e0df267": TokenInfo(
        currency=CurrencyInfo(symbol="BBANK", name="BlockBank"), scaling=Decimal("1e-18")
    ),
    "0xf4b54874cd8a6c863e3a904c18fda964661ec363": TokenInfo(
        currency=CurrencyInfo(symbol="DWS", name="DWS"), scaling=Decimal("1e-18")
    ),
    "0xf4b6664bb81bd7314ae65eab2ee675505e3e9cb6": TokenInfo(
        currency=CurrencyInfo(symbol="DTH", name="DINESHTECH"), scaling=Decimal("1e-2")
    ),
    "0xf4bbd1f932bda87c24fe13a50912a13b06ed2601": TokenInfo(
        currency=CurrencyInfo(symbol="XEV", name="Xevenue Shares"), scaling=Decimal("1e-18")
    ),
    "0xf4c07b1865bc326a3c01339492ca7538fd038cc0": TokenInfo(
        currency=CurrencyInfo(symbol="PBT", name="Primalbase Token"), scaling=Decimal("1e-4")
    ),
    "0xf4c17bc4979c1dc7b4ca50115358dec58c67fd9d": TokenInfo(
        currency=CurrencyInfo(symbol="OPM", name="Omega Protocol Money"), scaling=Decimal("1e-18")
    ),
    "0xf4c571fb6dd704e58561cdd275fa4b80cfe82f76": TokenInfo(
        currency=CurrencyInfo(symbol="RFX", name="ROTH"), scaling=Decimal("1e-8")
    ),
    "0xf4cd3d3fda8d7fd6c5a500203e38640a70bf9577": TokenInfo(
        currency=CurrencyInfo(symbol="YF-DAI", name="YfDAI.finance"), scaling=Decimal("1e-18")
    ),
    "0xf4d2888d29d722226fafa5d9b24f9164c092421e": TokenInfo(
        currency=CurrencyInfo(symbol="LOOKS", name="LooksRare"), scaling=Decimal("1e-18")
    ),
    "0xf4d861575ecc9493420a3f5a14f85b13f0b50eb3": TokenInfo(
        currency=CurrencyInfo(symbol="FCL", name="Fractal"), scaling=Decimal("1e-18")
    ),
    "0xf4e4f9e5ba2b0892c289ef2de60ca44e1f6b2527": TokenInfo(
        currency=CurrencyInfo(symbol="DET", name="DET Token"), scaling=Decimal("1e-8")
    ),
    "0xf4eebdd0704021ef2a6bbe993fdf93030cd784b4": TokenInfo(
        currency=CurrencyInfo(symbol="IEOS", name="iEOS"), scaling=Decimal("1e-18")
    ),
    "0xf4faea455575354d2699bc209b0a65ca99f69982": TokenInfo(
        currency=CurrencyInfo(symbol="NOBS", name="No BS Crypto"), scaling=Decimal("1e-18")
    ),
    "0xf4fe95603881d0e07954fd7605e0e9a916e42c44": TokenInfo(
        currency=CurrencyInfo(symbol="WHEN", name="WHEN Token"), scaling=Decimal("1e-18")
    ),
    "0xf5078213b8d39e0eec2011d9486c17ddf07ea003": TokenInfo(
        currency=CurrencyInfo(symbol="RBC", name="Roti Bank Coin"), scaling=Decimal("1e-18")
    ),
    "0xf51ebf9a26dbc02b13f8b3a9110dac47a4d62d78": TokenInfo(
        currency=CurrencyInfo(symbol="APIX", name="APIX"), scaling=Decimal("1e-18")
    ),
    "0xf5238462e7235c7b62811567e63dd17d12c2eaa0": TokenInfo(
        currency=CurrencyInfo(symbol="CGT", name="CACHE Gold"), scaling=Decimal("1e-8")
    ),
    "0xf525cc44ba797d91413a490a3a7bf5532c8fd378": TokenInfo(
        currency=CurrencyInfo(symbol="LIT", name="LIUM"), scaling=Decimal("1e-18")
    ),
    "0xf52b2237418f59e4ae3184d8cd7780c9b2f11b36": TokenInfo(
        currency=CurrencyInfo(symbol="BNW", name="BitNetwork"), scaling=Decimal("1e-8")
    ),
    "0xf5312da58ab6c1706d651ed9fcd3ca000c3a25b7": TokenInfo(
        currency=CurrencyInfo(symbol="MOONSHIT", name="10X Long Shitcoin Index Token"), scaling=Decimal("1e-18")
    ),
    "0xf53ad2c6851052a81b42133467480961b2321c09": TokenInfo(
        currency=CurrencyInfo(symbol="PETH", name="Pooled Ether"), scaling=Decimal("1e-18")
    ),
    "0xf53c580bc4065405bc649cc077ff4f2f28528f4b": TokenInfo(
        currency=CurrencyInfo(symbol="BWT", name="Bittwatt"), scaling=Decimal("1e-18")
    ),
    "0xf552b656022c218c26dad43ad88881fc04116f76": TokenInfo(
        currency=CurrencyInfo(symbol="MORK", name="MORK"), scaling=Decimal("1e-4")
    ),
    "0xf5555732b3925356964695578fefcffcd31bcbb8": TokenInfo(
        currency=CurrencyInfo(symbol="PMD", name="Promodio"), scaling=Decimal("1e-9")
    ),
    "0xf5581dfefd8fb0e4aec526be659cfab1f8c781da": TokenInfo(
        currency=CurrencyInfo(symbol="HOPR", name="HOPR"), scaling=Decimal("1e-18")
    ),
    "0xf56842af3b56fd72d17cb103f92d027bba912e89": TokenInfo(
        currency=CurrencyInfo(symbol="BAMBOO", name="BambooDeFi"), scaling=Decimal("1e-18")
    ),
    "0xf5717f5df41ea67ef67dfd3c1d02f9940bcf5d08": TokenInfo(
        currency=CurrencyInfo(symbol="SNN", name="SeChain"), scaling=Decimal("1e-3")
    ),
    "0xf573303b74968cbf2045eb8c8f945b48954d711e": TokenInfo(
        currency=CurrencyInfo(symbol="ABBV.CX", name="Abbvie"), scaling=Decimal("1e-8")
    ),
    "0xf576ff0d7e4c1e8f27dbd50321e95e36a965985f": TokenInfo(
        currency=CurrencyInfo(symbol="AFC", name="Apiary Fund Coin"), scaling=Decimal("1e-18")
    ),
    "0xf5774f42b28f35429aac35f8eb57541c511fdd49": TokenInfo(
        currency=CurrencyInfo(symbol="ARCG", name="Arch Crypton Game"), scaling=Decimal("1e-18")
    ),
    "0xf57e7e7c23978c3caec3c3548e3d615c346e79ff": TokenInfo(
        currency=CurrencyInfo(symbol="IMX", name="Immutable X"), scaling=Decimal("1e-18")
    ),
    "0xf5832512cfda8083e5b2dd0aa7c1b9265c03ba1f": TokenInfo(
        currency=CurrencyInfo(symbol="SZC", name="Zugacoin"), scaling=Decimal("1e-8")
    ),
    "0xf5839f46ed000d70cbab1fcd03e29e85f3aecd82": TokenInfo(
        currency=CurrencyInfo(symbol="BCT", name="BitCardTour"), scaling=Decimal("1e-18")
    ),
    "0xf59ae934f6fe444afc309586cc60a84a0f89aaea": TokenInfo(
        currency=CurrencyInfo(symbol="PDEX", name="Polkadex"), scaling=Decimal("1e-18")
    ),
    "0xf5a562597d5fb5cc19482379755e1a5275a6607b": TokenInfo(
        currency=CurrencyInfo(symbol="XFOC", name="XFOC"), scaling=Decimal("1e-7")
    ),
    "0xf5b815344641412401d8e868790dbd125e6761ca": TokenInfo(
        currency=CurrencyInfo(symbol="PCO", name="Pecunio"), scaling=Decimal("1e-8")
    ),
    "0xf5c0e24aca5217bcbae662871cae1a86873f02db": TokenInfo(
        currency=CurrencyInfo(symbol="GATOR", name="Alligator + Fractal Set"), scaling=Decimal("1e-18")
    ),
    "0xf5d0fefaab749d8b14c27f0de60cc6e9e7f848d1": TokenInfo(
        currency=CurrencyInfo(symbol="YFARM", name="YFARM Token"), scaling=Decimal("1e-18")
    ),
    "0xf5d669627376ebd411e34b98f19c868c8aba5ada": TokenInfo(
        currency=CurrencyInfo(symbol="AXS", name="Axie Infinity Shard"), scaling=Decimal("1e-18")
    ),
    "0xf5d714d9cd577b7daf83f84aea37a1eb0787e7ad": TokenInfo(
        currency=CurrencyInfo(symbol="HLS", name="Helios Protocol"), scaling=Decimal("1e-18")
    ),
    "0xf5dce57282a584d2746faf1593d3121fcac444dc": TokenInfo(
        currency=CurrencyInfo(symbol="CSAI", name="cSAI"), scaling=Decimal("1e-8")
    ),
    "0xf5e5421057606c4c629caec0d726976d9d4d7c51": TokenInfo(
        currency=CurrencyInfo(symbol="EPAM.CX", name="EPAM Systems Inc"), scaling=Decimal("1e-8")
    ),
    "0xf5e7f08c91b5d8579746eaad70ac509e94e2f1d3": TokenInfo(
        currency=CurrencyInfo(symbol="BID", name="Bidcoin"), scaling=Decimal("1e-18")
    ),
    "0xf6117cc92d7247f605f11d4c942f0feda3399cb5": TokenInfo(
        currency=CurrencyInfo(symbol="MTCN", name="Multicoin"), scaling=Decimal("1e-18")
    ),
    "0xf61718057901f84c4eec4339ef8f0d86d2b45600": TokenInfo(
        currency=CurrencyInfo(symbol="ySUSD", name="iearn SUSD"), scaling=Decimal("1e-18")
    ),
    "0xf6276830c265a779a2225b9d2fcbab790cbeb92b": TokenInfo(
        currency=CurrencyInfo(symbol="XCEL", name="XcelToken"), scaling=Decimal("1e-18")
    ),
    "0xf629cbd94d3791c9250152bd8dfbdf380e2a3b9c": TokenInfo(
        currency=CurrencyInfo(symbol="ENJ", name="Enjin Coin"), scaling=Decimal("1e-18")
    ),
    "0xf6317dd9b04097a9e7b016cd23dcaa7cfe19d9c6": TokenInfo(
        currency=CurrencyInfo(symbol="TOPB", name="TOPBTC Token"), scaling=Decimal("1e-18")
    ),
    "0xf647902282cd054a74d036d986efd8bb4ac36c9c": TokenInfo(
        currency=CurrencyInfo(symbol="BIIDR", name="Bit-IDR"), scaling=Decimal("1e-18")
    ),
    "0xf649c39e7efdbac6c9adb65c43e87894fc14aedd": TokenInfo(
        currency=CurrencyInfo(symbol="AWC", name="All World Coin"), scaling=Decimal("1e-8")
    ),
    "0xf650c3d88d12db855b8bf7d11be6c55a4e07dcc9": TokenInfo(
        currency=CurrencyInfo(symbol="CUSDT", name="cUSDT"), scaling=Decimal("1e-8")
    ),
    "0xf660ca1e228e7be1fa8b4f5583145e31147fb577": TokenInfo(
        currency=CurrencyInfo(symbol="CET", name="Dicet"), scaling=Decimal("1e-18")
    ),
    "0xf6650117017ffd48b725b4ec5a00b414097108a7": TokenInfo(
        currency=CurrencyInfo(symbol="XIDO", name="Xido Finance"), scaling=Decimal("1e-18")
    ),
    "0xf67041758d3b6e56d6fdafa5b32038302c3634da": TokenInfo(
        currency=CurrencyInfo(symbol="TST", name="TBC Shopping Token"), scaling=Decimal("1e-18")
    ),
    "0xf67451dc8421f0e0afeb52faa8101034ed081ed9": TokenInfo(
        currency=CurrencyInfo(symbol="GAM", name="Gambit Token"), scaling=Decimal("1e-8")
    ),
    "0xf68fe4eeb1b4f93de4f11c29fdce6cf120b475c0": TokenInfo(
        currency=CurrencyInfo(symbol="SSA.CX", name="Sistema PJSFC GDR"), scaling=Decimal("1e-8")
    ),
    "0xf6923f7d96fc22c4b8010a865e41cf7edfb6379c": TokenInfo(
        currency=CurrencyInfo(symbol="IOOX", name="IOOX System"), scaling=Decimal("1e-8")
    ),
    "0xf6b1c627e95bfc3c1b4c9b825a032ff0fbf3e07d": TokenInfo(
        currency=CurrencyInfo(symbol="sJPY", name="Synth sJPY"), scaling=Decimal("1e-18")
    ),
    "0xf6b55acbbc49f4524aa48d19281a9a77c54de10f": TokenInfo(
        currency=CurrencyInfo(symbol="WLK", name="Wolk"), scaling=Decimal("1e-18")
    ),
    "0xf6b6aa0ef0f5edc2c1c5d925477f97eaf66303e7": TokenInfo(
        currency=CurrencyInfo(symbol="XGG", name="Going Gems"), scaling=Decimal("1e-8")
    ),
    "0xf6bf74a97d78f2242376769ef1e79885cf1f0c1c": TokenInfo(
        currency=CurrencyInfo(symbol="KAASO", name="KAASO"), scaling=Decimal("1e-18")
    ),
    "0xf6c0aa7ebfe9992200c67e5388e4f42da49e1783": TokenInfo(
        currency=CurrencyInfo(symbol="USD1", name="Psyche"), scaling=Decimal("1e-2")
    ),
    "0xf6c151ea50a4f1a50983eb98998a18be0a549ad5": TokenInfo(
        currency=CurrencyInfo(symbol="YFI2", name="YEARN2.FINANCE"), scaling=Decimal("1e-18")
    ),
    "0xf6cfe53d6febaeea051f400ff5fc14f0cbbdaca1": TokenInfo(
        currency=CurrencyInfo(symbol="DGPT", name="DigiPulse"), scaling=Decimal("1e-18")
    ),
    "0xf6dbe88ba55f1793ff0773c9b1275300f830914f": TokenInfo(
        currency=CurrencyInfo(symbol="AD", name="Asian Dragon"), scaling=Decimal("1e-8")
    ),
    "0xf6e9b246319ea30e8c2fa2d1540aaebf6f9e1b89": TokenInfo(
        currency=CurrencyInfo(symbol="IBCH", name="iBCH"), scaling=Decimal("1e-18")
    ),
    "0xf6f364fe92a87225caeaf3840700917416427e00": TokenInfo(
        currency=CurrencyInfo(symbol="BXC", name="Blox Chain"), scaling=Decimal("1e-18")
    ),
    "0xf70a642bd387f94380ffb90451c2c81d4eb82cbc": TokenInfo(
        currency=CurrencyInfo(symbol="STAR", name="Starbase"), scaling=Decimal("1e-18")
    ),
    "0xf70d160102cf7a22c1e432d6928a9d625db91170": TokenInfo(
        currency=CurrencyInfo(symbol="KUV", name="Kuverit"), scaling=Decimal("1e-18")
    ),
    "0xf70e431c0e077e794e202b7e2a3da03a394fa0fb": TokenInfo(
        currency=CurrencyInfo(symbol="BTHT", name="Bitherium"), scaling=Decimal("1e-0")
    ),
    "0xf722b01910f93b84eda9ca128b9f05821a41eae1": TokenInfo(
        currency=CurrencyInfo(symbol="VRE", name="Vrenelium Token"), scaling=Decimal("1e-18")
    ),
    "0xf7269a10e85d4aa8282529516cf86847748da2bf": TokenInfo(
        currency=CurrencyInfo(symbol="CLA", name="Candela Coin"), scaling=Decimal("1e-18")
    ),
    "0xf728007ada0bfa496f4a90c53f978452433f07f5": TokenInfo(
        currency=CurrencyInfo(symbol="AMD.CX", name="Advanced Micro Devices Inc"), scaling=Decimal("1e-8")
    ),
    "0xf72fcd9dcf0190923fadd44811e240ef4533fc86": TokenInfo(
        currency=CurrencyInfo(symbol="MVIXY", name="Mirrored ProShares VIX"), scaling=Decimal("1e-18")
    ),
    "0xf73b1f84e0c16cd56b0fad03295213a3098de0de": TokenInfo(
        currency=CurrencyInfo(symbol="SHT", name="Shine Layer2"), scaling=Decimal("1e-18")
    ),
    "0xf73fc4b74a4cc6f9ea203a9d5bbff4ffce3a4c48": TokenInfo(
        currency=CurrencyInfo(symbol="PHN", name="Phillionex"), scaling=Decimal("1e-18")
    ),
    "0xf7461c8d8e469e9c41a9013dc09ba8abed66ef65": TokenInfo(
        currency=CurrencyInfo(symbol="CTAT", name="Cryptassist"), scaling=Decimal("1e-8")
    ),
    "0xf7623a0a44045b907d81aad8479aa3c4a818211d": TokenInfo(
        currency=CurrencyInfo(symbol="SPA", name="SperaxToken"), scaling=Decimal("1e-18")
    ),
    "0xf784682c82526e245f50975190ef0fff4e4fc077": TokenInfo(
        currency=CurrencyInfo(symbol="ILK", name="INLOCK Token"), scaling=Decimal("1e-8")
    ),
    "0xf7920b0768ecb20a123fac32311d07d193381d6f": TokenInfo(
        currency=CurrencyInfo(symbol="TNB", name="Time New Bank"), scaling=Decimal("1e-18")
    ),
    "0xf7970499814654cd13cb7b6e7634a12a7a8a9abc": TokenInfo(
        currency=CurrencyInfo(symbol="TOM", name="TOM Finance"), scaling=Decimal("1e-18")
    ),
    "0xf7a219fffeade6cd98789da5642b687f743270eb": TokenInfo(
        currency=CurrencyInfo(symbol="RHEA", name="Rhea Protocol"), scaling=Decimal("1e-18")
    ),
    "0xf7b098298f7c69fc14610bf71d5e02c60792894c": TokenInfo(
        currency=CurrencyInfo(symbol="GUP", name="Guppy"), scaling=Decimal("1e-3")
    ),
    "0xf7d1f35518950e78c18e5a442097ca07962f4d8a": TokenInfo(
        currency=CurrencyInfo(symbol="OSPVS", name="Onyx S&P 500 Short"), scaling=Decimal("1e-18")
    ),
    "0xf7e04d8a32229b4ca63aa51eea9979c7287fea48": TokenInfo(
        currency=CurrencyInfo(symbol="BWF", name="Beowulf"), scaling=Decimal("1e-5")
    ),
    "0xf7e983781609012307f2514f63d526d83d24f466": TokenInfo(
        currency=CurrencyInfo(symbol="MYD", name="MyDoc Token"), scaling=Decimal("1e-16")
    ),
    "0xf80d589b3dbe130c270a69f1a69d050f268786df": TokenInfo(
        currency=CurrencyInfo(symbol="DAM", name="Datamine"), scaling=Decimal("1e-18")
    ),
    "0xf813f3902bbc00a6dce378634d3b79d84f9803d7": TokenInfo(
        currency=CurrencyInfo(symbol="PATH", name="PATH Token"), scaling=Decimal("1e-18")
    ),
    "0xf82d62d65f0c670ac4d88abdf1afefac11522a16": TokenInfo(
        currency=CurrencyInfo(symbol="BTM", name="BTMcoin"), scaling=Decimal("1e-18")
    ),
    "0xf83d7ff2e4b43ebad2fa534e621e31076f4d254c": TokenInfo(
        currency=CurrencyInfo(symbol="HPAY", name="Hyper Credit Network"), scaling=Decimal("1e-18")
    ),
    "0xf8483e2d6560585c02d46bf7b3186bf154a96166": TokenInfo(
        currency=CurrencyInfo(symbol="ICH", name="IdeaChain"), scaling=Decimal("1e-8")
    ),
    "0xf84df2db2c87dd650641f8904af71ebfc3dde0ea": TokenInfo(
        currency=CurrencyInfo(symbol="UC", name="YouLive Coin"), scaling=Decimal("1e-18")
    ),
    "0xf85ef57fcdb36d628d063fa663e61e44d35ae661": TokenInfo(
        currency=CurrencyInfo(symbol="GBPX", name="eToro Pound Sterling"), scaling=Decimal("1e-18")
    ),
    "0xf85feea2fdd81d51177f6b8f35f0e6734ce45f5f": TokenInfo(
        currency=CurrencyInfo(symbol="CMT", name="CyberMiles"), scaling=Decimal("1e-18")
    ),
    "0xf87271ff78a3de23bb7a6fbd3c7080199f6ae82b": TokenInfo(
        currency=CurrencyInfo(symbol="XGT", name="Guten Check"), scaling=Decimal("1e-18")
    ),
    "0xf872f60a163701cb2cfc240d728ea3df51ba11f9": TokenInfo(
        currency=CurrencyInfo(symbol="TDE", name="Trade Ecology Token"), scaling=Decimal("1e-18")
    ),
    "0xf87f0d9153fea549c728ad61cb801595a68b73de": TokenInfo(
        currency=CurrencyInfo(symbol="BANX", name="Ubanx"), scaling=Decimal("1e-18")
    ),
    "0xf88951d7b676798705fd3a362ba5b1dbca2b233b": TokenInfo(
        currency=CurrencyInfo(symbol="PXL", name="Piction Network"), scaling=Decimal("1e-18")
    ),
    "0xf8a3dc13b7a8da473f80660f513c4343e4edd7f7": TokenInfo(
        currency=CurrencyInfo(symbol="LOTEU", name="LOTEU"), scaling=Decimal("1e-8")
    ),
    "0xf8a4a419c2d7140e49ef952a7e7ae1bd4a8b6b9c": TokenInfo(
        currency=CurrencyInfo(symbol="LITH", name="Lith Token"), scaling=Decimal("1e-18")
    ),
    "0xf8ad7dfe656188a23e89da09506adf7ad9290d5d": TokenInfo(
        currency=CurrencyInfo(symbol="BLY", name="Blocery"), scaling=Decimal("1e-18")
    ),
    "0xf8b358b3397a8ea5464f8cc753645d42e14b79ea": TokenInfo(
        currency=CurrencyInfo(symbol="ABL", name="Airbloc"), scaling=Decimal("1e-18")
    ),
    "0xf8c3527cc04340b208c854e985240c02f7b7793f": TokenInfo(
        currency=CurrencyInfo(symbol="FRONT", name="Frontier"), scaling=Decimal("1e-18")
    ),
    "0xf8c595d070d104377f58715ce2e6c93e49a87f3c": TokenInfo(
        currency=CurrencyInfo(symbol="DACC", name="DACC"), scaling=Decimal("1e-6")
    ),
    "0xf8cc67e304f8e1a351ed83b4dbbe6b4076d51376": TokenInfo(
        currency=CurrencyInfo(symbol="EXCHHEDGE", name="1X Short Exchange Token Index Token"), scaling=Decimal("1e-18")
    ),
    "0xf8d1254fc324d2e75a5a37f5bd4ca34a20ef460d": TokenInfo(
        currency=CurrencyInfo(symbol="ADVC", name="Advertisingcoin"), scaling=Decimal("1e-8")
    ),
    "0xf8d9fd49d0519a7b93f3ce80c2c070f1294ead26": TokenInfo(
        currency=CurrencyInfo(symbol="KAM", name="Kamari"), scaling=Decimal("1e-18")
    ),
    "0xf8e06e4e4a80287fdca5b02dccecaa9d0954840f": TokenInfo(
        currency=CurrencyInfo(symbol="TGAME", name="Truegame"), scaling=Decimal("1e-18")
    ),
    "0xf8e386eda857484f5a12e4b5daa9984e06e73705": TokenInfo(
        currency=CurrencyInfo(symbol="IND", name="Indorse"), scaling=Decimal("1e-18")
    ),
    "0xf8ed6c51762208ff26f8f3e4efd4e06af2da649c": TokenInfo(
        currency=CurrencyInfo(symbol="AXA", name="Alldex Alliance"), scaling=Decimal("1e-18")
    ),
    "0xf8f237d074f637d777bcd2a4712bde793f94272b": TokenInfo(
        currency=CurrencyInfo(symbol="ERC223", name="ERC223"), scaling=Decimal("1e-10")
    ),
    "0xf8fe64a5e8969a7947382e290c91e1fa715a7ec9": TokenInfo(
        currency=CurrencyInfo(symbol="X.CX", name="US Steel Corp"), scaling=Decimal("1e-8")
    ),
    "0xf906997808f73b09c1007b98ab539b189282b192": TokenInfo(
        currency=CurrencyInfo(symbol="USDG", name="USDG"), scaling=Decimal("1e-3")
    ),
    "0xf911a7ec46a2c6fa49193212fe4a2a9b95851c27": TokenInfo(
        currency=CurrencyInfo(symbol="XAMP", name="Antiample"), scaling=Decimal("1e-9")
    ),
    "0xf921ae2dac5fa128dc0f6168bf153ea0943d2d43": TokenInfo(
        currency=CurrencyInfo(symbol="FIRE", name="Fire Protocol"), scaling=Decimal("1e-8")
    ),
    "0xf93340b1a3adf7eedcaec25fae8171d4b736e89f": TokenInfo(
        currency=CurrencyInfo(symbol="PXUSD-MAR2021", name="pxUSD Synthetic USD Expiring 1 April 2021"),
        scaling=Decimal("1e-18"),
    ),
    "0xf938424f7210f31df2aee3011291b658f872e91e": TokenInfo(
        currency=CurrencyInfo(symbol="VISR", name="Visor"), scaling=Decimal("1e-18")
    ),
    "0xf947b0824c3995787efc899017a36bc9f281265e": TokenInfo(
        currency=CurrencyInfo(symbol="LOTO", name="Lotoblock"), scaling=Decimal("1e-8")
    ),
    "0xf94b5c5651c888d928439ab6514b93944eee6f48": TokenInfo(
        currency=CurrencyInfo(symbol="YLD", name="YIELD App"), scaling=Decimal("1e-18")
    ),
    "0xf9520516c8e16fd500dff0c27916c81fadb67341": TokenInfo(
        currency=CurrencyInfo(symbol="DFP", name="Digital Fund Coin"), scaling=Decimal("1e-8")
    ),
    "0xf96459323030137703483b46fd59a71d712bf0aa": TokenInfo(
        currency=CurrencyInfo(symbol="XTK", name="XTAKE"), scaling=Decimal("1e-6")
    ),
    "0xf964e7dba960437ce4db92e2f712297a292c8006": TokenInfo(
        currency=CurrencyInfo(symbol="PBYI.CX", name="Puma Biotechnology Inc"), scaling=Decimal("1e-8")
    ),
    "0xf96aa656ec0e0ac163590db372b430cf3c0d61ca": TokenInfo(
        currency=CurrencyInfo(symbol="TGT", name="Twogap"), scaling=Decimal("1e-18")
    ),
    "0xf970b8e36e23f7fc3fd752eea86f8be8d83375a6": TokenInfo(
        currency=CurrencyInfo(symbol="RCN", name="Ripio Credit Network"), scaling=Decimal("1e-18")
    ),
    "0xf974b5f9ac9c6632fee8b76c61b0242ce69c839d": TokenInfo(
        currency=CurrencyInfo(symbol="ZYX", name="ZYX"), scaling=Decimal("1e-18")
    ),
    "0xf97b5d65da6b0468b90d531ddae2a69843e6797d": TokenInfo(
        currency=CurrencyInfo(symbol="LEO", name="LEOcoin"), scaling=Decimal("1e-18")
    ),
    "0xf9933cb5f0397bf020bb950c307e30dd8f62080f": TokenInfo(
        currency=CurrencyInfo(symbol="ZXTH", name="ZXTH"), scaling=Decimal("1e-18")
    ),
    "0xf9986d445ced31882377b5d6a5f58eaea72288c3": TokenInfo(
        currency=CurrencyInfo(symbol="ERD", name="Elrond"), scaling=Decimal("1e-18")
    ),
    "0xf99af7443fefa14e9d42ce935a575b8d1aac06b3": TokenInfo(
        currency=CurrencyInfo(symbol="DBK.CX", name="Deutsche Bank AG"), scaling=Decimal("1e-8")
    ),
    "0xf99d58e463a2e07e5692127302c20a191861b4d6": TokenInfo(
        currency=CurrencyInfo(symbol="ANY", name="Anyswap"), scaling=Decimal("1e-18")
    ),
    "0xf9c36c7ad7fa0f0862589c919830268d1a2581a1": TokenInfo(
        currency=CurrencyInfo(symbol="BOA", name="BOA"), scaling=Decimal("1e-18")
    ),
    "0xf9ccebced681780c6d9d35607edc61f77aa8ef7a": TokenInfo(
        currency=CurrencyInfo(symbol="WOLF", name="WolfWorld"), scaling=Decimal("1e-18")
    ),
    "0xf9d9702d031407f425a4412682fdc56b07d05262": TokenInfo(
        currency=CurrencyInfo(symbol="WOC", name="WallOfChain"), scaling=Decimal("1e-18")
    ),
    "0xf9e5af7b42d31d51677c75bbbd37c1986ec79aee": TokenInfo(
        currency=CurrencyInfo(symbol="QCX", name="QuickX Protocol"), scaling=Decimal("1e-8")
    ),
    "0xf9ed2f109a39eb0ac54e1cf5fee0216a2ae09183": TokenInfo(
        currency=CurrencyInfo(symbol="HMI.CX", name="Huami Corporation"), scaling=Decimal("1e-8")
    ),
    "0xf9f0fc7167c311dd2f1e21e9204f87eba9012fb2": TokenInfo(
        currency=CurrencyInfo(symbol="EHT", name="EasyHomes"), scaling=Decimal("1e-8")
    ),
    "0xf9f7c29cfdf19fcf1f2aa6b84aa367bcf1bd1676": TokenInfo(
        currency=CurrencyInfo(symbol="DTT", name="Delphi Technologies Token"), scaling=Decimal("1e-18")
    ),
    "0xf9fb4ad91812b704ba883b11d2b576e890a6730a": TokenInfo(
        currency=CurrencyInfo(symbol="AAMMWETH", name="Aave AMM WETH"), scaling=Decimal("1e-18")
    ),
    "0xfa05a73ffe78ef8f1a739473e462c54bae6567d9": TokenInfo(
        currency=CurrencyInfo(symbol="LUN", name="Lunyr"), scaling=Decimal("1e-18")
    ),
    "0xfa0ef5e034cae1ae752d59bdb8adcde37ed7ab97": TokenInfo(
        currency=CurrencyInfo(symbol="TCA", name="TangguoTao Token"), scaling=Decimal("1e-18")
    ),
    "0xfa1004e9c0063e59dbf965b9490f3153b87fb45f": TokenInfo(
        currency=CurrencyInfo(symbol="UZT", name="Uzone Token"), scaling=Decimal("1e-8")
    ),
    "0xfa12040497bc7b6077ea125bad27daa8b74e7edc": TokenInfo(
        currency=CurrencyInfo(symbol="WIS", name="Wish Coin"), scaling=Decimal("1e-18")
    ),
    "0xfa14fa6958401314851a17d6c5360ca29f74b57b": TokenInfo(
        currency=CurrencyInfo(symbol="SAITO", name="Saito"), scaling=Decimal("1e-18")
    ),
    "0xfa1a856cfa3409cfa145fa4e20eb270df3eb21ab": TokenInfo(
        currency=CurrencyInfo(symbol="IOST", name="IOSToken"), scaling=Decimal("1e-18")
    ),
    "0xfa1de2ee97e4c10c94c91cb2b5062b89fb140b82": TokenInfo(
        currency=CurrencyInfo(symbol="EDC", name="Education Credits"), scaling=Decimal("1e-6")
    ),
    "0xfa2aadaad9e258ea845426822bcf47488ce8420c": TokenInfo(
        currency=CurrencyInfo(symbol="NTES.CX", name="NetEase Inc"), scaling=Decimal("1e-8")
    ),
    "0xfa3118b34522580c35ae27f6cf52da1dbb756288": TokenInfo(
        currency=CurrencyInfo(symbol="LET", name="Linkeye"), scaling=Decimal("1e-6")
    ),
    "0xfa456cf55250a839088b27ee32a424d7dacb54ff": TokenInfo(
        currency=CurrencyInfo(symbol="BTT", name="Blocktrade"), scaling=Decimal("1e-18")
    ),
    "0xfa5047c9c78b8877af97bdcb85db743fd7313d4a": TokenInfo(
        currency=CurrencyInfo(symbol="ROOK", name="KeeperDAO"), scaling=Decimal("1e-18")
    ),
    "0xfa5e27893aee4805283d86e4283da64f8c72dd56": TokenInfo(
        currency=CurrencyInfo(symbol="APEUSD-UMA-DEC21", name="apeUSD-UMA Synthetic USD (Dec 2021)"),
        scaling=Decimal("1e-18"),
    ),
    "0xfa6de2697d59e88ed7fc4dfe5a33dac43565ea41": TokenInfo(
        currency=CurrencyInfo(symbol="DEFI5", name="DEFI Top 5 Index"), scaling=Decimal("1e-18")
    ),
    "0xfa75b65e52a6cbc5503f45f4abba2c5df4688875": TokenInfo(
        currency=CurrencyInfo(symbol="SET", name="Swytch"), scaling=Decimal("1e-18")
    ),
    "0xfa91f4177476633f100c59d336c0f2ffad414cba": TokenInfo(
        currency=CurrencyInfo(symbol="XYS", name="ANALYSX"), scaling=Decimal("1e-18")
    ),
    "0xfab46e002bbf0b4509813474841e0716e6730136": TokenInfo(
        currency=CurrencyInfo(symbol="FAU", name="FaucetToken"), scaling=Decimal("1e-18")
    ),
    "0xfab5a05c933f1a2463e334e011992e897d56ef0a": TokenInfo(
        currency=CurrencyInfo(symbol="DOTX", name="DeFi of Thrones"), scaling=Decimal("1e-18")
    ),
    "0xfaccd5fc83c3e4c3c1ac1ef35d15adf06bcf209c": TokenInfo(
        currency=CurrencyInfo(symbol="TBC2", name="TheBillionCoin2"), scaling=Decimal("1e-8")
    ),
    "0xfad45e47083e4607302aa43c65fb3106f1cd7607": TokenInfo(
        currency=CurrencyInfo(symbol="HOGE", name="Hoge Finance"), scaling=Decimal("1e-9")
    ),
    "0xfad572db566e5234ac9fc3d570c4edc0050eaa92": TokenInfo(
        currency=CurrencyInfo(symbol="BTH", name="Bytether"), scaling=Decimal("1e-18")
    ),
    "0xfade17a07ba3b480aa1714c3724a52d4c57d410e": TokenInfo(
        currency=CurrencyInfo(symbol="VEGAN", name="Vegan"), scaling=Decimal("1e-8")
    ),
    "0xfae4ee59cdd86e3be9e8b90b53aa866327d7c090": TokenInfo(
        currency=CurrencyInfo(symbol="CPC", name="CPChain"), scaling=Decimal("1e-18")
    ),
    "0xfb0aaa0432112779d9ac483d9d5e3961ece18eec": TokenInfo(
        currency=CurrencyInfo(symbol="USD-G", name="USD Gluwacoin"), scaling=Decimal("1e-18")
    ),
    "0xfb12e3cca983b9f59d90912fd17f8d745a8b2953": TokenInfo(
        currency=CurrencyInfo(symbol="LUCK", name="LUCKY"), scaling=Decimal("1e-0")
    ),
    "0xfb130d93e49dca13264344966a611dc79a456bc5": TokenInfo(
        currency=CurrencyInfo(symbol="DOGEGF", name="DogeGF"), scaling=Decimal("1e-18")
    ),
    "0xfb1534a824075c1e2aa4e914384d3e0a89f67d14": TokenInfo(
        currency=CurrencyInfo(symbol="FTCH.CX", name="Farfetch Ltd"), scaling=Decimal("1e-8")
    ),
    "0xfb1e5f5e984c28ad7e228cdaa1f8a0919bb6a09b": TokenInfo(
        currency=CurrencyInfo(symbol="GES", name="Galaxy eSolutions"), scaling=Decimal("1e-18")
    ),
    "0xfb2c4f8a6e30c3b8c97bc61050cafde5eeebb500": TokenInfo(
        currency=CurrencyInfo(symbol="IP.CX", name="International Paper"), scaling=Decimal("1e-8")
    ),
    "0xfb2f26f266fb2805a387230f2aa0a331b4d96fba": TokenInfo(
        currency=CurrencyInfo(symbol="EDGE", name="Edge"), scaling=Decimal("1e-18")
    ),
    "0xfb444c1f2b718ddfc385cb8fd9f2d1d776b24668": TokenInfo(
        currency=CurrencyInfo(symbol="ELAMA", name="Elamachain"), scaling=Decimal("1e-18")
    ),
    "0xfb5453340c03db5ade474b27e68b6a9c6b2823eb": TokenInfo(
        currency=CurrencyInfo(symbol="ROBOT", name="Robot"), scaling=Decimal("1e-18")
    ),
    "0xfb559ce67ff522ec0b9ba7f5dc9dc7ef6c139803": TokenInfo(
        currency=CurrencyInfo(symbol="PROB", name="Probit Token"), scaling=Decimal("1e-18")
    ),
    "0xfb5a551374b656c6e39787b1d3a03feab7f3a98e": TokenInfo(
        currency=CurrencyInfo(symbol="TOS", name="ThingsOperatingSystem"), scaling=Decimal("1e-18")
    ),
    "0xfb62ae373aca027177d1c18ee0862817f9080d08": TokenInfo(
        currency=CurrencyInfo(symbol="DPET", name="My DeFi Pet"), scaling=Decimal("1e-18")
    ),
    "0xfb6becd99282d7ca14d0890f3e4f073d9dd522e9": TokenInfo(
        currency=CurrencyInfo(symbol="BOA", name="Blockchain of Africa"), scaling=Decimal("1e-8")
    ),
    "0xfb7b4564402e5500db5bb6d63ae671302777c75a": TokenInfo(
        currency=CurrencyInfo(symbol="DEXT", name="DexTools"), scaling=Decimal("1e-18")
    ),
    "0xfb84176fe449b51661757d7c45d6ba8a9877bd5d": TokenInfo(
        currency=CurrencyInfo(symbol="UPC", name="Unimpeded Coin"), scaling=Decimal("1e-8")
    ),
    "0xfb8bf095ebcdad57d2e37573a505e7d3bafdd3cc": TokenInfo(
        currency=CurrencyInfo(symbol="DPN", name="Dipnet"), scaling=Decimal("1e-8")
    ),
    "0xfb9553afa2b5c19c5f8e5b8ee175fc01abd1555f": TokenInfo(
        currency=CurrencyInfo(symbol="HBC", name="Hybrid Bank Cash"), scaling=Decimal("1e-18")
    ),
    "0xfb9ec3111b7d68a8d80491cbf356dc4881e7e4f0": TokenInfo(
        currency=CurrencyInfo(symbol="ORCL.CX", name="Oracle"), scaling=Decimal("1e-8")
    ),
    "0xfb9fc4ccc2538172fe76f7dc231a6969950e57c8": TokenInfo(
        currency=CurrencyInfo(symbol="WEV", name="Weave DAO Token"), scaling=Decimal("1e-18")
    ),
    "0xfbb6b34dd77274a06ea2e5462a5e0b9e23ce478e": TokenInfo(
        currency=CurrencyInfo(symbol="APEUSD-UNI-DEC21", name="apeUSD-UNI Synthetic USD (Dec 2021)"),
        scaling=Decimal("1e-18"),
    ),
    "0xfbbe9b1142c699512545f47937ee6fae0e4b0aa9": TokenInfo(
        currency=CurrencyInfo(symbol="EDDA", name="EDDASwap"), scaling=Decimal("1e-18")
    ),
    "0xfbc1473e245b8afbba3b46116e0b01f91a026633": TokenInfo(
        currency=CurrencyInfo(symbol="CRU", name="Crypto Unit Token"), scaling=Decimal("1e-0")
    ),
    "0xfbccadbe483adfac499c82ac31d17965043f6174": TokenInfo(
        currency=CurrencyInfo(symbol="MIDDOOM", name="10X Short Midcap Index Token"), scaling=Decimal("1e-18")
    ),
    "0xfbcecb002177e530695b8976638fbd18d2038c3c": TokenInfo(
        currency=CurrencyInfo(symbol="BEFX", name="Belifex"), scaling=Decimal("1e-8")
    ),
    "0xfbcfd010d007d10d49f516bb738f4aed12880225": TokenInfo(
        currency=CurrencyInfo(symbol="WILD", name="WildLife"), scaling=Decimal("1e-18")
    ),
    "0xfbd0d1c77b501796a35d86cf91d65d9778eee695": TokenInfo(
        currency=CurrencyInfo(symbol="TWNKL", name="Rainbow Currency"), scaling=Decimal("1e-3")
    ),
    "0xfbd86312f156b0cc976e558b62da068bbafcaf9c": TokenInfo(
        currency=CurrencyInfo(symbol="ETHW", name="Ethereum wizard"), scaling=Decimal("1e-12")
    ),
    "0xfbdd194376de19a88118e84e279b977f165d01b8": TokenInfo(
        currency=CurrencyInfo(symbol="BTD", name="BTD"), scaling=Decimal("1e-18")
    ),
    "0xfbe878ced08132bd8396988671b450793c44bc12": TokenInfo(
        currency=CurrencyInfo(symbol="FOXT", name="Fox Trading Token"), scaling=Decimal("1e-18")
    ),
    "0xfbeea1c75e4c4465cb2fccc9c6d6afe984558e20": TokenInfo(
        currency=CurrencyInfo(symbol="DDIM", name="DuckDaoDime"), scaling=Decimal("1e-18")
    ),
    "0xfc05987bd2be489accf0f509e44b0145d68240f7": TokenInfo(
        currency=CurrencyInfo(symbol="ESS", name="Essentia"), scaling=Decimal("1e-18")
    ),
    "0xfc0d6cf33e38bce7ca7d89c0e292274031b7157a": TokenInfo(
        currency=CurrencyInfo(symbol="NTVRK", name="Netvrk"), scaling=Decimal("1e-18")
    ),
    "0xfc1e690f61efd961294b3e1ce3313fbd8aa4f85d": TokenInfo(
        currency=CurrencyInfo(symbol="ADAI", name="Aave DAI v1"), scaling=Decimal("1e-18")
    ),
    "0xfc29b6e626b67776675fff55d5bc0452d042f434": TokenInfo(
        currency=CurrencyInfo(symbol="BHT", name="BHEX Token"), scaling=Decimal("1e-18")
    ),
    "0xfc2c4d8f95002c14ed0a7aa65102cac9e5953b5e": TokenInfo(
        currency=CurrencyInfo(symbol="RBLX", name="Rublix"), scaling=Decimal("1e-18")
    ),
    "0xfc2f7ab5821e727a2efd120dae507c47b92fe055": TokenInfo(
        currency=CurrencyInfo(symbol="YEC", name="YEECORE"), scaling=Decimal("1e-8")
    ),
    "0xfc44ec51c80e35a87bc2140299b1636ec83dfb04": TokenInfo(
        currency=CurrencyInfo(symbol="ACDC", name="Volt"), scaling=Decimal("1e-18")
    ),
    "0xfc4b8ed459e00e5400be803a9bb3954234fd50e3": TokenInfo(
        currency=CurrencyInfo(symbol="AWBTC", name="Aave WBTC v1"), scaling=Decimal("1e-8")
    ),
    "0xfc4b9e2d71a7795102eb0c0e8b5da992946a62de": TokenInfo(
        currency=CurrencyInfo(symbol="CCT", name="Coupon Chain"), scaling=Decimal("1e-18")
    ),
    "0xfc5e03176b1eb31ac1ffab16431650b2e09bbb4c": TokenInfo(
        currency=CurrencyInfo(symbol="SMG.CX", name="The Scotts Miracle-Gro Company"), scaling=Decimal("1e-8")
    ),
    "0xfc64c0adf4a08008e3fa2bf9c03540032b1c8288": TokenInfo(
        currency=CurrencyInfo(symbol="g9tro", name="g9tro Crowdfunding Platform"), scaling=Decimal("1e-10")
    ),
    "0xfc82bb4ba86045af6f327323a46e80412b91b27d": TokenInfo(
        currency=CurrencyInfo(symbol="PROM", name="Prometeus"), scaling=Decimal("1e-18")
    ),
    "0xfc858154c0b2c4a3323046fb505811f110ebda57": TokenInfo(
        currency=CurrencyInfo(symbol="NOIA", name="NOIA Token"), scaling=Decimal("1e-18")
    ),
    "0xfc89f1b932079b462ef9c8757de5a28e387b847b": TokenInfo(
        currency=CurrencyInfo(
            symbol="REALTOKEN-18276-APPOLINE-ST-DETROIT-MI", name="RealToken 18276 Appoline St Detroit MI"
        ),
        scaling=Decimal("1e-18"),
    ),
    "0xfc979087305a826c2b2a0056cfaba50aad3e6439": TokenInfo(
        currency=CurrencyInfo(symbol="DAFI", name="Dafi Protocol"), scaling=Decimal("1e-18")
    ),
    "0xfca47962d45adfdfd1ab2d972315db4ce7ccf094": TokenInfo(
        currency=CurrencyInfo(symbol="IXT", name="iXledger"), scaling=Decimal("1e-8")
    ),
    "0xfca59cd816ab1ead66534d82bc21e7515ce441cf": TokenInfo(
        currency=CurrencyInfo(symbol="RARI", name="Rarible"), scaling=Decimal("1e-18")
    ),
    "0xfcac7a7515e9a9d7619fa77a1fa738111f66727e": TokenInfo(
        currency=CurrencyInfo(symbol="PCH", name="Pitch"), scaling=Decimal("1e-18")
    ),
    "0xfcce9526e030f1691966d5a651f5ebe1a5b4c8e4": TokenInfo(
        currency=CurrencyInfo(symbol="OSPV", name="Onyx S&P 500"), scaling=Decimal("1e-18")
    ),
    "0xfcd862985628b254061f7a918035b80340d045d3": TokenInfo(
        currency=CurrencyInfo(symbol="gif", name="GifCoin"), scaling=Decimal("1e-18")
    ),
    "0xfcdae8771f8d28e3b9027ab58f4a20749767a097": TokenInfo(
        currency=CurrencyInfo(symbol="SXR", name="SecureXR"), scaling=Decimal("1e-8")
    ),
    "0xfcf1d048fad53ff6afb801659cf8b7fa2468d170": TokenInfo(
        currency=CurrencyInfo(symbol="WDNA", name="WDNA"), scaling=Decimal("1e-18")
    ),
    "0xfcf8eda095e37a41e002e266daad7efc1579bc0a": TokenInfo(
        currency=CurrencyInfo(symbol="FLEX", name="FLEX Coin"), scaling=Decimal("1e-18")
    ),
    "0xfd0df7b58bd53d1dd4835ecd69a703b4b26f7816": TokenInfo(
        currency=CurrencyInfo(symbol="MZG", name="Moozicore"), scaling=Decimal("1e-18")
    ),
    "0xfd107b473ab90e8fbd89872144a3dc92c40fa8c9": TokenInfo(
        currency=CurrencyInfo(symbol="LALA", name="LALA World"), scaling=Decimal("1e-18")
    ),
    "0xfd1e80508f243e64ce234ea88a5fd2827c71d4b7": TokenInfo(
        currency=CurrencyInfo(symbol="MEDX", name="MediBlocX"), scaling=Decimal("1e-8")
    ),
    "0xfd25676fc2c4421778b18ec7ab86e7c5701df187": TokenInfo(
        currency=CurrencyInfo(symbol="ACOIN", name="Alchemy"), scaling=Decimal("1e-18")
    ),
    "0xfd3305e1c7cb5d269fb6ced8eb8240255a50e7a4": TokenInfo(
        currency=CurrencyInfo(symbol="CDB", name="Cloudbit Token"), scaling=Decimal("1e-8")
    ),
    "0xfd3e213eb8d3d01ff737010eb2ad18a205a1b5ad": TokenInfo(
        currency=CurrencyInfo(symbol="IRBT.CX", name="iRobot Corporation"), scaling=Decimal("1e-8")
    ),
    "0xfd45e61e085b3e7a1990a47828d757755b206eee": TokenInfo(
        currency=CurrencyInfo(symbol="CP", name="CoinPark Token"), scaling=Decimal("1e-18")
    ),
    "0xfd62247943f94c3910a4922af2c62c2d3fac2a8f": TokenInfo(
        currency=CurrencyInfo(symbol="BTE", name="BTEcoin"), scaling=Decimal("1e-18")
    ),
    "0xfd66c6771d00b5646949086152b7ccdca25e5686": TokenInfo(
        currency=CurrencyInfo(symbol="KAYA", name="LATTICE80 KAYA Token"), scaling=Decimal("1e-18")
    ),
    "0xfd8971d5e8e1740ce2d0a84095fca4de729d0c16": TokenInfo(
        currency=CurrencyInfo(symbol="ZLA", name="Zilla"), scaling=Decimal("1e-18")
    ),
    "0xfda1f5278b9aa923b5e581565d599810c78c71f5": TokenInfo(
        currency=CurrencyInfo(symbol="KSG", name="KING'S GLOBAL TOKEN"), scaling=Decimal("1e-18")
    ),
    "0xfdb29741f239a2406ae287913ef12415160378d3": TokenInfo(
        currency=CurrencyInfo(symbol="OS", name="EthOS"), scaling=Decimal("1e-18")
    ),
    "0xfdbc1adc26f0f8f8606a5d63b7d3a3cd21c22b23": TokenInfo(
        currency=CurrencyInfo(symbol="1WO", name="1World"), scaling=Decimal("1e-8")
    ),
    "0xfdc3d57eb7839ca68a2fad7a93799c8e8afa61b7": TokenInfo(
        currency=CurrencyInfo(symbol="ALGOHEDGE", name="1X Short Algorand Token"), scaling=Decimal("1e-18")
    ),
    "0xfdcc07ab60660de533b5ad26e1457b565a9d59bd": TokenInfo(
        currency=CurrencyInfo(symbol="MART", name="Martcoin"), scaling=Decimal("1e-18")
    ),
    "0xfdccb100ecb130377c70c17c15c8a2fa5b61b18e": TokenInfo(
        currency=CurrencyInfo(symbol="WB.CX", name="Weibo Corporation"), scaling=Decimal("1e-8")
    ),
    "0xfdeaa4ab9fea519afd74df2257a21e5bca0dfd3f": TokenInfo(
        currency=CurrencyInfo(symbol="BCAT", name="BCAT"), scaling=Decimal("1e-18")
    ),
    "0xfdfe8b7ab6cf1bd1e3d14538ef40686296c42052": TokenInfo(
        currency=CurrencyInfo(symbol="SKRP", name="Skraps"), scaling=Decimal("1e-18")
    ),
    "0xfe16a9e3904f928cc6a34507d6d667f731c66bb0": TokenInfo(
        currency=CurrencyInfo(symbol="EDBT", name="Easy Deals"), scaling=Decimal("1e-8")
    ),
    "0xfe18be6b3bd88a2d2a7f928d00292e7a9963cfc6": TokenInfo(
        currency=CurrencyInfo(symbol="SBTC", name="sBTC"), scaling=Decimal("1e-18")
    ),
    "0xfe2786d7d1ccab8b015f6ef7392f67d778f8d8d7": TokenInfo(
        currency=CurrencyInfo(symbol="PRQ", name="Parsiq Token"), scaling=Decimal("1e-18")
    ),
    "0xfe2e637202056d30016725477c5da089ab0a043a": TokenInfo(
        currency=CurrencyInfo(symbol="SETH2", name="sETH2"), scaling=Decimal("1e-18")
    ),
    "0xfe33ae95a9f0da8a845af33516edc240dcd711d6": TokenInfo(
        currency=CurrencyInfo(symbol="SDASH", name="sDASH"), scaling=Decimal("1e-18")
    ),
    "0xfe39e6a32acd2af7955cb3d406ba2b55c901f247": TokenInfo(
        currency=CurrencyInfo(symbol="ZT", name="ZBG Token"), scaling=Decimal("1e-18")
    ),
    "0xfe3a06a947a036eff9f9e8ec25b385ff4e853c38": TokenInfo(
        currency=CurrencyInfo(symbol="TUT", name="Trust Union"), scaling=Decimal("1e-18")
    ),
    "0xfe3a103054e73dce81673ebd6c5b3740ac2b8b40": TokenInfo(
        currency=CurrencyInfo(symbol="OHL.CX", name="Obrascón Huarte Lain S.A."), scaling=Decimal("1e-8")
    ),
    "0xfe3e6a25e6b192a42a44ecddcd13796471735acf": TokenInfo(
        currency=CurrencyInfo(symbol="REEF", name="Reef Finance"), scaling=Decimal("1e-18")
    ),
    "0xfe5d908c9ad85f651185daa6a4770726e2b27d09": TokenInfo(
        currency=CurrencyInfo(symbol="BHR", name="BETHER"), scaling=Decimal("1e-18")
    ),
    "0xfe5f141bf94fe84bc28ded0ab966c16b17490657": TokenInfo(
        currency=CurrencyInfo(symbol="LBA", name="LibraToken"), scaling=Decimal("1e-18")
    ),
    "0xfe69bc0920fb63c5924cfc322dc4a5cc23d9afed": TokenInfo(
        currency=CurrencyInfo(symbol="LZE", name="LYZE"), scaling=Decimal("1e-18")
    ),
    "0xfe76be9cec465ed3219a9972c21655d57d21aec6": TokenInfo(
        currency=CurrencyInfo(symbol="PTN", name="PalletOneToken"), scaling=Decimal("1e-18")
    ),
    "0xfe7b915a0baa0e79f85c5553266513f7c1c03ed0": TokenInfo(
        currency=CurrencyInfo(symbol="THUG", name="THUG LIFE Coin"), scaling=Decimal("1e-18")
    ),
    "0xfe831929098b5ff5d736105bd68ba9460ef07207": TokenInfo(
        currency=CurrencyInfo(symbol="CYCLE", name="Cycle"), scaling=Decimal("1e-18")
    ),
    "0xfe9a29ab92522d14fc65880d817214261d8479ae": TokenInfo(
        currency=CurrencyInfo(symbol="SNOW", name="Snowswap"), scaling=Decimal("1e-18")
    ),
    "0xfec0cf7fe078a500abf15f1284958f22049c2c7e": TokenInfo(
        currency=CurrencyInfo(symbol="ART", name="Maecenas"), scaling=Decimal("1e-18")
    ),
    "0xfedae5642668f8636a11987ff386bfd215f942ee": TokenInfo(
        currency=CurrencyInfo(symbol="PAL", name="PAL Network"), scaling=Decimal("1e-18")
    ),
    "0xfee2fa52de307316d9d47ffe3781d4cba2c4f6fd": TokenInfo(
        currency=CurrencyInfo(symbol="ARC", name="Arthur Chain"), scaling=Decimal("1e-18")
    ),
    "0xfee4dbe2751bf8d1b1b861aaf9664961f19ce91a": TokenInfo(
        currency=CurrencyInfo(symbol="QDEFI", name="Q DeFi Rating & Governance Token v2.0"), scaling=Decimal("1e-18")
    ),
    "0xfeea0bdd3d07eb6fe305938878c0cadbfa169042": TokenInfo(
        currency=CurrencyInfo(symbol="8PAY", name="8PAY"), scaling=Decimal("1e-18")
    ),
    "0xfef3884b603c33ef8ed4183346e093a173c94da6": TokenInfo(
        currency=CurrencyInfo(symbol="METM", name="MetaMorph"), scaling=Decimal("1e-18")
    ),
    "0xfef3bef71a5eb97e097039038776fd967ae5b106": TokenInfo(
        currency=CurrencyInfo(symbol="YFMS", name="YFMoonshot"), scaling=Decimal("1e-18")
    ),
    "0xfef4185594457050cc9c23980d301908fe057bb1": TokenInfo(
        currency=CurrencyInfo(symbol="VIDT", name="VIDT Datalink"), scaling=Decimal("1e-18")
    ),
    "0xff0e5e014cf97e0615cb50f6f39da6388e2fae6e": TokenInfo(
        currency=CurrencyInfo(symbol="OGO", name="Origo"), scaling=Decimal("1e-18")
    ),
    "0xff18dbc487b4c2e3222d115952babfda8ba52f5f": TokenInfo(
        currency=CurrencyInfo(symbol="LIFE", name="LIFE"), scaling=Decimal("1e-18")
    ),
    "0xff19138b039d938db46bdda0067dc4ba132ec71c": TokenInfo(
        currency=CurrencyInfo(symbol="SNET", name="Snetwork"), scaling=Decimal("1e-8")
    ),
    "0xff19a86c938acdf34f4fc6f5a8567106647c7a8f": TokenInfo(
        currency=CurrencyInfo(symbol="BANK", name="Abele Trust"), scaling=Decimal("1e-0")
    ),
    "0xff20817765cb7f73d4bde2e66e067e58d11095c2": TokenInfo(
        currency=CurrencyInfo(symbol="AMP", name="Amp"), scaling=Decimal("1e-18")
    ),
    "0xff2b3353c3015e9f1fbf95b9bda23f58aa7ce007": TokenInfo(
        currency=CurrencyInfo(symbol="BITX", name="BitScreener"), scaling=Decimal("1e-18")
    ),
    "0xff340f03e226b669c873516755a6b88a45b0b2ac": TokenInfo(
        currency=CurrencyInfo(symbol="NSRT", name="New Silk Road BRICS Token"), scaling=Decimal("1e-18")
    ),
    "0xff362c6a335e373633f1677540aac6917208dc0d": TokenInfo(
        currency=CurrencyInfo(symbol="DFC", name="DeFiCoin"), scaling=Decimal("1e-8")
    ),
    "0xff3ab23b0e08bb2d575aa00909ceb478607e2f32": TokenInfo(
        currency=CurrencyInfo(symbol="YELP.CX", name="Yelp"), scaling=Decimal("1e-8")
    ),
    "0xff40858a83396f9ef76608d3ea3db812c7830a48": TokenInfo(
        currency=CurrencyInfo(symbol="WFC.CX", name="Wells Fargo & Co"), scaling=Decimal("1e-8")
    ),
    "0xff44b5719f0b77a9951636fc5e69d3a1fc9e7d73": TokenInfo(
        currency=CurrencyInfo(symbol="4ART", name="4ART Coin"), scaling=Decimal("1e-18")
    ),
    "0xff44b937788215eca197baaf9af69dbdc214aa04": TokenInfo(
        currency=CurrencyInfo(symbol="ROCKI", name="Rocki"), scaling=Decimal("1e-18")
    ),
    "0xff56cc6b1e6ded347aa0b7676c85ab0b3d08b0fa": TokenInfo(
        currency=CurrencyInfo(symbol="ORBS", name="Orbs"), scaling=Decimal("1e-18")
    ),
    "0xff5c25d2f40b47c4a37f989de933e26562ef0ac0": TokenInfo(
        currency=CurrencyInfo(symbol="KNT", name="Kora Network"), scaling=Decimal("1e-16")
    ),
    "0xff603f43946a3a28df5e6a73172555d8c8b02386": TokenInfo(
        currency=CurrencyInfo(symbol="RNT", name="OneRoot Network"), scaling=Decimal("1e-18")
    ),
    "0xff742d05420b6aca4481f635ad8341f81a6300c2": TokenInfo(
        currency=CurrencyInfo(symbol="ASD", name="AscendEx Token"), scaling=Decimal("1e-18")
    ),
    "0xff75ced57419bcaebe5f05254983b013b0646ef5": TokenInfo(
        currency=CurrencyInfo(symbol="COOK", name="Cook"), scaling=Decimal("1e-18")
    ),
    "0xff8998b32a2b3da59de78518086ea4431b30a2c6": TokenInfo(
        currency=CurrencyInfo(symbol="BVES", name="Behavior Value Ecosystem"), scaling=Decimal("1e-8")
    ),
    "0xff8be4b22cedc440591dcb1e641eb2a0dd9d25a5": TokenInfo(
        currency=CurrencyInfo(symbol="URAC", name="Uranus"), scaling=Decimal("1e-18")
    ),
    "0xff98a08c143311719ca492e4b8c950c940f26872": TokenInfo(
        currency=CurrencyInfo(symbol="JEX", name="Jex Token"), scaling=Decimal("1e-4")
    ),
    "0xffa93aacf49297d51e211817452839052fdfb961": TokenInfo(
        currency=CurrencyInfo(symbol="DCC", name="Distributed Credit Chain"), scaling=Decimal("1e-18")
    ),
    "0xffaa5ffc455d9131f8a2713a741fd1960330508b": TokenInfo(
        currency=CurrencyInfo(symbol="QRG", name="QRG"), scaling=Decimal("1e-18")
    ),
    "0xffb5531e6a916d228958016441146299ab5eddd0": TokenInfo(
        currency=CurrencyInfo(symbol="ZAY", name="Zayka Token"), scaling=Decimal("1e-18")
    ),
    "0xffc63b9146967a1ba33066fb057ee3722221acf0": TokenInfo(
        currency=CurrencyInfo(symbol="A", name="Alpha Token"), scaling=Decimal("1e-18")
    ),
    "0xffc97d72e13e01096502cb8eb52dee56f74dad7b": TokenInfo(
        currency=CurrencyInfo(symbol="AAAVE", name="Aave AAVE"), scaling=Decimal("1e-18")
    ),
    "0xffe02ee4c69edf1b340fcad64fbd6b37a7b9e265": TokenInfo(
        currency=CurrencyInfo(symbol="NANJ", name="NANJCOIN"), scaling=Decimal("1e-8")
    ),
    "0xffe510a92434a0df346c5e72a3494b043cf249eb": TokenInfo(
        currency=CurrencyInfo(symbol="LBXC", name="LUX BIO EXCHANGE COIN"), scaling=Decimal("1e-18")
    ),
    "0xffe8196bc259e8dedc544d935786aa4709ec3e64": TokenInfo(
        currency=CurrencyInfo(symbol="HDG", name="Hedge"), scaling=Decimal("1e-18")
    ),
    "0xfff3ada5a2555a2b59bff4f44dfad90146cce8cb": TokenInfo(
        currency=CurrencyInfo(symbol="DXR", name="DEXTER"), scaling=Decimal("1e-18")
    ),
    "0xffffffff2ba8f66d4e51811c5190992176930278": TokenInfo(
        currency=CurrencyInfo(symbol="COMBO", name="Furucombo"), scaling=Decimal("1e-18")
    ),
    "0xfffffffff15abf397da76f1dcc1a1604f45126db": TokenInfo(
        currency=CurrencyInfo(symbol="FSW", name="Falconswap"), scaling=Decimal("1e-18")
    ),
}