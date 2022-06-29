GET_TRANSACTION_QUERY = """
    SELECT
        tx_out.address AS address,
        tx_out.value AS amount,
        NULL AS transaction_pointer_hash,
        NULL::int AS transaction_pointer_index,
        'txout' AS type
    FROM tx_out
    LEFT JOIN tx ON tx_out.tx_id = tx.id
    WHERE tx.hash = decode($1, 'hex')
    UNION
    SELECT
        stake_address.view AS address,
        withdrawal.amount AS amount,
        NULL AS transaction_pointer_hash,
        NULL::int AS transaction_pointer_index,
        'withdrawal' AS type
    FROM withdrawal
    LEFT JOIN stake_address ON withdrawal.addr_id = stake_address.id
    LEFT JOIN tx ON tx.id = withdrawal.tx_id
    WHERE tx.hash = decode($1, 'hex')
    UNION
    SELECT
        tx_out.address AS address,
        tx_out.value AS amount,
        encode(tx.hash, 'hex') AS transaction_pointer_hash,
        tx_in.tx_out_index::int AS transaction_pointer_index,
        'txin' AS type
    FROM tx_out
    LEFT JOIN tx_in ON tx_out.tx_id = tx_in.tx_out_id AND tx_out.index = tx_in.tx_out_index
    LEFT JOIN tx ON tx_out.tx_id = tx.id
    WHERE tx_in.tx_in_id = (SELECT tx.id FROM tx WHERE tx.hash = decode($1, 'hex'))

"""

GET_BLOCK_BY_HASH_QUERY = """
    SELECT 
        block.id AS id,
        encode(block.hash, 'hex') AS hash,  
        block.block_no AS height, 
        extract(epoch from block.time) * 1000 AS timestamp_ms
    FROM block 
    WHERE block.hash = decode($1, 'hex')
"""

GET_BLOCK_BY_HEIGHT_QUERY = """
    SELECT 
        block.id AS id,
        encode(block.hash, 'hex') AS hash, 
        block.block_no AS height, 
        extract(epoch from block.time) * 1000 AS timestamp_ms
    FROM block 
    WHERE block.block_no = $1
"""
GET_LIST_OF_TRANSACTION_QUERY = """
    SELECT 
        encode(tx.hash, 'hex') AS hash 
    FROM tx 
    WHERE tx.block_id = $1
"""

GET_BLOCK_COUNT_QUERY = """
    SELECT 
        block.block_no AS block_count
    FROM block 
    WHERE block.block_no IS NOT NULL
    ORDER BY block.block_no DESC
    LIMIT 1
"""
